# ultra_sparse_coverage_threshold

**Status:** 🟢 LIVE_FULL — matches proposal (if any), running in production path  
**Category:** [Activation and Diagnostic Thresholds](../categories/Activation-and-Diagnostic-Thresholds.md)  
**Type:** Parameter (constants)  
**Responsible (module):** `specs/canon/diagnostic_rules.yaml + sphere/diagnostics/anomaly_detector.py`  
**Value / default:** 0.02

## Yields (formula)

Below this coverage, the read is flagged zero-signal / anomalous rather than substantive structure.

## Needed by (consumers)

- *sphere/diagnostics/anomaly_detector.py*

## Origin

parameter_catalog.md §4

## Notes

**HWIKI-CAT-02:** From CAT-01 delta — diagnostic ultra-sparse gate.

---
[← back to category](../categories/Activation-and-Diagnostic-Thresholds.md) · [wiki home](../index.md)
