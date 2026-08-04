# TOTAL_HEXES

**Status:** 🟢 LIVE_FULL — matches proposal (if any), running in production path  
**Category:** [Geometry](../categories/Geometry.md)  
**Type:** Derived variable  
**Responsible (module):** `hex census tooling`  
**Value / default:** 72,000 (72,240 GCS defect variant)

## In plain words

finest hex count under the ontology — TOTAL_FAMILIES × [HEXES_PER_FAMILY](../pages/HEXES-PER-FAMILY.md); Euler checks use this lattice size.

## Definition

- **Receives:** [TOTAL_FAMILIES](../pages/TOTAL-FAMILIES.md), [HEXES_PER_FAMILY](../pages/HEXES-PER-FAMILY.md)
- **Does:** TOTAL_HEXES = TOTAL_FAMILIES × [HEXES_PER_FAMILY](../pages/HEXES-PER-FAMILY.md); Euler's theorem requires 12 pentagon defects to close a hex sphere, which produces the 72,240 GCS variant.
- **Outputs:** `72,000 (72,240 GCS defect variant)` → [TOTAL_SIDES](../pages/TOTAL-SIDES.md)
- **Exists for:** hex substrate census

## Yields (formula)

TOTAL_HEXES = TOTAL_FAMILIES × [HEXES_PER_FAMILY](../pages/HEXES-PER-FAMILY.md); Euler's theorem requires 12 pentagon defects to close a hex sphere, which produces the 72,240 GCS variant.

## Produced from (inputs)

- [TOTAL_FAMILIES](../pages/TOTAL-FAMILIES.md)
- [HEXES_PER_FAMILY](../pages/HEXES-PER-FAMILY.md)

## Needed by (consumers)

- [TOTAL_SIDES](../pages/TOTAL-SIDES.md)

## See also

- [TOTAL_FAMILIES](../pages/TOTAL-FAMILIES.md)
- [HEXES_PER_FAMILY](../pages/HEXES-PER-FAMILY.md)
- [TOTAL_SIDES](../pages/TOTAL-SIDES.md)

## Origin

Java 20_GEOMETRY + Euler closed-sphere constraint (SCIENCE.md) — Theory Explainer: plain_lang: finest hex count under the ontology — TOTAL_FAMILIES × [HEXES_PER_FAMILY](../pages/HEXES-PER-FAMILY.md); Euler checks use this lattice size. author: Hesperia wiki (hex census tooling). extent: full. reasoning: hex substrate census. application: [TOTAL_FAMILIES](../pages/TOTAL-FAMILIES.md), [HEXES_PER_FAMILY](../pages/HEXES-PER-FAMILY.md).

## Notes

**HWIKI-PLAIN-C:** algebra plain_lang polished 2026-08-04. **HWIKI-PLAIN-B:** plain_lang backfilled from formula/notes 2026-08-04.

---
[← back to category](../categories/Geometry.md) · [wiki home](../index.md) · [Wire Map](Wiki-Wire-Map.md)
