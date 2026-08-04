# EDGE_UTILIZATION_RATIO

**Status:** 🟢 LIVE_FULL — matches proposal (if any), running in production path  
**Category:** [Graph and Structural Metrics](../categories/Graph-and-Structural-Metrics.md)  
**Type:** Derived variable  
**Responsible (module):** `core/layers/layer_2.py::compute_L2 -> result["EDGE_UTILIZATION_RATIO"]`  
**Value / default:** float [0,1]

## In plain words

What fraction of all edges among visited families the BFS tree itself actually used, versus edges that exist but weren't traversal edges.

## Definition

- **Receives:** [L2 — Topology Traversal](../pages/L2-Topology-Traversal.md)
- **Does:** BFS tree edges / total induced-subgraph edges
- **Outputs:** `float [0,1]` → *no named wiki consumer yet*
- **Exists for:** L2 topology-traversal field — how activation spreads from L1 dominant

## Yields (formula)

BFS tree edges / total induced-subgraph edges

## Produced from (inputs)

- [L2 — Topology Traversal](../pages/L2-Topology-Traversal.md)

## See also

- [L2 — Topology Traversal](../pages/L2-Topology-Traversal.md)
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

## Origin

Hesperia-native `35_SPEC` L2 instrumentation — no Java prototype ancestor — Theory Explainer: plain_lang: What fraction of all edges among visited families the BFS tree itself actually used, versus edges that exist but weren't traversal edges.. author: Hesperia L2 (35_SPEC / output_catalog §2). extent: full. reasoning: L2 topology-traversal field — how activation spreads from L1 dominant. application: [L2 — Topology Traversal](../pages/L2-Topology-Traversal.md), L3–L9.

## Notes

**HWIKI-CATALOG-L2 / HWIKI-PLAIN:** What fraction of all edges among visited families the BFS tree itself actually used, versus edges that exist but weren't traversal edges. Source: `docs/foundations/output_catalog.md` §2, re-verified against `compute_L2` 2026-08-04.

---
[← back to category](../categories/Graph-and-Structural-Metrics.md) · [wiki home](../index.md) · [Wire Map](Wiki-Wire-Map.md)
