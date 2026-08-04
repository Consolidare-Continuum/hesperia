# DEPTH_GROWTH_RATIO (L6)

**Status:** 🟢 LIVE_FULL — matches proposal (if any), running in production path  
**Category:** [Stability and Control Theory](../categories/Stability-and-Control-Theory.md)  
**Type:** Layer variable  
**Responsible (module):** `core/layers/layer_6.py (L6_LIVE_FIELDS)`  
**Value / default:** mass_at_depth[1]/mass_at_depth[0]

## Yields (formula)

DEPTH_GROWTH_RATIO = mass_at_depth[1] / (mass_at_depth[0] + eps) when len≥2 and mass[0]>0; else 0.

## Needed by (consumers)

- [FIBONACCI_DEVIATION_SCORE (L6)](../pages/FIBONACCI-DEVIATION-SCORE-L6.md)
- [EXPONENTIAL_FIT_ERROR (L6)](../pages/EXPONENTIAL-FIT-ERROR-L6.md)

## Origin

39_SPEC Layer-6 Group IV

## Notes

**HWIKI-L6-02:** Truly LIVE depth-growth signal from activation mass ladder — not a stub.

---
[← back to category](../categories/Stability-and-Control-Theory.md) · [wiki home](../index.md)
