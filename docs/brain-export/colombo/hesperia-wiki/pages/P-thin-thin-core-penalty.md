# P_thin (thin-core penalty)

**Status:** 🟢 LIVE_FULL — matches proposal (if any), running in production path  
**Category:** [Core Math Contract](../categories/Core-Math-Contract.md)  
**Type:** Formula / penalty  
**Responsible (module):** `core/math/core_math.py`  
**Value / default:** k_thin = 0.30, tau_core = 0.25

## In plain words

if the fused field leans too hard on Dict B vs Dict A, tax it as a thin core.

## Definition

- **Receives:** [alpha (fusion weight)](../pages/alpha-fusion-weight.md)
- **Does:** CoreShare = sumS/(sumS+sumL+eps); P_thin = k_thin·(1-CoreShare) — taxes energy leaning too much on Dict B (L) vs Dict A (S).
- **Outputs:** `k_thin = 0.30, tau_core = 0.25` → [metric_governance](../pages/metric-governance.md)
- **Exists for:** protects surface-biased fusion intent of [alpha (fusion weight)](../pages/alpha-fusion-weight.md)

## Yields (formula)

CoreShare = sumS/(sumS+sumL+eps); P_thin = k_thin·(1-CoreShare) — taxes energy leaning too much on Dict B (L) vs Dict A (S).

## Produced from (inputs)

- [alpha (fusion weight)](../pages/alpha-fusion-weight.md)

## Needed by (consumers)

- [metric_governance](../pages/metric-governance.md)

## See also

- [alpha (fusion weight)](../pages/alpha-fusion-weight.md)
- [metric_governance](../pages/metric-governance.md)
- [E_cap](../pages/E-cap.md)
- [eta (centroid threshold)](../pages/eta-centroid-threshold.md)
- [energy_conservation_tolerance](../pages/energy-conservation-tolerance.md)

## Origin

22_SPEC §9 — Theory Explainer: plain_lang: if the fused field leans too hard on Dict B vs Dict A, tax it as a thin core. author: 22_SPEC penalty suite. extent: full. reasoning: protects surface-biased fusion intent of [alpha (fusion weight)](../pages/alpha-fusion-weight.md). application: [metric_governance](../pages/metric-governance.md).

## Notes

**HWIKI-DOC-23:** Member of the five-penalty suite → [metric_governance](../pages/metric-governance.md).

---
[← back to category](../categories/Core-Math-Contract.md) · [wiki home](../index.md) · [Wire Map](Wiki-Wire-Map.md)
