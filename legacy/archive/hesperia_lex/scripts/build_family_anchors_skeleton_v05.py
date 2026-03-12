#!/usr/bin/env python3

# HESPERIA — Reference Architecture Definition (RAD)
# Copyright © 2026 igareosh.com — Platonov Igor (aka @igareosh). All rights reserved.
# Restricted Research Disclosure License. Inspection and reference only.
# No reproduction, redistribution, or use without explicit written permission from the author.
# See LEGAL_NOTICE.md for full terms.

"""
Generate FAMILY_ANCHORS_v0_5.json skeleton (288 families) from invariant_catalog.AREA_FAMILY_MAP.
Run from repo root CLIENTS/hesperia. Output: hesperia_lex/curated/FAMILY_ANCHORS_v0_5.json.
Skeleton satisfies 5–20 positive, 3–10 negative per family; replace with curated anchors before freeze.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent.parent
if str(REPO) not in sys.path:
    sys.path.insert(0, str(REPO))

from sphere_rag.invariant_catalog import AREA_FAMILY_MAP, FAMILIES_PER_AREA

# Use AREA_FAMILY_MAP key order (Python 3.7+ insertion order)
AREA_ORDER = list(AREA_FAMILY_MAP.keys())
assert len(AREA_ORDER) == 12

# Per-area extra positive/negative terms (skeleton filler; replace with curated)
AREA_POSITIVE_EXTRAS: dict[str, list[str]] = {
    "GOOD": ["generosity", "benevolence", "kindness", "virtue", "goodwill"],
    "CARE": ["support", "nurture", "comfort", "safety", "attention"],
    "ORDER": ["structure", "stability", "rules", "discipline", "organization"],
    "CONTROL": ["oversight", "enforcement", "authority", "compliance", "regulation"],
    "INDIFFERENCE": ["neglect", "apathy", "detachment", "bystanding", "withholding"],
    "HARM": ["violence", "exploitation", "oppression", "abuse", "coercion"],
    "DESTRUCTION": ["demolition", "erasure", "collapse", "damage", "removal"],
    "CHAOS": ["instability", "turbulence", "conflict", "fragmentation", "flux"],
    "FREEDOM": ["autonomy", "liberty", "choice", "privacy", "consent"],
    "TRUTH": ["accuracy", "evidence", "verification", "clarity", "honesty"],
    "DECEIT": ["lies", "misinformation", "concealment", "fraud", "manipulation"],
    "CREATION": ["imagination", "invention", "design", "building", "synthesis"],
}
AREA_NEGATIVE_EXTRAS: dict[str, list[str]] = {
    "GOOD": ["selfishness", "greed", "exploitation", "harm", "neglect"],
    "CARE": ["neglect", "coldness", "abandonment", "indifference", "harm"],
    "ORDER": ["chaos", "disorder", "instability", "neglect", "arbitrariness"],
    "CONTROL": ["freedom", "anarchy", "evasion", "rebellion", "disorder"],
    "INDIFFERENCE": ["care", "attention", "engagement", "responsibility", "concern"],
    "HARM": ["care", "protection", "healing", "safety", "goodwill"],
    "DESTRUCTION": ["creation", "preservation", "repair", "building", "growth"],
    "CHAOS": ["order", "stability", "coordination", "predictability", "control"],
    "FREEDOM": ["coercion", "restriction", "control", "oppression", "captivity"],
    "TRUTH": ["lies", "deceit", "obfuscation", "misinformation", "fraud"],
    "DECEIT": ["truth", "transparency", "honesty", "disclosure", "integrity"],
    "CREATION": ["destruction", "erasure", "demolition", "neglect", "stagnation"],
}


def slug(s: str) -> str:
    return re.sub(r"[^\w\s-]", "", s).lower().replace("-", " ").strip() or s.lower()


def main() -> int:
    out: dict[str, dict] = {}
    idx = 0
    for area in AREA_ORDER:
        families = AREA_FAMILY_MAP[area]
        pos_extras = AREA_POSITIVE_EXTRAS.get(area, ["value", "practice", "quality", "support", "form"])[:5]
        neg_extras = AREA_NEGATIVE_EXTRAS.get(area, ["opposite", "harm", "neglect"])[:5]
        for label in families:
            key = str(idx)
            label_slug = slug(label)
            # 5–20 positive: label + extras (skeleton uses 5–8)
            positive = [label_slug] + [w for w in pos_extras if w != label_slug][:7]
            if len(positive) < 5:
                positive.extend(["value", "practice", "quality"][: 5 - len(positive)])
            positive = positive[:20]
            # 3–10 negative
            negative = neg_extras[: max(3, min(10, len(neg_extras)))]
            out[key] = {"label": label, "positive": positive, "negative": negative}
            idx += 1
    assert idx == 288, idx
    out_path = REPO / "hesperia_lex" / "curated" / "FAMILY_ANCHORS_v0_5.json"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2, ensure_ascii=False)
    print(f"Written: {out_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
