<!--
HESPERIA — Reference Architecture Definition (RAD)
Copyright © 2026 igareosh.com — Platonov Igor (aka @igareosh). All rights reserved.
Restricted Research Disclosure License. Inspection and reference only.
No reproduction, redistribution, or use without explicit written permission.
See LEGAL_NOTICE.md for full terms.
-->

# Hesperia — agents-oriented path: assessment, opinion, and further path (Ethan)

**Purpose**: Address Gena's developments, consolidate opinion, and propose a realistic deployable agents-oriented path for Hesperia per project foundations. **Owner**: Ethan. **Task**: [TASK-ETHAN-HESPERIA-AGENTS-PATH.md](TASK-ETHAN-HESPERIA-AGENTS-PATH.md). **Added**: 2026-02-17.

**Refs**: [projects/hesperia/PROJECT-CHARTER.md](../projects/hesperia/PROJECT-CHARTER.md), [CONTEXT-PACKET.md](../projects/hesperia/CONTEXT-PACKET.md), [SCOPE-AND-SYNC.md](../projects/hesperia/SCOPE-AND-SYNC.md), [ARCH-DECISION.md](../projects/hesperia/ARCH-DECISION.md); [HESPERIA-FAMILIES-CHROMA-SCHEMA.md](HESPERIA-FAMILIES-CHROMA-SCHEMA.md), [BOOKS-LAYER-AND-MATRIX-COMPRESSED-WORLD-VIEW.md](BOOKS-LAYER-AND-MATRIX-COMPRESSED-WORLD-VIEW.md); [CLIENTS/hesperia/DOC_INDEX.md](../CLIENTS/hesperia/DOC_INDEX.md).

---

## 1. Assessment of Gena's developments

**Delivered:**

| Deliverable | Location | Role |
|-------------|----------|------|
| Families schema + coordinates | HESPERIA-FAMILIES-CHROMA-SCHEMA.md | Layer hesperia_families; CSV canonical; area_id, global_id, area_name, family_name; alignment with 13_SPEC, 15_SPEC, 20_GEOMETRY. |
| §6 Calculable units and traversal | Same doc §6 | Hex unit, truth unit, borders, paths, traversal length, loops, loopability (formula ref), output road traversal in coordinates (road_coordinates, border_passings). All tied to 20_GEOMETRY, 40_POLICY, 13_SPEC. |
| Compressed world view | BOOKS-LAYER-AND-MATRIX-COMPRESSED-WORLD-VIEW.md | Single description: 12 areas, families preset, chunk→statements, hexagons, sphere, loopability/traversal and variables (Gena); matrix + books layer wiring. |
| Ingest script | cluster/chroma-server/ingest_hesperia_families.py | CSV → Chroma layer=hesperia_families; Abelard runs. |
| Matrix run (agents context) | cluster/chroma-server/matrix_run.py | CSV (and optional Chroma); returns JSON: geometry, hex_unit, truth_unit, borders, road_coordinates, border_passings, traversal_length, is_loop, loopability ref. Callable by agents. |

**Fit with current Hesperia scope:** SCOPE-AND-SYNC and CONTEXT-PACKET say "semantic layer not in scope yet" and "No semantic layer (RAG, semantic engine, indexing, families ingestion, Chroma for hesperia content)". The schema doc explicitly states: the Chroma families table is for **Albina scopes in the cursor repo**, not the Hesperia **product** semantic engine. So:

- **Product (Hesperia)** = specs and code in CLIENTS/hesperia and workspace; semantic layer (full RAG, sphere engine) = not in scope for the product phase.
- **Cursor repo / agents** = use of Hesperia **data and geometry** (CSV, schema, formulas from specs) to serve **agents**: families table in Chroma for Albina and Cursor, matrix_run for calculable results, compressed world view for context. This is **agents-oriented tooling** that consumes Hesperia documentation and canonical data; it does not implement the full Hesperia semantic engine in this repo.

**Conclusion:** Gena's work is **consistent** with project foundations when read as **cursor-repo agents capability** grounded in Hesperia docs. It does not expand the **product** semantic layer; it adds a well-bounded agents-facing layer (matrix, schema, run) that can later feed or align with the product when semantic layer is in scope (schema §4 scope note).

---

## 2. Consolidated opinion

**In place:** (a) Single canonical matrix (CSV) and schema (area_id, global_id, names); (b) calculable semantics (§6) aligned with Hesperia specs; (c) one script to run on matrix and return structured results (matrix_run); (d) ingest path for Chroma (Abelard); (e) compressed world-view description and wiring (FPF + books + matrix) in rules. Ownership is clear: Gena = matrix/main dev; Abelard = ingest; Grace = triage.

**Risks / clarifications:** (1) **Scope wording**: SCOPE-AND-SYNC says "families ingestion" and "Chroma for hesperia content" are not in scope — that refers to the **product** semantic layer. The cursor-repo use (Chroma layer hesperia_families for Albina/agents) should be explicitly **out of scope of the product phase** but **in scope of cursor-repo agents development**. Recommend Grace add one sentence to SCOPE-AND-SYNC or CONTEXT-PACKET §2.1: "Agents use of matrix in cursor repo (Chroma layer hesperia_families, matrix_run, schema) is cursor-repo scope, not Hesperia product semantic layer; product semantic layer remains not in scope." (2) **Loopability value**: L_full / L_weighted require activation data (TAU_FAMILY, per-family activation); matrix_run correctly returns formula ref and requires_activation_data. No change needed; future step if activation pipeline exists. (3) **Books–matrix wiring**: PAUSED; when un-paused, bounding(concept, source, family, area) becomes retrievable; path already defined in TASK-ABELARD-WIRE-FAMILIES-TO-BOOKS-LAYER.

**Alignment:** Schema and §6 cite 13_SPEC, 20_GEOMETRY, 40_POLICY; matrix_run uses same constants and ring logic. Compressed world view and DOC_INDEX/specs are aligned. No conflict with ARCH-DECISION (no new service boundary; scripts and Chroma layer are cursor-repo assets).

---

## 3. Further path — agents-oriented development (realistic, deployable, addressable)

**Principle:** Develop Hesperia **for agents** in the cursor repo in phases that stay **grounded in Hesperia documentation** and **project foundations**, without committing the **product** to semantic-layer scope until a later decision.

**Phase A (current — done or in hand)**
- Matrix and schema (Gena); §6 calculable units; compressed world view; matrix_run; ingest script.
- **Deployable:** Abelard runs ingest when Chroma is up; agents call matrix_run (CSV fallback).
- **Addressable:** active.md rows; TASK-TEAM-MATRIX-RUN-AGENTS-CONTEXT, TASK-GENA-*, HESPERIA-FAMILIES-CHROMA-SCHEMA, CHROMA-BOOKS-LIST-AND-WIRING.

**Phase B (next — realistic)**
1. **Scope clarification:** Grace updates SCOPE-AND-SYNC or CONTEXT-PACKET §2.1 to state explicitly that agents use of matrix (Chroma layer hesperia_families, matrix_run, schema) is cursor-repo scope, not Hesperia product semantic layer.
2. **Ingest:** Abelard completes hesperia families ingest (existing OPEN row).
3. **Wiring:** Wire hesperia families table to FPF as pylon in Albina construction (existing TBD row) when Abelard DONE.
4. **Optional:** Cursor or Gena add a single sentence in agent rules or README: "When matrix-derived context is needed, run cluster/chroma-server/matrix_run.py or query Chroma layer=hesperia_families."

**Phase C (later — when un-paused)**
5. **Books–matrix wiring:** Un-pause TASK-ABELARD-WIRE-FAMILIES-TO-BOOKS-LAYER; bounding(concept, source, family, area) on books chunks; agents can resolve family/area → books and books → (family, area, concept).
6. **Loopability/traversal preset:** If activation/novelty pipeline is introduced, Gena implements preset per 40_POLICY; matrix_run or a sibling script can then return L_full when data available.

**Phase D (product — out of current agents path)**
7. **Hesperia product semantic layer:** When project decides to put "semantic layer" in scope (RAG, sphere engine, indexing in workspace/product), SCOPE-AND-SYNC and CONTEXT-PACKET are updated by Grace; schema and coordinates in cursor repo remain the **reference** for alignment (same area_id, global_id, 13_SPEC, 20_GEOMETRY). No new cursor-repo commitment in this report for Phase D.

**Ownership and refs:**
- Grace: scope wording, triage, follow-on tasks.
- Gena: matrix/main dev, loopability preset when applicable.
- Abelard: ingest, Chroma, books-layer wiring when un-paused.
- Cursor: optional wiring of matrix_run or Chroma query into agent context.
- Foundations: PROJECT-CHARTER, CONTEXT-PACKET, SCOPE-AND-SYNC, ARCH-DECISION; CLIENTS/hesperia DOC_INDEX and numbered specs (10_MASTER_SPEC, 11_BLUEPRINT, 20_GEOMETRY, 40_POLICY, etc.).

---

## 4. Summary

- **Assessment:** Gena's developments (schema, §6, compressed world view, ingest, matrix_run) form a coherent **agents-oriented** layer in the cursor repo, grounded in Hesperia docs; they do not expand the Hesperia **product** semantic layer.
- **Opinion:** Clarify scope (agents use of matrix = cursor-repo; product semantic layer = still not in scope); otherwise current design is consistent and addressable.
- **Path:** Phase A done/in hand; Phase B = scope sentence + ingest + FPF/Albina wire + optional agent doc; Phase C = books–matrix wiring and (if data exists) loopability preset; Phase D = product semantic layer only when project scope changes.

---

**SIGNED: Architecture (Ethan) | hesperia agents path report | 2026-02-17 | governance**
