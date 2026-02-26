#!/usr/bin/env python3
"""
HESPERIA v0.6 — Build family specification for Dict A v0.6 (288 families).
Output: label, core_definition, positive_axis, negative_axis, central_examples.
Skeleton from invariant_catalog.AREA_FAMILY_MAP; replace with curated content before freeze.
Run from repo root CLIENTS/hesperia. Output: hesperia_lex/curated/FAMILY_SPEC_v0_6.json.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent.parent
if str(REPO) not in sys.path:
    sys.path.insert(0, str(REPO))

from sphere_rag.invariant_catalog import AREA_FAMILY_MAP

AREA_ORDER = list(AREA_FAMILY_MAP.keys())
assert len(AREA_ORDER) == 12

# One-line placeholders per area for skeleton (replace with curated)
AREA_DEFINITION: dict[str, str] = {
    "GOOD": "Moral good, virtue, and prosocial orientation.",
    "CARE": "Nurturing, support, and protection of the vulnerable.",
    "ORDER": "Structure, stability, and governance.",
    "CONTROL": "Oversight, enforcement, and restriction.",
    "INDIFFERENCE": "Neglect, detachment, and withholding engagement.",
    "HARM": "Violence, exploitation, and damage to others.",
    "DESTRUCTION": "Demolition, erasure, and removal.",
    "CHAOS": "Instability, unpredictability, and breakdown.",
    "FREEDOM": "Autonomy, choice, and absence of coercion.",
    "TRUTH": "Accuracy, evidence, and transparency.",
    "DECEIT": "Lies, concealment, and manipulation.",
    "CREATION": "Building, invention, and growth.",
}
AREA_POSITIVE: dict[str, str] = {
    "GOOD": "selflessness, virtue, reciprocity",
    "CARE": "support, comfort, safety",
    "ORDER": "structure, rules, predictability",
    "CONTROL": "oversight, compliance, boundaries",
    "INDIFFERENCE": "detachment, non-interference",
    "HARM": "coercion, injury, abuse",
    "DESTRUCTION": "removal, demolition, erasure",
    "CHAOS": "flux, disruption, disorder",
    "FREEDOM": "choice, consent, liberty",
    "TRUTH": "accuracy, verification, disclosure",
    "DECEIT": "concealment, misrepresentation",
    "CREATION": "building, design, synthesis",
}
AREA_NEGATIVE: dict[str, str] = {
    "GOOD": "selfishness, harm, neglect",
    "CARE": "neglect, coldness, abandonment",
    "ORDER": "chaos, arbitrariness, neglect",
    "CONTROL": "anarchy, evasion, rebellion",
    "INDIFFERENCE": "engagement, responsibility, care",
    "HARM": "care, protection, healing",
    "DESTRUCTION": "creation, preservation, repair",
    "CHAOS": "order, stability, control",
    "FREEDOM": "coercion, restriction, captivity",
    "TRUTH": "lies, obfuscation, fabrication",
    "DECEIT": "honesty, transparency, integrity",
    "CREATION": "destruction, stagnation, neglect",
}


def main() -> int:
    out: list[dict] = []
    idx = 0
    for area in AREA_ORDER:
        families = AREA_FAMILY_MAP[area]
        core_def = AREA_DEFINITION.get(area, "Semantic family in the taxonomy.")
        pos_axis = AREA_POSITIVE.get(area, "positive pole")
        neg_axis = AREA_NEGATIVE.get(area, "negative pole")
        for label in families:
            # Central examples: label plus area-typical terms
            examples = f"{label}, {area.lower()}"
            out.append({
                "family_id": idx,
                "label": label,
                "core_definition": core_def,
                "positive_axis": pos_axis,
                "negative_axis": neg_axis,
                "central_examples": examples,
            })
            idx += 1
    assert idx == 288, idx
    out_path = REPO / "hesperia_lex" / "curated" / "FAMILY_SPEC_v0_6.json"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2, ensure_ascii=False)
    print(f"Written: {out_path} ({len(out)} families)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
