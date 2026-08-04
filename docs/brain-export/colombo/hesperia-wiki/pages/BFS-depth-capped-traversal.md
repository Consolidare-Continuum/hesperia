# BFS depth-capped traversal

**Status:** 🟢 LIVE_FULL — matches proposal (if any), running in production path  
**Category:** [Graph and Structural Metrics](../categories/Graph-and-Structural-Metrics.md)  
**Type:** Algorithm  
**Responsible (module):** `L2 traversal`  
**Value / default:** —

## In plain words

walk outward from the start family by unweighted shortest hops, stopping at a max depth — the L2 reachability engine.

## Definition

- **Receives:** *none declared (constant, hub, or external)*
- **Does:** Unweighted shortest paths, depth-capped breadth-first search.
- **Outputs:** `—` → [Circuit rank (LOOP_COUNT/LOOP_DENSITY)](../pages/Circuit-rank-LOOP-COUNT-LOOP-DENSITY.md), [Clustering coefficient](../pages/Clustering-coefficient.md), [L2 — Topology Traversal](../pages/L2-Topology-Traversal.md)
- **Exists for:** Moore/Lee BFS used by L2 topology

## Yields (formula)

Unweighted shortest paths, depth-capped breadth-first search.

## Needed by (consumers)

- [Circuit rank (LOOP_COUNT/LOOP_DENSITY)](../pages/Circuit-rank-LOOP-COUNT-LOOP-DENSITY.md)
- [Clustering coefficient](../pages/Clustering-coefficient.md)
- [L2 — Topology Traversal](../pages/L2-Topology-Traversal.md)

## See also

- [Circuit rank (LOOP_COUNT/LOOP_DENSITY)](../pages/Circuit-rank-LOOP-COUNT-LOOP-DENSITY.md)
- [Clustering coefficient](../pages/Clustering-coefficient.md)
- [L2 — Topology Traversal](../pages/L2-Topology-Traversal.md)

## Origin

Moore (1959) / Lee (1961) — Theory Explainer: plain_lang: walk outward from the start family by unweighted shortest hops, stopping at a max depth — the L2 reachability engine. author: Hesperia wiki (L2 traversal). extent: full. reasoning: Moore/Lee BFS used by L2 topology. application: [Circuit rank (LOOP_COUNT/LOOP_DENSITY)](../pages/Circuit-rank-LOOP-COUNT-LOOP-DENSITY.md), [Clustering coefficient](../pages/Clustering-coefficient.md).

## Notes

**HWIKI-PLAIN-C:** algebra plain_lang polished 2026-08-04. **HWIKI-PLAIN-B:** plain_lang backfilled from formula/notes 2026-08-04.

---
[← back to category](../categories/Graph-and-Structural-Metrics.md) · [wiki home](../index.md) · [Wire Map](Wiki-Wire-Map.md)
