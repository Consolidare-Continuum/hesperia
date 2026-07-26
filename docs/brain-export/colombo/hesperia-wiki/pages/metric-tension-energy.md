# metric_tension_energy

**Status:** 🟢 LIVE_FULL — matches proposal (if any), running in production path  
**Category:** [Tension and Bipolar Adversity](../categories/Tension-and-Bipolar-Adversity.md)  
**Type:** Formula / function  
**Responsible (module):** `core/math/core_math.py`  
**Value / default:** —

## Yields (formula)

tension_energy = 1 − gapF (gap between top-2 family energies).

## Produced from (inputs)

- *F_vec[288]*

## Origin

Java 21_MATH `tensionEnergy` name — formula changed

## Notes

One of the few v0.3-era metric names that survived essentially unchanged in identifier, changed in formula. 17 files consume it across `hesperia/engine/output_trace.py` and `core/propagation/*`.

---
[← back to category](../categories/Tension-and-Bipolar-Adversity.md) · [wiki home](../index.md)
