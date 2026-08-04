# P_guard (guard penalty)

**Status:** 🟢 LIVE_FULL — matches proposal (if any), running in production path  
**Category:** [Core Math Contract](../categories/Core-Math-Contract.md)  
**Type:** Formula / penalty  
**Responsible (module):** `core/math/core_math.py`  
**Value / default:** k_guard = 0.30

## In plain words

guard failures are not only hard stops — they also cost governance score.

## Definition

- **Receives:** *Sigma/Gamma/Theta guards*
- **Does:** P_guard = clamp(k_guard·(sigma_fail+gamma_violation+theta_reject), 0, 1) — Sigma/Gamma/Theta guard failures taxed directly into governance.
- **Outputs:** `k_guard = 0.30` → [metric_governance](../pages/metric-governance.md), [metric_obstacle_score](../pages/metric-obstacle-score.md)
- **Exists for:** softens binary gates into a continuous health signal

## Yields (formula)

P_guard = clamp(k_guard·(sigma_fail+gamma_violation+theta_reject), 0, 1) — Sigma/Gamma/Theta guard failures taxed directly into governance.

## Produced from (inputs)

- *Sigma/Gamma/Theta guards*

## Needed by (consumers)

- [metric_governance](../pages/metric-governance.md)
- [metric_obstacle_score](../pages/metric-obstacle-score.md)

## See also

- [metric_governance](../pages/metric-governance.md)
- [metric_obstacle_score](../pages/metric-obstacle-score.md)

## Origin

22_SPEC §11 — Theory Explainer: plain_lang: guard failures are not only hard stops — they also cost governance score. author: 22_SPEC penalty suite. extent: full. reasoning: softens binary gates into a continuous health signal. application: [metric_governance](../pages/metric-governance.md), [metric_obstacle_score](../pages/metric-obstacle-score.md).

## Notes

**HWIKI-DOC-23:** Member of the five-penalty suite → [metric_governance](../pages/metric-governance.md).

---
[← back to category](../categories/Core-Math-Contract.md) · [wiki home](../index.md) · [Wire Map](Wiki-Wire-Map.md)
