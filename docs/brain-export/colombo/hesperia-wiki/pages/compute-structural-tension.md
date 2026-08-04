# compute_structural_tension

**Status:** 🟢 LIVE_SUCCESSOR — same idea, different name/formula than any Java ancestor  
**Category:** [Tension and Bipolar Adversity](../categories/Tension-and-Bipolar-Adversity.md)  
**Type:** Formula / function  
**Responsible (module):** `core/math/stability_metrics.py`  
**Value / default:** —

## In plain words

how contested the area field is — one minus the dominant area's share of total activation (closer to 1 means no clear winner).

## Definition

- **Receives:** *A_vec[12] (area activation vector)*, [compute_tension](../pages/compute-tension.md)
- **Does:** structural_tension = 1 − max(area)/sum(area) — dominance-competition tension.
- **Outputs:** `—` → *no named wiki consumer yet*
- **Exists for:** dominance-competition tension; HHI-adjacent building block

## Yields (formula)

structural_tension = 1 − max(area)/sum(area) — dominance-competition tension.

## Produced from (inputs)

- *A_vec[12] (area activation vector)*
- [compute_tension](../pages/compute-tension.md)

## See also

- [compute_tension](../pages/compute-tension.md)
- [metric_tension_energy](../pages/metric-tension-energy.md)

## Origin

No direct Java ancestor named this way — Theory Explainer: plain_lang: how contested the area field is — one minus the dominant area's share of total activation (closer to 1 means no clear winner). author: Hesperia wiki (core/math/stability_metrics.py). extent: full. reasoning: dominance-competition tension; HHI-adjacent building block. application: [[A_vec[12] (area activation vector)]].

## Notes

**HWIKI-WIRE:** attached to category anchor [compute_tension](../pages/compute-tension.md). **HWIKI-PLAIN-C:** algebra plain_lang polished 2026-08-04. **HWIKI-PLAIN-B:** plain_lang backfilled from formula/notes 2026-08-04. Max-share concentration, HHI-adjacent building block.

---
[← back to category](../categories/Tension-and-Bipolar-Adversity.md) · [wiki home](../index.md) · [Wire Map](Wiki-Wire-Map.md)
