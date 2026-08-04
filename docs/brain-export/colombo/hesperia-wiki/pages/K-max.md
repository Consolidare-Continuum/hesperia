# K_max

**Status:** 🟢 LIVE_FULL — matches proposal (if any), running in production path  
**Category:** [Core Math Contract](../categories/Core-Math-Contract.md)  
**Type:** Parameter (constant)  
**Responsible (module):** `core/math/core_math.py`  
**Value / default:** 5

## In plain words

hard cap on how many centroid indices may be selected as 'active' in one traversal.

## Definition

- **Receives:** [eta (centroid threshold)](../pages/eta-centroid-threshold.md)
- **Does:** Cap on the number of centroid indices selected.
- **Outputs:** `5` → *no named wiki consumer yet*
- **Exists for:** limits how many simultaneous activation foci the core math keeps

## Yields (formula)

Cap on the number of centroid indices selected.

## Produced from (inputs)

- [eta (centroid threshold)](../pages/eta-centroid-threshold.md)

## See also

- [eta (centroid threshold)](../pages/eta-centroid-threshold.md)

## Origin

22_SPEC §4 — Theory Explainer: plain_lang: hard cap on how many centroid indices may be selected as 'active' in one traversal. author: Hesperia wiki (core/math/core_math.py). extent: full. reasoning: limits how many simultaneous activation foci the core math keeps. application: [eta (centroid threshold)](../pages/eta-centroid-threshold.md).

## Notes

**HWIKI-PLAIN-C:** algebra plain_lang polished 2026-08-04. **HWIKI-PLAIN-B:** plain_lang backfilled from formula/notes 2026-08-04. Caps 'how many things are active' in one traversal.

---
[← back to category](../categories/Core-Math-Contract.md) · [wiki home](../index.md) · [Wire Map](Wiki-Wire-Map.md)
