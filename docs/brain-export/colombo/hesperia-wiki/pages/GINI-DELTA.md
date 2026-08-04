# GINI_DELTA

**Status:** 🟢 LIVE_FULL — matches proposal (if any), running in production path  
**Category:** [Graph and Structural Metrics](../categories/Graph-and-Structural-Metrics.md)  
**Type:** Derived variable  
**Responsible (module):** `core/layers/layer_3.py::compute_L3 -> result["GINI_DELTA"]`  
**Value / default:** float

## In plain words

Change in [Gini concentration](../pages/Gini-concentration.md) between the two runs — L3's application of the general Jaccard/Gini algorithm pages to a paired comparison.

## Definition

- **Receives:** [L3 — Baseline/Shadow Comparison](../pages/L3-Baseline-Shadow-Comparison.md)
- **Does:** shadow.GINI_COEFFICIENT - baseline.GINI_COEFFICIENT
- **Outputs:** `float` → *no named wiki consumer yet*
- **Exists for:** L3 baseline/shadow delta field — turns single-run measures into comparison

## Yields (formula)

shadow.GINI_COEFFICIENT - baseline.GINI_COEFFICIENT

## Produced from (inputs)

- [L3 — Baseline/Shadow Comparison](../pages/L3-Baseline-Shadow-Comparison.md)

## See also

- [L3 — Baseline/Shadow Comparison](../pages/L3-Baseline-Shadow-Comparison.md)
- [SHADOW_ENABLED](../pages/SHADOW-ENABLED.md)
- [DOMINANT_FAMILY_CHANGED](../pages/DOMINANT-FAMILY-CHANGED.md)
- [DOMINANT_AREA_CHANGED](../pages/DOMINANT-AREA-CHANGED.md)
- [DOMINANT_FAMILY_DELTA_HITS](../pages/DOMINANT-FAMILY-DELTA-HITS.md)
- [DOMINANCE_RATIO_DELTA](../pages/DOMINANCE-RATIO-DELTA.md)
- [COVERAGE_RATIO_DELTA](../pages/COVERAGE-RATIO-DELTA.md)
- [UNIQUE_FAMILIES_HIT_DELTA](../pages/UNIQUE-FAMILIES-HIT-DELTA.md)
- [AREA_SPREAD_DELTA](../pages/AREA-SPREAD-DELTA.md)
- [ENTROPY_DELTA](../pages/ENTROPY-DELTA.md)
- [ALTITUDE_MEAN_DELTA](../pages/ALTITUDE-MEAN-DELTA.md)
- [ALTITUDE_DOMINANT_DELTA](../pages/ALTITUDE-DOMINANT-DELTA.md)

## Origin

Hesperia-native `36_SPEC` L3 instrumentation — no Java prototype ancestor — Theory Explainer: plain_lang: Change in [Gini concentration](../pages/Gini-concentration.md) between the two runs — L3's application of the general Jaccard/Gini algorithm pages to a paired comparison.. author: Hesperia L3 (36_SPEC / output_catalog §3). extent: full. reasoning: L3 baseline/shadow delta field — turns single-run measures into comparison. application: [L3 — Baseline/Shadow Comparison](../pages/L3-Baseline-Shadow-Comparison.md), L4–L9.

## Notes

**HWIKI-CATALOG-L3 / HWIKI-PLAIN:** Change in [Gini concentration](../pages/Gini-concentration.md) between the two runs — L3's application of the general Jaccard/Gini algorithm pages to a paired comparison. Source: `docs/foundations/output_catalog.md` §3, re-verified against `compute_L3` 2026-08-04.

---
[← back to category](../categories/Graph-and-Structural-Metrics.md) · [wiki home](../index.md) · [Wire Map](Wiki-Wire-Map.md)
