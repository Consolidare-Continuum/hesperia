#!/usr/bin/env python3
"""
HESPERIA v0.5 — Determinism verification for dense projection.
Run fixed sentence 10 times; assert identical output within 1e-9 tolerance.
"""
from __future__ import annotations

import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
if str(REPO) not in sys.path:
    sys.path.insert(0, str(REPO))

FIXED_SENTENCE = "Altruism and trust reinforce social care and protection within a community."
N_RUNS = 10
TOL = 1e-9


def main() -> int:
    import os
    os.environ.setdefault("HESPERIA_ATTRIBUTION_MODE", "dense")
    from sphere_rag.analyze_v033 import analyze_v033
    first: dict | None = None
    for _ in range(N_RUNS):
        minimal, extended = analyze_v033(FIXED_SENTENCE, assets_root=REPO / "hesperia_lex" / "frozen")
        if first is None:
            first = {**minimal, **extended}
            continue
        for key in first:
            a = first.get(key)
            b = minimal.get(key) if key in minimal else extended.get(key)
            if isinstance(a, (int, float)) and isinstance(b, (int, float)):
                if abs(float(a) - float(b)) > TOL:
                    print(f"FAIL: {key} differs: {a} vs {b}", file=sys.stderr)
                    return 1
            elif a != b:
                print(f"FAIL: {key} differs: {a} vs {b}", file=sys.stderr)
                return 1
    print("PASS: 10 runs identical within tolerance")
    return 0


if __name__ == "__main__":
    sys.exit(main())
