# decay

**Status:** 🟢 LIVE_FULL — matches proposal (if any), running in production path  
**Category:** [Core Math Contract](../categories/Core-Math-Contract.md)  
**Type:** Parameter (constant)  
**Responsible (module):** `core/math/core_math.py — base_step()`  
**Value / default:** 0.04

## In plain words

after each diffusion step, shrink remaining energy by a fixed fraction so the field does not stay forever-hot — damped attrition before the next step.

## Definition

- **Receives:** [lambda (lazy step)](../pages/lambda-lazy-step.md)
- **Does:** E_next = clamp(D·(1-decay), 0, [E_cap](../pages/E-cap.md)) — damped discrete-time attrition after each diffusion step.
- **Outputs:** `0.04` → [metric_obstacle_score](../pages/metric-obstacle-score.md)
- **Exists for:** discrete-time attrition after diffusion; partner of [E_cap](../pages/E-cap.md)

## Yields (formula)

E_next = clamp(D·(1-decay), 0, [E_cap](../pages/E-cap.md)) — damped discrete-time attrition after each diffusion step.

## Produced from (inputs)

- [lambda (lazy step)](../pages/lambda-lazy-step.md)

## Needed by (consumers)

- [metric_obstacle_score](../pages/metric-obstacle-score.md)

## See also

- [lambda (lazy step)](../pages/lambda-lazy-step.md)
- [metric_obstacle_score](../pages/metric-obstacle-score.md)
- [Energy conservation epsilon](../pages/Energy-conservation-epsilon.md)

## Origin

22_SPEC §5 — Theory Explainer: plain_lang: after each diffusion step, shrink remaining energy by a fixed fraction so the field does not stay forever-hot — damped attrition before the next step. author: Hesperia wiki (core/math/core_math.py — base_step()). extent: full. reasoning: discrete-time attrition after diffusion; partner of [E_cap](../pages/E-cap.md). application: [lambda (lazy step)](../pages/lambda-lazy-step.md).

## Notes

**HWIKI-PLAIN-C:** algebra plain_lang polished 2026-08-04. **HWIKI-PLAIN-B:** plain_lang backfilled from formula/notes 2026-08-04. Structural analogy to LIF self-decay (Lapicque 1907) noted in related H_self paths; not claimed as literal.

---
[← back to category](../categories/Core-Math-Contract.md) · [wiki home](../index.md) · [Wire Map](Wiki-Wire-Map.md)
