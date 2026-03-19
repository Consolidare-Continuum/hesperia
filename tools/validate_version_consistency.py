#!/usr/bin/env python3
# HESPERIA — Task 6 Phase 1.8: version authority quick check.
# Copyright © 2026 igareosh.com. See LEGAL_NOTICE.md.
#
# Usage: python3 tools/validate_version_consistency.py

from __future__ import annotations

import re
import sys
from pathlib import Path

_REPO = Path(__file__).resolve().parents[1]
_VERSION_YAML = _REPO / "VERSION.yaml"
_PYPROJECT = _REPO / "pyproject.toml"


def main() -> int:
    errs: list[str] = []
    if not _VERSION_YAML.is_file():
        errs.append(f"missing {_VERSION_YAML}")
    if not _PYPROJECT.is_file():
        errs.append("missing pyproject.toml")
    if errs:
        print("\n".join(errs), file=sys.stderr)
        return 1

    import yaml

    doc = yaml.safe_load(_VERSION_YAML.read_text(encoding="utf-8")) or {}
    sys_v = str(doc.get("system_version", ""))
    pp = _PYPROJECT.read_text(encoding="utf-8")
    m = re.search(r'^version\s*=\s*"([^"]+)"', pp, re.M)
    pp_v = m.group(1) if m else ""
    if sys_v != pp_v:
        errs.append(f"VERSION.yaml system_version ({sys_v!r}) != pyproject version ({pp_v!r})")

    hesperia_link = _REPO / "hesperia" / "VERSION.yaml"
    if hesperia_link.is_file():
        if hesperia_link.resolve() != _VERSION_YAML.resolve():
            errs.append("hesperia/VERSION.yaml does not resolve to root VERSION.yaml")
    else:
        errs.append("hesperia/VERSION.yaml missing (expected symlink to ../VERSION.yaml)")

    sch = doc.get("schema") or {}
    if not sch.get("public_output"):
        errs.append("VERSION.yaml schema.public_output missing")

    if errs:
        print("validate_version_consistency: FAIL", file=sys.stderr)
        for e in errs:
            print(" ", e, file=sys.stderr)
        return 1

    print(f"validate_version_consistency: OK system_version={sys_v} public_output_schema={sch.get('public_output')}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
