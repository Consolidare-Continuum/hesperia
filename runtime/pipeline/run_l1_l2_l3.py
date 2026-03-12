#!/usr/bin/env python3
"""
Run L1+L2 for baseline (B) and shadow (S), then L3. Output logged and reportable.
Usage: python3 -m runtime.pipeline.layers.run_l1_l2_l3 [--text_b "base"] [--text_s "shadow"] [--out path.json]
If only --text_b given, S uses same text (zero divergence expected).
"""

from __future__ import annotations

import argparse
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
    load_defaults,
)


def _run_l1_l2(text: str, assets: Path, dict_a: dict, dict_b: dict, defaults: dict):
    tokens = tokenize(normalize(text))
    matched, _ = attribute(tokens, dict_a, dict_b)
    F = int(defaults.get("F", 288))
    A = int(defaults.get("A", 12))
    eps = float(defaults.get("eps", 1e-9))
    MAX_ALLOWED_DEPTH = int(defaults.get("MAX_ALLOWED_DEPTH", 8))
    L1 = compute_L1(len(tokens), matched, F=F, A=A, eps=eps)
    hits = [0] * F
    for fg, _ in matched:
        if 0 <= fg < F:
            hits[fg] += 1
    adjacency = build_canonical_stub_adjacency(F, A)
    L2 = compute_L2(L1, hits, adjacency=adjacency, area=None, F=F, A=A, MAX_ALLOWED_DEPTH=MAX_ALLOWED_DEPTH, eps=eps)
    return L1, L2, hits


def main() -> None:
    ap = argparse.ArgumentParser(description="Run L1+L2 (B), L1+L2 (S), L3; output logged and reportable.")
    ap.add_argument("--text_b", type=str, default="justice lie fairness truth good order harm freedom")
    ap.add_argument("--text_s", type=str, default=None, help="Shadow text; if omitted, use text_b")
    ap.add_argument("--out", type=Path, default=None)
    args = ap.parse_args()
    text_s = args.text_s if args.text_s is not None else args.text_b

    assets = _HESPERIA / "lexicon" / "curated"
    dict_a = load_dict_a(assets_root=assets)
    dict_b = load_dict_b()
    if not dict_a:
        dict_a = {}
    defaults = load_defaults()

    L1_B, L2_B, hits_B = _run_l1_l2(args.text_b, assets, dict_a, dict_b, defaults)
    L1_S, L2_S, hits_S = _run_l1_l2(text_s, assets, dict_a, dict_b, defaults)

    F = int(defaults.get("F", 288))
    A = int(defaults.get("A", 12))
    L3 = compute_L3(
        L1_B, L2_B, hits_B,
        L1_S, L2_S, hits_S,
        F=F, A=A,
        SHADOW_MAX_DEVIATION=float(defaults.get("SHADOW_MAX_DEVIATION", 0.25)),
        SHADOW_MAX_CROSS_AREA_DELTA=float(defaults.get("SHADOW_MAX_CROSS_AREA_DELTA", 0.10)),
        SHADOW_ALLOW_AREA_FLIP=bool(defaults.get("SHADOW_ALLOW_AREA_FLIP", False)),
        TOP_K=int(defaults.get("TOP_K", 10)),
        eps=1e-12,
    )

    result = {
        "run": "L1+L2+L3",
        "text_b_preview": args.text_b[:80] + ("..." if len(args.text_b) > 80 else ""),
        "text_s_preview": text_s[:80] + ("..." if len(text_s) > 80 else ""),
        "L1_B": L1_B, "L2_B": L2_B,
        "L1_S": L1_S, "L2_S": L2_S,
        "L3": L3,
    }

    json_str = json.dumps(result, indent=2)
    if args.out:
        args.out.write_text(json_str, encoding="utf-8")
        print("L1+L2+L3 output written to", args.out, file=sys.stderr)
    print(json_str)
    print(
        "\n--- L3 reportable ---\n"
        f"SHADOW_DEVIATION_SCORE={L3['SHADOW_DEVIATION_SCORE']:.4f} SHADOW_ACCEPTABILITY_GATE={L3['SHADOW_ACCEPTABILITY_GATE']}",
        file=sys.stderr,
    )


if __name__ == "__main__":
    main()
