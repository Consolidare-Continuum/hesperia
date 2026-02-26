#!/usr/bin/env python3
"""
HESPERIA v0.5 — Operational verification (dense mode).
Run in production API env or with same venv + PYTHONPATH as API.
Sets HESPERIA_ATTRIBUTION_MODE=dense before import, then:
  1. Unknown-token test: "randomwordthatneverexisted" → must succeed (200/dense), not 400 (sparse vacuum).
  2. Vacuum-elimination test: "architecture and symbolism influence belief systems" → 200, coverage ≈ 1.0.
  3. Shadow differential: same sentence base vs shadow → metrics must differ.
Exit 0 = all pass; non-zero = fail.
"""
from __future__ import annotations

import os
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
os.environ["HESPERIA_ATTRIBUTION_MODE"] = "dense"
if str(REPO) not in sys.path:
    sys.path.insert(0, str(REPO))


def main() -> int:
    from sphere_rag.analyze_v033 import analyze_v033

    failures = []

    # 1. Unknown-token test: dense must return 200 (no vacuum); sparse would 400
    try:
        minimal, extended = analyze_v033("randomwordthatneverexisted", assets_root=REPO / "hesperia_lex" / "frozen")
        if minimal.get("dominant_area") is None and minimal.get("dominant_family") is None:
            failures.append("1. Unknown token: got None dominant (sparse fallback?)")
        else:
            print("1. Unknown-token test: PASS (200/dense — no vacuum)")
    except ValueError as e:
        if "semantic_vacuum" in str(e):
            failures.append(f"1. Unknown-token test: FAIL — semantic_vacuum (sparse path active): {e}")
        else:
            failures.append(f"1. Unknown-token test: FAIL — {e}")
    except Exception as e:
        failures.append(f"1. Unknown-token test: FAIL — {type(e).__name__}: {e}")

    # 2. Vacuum-elimination test: previously vacuum sentence must 200, coverage ≈ 1.0
    try:
        minimal, extended = analyze_v033(
            "architecture and symbolism influence belief systems",
            assets_root=REPO / "hesperia_lex" / "frozen",
        )
        cov = extended.get("attribution_coverage")
        if cov is None:
            failures.append("2. Vacuum-elimination: no attribution_coverage in extended")
        elif abs(float(cov) - 1.0) > 0.01:
            failures.append(f"2. Vacuum-elimination: coverage={cov} (expected ≈1.0)")
        else:
            print("2. Vacuum-elimination test: PASS (200, coverage ≈ 1.0)")
    except ValueError as e:
        if "semantic_vacuum" in str(e):
            failures.append(f"2. Vacuum-elimination: FAIL — still vacuum: {e}")
        else:
            failures.append(f"2. Vacuum-elimination: FAIL — {e}")
    except Exception as e:
        failures.append(f"2. Vacuum-elimination: FAIL — {type(e).__name__}: {e}")

    # 3. Shadow differential: base vs shadow — expect different metrics when core math uses seed/traversal
    sentence = "Altruism and trust strengthen mutual care within communities."
    try:
        min_base, ext_base = analyze_v033(sentence, shadow_enabled=False, assets_root=REPO / "hesperia_lex" / "frozen")
        min_shadow, ext_shadow = analyze_v033(sentence, shadow_enabled=True, assets_root=REPO / "hesperia_lex" / "frozen")
        same = (
            min_base.get("governance") == min_shadow.get("governance")
            and min_base.get("loopability") == min_shadow.get("loopability")
            and min_base.get("tension_energy") == min_shadow.get("tension_energy")
            and min_base.get("obstacle_score") == min_shadow.get("obstacle_score")
        )
        if same:
            failures.append("3. Shadow differential: base and shadow metrics identical")
        else:
            print("3. Shadow differential test: PASS (measurable deltas)")
    except Exception as e:
        failures.append(f"3. Shadow differential: FAIL — {type(e).__name__}: {e}")

    if failures:
        for f in failures:
            print(f"FAIL: {f}", file=sys.stderr)
        return 1
    print("All v0.5 operational checks passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
