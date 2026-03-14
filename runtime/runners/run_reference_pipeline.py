#!/usr/bin/env python3
# HESPERIA — Thin wrapper over analysis service. No direct pipeline import.
# Copyright © 2026 igareosh.com. See LEGAL_NOTICE.md.

"""Public entry point: structural analysis. Delegates to runtime.services.analysis_service only."""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))


def main() -> None:
    import argparse
    from runtime.services.analysis_service import run_structural_analysis
    from runtime.artifact_writer import write_public_json

    ap = argparse.ArgumentParser(description="Run structural analysis (canonical entry point).")
    ap.add_argument("--text", default="justice lie fairness truth good order harm freedom")
    ap.add_argument("--out", type=Path, default=None)
    ap.add_argument("--document-id", default="reference")
    ap.add_argument("--assets-root", type=Path, default=None)
    ap.add_argument("--policy-mode", dest="policy_mode", default=None)
    args = ap.parse_args()

    out = run_structural_analysis(
        args.text,
        assets_root=args.assets_root or (ROOT / "lexicon" / "curated"),
        policy_mode=args.policy_mode,
        stages="full",
    )
    if args.out:
        write_public_json(args.out, out)
        print("Output written to", args.out, file=sys.stderr)
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
