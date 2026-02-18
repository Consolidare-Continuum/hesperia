# Task: Grace + Ethan — Hesperia multiple loop runs, self-analysis by traversal deviations, informatics logic integration, co-create boundaries

**Purpose**: (1) **Multiple loop runs**: Run matrix/traversal in loops (vary start, direction, steps); capture per-run outputs. (2) **Self-analysis**: Analyse traversal deviations by run (compare runs, derive deviation metrics from road_coordinates, border_passings, path). (3) **Plans**: Informatica logic integration — how informatics/logic layer plugs into matrix and traversal (specs, schema, agents context). (4) **Co-create boundaries**: Define boundaries (scope, interfaces, guardrails) from the previous two — deviation-based analysis + informatics logic integration. **Owners**: Grace (triage, scope, self-task), Ethan (delivery: runs, analysis, plans, boundaries). **Added**: 2026-02-17. **Status**: DONE (2026-02-17).

**Refs**: [HESPERIA-FAMILIES-CHROMA-SCHEMA.md](HESPERIA-FAMILIES-CHROMA-SCHEMA.md) §6, [HESPERIA-AGENTS-PATH-ETHAN-REPORT.md](HESPERIA-AGENTS-PATH-ETHAN-REPORT.md), [TASK-TEAM-MATRIX-RUN-AGENTS-CONTEXT.md](TASK-TEAM-MATRIX-RUN-AGENTS-CONTEXT.md); cluster/chroma-server/matrix_run.py; [CLIENTS/hesperia/40_POLICY__Loopability_and_traversal.txt](../CLIENTS/hesperia/40_POLICY__Loopability_and_traversal.txt); [projects/hesperia/CONTEXT-PACKET.md](../projects/hesperia/CONTEXT-PACKET.md).

---

## 1. Scope (Grace + Ethan)

| Stream | Description | Output |
|--------|-------------|--------|
| **Multiple loop runs** | Execute matrix_run (or equivalent traversal) in a loop; vary `--start` (0..11), `--direction` (±1), `--steps` (e.g. 12, 24); record each run’s JSON (road_coordinates, border_passings, traversal_length, is_loop). | Run log or small harness; dataset of N runs. |
| **Self-analysis by run** | For each run (or pairwise), compute **traversal deviations**: e.g. path difference, border-passing differences, length/loop consistency. Self-analysis = summary metrics and/or report of how runs deviate. | Deviation metrics; short self-analysis report. |
| **Plans: informatics logic integration** | Document how **informatics logic** (data structures, reasoning, logic layer) integrates with matrix and traversal: inputs, outputs, schema alignment, agents context. Ref Hesperia specs (e.g. 12_SPEC, 14_SPEC, 40_POLICY). | Plan or addendum (informatics logic ↔ matrix/traversal). |
| **Co-create boundaries** | Using (1) deviation-based self-analysis and (2) informatics logic integration plan, **co-create boundaries**: scope boundaries, interface boundaries, guardrails (what is in/out of scope for agents, product, cursor-repo). | Boundaries doc or section in CONTEXT-PACKET / governance. |

---

## 2. Execution notes

- **Runs**: Use `matrix_run.py` from repo root; CSV default. Optionally script a small loop (e.g. all 12 starts × 2 directions × 1 full ring) and collect JSONs.
- **Deviations**: Define “deviation” (e.g. same start/direction/steps → same road_coordinates; or compare different runs and quantify difference). No new code required in matrix_run if analysis is post-hoc.
- **Informatics logic**: Align with existing Hesperia docs (DOC_INDEX, 12_SPEC, 14_SPEC); cursor-repo scope only (agents context).
- **Boundaries**: One-page or structured list: what is fixed (geometry, schema), what is variable (runs, activation when present), what is out of scope (product semantic layer until Phase D).

---

## 3. Deliverables

1. **Run dataset or run log** (multiple loop runs).
2. **Self-analysis report** (traversal deviations by run; metrics and summary).
3. **Informatics logic integration plan** (how informatics/logic plugs into matrix/traversal; refs to schema and specs).
4. **Boundaries** (co-created from 1+2): scope, interfaces, guardrails; add to governance or projects/hesperia as agreed.

---

## 4. Completion

**Done 2026-02-17 (Ethan delivery).** (1) Run dataset: harness `cluster/chroma-server/multi_loop_runs_harness.py`; 24 runs in `cluster/chroma-server/multi_loop_runs/` (12 start × 2 direction × 12 steps); index.json. (2) Self-analysis: [HESPERIA-MULTIPLE-LOOP-RUNS-SELF-ANALYSIS-REPORT.md](HESPERIA-MULTIPLE-LOOP-RUNS-SELF-ANALYSIS-REPORT.md). (3) Informatics logic integration: [HESPERIA-INFORMATICS-LOGIC-INTEGRATION-PLAN.md](HESPERIA-INFORMATICS-LOGIC-INTEGRATION-PLAN.md). (4) Boundaries: [HESPERIA-MULTIPLE-LOOP-BOUNDARIES.md](HESPERIA-MULTIPLE-LOOP-BOUNDARIES.md). active.md row set to DONE.
