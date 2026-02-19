from __future__ import annotations

import hashlib
import re
from dataclasses import dataclass
from pathlib import Path

from .geometry import (
    AREAS,
    FAMILIES_PER_AREA,
    HEXES_PER_FAMILY,
    SIDES_PER_HEX,
    TOTAL_FAMILIES,
    side_id_from_coord,
)


CANONICAL_AREAS = [
    "GOOD",
    "HARM",
    "TRUTH",
    "DECEIT",
    "ORDER",
    "CHAOS",
    "FREEDOM",
    "CONTROL",
    "CARE",
    "INDIFFERENCE",
    "CREATION",
    "DESTRUCTION",
]


@dataclass(frozen=True, slots=True)
class KeywordHit:
    keyword: str
    area_id: int
    family_global: int
    score: float  # [0,1]


@dataclass(frozen=True, slots=True)
class SeedSide:
    side_id: int
    tau: float  # [0,1]
    provenance_weight: float  # >= 0

    @property
    def w(self) -> float:
        return self.tau * self.provenance_weight


@dataclass(frozen=True, slots=True)
class SeedResult:
    keywords: list[str]
    hits: list[KeywordHit]
    seed_sides: list[SeedSide]
    area_activation: list[float]  # length 12, unnormalized mass
    family_activation: list[float]  # length 288, unnormalized mass
    start_area_id: int
    start_family_global: int


_WS_RE = re.compile(r"\s+")
_NON_ALNUM_RE = re.compile(r"[^a-z0-9]+")


def _norm(s: str) -> str:
    s = s.strip().lower()
    s = _WS_RE.sub(" ", s)
    return s


def _tokens(s: str) -> set[str]:
    s = _norm(s)
    s = _NON_ALNUM_RE.sub(" ", s)
    return {t for t in s.split() if t}


def _stable_u32(text: str) -> int:
    h = hashlib.sha256(text.encode("utf-8")).digest()
    return int.from_bytes(h[:4], "big", signed=False)


def load_families_table(path: str | Path) -> list[tuple[int, str, str]]:
    """Returns list of (family_global_0based, area_name, family_name), sorted by family_global."""
    p = Path(path)
    if not p.is_file():
        raise FileNotFoundError(f"families table not found: {p}")
    rows: list[tuple[int, str, str]] = []
    with p.open("r", encoding="utf-8", errors="replace") as f:
        header = True
        for line in f:
            if header:
                header = False
                continue
            line = line.strip()
            if not line:
                continue
            parts = line.split("\t")
            if len(parts) < 3:
                continue
            try:
                num_1based = int(parts[0].strip())
            except ValueError:
                continue
            area = parts[1].strip()
            fam = parts[2].strip()
            if not area or not fam:
                continue
            family_global = num_1based - 1
            if 0 <= family_global < TOTAL_FAMILIES:
                rows.append((family_global, area, fam))
    rows.sort(key=lambda x: x[0])
    return rows


def _best_family_for_keyword(
    keyword: str,
    families: list[tuple[int, str, str]],
) -> tuple[int, int, float]:
    """Returns (area_id, family_global, score). Deterministic."""
    kw = _norm(keyword)
    kw_toks = _tokens(keyword)
    if not kw:
        fam = 0
        return 0, fam, 0.0

    # Exact area match
    for area_id, area_name in enumerate(CANONICAL_AREAS):
        if kw == area_name.lower():
            fam = area_id * FAMILIES_PER_AREA
            return area_id, fam, 0.9

    # Family name matching
    best: tuple[float, int, int] | None = None  # (score, family_global, area_id)
    for family_global, area_name, family_name in families:
        name_n = _norm(family_name)
        if kw == name_n:
            area_id = CANONICAL_AREAS.index(area_name) if area_name in CANONICAL_AREAS else family_global // FAMILIES_PER_AREA
            return area_id, family_global, 1.0
        name_toks = _tokens(family_name)
        inter = len(kw_toks & name_toks)
        if inter == 0:
            # substring match on normalized
            if kw in name_n and len(kw) >= 4:
                score = 0.7
            else:
                continue
        else:
            score = inter / max(1, len(kw_toks))
            score = 0.6 + 0.4 * min(1.0, score)  # map to [0.6,1.0]
        area_id = CANONICAL_AREAS.index(area_name) if area_name in CANONICAL_AREAS else family_global // FAMILIES_PER_AREA
        key = (score, -family_global, -area_id)  # prefer higher score, then lower family_global, then lower area_id
        if best is None or key > (best[0], -best[1], -best[2]):
            best = (score, family_global, area_id)
    if best is not None:
        score, family_global, area_id = best
        return area_id, family_global, float(score)

    # Fallback: hashed family
    u = _stable_u32(kw)
    family_global = u % TOTAL_FAMILIES
    area_id = family_global // FAMILIES_PER_AREA
    return area_id, family_global, 0.2


def keywords_to_seed(
    keywords: list[str],
    *,
    families_table_path: str | Path = "31_FAMILIES__area_family_table_full.txt",
    provenance_weight: float = 1.0,
) -> SeedResult:
    families = load_families_table(families_table_path)
    area_activation = [0.0 for _ in range(AREAS)]
    family_activation = [0.0 for _ in range(TOTAL_FAMILIES)]
    hits: list[KeywordHit] = []
    seed_sides: list[SeedSide] = []

    for kw in keywords:
        area_id, family_global, score = _best_family_for_keyword(kw, families)
        hits.append(KeywordHit(keyword=kw, area_id=area_id, family_global=family_global, score=score))

        family_local = family_global % FAMILIES_PER_AREA
        # Spread within family deterministically per keyword.
        hex_index = _stable_u32(f"{kw}|hex") % HEXES_PER_FAMILY
        side_index = _stable_u32(f"{kw}|side") % SIDES_PER_HEX
        side_id = side_id_from_coord(area_id, family_local, hex_index, side_index)

        tau = max(0.0, min(1.0, score))
        seed_sides.append(SeedSide(side_id=side_id, tau=tau, provenance_weight=max(0.0, provenance_weight)))
        area_activation[area_id] += tau
        family_activation[family_global] += tau

    # Deterministic start point: argmax area_activation, ties -> lowest area_id.
    start_area_id = max(range(AREAS), key=lambda i: (area_activation[i], -i))
    start_family_global = max(
        range(TOTAL_FAMILIES),
        key=lambda f: (
            family_activation[f] if (f // FAMILIES_PER_AREA) == start_area_id else -1.0,
            -f,
        ),
    )

    # Stabilize ordering for output determinism.
    hits_sorted = sorted(hits, key=lambda h: (_norm(h.keyword), h.family_global, h.area_id))
    seed_sides_sorted = sorted(seed_sides, key=lambda s: (s.side_id, -s.tau))

    return SeedResult(
        keywords=list(keywords),
        hits=hits_sorted,
        seed_sides=seed_sides_sorted,
        area_activation=area_activation,
        family_activation=family_activation,
        start_area_id=start_area_id,
        start_family_global=start_family_global,
    )
