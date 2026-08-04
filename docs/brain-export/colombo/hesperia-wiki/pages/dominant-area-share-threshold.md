# dominant_area_share_threshold

**Status:** 🟢 LIVE_SUCCESSOR — same idea, different name/formula than any Java ancestor  
**Category:** [Activation and Diagnostic Thresholds](../categories/Activation-and-Diagnostic-Thresholds.md)  
**Type:** Parameter (constant)  
**Responsible (module):** `sphere/diagnostics/monotony_detector.py`  
**Value / default:** 0.65

## In plain words

if the dominant area's share of activation clears this threshold, classify the read as dominance (wired successor of Java X_A).

## Definition

- **Receives:** *A_vec[12] (area activation vector)*
- **Does:** compute_dominant_area_share(area_vector) >= threshold triggers dominance classification.
- **Outputs:** `0.65` → [X_A / X_F alignment (Java)](../pages/X-A-X-F-alignment-Java.md), [activation_threshold](../pages/activation-threshold.md), [area_active_threshold](../pages/area-active-threshold.md), [coverage_threshold (monotony)](../pages/coverage-threshold-monotony.md), [curvature_threshold / severe](../pages/curvature-threshold-severe.md), [jump_rate_threshold / severe](../pages/jump-rate-threshold-severe.md), [low_stability_threshold](../pages/low-stability-threshold.md), [ultra_sparse_coverage_threshold](../pages/ultra-sparse-coverage-threshold.md), [excessive_jump_threshold](../pages/excessive-jump-threshold.md), [transition_concentration_threshold](../pages/transition-concentration-threshold.md), [unique_areas_max](../pages/unique-areas-max.md)
- **Exists for:** share-fraction rule trigger in rules config

## Yields (formula)

compute_dominant_area_share(area_vector) >= threshold triggers dominance classification.

## Produced from (inputs)

- *A_vec[12] (area activation vector)*

## Needed by (consumers)

- [X_A / X_F alignment (Java)](../pages/X-A-X-F-alignment-Java.md)
- [activation_threshold](../pages/activation-threshold.md)
- [area_active_threshold](../pages/area-active-threshold.md)
- [coverage_threshold (monotony)](../pages/coverage-threshold-monotony.md)
- [curvature_threshold / severe](../pages/curvature-threshold-severe.md)
- [jump_rate_threshold / severe](../pages/jump-rate-threshold-severe.md)
- [low_stability_threshold](../pages/low-stability-threshold.md)
- [ultra_sparse_coverage_threshold](../pages/ultra-sparse-coverage-threshold.md)
- [excessive_jump_threshold](../pages/excessive-jump-threshold.md)
- [transition_concentration_threshold](../pages/transition-concentration-threshold.md)
- [unique_areas_max](../pages/unique-areas-max.md)

## See also

- [X_A / X_F alignment (Java)](../pages/X-A-X-F-alignment-Java.md)
- [activation_threshold](../pages/activation-threshold.md)
- [area_active_threshold](../pages/area-active-threshold.md)
- [coverage_threshold (monotony)](../pages/coverage-threshold-monotony.md)
- [curvature_threshold / severe](../pages/curvature-threshold-severe.md)
- [jump_rate_threshold / severe](../pages/jump-rate-threshold-severe.md)
- [low_stability_threshold](../pages/low-stability-threshold.md)
- [ultra_sparse_coverage_threshold](../pages/ultra-sparse-coverage-threshold.md)
- [excessive_jump_threshold](../pages/excessive-jump-threshold.md)
- [transition_concentration_threshold](../pages/transition-concentration-threshold.md)
- [unique_areas_max](../pages/unique-areas-max.md)
- [detect_dominant_area / detect_dominant_family](../pages/detect-dominant-area-detect-dominant-family.md)

## Origin

Java 20_GEOMETRY `X_A` alignment concept — Theory Explainer: plain_lang: if the dominant area's share of activation clears this threshold, classify the read as dominance (wired successor of Java X_A). author: Hesperia wiki (sphere/diagnostics/monotony_detector.py). extent: full. reasoning: share-fraction rule trigger in rules config. application: [X_A / X_F alignment (Java)](../pages/X-A-X-F-alignment-Java.md).

## Notes

**HWIKI-PLAIN-C:** algebra plain_lang polished 2026-08-04. **HWIKI-PLAIN-B:** plain_lang backfilled from formula/notes 2026-08-04. Real, wired successor of Java's X_A — has a threshold AND a rule trigger in `rule_registry.py`. No family-share (`X_F`) counterpart exists yet — see [X_A / X_F alignment (Java)](../pages/X-A-X-F-alignment-Java.md).

---
[← back to category](../categories/Activation-and-Diagnostic-Thresholds.md) · [wiki home](../index.md) · [Wire Map](Wiki-Wire-Map.md)
