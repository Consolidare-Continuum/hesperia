<!--
HESPERIA — Reference Architecture Definition (RAD)
Copyright © 2026 igareosh.com — Platonov Igor (aka @igareosh). All rights reserved.
Restricted Research Disclosure License. Inspection and reference only.
No reproduction, redistribution, or use without explicit written permission.
See LEGAL_NOTICE.md for full terms.
-->

# Hesperia multiple loop runs — co-created boundaries

**Purpose**: Boundaries (scope, interfaces, guardrails) co-created from (1) deviation-based self-analysis and (2) informatics logic integration plan. **Task**: [TASK-GRACE-ETHAN-HESPERIA-MULTIPLE-LOOP-RUNS.md](TASK-GRACE-ETHAN-HESPERIA-MULTIPLE-LOOP-RUNS.md). **Owners**: Grace + Ethan. **Added**: 2026-02-17.

**Refs**: [HESPERIA-MULTIPLE-LOOP-RUNS-SELF-ANALYSIS-REPORT.md](HESPERIA-MULTIPLE-LOOP-RUNS-SELF-ANALYSIS-REPORT.md), [HESPERIA-INFORMATICS-LOGIC-INTEGRATION-PLAN.md](HESPERIA-INFORMATICS-LOGIC-INTEGRATION-PLAN.md); [projects/hesperia/CONTEXT-PACKET.md](../projects/hesperia/CONTEXT-PACKET.md), [projects/hesperia/SCOPE-AND-SYNC.md](../projects/hesperia/SCOPE-AND-SYNC.md). **Core mode MVP (areas/families only, logic tests)**: [ETHAN-HESPERIA-CORE-MODE-MVP.md](ETHAN-HESPERIA-CORE-MODE-MVP.md).

---

## 1. What is fixed

- **Geometry**: 12 areas, ring adjacency, 24 families per area, 250 hexes per family, 6 sides per hex (20_GEOMETRY, 13_SPEC). Not configurable in cursor-repo.
- **Ring step formula**: area_at(step) = (start + direction×step + 12) % 12 (40_POLICY §4.3). Deterministic.
- **Schema §6**: Hex unit, truth unit, paths, borders, traversal length, loops, loopability formula ref, output road traversal in coordinates. Definitions and formulas are fixed; implementation (matrix_run) conforms.

---

## 2. What is variable

- **Run parameters**: start_area_id (0..11), direction (±1), steps. Multiple loop runs vary these; deviation between runs is parameter-driven (see self-analysis report).
- **Matrix source**: CSV (canonical) or Chroma layer=hesperia_families. Same coordinates; source is switchable.
- **Activation data**: When present, loopability value (L_full, L_weighted) can be computed; today matrix_run returns formula ref only.

---

## 3. Interfaces (guardrails)

- **Matrix ↔ traversal**: Traversal reads matrix (CSV or Chroma); no write from traversal to matrix. Path output (road_coordinates, border_passings) is read-only for downstream (apple scripts, reporting).
- **Agents ↔ matrix/traversal**: Agents call matrix_run (CLI) or query Chroma layer=hesperia_families; they do not change geometry or schema. Apple path imprint writes to path store (apple_paths/), not to matrix.
- **Cursor-repo ↔ Hesperia product**: Cursor-repo uses Hesperia **data and geometry** for agents only. Product semantic layer (RAG, full engine, 14_SPEC services in product) is **out of scope** until Phase D (SCOPE-AND-SYNC).

---

## 4. Out of scope (until project decision)

- **Product semantic layer**: Full Hesperia semantic engine, RAG, indexing in product workspace. Not in cursor-repo scope.
- **Region/obstacle/activation in traversal**: TraversalService runLoop(region, maxPasses, …) and loopability **value** require region and activation data; cursor-repo implements ring-only traversal and formula ref until data exists.
- **Books–matrix wiring**: Un-paused 2026-02-17 (TASK-ABELARD-WIRE-FAMILIES-TO-BOOKS-LAYER DONE); bounding(concept, source, family, area) retrievable via hesperia_families; boundary remains: books layer is separate from matrix path store.

---

## 5. Summary

Boundaries: **fixed** = geometry and schema §6 formulas; **variable** = run params, matrix source, activation when present; **interfaces** = matrix/traversal read-only for agents, path store separate; **out of scope** = product semantic layer, full TraversalService/region/activation, until scope or data change.

---

**SIGNED: Product (Ethan) | boundaries co-created from self-analysis + informatics plan | 2026-02-17 | governance**
