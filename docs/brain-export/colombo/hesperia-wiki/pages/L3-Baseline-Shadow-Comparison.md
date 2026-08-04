# L3 — Baseline/Shadow Comparison

**Status:** 🔵 BEYOND — shipped in LIVE, not proposed in the Java corpus  
**Category:** [Graph and Structural Metrics](../categories/Graph-and-Structural-Metrics.md)  
**Type:** Hub / concept  
**Responsible (module):** `core/layers/layer_3.py::compute_L3 (36_SPEC)`  
**Value / default:** 25

## In plain words

runs L1+L2 twice (baseline text vs. shadow/counter text) and diffs every metric — the layer that turns single-run measurements into a comparison.

## Definition

- **Receives:** [L1 — Structural Activation Census](../pages/L1-Structural-Activation-Census.md), [L2 — Topology Traversal](../pages/L2-Topology-Traversal.md)
- **Does:** Hub: runs L1+L2 twice (baseline text vs. shadow/counter text) and diffs every metric — the layer that turns single-run measurements into a comparison.
- **Outputs:** `25` → [L4 — Evidence Retrieval](../pages/L4-Evidence-Retrieval.md), [SHADOW_ENABLED](../pages/SHADOW-ENABLED.md), [DOMINANT_FAMILY_CHANGED](../pages/DOMINANT-FAMILY-CHANGED.md), [DOMINANT_AREA_CHANGED](../pages/DOMINANT-AREA-CHANGED.md), [DOMINANT_FAMILY_DELTA_HITS](../pages/DOMINANT-FAMILY-DELTA-HITS.md), [DOMINANCE_RATIO_DELTA](../pages/DOMINANCE-RATIO-DELTA.md), [COVERAGE_RATIO_DELTA](../pages/COVERAGE-RATIO-DELTA.md), [UNIQUE_FAMILIES_HIT_DELTA](../pages/UNIQUE-FAMILIES-HIT-DELTA.md), [AREA_SPREAD_DELTA](../pages/AREA-SPREAD-DELTA.md), [ENTROPY_DELTA](../pages/ENTROPY-DELTA.md), [GINI_DELTA](../pages/GINI-DELTA.md), [ALTITUDE_MEAN_DELTA](../pages/ALTITUDE-MEAN-DELTA.md), [ALTITUDE_DOMINANT_DELTA](../pages/ALTITUDE-DOMINANT-DELTA.md), [TRAVERSAL_DEPTH_DELTA](../pages/TRAVERSAL-DEPTH-DELTA.md), [REACHABLE_NODES_DELTA](../pages/REACHABLE-NODES-DELTA.md), [MAX_DISTANCE_DELTA](../pages/MAX-DISTANCE-DELTA.md), [CROSS_AREA_RATIO_DELTA](../pages/CROSS-AREA-RATIO-DELTA.md), [LOOP_DENSITY_DELTA](../pages/LOOP-DENSITY-DELTA.md), [EDGE_UTILIZATION_DELTA](../pages/EDGE-UTILIZATION-DELTA.md), [VISITED_JACCARD_SIMILARITY](../pages/VISITED-JACCARD-SIMILARITY.md), [VISITED_SYMMETRIC_DIFFERENCE_RATIO](../pages/VISITED-SYMMETRIC-DIFFERENCE-RATIO.md), [FAMILY_HIT_VECTOR_L1_DELTA](../pages/FAMILY-HIT-VECTOR-L1-DELTA.md), [HIT_VECTOR_COSINE_SIMILARITY](../pages/HIT-VECTOR-COSINE-SIMILARITY.md), [TOP_K_OVERLAP_RATIO](../pages/TOP-K-OVERLAP-RATIO.md), [SHADOW_DEVIATION_SCORE](../pages/SHADOW-DEVIATION-SCORE.md), [SHADOW_ACCEPTABILITY_GATE](../pages/SHADOW-ACCEPTABILITY-GATE.md), [L7 — Consistency and Decision](../pages/L7-Consistency-and-Decision.md), [L8 — Unit Standardization](../pages/L8-Unit-Standardization.md)
- **Exists for:** **HWIKI-CATALOG-L3:** Source: `docs/foundations/output_catalog.md` §3, re-verified against `compute_L3` 2026-08-04

## Yields (formula)

Hub: runs L1+L2 twice (baseline text vs. shadow/counter text) and diffs every metric — the layer that turns single-run measurements into a comparison.

## Produced from (inputs)

- [L1 — Structural Activation Census](../pages/L1-Structural-Activation-Census.md)
- [L2 — Topology Traversal](../pages/L2-Topology-Traversal.md)

## Needed by (consumers)

- [L4 — Evidence Retrieval](../pages/L4-Evidence-Retrieval.md)
- [SHADOW_ENABLED](../pages/SHADOW-ENABLED.md)
- [DOMINANT_FAMILY_CHANGED](../pages/DOMINANT-FAMILY-CHANGED.md)
- [DOMINANT_AREA_CHANGED](../pages/DOMINANT-AREA-CHANGED.md)
- [DOMINANT_FAMILY_DELTA_HITS](../pages/DOMINANT-FAMILY-DELTA-HITS.md)
- [DOMINANCE_RATIO_DELTA](../pages/DOMINANCE-RATIO-DELTA.md)
- [COVERAGE_RATIO_DELTA](../pages/COVERAGE-RATIO-DELTA.md)
- [UNIQUE_FAMILIES_HIT_DELTA](../pages/UNIQUE-FAMILIES-HIT-DELTA.md)
- [AREA_SPREAD_DELTA](../pages/AREA-SPREAD-DELTA.md)
- [ENTROPY_DELTA](../pages/ENTROPY-DELTA.md)
- [GINI_DELTA](../pages/GINI-DELTA.md)
- [ALTITUDE_MEAN_DELTA](../pages/ALTITUDE-MEAN-DELTA.md)
- [ALTITUDE_DOMINANT_DELTA](../pages/ALTITUDE-DOMINANT-DELTA.md)
- [TRAVERSAL_DEPTH_DELTA](../pages/TRAVERSAL-DEPTH-DELTA.md)
- [REACHABLE_NODES_DELTA](../pages/REACHABLE-NODES-DELTA.md)
- [MAX_DISTANCE_DELTA](../pages/MAX-DISTANCE-DELTA.md)
- [CROSS_AREA_RATIO_DELTA](../pages/CROSS-AREA-RATIO-DELTA.md)
- [LOOP_DENSITY_DELTA](../pages/LOOP-DENSITY-DELTA.md)
- [EDGE_UTILIZATION_DELTA](../pages/EDGE-UTILIZATION-DELTA.md)
- [VISITED_JACCARD_SIMILARITY](../pages/VISITED-JACCARD-SIMILARITY.md)
- [VISITED_SYMMETRIC_DIFFERENCE_RATIO](../pages/VISITED-SYMMETRIC-DIFFERENCE-RATIO.md)
- [FAMILY_HIT_VECTOR_L1_DELTA](../pages/FAMILY-HIT-VECTOR-L1-DELTA.md)
- [HIT_VECTOR_COSINE_SIMILARITY](../pages/HIT-VECTOR-COSINE-SIMILARITY.md)
- [TOP_K_OVERLAP_RATIO](../pages/TOP-K-OVERLAP-RATIO.md)
- [SHADOW_DEVIATION_SCORE](../pages/SHADOW-DEVIATION-SCORE.md)
- [SHADOW_ACCEPTABILITY_GATE](../pages/SHADOW-ACCEPTABILITY-GATE.md)
- [L7 — Consistency and Decision](../pages/L7-Consistency-and-Decision.md)
- [L8 — Unit Standardization](../pages/L8-Unit-Standardization.md)

## See also

- [L1 — Structural Activation Census](../pages/L1-Structural-Activation-Census.md)
- [L2 — Topology Traversal](../pages/L2-Topology-Traversal.md)
- [L4 — Evidence Retrieval](../pages/L4-Evidence-Retrieval.md)
- [SHADOW_ENABLED](../pages/SHADOW-ENABLED.md)
- [DOMINANT_FAMILY_CHANGED](../pages/DOMINANT-FAMILY-CHANGED.md)
- [DOMINANT_AREA_CHANGED](../pages/DOMINANT-AREA-CHANGED.md)
- [DOMINANT_FAMILY_DELTA_HITS](../pages/DOMINANT-FAMILY-DELTA-HITS.md)
- [DOMINANCE_RATIO_DELTA](../pages/DOMINANCE-RATIO-DELTA.md)
- [COVERAGE_RATIO_DELTA](../pages/COVERAGE-RATIO-DELTA.md)
- [UNIQUE_FAMILIES_HIT_DELTA](../pages/UNIQUE-FAMILIES-HIT-DELTA.md)
- [AREA_SPREAD_DELTA](../pages/AREA-SPREAD-DELTA.md)
- [ENTROPY_DELTA](../pages/ENTROPY-DELTA.md)

## Origin

Hesperia-native `36_SPEC` L3 instrumentation — no Java prototype ancestor — Theory Explainer: plain_lang: runs L1+L2 twice (baseline text vs. shadow/counter text) and diffs every metric — the layer that turns single-run measurements into a comparison. author: Hesperia wiki (core/layers/layer_3.py::compute_L3 (36_SPEC)). extent: full. reasoning: **HWIKI-CATALOG-L3:** Source: `docs/foundations/output_catalog.md` §3, re-verified against `compute_L3` 2026-08-04. application: [L4 — Evidence Retrieval](../pages/L4-Evidence-Retrieval.md).

## Notes

**HWIKI-PLAIN-B:** plain_lang backfilled from formula/notes 2026-08-04. **HWIKI-CATALOG-L3:** Source: `docs/foundations/output_catalog.md` §3, re-verified against `compute_L3` 2026-08-04.

---
[← back to category](../categories/Graph-and-Structural-Metrics.md) · [wiki home](../index.md) · [Wire Map](Wiki-Wire-Map.md)
