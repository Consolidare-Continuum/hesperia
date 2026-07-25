# CONDITION_NUMBER (L6)

**Status:** 🟢 LIVE_FULL — matches proposal (if any), running in production path  
**Category:** [Stability and Control Theory](../categories/Stability-and-Control-Theory.md)  
**Type:** Layer variable  
**Responsible (module):** `core/layers/layer_6.py:52,91`  
**Value / default:** 1.0 (no-perturbation stub)

## Yields (formula)

CONDITION_NUMBER — ill-conditioning proxy of the hit/response surface; enters GLOBAL_STABILITY_SCORE denominator.

## Needed by (consumers)

- [LYAPUNOV_ESTIMATE / GLOBAL_STABILITY_SCORE](../pages/LYAPUNOV-ESTIMATE-GLOBAL-STABILITY-SCORE.md)

## Origin

39_SPEC Layer-6

## Notes

**HWIKI-L6-01:** When no perturbation data, stubbed to 1.0. Downstream: GLOBAL_STABILITY_SCORE.

---
[← back to category](../categories/Stability-and-Control-Theory.md) · [wiki home](../index.md)
