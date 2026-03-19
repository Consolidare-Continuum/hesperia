<!--
HESPERIA — Reference Architecture Definition (RAD)
Copyright © 2026 igareosh.com — Platonov Igor (aka @igareosh). All rights reserved.
Restricted Research Disclosure License. Inspection and reference only.
No reproduction, redistribution, or use without explicit written permission.
See LEGAL_NOTICE.md for full terms.
-->

# Hesperia families — Chroma schema (Gena)

**Purpose**: Schema and discovery for the hesperia families table in Chroma. **Layer**: `hesperia_families`. **Main dev**: Gena (books layer + matrix + compressed world view, loopability/traversal preset, variables). **Ref**: [TASK-HESPERIA-FAMILIES-CHROMA-ALBINA.md](TASK-HESPERIA-FAMILIES-CHROMA-ALBINA.md). **Compressed world view**: [BOOKS-LAYER-AND-MATRIX-COMPRESSED-WORLD-VIEW.md](BOOKS-LAYER-AND-MATRIX-COMPRESSED-WORLD-VIEW.md) — general description of books layer and matrix (12 areas, families preset, hexagons, loopability/traversal, variables; loopability/traversal preset and variables to be programmed by Gena; refs Hesperia docs). **Schema extension §6**: Hex unit, truth unit, traversal length, paths, borders, loops, loopability, output road traversal in coordinates (families, border passings) — defined and calculable per §6; task [TASK-GENA-SCHEMA-HEX-TRAVERSAL-UNITS.md](TASK-GENA-SCHEMA-HEX-TRAVERSAL-UNITS.md). **Code run (agents context)**: [TASK-TEAM-MATRIX-RUN-AGENTS-CONTEXT.md](TASK-TEAM-MATRIX-RUN-AGENTS-CONTEXT.md) — implement run on matrix returning calculable-for-model results; Gena lead.

**Updated**: 2026-02-16

---

## 1. Main mandatory source: CSV

**The CSV is the main mandatory source.** All coordinates and names are defined from it.

| Source | Location | Role |
|--------|----------|------|
| **CSV (main, mandatory)** | `CLIENTS/hesperia/v0.1/hex_sphere_areas_families_ideal_proportions.csv` | **Canonical**: columns `number`, `area`, `family` (+ target_*, words_*). Defines **coordinates** and **AreaName**, **FamilyName**. One row per family; row order = coordinate space. |
| **Books per area** | `CLIENTS/hesperia/50_DATA__120_books_authors_raw.txt` | Area → book_refs (Author — Title); joined by area name. |

**CSV columns (relevant)**: `number`, `area`, `family`, `target_units_total`, `target_statements`, `target_descriptions`, `target_peacemakers`, `words_statements`, `words_descriptions`, `words_peacemakers`, `words_total`. Coordinates are **number** (global_id) and **area** (area_name; area_id = index of unique area in CSV order or fixed 0..11 map).

---

## 2. Chroma metadata (mandatory) — from CSV coordinates

| Field | Type | Source (CSV) | Purpose |
|-------|------|--------------|---------|
| **source** | string | — | `hex_sphere_areas_families_ideal_proportions.csv` (main mandatory ref) |
| **layer** | string | — | `hesperia_families` |
| **area_name** | string | CSV `area` | AreaName — first-class variable |
| **family_name** | string | CSV `family` | FamilyName — first-class variable |
| **global_id** | int | CSV `number` | Row coordinate from CSV; encodable, retrievable |
| **area_id** | int | Derived from CSV `area` | Area index 0..11 (canonical area order) for matrix coordinates |
| **concept** | string | — | Short concept/summary (or placeholder) |
| **book_refs** | string | 50_DATA joined by area_name | JSON array of "Author — Title" |

Optional (from CSV): `target_units_total`, `target_statements`, `words_total` etc. may be stored as metadata if needed for retrieval.

**Document text** (for embedding): `{area_name} {family_name}: {concept}`.

---

## 3. Coordinates (from CSV)

- **global_id** = CSV column `number` (1..N). Unique row coordinate; interpretable.
- **area_id** = index of CSV `area` in canonical area order (0=GOOD, 1=HARM, 2=TRUTH, 3=DECEIT, 4=ORDER, 5=CHAOS, 6=FREEDOM, 7=CONTROL, 8=CARE, 9=INDIFFERENCE, 10=CREATION, 11=DESTRUCTION).
- **area_name** = CSV column `area`; **family_name** = CSV column `family`.
- Scripts encode/decode: coordinate (global_id, area_id) ↔ (area_name, family_name) using the CSV as authority.

---

## 4. Alignment with hesperia project (specs and scripts)

| Ref | Alignment |
|-----|-----------|
| **13_SPEC__Indexing_and_Coordinates_v1_0.txt** | Spec uses **area** ∈ [0..11], **familyGlobal** = area×24+familyLocal ∈ [0..287] (0-based). Our **area_id** = spec `area`. Our **global_id** = CSV `number` (1..288); **spec familyGlobal = global_id − 1**. So coordinates are interoperable: `familyLocal = (global_id - 1) % 24`. |
| **15_SPEC__Data_and_Schema_v0_1.txt** | Spec tables `area` (id 0..11, name), `family` (id 0..287, area_id, local_index 0..23, name). Our metadata: **area_name** = area.name, **family_name** = family.name, **global_id** = family.id+1 (CSV 1-based), **area_id** = area.id. Fit. |
| **Python: statements/classify_statements.py** | Loads families by area from a tab-separated file (number, area, family). Same shape as our CSV. Expects `area` + list of `family` names; our table has **area_name**, **family_name** per row — group by area_name to get the list. Script can be fed from CSV or from Chroma (query layer=hesperia_families where area_name=X). **Fits.** |
| **Java-style semi-scripts / specs** | 20_GEOMETRY, 21_MATH, 23_PROTOTYPE use area, familyGlobal, familyLocal. Our **area_id** and **global_id** (with global_id−1 = familyGlobal) match. No Java code in repo; schema aligns with spec coordinate system. |

**Scope note**: Current hesperia project phase = documentation and scripting only; semantic layer not in scope (SCOPE-AND-SYNC). The Chroma families table is for **Albina scopes** in the cursor repo, not the hesperia product semantic engine. When semantic layer is in scope, this table can feed or align with it via the same coordinates.

---

## 5. Script location

- **Ingest**: `cluster/chroma-server/ingest_hesperia_families.py` — reads **CSV first** (mandatory), then 50 for book_refs. Abelard runs (mass ingest = Abelard).
- **Query**: `layer=hesperia_families`; filter by `area_name`, `family_name`, `global_id`, `area_id`.

---

## 6. Calculable units and traversal (hex unit, truth unit, paths, borders, loops, loopability, output road traversal)

Definitions and formulas below are **calculable from schema coordinates and constants**; direct math from Hesperia docs: `CLIENTS/hesperia/20_GEOMETRY__formalized_structure_java.txt`, `40_POLICY__Loopability_and_traversal.txt`, `13_SPEC__Indexing_and_Coordinates_v1_0.txt`.

### 6.1 Geometry constants (from 20_GEOMETRY, 13_SPEC)

```
AREA_COUNT = 12
FAMILIES_PER_AREA = 24
HEXES_PER_FAMILY = 250
SIDES_PER_HEX = 6
TOTAL_FAMILIES = 288
TOTAL_HEXES = 72_000
TOTAL_SIDES = 432_000
```

Schema coordinates: **area_id** ∈ [0..11], **global_id** ∈ [1..288] (CSV); spec **familyGlobal** = global_id − 1; **familyLocal** = (global_id − 1) % 24.

### 6.2 Hex unit

- **Definition**: One hexagonal unit; 6 sides; one statement per side. Identified by (area_id, familyGlobal, hexIndex) with familyGlobal = global_id − 1, hexIndex ∈ [0..249].
- **Derivation**: From schema (area_id, global_id) plus hexIndex. Count per family = HEXES_PER_FAMILY; total hexes = TOTAL_HEXES.
- **Ref**: 20_GEOMETRY §2–3; 13_SPEC §2–3.

### 6.3 Truth unit

- **Definition**: Atomic truth slot = one **side** of a hex. One statement (3–5 sentences) per side; truth weight τ ∈ [0,1]. Identified by (area_id, familyLocal, hexIndex, sideIndex) or by linear **sideId** ∈ [0..431999] per 13_SPEC.
- **Derivation**: sideId = ((familyGlobal * HEXES_PER_FAMILY) + hexIndex) * SIDES_PER_HEX + sideIndex; familyGlobal = area_id * FAMILIES_PER_AREA + familyLocal; familyLocal = (global_id − 1) % 24.
- **Ref**: 20_GEOMETRY §4 (Truth Representation); 13_SPEC §3.

### 6.4 Borders

- **Definition**: Boundaries between **areas** (ring adjacency) or between **family regions** (change of family/area).
- **Area border**: Ring adjacency — left(area_id) = (area_id − 1 + 12) % 12, right(area_id) = (area_id + 1) % 12. Ref: 40_POLICY §2.1.
- **Family/area border passing**: A step (from_area_id, from_global_id) → (to_area_id, to_global_id) crosses an area border if from_area_id ≠ to_area_id; crosses a family border if from_global_id ≠ to_global_id.
- **Calculable**: From any two consecutive (area_id, global_id) in a path.

### 6.5 Paths

- **Definition**: Ordered sequence of steps along the ring or within the sphere. Each step = (area_id, global_id) or (area_id, familyLocal) at a given step index.
- **Encoding**: Path = list of (area_id, global_id) or (area_id, step_index). Ring traversal: area_at(step) = (start_area + direction * step + 12) % 12 per 40_POLICY §4.3; direction +1 = clockwise, −1 = counterclockwise.
- **Calculable**: From start_area_id, direction, and step count; family at each step from CSV/Chroma by area_id.

### 6.6 Traversal length

- **Definition**: Number of steps (hops) in a path. For one full ring: STEPS_PER_PASS = AREA_COUNT = 12 (40_POLICY §4.1).
- **Formula**: traversal_length = len(path) or step_count.
- **Calculable**: From path size or from (end_step − start_step).

### 6.7 Loops

- **Definition**: Closed traversal: path that returns to the starting area (e.g. one full ring). Full ring CW or CCW = one loop.
- **Derivation**: path is a loop iff path[0].area_id == path[-1].area_id and len(path) > 1 (or step_count % 12 == 0 for ring).
- **Ref**: 40_POLICY §4 (Ring Traversal), §10 (Loopability).

### 6.8 Loopability

- **Definition**: Metric = how much **new semantic territory** per hop; novelty-driven (families + statements crossing threshold). Ref: 40_POLICY §10–11.
- **Formula (full pass)**: L_full = G_F[p] / STEPS_PER_PASS, where G_F[p] = count of family novelty events in pass p. Optionally L_weighted = (G_F[p] + λ * G_S[p]) / STEPS_PER_PASS (λ balances family vs statement novelty).
- **Calculable**: From cumulative activation per family and threshold TAU_FAMILY; count steps where a family first crosses threshold; divide by STEPS_PER_PASS.

### 6.9 Output road traversal in coordinates (families, border passings)

- **Definition**: Result of a traversal expressed as **coordinates** and **border passings** so that scripts can compute and emit the road.
- **Output format**:
  - **road_coordinates**: list of (area_id, global_id) or (area_name, family_name) in visit order — i.e. the sequence of (family, area) positions along the path.
  - **border_passings**: list of border-crossing events:
    - **Area border passing**: (from_area_id, to_area_id) or (from_area_name, to_area_name) when the path moves from one area to a neighbour on the ring.
    - **Family border passing**: (from_global_id, to_global_id) or (from_family_name, to_family_name) when the path moves to a different family (and optionally from_area_id, to_area_id for family areas).
- **Calculable**: From path (ordered list of (area_id, global_id)); iterate and emit each (area_id, global_id); detect border_passings when area_id or global_id changes between consecutive steps.
- **Ref**: 40_POLICY (traversal order, steps); schema coordinates §3 above.
