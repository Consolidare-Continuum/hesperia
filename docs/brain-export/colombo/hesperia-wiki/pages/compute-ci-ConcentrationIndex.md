# compute_ci (ConcentrationIndex)

**Status:** 🟢 LIVE_SUCCESSOR — same idea, different name/formula than any Java ancestor  
**Category:** [Graph and Structural Metrics](../categories/Graph-and-Structural-Metrics.md)  
**Type:** Formula / function  
**Responsible (module):** `core/domain/primitive_metrics.py:64`  
**Value / default:** —

## Yields (formula)

Normalized HHI over node hit-counts: ci = (hhi-baseline)/(1-baseline).

## Produced from (inputs)

- *ActiveGraph (KME concept graph)*

## Needed by (consumers)

- [KME Primitives and Derived Metrics](../pages/KME-Primitives-and-Derived-Metrics.md)

## Origin

Java 20_GEOMETRY `C(R)` concept (dominance/concentration family)

## Notes

Same discipline as C(R)=L/active, different formula (HHI concentration, not component-ratio).

---
[← back to category](../categories/Graph-and-Structural-Metrics.md) · [wiki home](../index.md)
