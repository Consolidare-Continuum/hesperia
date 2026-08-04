# transition_concentration_threshold

**Status:** 🟢 LIVE_FULL — matches proposal (if any), running in production path  
**Category:** [Activation and Diagnostic Thresholds](../categories/Activation-and-Diagnostic-Thresholds.md)  
**Type:** Parameter (constants)  
**Responsible (module):** `assets/specs/canon/diagnostic_rules.yaml + sphere/diagnostics/anomaly_detector.py`  
**Value / default:** 0.75

## In plain words

Above this, transition mass collapsing into one route is flagged artifact-like concentration.

## Definition

- **Receives:** [dominant_area_share_threshold](../pages/dominant-area-share-threshold.md)
- **Does:** Above this, transition mass collapsing into one route is flagged artifact-like concentration.
- **Outputs:** `0.75` → *sphere/diagnostics/anomaly_detector.py*
- **Exists for:** **HWIKI-CAT-02:** CAT-01 delta — transition concentration

## Yields (formula)

Above this, transition mass collapsing into one route is flagged artifact-like concentration.

## Produced from (inputs)

- [dominant_area_share_threshold](../pages/dominant-area-share-threshold.md)

## Needed by (consumers)

- *sphere/diagnostics/anomaly_detector.py*

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
- [unique_areas_max](../pages/unique-areas-max.md)

## Origin

parameter_catalog.md §4 — Theory Explainer: plain_lang: Above this, transition mass collapsing into one route is flagged artifact-like concentration. author: Hesperia wiki (assets/specs/canon/diagnostic_rules.yaml + sphere/diagnostics/anomaly_detector.py). extent: full. reasoning: **HWIKI-CAT-02:** CAT-01 delta — transition concentration. application: *sphere/diagnostics/anomaly_detector.py*.

## Notes

**HWIKI-WIRE:** attached to category anchor [dominant_area_share_threshold](../pages/dominant-area-share-threshold.md). **HWIKI-PLAIN-B:** plain_lang backfilled from formula/notes 2026-08-04. **HWIKI-CAT-02:** CAT-01 delta — transition concentration.

---
[← back to category](../categories/Activation-and-Diagnostic-Thresholds.md) · [wiki home](../index.md) · [Wire Map](Wiki-Wire-Map.md)
