# OPPOSITE_OFFSET

**Status:** 🟢 LIVE_FULL — matches proposal (if any), running in production path  
**Category:** [Tension and Bipolar Adversity](../categories/Tension-and-Bipolar-Adversity.md)  
**Type:** Parameter (constant)  
**Responsible (module):** `core/math/dict_b.py:26`  
**Value / default:** 6

## Yields (formula)

Offset defining opposite-area exclusion pairs (i, i+6), same offset compute_tension uses.

## Produced from (inputs)

- [Icosahedral Surface Graph](../pages/Icosahedral-Surface-Graph.md)

## Needed by (consumers)

- [compute_tension](../pages/compute-tension.md)
- *build_exclusion_pairs*

## Origin

Java 21_MATH bipolar axis convention (offset changed from interleaved to +6)

## Notes

**Not geometric antipodes.** After `get_aligned_area_coordinates`, true antipodes are a different pairing (see [compute_tension](../pages/compute-tension.md) HWIKI-OPEN-01). OPPOSITE_OFFSET is the shipped bipolar *index* convention.

---
[← back to category](../categories/Tension-and-Bipolar-Adversity.md) · [wiki home](../index.md)
