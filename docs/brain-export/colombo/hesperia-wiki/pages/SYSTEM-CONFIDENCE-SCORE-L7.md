# SYSTEM_CONFIDENCE_SCORE (L7)

**Status:** 🟢 LIVE_FULL — matches proposal (if any), running in production path  
**Category:** [Evidence and Trust](../categories/Evidence-and-Trust.md)  
**Type:** Layer variable  
**Responsible (module):** `core/layers/layer_7.py (~conf product; out SYSTEM_CONFIDENCE_SCORE)`  
**Value / default:** clamp01 product

## Yields (formula)

SYSTEM_CONFIDENCE_SCORE folds L1–L6 consistency gates and includes l6[GLOBAL_STABILITY_SCORE] in the confidence product path.

## Produced from (inputs)

- [LYAPUNOV_ESTIMATE / GLOBAL_STABILITY_SCORE](../pages/LYAPUNOV-ESTIMATE-GLOBAL-STABILITY-SCORE.md)
- [CONSIST_STABILITY_REGIME_VALID (L7)](../pages/CONSIST-STABILITY-REGIME-VALID-L7.md)

## Needed by (consumers)

- [SI_SYSTEM_CONFIDENCE_U1000 (L8)](../pages/SI-SYSTEM-CONFIDENCE-U1000-L8.md)
- *SI_SYSTEM_CONFIDENCE_PCT (L8)*
- *L9 pillars*

## Origin

40_SPEC Layer-7

## Notes

**HWIKI-L7-01:** Primary L7 consumer of GLOBAL_STABILITY_SCORE — not a full L7 census; slice is stability→confidence only.

---
[← back to category](../categories/Evidence-and-Trust.md) · [wiki home](../index.md)
