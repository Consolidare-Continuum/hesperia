# CCI (KME derived)

**Status:** 🟢 LIVE_FULL — matches proposal (if any), running in production path  
**Category:** [Graph and Structural Metrics](../categories/Graph-and-Structural-Metrics.md)  
**Type:** Derived metric  
**Responsible (module):** `hesperia/engine/kme/derived/calculator.py:78`  
**Value / default:** —

## Yields (formula)

clamp01(COH * NC)

## Produced from (inputs)

- [KME Primitives and Derived Metrics](../pages/KME-Primitives-and-Derived-Metrics.md)

## Needed by (consumers)

- *hesperia/engine/kme/pipeline.py*
- *fingerprint/builder.py*

## Origin

BEYOND Java — pure algebra over PrimitiveMetrics (clamp01 + safe_div) — Theory Explainer: plain_lang: COH×NC product built only from LD/COH/NC/PR/PV/CI primitives. author: Hesperia KME derived layer (no classical namesake). extent: product_metric. reasoning: clamp01+safe_div keeps fingerprint comparable. application: pipeline / clinical_bridge / fingerprint.

## Notes

**HWIKI-KME-01/03:** COH×NC product. Formula `clamp01(COH * NC)`. Consumers: pipeline / clinical_bridge / fingerprint (Felix HWIKI-KME-02). Not clinical TFP judgment — algebra only.

---
[← back to category](../categories/Graph-and-Structural-Metrics.md) · [wiki home](../index.md)
