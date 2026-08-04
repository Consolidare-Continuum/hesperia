# count_triangles / count_connected_triplets

**Status:** 🟢 LIVE_FULL — matches proposal (if any), running in production path  
**Category:** [Graph and Structural Metrics](../categories/Graph-and-Structural-Metrics.md)  
**Type:** Formula / function  
**Responsible (module):** `core/domain/primitive_metrics.py:122-145`  
**Value / default:** —

## In plain words

count three-node cliques (and connected triplets) in the visited graph — feeds local clustering-style metrics.

## Definition

- **Receives:** *ActiveGraph (KME concept graph)*
- **Does:** Deterministic triangle count; sum of C(deg(v),2) per node.
- **Outputs:** `—` → [KME Primitives and Derived Metrics](../pages/KME-Primitives-and-Derived-Metrics.md), [Clustering coefficient](../pages/Clustering-coefficient.md)
- **Exists for:** triangle/triplet census for clustering

## Yields (formula)

Deterministic triangle count; sum of C(deg(v),2) per node.

## Produced from (inputs)

- *ActiveGraph (KME concept graph)*

## Needed by (consumers)

- [KME Primitives and Derived Metrics](../pages/KME-Primitives-and-Derived-Metrics.md)
- [Clustering coefficient](../pages/Clustering-coefficient.md)

## See also

- [KME Primitives and Derived Metrics](../pages/KME-Primitives-and-Derived-Metrics.md)
- [Clustering coefficient](../pages/Clustering-coefficient.md)

## Origin

No Java ancestor — Theory Explainer: plain_lang: count three-node cliques (and connected triplets) in the visited graph — feeds local clustering-style metrics. author: Hesperia wiki (core/domain/primitive_metrics.py:122-145). extent: full. reasoning: triangle/triplet census for clustering. application: [KME Primitives and Derived Metrics](../pages/KME-Primitives-and-Derived-Metrics.md).

## Notes

**HWIKI-PLAIN-C:** algebra plain_lang polished 2026-08-04. **HWIKI-PLAIN-B:** plain_lang backfilled from formula/notes 2026-08-04. Feeds clustering-coefficient-style derived metrics.

---
[← back to category](../categories/Graph-and-Structural-Metrics.md) · [wiki home](../index.md) · [Wire Map](Wiki-Wire-Map.md)
