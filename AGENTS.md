<!--
HESPERIA — Reference Architecture Definition (RAD)
Copyright © 2026 igareosh.com — Platonov Igor (aka @igareosh). All rights reserved.
Restricted Research Disclosure License. Inspection and reference only.
No reproduction, redistribution, or use without explicit written permission.
See LEGAL_NOTICE.md for full terms.
-->

# AGENT GUIDELINES — HESPERIA (v0.5)

This repository is in the Reference Architecture state. **Single version: v0.5** end-to-end. Version suffixes stripped from active code; versioned tools/calibration/validation moved to `legacy/deprecated/`. Agents must align all work with the current top-level layout and avoid legacy-era paths.

## Canonical Top-Level Structure

Active repository structure:

- `core/`
- `hesperia/` (engine: `hesperia.engine.kme` — Knowledge Metrics Engine)
- `runtime/`
- `lexicon/`
- `tools/`
- `assets/`
- `tests/`
- `docs/`
- `legacy/`

Do not use or reintroduce old roots such as `sphere_rag/`, `hesperia_lex/`, `scripts/`, `api/`, `governance/`, or `project/` as active top-level architecture.

## Responsibilities

- `core/`
  - Deterministic computation layers.
  - `layer_1` through `layer_9`.
  - Topology, math, propagation.
  - **Topology (10+2):** Area graph is an **icosahedral surface graph** (12 nodes, 30 edges, degree 5 per node). 10 operational areas (240 families, 60k hexes); 2 reserved service areas (48 families, 12k hexes). Meta reference nodes A6, A12 (indices 5, 11) have reduced propagation weight; reserved areas are stateless. Full 12-area geometry used internally; public outputs expose only 10 areas. See `docs/TOPOLOGY_INVARIANTS.md`.

- `runtime/`
  - Execution pipelines.
  - Runtime orchestration.
  - API server.

- `lexicon/`
  - Dictionary systems.
  - Lexical validation tooling.

- `tools/`
  - Developer utilities.
  - Diagnostics.
  - Data generation and operational helpers.

- `assets/`
  - Runtime/static artifacts and data resources.

- `tests/`
  - Pytest unit and integration suites.

- `docs/`
  - Specs.
  - Architecture documentation.
  - Governance rules that remain active documentation.
  - **`docs/HESPERIA_SYSTEM_AWARENESS.md`** — end-to-end system & product awareness for agents (placement engine, projection, GTM, risks). **`docs/research/`** — deep research archive.

- `legacy/`
  - Archived historical code and references.
  - Not part of the active execution stack.

## Knowledge Metrics Engine (KME)

- **Short identifier:** KME. **Module path:** `hesperia.engine.kme`.
- **Purpose:** Deterministic structural knowledge metrics and fingerprints (6 primitives, 35 derived, 41-value fingerprint, domain profile). Integrated into main E2E pipeline.
- **Structure:** `hesperia/engine/kme/` with subpackages `primitives/`, `derived/`, `fingerprint/`, `profiling/`, `validation/`; plus `models`, `extractor`, `loader`, `active_graph`, `bridge`, `pipeline`.
- **Legacy entry point:** `core.domain` re-exports from `hesperia.engine.kme`. Prefer `from hesperia.engine.kme import ...` for new code.

## Active Execution Stack

Treat the following as the active runtime stack:

- `runtime/`
- `core/`
- `lexicon/`

## Legacy Safety Rule

Agents must never modify code under `legacy/` unless explicitly instructed to perform archival maintenance.

## System awareness (further development)

- **`docs/HESPERIA_SYSTEM_AWARENESS.md`** — placement inspector, public projection, evidence/trust, TRIZ/KME; TFP/clinical as domain plug-in.
- **`docs/research/HESPERIA_RAD_DEEP_RESEARCH_2026-03-18.md`** — long-form synthesis.
- **`docs/HESPERIA_*.md`** — repository map, dependency graph, variable catalog, product lines/stack.
- **`docs/specs/README.md`** — spec hub (Ethan dynamics, calibration, Grace triage).
- **Dynamics:** **`PHASE2`–`PHASE4`** (L5/L4/L8) + **`HEX_CAP`**; proceed log `ETHAN-OPEN-WORKFLOW-PROCEED.md`.
- **Calibration:** `docs/specs/HESPERIA_DYNAMICS_CALIBRATION_SPEC_v0_1.md`.
- **Grace triage:** `docs/specs/TRIAGE_TASK_GRACE.md` → output `docs/specs/triage/GRACE_TRIAGE_REPORT.md`.
- **Cursor open workflow (this repo):** `docs/CURSOR_OPEN_WORKFLOW.md` — OPEN queue + proceed order; global orchestrator may live on another host.

## Path/Command Hygiene

- Keep examples and commands aligned to active modules.
- Use `python3 -m runtime.pipeline.run_l1_through_l9` for the L1→L9 pipeline entrypoint.
- Use `python3 -m runtime.semantic_field.run_semantic_field --config … --output …` for **semantic field equations** (see `configs/semantic_field_example.json`, `runtime/semantic_field/README.md`).
- Use `python3 -m runtime.semantic_field.run_field_calibration --config … --output …/run_output_e2e_field_calibration.json` for **HCI parameter grid calibration** (writes `*_best.json`, `*_topk.json`; see `configs/field_calibration_example.json`, `docs/specs/HSPR_CALIBRATION_INDEX_v1.md`).
- Keep pytest references pointed at `tests/`.

## Scope

These rules apply to the full repository rooted at this directory.
