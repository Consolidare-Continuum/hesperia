#!/usr/bin/env python3
"""
Canonical pipeline CLI: delegates to sphere.pipeline.run_pipeline.
Use this as the reference entrypoint for L1–L10 + USF + propagation + guards.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))


def main() -> None:
    ap = argparse.ArgumentParser(
        description="Run canonical HESPERIA pipeline (sphere.pipeline.run_pipeline)"
    )
    ap.add_argument(
        "--text",
        default="justice lie fairness truth good order harm freedom",
        help="Input text to process",
    )
    ap.add_argument("--out", type=Path, default=None, help="Write full result JSON to path")
    ap.add_argument(
        "--document-id",
        default="reference",
        help="Document ID for USF",
    )
    ap.add_argument(
        "--assets-root",
        type=Path,
        default=None,
        help="Lexicon/curated assets root (default: repo/lexicon/curated)",
    )
    ap.add_argument(
        "--topology-data-root",
        type=Path,
        default=None,
        help="Topology data root for adjacency and family→area (optional)",
    )
    args = ap.parse_args()

    config = {
        "pipeline_version": "v1",
        "deterministic": True,
        "assets_root": args.assets_root or (ROOT / "lexicon" / "curated"),
    }
    if args.topology_data_root is not None:
        config["topology_data_root"] = args.topology_data_root

    from sphere.pipeline.pipeline_runner import run_pipeline

    result = run_pipeline(
        args.text,
        config,
        document_id=args.document_id,
    )

    j = json.dumps(result, indent=2)
    if args.out:
        args.out.write_text(j, encoding="utf-8")
        print("Output written to", args.out, file=sys.stderr)
    print(j)


if __name__ == "__main__":
    main()
