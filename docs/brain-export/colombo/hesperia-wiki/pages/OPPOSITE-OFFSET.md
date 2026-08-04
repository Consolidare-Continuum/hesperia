# OPPOSITE_OFFSET

**Status:** 🔴 DEAD (name) / 🟢 ALGORITHM SURVIVED — see linked live page  
**Category:** [Tension and Bipolar Adversity](../categories/Tension-and-Bipolar-Adversity.md)  
**Type:** Parameter (constant)  
**Responsible (module):** `core/result/contract.py:64 (inlined `i, i+6` in compute_tension)`  
**Value / default:** 6

## Yields (formula)

Offset defining opposite-area exclusion pairs (i, i+6), same offset compute_tension uses.

## Produced from (inputs)

- [Icosahedral Surface Graph](../pages/Icosahedral-Surface-Graph.md)

## Needed by (consumers)

- [compute_tension](../pages/compute-tension.md)
- [build_exclusion_pairs / area_projection](../pages/build-exclusion-pairs-area-projection.md)

## Origin

Java 21_MATH bipolar axis convention (offset changed from interleaved to +6)

## Notes

**Not geometric antipodes.** After `get_aligned_area_coordinates`, true antipodes are a different pairing (see [compute_tension](../pages/compute-tension.md) HWIKI-OPEN-01). OPPOSITE_OFFSET is the shipped bipolar *index* convention. Reclassified 2026-08-04: no longer a named module constant since core/math/dict_b.py was deleted (f44b3454) as dead duplicate — but the `+6` pairing it defined is inlined verbatim in [compute_tension](../pages/compute-tension.md)'s `pairs = [(i, i + 6) for i in range(6)]`, so the value/algorithm survives even though the standalone constant does not.

---
[← back to category](../categories/Tension-and-Bipolar-Adversity.md) · [wiki home](../index.md)
