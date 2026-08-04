# FIXED_POINT_DETECTION (L6)

**Status:** 🟢 LIVE_FULL — matches proposal (if any), running in production path  
**Category:** [Stability and Control Theory](../categories/Stability-and-Control-Theory.md)  
**Type:** Layer variable  
**Responsible (module):** `core/layers/layer_6.py:73,101`  
**Value / default:** True (no-perturbation stub)

## In plain words

whether the structural read has settled into a fixed point (no further meaningful change under the scaffold test).

## Definition

- **Receives:** [MONOTONICITY_CHECK (L6)](../pages/MONOTONICITY-CHECK-L6.md)
- **Does:** FIXED_POINT_DETECTION — whether the structural read has settled into a fixed point (stub True, vacuously, without a real iterative dynamical model).
- **Outputs:** `True (no-perturbation stub)` → [CYCLE_DETECTION_FUNCTIONAL (L6)](../pages/CYCLE-DETECTION-FUNCTIONAL-L6.md)
- **Exists for:** L6 Group-IV dynamical fixed-point flag

## Yields (formula)

FIXED_POINT_DETECTION — whether the structural read has settled into a fixed point (stub True, vacuously, without a real iterative dynamical model).

## Produced from (inputs)

- [MONOTONICITY_CHECK (L6)](../pages/MONOTONICITY-CHECK-L6.md)

## Needed by (consumers)

- [CYCLE_DETECTION_FUNCTIONAL (L6)](../pages/CYCLE-DETECTION-FUNCTIONAL-L6.md)

## See also

- [MONOTONICITY_CHECK (L6)](../pages/MONOTONICITY-CHECK-L6.md)
- [CYCLE_DETECTION_FUNCTIONAL (L6)](../pages/CYCLE-DETECTION-FUNCTIONAL-L6.md)

## Origin

39_SPEC Layer-6 — Theory Explainer: plain_lang: whether the structural read has settled into a fixed point (no further meaningful change under the scaffold test). author: Hesperia wiki (core/layers/layer_6.py:73,101). extent: full. reasoning: L6 Group-IV dynamical fixed-point flag. application: [CYCLE_DETECTION_FUNCTIONAL (L6)](../pages/CYCLE-DETECTION-FUNCTIONAL-L6.md).

## Notes

**HWIKI-PLAIN-C:** algebra plain_lang polished 2026-08-04. **HWIKI-PLAIN-B:** plain_lang backfilled from formula/notes 2026-08-04. **HWIKI-CATALOG-L6-GROUP-IV (2026-08-04):** Closes the Coverage-Ledger's named next-wave candidate — Group-IV scaffold constant, same status as the other 21 L6 stubs (`docs/foundations/output_catalog.md` §6: "documented no-perturbation identity constants... a named scaffold reserved for a future perturbation-analysis pass — not an oversight"). Verified against `layer_6.py` directly.

---
[← back to category](../categories/Stability-and-Control-Theory.md) · [wiki home](../index.md) · [Wire Map](Wiki-Wire-Map.md)
