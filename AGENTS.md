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
  - **Topology (10+2):** 10 operational areas (240 families, 60k hexes); 2 reserved service areas (48 families, 12k hexes). Reserved areas are stateless; full 12-area geometry used internally; public outputs expose only 10 areas. See `docs/TOPOLOGY_INVARIANTS.md`.

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

## Path/Command Hygiene

- Keep examples and commands aligned to active modules.
- Use `python3 -m runtime.pipeline.run_l1_through_l9` for the L1→L9 pipeline entrypoint.
- Keep pytest references pointed at `tests/`.

## Scope

These rules apply to the full repository rooted at this directory.
