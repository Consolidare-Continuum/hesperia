# PATH_COUNT

**Status:** 🟢 LIVE_FULL — matches proposal (if any), running in production path  
**Category:** [Graph and Structural Metrics](../categories/Graph-and-Structural-Metrics.md)  
**Type:** Derived variable  
**Responsible (module):** `core/layers/layer_2.py::compute_L2 -> result["PATH_COUNT"]`  
**Value / default:** int

## In plain words

Edge count of the BFS spanning tree — one less than the node count, by construction.

## Definition

- **Receives:** [L2 — Topology Traversal](../pages/L2-Topology-Traversal.md)
- **Does:** [TOTAL_REACHABLE_NODES](../pages/TOTAL-REACHABLE-NODES.md) - 1
- **Outputs:** `int` → *no named wiki consumer yet*
- **Exists for:** L2 topology-traversal field — how activation spreads from L1 dominant

## Yields (formula)

[TOTAL_REACHABLE_NODES](../pages/TOTAL-REACHABLE-NODES.md) - 1

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
- [BRANCHING_FACTOR_MEAN](../pages/BRANCHING-FACTOR-MEAN.md)

## Origin

Hesperia-native `35_SPEC` L2 instrumentation — no Java prototype ancestor — Theory Explainer: plain_lang: Edge count of the BFS spanning tree — one less than the node count, by construction.. author: Hesperia L2 (35_SPEC / output_catalog §2). extent: full. reasoning: L2 topology-traversal field — how activation spreads from L1 dominant. application: [L2 — Topology Traversal](../pages/L2-Topology-Traversal.md), L3–L9.

## Notes

**HWIKI-CATALOG-L2 / HWIKI-PLAIN:** Edge count of the BFS spanning tree — one less than the node count, by construction. Source: `docs/foundations/output_catalog.md` §2, re-verified against `compute_L2` 2026-08-04.

---
[← back to category](../categories/Graph-and-Structural-Metrics.md) · [wiki home](../index.md) · [Wire Map](Wiki-Wire-Map.md)
