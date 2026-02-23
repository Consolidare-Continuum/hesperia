"""Validate families.yaml (v0.4.1.3) with semantic integrity checks and audit report."""
from __future__ import annotations

from collections import Counter, defaultdict
from pathlib import Path
import re
import unicodedata
from typing import Any

REPO_ROOT = Path(__file__).resolve().parent.parent.parent.parent
TABLE_PATH = REPO_ROOT / "31_FAMILIES__area_family_table_full.txt"
AUDIT_REPORT_PATH = REPO_ROOT / "assets" / "v0413" / "families_semantic_audit_report.txt"

AREA_ORDER = [
    "GOOD", "HARM", "TRUTH", "DECEIT", "ORDER", "CHAOS",
    "FREEDOM", "CONTROL", "CARE", "INDIFFERENCE", "CREATION", "DESTRUCTION",
]

TEMPLATE_PHRASES = [
    "domain concerning",
    "structural role within the taxonomy",
    "promotes or instantiates",
    "structural opposite or absence",
]

MECHANISM_WORDS = {
    "protects", "repairs", "shares", "verifies", "documents",
    "deceives", "extracts", "coerces", "measures", "audits",
    "permits", "blocks", "governs", "creates", "removes",
}

BANNED_TOKENS = {"thing", "stuff", "good", "bad", "nice", "mean", "help"}
AREA_TOKEN_EXCEPTIONS = {
    "truth": {3},
    "harm": {2},
}


def _slug(s: str) -> str:
    s = unicodedata.normalize("NFKC", s).lower()
    return re.sub(r"[^a-z0-9]+", "_", s).strip("_")


def _norm_token(s: str) -> str:
    s = unicodedata.normalize("NFKC", s).lower()
    s = re.sub(r"[^a-z0-9]+", "", s)
    return s


def load_canonical_table(table_path: Path | None = None) -> dict[int, tuple[int, str]]:
    path = table_path or TABLE_PATH
    if not path.exists():
        return {}
    out: dict[int, tuple[int, str]] = {}
    area_to_id = {a: i + 1 for i, a in enumerate(AREA_ORDER)}
    for line in path.read_text(encoding="utf-8").splitlines()[1:]:
        if not line.strip():
            continue
        num, area_name, label = line.split("\t")[:3]
        out[int(num)] = (area_to_id[area_name.strip()], label.strip())
    return out


def validate_families_yaml(
    data: dict[str, Any],
    canonical: dict[int, tuple[int, str]] | None = None,
    table_path: Path | None = None,
) -> tuple[list[str], list[str], str]:
    errors: list[str] = []
    warnings: list[str] = []
    canonical = canonical or load_canonical_table(table_path)

    if data.get("version") != "v0.4.1.3":
        errors.append(f'version must be "v0.4.1.3", got {data.get("version")!r}')
    if data.get("total_families") != 288:
        errors.append(f"total_families must be 288, got {data.get('total_families')}")

    families: list[dict[str, Any]] = data.get("families") or []
    if len(families) != 288:
        errors.append(f"families list must have 288 entries, got {len(families)}")

    seen_ids: set[int] = set()
    seen_label_slugs: dict[str, int] = {}
    by_area: dict[int, list[dict[str, Any]]] = defaultdict(list)
    central_users: dict[str, list[int]] = defaultdict(list)
    boundary_users: dict[str, list[int]] = defaultdict(list)
    label_to_ids: dict[str, list[int]] = defaultdict(list)
    by_id: dict[int, dict[str, Any]] = {}

    for i, f in enumerate(families):
        fid = f.get("family_id")
        if not isinstance(fid, int) or not (1 <= fid <= 288):
            errors.append(f"families[{i}]: family_id must be int 1-288, got {fid!r}")
            continue
        if fid in seen_ids:
            errors.append(f"families[{i}]: duplicate family_id {fid}")
        seen_ids.add(fid)
        by_id[fid] = f

        area_id = f.get("area_id")
        if not isinstance(area_id, int) or not (1 <= area_id <= 12):
            errors.append(f"families[{i}]: area_id must be int 1-12, got {area_id!r}")
            continue

        label = str(f.get("label", "")).strip()
        if not label:
            errors.append(f"families[{i}]: label must be non-empty string")
        elif fid in canonical:
            exp_area, exp_label = canonical[fid]
            if area_id != exp_area:
                errors.append(f"family_id {fid}: area_id mismatch {area_id} != {exp_area}")
            if label != exp_label:
                errors.append(f"family_id {fid}: label mismatch {label!r} != {exp_label!r}")

        label_slug = str(f.get("label_slug", "")).strip()
        if not label_slug:
            errors.append(f"family_id {fid}: missing label_slug")
        else:
            base_slug = _slug(label)
            if label_slug != base_slug and not re.fullmatch(rf"{re.escape(base_slug)}_a\d+", label_slug):
                errors.append(
                    f"family_id {fid}: label_slug {label_slug!r} must be normalized label {base_slug!r} or area-suffixed variant"
                )
        if label_slug in seen_label_slugs:
            errors.append(f"label_slug {label_slug!r} duplicated by family_ids {seen_label_slugs[label_slug]} and {fid}")
        else:
            seen_label_slugs[label_slug] = fid

        core = str(f.get("core_definition", ""))
        pos = str(f.get("positive_axis", ""))
        neg = str(f.get("negative_axis", ""))
        if not core.strip():
            errors.append(f"family_id {fid}: core_definition missing")
        core_l = core.lower()
        for t in TEMPLATE_PHRASES:
            if t in core_l:
                errors.append(f"family_id {fid}: core_definition contains banned template phrase {t!r}")

        if not any(w in pos.lower() for w in MECHANISM_WORDS):
            errors.append(f"family_id {fid}: positive_axis missing mechanism word")
        if not any(w in neg.lower() for w in MECHANISM_WORDS):
            errors.append(f"family_id {fid}: negative_axis missing mechanism word")

        excluded = f.get("excluded_neighbors") or []
        if not isinstance(excluded, list) or not all(isinstance(x, int) for x in excluded):
            errors.append(f"family_id {fid}: excluded_neighbors must be list[int]")
            excluded = []
        allowed_adj = {x for x in [fid - 2, fid - 1, fid + 1, fid + 2] if 1 <= x <= 288}
        if excluded and set(excluded).issubset(allowed_adj):
            errors.append(f"family_id {fid}: excluded_neighbors look like numeric adjacency only: {excluded}")

        central = f.get("central_examples") or []
        boundary = f.get("boundary_examples") or []
        if not isinstance(central, list):
            errors.append(f"family_id {fid}: central_examples must be list")
            central = []
        if not isinstance(boundary, list):
            errors.append(f"family_id {fid}: boundary_examples must be list")
            boundary = []

        if len(central) < 6:
            errors.append(f"family_id {fid}: central_examples must have >=6 tokens")
        if len(boundary) < 4:
            errors.append(f"family_id {fid}: boundary_examples must have >=4 tokens")

        norm_c = {_norm_token(str(x)) for x in central}
        norm_b = {_norm_token(str(x)) for x in boundary}
        if norm_c & norm_b:
            errors.append(f"family_id {fid}: central/boundary intersection: {sorted(norm_c & norm_b)}")

        for name, toks in [("central_examples", central), ("boundary_examples", boundary)]:
            for tok in toks:
                if not isinstance(tok, str):
                    errors.append(f"family_id {fid}: {name} token must be str, got {tok!r}")
                    continue
                if " " in tok or "&" in tok or "/" in tok:
                    errors.append(f"family_id {fid}: {name} token must be one token and cannot contain '&' or '/': {tok!r}")
                norm = _norm_token(tok)
                if not norm:
                    errors.append(f"family_id {fid}: {name} token empty after normalization: {tok!r}")
                    continue
                if name == "central_examples":
                    central_users[norm].append(fid)
                else:
                    boundary_users[norm].append(fid)
                if norm in BANNED_TOKENS:
                    errors.append(f"family_id {fid}: banned token {norm!r}")
                if norm in AREA_TOKEN_EXCEPTIONS and area_id not in AREA_TOKEN_EXCEPTIONS[norm]:
                    errors.append(f"family_id {fid}: token {norm!r} only allowed in areas {sorted(AREA_TOKEN_EXCEPTIONS[norm])}")

        if not f.get("notes"):
            warnings.append(f"family_id {fid}: notes missing")

        label_to_ids[label.lower()].append(fid)
        by_area[area_id].append({"id": fid, "central": norm_c, "boundary": norm_b})

    for fid in range(1, 289):
        if fid not in seen_ids:
            errors.append(f"family_id {fid} missing")

    # Intra-area overlap checks
    for area_id, items in by_area.items():
        for i in range(len(items)):
            for j in range(i + 1, len(items)):
                a, b = items[i], items[j]
                c_overlap = a["central"] & b["central"]
                b_overlap = a["boundary"] & b["boundary"]
                if len(c_overlap) > 1:
                    errors.append(
                        f"area {area_id}: central overlap >1 between family {a['id']} and {b['id']}: {sorted(c_overlap)}"
                    )
                if len(b_overlap) > 1:
                    errors.append(
                        f"area {area_id}: boundary overlap >1 between family {a['id']} and {b['id']}: {sorted(b_overlap)}"
                    )

    # Cross-area duplicates
    for tok, ids in central_users.items():
        if len(set(ids)) > 2:
            errors.append(f"central token {tok!r} used by >2 families: {sorted(set(ids))}")
    for tok, ids in boundary_users.items():
        if len(set(ids)) > 6:
            errors.append(f"boundary token {tok!r} used by >6 families: {sorted(set(ids))}")

    # Exclusion symmetry
    for fid, fam in by_id.items():
        excluded = fam.get("excluded_neighbors") or []
        notes = str(fam.get("notes") or "")
        for other in excluded:
            ofam = by_id.get(other)
            if not ofam:
                errors.append(f"family_id {fid}: excluded neighbor {other} does not exist")
                continue
            back = ofam.get("excluded_neighbors") or []
            if fid not in back and "asymmetric_exclusion:" not in notes:
                errors.append(f"family_id {fid}: excludes {other} without symmetry or asymmetric_exclusion note")

    # Mirrors for duplicate labels
    for _, ids in label_to_ids.items():
        if len(ids) <= 1:
            continue
        if len(ids) == 2:
            a, b = ids
            fa, fb = by_id[a], by_id[b]
            ma = sorted(fa.get("mirrors") or [])
            mb = sorted(fb.get("mirrors") or [])
            if ma != [b] or mb != [a]:
                errors.append(f"mirror labels {a}<->{b}: mirrors fields must reference each other")
            if str(fa.get("core_definition", "")).strip() == str(fb.get("core_definition", "")).strip():
                errors.append(f"mirror labels {a}<->{b}: core_definition must differ")
            ca = {_norm_token(x) for x in (fa.get("central_examples") or [])}
            cb = {_norm_token(x) for x in (fb.get("central_examples") or [])}
            if ca & cb:
                errors.append(f"mirror labels {a}<->{b}: central overlap must be 0, got {sorted(ca & cb)}")

    # Build audit report
    lines: list[str] = []
    lines.append("Families v0.4.1.3 semantic audit report")
    lines.append("=" * 52)
    lines.append(f"families_count={len(families)} errors={len(errors)} warnings={len(warnings)}")
    lines.append("")
    lines.append("Per-area max overlap summary (central/boundary):")
    for area_id in range(1, 13):
        items = by_area.get(area_id, [])
        max_c = max_b = 0
        for i in range(len(items)):
            for j in range(i + 1, len(items)):
                max_c = max(max_c, len(items[i]["central"] & items[j]["central"]))
                max_b = max(max_b, len(items[i]["boundary"] & items[j]["boundary"]))
        lines.append(f"area {area_id:02d}: max_central_overlap={max_c} max_boundary_overlap={max_b}")

    lines.append("")
    lines.append("Top duplicated central tokens:")
    for tok, n in Counter({k: len(set(v)) for k, v in central_users.items()}).most_common(20):
        if n > 1:
            lines.append(f"  {tok}: {n} families {sorted(set(central_users[tok]))}")
    lines.append("")
    lines.append("Top duplicated boundary tokens:")
    for tok, n in Counter({k: len(set(v)) for k, v in boundary_users.items()}).most_common(20):
        if n > 1:
            lines.append(f"  {tok}: {n} families {sorted(set(boundary_users[tok]))}")

    lines.append("")
    lines.append("Mirror pairs:")
    seen_pairs: set[tuple[int, int]] = set()
    for _, ids in label_to_ids.items():
        if len(ids) == 2:
            a, b = sorted(ids)
            if (a, b) not in seen_pairs:
                lines.append(f"  {a}<->{b}")
                seen_pairs.add((a, b))

    lines.append("")
    lines.append("Per-family counts (real + structural-ready):")
    for f in sorted(families, key=lambda x: int(x.get("family_id", 999))):
        fid = int(f.get("family_id", 0))
        c = len(f.get("central_examples") or [])
        b = len(f.get("boundary_examples") or [])
        structural = 2 if f.get("label_slug") else 0
        lines.append(f"  family {fid:03d}: central={c} boundary={b} structural={structural} real={c+b}")

    report = "\n".join(lines) + "\n"
    return errors, warnings, report
