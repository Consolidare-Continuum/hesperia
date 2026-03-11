# Hesperia — mid-stage product report (internal and external)

**Purpose**: Consolidation of what is done, what we need, and where we go. Usable as internal status and as external-facing product report. **Owner**: Grace. **Date**: 2026-02-18.

---

## Executive summary

Hesperia is the prichindel.com semantic-substrate product (specs, sphere, matrix, RAG, families). We are at **mid-stage**: the **agents-oriented layer** is live — matrix in Chroma, context RAG daemon deployed, books–families retrieval and loopability value (L_full) when activation data is provided. The **product semantic layer** (full RAG engine in product workspace) remains out of scope until Phase D. This report consolidates done items, gaps, and direction for both internal and external use.

---

## What Hesperia is now (state — already)

**Single source**: [governance/ETHAN-HESPERIA-STATE-NOW-ASSESSMENT.md](../../governance/ETHAN-HESPERIA-STATE-NOW-ASSESSMENT.md).

- **What it is**: A **geometry-safe semantic traversal kernel** — in product terms, a **deterministic semantic traversal and validation core**. Clean structural baseline: fixed geometry (12×24×250), deterministic ring traversal, border tracking, context packet with adjacency hints, logic layer + safeguard, apple coverage. No noise, no retrieval in core calibration, no drift.
- **What it does**: Provides deterministic context framing for agents (context governor), structural path validation, coverage verification (apple), path comparison framework, and a logic-layer baseline. It does **not** yet do semantic reasoning, value-evaluating, or content-level conflict detection; it is structure-only traversal. Do not touch ring order, adjacency, family counts, hex geometry, or safeguard threshold until Phase D is defined. Next step: choose direction (harden structure / inject semantic weight / controlled retrieval / Phase D) and lock one formal spec.

---

# Part A — Internal report

## 1. What is done

| Area | Deliverable | Owner | Ref |
|------|-------------|--------|-----|
| **Project bootstrap** | Charter, CONTEXT-PACKET, ARCH-DECISION (WBS approved) | Grace, Ethan | PROJECT-CHARTER.md, CONTEXT-PACKET.md, ARCH-DECISION.md |
| **Scope and sync** | Documentation and scripting only; agents use of matrix = cursor-repo; product semantic layer not in scope | Grace | SCOPE-AND-SYNC.md, CONTEXT-PACKET §2.1 |
| **Families → Chroma** | Schema (AreaName, FamilyName, concept, books), ingest script, 288 rows layer=hesperia_families | Gena, Abelard | HESPERIA-FAMILIES-CHROMA-SCHEMA.md, ingest_hesperia_families.py |
| **Schema §6 (calculable)** | Hex unit, truth unit, paths, borders, traversal length, loops, loopability, road coordinates, border passings | Gena | HESPERIA-FAMILIES-CHROMA-SCHEMA.md §6 |
| **matrix_run** | CLI: geometry, path, road_coordinates, border_passings, traversal_length, is_loop, loopability (formula ref); CSV or Chroma | Gena | matrix_run.py, README §Matrix run |
| **Context RAG daemon** | Single entry point: calculable + optional retrieval + coherence_hints; matrix_run + Chroma; packet schema | Ethan (proposal), Gena (code), Abelard (deploy), Cursor (rules) | context_rag.py, CONTEXT-RAG-PACKET-SCHEMA.md |
| **Books–families wiring** | Bounding(concept, source, family, area); retrieval block includes books chunks when query/area_id/family_name | Abelard (verify), Gena (code) | context_rag.py _query_books_chunks, CHROMA-BOOKS-LIST-AND-WIRING |
| **L_full in context RAG** | When activation data provided (--activation PATH): L_full in calculable.loopability per 40_POLICY §11 | Gena | context_rag.py --activation, CONTEXT-RAG-PACKET-SCHEMA |
| **Semantic engine decision** | Use Chroma as semantic engine; no tech investigation for alternate engine unless Phase D or limits | Ethan | ETHAN-HESPERIA-SEMANTIC-ENGINE-REPORT.md |
| **Albina / FPF wiring** | hesperia_families as pylon alongside FPF and books; policy and ALBINA.md updated | Cursor | CHROMA-USAGE-POLICY, CHROMA-BOOKS-LIST-AND-WIRING, ALBINA.md |
| **Apple path tooling** | apple_path_imprint.py, apple_involvements.py; path store apple_paths/ | Gena | TASK-GENA-APPLE-HESPERIDES-PATH-SCRIPTS.md |
| **Multiple loop runs** | Harness, 24 runs, self-analysis report, informatics integration plan, boundaries doc | Grace, Ethan | TASK-GRACE-ETHAN-HESPERIA-MULTIPLE-LOOP-RUNS.md, HESPERIA-MULTIPLE-LOOP-BOUNDARIES.md |
| **Brain sync** | DOC_INDEX, WORKSPACE, CLIENTS/hesperia examination | Gena | EXAMINATION-2026-02-16.md |

All listed hesperia tasks in active.md for this phase are **DONE**. No OPEN hesperia rows as of 2026-02-18.

## 2. What we need

| Need | Status | Note |
|------|--------|------|
| **Activation data pipeline** | Not in place | L_full is computed when --activation file is provided; no automated activation feed yet. Optional for current use. |
| **Product semantic layer** | Out of scope (Phase D) | Full Hesperia RAG/engine in product workspace; when scope changes, Grace updates SCOPE-AND-SYNC and CONTEXT-PACKET. |
| **Region/obstacle in traversal** | Out of scope until data | TraversalService runLoop(region, …) and full loopability from region/activation; cursor-repo has ring-only + formula ref + L_full when activation file given. |
| **Open tasks** | None | Next work: new assignments from Grace/Albina or scope change (e.g. Phase D). |

## 3. Where we go (internal)

- **Next gates**: (1) New tasks only when Grace/Albina assign and triage into active.md. (2) Phase D only when product decision to bring semantic layer in scope — then SCOPE-AND-SYNC and CONTEXT-PACKET updated, WBS/ARCH-DECISION if needed.
- **Activation**: If we want L_full in production without manual --activation file, we need an activation data pipeline (source, format, who produces it). Not blocking current agents use.
- **Stability**: Boundaries (HESPERIA-MULTIPLE-LOOP-BOUNDARIES) are fixed; matrix and context RAG are the agents’ interface; product layer remains separate until Phase D.

---

# Part B — External report

## 1. Product description

**Hesperia** is a semantic-substrate product under the **prichindel.com** brand. It combines a formal **matrix** (12 areas × 24 families), **ring traversal**, and **calculable outputs** (geometry, path, borders, loopability) with optional **retrieval** (families, books) for AI and agent use. Ownership and IP: prichindel.com / igareosh.

## 2. Progress (mid-stage)

- **Matrix and schema**: Canonical matrix is defined and available (CSV and Chroma); schema includes coordinates, hex/truth units, paths, borders, traversal, and loopability.
- **Context service**: A single **context RAG** entry point provides a structured packet: calculable geometry and path, optional retrieval (families and book chunks), and coherence hints. Deployed and callable from the cursor repo.
- **Books–families link**: Retrieval can include book chunks scoped by family/area/concept when requested.
- **Loopability**: When activation data is available, the context packet includes the loopability value L_full (per policy). Without activation data, the packet carries the formula reference.
- **Boundaries**: Geometry and formulas are fixed; run parameters and matrix source are configurable; interfaces are read-only for agents. The full product semantic layer (RAG engine in product workspace) is planned for a later phase (Phase D).

## 3. Capabilities (current)

- **Structured context for AI**: One command returns a JSON context packet (calculable + optional retrieval + coherence hints) for use in prompts or workflows.
- **Matrix and traversal**: Ring traversal (start, direction, steps) with deterministic path, border passings, and road coordinates.
- **Families and books**: Query by area/family or free text; retrieval of families and related book chunks with bounding metadata.
- **Path tooling**: Paths can be stored and analysed (e.g. involvements by area and family).

## 4. Where we go (external)

- **Current stage**: Mid-stage — agents-oriented layer is live and stable; product semantic layer is not yet in scope.
- **Roadmap**: When the product moves to **Phase D**, the full semantic layer (RAG, indexing, services in the product workspace) will be brought in scope. Until then, delivery is via the context RAG and matrix tooling described above.
- **Dependencies**: Chroma as the semantic/knowledge backend; cursor repo (or equivalent) for scripts and state. No external client-facing commitments beyond what is documented here.

---

**SIGNED: Product (Grace) | Hesperia mid-stage consolidation, internal and external | 2026-02-18 | projects/hesperia**
