# KCR (KME derived)

**Status:** 🟢 LIVE_FULL — matches proposal (if any), running in production path  
**Category:** [Graph and Structural Metrics](../categories/Graph-and-Structural-Metrics.md)  
**Type:** Derived metric  
**Responsible (module):** `core/domain/derived_metrics.py:85`  
**Value / default:** —

## Yields (formula)

clamp01(safe_div(LD, NC))

## Produced from (inputs)

- [KME Primitives and Derived Metrics](../pages/KME-Primitives-and-Derived-Metrics.md)

## Needed by (consumers)

- *core/domain/pipeline.py*
- *core/domain/fingerprint.py*

## Origin

BEYOND Java — pure algebra over PrimitiveMetrics (clamp01 + safe_div) — Theory Explainer: plain_lang: LD/NC ratio built only from LD/COH/NC/PR/PV/CI primitives. author: Hesperia KME derived layer (no classical namesake). extent: product_metric. reasoning: clamp01+safe_div keeps fingerprint comparable. application: pipeline / clinical_bridge / fingerprint.

## Notes

**HWIKI-KME-01/03:** LD/NC ratio. Formula `clamp01(safe_div(LD, NC))`. Consumers: pipeline / clinical_bridge / fingerprint (Felix HWIKI-KME-02). Not clinical TFP judgment — algebra only.

---
[← back to category](../categories/Graph-and-Structural-Metrics.md) · [wiki home](../index.md)
