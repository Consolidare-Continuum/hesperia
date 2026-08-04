# coverage_threshold (monotony)

**Status:** 🟢 LIVE_FULL — matches proposal (if any), running in production path  
**Category:** [Activation and Diagnostic Thresholds](../categories/Activation-and-Diagnostic-Thresholds.md)  
**Type:** Parameter (constant)  
**Responsible (module):** `assets/specs/canon/diagnostic_rules.yaml`  
**Value / default:** 0.20

## In plain words

coverage floor used with entropy_threshold to decide the monotony regime.

## Definition

- **Receives:** [dominant_area_share_threshold](../pages/dominant-area-share-threshold.md)
- **Does:** Joint with entropy_threshold for the monotony regime.
- **Outputs:** `0.20` → *no named wiki consumer yet*
- **Exists for:** joint monotony gate with entropy

## Yields (formula)

Joint with entropy_threshold for the monotony regime.

## Produced from (inputs)

- [dominant_area_share_threshold](../pages/dominant-area-share-threshold.md)

## See also

- [dominant_area_share_threshold](../pages/dominant-area-share-threshold.md)
- [activation_threshold](../pages/activation-threshold.md)
- [area_active_threshold](../pages/area-active-threshold.md)
- [curvature_threshold / severe](../pages/curvature-threshold-severe.md)
- [jump_rate_threshold / severe](../pages/jump-rate-threshold-severe.md)
- [low_stability_threshold](../pages/low-stability-threshold.md)
- [ultra_sparse_coverage_threshold](../pages/ultra-sparse-coverage-threshold.md)
- [excessive_jump_threshold](../pages/excessive-jump-threshold.md)
- [transition_concentration_threshold](../pages/transition-concentration-threshold.md)
- [unique_areas_max](../pages/unique-areas-max.md)

## Origin

No Java ancestor — Theory Explainer: plain_lang: coverage floor used with entropy_threshold to decide the monotony regime. author: Hesperia wiki (assets/specs/canon/diagnostic_rules.yaml). extent: full. reasoning: joint monotony gate with entropy. application: Activation and Diagnostic Thresholds.

## Notes

**HWIKI-WIRE:** attached to category anchor [dominant_area_share_threshold](../pages/dominant-area-share-threshold.md). **HWIKI-PLAIN-C:** algebra plain_lang polished 2026-08-04. **HWIKI-PLAIN-B:** plain_lang backfilled from formula/notes 2026-08-04.

---
[← back to category](../categories/Activation-and-Diagnostic-Thresholds.md) · [wiki home](../index.md) · [Wire Map](Wiki-Wire-Map.md)
