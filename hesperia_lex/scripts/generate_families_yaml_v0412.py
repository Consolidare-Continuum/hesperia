#!/usr/bin/env python3
"""
Generate initial families.yaml (v0.4.1.2) from 31_FAMILIES__area_family_table_full.txt.
Fills structural placeholders; definitions and examples are minimal and should be refined.
Output: hesperia_lex/definitions/v0412/families.yaml
"""
from __future__ import annotations

import re
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent.parent
TABLE_PATH = REPO_ROOT / "31_FAMILIES__area_family_table_full.txt"
OUT_PATH = REPO_ROOT / "hesperia_lex" / "definitions" / "v0412" / "families.yaml"

AREA_ORDER = [
    "GOOD", "HARM", "TRUTH", "DECEIT", "ORDER", "CHAOS",
    "FREEDOM", "CONTROL", "CARE", "INDIFFERENCE", "CREATION", "DESTRUCTION",
]


def _tokenize_label(label: str) -> list[str]:
    """Single-token candidates from label: split on non-alpha, lowercase, drop empty."""
    tokens = re.sub(r"[^a-zA-Z0-9\s-]", " ", label).split()
    return [t.lower() for t in tokens if t]


def _ensure_central_examples(label: str, area: str, n: int = 4) -> list[str]:
    """At least 3, up to 6 single-token central examples. Prefer label-derived."""
    tokens = _tokenize_label(label)
    out = list(dict.fromkeys(tokens))[:4]
    # Fallback words per area so we have 3–6
    fallbacks: dict[str, list[str]] = {
        "GOOD": ["care", "trust", "help", "fair", "support"],
        "HARM": ["harm", "hurt", "abuse", "risk", "damage"],
        "TRUTH": ["fact", "evidence", "proof", "valid", "clear"],
        "DECEIT": ["lie", "fake", "hide", "trick", "false"],
        "ORDER": ["rule", "structure", "process", "system", "protocol"],
        "CHAOS": ["noise", "disorder", "drift", "change", "random"],
        "FREEDOM": ["choice", "right", "open", "free", "access"],
        "CONTROL": ["limit", "rule", "gate", "power", "restrict"],
        "CARE": ["care", "support", "shelter", "aid", "comfort"],
        "INDIFFERENCE": ["neglect", "ignore", "cold", "absent", "passive"],
        "CREATION": ["create", "build", "design", "make", "art"],
        "DESTRUCTION": ["remove", "break", "end", "loss", "ruin"],
    }
    pool = fallbacks.get(area, fallbacks["GOOD"])
    for w in pool:
        if len(out) >= n:
            break
        if w not in out:
            out.append(w)
    return out[:6]


def _ensure_boundary_examples(area: str, n: int = 3) -> list[str]:
    """2–4 single-token boundary examples (edge tension)."""
    by_area: dict[str, list[str]] = {
        "GOOD": ["neglect", "harm", "bias"],
        "HARM": ["mercy", "restraint", "limit"],
        "TRUTH": ["uncertainty", "bias", "noise"],
        "DECEIT": ["truth", "transparency", "limit"],
        "ORDER": ["chaos", "drift", "edge"],
        "CHAOS": ["order", "stability", "limit"],
        "FREEDOM": ["control", "restriction", "limit"],
        "CONTROL": ["freedom", "escape", "chaos"],
        "CARE": ["neglect", "indifference", "harm"],
        "INDIFFERENCE": ["care", "attention", "bias"],
        "CREATION": ["destruction", "decay", "limit"],
        "DESTRUCTION": ["creation", "preservation", "limit"],
    }
    return by_area.get(area, ["limit", "edge", "boundary"])[:n]


def main() -> None:
    lines = TABLE_PATH.read_text(encoding="utf-8").strip().splitlines()
    rows = [l.split("\t") for l in lines[1:] if l]
    area_to_id = {a: i + 1 for i, a in enumerate(AREA_ORDER)}

    families: list[dict] = []
    for row in rows:
        if len(row) < 3:
            continue
        num = int(row[0])
        area_name = row[1].strip()
        label = row[2].strip()
        area_id = area_to_id.get(area_name, 1)
        # Same-area neighbors for excluded_neighbors (1–3)
        same_area = [r for r in rows if len(r) >= 3 and r[1].strip() == area_name]
        same_area_nums = [int(r[0]) for r in same_area]
        idx_in_area = same_area_nums.index(num) if num in same_area_nums else 0
        neighbors = []
        for d in (1, -1, 2):
            i2 = idx_in_area + d
            if 0 <= i2 < len(same_area_nums) and same_area_nums[i2] != num:
                neighbors.append(same_area_nums[i2])
                if len(neighbors) >= 3:
                    break

        central = _ensure_central_examples(label, area_name, 4)
        boundary = _ensure_boundary_examples(area_name, 3)

        families.append({
            "family_id": num,
            "area_id": area_id,
            "label": label,
            "core_definition": f"Domain concerning {label} and its structural role within the taxonomy.",
            "positive_axis": f"Promotes or instantiates {label} in context.",
            "negative_axis": "Structural opposite or absence of the domain.",
            "excluded_neighbors": neighbors[:3],
            "central_examples": central,
            "boundary_examples": boundary,
        })

    out_lines = [
        'version: "v0.4.1.2"',
        "total_families: 288",
        "",
        "families:",
    ]
    for f in families:
        out_lines.append("  - family_id: " + str(f["family_id"]))
        out_lines.append("    area_id: " + str(f["area_id"]))
        out_lines.append('    label: "' + f["label"].replace('"', '\\"') + '"')
        out_lines.append('    core_definition: "' + f["core_definition"].replace('"', '\\"') + '"')
        out_lines.append('    positive_axis: "' + f["positive_axis"].replace('"', '\\"') + '"')
        out_lines.append('    negative_axis: "' + f["negative_axis"].replace('"', '\\"') + '"')
        out_lines.append("    excluded_neighbors: " + str(f["excluded_neighbors"]))
        out_lines.append("    central_examples:")
        for w in f["central_examples"]:
            out_lines.append('      - ' + w)
        out_lines.append("    boundary_examples:")
        for w in f["boundary_examples"]:
            out_lines.append('      - ' + w)
        out_lines.append("")

    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUT_PATH.write_text("\n".join(out_lines), encoding="utf-8")
    print(f"Wrote {OUT_PATH}: {len(families)} families")


if __name__ == "__main__":
    main()
