# activation_threshold

**Status:** 🟢 LIVE_FULL — matches proposal (if any), running in production path  
**Category:** [Activation and Diagnostic Thresholds](../categories/Activation-and-Diagnostic-Thresholds.md)  
**Type:** Parameter (constant)  
**Responsible (module):** `diagnostics config`  
**Value / default:** 0.01

## In plain words

sparse activation floor — below this energy a cell does not count as a hit.

## Definition

- **Receives:** [dominant_area_share_threshold](../pages/dominant-area-share-threshold.md)
- **Does:** Sparse activation floor — what counts as a hit.
- **Outputs:** `0.01` → *no named wiki consumer yet*
- **Exists for:** diagnostics/config threshold for hit detection

## Yields (formula)

Sparse activation floor — what counts as a hit.

## Produced from (inputs)

- [dominant_area_share_threshold](../pages/dominant-area-share-threshold.md)

## See also

- [dominant_area_share_threshold](../pages/dominant-area-share-threshold.md)
- [area_active_threshold](../pages/area-active-threshold.md)
- [coverage_threshold (monotony)](../pages/coverage-threshold-monotony.md)
- [curvature_threshold / severe](../pages/curvature-threshold-severe.md)
- [jump_rate_threshold / severe](../pages/jump-rate-threshold-severe.md)
- [low_stability_threshold](../pages/low-stability-threshold.md)
- [ultra_sparse_coverage_threshold](../pages/ultra-sparse-coverage-threshold.md)
- [excessive_jump_threshold](../pages/excessive-jump-threshold.md)
- [transition_concentration_threshold](../pages/transition-concentration-threshold.md)
- [unique_areas_max](../pages/unique-areas-max.md)

## Origin

No Java ancestor — Theory Explainer: plain_lang: sparse activation floor — below this energy a cell does not count as a hit. author: Hesperia wiki (diagnostics config). extent: full. reasoning: diagnostics/config threshold for hit detection. application: Activation and Diagnostic Thresholds.

## Notes

**HWIKI-WIRE:** attached to category anchor [dominant_area_share_threshold](../pages/dominant-area-share-threshold.md). **HWIKI-PLAIN-C:** algebra plain_lang polished 2026-08-04. **HWIKI-PLAIN-B:** plain_lang backfilled from formula/notes 2026-08-04.

---
[← back to category](../categories/Activation-and-Diagnostic-Thresholds.md) · [wiki home](../index.md) · [Wire Map](Wiki-Wire-Map.md)
