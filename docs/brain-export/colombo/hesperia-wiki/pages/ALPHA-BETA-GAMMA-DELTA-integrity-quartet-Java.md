# ALPHA/BETA/GAMMA/DELTA integrity quartet (Java)

**Status:** 🔴 DEAD — no implementation under this name or a successor formula  
**Category:** [Dead and Rejected Science](../categories/Dead-and-Rejected-Science.md)  
**Type:** Formula (never implemented)  
**Responsible (module):** `n/a — not in DEFAULT_CONFIG`  
**Value / default:** ALPHA=0.35, BETA=0.30, GAMMA=0.25, DELTA=0.20

## Yields (formula)

4-constant exponential decay model driving contextIntegrity / forecastIntegrity / regionReliability.

## Origin

Java 21_MATH v1.1 (Stability Control Formalization)

## Notes

**Documented design pivot**: shipped control is additive penalty-governance ([metric_governance](../pages/metric-governance.md)), not multiplicative exponential-integrity powers — easier to reason about and CI-test per-penalty. [LYAPUNOV_ESTIMATE / GLOBAL_STABILITY_SCORE](../pages/LYAPUNOV-ESTIMATE-GLOBAL-STABILITY-SCORE.md) is the live descendant of the same underlying question ('will this read degrade'), via a different, honestly-labeled proxy.

---
[← back to category](../categories/Dead-and-Rejected-Science.md) · [wiki home](../index.md)
