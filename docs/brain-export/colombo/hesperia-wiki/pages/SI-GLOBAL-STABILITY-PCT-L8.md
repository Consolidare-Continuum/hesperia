# SI_GLOBAL_STABILITY_PCT (L8)

**Status:** 🟢 LIVE_FULL — matches proposal (if any), running in production path  
**Category:** [Evidence and Trust](../categories/Evidence-and-Trust.md)  
**Type:** Scaled indicator  
**Responsible (module):** `core/layers/layer_8.py:49`  
**Value / default:** 0–100%

## Yields (formula)

SI_GLOBAL_STABILITY_PCT = _ratio_to_pct(l6[GLOBAL_STABILITY_SCORE]).

## Produced from (inputs)

- [LYAPUNOV_ESTIMATE / GLOBAL_STABILITY_SCORE](../pages/LYAPUNOV-ESTIMATE-GLOBAL-STABILITY-SCORE.md)
- [SI_GLOBAL_STABILITY_U1000 (L8)](../pages/SI-GLOBAL-STABILITY-U1000-L8.md)

## Needed by (consumers)

- *SI_SYSTEM_CONFIDENCE_PCT (L8)*

## Origin

41_SPEC Layer-8

## Notes

**HWIKI-L8-01:** Percent twin of SI_GLOBAL_STABILITY_U1000.

---
[← back to category](../categories/Evidence-and-Trust.md) · [wiki home](../index.md)
