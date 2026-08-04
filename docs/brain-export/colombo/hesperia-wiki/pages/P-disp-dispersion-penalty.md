# P_disp (dispersion penalty)

**Status:** 🟢 LIVE_FULL — matches proposal (if any), running in production path  
**Category:** [Core Math Contract](../categories/Core-Math-Contract.md)  
**Type:** Formula / penalty  
**Responsible (module):** `core/math/core_math.py`  
**Value / default:** k_disp = 0.25

## In plain words

smear across many sides → higher dispersion tax.

## Definition

- **Receives:** [compute_entropy (Shannon)](../pages/compute-entropy-Shannon.md)
- **Does:** P_disp = k_disp·H_norm, H_norm = H/ln(M) — normalized Shannon entropy of E_end over active sides.
- **Outputs:** `k_disp = 0.25` → [metric_governance](../pages/metric-governance.md)
- **Exists for:** same H tool as [compute_entropy (Shannon)](../pages/compute-entropy-Shannon.md)

## Yields (formula)

P_disp = k_disp·H_norm, H_norm = H/ln(M) — normalized Shannon entropy of E_end over active sides.

## Produced from (inputs)

- [compute_entropy (Shannon)](../pages/compute-entropy-Shannon.md)

## Needed by (consumers)

- [metric_governance](../pages/metric-governance.md)

## See also

- [compute_entropy (Shannon)](../pages/compute-entropy-Shannon.md)
- [metric_governance](../pages/metric-governance.md)

## Origin

22_SPEC §10 — Theory Explainer: plain_lang: smear across many sides → higher dispersion tax. author: Shannon entropy reused as penalty input. extent: full. reasoning: same H tool as [compute_entropy (Shannon)](../pages/compute-entropy-Shannon.md). application: [metric_governance](../pages/metric-governance.md).

## Notes

**HWIKI-DOC-23:** Member of the five-penalty suite → [metric_governance](../pages/metric-governance.md).

---
[← back to category](../categories/Core-Math-Contract.md) · [wiki home](../index.md) · [Wire Map](Wiki-Wire-Map.md)
