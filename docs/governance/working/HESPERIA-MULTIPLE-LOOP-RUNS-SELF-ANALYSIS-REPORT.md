<!--
HESPERIA — Reference Architecture Definition (RAD)
Copyright © 2026 igareosh.com — Platonov Igor (aka @igareosh). All rights reserved.
Restricted Research Disclosure License. Inspection and reference only.
No reproduction, redistribution, or use without explicit written permission.
See LEGAL_NOTICE.md for full terms.
-->

# Hesperia multiple loop runs — self-analysis report (traversal deviations by run)

**Purpose**: Self-analysis of traversal deviations across multiple matrix runs. **Task**: [TASK-GRACE-ETHAN-HESPERIA-MULTIPLE-LOOP-RUNS.md](TASK-GRACE-ETHAN-HESPERIA-MULTIPLE-LOOP-RUNS.md). **Owner**: Ethan (delivery). **Added**: 2026-02-17.

**Dataset**: 24 runs from harness `cluster/chroma-server/multi_loop_runs_harness.py` — 12 start area_id × 2 directions (CW=1, CCW=-1) × 12 steps (one full ring). Stored in `cluster/chroma-server/multi_loop_runs/*.json`; index in `multi_loop_runs/index.json`.

---

## 1. Deviation definition

- **Path**: Ordered sequence of steps = `road_coordinates` (each step: area_id, global_id, area_name, family_name).
- **Same run params** (start, direction, steps): Path is **deterministic** per 40_POLICY ring formula; re-runs yield identical road_coordinates.
- **Traversal deviation (cross-run)**: Two runs with **different** (start, direction) produce **different** path sequences. Deviation is quantified by:
  - **Area sequence**: List of area_id per step. Two runs deviate if their area sequences differ (e.g. start0 dir1 → areas 0,1,2,…,11; start1 dir1 → 1,2,…,11,0).
  - **Border-passing count**: area_border_passings length (full ring 12 steps = 11 area borders crossed); family_border_passings length (depends on which family is chosen per area — first in list).
  - **Set of areas touched**: For 12 steps, all 12 areas are touched in every run; set overlap = 12. Deviation shows in **order**, not in set.

---

## 2. Metrics (from dataset)

| Metric | Value |
|--------|--------|
| Runs | 24 |
| Steps per run | 12 |
| traversal_length | 12 (all runs) |
| area_border_passings per run | 11 (full ring: 12 steps ⇒ 11 borders) |
| Determinism | Same (start, direction, steps) → same road_coordinates (matrix_run is deterministic). |

**Cross-run deviation (by design)**:
- **Same start, opposite direction**: CW vs CCW → reversed area sequence; same areas, opposite order.
- **Different start, same direction**: Shifted area sequence (e.g. start 0 CW = 0,1,…,11; start 1 CW = 1,2,…,11,0).
- **Different start, opposite direction**: Shifted and reversed.

No “anomaly” deviation: all runs conform to ring geometry (40_POLICY §4.3). Deviation between runs is **expected** from parameter difference.

---

## 3. Summary

- **Run log**: 24 JSON files; index in `multi_loop_runs/index.json`. Harness: `multi_loop_runs_harness.py`.
- **Self-analysis**: Paths are deterministic per (start, direction, steps). Cross-run deviations are **parameter-driven** (different start/direction → different path order); no inconsistency with schema or 40_POLICY.
- **Use for boundaries**: Fixed = geometry, 12 areas, ring step formula. Variable = start, direction, steps, and (when available) activation data for loopability value.

---

**SIGNED: Product (Ethan) | multiple loop runs self-analysis | 2026-02-17 | governance**
