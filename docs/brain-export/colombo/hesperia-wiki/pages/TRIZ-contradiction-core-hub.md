# TRIZ contradiction core hub

**Status:** 🔵 BEYOND — shipped in LIVE, not proposed in the Java corpus  
**Category:** [Graph and Structural Metrics](../categories/Graph-and-Structural-Metrics.md)  
**Type:** Hub / concept  
**Responsible (module):** `hesperia/extensions/triz/{pipeline,contradiction_engine,triz_classifier,contradiction_contract}.py`  
**Value / default:** —

## Yields (formula)

Hub: run_triz_layer / detect_contradictions / classify_contradiction(s) over ContradictionSignal models; contract forbids synonym drift.

## Produced from (inputs)

- [Louvain communities (seed 42)](../pages/Louvain-communities-seed-42.md)

## Needed by (consumers)

- *TRIZ pipeline.run_triz_layer*
- *contradiction_engine.detect_contradictions*
- *triz_classifier.classify_contradiction*

## Origin

extensions/triz — Class B inventives surface

## Notes

**HWIKI-TRIZ-02:** Core hub beyond Louvain inventory (TRIZ-01). Pins: pipeline.py, contradiction_engine.py, triz_classifier.py, contradiction_contract.py.

---
[← back to category](../categories/Graph-and-Structural-Metrics.md) · [wiki home](../index.md)
