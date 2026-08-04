# MONOTONICITY_CHECK (L6)

**Status:** 🟢 LIVE_FULL — matches proposal (if any), running in production path  
**Category:** [Stability and Control Theory](../categories/Stability-and-Control-Theory.md)  
**Type:** Layer variable  
**Responsible (module):** `core/layers/layer_6.py:72,100`  
**Value / default:** True (no-perturbation stub)

## In plain words

whether activation mass decays monotonically across BFS depth — flags non-monotonic ladders.

## Definition

- **Receives:** *none declared (constant, hub, or external)*
- **Does:** MONOTONICITY_CHECK — whether mass [decay](../pages/decay.md) across BFS depth is monotonic (stub True, vacuously, without a real multi-sample trajectory to check).
- **Outputs:** `True (no-perturbation stub)` → [FIXED_POINT_DETECTION (L6)](../pages/FIXED-POINT-DETECTION-L6.md)
- **Exists for:** L6 Group-IV depth-ladder check

## Yields (formula)

MONOTONICITY_CHECK — whether mass [decay](../pages/decay.md) across BFS depth is monotonic (stub True, vacuously, without a real multi-sample trajectory to check).

## Needed by (consumers)

- [FIXED_POINT_DETECTION (L6)](../pages/FIXED-POINT-DETECTION-L6.md)

## See also

- [FIXED_POINT_DETECTION (L6)](../pages/FIXED-POINT-DETECTION-L6.md)

## Origin

39_SPEC Layer-6 — Theory Explainer: plain_lang: whether activation mass decays monotonically across BFS depth — flags non-monotonic ladders. author: Hesperia wiki (core/layers/layer_6.py:72,100). extent: full. reasoning: L6 Group-IV depth-ladder check. application: [FIXED_POINT_DETECTION (L6)](../pages/FIXED-POINT-DETECTION-L6.md).

## Notes

**HWIKI-PLAIN-C:** algebra plain_lang polished 2026-08-04. **HWIKI-PLAIN-B:** plain_lang backfilled from formula/notes 2026-08-04. **HWIKI-CATALOG-L6-GROUP-IV (2026-08-04):** Closes the Coverage-Ledger's named next-wave candidate — Group-IV scaffold constant, same status as the other 21 L6 stubs (`docs/foundations/output_catalog.md` §6: "documented no-perturbation identity constants... a named scaffold reserved for a future perturbation-analysis pass — not an oversight"). Verified against `layer_6.py` directly.

---
[← back to category](../categories/Stability-and-Control-Theory.md) · [wiki home](../index.md) · [Wire Map](Wiki-Wire-Map.md)
