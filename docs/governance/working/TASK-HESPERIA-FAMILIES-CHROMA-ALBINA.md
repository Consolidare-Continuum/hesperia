<!--
HESPERIA — Reference Architecture Definition (RAD)
Copyright © 2026 igareosh.com — Platonov Igor (aka @igareosh). All rights reserved.
Restricted Research Disclosure License. Inspection and reference only.
No reproduction, redistribution, or use without explicit written permission.
See LEGAL_NOTICE.md for full terms.
-->

# Task: Hesperia families → Chroma operational table for Albina

**Purpose**: Make sense of Hesperia family/area sources; produce an operational Chroma table (scriptable, fast access) mapping family names → concept and books; for Albina AI agent scopes enhancement. **Owner (triage)**: Grace. **Next step**: Wire table to FPF as additional pylon in Albina construction (separate task).

**Source**: Boss request (Grace triage). **Added**: 2026-02-16.

---

## 1. Scope

### 1.1 Source files and latest-dated discovery

**Family versions vary.** Gena (or implementer) must **discover the latest-dated** families source(s) in repo and workspace before consolidating. Candidates:

| Location | File(s) | Note |
|----------|---------|------|
| **Workspace** (prichindel) | `HESPERIA_FAMILIES_BASE_links_v0_1.csv`, `HESPERIA_FAMILIES_FULL_matrix_v0_1.csv` (Nov 27) | Matrix coordinates: from_global_id, from_area_id, to_global_id, to_area_id |
| **Workspace** | `33_FAMILIES__Passes_and_Stops_description_v0_1.txt`, `HESPERIA_FAMILIES_PASSES_*.csv` (Nov 27) | Passes, stops |
| **Repo** | `31_FAMILIES__area_family_table_full.txt` | number, **area**, **family** (canonical names) |
| **Repo** | `v0.1/hex_sphere_areas_families_ideal_proportions.csv`, `v0.1/HESPERIA_families_concise_v2.txt` | area, family, proportions; ring order |
| **Repo** | `30_FAMILIES__HESPERIA_hex_canonical_v1_0.txt`, `32_FAMILIES__concise_spec_v2_1.txt` | Canonical hex, concise spec |
| **Repo** | `50_DATA__120_books_authors_raw.txt` | Area, Author, Title, Notes — books per area |

**Canonical names**: **AreaName** and **FamilyName** must be **first-class variables** in the schema (not only coordinates). Use **latest-dated** families file(s) for the authoritative list; reconcile with 31/32/30 and workspace matrix CSVs as needed.

**World-view matrix**: Families (AreaName + FamilyName) represent **contexts**; books best fit for **term/concept explanation** (conceptual). Goal: one coherent mapping **family (area, name) → concept → books**, with **matrix coordinates** for encoding and retrieval.

### 1.2 Deliverable: Chroma operational table

- **Table** in Chroma: scriptable, fast access from **terms/family names** → **concept** and **books** they represent.
- **Books** will be (or are) in Chroma **books** layer; this table links families to book identifiers/titles so Albina (and FPF later) can resolve family → concept → books.
- **Schema (mandatory)**:
  - **AreaName** (string) and **FamilyName** (string) as **first-class variables** — present in every record; interpretable when finding; used for lookup and display.
  - **Matrix coordinates**: encodable and retrievable (e.g. `area_id`, `global_id`, or row index from the authoritative matrix). Coordinates must be **interpretable** (human or script can resolve coordinate → AreaName/FamilyName) and **encodable** (script can encode family/area → coordinates and back).
  - concept/summary text; book refs (ids or titles; link to books layer when available).
- **Layer**: New layer or dedicated collection (e.g. `layer=hesperia_families` or `families`) with the above metadata.
- **Scripting**: Encode for **fast access** by **AreaName**, **FamilyName**, and by **matrix coordinates**; scripts can query Chroma for Albina (by name or by coordinates).

### 1.3 Purpose

- **Albina AI agent scopes enhancement**: Albina can use this table to scope context (family → concept, books) for reasoning and retrieval.
- **Follow-up task (next)**: Wire this table/collection to **FPF** as an **additional pylon** in Albina construction.

---

## 2. Roles and refs

| Step | Owner | Action |
|------|--------|--------|
| Discover latest | Gena | Find latest-dated families file(s) in repo and workspace; versions vary — use as authoritative source for names and coordinates. |
| Design / spec | Ethan or Gena | Consolidate sources → single world-view matrix (family→concept→books); define Chroma schema with **AreaName**, **FamilyName**, **matrix coordinates** (interpretable, encodable, retrievable). |
| Script + schema | Gena | Script(s) to build the table (from latest sources + CSV/txt), encode for Chroma; query API for fast access by **AreaName**, **FamilyName**, and by **matrix coordinates**. |
| Ingest to Chroma | Abelard | Run ingest (mass ingest = Abelard per CHROMA-USAGE-POLICY). Use schema and script produced by Gena. |
| Wire to FPF (next) | (TBD) | Separate task: add this table as pylon in Albina construction (FPF integration). |

Refs: [CHROMA-USAGE-POLICY.md](CHROMA-USAGE-POLICY.md), [CHROMA-BOOKS-LIST-AND-WIRING.md](CHROMA-BOOKS-LIST-AND-WIRING.md), [projects/hesperia/SCOPE-AND-SYNC.md](projects/hesperia/SCOPE-AND-SYNC.md).

---

## 3. Acceptance

- **Latest-dated** families source(s) identified and used for the authoritative list.
- **AreaName** and **FamilyName** present as variables in every record; interpretable on find.
- **Matrix coordinates** (e.g. area_id, global_id) encodable and retrievable; scripts can resolve coordinate ↔ AreaName/FamilyName.
- One consolidated mapping (or spec) family (area, name) → concept, books.
- Chroma collection/layer with scriptable ingest and fast lookup by **name** and by **coordinates**.
- Documented schema and script location in repo.
- Albina can use the table for scopes enhancement (query path documented).
- Follow-up task recorded: wire table to FPF as pylon for Albina.

---

## 4. Next tasks (after table is in Chroma)

- **Wire families mapping to books layer** (Abelard): The **coordinate** is the **bounding** between **concept**, **source**, **family**, and **area**. Task: [TASK-ABELARD-WIRE-FAMILIES-TO-BOOKS-LAYER.md](TASK-ABELARD-WIRE-FAMILIES-TO-BOOKS-LAYER.md). **DONE 2026-02-17** (un-paused); bounding in [CHROMA-BOOKS-LIST-AND-WIRING.md](CHROMA-BOOKS-LIST-AND-WIRING.md) §Coordinate = bounding.
- **Wire hesperia families table to FPF** as an **additional pylon** in Albina construction. **DONE 2026-02-17**: Cursor wired layer=hesperia_families in CHROMA-USAGE-POLICY (§2.1–2.2), CHROMA-BOOKS-LIST-AND-WIRING (Albina = fpf + books + hesperia_families), and cluster/ALBINA.md (FPF mode exception includes hesperia_families). Albina can now query Chroma including hesperia_families to combine family→concept→books with FPF.

---

**SIGNED: Product/Triage (Grace) | hesperia families Chroma Albina | 2026-02-16 | governance**
