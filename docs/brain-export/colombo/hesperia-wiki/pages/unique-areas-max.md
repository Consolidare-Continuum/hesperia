# unique_areas_max

**Status:** 🟢 LIVE_FULL — matches proposal (if any), running in production path  
**Category:** [Activation and Diagnostic Thresholds](../categories/Activation-and-Diagnostic-Thresholds.md)  
**Type:** Parameter (constants)  
**Responsible (module):** `sphere/diagnostics/monotony_detector.py:51,89`  
**Value / default:** 2

## In plain words

Caps how many distinct areas a read can touch and still be labeled monotonous.

## Definition

- **Receives:** [dominant_area_share_threshold](../pages/dominant-area-share-threshold.md)
- **Does:** Caps how many distinct areas a read can touch and still be labeled monotonous.
- **Outputs:** `2` → *sphere/diagnostics/monotony_detector.py*
- **Exists for:** **HWIKI-CAT-02:** CAT-01 delta — monotony cardinality cap

## Yields (formula)

Caps how many distinct areas a read can touch and still be labeled monotonous.

## Produced from (inputs)

- [dominant_area_share_threshold](../pages/dominant-area-share-threshold.md)

## Needed by (consumers)

- *sphere/diagnostics/monotony_detector.py*

## See also

- [dominant_area_share_threshold](../pages/dominant-area-share-threshold.md)
- [activation_threshold](../pages/activation-threshold.md)
- [area_active_threshold](../pages/area-active-threshold.md)
- [coverage_threshold (monotony)](../pages/coverage-threshold-monotony.md)
- [curvature_threshold / severe](../pages/curvature-threshold-severe.md)
- [jump_rate_threshold / severe](../pages/jump-rate-threshold-severe.md)
- [low_stability_threshold](../pages/low-stability-threshold.md)
- [ultra_sparse_coverage_threshold](../pages/ultra-sparse-coverage-threshold.md)
- [excessive_jump_threshold](../pages/excessive-jump-threshold.md)
- [transition_concentration_threshold](../pages/transition-concentration-threshold.md)

## Origin

parameter_catalog.md §4 — Theory Explainer: plain_lang: Caps how many distinct areas a read can touch and still be labeled monotonous. author: Hesperia wiki (sphere/diagnostics/monotony_detector.py:51,89). extent: full. reasoning: **HWIKI-CAT-02:** CAT-01 delta — monotony cardinality cap. application: *sphere/diagnostics/monotony_detector.py*.

## Notes

**HWIKI-WIRE:** attached to category anchor [dominant_area_share_threshold](../pages/dominant-area-share-threshold.md). **HWIKI-PLAIN-B:** plain_lang backfilled from formula/notes 2026-08-04. **HWIKI-CAT-02:** CAT-01 delta — monotony cardinality cap.

---
[← back to category](../categories/Activation-and-Diagnostic-Thresholds.md) · [wiki home](../index.md) · [Wire Map](Wiki-Wire-Map.md)
