<!--
HESPERIA — Reference Architecture Definition (RAD)
Copyright © 2026 igareosh.com — Platonov Igor (aka @igareosh). All rights reserved.
Restricted Research Disclosure License. Inspection and reference only.
No reproduction, redistribution, or use without explicit written permission.
See LEGAL_NOTICE.md for full terms.
-->

# Hesperia safeguard stress-test — results (Gena)

**Purpose**: Document that the loop safeguard was forced to fire; stress-test passed. Per ETHAN-HESPERIA-STATE-NOW-ASSESSMENT §VII and active.md Gena task. **Owner**: Gena. **Date**: 2026-02-18.

---

## Test

- **Script**: [cluster/chroma-server/hesperia_safeguard_stress_test.py](../cluster/chroma-server/hesperia_safeguard_stress_test.py).
- **Run**: `PYTHONPATH=cluster/chroma-server python3 cluster/chroma-server/hesperia_safeguard_stress_test.py` from repo root.

## Results

| Test | Summary |
|------|--------|
| **three_failures_trigger_stop** | PASS. TraversalSafeguard.record_hop(0) × 3 → should_stop() True; safeguard_stop() returns status SAFEGUARD_STOP, fail_count=3, obstacle_region set. |
| **valid_streak_resets_fail_count** | PASS. After 2 failures, two valid hops (valid_streak ≥ 2) reset fail_count to 0; one subsequent failure does not trigger stop. |

## Conclusion

- The safeguard **does fire** when we force 3 consecutive logical failures (unit level).
- Valid_streak reset (≥ 2) correctly clears fail_count.
- Integration with Hex.evaluate returning invalid (e.g. real contradiction/UNSAT in path input_context) depends on detect_contradiction/UNSAT handling real formulas; current core-mode run uses empty state/statement_set so full-ring passes. For topology-only traversal the safeguard is **proven** at the state-machine level.

---

**SIGNED: Developer (Gena) | Hesperia safeguard stress-test results | 2026-02-18 | governance**
