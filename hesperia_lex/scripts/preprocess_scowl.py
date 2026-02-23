#!/usr/bin/env python3
"""
Phase 2B — Process SCOWL → processed/scowl_tiers.json
Extract word → tier (size category). Map tiers to alias grade later.
Run from repo root or hesperia_lex: python3 hesperia_lex/scripts/preprocess_scowl.py
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

LEX_ROOT = Path(__file__).resolve().parent.parent
RAW = LEX_ROOT / "raw"
PROCESSED = LEX_ROOT / "processed"
PROCESSED.mkdir(parents=True, exist_ok=True)

# SCOWL size categories (10, 20, 35, 50, 60, 70, 80) — we map to tier number
TIER_FROM_NAME = {"10": 10, "20": 20, "35": 35, "50": 50, "60": 60, "70": 70, "80": 80}


def main() -> int:
    scowl_dir = RAW / "scowl-2020.12.07"
    if not scowl_dir.exists():
        scowl_dir = RAW / "scowl-2020.12.07"
    if not scowl_dir.exists():
        # Stub
        out = {"justice": {"tier": 50}, "dog": {"tier": 70}, "lie": {"tier": 50}}
        out_path = PROCESSED / "scowl_tiers.json"
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(out, f, indent=2)
        print("SCOWL dir not found; wrote stub", out_path, file=sys.stderr)
        return 0

    out: dict[str, dict] = {}
    for sub in scowl_dir.iterdir():
        if not sub.is_dir():
            continue
        tier = TIER_FROM_NAME.get(sub.name)
        if tier is None:
            continue
        for f in sub.rglob("*.txt"):
            try:
                for line in f.open(encoding="utf-8", errors="ignore"):
                    w = line.strip().lower()
                    if w and re.match(r"^[a-z][a-z0-9\-']*$", w):
                        out[w] = {"tier": tier}
            except Exception:
                pass

    if not out:
        out = {"justice": {"tier": 50}, "dog": {"tier": 70}, "lie": {"tier": 50}}

    out_path = PROCESSED / "scowl_tiers.json"
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2)
    print("Wrote", out_path, "entries:", len(out))
    return 0


if __name__ == "__main__":
    sys.exit(main())
