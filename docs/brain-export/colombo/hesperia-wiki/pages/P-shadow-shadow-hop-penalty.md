# P_shadow (shadow-hop penalty)

**Status:** 🟢 LIVE_FULL — matches proposal (if any), running in production path  
**Category:** [Core Math Contract](../categories/Core-Math-Contract.md)  
**Type:** Formula / penalty  
**Responsible (module):** `core/math/core_math.py`  
**Value / default:** k_shadow = 0.40, max_shadow_hops = 2

## In plain words

each shadow-propagation hop needed to correct the field costs governance; heaviest single k among the five.

## Definition

- **Receives:** [shadow_step](../pages/shadow-step.md)
- **Does:** P_shadow = k_shadow·(shadow_hops/max_shadow_hops) — the largest single weight of the five penalties.
- **Outputs:** `k_shadow = 0.40, max_shadow_hops = 2` → [metric_governance](../pages/metric-governance.md), [metric_obstacle_score](../pages/metric-obstacle-score.md)
- **Exists for:** fallback hops are expensive by design

## Yields (formula)

P_shadow = k_shadow·(shadow_hops/max_shadow_hops) — the largest single weight of the five penalties.

## Produced from (inputs)

- [shadow_step](../pages/shadow-step.md)

## Needed by (consumers)

- [metric_governance](../pages/metric-governance.md)
- [metric_obstacle_score](../pages/metric-obstacle-score.md)

## See also

- [shadow_step](../pages/shadow-step.md)
- [metric_governance](../pages/metric-governance.md)
- [metric_obstacle_score](../pages/metric-obstacle-score.md)
- [Energy conservation epsilon](../pages/Energy-conservation-epsilon.md)

## Origin

22_SPEC §11 — Theory Explainer: plain_lang: each shadow-propagation hop needed to correct the field costs governance; heaviest single k among the five. author: 22_SPEC penalty suite. extent: full. reasoning: fallback hops are expensive by design. application: [metric_governance](../pages/metric-governance.md), [metric_obstacle_score](../pages/metric-obstacle-score.md).

## Notes

**HWIKI-DOC-23:** Member of the five-penalty suite → [metric_governance](../pages/metric-governance.md).

---
[← back to category](../categories/Core-Math-Contract.md) · [wiki home](../index.md) · [Wire Map](Wiki-Wire-Map.md)
