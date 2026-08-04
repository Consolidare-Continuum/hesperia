# DEPTH_GROWTH_RATIO (L6)

**Status:** 🟢 LIVE_FULL — matches proposal (if any), running in production path  
**Category:** [Stability and Control Theory](../categories/Stability-and-Control-Theory.md)  
**Type:** Layer variable  
**Responsible (module):** `core/layers/layer_6.py (L6_LIVE_FIELDS)`  
**Value / default:** mass_at_depth[1]/mass_at_depth[0]

## In plain words

how much activation mass grows from BFS depth 0 to depth 1 — mass_at_depth[1] over mass_at_depth[0]; 0 if the ladder is too short.

## Definition

- **Receives:** *none declared (constant, hub, or external)*
- **Does:** DEPTH_GROWTH_RATIO = mass_at_depth[1] / (mass_at_depth[0] + eps) when len≥2 and mass[0]>0; else 0.
- **Outputs:** `mass_at_depth[1]/mass_at_depth[0]` → [FIBONACCI_DEVIATION_SCORE (L6)](../pages/FIBONACCI-DEVIATION-SCORE-L6.md), [EXPONENTIAL_FIT_ERROR (L6)](../pages/EXPONENTIAL-FIT-ERROR-L6.md), [POWER_LAW_FIT_ERROR (L6)](../pages/POWER-LAW-FIT-ERROR-L6.md)
- **Exists for:** LIVE L6 depth-growth signal from the activation mass ladder

## Yields (formula)

DEPTH_GROWTH_RATIO = mass_at_depth[1] / (mass_at_depth[0] + eps) when len≥2 and mass[0]>0; else 0.

## Needed by (consumers)

- [FIBONACCI_DEVIATION_SCORE (L6)](../pages/FIBONACCI-DEVIATION-SCORE-L6.md)
- [EXPONENTIAL_FIT_ERROR (L6)](../pages/EXPONENTIAL-FIT-ERROR-L6.md)
- [POWER_LAW_FIT_ERROR (L6)](../pages/POWER-LAW-FIT-ERROR-L6.md)

## See also

- [FIBONACCI_DEVIATION_SCORE (L6)](../pages/FIBONACCI-DEVIATION-SCORE-L6.md)
- [EXPONENTIAL_FIT_ERROR (L6)](../pages/EXPONENTIAL-FIT-ERROR-L6.md)
- [POWER_LAW_FIT_ERROR (L6)](../pages/POWER-LAW-FIT-ERROR-L6.md)

## Origin

39_SPEC Layer-6 Group IV — Theory Explainer: plain_lang: how much activation mass grows from BFS depth 0 to depth 1 — mass_at_depth[1] over mass_at_depth[0]; 0 if the ladder is too short. author: Hesperia wiki (core/layers/layer_6.py (L6_LIVE_FIELDS)). extent: full. reasoning: LIVE L6 depth-growth signal from the activation mass ladder. application: [FIBONACCI_DEVIATION_SCORE (L6)](../pages/FIBONACCI-DEVIATION-SCORE-L6.md), [EXPONENTIAL_FIT_ERROR (L6)](../pages/EXPONENTIAL-FIT-ERROR-L6.md).

## Notes

**HWIKI-PLAIN-C:** algebra plain_lang polished 2026-08-04. **HWIKI-PLAIN-B:** plain_lang backfilled from formula/notes 2026-08-04. **HWIKI-L6-02:** Truly LIVE depth-growth signal from activation mass ladder — not a stub.

---
[← back to category](../categories/Stability-and-Control-Theory.md) · [wiki home](../index.md) · [Wire Map](Wiki-Wire-Map.md)
