# OPPOSITE_OFFSET

**Status:** 🔴 DEAD (name) / 🟢 ALGORITHM SURVIVED — see linked live page  
**Category:** [Tension and Bipolar Adversity](../categories/Tension-and-Bipolar-Adversity.md)  
**Type:** Parameter (constant)  
**Responsible (module):** `core/result/contract.py:64 (inlined `i, i+6` in compute_tension)`  
**Value / default:** 6

## In plain words

Offset defining opposite-area exclusion pairs (i, i+6), same offset [compute_tension](../pages/compute-tension.md) uses.

## Definition

- **Receives:** [Icosahedral Surface Graph](../pages/Icosahedral-Surface-Graph.md)
- **Does:** Offset defining opposite-area exclusion pairs (i, i+6), same offset [compute_tension](../pages/compute-tension.md) uses.
- **Outputs:** `6` → [compute_tension](../pages/compute-tension.md), [build_exclusion_pairs / area_projection](../pages/build-exclusion-pairs-area-projection.md)
- **Exists for:** **Not geometric antipodes.** After `get_aligned_area_coordinates`, true antipodes are a different pairing (see compute_tension HWIKI-OPEN-01)

## Yields (formula)

Offset defining opposite-area exclusion pairs (i, i+6), same offset [compute_tension](../pages/compute-tension.md) uses.

## Produced from (inputs)

- [Icosahedral Surface Graph](../pages/Icosahedral-Surface-Graph.md)

## Needed by (consumers)

- [compute_tension](../pages/compute-tension.md)
- [build_exclusion_pairs / area_projection](../pages/build-exclusion-pairs-area-projection.md)

## See also

- [Icosahedral Surface Graph](../pages/Icosahedral-Surface-Graph.md)
- [compute_tension](../pages/compute-tension.md)
- [build_exclusion_pairs / area_projection](../pages/build-exclusion-pairs-area-projection.md)

## Origin

Java 21_MATH bipolar axis convention (offset changed from interleaved to +6) — Theory Explainer: plain_lang: Offset defining opposite-area exclusion pairs (i, i+6), same offset [compute_tension](../pages/compute-tension.md) uses. author: Hesperia wiki (core/result/contract.py:64 (inlined `i, i+6` in compute_tension)). extent: structural_analogy. reasoning: **Not geometric antipodes.** After `get_aligned_area_coordinates`, true antipodes are a different pairing (see compute_tension HWIKI-OPEN-01). application: [compute_tension](../pages/compute-tension.md), [build_exclusion_pairs / area_projection](../pages/build-exclusion-pairs-area-projection.md).

## Notes

**HWIKI-PLAIN-B:** plain_lang backfilled from formula/notes 2026-08-04. **Not geometric antipodes.** After `get_aligned_area_coordinates`, true antipodes are a different pairing (see [compute_tension](../pages/compute-tension.md) HWIKI-OPEN-01). OPPOSITE_OFFSET is the shipped bipolar *index* convention. Reclassified 2026-08-04: no longer a named module constant since core/math/dict_b.py was deleted (f44b3454) as dead duplicate — but the `+6` pairing it defined is inlined verbatim in [compute_tension](../pages/compute-tension.md)'s `pairs = [(i, i + 6) for i in range(6)]`, so the value/algorithm survives even though the standalone constant does not.

---
[← back to category](../categories/Tension-and-Bipolar-Adversity.md) · [wiki home](../index.md) · [Wire Map](Wiki-Wire-Map.md)
