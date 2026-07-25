# count_triangles / count_connected_triplets

**Status:** 🟢 LIVE_FULL — matches proposal (if any), running in production path  
**Category:** [Graph and Structural Metrics](../categories/Graph-and-Structural-Metrics.md)  
**Type:** Formula / function  
**Responsible (module):** `hesperia/engine/kme/primitives/calculator.py:122-145`  
**Value / default:** —

## Yields (formula)

Deterministic triangle count; sum of C(deg(v),2) per node.

## Produced from (inputs)

- *ActiveGraph (KME concept graph)*

## Needed by (consumers)

- [KME Primitives and Derived Metrics](../pages/KME-Primitives-and-Derived-Metrics.md)

## Origin

No Java ancestor

## Notes

Feeds clustering-coefficient-style derived metrics.

---
[← back to category](../categories/Graph-and-Structural-Metrics.md) · [wiki home](../index.md)
