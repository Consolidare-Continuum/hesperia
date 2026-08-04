# SI_GLOBAL_STABILITY_U1000 (L8)

**Status:** 🟢 LIVE_FULL — matches proposal (if any), running in production path  
**Category:** [Evidence and Trust](../categories/Evidence-and-Trust.md)  
**Type:** Scaled indicator  
**Responsible (module):** `core/layers/layer_8.py:48`  
**Value / default:** 0–1000

## Yields (formula)

SI_GLOBAL_STABILITY_U1000 = _ratio_to_u1000(l6[GLOBAL_STABILITY_SCORE]) — scaled publish of L6 global stability.

## Produced from (inputs)

- [LYAPUNOV_ESTIMATE / GLOBAL_STABILITY_SCORE](../pages/LYAPUNOV-ESTIMATE-GLOBAL-STABILITY-SCORE.md)

## Needed by (consumers)

- [SI_GLOBAL_STABILITY_PCT (L8)](../pages/SI-GLOBAL-STABILITY-PCT-L8.md)

## Origin

41_SPEC Layer-8

## Notes

**HWIKI-L8-01:** Direct L8 scaled consumer of GLOBAL_STABILITY_SCORE.

---
[← back to category](../categories/Evidence-and-Trust.md) · [wiki home](../index.md)
