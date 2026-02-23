"""
Validate families.yaml (v0.4.1.2): schema, field rules, label match to 31_FAMILIES.
Build must fail if any validation rule fails.
"""
from __future__ import annotations

from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parent.parent.parent.parent
TABLE_PATH = REPO_ROOT / "31_FAMILIES__area_family_table_full.txt"


def load_canonical_table(table_path: Path | None = None) -> dict[int, tuple[int, str]]:
    """Load 31_FAMILIES table. Returns family_id (1-288) -> (area_id 1-12, label)."""
    path = table_path or TABLE_PATH
    if not path.exists():
        return {}
    lines = path.read_text(encoding="utf-8").strip().splitlines()
    area_order = [
        "GOOD", "HARM", "TRUTH", "DECEIT", "ORDER", "CHAOS",
        "FREEDOM", "CONTROL", "CARE", "INDIFFERENCE", "CREATION", "DESTRUCTION",
    ]
    area_to_id = {a: i + 1 for i, a in enumerate(area_order)}
    out: dict[int, tuple[int, str]] = {}
    for line in lines[1:]:
        if not line.strip():
            continue
        parts = line.split("\t")
        if len(parts) < 3:
            continue
        num = int(parts[0])
        area_name = parts[1].strip()
        label = parts[2].strip()
        area_id = area_to_id.get(area_name, 1)
        out[num] = (area_id, label)
    return out


def validate_families_yaml(
    data: dict[str, Any],
    canonical: dict[int, tuple[int, str]] | None = None,
    table_path: Path | None = None,
) -> list[str]:
    """
    Validate loaded families.yaml. Returns list of error strings (empty if valid).
    Build must fail if any error is returned.
    """
    errors: list[str] = []
    if canonical is None:
        canonical = load_canonical_table(table_path)

    if data.get("version") != "v0.4.1.2":
        errors.append(f'version must be "v0.4.1.2", got {data.get("version")!r}')
    total = data.get("total_families")
    if total != 288:
        errors.append(f"total_families must be 288, got {total}")

    families: list[dict] = data.get("families") or []
    if len(families) != 288:
        errors.append(f"families list must have 288 entries, got {len(families)}")

    seen_ids: set[int] = set()
    for i, f in enumerate(families):
        fid = f.get("family_id")
        if fid is None:
            errors.append(f"families[{i}]: missing family_id")
            continue
        if not isinstance(fid, int) or not (1 <= fid <= 288):
            errors.append(f"families[{i}]: family_id must be int 1-288, got {fid!r}")
        if fid in seen_ids:
            errors.append(f"families[{i}]: duplicate family_id {fid}")
        seen_ids.add(fid)

        area_id = f.get("area_id")
        if area_id is not None and (not isinstance(area_id, int) or not (1 <= area_id <= 12)):
            errors.append(f"families[{i}]: area_id must be int 1-12, got {area_id!r}")

        label = f.get("label")
        if not isinstance(label, str) or not label.strip():
            errors.append(f"families[{i}]: label must be non-empty string")
        elif canonical and fid in canonical:
            expected_area_id, expected_label = canonical[fid]
            if label.strip() != expected_label.strip():
                errors.append(
                    f"families[{i}]: label mismatch for family_id {fid}: "
                    f"got {label!r}, canonical is {expected_label!r}"
                )
            if area_id is not None and int(area_id) != expected_area_id:
                errors.append(
                    f"families[{i}]: area_id mismatch for family_id {fid}: "
                    f"got {area_id}, canonical is {expected_area_id}"
                )

        central = f.get("central_examples") or []
        if not isinstance(central, list):
            errors.append(f"families[{i}]: central_examples must be list")
        else:
            if len(central) < 3:
                errors.append(f"families[{i}]: central_examples must have at least 3, got {len(central)}")
            for j, w in enumerate(central):
                if not isinstance(w, str) or " " in w.strip():
                    errors.append(f"families[{i}].central_examples[{j}]: must be single token (no space), got {w!r}")

        boundary = f.get("boundary_examples") or []
        if not isinstance(boundary, list):
            errors.append(f"families[{i}]: boundary_examples must be list")
        else:
            if len(boundary) < 2:
                errors.append(f"families[{i}]: boundary_examples must have at least 2, got {len(boundary)}")
            for j, w in enumerate(boundary):
                if not isinstance(w, str) or " " in w.strip():
                    errors.append(f"families[{i}].boundary_examples[{j}]: must be single token (no space), got {w!r}")

    for fid in range(1, 289):
        if fid not in seen_ids:
            errors.append(f"family_id {fid} missing")

    return errors
