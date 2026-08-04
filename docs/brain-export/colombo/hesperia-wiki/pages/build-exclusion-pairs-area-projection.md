# build_exclusion_pairs / area_projection

**Status:** 🔴 DEAD (name) / 🟢 ALGORITHM SURVIVED — see linked live page  
**Category:** [Concept Dictionary](../categories/Concept-Dictionary.md)  
**Type:** Formula / function  
**Responsible (module):** `core/result/contract.py:64 (inlined `i, i+6` in compute_tension)`  
**Value / default:** —

## Yields (formula)

Constructs opposite-area exclusion pairs and projects weights onto areas.

## Produced from (inputs)

- [OPPOSITE_OFFSET](../pages/OPPOSITE-OFFSET.md)

## Needed by (consumers)

- [structural_coherence_pass](../pages/structural-coherence-pass.md)
- [tension_from_conflict](../pages/tension-from-conflict.md)

## Origin

No direct Java ancestor

## Notes

Reclassified 2026-08-04: no standalone function survives (core/math/dict_b.py deleted, f44b3454), but the exclusion-pair construction itself is inlined verbatim as `pairs = [(i, i + 6) for i in range(6)]` inside [compute_tension](../pages/compute-tension.md) — same as [OPPOSITE_OFFSET](../pages/OPPOSITE-OFFSET.md)'s finding. Not to be confused with `build_family_area_projection` in sphere/propagation/family_projection.py — despite the similar name, that function distributes propagated mass across families within an area (a different job); it is not this function's successor.

---
[← back to category](../categories/Concept-Dictionary.md) · [wiki home](../index.md)
