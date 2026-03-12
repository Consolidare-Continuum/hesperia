<!--
HESPERIA — Reference Architecture Definition (RAD)
Copyright © 2026 igareosh.com — Platonov Igor (aka @igareosh). All rights reserved.
Restricted Research Disclosure License. Inspection and reference only.
No reproduction, redistribution, or use without explicit written permission.
See LEGAL_NOTICE.md for full terms.
-->

# Hesperia context RAG daemon — MVP proposal (Ethan)

**Purpose**: Structured proposal for turning the current Hesperia agents-oriented layer into a **RAG deployment daemon** that provides Cursor with **context calculation** (math- and program-based; sources and statements → values for AI coherence and context correction). **Owner**: Ethan. **Task**: [TASK-ETHAN-HESPERIA-RAG-DAEMON-MVP.md](TASK-ETHAN-HESPERIA-RAG-DAEMON-MVP.md). **Added**: 2026-02-17.

**Refs**: [HESPERIA-AGENTS-PATH-ETHAN-REPORT.md](HESPERIA-AGENTS-PATH-ETHAN-REPORT.md), [HESPERIA-FAMILIES-CHROMA-SCHEMA.md](HESPERIA-FAMILIES-CHROMA-SCHEMA.md), [BOOKS-LAYER-AND-MATRIX-COMPRESSED-WORLD-VIEW.md](BOOKS-LAYER-AND-MATRIX-COMPRESSED-WORLD-VIEW.md); cluster/chroma-server/matrix_run.py, ingest_hesperia_families.py; [projects/hesperia/CONTEXT-PACKET.md](../projects/hesperia/CONTEXT-PACKET.md).

---

## 1. Current-state summary

| Component | Location | Role |
|-----------|----------|------|
| **Canonical matrix (CSV)** | CLIENTS/hesperia/v0.1/hex_sphere_areas_families_ideal_proportions.csv | 288 families; columns number, area, family; defines global_id, area_id, area_name, family_name. |
| **Chroma layer** | layer=hesperia_families | Ingest from CSV; 288 rows; query by area_name, family_name, global_id, area_id. |
| **Schema §6 (calculable units)** | HESPERIA-FAMILIES-CHROMA-SCHEMA.md §6 | Hex unit, truth unit, borders, paths, traversal length, loops, loopability (formula ref), road_coordinates, border_passings. All derivable from coordinates + constants (20_GEOMETRY, 40_POLICY, 13_SPEC). |
| **matrix_run.py** | cluster/chroma-server/matrix_run.py | CLI: --start, --direction, --steps, [--chroma]. Returns JSON: matrix_source, geometry, hex_unit, truth_unit, borders, path_params, road_coordinates, border_passings (area + family), traversal_length, is_loop, loopability (formula_ref + requires_activation_data). CSV fallback when Chroma down. |
| **Compressed world view** | BOOKS-LAYER-AND-MATRIX-COMPRESSED-WORLD-VIEW.md | 12 areas, families preset, chunk→statements, hexagons, sphere, loopability/traversal; matrix + books layer wiring. |
| **Books layer** | Chroma layer=books (and books_general) | Chunks with metadata; bounding(concept, source, family, area) when families–books wiring active (TASK-ABELARD-WIRE-FAMILIES-TO-BOOKS-LAYER). |
| **Agent usage** | cursor-main-awareness.mdc, CHROMA-BOOKS-LIST-AND-WIRING | When matrix-derived context needed: run matrix_run.py or query Chroma layer=hesperia_families. FPF + books + matrix as option when fpf_mode=1. |

**Gap today**: Cursor (and automation) get context by (1) calling matrix_run.py ad hoc or (2) querying Chroma. There is no **single entry point** that returns a **context packet** combining: (a) calculable geometry and traversal values, (b) optional retrieval (families, and when wired books/statements), (c) a stable contract so the AI can **use values to adjust coherence** (e.g. “this answer is in area X; traversal says next area is Y; border_passings say we crossed Z”). So the **model** (what we have) is not yet structured as a **daemon** that **computes and serves context** in one call.

---

## 2. Model adjustment — structure as a daemon

**Idea**: Treat the existing pieces as **backends** of a **context-calculation service** (daemon) that:

1. **Accepts** a small request (e.g. “context for this query” or “context packet for area_id X / path params Y”).
2. **Computes** deterministic values (geometry, path, road_coordinates, border_passings, traversal_length, is_loop) from matrix_run logic and schema §6.
3. **Optionally retrieves** from Chroma: families (layer=hesperia_families), and when wired books (layer=books) with bounding(concept, source, family, area).
4. **Returns** a **context packet** (JSON or equivalent): calculable block + optional retrieval block + **statements/sources** when available, so Cursor can inject “values” (coordinates, borders, traversal, sourced statements) into the prompt or use them to correct drift.

**No new semantics**: Reuse matrix_run, schema §6, Chroma queries. The daemon is a **thin orchestration layer**: one process or script that (a) runs matrix_run (or inlines its logic), (b) calls Chroma for families (and books if wired), (c) assembles one response. Deploy as: **HTTP service** (e.g. Flask/FastAPI on prichindel) or **CLI + wrapper** that Cursor/automation invokes (e.g. `context_rag --query "..."` or `context_rag --path --start 0 --steps 12`). MVP prefers **CLI-first**: one command returns the context packet; later add HTTP if needed.

**Ownership**: Gena = daemon code and matrix/Chroma orchestration; Abelard = deploy (run on prichindel, same host as Chroma), ingest and Chroma unchanged.

---

## 3. MVP definition

### 3.1 Scope (in)

- **Single entry point**: One command (e.g. `python cluster/chroma-server/context_rag.py [options]`) that returns a **context packet**.
- **Packet contents**:
  - **calculable**: Same as matrix_run today (geometry, hex_unit, truth_unit, borders, path_params, road_coordinates, border_passings, traversal_length, is_loop, loopability ref). All from schema §6 and existing matrix_run logic; no new math.
  - **retrieval** (optional): If `--query "..."` or `--area_id N` / `--family_name X`: up to K families from Chroma (layer=hesperia_families); when books–families wiring is on, up to M chunks from layer=books (or books_general) with bounding(concept, source, family, area). So the packet can include **sources and statements** (chunk text + metadata) for the AI to use.
  - **coherence hints** (optional): Short structured block that an agent can use to “adjust context”: e.g. `current_area_id`, `suggested_adjacent_areas` (from borders), `traversal_summary` (e.g. “one full ring CW”), `border_passings_count`. These are **values** derived from the calculable block, not free text.
- **Contract**: JSON stdout or HTTP JSON. Schema of the packet is documented (e.g. in this repo) so Cursor and automation can rely on it.
- **Fallback**: If Chroma is down: packet still returns calculable block from CSV (same as matrix_run); retrieval block empty or minimal.

### 3.2 Scope (out of MVP)

- Loopability **value** L_full (requires activation data); MVP keeps formula_ref + requires_activation_data.
- Full Hesperia **product** semantic layer (RAG sphere engine in workspace); cursor-repo only.
- Changing SCOPE-AND-SYNC for the product.

### 3.3 Interfaces (MVP)

| Interface | Description |
|-----------|-------------|
| **CLI** | `context_rag.py [--path] [--start N] [--direction 1\|-1] [--steps N] [--query "..." ] [--chroma] [--data-dir PATH]`. If --path: same as matrix_run (path + calculable). If --query: add retrieval block (Chroma families + optional books). Default: path with 12 steps from 0. |
| **Output** | JSON: `matrix_source`, `calculable` (geometry, hex_unit, truth_unit, borders, path_params, road_coordinates, border_passings, traversal_length, is_loop, loopability), optional `retrieval` (families[], chunks[] with source/family/area), optional `coherence_hints` (current_area_id, suggested_adjacent_areas, traversal_summary, border_passings_count). |
| **Cursor usage** | Cursor (or workflow) runs `context_rag.py` when it needs context; parses JSON and injects calculable + coherence_hints + (if present) retrieval into context. Values (coordinates, borders, traversal) used to adjust coherence or ground answers. |

### 3.4 How sources and statements feed values for coherence

- **Calculable values**: area_id, road_coordinates, border_passings, traversal_length, is_loop. The AI can use these to stay “on path” (e.g. “we are in area 3; next areas on the ring are 2 and 4”) or to report “we crossed N area borders.”
- **Retrieval (sources/statements)**: When --query or area/family filter is used, the packet includes chunks (and metadata: source, family, area). Those are **authoritative statements** (per compressed world view: “statement = as true when author wording”). The AI can cite source and family/area and use them to **correct** or **ground** an answer when values go off (e.g. contradicting a sourced statement).
- **Coherence hints**: Explicit short fields (suggested_adjacent_areas, traversal_summary) give the model **numerical/structural anchors** without requiring it to re-derive from geometry. So “context calculation” = calculable block + optional retrieval + coherence_hints; the AI gets **values** to adjust coherence and contexts.

---

## 4. Phased steps (realistic, deployable, addressable)

| Phase | Step | Owner | Description |
|-------|------|--------|-------------|
| **MVP build** | 4.1 | Gena | Add `context_rag.py` (or equivalent name) in cluster/chroma-server/: (1) reuse matrix_run logic (or call matrix_run in-process) for calculable block; (2) optional Chroma query (layer=hesperia_families, and layer=books when wiring present) for retrieval; (3) build coherence_hints from calculable; (4) output single JSON. CLI args as in §3.3. Doc: short README or § in cluster/chroma-server/README.md. |
| **MVP build** | 4.2 | Gena | Define and document the **context packet JSON schema** (calculable, retrieval, coherence_hints) in governance/ or cluster/chroma-server/ (e.g. CONTEXT-RAG-PACKET-SCHEMA.md). |
| **MVP deploy** | 4.3 | Abelard | Run context_rag.py on prichindel (cron or on-demand; same env as matrix_run and Chroma). No new service boundary; script invocable from Cursor/automation. If later HTTP is needed, add in a follow-on task. |
| **Cursor wiring** | 4.4 | Cursor | When matrix-derived or context-RAG context is needed, invoke context_rag.py (or document in rules/README: “run context_rag.py for full context packet”). Optional: MCP or workflow step that calls context_rag and passes packet into context. |
| **Later** | 4.5 | Gena / Abelard | If books–families wiring is un-paused: ensure context_rag retrieval block can include books chunks with bounding(concept, source, family, area). |
| **Later** | 4.6 | Gena | When activation data exists: add loopability value L_full to calculable block per 40_POLICY. |

Handoffs: Grace triages and keeps active.md rows (Gena 4.1–4.2, Abelard 4.3, Cursor 4.4). Ethan signs off this proposal; no implementation in this task.

---

## 5. Summary

- **Current state**: Matrix, schema §6, matrix_run, Chroma hesperia_families, compressed world view, and FPF/books wiring exist; no single context-calculation entry point.
- **Model adjustment**: Structure them as backends of a **context RAG daemon** (CLI-first): one command returns a **context packet** = calculable + optional retrieval + coherence_hints.
- **MVP**: context_rag.py (or same) in cluster/chroma-server; JSON packet with calculable, retrieval, coherence_hints; Cursor invokes it for values to adjust coherence and contexts; deploy on prichindel.
- **Phased steps**: Gena (script + schema doc), Abelard (deploy/run), Cursor (wiring); later books retrieval and loopability value.

---

**SIGNED: Architecture (Ethan) | hesperia RAG daemon MVP proposal | 2026-02-17 | governance**
