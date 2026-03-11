#!/usr/bin/env python3
"""Validate families.yaml (v0.4.1.3) and emit semantic audit report."""
from __future__ import annotations

import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent.parent
DEFINITIONS_DIR = REPO_ROOT / "lexicon" / "definitions" / "v0413"
FAMILIES_YAML = DEFINITIONS_DIR / "families.yaml"
TABLE_PATH = REPO_ROOT / "31_FAMILIES__area_family_table_full.txt"
AUDIT_PATH = REPO_ROOT / "assets" / "v0413" / "families_semantic_audit_report.txt"


def main() -> int:
    if not FAMILIES_YAML.exists():
        print(f"Missing {FAMILIES_YAML}", file=sys.stderr)
        return 1
    raw = FAMILIES_YAML.read_text(encoding="utf-8")
    try:
        import json
        data = json.loads(raw)
    except Exception:
        try:
            import yaml
            data = yaml.safe_load(raw)
        except ImportError:
            print("PyYAML required when families.yaml is not JSON-compatible.", file=sys.stderr)
            return 1
    sys.path.insert(0, str(DEFINITIONS_DIR))
    import validate as vmod

    errors, warnings, report = vmod.validate_families_yaml(data, table_path=TABLE_PATH)
    AUDIT_PATH.parent.mkdir(parents=True, exist_ok=True)
    AUDIT_PATH.write_text(report, encoding="utf-8")

    for w in warnings:
        print("VALIDATE_WARN:", w)
    if errors:
        for e in errors:
            print("VALIDATE_ERR:", e, file=sys.stderr)
        print(f"Wrote audit report: {AUDIT_PATH}")
        return 1

    print("OK: families.yaml valid (v0.4.1.3)")
    print(f"Wrote audit report: {AUDIT_PATH}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
