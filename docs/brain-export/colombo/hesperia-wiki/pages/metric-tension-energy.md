# metric_tension_energy

**Status:** 🟢 LIVE_FULL — matches proposal (if any), running in production path  
**Category:** [Tension and Bipolar Adversity](../categories/Tension-and-Bipolar-Adversity.md)  
**Type:** Formula / function  
**Responsible (module):** `core/math/core_math.py`  
**Value / default:** —

## In plain words

how close the top two family energies are — when the gap shrinks, tension_energy rises (ambiguous which family leads).

## Definition

- **Receives:** *F_vec[288]*, [compute_tension](../pages/compute-tension.md)
- **Does:** tension_energy = 1 − gapF (gap between top-2 family energies).
- **Outputs:** `—` → *no named wiki consumer yet*
- **Exists for:** surviving v0.3-era tension name used by governance/TRIZ consumers

## Yields (formula)

tension_energy = 1 − gapF (gap between top-2 family energies).

## Produced from (inputs)

- *F_vec[288]*
- [compute_tension](../pages/compute-tension.md)

## See also

- [compute_tension](../pages/compute-tension.md)
- [contradiction_pressure -> tension_energy](../pages/contradiction-pressure-tension-energy.md)
- [compute_structural_tension](../pages/compute-structural-tension.md)

## Origin

Java 21_MATH `tensionEnergy` name — formula changed — Theory Explainer: plain_lang: how close the top two family energies are — when the gap shrinks, tension_energy rises (ambiguous which family leads). author: Hesperia wiki (core/math/core_math.py). extent: full. reasoning: surviving v0.3-era tension name used by governance/TRIZ consumers. application: *F_vec[288*].

## Notes

**HWIKI-WIRE:** attached to category anchor [compute_tension](../pages/compute-tension.md). **HWIKI-PLAIN-C:** algebra plain_lang polished 2026-08-04. **HWIKI-PLAIN-B:** plain_lang backfilled from formula/notes 2026-08-04. One of the few v0.3-era metric names that survived essentially unchanged in identifier, changed in formula. 17 files consume it across `hesperia/engine/output_trace.py` and `core/propagation/*`.

---
[← back to category](../categories/Tension-and-Bipolar-Adversity.md) · [wiki home](../index.md) · [Wire Map](Wiki-Wire-Map.md)
