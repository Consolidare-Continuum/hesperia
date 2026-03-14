#!/usr/bin/env python3
# HESPERIA — Thin wrapper over analysis service. No direct layer import.
# Copyright © 2026 igareosh.com. See LEGAL_NOTICE.md.

"""Public entry point: structural analysis (L1+L2+L3 only). Delegates to core.services.analysis_service only."""
from __future__ import annotations

import json
import sys
from pathlib import Path

_HERE = Path(__file__).resolve().parent
_HESPERIA = _HERE.parents[1]
if str(_HESPERIA) not in sys.path:
    sys.path.insert(0, str(_HESPERIA))


def main() -> None:
    import argparse
    from core.services.analysis_service import run_structural_analysis
    from runtime.artifact_writer import write_public_json

    ap = argparse.ArgumentParser(description="Run structural analysis (L1+L2+L3 stages).")
    ap.add_argument("--text", type=str, default="justice lie fairness truth good order harm freedom")
    ap.add_argument("--text-s", type=str, default=None)
    ap.add_argument("--out", type=Path, default=None)
    args = ap.parse_args()
    text_s = args.text_s or args.text

    assets = _HESPERIA / "lexicon" / "curated"
    out = run_structural_analysis(args.text, assets_root=assets, stages="L1_L2_L3")
    if args.out:
        write_public_json(args.out, out)
        print("L1+L2+L3 output written to", args.out, file=sys.stderr)
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
