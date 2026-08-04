# compute_ci (ConcentrationIndex)

**Status:** 🟢 LIVE_SUCCESSOR — same idea, different name/formula than any Java ancestor  
**Category:** [Graph and Structural Metrics](../categories/Graph-and-Structural-Metrics.md)  
**Type:** Formula / function  
**Responsible (module):** `core/domain/primitive_metrics.py:64`  
**Value / default:** —

## In plain words

how piled-up hits are on a few nodes versus spread evenly — a normalized Herfindahl (HHI) concentration score on node hit-counts.

## Definition

- **Receives:** *ActiveGraph (KME concept graph)*
- **Does:** Normalized HHI over node hit-counts: ci = (hhi-baseline)/(1-baseline).
- **Outputs:** `—` → [KME Primitives and Derived Metrics](../pages/KME-Primitives-and-Derived-Metrics.md)
- **Exists for:** KME primitive CI — concentration, not component count

## Yields (formula)

Normalized HHI over node hit-counts: ci = (hhi-baseline)/(1-baseline).

## Produced from (inputs)

- *ActiveGraph (KME concept graph)*

## Needed by (consumers)

- [KME Primitives and Derived Metrics](../pages/KME-Primitives-and-Derived-Metrics.md)

## See also

- [KME Primitives and Derived Metrics](../pages/KME-Primitives-and-Derived-Metrics.md)

## Origin

Java 20_GEOMETRY `C(R)` concept (dominance/concentration family) — Theory Explainer: plain_lang: how piled-up hits are on a few nodes versus spread evenly — a normalized Herfindahl (HHI) concentration score on node hit-counts. author: Hesperia wiki (core/domain/primitive_metrics.py:64). extent: full. reasoning: KME primitive CI — concentration, not component count. application: [KME Primitives and Derived Metrics](../pages/KME-Primitives-and-Derived-Metrics.md).

## Notes

**HWIKI-PLAIN-C:** algebra plain_lang polished 2026-08-04. **HWIKI-PLAIN-B:** plain_lang backfilled from formula/notes 2026-08-04. Same discipline as C(R)=L/active, different formula (HHI concentration, not component-ratio).

---
[← back to category](../categories/Graph-and-Structural-Metrics.md) · [wiki home](../index.md) · [Wire Map](Wiki-Wire-Map.md)
