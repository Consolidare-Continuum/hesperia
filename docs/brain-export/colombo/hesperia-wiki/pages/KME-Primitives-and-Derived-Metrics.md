# KME Primitives and Derived Metrics

**Status:** 🔵 BEYOND — shipped in LIVE, not proposed in the Java corpus  
**Category:** [Graph and Structural Metrics](../categories/Graph-and-Structural-Metrics.md)  
**Type:** Hub / concept  
**Responsible (module):** `hesperia/engine/kme/derived/calculator.py + primitives/calculator.py`  
**Value / default:** 6 primitives → 35 derived

## Yields (formula)

Hub: PrimitiveMetrics (LD,COH,NC,PR,PV,CI) → compute_derived_metrics → DerivedMetrics (35) → to_derived_vector / fingerprint.

## Produced from (inputs)

- [compute_ld (LogicalDensity)](../pages/compute-ld-LogicalDensity.md)
- [compute_ci (ConcentrationIndex)](../pages/compute-ci-ConcentrationIndex.md)
- [compute_nc (NodeCoverage)](../pages/compute-nc-NodeCoverage.md)
- [largest_component_size](../pages/largest-component-size.md)
- [count_triangles / count_connected_triplets](../pages/count-triangles-count-connected-triplets.md)

## Needed by (consumers)

- *hesperia/engine/kme/pipeline.py*
- *clinical_bridge.py*
- *fingerprint/builder.py*

## Origin

No Java 1:1 names — BEYOND comparability fingerprint layer

## Notes

**HWIKI-KME-01:** Individual derived symbols below are stubs with formula+module pins from Felix HWIKI-KME-02. **HWIKI-KME-03:** plain-lang / theory notes expanded on each derived page.

---
[← back to category](../categories/Graph-and-Structural-Metrics.md) · [wiki home](../index.md)
