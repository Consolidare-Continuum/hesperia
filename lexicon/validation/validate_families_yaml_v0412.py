#!/usr/bin/env python3
"""Validate families.yaml (v0.4.1.2). Exit 0 if valid, 1 and errors to stderr otherwise."""
from __future__ import annotations

import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent.parent
DEFINITIONS_DIR = REPO_ROOT / "lexicon" / "definitions" / "v0412"
FAMILIES_YAML = DEFINITIONS_DIR / "families.yaml"
TABLE_PATH = REPO_ROOT / "31_FAMILIES__area_family_table_full.txt"


def main() -> int:
    if not FAMILIES_YAML.exists():
        print(f"Missing {FAMILIES_YAML}", file=sys.stderr)
        return 1
    try:
        import yaml
    except ImportError:
        print("PyYAML required: pip install pyyaml", file=sys.stderr)
        return 1
    with open(FAMILIES_YAML, encoding="utf-8") as f:
        data = yaml.safe_load(f)
    sys.path.insert(0, str(DEFINITIONS_DIR))
    import validate as vmod
    errors = vmod.validate_families_yaml(data, table_path=TABLE_PATH)
    if errors:
        for e in errors:
            print("VALIDATE_ERR:", e, file=sys.stderr)
        return 1
    print("OK: families.yaml valid (v0.4.1.2)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
