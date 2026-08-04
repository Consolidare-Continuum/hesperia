# CONCEPTUAL_COHERENCE_INDEX (L6)

**Status:** 🟢 LIVE_FULL — matches proposal (if any), running in production path  
**Category:** [Stability and Control Theory](../categories/Stability-and-Control-Theory.md)  
**Type:** Layer variable  
**Responsible (module):** `core/layers/layer_6.py:78,105`  
**Value / default:** —

## In plain words

a single L6 coherence read: stability radius × (1 − family entropy) × global stability — high when the structure is both stable and focused.

## Definition

- **Receives:** [STABILITY_RADIUS (L6)](../pages/STABILITY-RADIUS-L6.md), [LYAPUNOV_ESTIMATE / GLOBAL_STABILITY_SCORE](../pages/LYAPUNOV-ESTIMATE-GLOBAL-STABILITY-SCORE.md)
- **Does:** CONCEPTUAL_COHERENCE_INDEX = STABILITY_RADIUS · (1 − [NORMALIZED_FAMILY_ENTROPY](../pages/NORMALIZED-FAMILY-ENTROPY.md)) · GLOBAL_STABILITY_SCORE.
- **Outputs:** `—` → *L7/L8 stability regime consumers*
- **Exists for:** combines STABILITY_RADIUS, L1 entropy, and GLOBAL_STABILITY_SCORE

## Yields (formula)

CONCEPTUAL_COHERENCE_INDEX = STABILITY_RADIUS · (1 − [NORMALIZED_FAMILY_ENTROPY](../pages/NORMALIZED-FAMILY-ENTROPY.md)) · GLOBAL_STABILITY_SCORE.

## Produced from (inputs)

- [STABILITY_RADIUS (L6)](../pages/STABILITY-RADIUS-L6.md)
- [LYAPUNOV_ESTIMATE / GLOBAL_STABILITY_SCORE](../pages/LYAPUNOV-ESTIMATE-GLOBAL-STABILITY-SCORE.md)

## Needed by (consumers)

- *L7/L8 stability regime consumers*

## See also

- [STABILITY_RADIUS (L6)](../pages/STABILITY-RADIUS-L6.md)
- [LYAPUNOV_ESTIMATE / GLOBAL_STABILITY_SCORE](../pages/LYAPUNOV-ESTIMATE-GLOBAL-STABILITY-SCORE.md)

## Origin

39_SPEC Layer-6 — Theory Explainer: plain_lang: a single L6 coherence read: stability radius × (1 − family entropy) × global stability — high when the structure is both stable and focused. author: Hesperia wiki (core/layers/layer_6.py:78,105). extent: full. reasoning: combines STABILITY_RADIUS, L1 entropy, and GLOBAL_STABILITY_SCORE. application: *L7/L8 stability regime consumers*.

## Notes

**HWIKI-PLAIN-C:** algebra plain_lang polished 2026-08-04. **HWIKI-PLAIN-B:** plain_lang backfilled from formula/notes 2026-08-04. **HWIKI-L6-01:** Combines stability radius, L1 family entropy, and GLOBAL_STABILITY_SCORE.

---
[← back to category](../categories/Stability-and-Control-Theory.md) · [wiki home](../index.md) · [Wire Map](Wiki-Wire-Map.md)
