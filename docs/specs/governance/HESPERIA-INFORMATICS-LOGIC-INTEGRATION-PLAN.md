# Hesperia — informatics logic integration plan (matrix and traversal)

**Purpose**: Document how the **informatics logic** layer (data structures, reasoning, logic) integrates with the matrix and traversal in the cursor-repo agents context. **Task**: [TASK-GRACE-ETHAN-HESPERIA-MULTIPLE-LOOP-RUNS.md](TASK-GRACE-ETHAN-HESPERIA-MULTIPLE-LOOP-RUNS.md). **Owner**: Ethan. **Added**: 2026-02-17.

**Refs**: [HESPERIA-FAMILIES-CHROMA-SCHEMA.md](HESPERIA-FAMILIES-CHROMA-SCHEMA.md) §6, [HESPERIA-AGENTS-PATH-ETHAN-REPORT.md](HESPERIA-AGENTS-PATH-ETHAN-REPORT.md); CLIENTS/hesperia/12_SPEC (Semantic Engine), 14_SPEC (Services and APIs — TraversalService), 40_POLICY (Loopability and traversal).

---

## 1. Integration points (cursor-repo scope)

| Layer | Role | Integration with matrix/traversal |
|-------|------|----------------------------------|
| **Matrix (data)** | Canonical coordinates: area_id, global_id, area_name, family_name. Source: CSV (mandatory) or Chroma layer=hesperia_families. | **Input** to traversal: ring step formula uses area_id; family at each step from matrix. Schema §6 defines path, borders, road_coordinates. |
| **Traversal (logic)** | Ring step: area_at(step) = (start + direction×step + 12) % 12 (40_POLICY §4.3). Deterministic path from (start, direction, steps). | **Output**: road_coordinates, border_passings (area and family), traversal_length, is_loop. Implemented in matrix_run.py; no activation data yet → loopability formula ref only. |
| **Informatics logic (spec)** | 14_SPEC TraversalService: runLoop(region, maxPasses, dominance, obstacleTheta) → LoopResult; 40_POLICY formulas (L_full, novelty). | **Alignment**: cursor-repo matrix_run implements **ring traversal only** (fixed geometry, no region/obstacle yet). When activation/region data exists, TraversalService contract can be fulfilled by extending matrix_run or a sibling script. |
| **Agents context** | query_knowledge (Chroma layer=hesperia_families); matrix_run.py (CLI); apple_path_imprint, apple_involvements. | **Consumption**: Agents get matrix-derived context via Chroma or matrix_run output; path can be imprinted and described (apple scripts). |

---

## 2. Inputs and outputs (contract)

- **Inputs**: (1) Matrix: CSV or Chroma layer=hesperia_families. (2) Path params: start_area_id (0..11), direction (±1), steps. (3) Optional later: region, activation vectors (for loopability value).
- **Outputs**: geometry constants, hex_unit, truth_unit, borders (area ring), path_params, road_coordinates, border_passings (area + family), traversal_length, is_loop, loopability (formula ref; value when activation data available).
- **Schema alignment**: All outputs are defined and calculable per schema §6; 20_GEOMETRY, 13_SPEC, 40_POLICY are the source for formulas.

---

## 3. Logic layer (Hesperia product vs cursor-repo)

- **Product (Hesperia)** per 14_SPEC: TraversalService, GeometryService, AttributionService, etc. — full semantic engine. **Not in scope** for cursor-repo; product semantic layer is Phase D when scope changes.
- **Cursor-repo**: Implements **traversal logic** sufficient for agents: ring path from (start, direction, steps); matrix as data source; no region/obstacle/activation yet. Informatics logic **integration** = this plan: same formulas, same coordinates, same output shape; cursor-repo is a **subset** of the spec that agents can call today.

---

## 4. Summary

Informatics logic integrates with matrix and traversal by: (1) using matrix (CSV/Chroma) as single source of coordinates and names; (2) applying 40_POLICY ring step formula to produce path and border_passings; (3) exposing outputs per schema §6; (4) aligning with 14_SPEC TraversalService conceptually (ring traversal only); (5) serving agents via matrix_run, Chroma, and apple scripts. No new code in matrix_run required for this plan; extensions (activation, loopability value, region) when data and scope allow.

---

**SIGNED: Product (Ethan) | informatics logic integration plan | 2026-02-17 | governance**
