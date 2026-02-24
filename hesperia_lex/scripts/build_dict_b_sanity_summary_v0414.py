#!/usr/bin/env python3
"""Emit one minimal sanity summary for Dict B (B1) freeze: counts + top 10 area/family.
Prevents future 'it built but it is garbage' situations.
Token set = Dict A keys | B0 keys | token_to_side keys (when present).
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

# Resolve repo root from script location
REPO_ROOT = Path(__file__).resolve().parent.parent.parent
ASSETS = REPO_ROOT / "assets"
FROZEN = REPO_ROOT / "hesperia_lex" / "frozen"
CURATED = REPO_ROOT / "hesperia_lex" / "curated"
OUT_FILE = REPO_ROOT / "assets" / "v0414" / "DICT_B_SANITY_SUMMARY_V0414.txt"
FAMILIES_PER_AREA = 24
# Full taxonomy surface: 12×24×250×6 (sphere_rag.invariant_catalog.TOTAL_SIDES)
TOTAL_SIDES_EXPECTED = 432_000


def load_dict_a() -> dict:
    # Prefer frozen; else curated; else assets (attribution_v033 default)
    candidates = []
    for base in (FROZEN, CURATED, ASSETS):
        for name in ("A_CORE_STAR_MAP_v0_4_1_1.json", "A_CORE_STAR_MAP_v0_4_1_3.json", "A_CORE_STAR_MAP_v1.json"):
            candidates.append(base / name)
    path = next((p for p in candidates if p.exists()), None)
    if path is None:
        return {}
    data = json.loads(path.read_text(encoding="utf-8"))
    out = {}
    for k, v in data.items():
        if k.startswith("_") or v is None:
            continue
        if isinstance(v, dict) and "familyGlobal" in v:
            fg = int(v["familyGlobal"])
            if 0 <= fg < 288:
                out[k.strip().lower()] = {"familyGlobal": fg}
        elif isinstance(v, list) and len(v) > 0:
            e = v[0]
            if isinstance(e, dict):
                sid = e.get("side_id")
                if sid is not None:
                    try:
                        fg = int(sid) // 1500  # SIDES_PER_FAMILY
                        if 0 <= fg < 288:
                            out[k.strip().lower()] = {"familyGlobal": fg}
                    except (TypeError, ValueError):
                        pass
    return out


def load_b0() -> dict[str, int]:
    for name in ("B0_TOKEN_TO_FAMILY_v0_4_1_4_from_A_v0_4_1_3.json", "dict_b_v040_from_a_v0413.json"):
        p = FROZEN / name
        if p.exists():
            data = json.loads(p.read_text(encoding="utf-8"))
            if isinstance(data, dict):
                return {str(k).strip().lower(): int(v) for k, v in data.items() if isinstance(k, str)}
    return {}


def load_b1() -> dict[str, int]:
    p = FROZEN / "B1_SIDE_TO_FAMILY_v0_4_1_4.json"
    if not p.exists():
        return {}
    data = json.loads(p.read_text(encoding="utf-8"))
    if isinstance(data, dict):
        return {str(k): int(v) for k, v in data.items() if isinstance(k, str)}
    return {}


def load_token_to_side() -> dict[str, int]:
    p = ASSETS / "token_to_side_id_v040.json"
    if not p.exists():
        return {}
    data = json.loads(p.read_text(encoding="utf-8"))
    if isinstance(data, dict):
        return {str(k).strip().lower(): int(v) for k, v in data.items() if isinstance(k, str)}
    return {}


def explain(token: str, dict_a: dict, b0: dict[str, int], b1: dict[str, int], token_to_side: dict[str, int]) -> tuple[str, int | None]:
    """Return (landing_source, familyGlobal)."""
    t = token.strip().lower()
    if t in dict_a:
        return "A", int(dict_a[t].get("familyGlobal", -1))
    if b1 and token_to_side and t in token_to_side:
        side_id = int(token_to_side[t])
        fg = b1.get(str(side_id))
        if fg is not None:
            return "B1", int(fg)
    if t in b0:
        return "B0", int(b0[t])
    return "NONE", None


def main() -> int:
    dict_a = load_dict_a()
    b0 = load_b0()
    b1 = load_b1()
    token_to_side = load_token_to_side()

    tokens = sorted(set(dict_a.keys()) | set(b0.keys()) | set(token_to_side.keys()))
    total = len(tokens)

    a_hit = b0_hit = b1_hit = skipped = collisions = 0
    family_counts: dict[int, int] = {}
    area_counts: dict[int, int] = {}

    for t in tokens:
        source, fg = explain(t, dict_a, b0, b1, token_to_side)
        if source == "A":
            a_hit += 1
        elif source == "B0":
            b0_hit += 1
        elif source == "B1":
            b1_hit += 1
        else:
            skipped += 1

        # Collision: token in both dict_a and (b0 or b1) with different family (we already resolved A wins, so no cross-source collision; collision = same token would map to different family if we used B instead of A — i.e. token in A and in B with A[family] != B[family])
        if fg is not None and 0 <= fg < 288:
            family_counts[fg] = family_counts.get(fg, 0) + 1
            area = fg // FAMILIES_PER_AREA
            area_counts[area] = area_counts.get(area, 0) + 1

    # Collision: token in dict_a and in b0/b1 with different family
    for t in tokens:
        in_a = t in dict_a
        in_b0 = t in b0
        in_b1 = token_to_side and t in token_to_side and b1.get(str(token_to_side[t])) is not None
        if in_a and (in_b0 or in_b1):
            fa = int(dict_a[t].get("familyGlobal", -1))
            fb = int(b0[t]) if in_b0 else int(b1.get(str(token_to_side[t]), -1))
            if fa != fb:
                collisions += 1

    top10_family = sorted(family_counts.items(), key=lambda x: -x[1])[:10]
    top10_area = sorted(area_counts.items(), key=lambda x: -x[1])[:10]

    # B1 participates in runtime attribution only when token→side mapping exists and is used
    b1_runtime_enabled = bool(token_to_side and b1)
    b1_side_count = len(b1)
    coverage_ratio = b1_side_count / TOTAL_SIDES_EXPECTED if TOTAL_SIDES_EXPECTED else 0.0

    lines = [
        "HESPERIA Dict B v0.4.1.4 — sanity summary (prevents 'built but garbage')",
        "",
        "topology_truth:",
        "  topology: sparse semantic activation layer (selective anchor mesh); not full geometric surface.",
        "  claim_whole_sphere: false",
        "",
        "runtime:",
        f"  b1_runtime_enabled: {str(b1_runtime_enabled).lower()}",
        "",
        "surface_coverage:",
        f"  side_count_meaning: surface subset produced by v0.4.0 embedding pass (sides with at least one placed token or role)",
        f"  b1_side_count: {b1_side_count}",
        f"  total_sides_expected: {TOTAL_SIDES_EXPECTED}",
        f"  coverage_ratio: {b1_side_count}/{TOTAL_SIDES_EXPECTED} = {coverage_ratio:.6f}",
        "",
        "counts:",
        f"  total_tokens_considered: {total}",
        f"  mapped_a_hit: {a_hit}",
        f"  mapped_b0_hit: {b0_hit}",
        f"  mapped_b1_hit: {b1_hit}",
        f"  skipped_unknown: {skipped}",
        f"  collisions: {collisions}",
        "",
        "per_family_top10: (familyGlobal count)",
    ]
    for fg, cnt in top10_family:
        lines.append(f"  {fg} {cnt}")
    lines.append("")
    lines.append("per_area_top10: (area count)")
    for area, cnt in top10_area:
        lines.append(f"  {area} {cnt}")

    OUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    OUT_FILE.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"wrote {OUT_FILE}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
