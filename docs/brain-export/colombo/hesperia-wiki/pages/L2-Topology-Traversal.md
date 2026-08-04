# L2 — Topology Traversal

**Status:** 🔵 BEYOND — shipped in LIVE, not proposed in the Java corpus  
**Category:** [Graph and Structural Metrics](../categories/Graph-and-Structural-Metrics.md)  
**Type:** Hub / concept  
**Responsible (module):** `core/layers/layer_2.py::compute_L2 (35_SPEC)`  
**Value / default:** 27

## In plain words

BFS traversal from L1's dominant family outward — how far and how densely activation reaches through the concept graph.

## Definition

- **Receives:** [L1 — Structural Activation Census](../pages/L1-Structural-Activation-Census.md), [BFS depth-capped traversal](../pages/BFS-depth-capped-traversal.md)
- **Does:** Hub: BFS traversal from L1's dominant family outward — how far and how densely activation reaches through the concept graph.
- **Outputs:** `27` → [L3 — Baseline/Shadow Comparison](../pages/L3-Baseline-Shadow-Comparison.md), [TRAVERSAL_START_FAMILY](../pages/TRAVERSAL-START-FAMILY.md), [BASE_NEIGHBOR_COUNT](../pages/BASE-NEIGHBOR-COUNT.md), [ACTIVE_NEIGHBOR_COUNT](../pages/ACTIVE-NEIGHBOR-COUNT.md), [NEIGHBOR_ACTIVATION_RATIO](../pages/NEIGHBOR-ACTIVATION-RATIO.md), [TRAVERSAL_DEPTH_REACHED](../pages/TRAVERSAL-DEPTH-REACHED.md), [TOTAL_REACHABLE_NODES](../pages/TOTAL-REACHABLE-NODES.md), [REACH_RATIO](../pages/REACH-RATIO.md), [MEAN_TRAVERSAL_DISTANCE](../pages/MEAN-TRAVERSAL-DISTANCE.md), [MAX_TRAVERSAL_DISTANCE](../pages/MAX-TRAVERSAL-DISTANCE.md), [TRAVERSAL_RADIUS_RATIO](../pages/TRAVERSAL-RADIUS-RATIO.md), [PATH_COUNT](../pages/PATH-COUNT.md), [BRANCHING_FACTOR_MEAN](../pages/BRANCHING-FACTOR-MEAN.md), [PROPAGATION_MASS_DECAY](../pages/PROPAGATION-MASS-DECAY.md), [MASS_RETENTION_RATIO](../pages/MASS-RETENTION-RATIO.md), [CROSS_AREA_TRAVERSAL_COUNT](../pages/CROSS-AREA-TRAVERSAL-COUNT.md), [CROSS_AREA_RATIO](../pages/CROSS-AREA-RATIO.md), [AREA_BOUNDARY_CROSSINGS](../pages/AREA-BOUNDARY-CROSSINGS.md), [TRAVERSAL_COMPACTNESS](../pages/TRAVERSAL-COMPACTNESS.md), [CENTRALITY_SHIFT](../pages/CENTRALITY-SHIFT.md), [EDGE_UTILIZATION_RATIO](../pages/EDGE-UTILIZATION-RATIO.md), [TRAVERSAL_SYMMETRY_INDEX](../pages/TRAVERSAL-SYMMETRY-INDEX.md), [GEOMETRIC_STABILITY_INDEX](../pages/GEOMETRIC-STABILITY-INDEX.md), [VISITED_IDS](../pages/VISITED-IDS.md), [MASS_AT_DEPTH](../pages/MASS-AT-DEPTH.md), [L4 — Evidence Retrieval](../pages/L4-Evidence-Retrieval.md), [L7 — Consistency and Decision](../pages/L7-Consistency-and-Decision.md), [L8 — Unit Standardization](../pages/L8-Unit-Standardization.md)
- **Exists for:** **HWIKI-CATALOG-L2:** Source: `docs/foundations/output_catalog.md` §2, re-verified against `compute_L2` 2026-08-04

## Yields (formula)

Hub: BFS traversal from L1's dominant family outward — how far and how densely activation reaches through the concept graph.

## Produced from (inputs)

- [L1 — Structural Activation Census](../pages/L1-Structural-Activation-Census.md)
- [BFS depth-capped traversal](../pages/BFS-depth-capped-traversal.md)

## Needed by (consumers)

- [L3 — Baseline/Shadow Comparison](../pages/L3-Baseline-Shadow-Comparison.md)
- [TRAVERSAL_START_FAMILY](../pages/TRAVERSAL-START-FAMILY.md)
- [BASE_NEIGHBOR_COUNT](../pages/BASE-NEIGHBOR-COUNT.md)
- [ACTIVE_NEIGHBOR_COUNT](../pages/ACTIVE-NEIGHBOR-COUNT.md)
- [NEIGHBOR_ACTIVATION_RATIO](../pages/NEIGHBOR-ACTIVATION-RATIO.md)
- [TRAVERSAL_DEPTH_REACHED](../pages/TRAVERSAL-DEPTH-REACHED.md)
- [TOTAL_REACHABLE_NODES](../pages/TOTAL-REACHABLE-NODES.md)
- [REACH_RATIO](../pages/REACH-RATIO.md)
- [MEAN_TRAVERSAL_DISTANCE](../pages/MEAN-TRAVERSAL-DISTANCE.md)
- [MAX_TRAVERSAL_DISTANCE](../pages/MAX-TRAVERSAL-DISTANCE.md)
- [TRAVERSAL_RADIUS_RATIO](../pages/TRAVERSAL-RADIUS-RATIO.md)
- [PATH_COUNT](../pages/PATH-COUNT.md)
- [BRANCHING_FACTOR_MEAN](../pages/BRANCHING-FACTOR-MEAN.md)
- [PROPAGATION_MASS_DECAY](../pages/PROPAGATION-MASS-DECAY.md)
- [MASS_RETENTION_RATIO](../pages/MASS-RETENTION-RATIO.md)
- [CROSS_AREA_TRAVERSAL_COUNT](../pages/CROSS-AREA-TRAVERSAL-COUNT.md)
- [CROSS_AREA_RATIO](../pages/CROSS-AREA-RATIO.md)
- [AREA_BOUNDARY_CROSSINGS](../pages/AREA-BOUNDARY-CROSSINGS.md)
- [TRAVERSAL_COMPACTNESS](../pages/TRAVERSAL-COMPACTNESS.md)
- [CENTRALITY_SHIFT](../pages/CENTRALITY-SHIFT.md)
- [EDGE_UTILIZATION_RATIO](../pages/EDGE-UTILIZATION-RATIO.md)
- [TRAVERSAL_SYMMETRY_INDEX](../pages/TRAVERSAL-SYMMETRY-INDEX.md)
- [GEOMETRIC_STABILITY_INDEX](../pages/GEOMETRIC-STABILITY-INDEX.md)
- [VISITED_IDS](../pages/VISITED-IDS.md)
- [MASS_AT_DEPTH](../pages/MASS-AT-DEPTH.md)
- [L4 — Evidence Retrieval](../pages/L4-Evidence-Retrieval.md)
- [L7 — Consistency and Decision](../pages/L7-Consistency-and-Decision.md)
- [L8 — Unit Standardization](../pages/L8-Unit-Standardization.md)

## See also

- [L1 — Structural Activation Census](../pages/L1-Structural-Activation-Census.md)
- [BFS depth-capped traversal](../pages/BFS-depth-capped-traversal.md)
- [L3 — Baseline/Shadow Comparison](../pages/L3-Baseline-Shadow-Comparison.md)
- [TRAVERSAL_START_FAMILY](../pages/TRAVERSAL-START-FAMILY.md)
- [BASE_NEIGHBOR_COUNT](../pages/BASE-NEIGHBOR-COUNT.md)
- [ACTIVE_NEIGHBOR_COUNT](../pages/ACTIVE-NEIGHBOR-COUNT.md)
- [NEIGHBOR_ACTIVATION_RATIO](../pages/NEIGHBOR-ACTIVATION-RATIO.md)
- [TRAVERSAL_DEPTH_REACHED](../pages/TRAVERSAL-DEPTH-REACHED.md)
- [TOTAL_REACHABLE_NODES](../pages/TOTAL-REACHABLE-NODES.md)
- [REACH_RATIO](../pages/REACH-RATIO.md)
- [MEAN_TRAVERSAL_DISTANCE](../pages/MEAN-TRAVERSAL-DISTANCE.md)
- [MAX_TRAVERSAL_DISTANCE](../pages/MAX-TRAVERSAL-DISTANCE.md)

## Origin

Hesperia-native `35_SPEC` L2 instrumentation — no Java prototype ancestor — Theory Explainer: plain_lang: BFS traversal from L1's dominant family outward — how far and how densely activation reaches through the concept graph. author: Hesperia wiki (core/layers/layer_2.py::compute_L2 (35_SPEC)). extent: full. reasoning: **HWIKI-CATALOG-L2:** Source: `docs/foundations/output_catalog.md` §2, re-verified against `compute_L2` 2026-08-04. application: [L3 — Baseline/Shadow Comparison](../pages/L3-Baseline-Shadow-Comparison.md).

## Notes

**HWIKI-PLAIN-B:** plain_lang backfilled from formula/notes 2026-08-04. **HWIKI-CATALOG-L2:** Source: `docs/foundations/output_catalog.md` §2, re-verified against `compute_L2` 2026-08-04.

---
[← back to category](../categories/Graph-and-Structural-Metrics.md) · [wiki home](../index.md) · [Wire Map](Wiki-Wire-Map.md)
