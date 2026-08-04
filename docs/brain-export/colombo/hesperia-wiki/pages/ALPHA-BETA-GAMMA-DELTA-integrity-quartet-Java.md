# ALPHA/BETA/GAMMA/DELTA integrity quartet (Java)

**Status:** 🔴 DEAD — no implementation under this name or a successor formula  
**Category:** [Dead and Rejected Science](../categories/Dead-and-Rejected-Science.md)  
**Type:** Formula (never implemented)  
**Responsible (module):** `n/a — not in DEFAULT_CONFIG`  
**Value / default:** ALPHA=0.35, BETA=0.30, GAMMA=0.25, DELTA=0.20

## In plain words

4-constant exponential decay model driving contextIntegrity / forecastIntegrity / regionReliability.

## Definition

- **Receives:** *none declared (constant, hub, or external)*
- **Does:** 4-constant exponential [decay](../pages/decay.md) model driving contextIntegrity / forecastIntegrity / regionReliability.
- **Outputs:** `ALPHA=0.35, BETA=0.30, GAMMA=0.25, DELTA=0.20` → [metric_governance](../pages/metric-governance.md)
- **Exists for:** shipped control is additive penalty-governance ([metric_governance](../pages/metric-governance.md)), not multiplicative exponential-integrity powers — easier to reason about and CI-test per-penalty

## Yields (formula)

4-constant exponential [decay](../pages/decay.md) model driving contextIntegrity / forecastIntegrity / regionReliability.

## Needed by (consumers)

- [metric_governance](../pages/metric-governance.md)

## See also

- [metric_governance](../pages/metric-governance.md)

## Origin

Java 21_MATH v1.1 (Stability Control Formalization) — Theory Explainer: plain_lang: 4-constant exponential decay model driving contextIntegrity / forecastIntegrity / regionReliability. author: Hesperia wiki (n/a — not in DEFAULT_CONFIG). extent: dead. reasoning: shipped control is additive penalty-governance ([metric_governance](../pages/metric-governance.md)), not multiplicative exponential-integrity powers — easier to reason about and CI-test per-penalty. application: Dead and Rejected Science.

## Notes

**HWIKI-PLAIN-B:** plain_lang backfilled from formula/notes 2026-08-04. **Documented design pivot**: shipped control is additive penalty-governance ([metric_governance](../pages/metric-governance.md)), not multiplicative exponential-integrity powers — easier to reason about and CI-test per-penalty. [LYAPUNOV_ESTIMATE / GLOBAL_STABILITY_SCORE](../pages/LYAPUNOV-ESTIMATE-GLOBAL-STABILITY-SCORE.md) is the live descendant of the same underlying question ('will this read degrade'), via a different, honestly-labeled proxy.

---
[← back to category](../categories/Dead-and-Rejected-Science.md) · [wiki home](../index.md) · [Wire Map](Wiki-Wire-Map.md)
