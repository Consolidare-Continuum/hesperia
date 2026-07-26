# P_amb (ambiguity penalty)

**Status:** 🟢 LIVE_FULL — matches proposal (if any), running in production path  
**Category:** [Core Math Contract](../categories/Core-Math-Contract.md)  
**Type:** Formula / penalty  
**Responsible (module):** `core/math/core_math.py`  
**Value / default:** k_amb = 0.35, delta_gap = 0.08

## Yields (formula)

gap = (e1-e2)/(e1+eps); P_amb = k_amb·(1-gap)^2 — taxes a too-close top-1/top-2 energy gap; degraded flag if gap < delta_gap.

## Produced from (inputs)

- *base_step*

## Needed by (consumers)

- [metric_governance](../pages/metric-governance.md)

## Origin

22_SPEC §8 — Theory Explainer: plain_lang: if top-1 and top-2 energies are almost tied, tax governance — the read is ambiguous. author: 22_SPEC penalty suite. extent: full. reasoning: independently tunable additive term. application: [metric_governance](../pages/metric-governance.md).

## Notes

**HWIKI-DOC-23:** Member of the five-penalty suite → [metric_governance](../pages/metric-governance.md).

---
[← back to category](../categories/Core-Math-Contract.md) · [wiki home](../index.md)
