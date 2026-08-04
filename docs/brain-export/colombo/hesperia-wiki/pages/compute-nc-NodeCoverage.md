# compute_nc (NodeCoverage)

**Status:** 🟢 LIVE_FULL — matches proposal (if any), running in production path  
**Category:** [Graph and Structural Metrics](../categories/Graph-and-Structural-Metrics.md)  
**Type:** Formula / function  
**Responsible (module):** `core/domain/primitive_metrics.py:55`  
**Value / default:** —

## In plain words

what fraction of the whole concept domain lit up — active nodes divided by total nodes (n/N).

## Definition

- **Receives:** *ActiveGraph (KME concept graph)*
- **Does:** NC = n/N — active concept nodes over the full domain node count.
- **Outputs:** `—` → [KME Primitives and Derived Metrics](../pages/KME-Primitives-and-Derived-Metrics.md)
- **Exists for:** KME primitive NC — coverage of the domain

## Yields (formula)

NC = n/N — active concept nodes over the full domain node count.

## Produced from (inputs)

- *ActiveGraph (KME concept graph)*

## Needed by (consumers)

- [KME Primitives and Derived Metrics](../pages/KME-Primitives-and-Derived-Metrics.md)

## See also

- [KME Primitives and Derived Metrics](../pages/KME-Primitives-and-Derived-Metrics.md)

## Origin

No Java ancestor — Theory Explainer: plain_lang: what fraction of the whole concept domain lit up — active nodes divided by total nodes (n/N). author: Hesperia wiki (core/domain/primitive_metrics.py:55). extent: full. reasoning: KME primitive NC — coverage of the domain. application: [KME Primitives and Derived Metrics](../pages/KME-Primitives-and-Derived-Metrics.md).

## Notes

**HWIKI-PLAIN-C:** algebra plain_lang polished 2026-08-04. **HWIKI-PLAIN-B:** plain_lang backfilled from formula/notes 2026-08-04.

---
[← back to category](../categories/Graph-and-Structural-Metrics.md) · [wiki home](../index.md) · [Wire Map](Wiki-Wire-Map.md)
