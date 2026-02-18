# Hesperia core mode MVP — mode, scope, outputs for logic tests (Ethan)

**Purpose**: Statements of **mode**, **scope**, and **output generation** so all scripts and matrix are functional and testable with **areas and families only** (core mode). No statements level, no books level. Output contract for MVP core and logic tests. **Owner**: Ethan. **Date**: 2026-02-18.

**Refs**: [HESPERIA-FAMILIES-CHROMA-SCHEMA.md](HESPERIA-FAMILIES-CHROMA-SCHEMA.md), [HESPERIA-MULTIPLE-LOOP-BOUNDARIES.md](HESPERIA-MULTIPLE-LOOP-BOUNDARIES.md), [CONTEXT-RAG-PACKET-SCHEMA.md](CONTEXT-RAG-PACKET-SCHEMA.md), [ETHAN-HESPERIA-OPERATOR-INTERFACE-SPEC.md](ETHAN-HESPERIA-OPERATOR-INTERFACE-SPEC.md).

---

## 1. Core mode (definition)

**Core mode** = operation and testing using **only areas and families** (geometry, path, coordinates, polarity). No **statements** (no formula/statement set, no v(φ) over statement content). No **books** (no retrieval chunks, no book_refs content in test inputs).

- **In scope for core**: area_id (0..11), area_name (12 canonical names), family_name, global_id, path as sequence of (area_id, global_id) or (area_id, family_name), road_coordinates, border_passings, geometry constants, path_params, loopability (formula_ref; L_full only when activation file provided), polarity axes, obstacle state (CLEAR / OBSTACLE_*), hazard map (area, family) → CLEAR | TENSION | UNSAFE.
- **Out of scope for core**: statement_set, retrieval.families (document text / concept), retrieval.chunks (books), any atom/formula content beyond area/family identifiers. Logic tests in core mode **do not** require or assert on statement or book content.

---

## 2. Scope — scripts and matrix (functional and testable)

| Script / component | In core mode | Output for logic tests |
|--------------------|--------------|-------------------------|
| **matrix_run.py** | Yes. Default: CSV; optional --chroma. | JSON: matrix_source, geometry, path_params, road_coordinates (step, area_id, global_id, area_name, family_name), border_passings (area_border_passings, family_border_passings), traversal_length, is_loop, loopability (formula_ref [+ L_full when --activation]). |
| **context_rag.py** | Yes when **no retrieval**: no --query, no --area_id, no --family_name (or core-mode flag). | JSON: matrix_source, calculable (same as matrix_run), coherence_hints (current_area_id, current_area_name, suggested_adjacent_areas, traversal_summary, border_passings_count). No retrieval key. Optional --activation for L_full only. |
| **hesperia_logic.py** | Yes. State and path keyed by area_id / (area_id, family_id) only; no statement_set in path_context for core tests. | Area.enforce/test_validity/detect_contradiction; Family/Hex/Path/Hop; obstacle state; VALIDATE/SATISFY/UNSAT/ENTAILS (stub on atoms keyed by area); hazard_map_update. Inputs: path = list (area_id, global_id), state = dict (area/family keys only). Outputs: boolean or result dict (valid, contradiction, state_after, obstacle). |
| **apple_path_imprint.py** | Yes. Input: matrix_run JSON (road_coordinates). | Writes path to apple_paths/{run_id}.json. Output file: path as list of positions (area_id, global_id or area_name, family_name). |
| **apple_involvements.py** | Yes. Input: path (from imprint or matrix_run JSON). | JSON/text: areas, families, area–family pairs, counts. No statement or book content. |
| **multi_loop_runs_harness.py** | Yes. Runs matrix_run in loop. | Directory of run JSONs (same shape as matrix_run); index.json. Logic tests can consume any run JSON (road_coordinates, path_params, etc.). |

**Matrix**: Canonical matrix = CSV (CLIENTS/hesperia/v0.1/hex_sphere_areas_families_ideal_proportions.csv) or Chroma layer=hesperia_families. In core mode, matrix is read-only; coordinates (area_id, area_name, family_name, global_id) and geometry (12 areas, 24 families per area) are the only data used. No statement or book payload required.

---

## 3. Output contract for MVP core (logic tests)

Logic tests that run **only on areas and families** may rely on the following outputs. All scripts above MUST produce these shapes in core mode so tests are deterministic and implementation-agnostic to statements/books.

### 3.1 matrix_run (and context_rag calculable block)

- **path_params**: `{ "start_area_id": int, "direction": 1|-1, "steps": int }`.
- **road_coordinates**: array of `{ "step": int, "area_id": int, "global_id": int, "area_name": string, "family_name": string }` in visit order.
- **border_passings**: `{ "area_border_passings": [...], "family_border_passings": [...] }` (crossing events; each event includes area_id / global_id or equivalent).
- **geometry**: AREA_COUNT=12, FAMILIES_PER_AREA=24, STEPS_PER_PASS=12, etc.
- **traversal_length**, **is_loop**: number, boolean.
- **loopability**: at least `{ "formula_ref": string, "requires_activation_data": bool }`; optionally **L_full** when activation data provided.

### 3.2 context_rag (core mode: no retrieval)

- **calculable**: same as §3.1.
- **coherence_hints**: `{ "current_area_id": int, "current_area_name": string, "suggested_adjacent_areas": [ { "area_id", "area_name", "direction" } ], "traversal_summary": string, "border_passings_count": { "area_border_passings": int, "family_border_passings": int } }`.
- **retrieval**: MUST be absent in core mode.

### 3.3 hesperia_logic (core mode)

- **Input**: path = list of (area_id, global_id); state = dict keyed by area/family (e.g. area_id or (area_id, global_id)); path_context without statement_set or with empty statement_set.
- **Output**: Area: (success: bool, message: str); Hex.evaluate: { valid, contradiction, state_after, obstacle }; Path.polarize(): dict area_id → +1|-1; obstacle state enum; hazard_map (area_id, family_id) → CLEAR | TENSION | UNSAFE.
- Logic tests MUST NOT pass or assert on statement_set or book content; only area_id, family_id, global_id, path, polarity, obstacle.

### 3.4 Apple scripts

- **apple_path_imprint**: output file with path (list of { area_id, global_id } or { area_name, family_name }).
- **apple_involvements**: output with areas list, families list, counts, area–family pairs; no statement or book content.

---

## 4. Testability (logic tests based only on areas and families)

- **Logic tests** may: invoke matrix_run (or context_rag without retrieval), parse JSON, assert on path_params, road_coordinates (sequence of area_id, family_name), traversal_length, is_loop, border_passings counts; invoke hesperia_logic with path and state keyed by area_id/family only, assert on valid/contradiction/obstacle and polarity; invoke apple scripts, assert on path and involvements (areas, families, counts).
- **Logic tests** must NOT: require statement_set, retrieval.chunks, or any book/statement content. Core mode is sufficient for geometry, path, polarity, and obstacle behaviour.
- **Output generation for MVP core**: All scripts above SHALL produce the outputs in §3 when run in core mode (matrix_run always; context_rag when no retrieval; hesperia_logic when state/path_context use only area/family keys; apple scripts by design). This enables a single test harness that runs logic tests from these outputs only.

---

## 5. Summary

| Item | Statement |
|------|-----------|
| **Mode** | Core mode = areas and families only; no statements level, no books level. |
| **Scope** | matrix_run, context_rag (no retrieval), hesperia_logic (area/family state only), apple_path_imprint, apple_involvements, multi_loop_runs harness — all functional and testable in core mode. |
| **Output** | Contract §3: path_params, road_coordinates, border_passings, geometry, loopability, coherence_hints; hesperia_logic result (valid, contradiction, obstacle, polarize); apple path and involvements. No retrieval, no statement_set, no chunks in core outputs. |
| **Logic tests** | Run against above outputs only; no dependency on statements or books. MVP core output generation is complete when scripts conform to §3. |

---

## 6. Internal calibration (Plan 1 invocation)

**Plan 1** ([ETHAN-HESPERIA-PLAN-1-INVOCATION-CORE-MODE.md](ETHAN-HESPERIA-PLAN-1-INVOCATION-CORE-MODE.md)) is an **internal calibration harness**: one run that executes all core-mode components (matrix_run, context_rag without retrieval, hesperia_logic, apple_path_imprint, apple_involvements) and writes all outputs to a timestamped log dir. It is for **calibration** and **general sense of state**; it outputs its own results, not the main product spec. The **MVP** (this document) is the mode, scope, and output **contract** for logic tests and core-mode behaviour; Plan 1 is the internal function that runs and logs everything for inspection.

---

**SIGNED: Architecture (Ethan) | Hesperia core mode MVP — mode, scope, outputs for logic tests | 2026-02-18 | governance**
