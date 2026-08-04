# tension_from_conflict

**Status:** 🔴 DEAD — no implementation under this name or a successor formula  
**Category:** [Tension and Bipolar Adversity](../categories/Tension-and-Bipolar-Adversity.md)  
**Type:** Formula / function  
**Responsible (module):** `n/a — core/math/dict_b.py deleted (f44b3454, confirmed-dead duplicate, zero importers)`  
**Value / default:** —

## Yields (formula)

tension = min(1, C·4) from exclusion conflict energy C.

## Produced from (inputs)

- [build_exclusion_pairs / area_projection](../pages/build-exclusion-pairs-area-projection.md)
- [structural_coherence_pass](../pages/structural-coherence-pass.md)

## Origin

No direct Java ancestor

## Notes

Reclassified 2026-08-04, module path updated 2026-08-04 (same day, second pass): dict-specific logic belongs in its respective registered module (core.dict_a/core.dict_b at hesperia/modules/default/dict_{a,b}_module.py — moved same day from core/runtime/ so core/ holds no module-registry-shaped code, wired via core/engine/module_aliases.py), not in generic core/math/ — that's why core/math/dict_b.py was correctly deleted as dead duplicate, not just relocated. [compute_tension](../pages/compute-tension.md) is the live general-purpose tension formula today, but it uses a different formula (L1 abs-sum over (i,i+6) opposite pairs, not conflict-energy C — see compute_tension notes) — this specific conflict-energy channel has no successor formula anywhere in current source.

---
[← back to category](../categories/Tension-and-Bipolar-Adversity.md) · [wiki home](../index.md)
