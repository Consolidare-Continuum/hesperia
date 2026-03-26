<!--
HESPERIA — Reference Architecture Definition (RAD)
Copyright © 2026 igareosh.com — Platonov Igor (aka @igareosh). All rights reserved.
Restricted Research Disclosure License. Inspection and reference only.
No reproduction, redistribution, or use without explicit written permission.
See LEGAL_NOTICE.md for full terms.
-->

# Hesperia — generalized input_context: narrative of 2026-02-17 tasks

**Purpose**: Wrap-up narrative for today’s Hesperia work in the cursor repo. Single read for future sessions: what was done, in what order, and how it fits together. **Produced**: Grace. **Date**: 2026-02-17.

---

## 1. Where we started

Hesperia is the prichindel.com semantic-substrate product (sphere, families, specs in CLIENTS/hesperia). In the **cursor repo** we do not build the product semantic layer; we use Hesperia **data and geometry** to serve **agents** (Albina, Cursor): a matrix of 12 areas × 24 families, ring traversal, and calculable outputs. That distinction — product vs cursor-repo agents use — was already in SCOPE-AND-SYNC and was reinforced today.

Before today: families schema and ingest path existed; Gena had delivered schema §6 (hex unit, truth unit, paths, borders, loopability ref), matrix_run.py, and the compressed world-view description. Abelard had run the families ingest (288 rows, layer=hesperia_families). The next step was to **wire** that table into the agents’ input_context and then extend the tooling around runs and paths.

---

## 2. Wire: matrix as pylon for Albina and FPF

The hesperia families table in Chroma (layer=hesperia_families) was live but not yet part of Albina’s construction. The task was to add it as an **additional pylon** alongside FPF and books so Albina can combine family→concept→books with first-principles input_context.

**Done (Cursor)**: Policy and wiring updated so that Albina (and query_knowledge when used as Albina) explicitly include **hesperia_families**: in CHROMA-USAGE-POLICY (layer list and §2.2), in CHROMA-BOOKS-LIST-AND-WIRING (Albina = fpf + books + books_general + hesperia_families), and in cluster/ALBINA.md (FPF exception). No code change — wiring is in the “upstairs” input_context: when to query which layers. The matrix is now a first-class pylon for Albina next to FPF and books.

---

## 3. Apple: virtual running body and path tooling

We introduced a **virtual running body** “apple hesperides” (apple): it has a self-describing position and a **path** (sequence of positions on the sphere). The sphere is the matrix looped as a body (12 areas, hex sides → statements). After any run (e.g. from matrix_run), we needed two scripts: one to **imprint** apple’s path on the matrix (persist it), and one to **describe** apple’s content involvements (which families and areas it touched).

**Done (Gena)**: Script 1 (`apple_path_imprint.py`) reads apple run JSON (stdin or file), writes to `cluster/chroma-server/apple_paths/<run_id>.json`. Script 2 (`apple_involvements.py`) reads a path (file or stdin) and outputs a description: areas, families, area–family pairs, counts, summary (JSON and optional text). Path store is under `apple_paths/`; README documents the flow (matrix_run → imprint → involvements). So: run the matrix, then imprint the path, then ask “what did apple touch?” — all in repo and callable by agents.

---

## 4. Multiple loop runs: harness, self-measurement, informatics plan, boundaries

The next block was to run the matrix **in a loop** (vary start, direction, steps), capture outputs, and then use that to (a) analyse **traversal deviations** by run, (b) document how **informatics logic** integrates with matrix and traversal, and (c) **co-create boundaries** (what is fixed, variable, in scope, out of scope).

**Done (Grace + Ethan)**:

- **Harness**: `multi_loop_runs_harness.py` runs matrix_run for all 12 start areas × 2 directions × 12 steps (one full ring each). **24 runs** were produced and stored in `cluster/chroma-server/multi_loop_runs/` with an index. So we have a small dataset of ring traversals.

- **Self-measurement**: A short report defines “deviation” (path difference when run parameters differ), states that paths are deterministic for the same (start, direction, steps), and that cross-run differences are **config_param-driven** — no inconsistency with schema or 40_POLICY. Metrics (traversal length, border counts) are summarized. That gives a clear baseline: fixed geometry, variable params, expected variation.

- **Informatics logic integration plan**: A governance doc describes how the informatics/logic layer (data structures, 14_SPEC TraversalService, 40_POLICY) plugs into the matrix and traversal: inputs (matrix CSV/Chroma, path params), outputs (road_coordinates, border_passings, etc.), alignment with schema §6, and agents’ use (matrix_run, Chroma, apple scripts). Cursor-repo is framed as a **subset** of the spec that agents can call today; full TraversalService (region, activation) stays for when data and scope allow.

- **Boundaries**: A second doc co-creates **boundaries** from the self-measurement and the informatics plan: **fixed** = geometry and §6 formulas; **variable** = run params, matrix source, activation when present; **interfaces** = matrix/traversal read-only for agents, path store separate; **out of scope** = product semantic layer, full TraversalService/region/activation until Phase D or data un-pause.

So in one day we went from “matrix in Chroma but not wired for Albina” to: matrix as pylon, apple path tooling, and a loop-run dataset plus explicit deviation logic, informatics integration, and boundaries. That gives future work a clear frame: what is stable, what is allowed to vary, and where the cursor-repo line is.

---

## 5. Generalized input_context (for future use)

- **Matrix in cursor repo**: Single canonical matrix (CSV + Chroma layer=hesperia_families). Used for **agents only** (Albina, Cursor, matrix_run, apple). Product semantic layer is not in scope.
- **Path and run**: One run = (start, direction, steps) → one path (road_coordinates, border_passings). Paths can be stored (apple_paths, multi_loop_runs) and analysed (involvements, deviations). Apple is the virtual body whose path we imprint and describe.
- **Policy**: CHROMA-USAGE-POLICY and CHROMA-BOOKS-LIST-AND-WIRING define who queries which layers; Albina gets fpf + books + hesperia_families. Boundaries doc (HESPERIA-MULTIPLE-LOOP-BOUNDARIES) states what is fixed vs variable and what is out of scope.
- **Next steps** (when needed): Wire families to books layer — **DONE 2026-02-17** (Abelard; bounding + retrieval in CHROMA-BOOKS-LIST-AND-WIRING). Product semantic layer only if scope changes (Phase D). No open hesperia task left from today’s batch; Grace checks DONEs and this narrative closes the day.

---

**Compliance**: Today’s deliverables are agent-facing (rules/docs for Abelard, Gena, Cursor). No team operational files (OPERATIONAL-LAYER, ROLE-RESOLUTIONS, entity folders) edited by assistants. Handoff artifacts signed per ARTIFACT-SIGNATURE-POLICY. Tone: imperative; did/asked/summary.

**SIGNED: Product/Triage (Grace) | narrative hesperia tasks 2026-02-17 | 2026-02-17 | governance**
