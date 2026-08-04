# SYSTEM_CONFIDENCE_SCORE (L7)

**Status:** 🟢 LIVE_FULL — matches proposal (if any), running in production path  
**Category:** [Evidence and Trust](../categories/Evidence-and-Trust.md)  
**Type:** Layer variable  
**Responsible (module):** `core/layers/layer_7.py (~conf product; out SYSTEM_CONFIDENCE_SCORE)`  
**Value / default:** clamp01 product

## In plain words

L7's overall confidence that the structural read is trustworthy — folds consistency gates and includes L6 global stability.

## Definition

- **Receives:** [LYAPUNOV_ESTIMATE / GLOBAL_STABILITY_SCORE](../pages/LYAPUNOV-ESTIMATE-GLOBAL-STABILITY-SCORE.md), [CONSIST_STABILITY_REGIME_VALID (L7)](../pages/CONSIST-STABILITY-REGIME-VALID-L7.md)
- **Does:** SYSTEM_CONFIDENCE_SCORE folds L1–L6 consistency gates and includes l6[GLOBAL_STABILITY_SCORE] in the confidence product path.
- **Outputs:** `clamp01 product` → [SI_SYSTEM_CONFIDENCE_U1000 (L8)](../pages/SI-SYSTEM-CONFIDENCE-U1000-L8.md), [SI_SYSTEM_CONFIDENCE_PCT (L8)](../pages/SI-SYSTEM-CONFIDENCE-PCT-L8.md), *L9 pillars*
- **Exists for:** primary L7 consumer of GLOBAL_STABILITY_SCORE

## Yields (formula)

SYSTEM_CONFIDENCE_SCORE folds L1–L6 consistency gates and includes l6[GLOBAL_STABILITY_SCORE] in the confidence product path.

## Produced from (inputs)

- [LYAPUNOV_ESTIMATE / GLOBAL_STABILITY_SCORE](../pages/LYAPUNOV-ESTIMATE-GLOBAL-STABILITY-SCORE.md)
- [CONSIST_STABILITY_REGIME_VALID (L7)](../pages/CONSIST-STABILITY-REGIME-VALID-L7.md)

## Needed by (consumers)

- [SI_SYSTEM_CONFIDENCE_U1000 (L8)](../pages/SI-SYSTEM-CONFIDENCE-U1000-L8.md)
- [SI_SYSTEM_CONFIDENCE_PCT (L8)](../pages/SI-SYSTEM-CONFIDENCE-PCT-L8.md)
- *L9 pillars*

## See also

- [LYAPUNOV_ESTIMATE / GLOBAL_STABILITY_SCORE](../pages/LYAPUNOV-ESTIMATE-GLOBAL-STABILITY-SCORE.md)
- [CONSIST_STABILITY_REGIME_VALID (L7)](../pages/CONSIST-STABILITY-REGIME-VALID-L7.md)
- [SI_SYSTEM_CONFIDENCE_U1000 (L8)](../pages/SI-SYSTEM-CONFIDENCE-U1000-L8.md)
- [SI_SYSTEM_CONFIDENCE_PCT (L8)](../pages/SI-SYSTEM-CONFIDENCE-PCT-L8.md)
- [SI_GLOBAL_STABILITY_U1000 (L8)](../pages/SI-GLOBAL-STABILITY-U1000-L8.md)
- [SI_GLOBAL_STABILITY_PCT (L8)](../pages/SI-GLOBAL-STABILITY-PCT-L8.md)
- [STABILITY_CURRENT_THRESHOLD / STABILITY_STALE_THRESHOLD](../pages/STABILITY-CURRENT-THRESHOLD-STABILITY-STALE-THRESHOLD.md)

## Origin

40_SPEC Layer-7 — Theory Explainer: plain_lang: L7's overall confidence that the structural read is trustworthy — folds consistency gates and includes L6 global stability. author: Hesperia wiki (core/layers/layer_7.py (~conf product; out SYSTEM_CONFIDENCE_SCORE)). extent: full. reasoning: primary L7 consumer of GLOBAL_STABILITY_SCORE. application: [SI_SYSTEM_CONFIDENCE_U1000 (L8)](../pages/SI-SYSTEM-CONFIDENCE-U1000-L8.md), [SI_SYSTEM_CONFIDENCE_PCT (L8)](../pages/SI-SYSTEM-CONFIDENCE-PCT-L8.md), *L9 pillars*.

## Notes

**HWIKI-PLAIN-C:** algebra plain_lang polished 2026-08-04. **HWIKI-PLAIN-B:** plain_lang backfilled from formula/notes 2026-08-04. **HWIKI-L7-01:** Primary L7 consumer of GLOBAL_STABILITY_SCORE — not a full L7 census; slice is stability→confidence only.

---
[← back to category](../categories/Evidence-and-Trust.md) · [wiki home](../index.md) · [Wire Map](Wiki-Wire-Map.md)
