# CONDITION_NUMBER (L6)

**Status:** 🟢 LIVE_FULL — matches proposal (if any), running in production path  
**Category:** [Stability and Control Theory](../categories/Stability-and-Control-Theory.md)  
**Type:** Layer variable  
**Responsible (module):** `core/layers/layer_6.py:52,91`  
**Value / default:** 1.0 (no-perturbation stub)

## In plain words

how ill-conditioned the hit/response surface looks — enters global stability; stubs to 1.0 when no perturbation data exists.

## Definition

- **Receives:** *none declared (constant, hub, or external)*
- **Does:** CONDITION_NUMBER — ill-conditioning proxy of the hit/response surface; enters GLOBAL_STABILITY_SCORE denominator.
- **Outputs:** `1.0 (no-perturbation stub)` → [LYAPUNOV_ESTIMATE / GLOBAL_STABILITY_SCORE](../pages/LYAPUNOV-ESTIMATE-GLOBAL-STABILITY-SCORE.md)
- **Exists for:** L6 ill-conditioning proxy

## Yields (formula)

CONDITION_NUMBER — ill-conditioning proxy of the hit/response surface; enters GLOBAL_STABILITY_SCORE denominator.

## Needed by (consumers)

- [LYAPUNOV_ESTIMATE / GLOBAL_STABILITY_SCORE](../pages/LYAPUNOV-ESTIMATE-GLOBAL-STABILITY-SCORE.md)

## See also

- [LYAPUNOV_ESTIMATE / GLOBAL_STABILITY_SCORE](../pages/LYAPUNOV-ESTIMATE-GLOBAL-STABILITY-SCORE.md)

## Origin

39_SPEC Layer-6 — Theory Explainer: plain_lang: how ill-conditioned the hit/response surface looks — enters global stability; stubs to 1.0 when no perturbation data exists. author: Hesperia wiki (core/layers/layer_6.py:52,91). extent: full. reasoning: L6 ill-conditioning proxy. application: [LYAPUNOV_ESTIMATE / GLOBAL_STABILITY_SCORE](../pages/LYAPUNOV-ESTIMATE-GLOBAL-STABILITY-SCORE.md).

## Notes

**HWIKI-PLAIN-C:** algebra plain_lang polished 2026-08-04. **HWIKI-PLAIN-B:** plain_lang backfilled from formula/notes 2026-08-04. **HWIKI-L6-01:** When no perturbation data, stubbed to 1.0. Downstream: GLOBAL_STABILITY_SCORE.

---
[← back to category](../categories/Stability-and-Control-Theory.md) · [wiki home](../index.md) · [Wire Map](Wiki-Wire-Map.md)
