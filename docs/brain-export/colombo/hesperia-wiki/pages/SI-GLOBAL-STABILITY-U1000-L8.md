# SI_GLOBAL_STABILITY_U1000 (L8)

**Status:** 🟢 LIVE_FULL — matches proposal (if any), running in production path  
**Category:** [Evidence and Trust](../categories/Evidence-and-Trust.md)  
**Type:** Scaled indicator  
**Responsible (module):** `core/layers/layer_8.py:48`  
**Value / default:** 0–1000

## In plain words

publish L6's global stability score on the 0–1000 unit scale so L9 and humans never see the raw ratio.

## Definition

- **Receives:** [LYAPUNOV_ESTIMATE / GLOBAL_STABILITY_SCORE](../pages/LYAPUNOV-ESTIMATE-GLOBAL-STABILITY-SCORE.md)
- **Does:** SI_GLOBAL_STABILITY_U1000 = _ratio_to_u1000(l6[GLOBAL_STABILITY_SCORE]) — scaled publish of L6 global stability.
- **Outputs:** `0–1000` → [SI_GLOBAL_STABILITY_PCT (L8)](../pages/SI-GLOBAL-STABILITY-PCT-L8.md)
- **Exists for:** L8 rescale consumer of GLOBAL_STABILITY_SCORE

## Yields (formula)

SI_GLOBAL_STABILITY_U1000 = _ratio_to_u1000(l6[GLOBAL_STABILITY_SCORE]) — scaled publish of L6 global stability.

## Produced from (inputs)

- [LYAPUNOV_ESTIMATE / GLOBAL_STABILITY_SCORE](../pages/LYAPUNOV-ESTIMATE-GLOBAL-STABILITY-SCORE.md)

## Needed by (consumers)

- [SI_GLOBAL_STABILITY_PCT (L8)](../pages/SI-GLOBAL-STABILITY-PCT-L8.md)

## See also

- [LYAPUNOV_ESTIMATE / GLOBAL_STABILITY_SCORE](../pages/LYAPUNOV-ESTIMATE-GLOBAL-STABILITY-SCORE.md)
- [SI_GLOBAL_STABILITY_PCT (L8)](../pages/SI-GLOBAL-STABILITY-PCT-L8.md)
- [SYSTEM_CONFIDENCE_SCORE (L7)](../pages/SYSTEM-CONFIDENCE-SCORE-L7.md)
- [CONSIST_STABILITY_REGIME_VALID (L7)](../pages/CONSIST-STABILITY-REGIME-VALID-L7.md)
- [STABILITY_CURRENT_THRESHOLD / STABILITY_STALE_THRESHOLD](../pages/STABILITY-CURRENT-THRESHOLD-STABILITY-STALE-THRESHOLD.md)

## Origin

41_SPEC Layer-8 — Theory Explainer: plain_lang: publish L6's global stability score on the 0–1000 unit scale so L9 and humans never see the raw ratio. author: Hesperia wiki (core/layers/layer_8.py:48). extent: full. reasoning: L8 rescale consumer of GLOBAL_STABILITY_SCORE. application: [SI_GLOBAL_STABILITY_PCT (L8)](../pages/SI-GLOBAL-STABILITY-PCT-L8.md).

## Notes

**HWIKI-PLAIN-C:** algebra plain_lang polished 2026-08-04. **HWIKI-PLAIN-B:** plain_lang backfilled from formula/notes 2026-08-04. **HWIKI-L8-01:** Direct L8 scaled consumer of GLOBAL_STABILITY_SCORE.

---
[← back to category](../categories/Evidence-and-Trust.md) · [wiki home](../index.md) · [Wire Map](Wiki-Wire-Map.md)
