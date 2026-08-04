# Circuit rank (LOOP_COUNT/LOOP_DENSITY)

**Status:** 🟢 LIVE_FULL — matches proposal (if any), running in production path  
**Category:** [Graph and Structural Metrics](../categories/Graph-and-Structural-Metrics.md)  
**Type:** Formula / function  
**Responsible (module):** `core/layers/layer_2.py`  
**Value / default:** —

## In plain words

how many independent loops sit in the visited subgraph — cycle-space dimension E−(V−1), reported as LOOP_COUNT/LOOP_DENSITY.

## Definition

- **Receives:** [BFS depth-capped traversal](../pages/BFS-depth-capped-traversal.md)
- **Does:** LOOP_COUNT = max(0, induced_edges - used_edges); LOOP_DENSITY = LOOP_COUNT / ([TOTAL_REACHABLE_NODES](../pages/TOTAL-REACHABLE-NODES.md) + eps).
- **Outputs:** `—` → *no named wiki consumer yet*
- **Exists for:** SCIENCE.md L2 lineage

## Yields (formula)

LOOP_COUNT = max(0, induced_edges - used_edges); LOOP_DENSITY = LOOP_COUNT / ([TOTAL_REACHABLE_NODES](../pages/TOTAL-REACHABLE-NODES.md) + eps).

## Produced from (inputs)

- [BFS depth-capped traversal](../pages/BFS-depth-capped-traversal.md)

## See also

- [BFS depth-capped traversal](../pages/BFS-depth-capped-traversal.md)
- [K(R) / L(R) / fragIndex (Java)](../pages/K-R-L-R-fragIndex-Java.md)
- [Clustering coefficient](../pages/Clustering-coefficient.md)
- [L2 — Topology Traversal](../pages/L2-Topology-Traversal.md)

## Origin

Kirchhoff (1847) — Theory Explainer: plain_lang: how many independent loops sit in the visited subgraph — cycle-space dimension E−(V−1), reported as LOOP_COUNT/LOOP_DENSITY. author: Gustav Kirchhoff (1847) circuit laws / algebraic graph theory. extent: full (formula), applied to semantic activation graph not electrical circuits. reasoning: SCIENCE.md L2 lineage. application: [BFS depth-capped traversal](../pages/BFS-depth-capped-traversal.md); same discipline family as dead [K(R) / L(R) / fragIndex (Java)](../pages/K-R-L-R-fragIndex-Java.md) but different invariant (cycle rank vs component count).

## Notes

**HWIKI-DOC-20:** Algebraic graph theory cycle rank on the BFS-induced subgraph.

---
[← back to category](../categories/Graph-and-Structural-Metrics.md) · [wiki home](../index.md) · [Wire Map](Wiki-Wire-Map.md)
