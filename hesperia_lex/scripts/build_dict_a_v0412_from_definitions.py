#!/usr/bin/env python3
"""
Build Dict A v0.4.1.2 from canonical families.yaml (definition-driven; no pool semantics).
Process: load families.yaml → validate → derive anchors from central + boundary examples
→ apply weight policy → merge structural fallback (≤4) → emit Dict A.
Output: hesperia_lex/curated/A_CORE_STAR_MAP_v0_4_1_2.json
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent.parent
DEFINITIONS_DIR = REPO_ROOT / "hesperia_lex" / "definitions" / "v0412"
FAMILIES_YAML = DEFINITIONS_DIR / "families.yaml"
TABLE_PATH = REPO_ROOT / "31_FAMILIES__area_family_table_full.txt"
OUT_PATH = REPO_ROOT / "hesperia_lex" / "curated" / "A_CORE_STAR_MAP_v0_4_1_2.json"

SIDES_PER_FAMILY = 1500

# Weight policy: central (high), boundary (low), structural fallback (≤4)
WEIGHT_CENTRAL_START = 0.78
WEIGHT_CENTRAL_DECAY = 0.03
WEIGHT_BOUNDARY_START = 0.42
WEIGHT_BOUNDARY_DECAY = 0.04
WEIGHT_STRUCTURAL = [0.55, 0.50, 0.45, 0.40]
MAX_STRUCTURAL_ANCHORS = 4


def _normalize(s: str) -> str:
    return re.sub(r"[^a-z0-9]+", "_", s.lower().strip()).strip("_") or "family"


def _load_yaml(path: Path) -> dict:
    try:
        import yaml
    except ImportError:
        raise SystemExit("PyYAML required: pip install pyyaml")
    with open(path, encoding="utf-8") as f:
        return yaml.safe_load(f)


def main() -> None:
    if not FAMILIES_YAML.exists():
        print(f"Missing {FAMILIES_YAML}", file=sys.stderr)
        sys.exit(1)

    data = _load_yaml(FAMILIES_YAML)
    sys.path.insert(0, str(DEFINITIONS_DIR))
    import validate as vmod
    errors = vmod.validate_families_yaml(data, table_path=TABLE_PATH)
    if errors:
        for e in errors:
            print("VALIDATE_ERR:", e, file=sys.stderr)
        sys.exit(1)

    families = data["families"]
    out: dict[str, list[dict]] = {
        "_comment": (
            "Dict A v0.4.1.2 definition-driven: central + boundary examples from families.yaml, "
            "structural fallback ≤4. No pool semantics."
        ),
    }

    for f in families:
        family_id = int(f["family_id"])
        label = f["label"]
        central = [str(x).strip().lower() for x in (f.get("central_examples") or []) if isinstance(x, str)]
        boundary = [str(x).strip().lower() for x in (f.get("boundary_examples") or []) if isinstance(x, str)]
        family_global = family_id - 1
        side_id = family_global * SIDES_PER_FAMILY

        slot = 0
        # Central examples (higher weight)
        for i, word in enumerate(central[:6]):
            w = WEIGHT_CENTRAL_START - i * WEIGHT_CENTRAL_DECAY
            w = max(0.25, min(0.95, round(w, 2)))
            key = f"{_normalize(word)}_{family_id}_{slot}"
            out[key] = [{"side_id": side_id, "weight": w, "map_code": "definition_central_v0412"}]
            slot += 1
        # Boundary examples (lower weight)
        for i, word in enumerate(boundary[:4]):
            w = WEIGHT_BOUNDARY_START - i * WEIGHT_BOUNDARY_DECAY
            w = max(0.20, min(0.50, round(w, 2)))
            key = f"{_normalize(word)}_{family_id}_{slot}"
            out[key] = [{"side_id": side_id, "weight": w, "map_code": "definition_boundary_v0412"}]
            slot += 1
        # Structural fallback: normalized label + up to 3 more from same-area labels (≤4 total)
        label_tokens = _normalize(label).split("_") if _normalize(label) else ["family"]
        structural_words = list(dict.fromkeys(label_tokens))[:MAX_STRUCTURAL_ANCHORS]
        while len(structural_words) < MAX_STRUCTURAL_ANCHORS:
            structural_words.append(structural_words[-1] if structural_words else "family")
        for i, word in enumerate(structural_words[:MAX_STRUCTURAL_ANCHORS]):
            w = WEIGHT_STRUCTURAL[i] if i < len(WEIGHT_STRUCTURAL) else 0.40
            key = f"{word}_{family_id}_{slot}"
            out[key] = [{"side_id": side_id, "weight": w, "map_code": "structural_fallback_v0412"}]
            slot += 1

    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUT_PATH.write_text(json.dumps(out, indent=2), encoding="utf-8")
    n = len([k for k in out if not k.startswith("_")])
    print(f"Wrote {OUT_PATH}: {n} entries (v0.4.1.2 definition-driven)")


if __name__ == "__main__":
    main()
