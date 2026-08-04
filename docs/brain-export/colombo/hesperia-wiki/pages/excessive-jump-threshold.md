# excessive_jump_threshold

**Status:** 🟢 LIVE_FULL — matches proposal (if any), running in production path  
**Category:** [Activation and Diagnostic Thresholds](../categories/Activation-and-Diagnostic-Thresholds.md)  
**Type:** Parameter (constants)  
**Responsible (module):** `specs/canon/diagnostic_rules.yaml + sphere/diagnostics/anomaly_detector.py`  
**Value / default:** 0.60

## Yields (formula)

Above this, a single-step trajectory change is anomalous rather than normal dynamics.

## Needed by (consumers)

- *sphere/diagnostics/anomaly_detector.py*

## Origin

parameter_catalog.md §4

## Notes

**HWIKI-CAT-02:** CAT-01 delta — change-point / jump anomaly.

---
[← back to category](../categories/Activation-and-Diagnostic-Thresholds.md) · [wiki home](../index.md)
