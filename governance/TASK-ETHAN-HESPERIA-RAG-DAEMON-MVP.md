# Task: Ethan — Hesperia project model → RAG deployment daemon (context MVP)

**Purpose**: Adjust the Hesperia project model so it becomes **structured and viable as a RAG deployment daemon** that provides Cursor with **necessary context calculation**. Start from what exists today; final station = **MVP**: a stable context RAG that works in a FPF-like way but **math- and program-based**, with **sources and statements calculations** to provide AI with **values to adjust coherence and contexts** where values go off. **Owner**: Ethan. **Triage**: Grace. **Added**: 2026-02-17.

**Refs**: [HESPERIA-AGENTS-PATH-ETHAN-REPORT.md](HESPERIA-AGENTS-PATH-ETHAN-REPORT.md), [projects/hesperia/CONTEXT-PACKET.md](../projects/hesperia/CONTEXT-PACKET.md), [projects/hesperia/SCOPE-AND-SYNC.md](../projects/hesperia/SCOPE-AND-SYNC.md); [HESPERIA-FAMILIES-CHROMA-SCHEMA.md](HESPERIA-FAMILIES-CHROMA-SCHEMA.md), [BOOKS-LAYER-AND-MATRIX-COMPRESSED-WORLD-VIEW.md](BOOKS-LAYER-AND-MATRIX-COMPRESSED-WORLD-VIEW.md); cluster/chroma-server/matrix_run.py, ingest_hesperia_families.py; [CLIENTS/hesperia/DOC_INDEX.md](../CLIENTS/hesperia/DOC_INDEX.md).

---

## 1. Scope

1. **Starting point (today)**: Current Hesperia agents-oriented layer: matrix + schema (§6 calculable units), Chroma layer hesperia_families, matrix_run (geometry, hex_unit, truth_unit, borders, road_coordinates, border_passings, traversal_length, is_loop, loopability); compressed world view; FPF/books wiring in cursor-repo. All of this is cursor-repo scope per CONTEXT-PACKET §2.1.

2. **Goal — RAG deployment daemon**: Propose and structure a path so that this layer becomes a **RAG deployment daemon** that:
   - Provides **Cursor** (and agents) with **necessary context calculation** (not only retrieval).
   - Is **math- and program-based**: sources, statements, and calculable values (from schema, matrix_run, and Hesperia specs) that can be used to **adjust AI coherence and contexts** where values go off — i.e. a stable **context RAG** that supplies **values** for correction/grounding, FPF-like but driven by calculations and statements.

3. **Final station — MVP**: An **MVP** based on prototype ideas and concept:
   - **Stable context RAG**: deterministic or scripted context computation (sources + statements + calculated values).
   - **Consumable by Cursor**: daemon or service that Cursor (and automation) can call for context packets.
   - **Math/program-based**: formulas, coordinates, traversal, loopability, and statement-level semantics from Hesperia docs; not only embedding similarity.

4. **Deliverable**: A **structured proposal** (document in governance/ or projects/hesperia/): (a) current-state summary; (b) model adjustment (how to structure the existing pieces as a daemon/service); (c) MVP definition (scope, interfaces, what “context calculation” returns, how sources and statements feed values for coherence); (d) phased steps (realistic, deployable, addressable) with ownership. Artifact signature per ARTIFACT-SIGNATURE-POLICY.

---

## 2. Out of scope (this task)

- Implementing the daemon code (handoff to Gena/Abelard after proposal).
- Changing Hesperia **product** semantic-layer scope (SCOPE-AND-SYNC unchanged for product; cursor-repo agents use only).

---

## 3. Handoffs

- **After Ethan deliverable**: Grace triages follow-on (implementation, deploy); Gena for code/scripts; Abelard for deploy/Chroma/ingest if needed.

---

## 4. Completion

- **Status**: DONE (2026-02-17). **Deliverable**: [HESPERIA-RAG-DAEMON-MVP-PROPOSAL-ETHAN.md](HESPERIA-RAG-DAEMON-MVP-PROPOSAL-ETHAN.md) — current-state summary, model adjustment (daemon as thin orchestration over matrix_run + Chroma), MVP definition (scope, interfaces, context packet, coherence hints), phased steps (Gena 4.1–4.2, Abelard 4.3, Cursor 4.4).
- **Team assigned (Grace, 2026-02-17)**: Ethan (proposal) → Gena (implement daemon/code after Ethan DONE) → Abelard (deploy/operate on prichindel after Gena DONE). Rows in active.md.

---

## 5. Green light (Grace)

- **Green light (2026-02-17)**: Gena cleared to start implementation (steps 4.1–4.2 per [HESPERIA-RAG-DAEMON-MVP-PROPOSAL-ETHAN.md](HESPERIA-RAG-DAEMON-MVP-PROPOSAL-ETHAN.md) §4). Boss approval recorded; no gate block.

---

## 6. Grace check (dones)

- **Ethan**: DONE. Deliverable [HESPERIA-RAG-DAEMON-MVP-PROPOSAL-ETHAN.md](HESPERIA-RAG-DAEMON-MVP-PROPOSAL-ETHAN.md) present; current-state summary, model adjustment, MVP definition, phased steps with ownership. Signed.
- **Gena**: DONE. Deliverables present: [context_rag.py](../cluster/chroma-server/context_rag.py), [CONTEXT-RAG-PACKET-SCHEMA.md](CONTEXT-RAG-PACKET-SCHEMA.md), README §Context RAG. Script returns packet (calculable + coherence_hints + optional retrieval); schema documented.
- **Abelard**: DONE. Deploy documented in [cluster/chroma-server/README.md](../cluster/chroma-server/README.md) §Context RAG (Deploy (Abelard)); on-demand from repo root; no new unit; verified runnable.
- **Chain**: Ethan → Gena → Abelard complete. Cursor wiring (step 4.4) remains optional; no OPEN blocker for MVP.
- **Follow-on assigned (Grace)**: Rows in active.md per Ethan proposal §4.4–4.6: Cursor (wire context_rag in rules/README; optional MCP/workflow); Gena (books chunks in retrieval when wiring un-paused §4.5; L_full when activation data §4.6). **§4.5 split**: Abelard = verify books layer + bounding available for context_rag when un-paused; Gena = ensure context_rag retrieval block includes books chunks (after or with Abelard).
- **Cursor (4.4)**: DONE (2026-02-17). Rules: cursor-main-awareness.mdc §Context RAG (full packet) — run context_rag.py from repo root, parse JSON, inject; refs schema + proposal. INDEX.md §Quick entry points: context_rag.py + schema link. Optional MCP/workflow step not implemented; document path complete.
- **Abelard (§4.5 verify)**: DONE (2026-02-17). [ABELARD-VERIFY-BOOKS-BOUNDING-FOR-CONTEXT-RAG.md](ABELARD-VERIFY-BOOKS-BOUNDING-FOR-CONTEXT-RAG.md) — books layer + bounding available; handoff to Gena for retrieval.chunks.
- **Unpause all**: Books–families wiring un-paused (TASK-ABELARD-WIRE DONE; HESPERIA-MULTIPLE-LOOP-BOUNDARIES, TASK-HESPERIA-FAMILIES-CHROMA-ALBINA updated). All assigned; Gena 4.5 and 4.6 OPEN — proceed.
- **Grace status (proceed)**: Ethan → Gena → Abelard → Cursor (4.4) → Abelard verify (4.5) → Gena (4.5 books chunks) = **all DONE**. **One OPEN**: Gena §4.6 — add L_full to context_rag when activation data exists. **Blocker**: activation data (TAU_FAMILY, per-family activation) not yet available; task remains OPEN until data or decision to stub. **Proceed**: run workflow → current step = Gena §4.6 (blocked on data); or assign other work; or close §4.6 as "later when activation pipeline exists".
- **End of day (2026-02-17)**: Notes — will continue other time. Context RAG MVP complete (proposal → implement → deploy → wire → verify → books chunks). Only §4.6 OPEN (L_full when activation data). Resume: run workflow or assign next; §4.6 when activation pipeline exists.

---

**SIGNED: Product/Triage (Grace) | task Ethan hesperia RAG daemon MVP | 2026-02-17 | governance**
