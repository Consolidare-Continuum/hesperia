# KDI (KME derived)

**Status:** 🟢 LIVE_FULL — matches proposal (if any), running in production path  
**Category:** [Graph and Structural Metrics](../categories/Graph-and-Structural-Metrics.md)  
**Type:** Derived metric  
**Responsible (module):** `core/domain/derived_metrics.py:72`  
**Value / default:** —

## In plain words

Knowledge Density Index — a clamped [0,1] fingerprint feature from KME primitives (LD=logical density, COH=coherence, NC=node coverage, PR=presence, PV=volume, CI=concentration); algebra `clamp01(LD * COH)` only, not a clinical TFP judgment.

## Definition

- **Receives:** [KME Primitives and Derived Metrics](../pages/KME-Primitives-and-Derived-Metrics.md)
- **Does:** clamp01(LD * COH)
- **Outputs:** `—` → *core/domain/pipeline.py*, *core/domain/fingerprint.py*
- **Exists for:** clamp01+safe_div keeps fingerprint comparable across runs

## Yields (formula)

clamp01(LD * COH)

## Produced from (inputs)

- [KME Primitives and Derived Metrics](../pages/KME-Primitives-and-Derived-Metrics.md)

## Needed by (consumers)

- *core/domain/pipeline.py*
- *core/domain/fingerprint.py*

## See also

- [KME Primitives and Derived Metrics](../pages/KME-Primitives-and-Derived-Metrics.md)
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

## Origin

BEYOND Java — pure algebra over PrimitiveMetrics (clamp01 + safe_div) — Theory Explainer: plain_lang: Knowledge Density Index — a clamped [0,1] fingerprint feature from KME primitives (LD=logical density, COH=coherence, NC=node coverage, PR=presence, PV=volume, CI=concentration); algebra `clamp01(LD * COH)` only, not a clinical TFP judgment. author: Hesperia KME derived layer (no classical namesake). extent: product_metric. reasoning: clamp01+safe_div keeps fingerprint comparable across runs. application: pipeline / clinical_bridge / fingerprint.

## Notes

**HWIKI-KME-01/03 / HWIKI-PLAIN-C:** Knowledge Density Index. Formula `clamp01(LD * COH)`. Consumers: pipeline / clinical_bridge / fingerprint (Felix HWIKI-KME-02). Not clinical TFP judgment — algebra only.

---
[← back to category](../categories/Graph-and-Structural-Metrics.md) · [wiki home](../index.md) · [Wire Map](Wiki-Wire-Map.md)
