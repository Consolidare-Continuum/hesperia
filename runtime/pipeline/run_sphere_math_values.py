#!/usr/bin/env python3
"""
Run all sphere math (L1–L9) and write one clean output file: values only, no commentary.
Usage: python3 -m runtime.pipeline.layers.run_sphere_math_values [--out path.json] [--profile path] [--text "input"]
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

_HERE = Path(__file__).resolve().parent
_HESPERIA = _HERE.parents[1]
if str(_HESPERIA) not in sys.path:
    sys.path.insert(0, str(_HESPERIA))

from core.attribution.structural import (
    attribute,
    load_dict_a,
    load_dict_b,
    normalize,
    tokenize,
)
from core.layers import (
    build_canonical_stub_adjacency,
    compute_L1,
    compute_L2,
    compute_L3,
    compute_L4,
    compute_L5,
    compute_L6,
    compute_L7,
    compute_L8,
    compute_L9,
    load_defaults,
    load_structure_profile,
)


def _round_floats(obj, ndigits=6):
    if isinstance(obj, float):
        return round(obj, ndigits)
    if isinstance(obj, dict):
        return {k: _round_floats(v, ndigits) for k, v in obj.items()}
    if isinstance(obj, list):
        return [_round_floats(x, ndigits) for x in obj]
    return obj


def main():
    import argparse
    ap = argparse.ArgumentParser(description="Run sphere math, write one values-only JSON.")
    ap.add_argument("--out", type=Path, default=_HESPERIA / "sphere_math_values.json")
    ap.add_argument("--profile", type=Path, default=None)
    ap.add_argument("--text", default="justice lie fairness truth good order harm freedom")
    args = ap.parse_args()

    assets = _HESPERIA / "lexicon" / "curated"
    dict_a = load_dict_a(assets_root=assets) or {}
    dict_b = load_dict_b()
    defaults = load_defaults()
    F = int(defaults.get("F", 288))
    A = int(defaults.get("A", 12))
    eps = float(defaults.get("eps", 1e-9))
    D = int(defaults.get("MAX_ALLOWED_DEPTH", 8))

    profile_id = None
    profile = None
    if args.profile and args.profile.exists():
        profile, _ = load_structure_profile(args.profile, F=F, A=A)
        profile_id = profile.get("profile_name") or profile.get("profile_version") or args.profile.stem

    tokens = tokenize(normalize(args.text))
    matched, _ = attribute(tokens, dict_a, dict_b)
    L1 = compute_L1(len(tokens), matched, F=F, A=A, eps=eps, profile_id=profile_id, profile=profile)
    hits = [0] * F
    for fg, _ in matched:
        if 0 <= fg < F:
            hits[fg] += 1
    adj = build_canonical_stub_adjacency(F, A)
    L2 = compute_L2(L1, hits, adjacency=adj, F=F, A=A, MAX_ALLOWED_DEPTH=D, eps=eps)
    visited_B = set(L2.get("VISITED_IDS", []))
    L1_S, L2_S, hits_S = L1, L2, hits[:]
    L3 = compute_L3(L1, L2, hits, L1_S, L2_S, hits_S, F=F, A=A, eps=1e-12, **{
        k: defaults.get(k) for k in ("SHADOW_MAX_DEVIATION", "SHADOW_MAX_CROSS_AREA_DELTA", "SHADOW_ALLOW_AREA_FLIP", "TOP_K") if k in defaults
    })
    R_B, R_S = [], []
    L4 = compute_L4(L1, L1_S, hits, hits_S, R_B, R_S, F=F, A=A, **{
        k: defaults.get(k) for k in ("RETRIEVAL_MODE_ID", "TOP_K", "MAX_SHORTFALL", "MIN_SUPPORT", "MAX_DUP_BOOK_CONC") if k in defaults
    })
    L5 = compute_L5(L1, L4, R_B, [], F=F, A=A, TOP_K=defaults.get("TOP_K", 20), MAX_SHORTFALL=defaults.get("MAX_SHORTFALL", 2), MAX_CONTRADICTION=defaults.get("MAX_CONTRADICTION", 0.50))
    L6 = compute_L6(L1, L2, F=F)
    L7 = compute_L7(L1, L2, L3, L4, L5, L6, visited_B=visited_B, F=F, A=A, **{
        k: defaults.get(k) for k in ("MIN_COVERAGE_RATIO", "MAX_CROSS_AREA_RATIO", "MAX_LYAPUNOV", "HIGH_CONF", "MED_CONF", "MIN_PCS") if k in defaults
    })
    L8 = compute_L8(L1, L2, L3, L4, L5, L6, L7)
    L9 = compute_L9(L3, L4, L7, L8, MAX_SHORTFALL=defaults.get("MAX_SHORTFALL", 2))

    out = {
        "input": {"token_count": len(tokens), "text_preview": args.text[:80]},
        "L1": _round_floats(L1),
        "L2": _round_floats(L2),
        "L3": _round_floats(L3),
        "L4": _round_floats(L4),
        "L5": _round_floats(L5),
        "L6": _round_floats(L6),
        "L7": _round_floats(L7),
        "L8": _round_floats(L8),
        "L9": _round_floats(L9),
    }
    path = Path(args.out)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(out, indent=2), encoding="utf-8")
    if sys.stdout.isatty():
        print(path.resolve(), file=sys.stderr)


if __name__ == "__main__":
    main()
