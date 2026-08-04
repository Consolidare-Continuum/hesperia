# Clustering coefficient

**Status:** 🟡 PARTIAL — present in a narrow slice/tool, not the full contract  
**Category:** [Graph and Structural Metrics](../categories/Graph-and-Structural-Metrics.md)  
**Type:** Formula  
**Responsible (module):** `core/layers/layer_2.py:_compute_clustering (LOCAL_CLUSTERING_COEFFICIENT)`  
**Value / default:** C(v) = 2t/(k(k-1))

## In plain words

of the friends of a node, how many are friends with each other — a local clumpiness score.

## Definition

- **Receives:** [count_triangles / count_connected_triplets](../pages/count-triangles-count-connected-triplets.md), [BFS depth-capped traversal](../pages/BFS-depth-capped-traversal.md)
- **Does:** Local clustering at the dominant family / start node of the L2 BFS.
- **Outputs:** `C(v) = 2t/(k(k-1))` → [KME Primitives and Derived Metrics](../pages/KME-Primitives-and-Derived-Metrics.md)
- **Exists for:** SCIENCE.md L2; code pin `_compute_clustering` in `layer_2.py`

## Yields (formula)

Local clustering at the dominant family / start node of the L2 BFS.

## Produced from (inputs)

- [count_triangles / count_connected_triplets](../pages/count-triangles-count-connected-triplets.md)
- [BFS depth-capped traversal](../pages/BFS-depth-capped-traversal.md)

## Needed by (consumers)

- [KME Primitives and Derived Metrics](../pages/KME-Primitives-and-Derived-Metrics.md)

## See also

- [count_triangles / count_connected_triplets](../pages/count-triangles-count-connected-triplets.md)
- [BFS depth-capped traversal](../pages/BFS-depth-capped-traversal.md)
- [KME Primitives and Derived Metrics](../pages/KME-Primitives-and-Derived-Metrics.md)
- [Circuit rank (LOOP_COUNT/LOOP_DENSITY)](../pages/Circuit-rank-LOOP-COUNT-LOOP-DENSITY.md)
- [L2 — Topology Traversal](../pages/L2-Topology-Traversal.md)

## Origin

Watts & Strogatz (1998) — Theory Explainer: plain_lang: of the friends of a node, how many are friends with each other — a local clumpiness score. author: Duncan Watts & Steven Strogatz (1998). extent: partial — formula verbatim at dominant/start node only; full small-world network model not adopted. reasoning: SCIENCE.md L2; code pin `_compute_clustering` in `layer_2.py`. application: [count_triangles / count_connected_triplets](../pages/count-triangles-count-connected-triplets.md), L2 LOCAL_CLUSTERING_COEFFICIENT.

## Notes

**HWIKI-DOC-19:** PARTIAL + code pin — formula only, not the full small-world apparatus. Felix verify: `core/layers/layer_2.py` lines ~42–43, ~142.

---
[← back to category](../categories/Graph-and-Structural-Metrics.md) · [wiki home](../index.md) · [Wire Map](Wiki-Wire-Map.md)
