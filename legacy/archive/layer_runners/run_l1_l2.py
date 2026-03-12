#!/usr/bin/env python3

# HESPERIA — Reference Architecture Definition (RAD)
# Copyright © 2026 igareosh.com — Platonov Igor (aka @igareosh). All rights reserved.
# Restricted Research Disclosure License. Inspection and reference only.
# No reproduction, redistribution, or use without explicit written permission from the author.
# See LEGAL_NOTICE.md for full terms.

"""
Run L1 then L2 — output logged and reportable (standard: run layer math X → output → logged → reportable).
From CLIENTS/hesperia: python -m sphere_rag.layers.run_l1_l2 [--text "input"] [--out path.json]
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

# Run from CLIENTS/hesperia
_HERE = Path(__file__).resolve().parent
_HESPERIA = _HERE.parent.parent
if str(_HESPERIA) not in sys.path:
    sys.path.insert(0, str(_HESPERIA))

from sphere_rag.attribution_v033 import (
    attribute,
    load_dict_a_v033,
    load_dict_b_v033,
    normalize,
    tokenize,
)
from sphere_rag.layers import (
    build_canonical_stub_adjacency,
    compute_L1,
    compute_L2,
    load_defaults,
)


def main() -> None:
    ap = argparse.ArgumentParser(description="Run L1 + L2 layer math; output logged and reportable.")
    ap.add_argument("--text", type=str, default="justice lie fairness truth good order harm freedom")
    ap.add_argument("--out", type=Path, default=None, help="JSON output path (default: stdout + optional file)")
    ap.add_argument("--write", type=Path, default=None, help="Same as --out (write results to file)")
    args = ap.parse_args()
    out_path = args.out or args.write

    assets = _HESPERIA / "hesperia_lex" / "curated"
    dict_a = load_dict_a_v033(assets_root=assets)
    dict_b = load_dict_b_v033()
    if not dict_a:
        dict_a = {}

    text = args.text
    tokens = tokenize(normalize(text))
    matched, _ = attribute(tokens, dict_a, dict_b)

    defaults = load_defaults()
    F = int(defaults.get("F", 288))
    A = int(defaults.get("A", 12))
    eps = float(defaults.get("eps", 1e-9))
    MAX_ALLOWED_DEPTH = int(defaults.get("MAX_ALLOWED_DEPTH", 8))

    # L1
    L1 = compute_L1(
        len(tokens),
        matched,
        F=F,
        A=A,
        eps=eps,
    )

    # hits for L2: same as L1 internal notion
    hits = [0] * F
    for fg, _ in matched:
        if 0 <= fg < F:
            hits[fg] += 1

    adjacency = build_canonical_stub_adjacency(F, A)
    L2 = compute_L2(
        L1,
        hits,
        adjacency=adjacency,
        area=None,
        F=F,
        A=A,
        MAX_ALLOWED_DEPTH=MAX_ALLOWED_DEPTH,
        eps=eps,
    )

    result = {
        "run": "L1+L2",
        "text_preview": text[:80] + ("..." if len(text) > 80 else ""),
        "total_tokens": len(tokens),
        "matched_count": len(matched),
        "L1": L1,
        "L2": L2,
    }

    json_str = json.dumps(result, indent=2)
    if out_path:
        out_path.write_text(json_str, encoding="utf-8")
        print("L1+L2 output written to", out_path, file=sys.stderr)
    print(json_str)

    # Short reportable summary
    print(
        "\n--- reportable summary ---\n"
        f"L1: COVERAGE_RATIO={L1['COVERAGE_RATIO']:.4f} DOMINANT_FAMILY_ID={L1['DOMINANT_FAMILY_ID']} DOMINANT_AREA_ID={L1['DOMINANT_AREA_ID']}\n"
        f"L2: TOTAL_REACHABLE_NODES={L2['TOTAL_REACHABLE_NODES']} TRAVERSAL_DEPTH_REACHED={L2['TRAVERSAL_DEPTH_REACHED']} GEOMETRIC_STABILITY_INDEX={L2['GEOMETRIC_STABILITY_INDEX']:.4f}",
        file=sys.stderr,
    )


if __name__ == "__main__":
    main()
