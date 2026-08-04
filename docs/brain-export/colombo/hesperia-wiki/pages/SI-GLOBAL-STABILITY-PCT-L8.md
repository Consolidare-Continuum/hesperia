# SI_GLOBAL_STABILITY_PCT (L8)

**Status:** 🟢 LIVE_FULL — matches proposal (if any), running in production path  
**Category:** [Evidence and Trust](../categories/Evidence-and-Trust.md)  
**Type:** Scaled indicator  
**Responsible (module):** `core/layers/layer_8.py:49`  
**Value / default:** 0–100%

## In plain words

same L6 global stability, published as a percent (0–100) twin of the U1000 form.

## Definition

- **Receives:** [LYAPUNOV_ESTIMATE / GLOBAL_STABILITY_SCORE](../pages/LYAPUNOV-ESTIMATE-GLOBAL-STABILITY-SCORE.md), [SI_GLOBAL_STABILITY_U1000 (L8)](../pages/SI-GLOBAL-STABILITY-U1000-L8.md)
- **Does:** SI_GLOBAL_STABILITY_PCT = _ratio_to_pct(l6[GLOBAL_STABILITY_SCORE]).
- **Outputs:** `0–100%` → [SI_SYSTEM_CONFIDENCE_PCT (L8)](../pages/SI-SYSTEM-CONFIDENCE-PCT-L8.md)
- **Exists for:** percent twin of SI_GLOBAL_STABILITY_U1000

## Yields (formula)

SI_GLOBAL_STABILITY_PCT = _ratio_to_pct(l6[GLOBAL_STABILITY_SCORE]).

## Produced from (inputs)

- [LYAPUNOV_ESTIMATE / GLOBAL_STABILITY_SCORE](../pages/LYAPUNOV-ESTIMATE-GLOBAL-STABILITY-SCORE.md)
- [SI_GLOBAL_STABILITY_U1000 (L8)](../pages/SI-GLOBAL-STABILITY-U1000-L8.md)

## Needed by (consumers)

- [SI_SYSTEM_CONFIDENCE_PCT (L8)](../pages/SI-SYSTEM-CONFIDENCE-PCT-L8.md)

## See also

- [LYAPUNOV_ESTIMATE / GLOBAL_STABILITY_SCORE](../pages/LYAPUNOV-ESTIMATE-GLOBAL-STABILITY-SCORE.md)
- [SI_GLOBAL_STABILITY_U1000 (L8)](../pages/SI-GLOBAL-STABILITY-U1000-L8.md)
- [SI_SYSTEM_CONFIDENCE_PCT (L8)](../pages/SI-SYSTEM-CONFIDENCE-PCT-L8.md)
- [SYSTEM_CONFIDENCE_SCORE (L7)](../pages/SYSTEM-CONFIDENCE-SCORE-L7.md)
- [CONSIST_STABILITY_REGIME_VALID (L7)](../pages/CONSIST-STABILITY-REGIME-VALID-L7.md)
- [STABILITY_CURRENT_THRESHOLD / STABILITY_STALE_THRESHOLD](../pages/STABILITY-CURRENT-THRESHOLD-STABILITY-STALE-THRESHOLD.md)

## Origin

41_SPEC Layer-8 — Theory Explainer: plain_lang: same L6 global stability, published as a percent (0–100) twin of the U1000 form. author: Hesperia wiki (core/layers/layer_8.py:49). extent: full. reasoning: percent twin of SI_GLOBAL_STABILITY_U1000. application: [SI_SYSTEM_CONFIDENCE_PCT (L8)](../pages/SI-SYSTEM-CONFIDENCE-PCT-L8.md).

## Notes

**HWIKI-PLAIN-C:** algebra plain_lang polished 2026-08-04. **HWIKI-PLAIN-B:** plain_lang backfilled from formula/notes 2026-08-04. **HWIKI-L8-01:** Percent twin of SI_GLOBAL_STABILITY_U1000.

---
[← back to category](../categories/Evidence-and-Trust.md) · [wiki home](../index.md) · [Wire Map](Wiki-Wire-Map.md)
