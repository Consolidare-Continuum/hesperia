# compute_ld (LogicalDensity)

**Status:** 🟢 LIVE_FULL — matches proposal (if any), running in production path  
**Category:** [Graph and Structural Metrics](../categories/Graph-and-Structural-Metrics.md)  
**Type:** Formula / function  
**Responsible (module):** `core/domain/primitive_metrics.py:84`  
**Value / default:** —

## In plain words

how densely the active concept graph is wired — average degree of active nodes over a high-degree reference (Deg95), clamped to [0,1].

## Definition

- **Receives:** *ActiveGraph (KME concept graph)*
- **Does:** ld = avgActiveDegree / Deg95, clamped to [0,1].
- **Outputs:** `—` → [KME Primitives and Derived Metrics](../pages/KME-Primitives-and-Derived-Metrics.md)
- **Exists for:** KME primitive LD — connectivity intensity of the live subgraph

## Yields (formula)

ld = avgActiveDegree / Deg95, clamped to [0,1].

## Produced from (inputs)

- *ActiveGraph (KME concept graph)*

## Needed by (consumers)

- [KME Primitives and Derived Metrics](../pages/KME-Primitives-and-Derived-Metrics.md)

## See also

- [KME Primitives and Derived Metrics](../pages/KME-Primitives-and-Derived-Metrics.md)

## Origin

No Java ancestor — Theory Explainer: plain_lang: how densely the active concept graph is wired — average degree of active nodes over a high-degree reference (Deg95), clamped to [0,1]. author: Hesperia wiki (core/domain/primitive_metrics.py:84). extent: full. reasoning: KME primitive LD — connectivity intensity of the live subgraph. application: [KME Primitives and Derived Metrics](../pages/KME-Primitives-and-Derived-Metrics.md).

## Notes

**HWIKI-PLAIN-C:** algebra plain_lang polished 2026-08-04. **HWIKI-PLAIN-B:** plain_lang backfilled from formula/notes 2026-08-04.

---
[← back to category](../categories/Graph-and-Structural-Metrics.md) · [wiki home](../index.md) · [Wire Map](Wiki-Wire-Map.md)
