# KME Primitives and Derived Metrics

**Status:** 🔵 BEYOND — shipped in LIVE, not proposed in the Java corpus  
**Category:** [Graph and Structural Metrics](../categories/Graph-and-Structural-Metrics.md)  
**Type:** Hub / concept  
**Responsible (module):** `core/domain/derived_metrics.py + core/domain/primitive_metrics.py`  
**Value / default:** 6 primitives → 35 derived

## In plain words

PrimitiveMetrics (LD,COH,NC,PR,PV,CI) → compute_derived_metrics → DerivedMetrics (35) → to_derived_vector / fingerprint.

## Definition

- **Receives:** [compute_ld (LogicalDensity)](../pages/compute-ld-LogicalDensity.md), [compute_ci (ConcentrationIndex)](../pages/compute-ci-ConcentrationIndex.md), [compute_nc (NodeCoverage)](../pages/compute-nc-NodeCoverage.md), [largest_component_size](../pages/largest-component-size.md), [count_triangles / count_connected_triplets](../pages/count-triangles-count-connected-triplets.md)
- **Does:** Hub: PrimitiveMetrics (LD,COH,NC,PR,PV,CI) → compute_derived_metrics → DerivedMetrics (35) → to_derived_vector / fingerprint.
- **Outputs:** `6 primitives → 35 derived` → *core/domain/pipeline.py*, *hesperia/engine/kme/clinical_bridge.py*, *core/domain/fingerprint.py*, [KDI (KME derived)](../pages/KDI-KME-derived.md), [CSI (KME derived)](../pages/CSI-KME-derived.md), [SPI (KME derived)](../pages/SPI-KME-derived.md), [TDS (KME derived)](../pages/TDS-KME-derived.md), [SSS (KME derived)](../pages/SSS-KME-derived.md), [KCI (KME derived)](../pages/KCI-KME-derived.md), [CCI (KME derived)](../pages/CCI-KME-derived.md), [SPS (KME derived)](../pages/SPS-KME-derived.md), [DCI (KME derived)](../pages/DCI-KME-derived.md), [CSI2 (KME derived)](../pages/CSI2-KME-derived.md), [KEF (KME derived)](../pages/KEF-KME-derived.md), [ASS (KME derived)](../pages/ASS-KME-derived.md), [CDR (KME derived)](../pages/CDR-KME-derived.md), [KCR (KME derived)](../pages/KCR-KME-derived.md), [TCI (KME derived)](../pages/TCI-KME-derived.md), [PEI (KME derived)](../pages/PEI-KME-derived.md), [KE (KME derived)](../pages/KE-KME-derived.md), [SCS (KME derived)](../pages/SCS-KME-derived.md), [CRI (KME derived)](../pages/CRI-KME-derived.md), [KNS (KME derived)](../pages/KNS-KME-derived.md), [CII (KME derived)](../pages/CII-KME-derived.md), [TEP (KME derived)](../pages/TEP-KME-derived.md), [KSI (KME derived)](../pages/KSI-KME-derived.md), [CDD (KME derived)](../pages/CDD-KME-derived.md), [SSR (KME derived)](../pages/SSR-KME-derived.md), [TER (KME derived)](../pages/TER-KME-derived.md), [CPC (KME derived)](../pages/CPC-KME-derived.md), [KBS (KME derived)](../pages/KBS-KME-derived.md), [TRI (KME derived)](../pages/TRI-KME-derived.md), [IDE (KME derived)](../pages/IDE-KME-derived.md), [KPS (KME derived)](../pages/KPS-KME-derived.md), [TBI (KME derived)](../pages/TBI-KME-derived.md), [KDI2 (KME derived)](../pages/KDI2-KME-derived.md), [CDI (KME derived)](../pages/CDI-KME-derived.md), [KVI (KME derived)](../pages/KVI-KME-derived.md)
- **Exists for:** **HWIKI-KME-01:** Individual derived symbols below are stubs with formula+module pins from Felix HWIKI-KME-02

## Yields (formula)

Hub: PrimitiveMetrics (LD,COH,NC,PR,PV,CI) → compute_derived_metrics → DerivedMetrics (35) → to_derived_vector / fingerprint.

## Produced from (inputs)

- [compute_ld (LogicalDensity)](../pages/compute-ld-LogicalDensity.md)
- [compute_ci (ConcentrationIndex)](../pages/compute-ci-ConcentrationIndex.md)
- [compute_nc (NodeCoverage)](../pages/compute-nc-NodeCoverage.md)
- [largest_component_size](../pages/largest-component-size.md)
- [count_triangles / count_connected_triplets](../pages/count-triangles-count-connected-triplets.md)

## Needed by (consumers)

- *core/domain/pipeline.py*
- *hesperia/engine/kme/clinical_bridge.py*
- *core/domain/fingerprint.py*
- [KDI (KME derived)](../pages/KDI-KME-derived.md)
- [CSI (KME derived)](../pages/CSI-KME-derived.md)
- [SPI (KME derived)](../pages/SPI-KME-derived.md)
- [TDS (KME derived)](../pages/TDS-KME-derived.md)
- [SSS (KME derived)](../pages/SSS-KME-derived.md)
- [KCI (KME derived)](../pages/KCI-KME-derived.md)
- [CCI (KME derived)](../pages/CCI-KME-derived.md)
- [SPS (KME derived)](../pages/SPS-KME-derived.md)
- [DCI (KME derived)](../pages/DCI-KME-derived.md)
- [CSI2 (KME derived)](../pages/CSI2-KME-derived.md)
- [KEF (KME derived)](../pages/KEF-KME-derived.md)
- [ASS (KME derived)](../pages/ASS-KME-derived.md)
- [CDR (KME derived)](../pages/CDR-KME-derived.md)
- [KCR (KME derived)](../pages/KCR-KME-derived.md)
- [TCI (KME derived)](../pages/TCI-KME-derived.md)
- [PEI (KME derived)](../pages/PEI-KME-derived.md)
- [KE (KME derived)](../pages/KE-KME-derived.md)
- [SCS (KME derived)](../pages/SCS-KME-derived.md)
- [CRI (KME derived)](../pages/CRI-KME-derived.md)
- [KNS (KME derived)](../pages/KNS-KME-derived.md)
- [CII (KME derived)](../pages/CII-KME-derived.md)
- [TEP (KME derived)](../pages/TEP-KME-derived.md)
- [KSI (KME derived)](../pages/KSI-KME-derived.md)
- [CDD (KME derived)](../pages/CDD-KME-derived.md)
- [SSR (KME derived)](../pages/SSR-KME-derived.md)
- [TER (KME derived)](../pages/TER-KME-derived.md)
- [CPC (KME derived)](../pages/CPC-KME-derived.md)
- [KBS (KME derived)](../pages/KBS-KME-derived.md)
- [TRI (KME derived)](../pages/TRI-KME-derived.md)
- [IDE (KME derived)](../pages/IDE-KME-derived.md)
- [KPS (KME derived)](../pages/KPS-KME-derived.md)
- [TBI (KME derived)](../pages/TBI-KME-derived.md)
- [KDI2 (KME derived)](../pages/KDI2-KME-derived.md)
- [CDI (KME derived)](../pages/CDI-KME-derived.md)
- [KVI (KME derived)](../pages/KVI-KME-derived.md)

## See also

- [compute_ld (LogicalDensity)](../pages/compute-ld-LogicalDensity.md)
- [compute_ci (ConcentrationIndex)](../pages/compute-ci-ConcentrationIndex.md)
- [compute_nc (NodeCoverage)](../pages/compute-nc-NodeCoverage.md)
- [largest_component_size](../pages/largest-component-size.md)
- [count_triangles / count_connected_triplets](../pages/count-triangles-count-connected-triplets.md)
- [KDI (KME derived)](../pages/KDI-KME-derived.md)
- [CSI (KME derived)](../pages/CSI-KME-derived.md)
- [SPI (KME derived)](../pages/SPI-KME-derived.md)
- [TDS (KME derived)](../pages/TDS-KME-derived.md)
- [SSS (KME derived)](../pages/SSS-KME-derived.md)
- [KCI (KME derived)](../pages/KCI-KME-derived.md)
- [CCI (KME derived)](../pages/CCI-KME-derived.md)

## Origin

No Java 1:1 names — BEYOND comparability fingerprint layer — Theory Explainer: plain_lang: PrimitiveMetrics (LD,COH,NC,PR,PV,CI) → compute_derived_metrics → DerivedMetrics (35) → to_derived_vector / fingerprint. author: Hesperia wiki (core/domain/derived_metrics.py + core/domain/primitive_metrics.py). extent: full. reasoning: **HWIKI-KME-01:** Individual derived symbols below are stubs with formula+module pins from Felix HWIKI-KME-02. application: *core/domain/pipeline.py*, *hesperia/engine/kme/clinical_bridge.py*, *core/domain/fingerprint.py*.

## Notes

**HWIKI-PLAIN-B:** plain_lang backfilled from formula/notes 2026-08-04. **HWIKI-KME-01:** Individual derived symbols below are stubs with formula+module pins from Felix HWIKI-KME-02. **HWIKI-KME-03:** plain-lang / theory notes expanded on each derived page.

---
[← back to category](../categories/Graph-and-Structural-Metrics.md) · [wiki home](../index.md) · [Wire Map](Wiki-Wire-Map.md)
