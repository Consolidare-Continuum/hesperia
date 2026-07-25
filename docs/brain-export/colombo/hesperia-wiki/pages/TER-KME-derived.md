# TER (KME derived)

**Status:** 🟢 LIVE_FULL — matches proposal (if any), running in production path  
**Category:** [Graph and Structural Metrics](../categories/Graph-and-Structural-Metrics.md)  
**Type:** Derived metric (stub)  
**Responsible (module):** `hesperia/engine/kme/derived/calculator.py:97`  
**Value / default:** —

## Yields (formula)

clamp01(safe_div(CI, LD))

## Produced from (inputs)

- [KME Primitives and Derived Metrics](../pages/KME-Primitives-and-Derived-Metrics.md)

## Needed by (consumers)

- *hesperia/engine/kme/pipeline.py*
- *fingerprint/builder.py*

## Origin

BEYOND Java — pure algebra over PrimitiveMetrics (clamp01 + safe_div)

## Notes

**HWIKI-KME-01 stub:** CI/LD ratio. Consumers: pipeline / clinical_bridge / fingerprint (Felix HWIKI-KME-02). Expand theory later.

---
[← back to category](../categories/Graph-and-Structural-Metrics.md) · [wiki home](../index.md)
