# FIBONACCI_DEVIATION_SCORE (L6)

**Status:** 🟢 LIVE_FULL — matches proposal (if any), running in production path  
**Category:** [Stability and Control Theory](../categories/Stability-and-Control-Theory.md)  
**Type:** Layer variable  
**Responsible (module):** `core/layers/layer_6.py (L6_LIVE_FIELDS)`  
**Value / default:** |m2 − (m1+m0)|

## In plain words

how far the depth-2 mass strays from 'depth1 + depth0' (Fibonacci-like growth) — large deviation means the ladder is not additive.

## Definition

- **Receives:** [DEPTH_GROWTH_RATIO (L6)](../pages/DEPTH-GROWTH-RATIO-L6.md)
- **Does:** FIBONACCI_DEVIATION_SCORE = |mass_at_depth[2] − (mass_at_depth[1] + mass_at_depth[0])| when len≥3; else 0.
- **Outputs:** `|m2 − (m1+m0)|` → *no named wiki consumer yet*
- **Exists for:** LIVE L6 fibonacci-like deviation on the depth mass ladder

## Yields (formula)

FIBONACCI_DEVIATION_SCORE = |mass_at_depth[2] − (mass_at_depth[1] + mass_at_depth[0])| when len≥3; else 0.

## Produced from (inputs)

- [DEPTH_GROWTH_RATIO (L6)](../pages/DEPTH-GROWTH-RATIO-L6.md)

## See also

- [DEPTH_GROWTH_RATIO (L6)](../pages/DEPTH-GROWTH-RATIO-L6.md)
- [EXPONENTIAL_FIT_ERROR (L6)](../pages/EXPONENTIAL-FIT-ERROR-L6.md)
- [POWER_LAW_FIT_ERROR (L6)](../pages/POWER-LAW-FIT-ERROR-L6.md)

## Origin

39_SPEC Layer-6 Group IV — Theory Explainer: plain_lang: how far the depth-2 mass strays from 'depth1 + depth0' (Fibonacci-like growth) — large deviation means the ladder is not additive. author: Hesperia wiki (core/layers/layer_6.py (L6_LIVE_FIELDS)). extent: full. reasoning: LIVE L6 fibonacci-like deviation on the depth mass ladder. application: [DEPTH_GROWTH_RATIO (L6)](../pages/DEPTH-GROWTH-RATIO-L6.md).

## Notes

**HWIKI-PLAIN-C:** algebra plain_lang polished 2026-08-04. **HWIKI-PLAIN-B:** plain_lang backfilled from formula/notes 2026-08-04. **HWIKI-L6-02:** LIVE fibonacci-like deviation on the depth mass ladder; companion of DEPTH_GROWTH_RATIO.

---
[← back to category](../categories/Stability-and-Control-Theory.md) · [wiki home](../index.md) · [Wire Map](Wiki-Wire-Map.md)
