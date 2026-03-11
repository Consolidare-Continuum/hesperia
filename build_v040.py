#!/usr/bin/env python3
"""Repository entrypoint for HESPERIA v0.4.0 build."""
from sphere_rag.build_v040 import run_build

if __name__ == "__main__":
    import argparse
    from pathlib import Path

    p = argparse.ArgumentParser(description="HESPERIA v0.4.0 build: Dict A → Dict B → surface")
    p.add_argument("--dict-a", type=Path, help="Path to Dict A (native or legacy)")
    p.add_argument("--assets-root", type=Path, help="Assets root (default: repo assets)")
    p.add_argument("--candidates", type=Path, help="Candidate tokens file (.txt or .json)")
    p.add_argument("--out-dir", type=Path, default=None, help="Output directory")
    p.add_argument("--mode", choices=["strict", "balanced", "exploratory"], default="balanced")
    p.add_argument("--allow-small-build", action="store_true", help="Allow build when covered families < 240")
    p.add_argument("--model-revision", type=str, required=True, help="Exact model revision pin (commit/tag)")
    args = p.parse_args()
    run_build(
        dict_a_path=args.dict_a,
        assets_root=args.assets_root,
        candidates_path=args.candidates,
        out_dir=args.out_dir,
        mode=args.mode,
        allow_small_build=args.allow_small_build,
        model_revision=args.model_revision,
    )
