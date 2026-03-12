<!--
HESPERIA — Reference Architecture Definition (RAD)
Copyright © 2026 igareosh.com — Platonov Igor (aka @igareosh). All rights reserved.
Restricted Research Disclosure License. Inspection and reference only.
No reproduction, redistribution, or use without explicit written permission.
See LEGAL_NOTICE.md for full terms.
-->

# Grace check: hesperia families table alignment with project

**Date**: 2026-02-16
**Purpose**: Confirm the Chroma families table (schema + CSV + script) fits the hesperia project and aligns with Python/Java semi-scripts and specs.

---

## 1. Does the table fit the hesperia project?

**Yes.** The table is built from the **main mandatory CSV** (`hex_sphere_areas_families_ideal_proportions.csv`) and 50_DATA for book_refs. It lives in Chroma as `layer=hesperia_families` for **Albina scopes** (cursor repo). Hesperia project scope (SCOPE-AND-SYNC) is currently documentation and scripting only; semantic layer is not in scope. The table is an Albina/cursor asset that uses hesperia **coordinates and names** from the same sources the project uses (13_SPEC, 15_SPEC, 31/CSV). When the hesperia semantic layer is in scope, this table can feed or align with it.

---

## 2. Python semi-scripts

| Script | Use | Fit |
|--------|-----|-----|
| **CLIENTS/hesperia/statements/classify_statements.py** | Loads families by area from a TSV (number, area, family). Uses **area** and list of **family** names for classification. | **Fits.** Same shape as our CSV. Table has area_name, family_name per row; grouping by area_name yields the same list. Script can be fed from CSV path or from Chroma (query layer=hesperia_families where area_name=X). |

---

## 3. Java / spec semi-scripts (coordinate system)

| Spec | Coordinate system | Table alignment |
|------|-------------------|-----------------|
| **13_SPEC__Indexing_and_Coordinates_v1_0.txt** | area [0..11], familyLocal [0..23], **familyGlobal** = area×24+familyLocal [0..287]. | **area_id** = spec `area`. **global_id** = CSV number (1..288) → spec **familyGlobal = global_id − 1**. familyLocal = (global_id−1) % 24. |
| **15_SPEC__Data_and_Schema_v0_1.txt** | Tables: area(id 0..11, name), family(id 0..287, area_id, local_index, name). | area_name = area.name, family_name = family.name, area_id = area.id, global_id = family.id+1 (CSV 1-based). |
| **10_MASTER_SPEC**, **21_MATH**, **20_GEOMETRY**, **23_PROTOTYPE** | Same constants (12 areas, 288 families, familyGlobal 0..287). | Coordinates in our schema match; conversion 1-based (CSV) ↔ 0-based (spec) is documented in HESPERIA-FAMILIES-CHROMA-SCHEMA.md §4. |

---

## 4. Conclusion

- **Table fits** the hesperia project: same sources (CSV, 50), same coordinate semantics (area_id, global_id/familyGlobal).
- **Python**: classify_statements.py aligns; can use CSV or Chroma.
- **Java/specs**: 13_SPEC, 15_SPEC coordinate system aligned; global_id (1-based) ↔ familyGlobal (0-based) documented.
- **Schema** (HESPERIA-FAMILIES-CHROMA-SCHEMA.md) updated with §4 alignment; no change to ingest script required.

**SIGNED: Product/Triage (Grace) | hesperia table alignment check | 2026-02-16 | governance**
