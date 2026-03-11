#!/usr/bin/env python3
"""Run L1..L9: attribution→L1→…→L9. L8 = SI_* units; L9 = branding. Output logged and reportable. Usage: python3 -m sphere_rag.layers.run_l1_through_l9 [--out path.json]"""
from __future__ import annotations
import argparse
import json
import sys
from pathlib import Path

_HERE = Path(__file__).resolve().parent
_HESPERIA = _HERE.parent.parent
if str(_HESPERIA) not in sys.path:
    sys.path.insert(0, str(_HESPERIA))

from sphere_rag.attribution_v033 import attribute, load_dict_a_v033, load_dict_b_v033, normalize, tokenize
from sphere_rag.layers import (
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
)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--text", default="justice lie fairness truth good order harm freedom")
    ap.add_argument("--out", type=Path, default=None)
    args = ap.parse_args()
    assets = _HESPERIA / "hesperia_lex" / "curated"
    dict_a = load_dict_a_v033(assets_root=assets) or {}
    dict_b = load_dict_b_v033()
    defaults = load_defaults()
    F = int(defaults.get("F", 288))
    A = int(defaults.get("A", 12))
    eps = float(defaults.get("eps", 1e-9))
    D = int(defaults.get("MAX_ALLOWED_DEPTH", 8))

    tokens = tokenize(normalize(args.text))
    matched, _ = attribute(tokens, dict_a, dict_b)
    L1 = compute_L1(len(tokens), matched, F=F, A=A, eps=eps)
    hits = [0] * F
    for fg, _ in matched:
        if 0 <= fg < F:
            hits[fg] += 1
    adj = build_canonical_stub_adjacency(F, A)
    L2 = compute_L2(L1, hits, adjacency=adj, F=F, A=A, MAX_ALLOWED_DEPTH=D, eps=eps)
    visited_B = set(L2.get("VISITED_IDS", []))

    L1_S, L2_S, hits_S = L1, L2, hits[:]
    L3 = compute_L3(L1, L2, hits, L1_S, L2_S, hits_S, F=F, A=A, eps=1e-12, **{k: defaults.get(k) for k in ("SHADOW_MAX_DEVIATION", "SHADOW_MAX_CROSS_AREA_DELTA", "SHADOW_ALLOW_AREA_FLIP", "TOP_K") if k in defaults})
    R_B, R_S = [], []
    L4 = compute_L4(L1, L1_S, hits, hits_S, R_B, R_S, F=F, A=A, **{k: defaults.get(k) for k in ("RETRIEVAL_MODE_ID", "TOP_K", "MAX_SHORTFALL", "MIN_SUPPORT", "MAX_DUP_BOOK_CONC") if k in defaults})
    L5 = compute_L5(L1, L4, R_B, [], F=F, A=A, TOP_K=defaults.get("TOP_K", 20), MAX_SHORTFALL=defaults.get("MAX_SHORTFALL", 2), MAX_CONTRADICTION=defaults.get("MAX_CONTRADICTION", 0.50))
    L6 = compute_L6(L1, L2, F=F)
    L7 = compute_L7(L1, L2, L3, L4, L5, L6, visited_B=visited_B, F=F, A=A, **{k: defaults.get(k) for k in ("MIN_COVERAGE_RATIO", "MAX_CROSS_AREA_RATIO", "MAX_LYAPUNOV", "HIGH_CONF", "MED_CONF") if k in defaults})
    L8 = compute_L8(L1, L2, L3, L4, L5, L6, L7)
    L9 = compute_L9(L3, L4, L7, L8, MAX_SHORTFALL=defaults.get("MAX_SHORTFALL", 2))

    out = {"run": "L1_through_L9", "text_preview": args.text[:80], "L1": L1, "L2": L2, "L3": L3, "L4": L4, "L5": L5, "L6": L6, "L7": L7, "L8": L8, "L9": L9}
    j = json.dumps(out, indent=2)
    if args.out:
        args.out.write_text(j, encoding="utf-8")
        print("Output written to", args.out, file=sys.stderr)
    print(j)
    print("--- reportable --- L7 DECISION_STATUS_CODE:", L7["DECISION_STATUS_CODE"], "OUTPUT_TRUST_TAG:", L7["OUTPUT_TRUST_TAG"], "L9 BRAND_WORD_TRUST:", L9["BRAND_WORD_TRUST"], file=sys.stderr)


if __name__ == "__main__":
    main()
