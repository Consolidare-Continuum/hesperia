<!--
HESPERIA — Reference Architecture Definition (RAD)
Copyright © 2026 igareosh.com — Platonov Igor (aka @igareosh). All rights reserved.
Restricted Research Disclosure License. Inspection and reference only.
No reproduction, redistribution, or use without explicit written permission.
See LEGAL_NOTICE.md for full terms.
-->

# AGENT GUIDELINES — HESPERIA **Engine Dynamics v0.5** (Canonical Release)

This repository is the **Hesperia Engine Dynamics** codebase — **Canonical Release v0.5**: sealed multiscale semantic physics (concept → hex → family → area → signals → HSPR), deterministic E2E proof. Versioned tools/calibration archived under `legacy/deprecated/` where noted. Align with the current top-level layout; avoid legacy-era roots as active architecture.

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

## Engine Dynamics v0.5 — documentation hub

- **`docs/HESPERIA_v0_5_ENGINE_DYNAMICS.md`** — **master index**: spec ↔ engine ↔ E2E; TFP testing grounds **out** of canonical release (§2).
- **`specs/release/HESPERIA_v0_5_ENGINE_DYNAMICS_RELEASE.md`** — canonical release narrative.
- **`CHANGELOG.md`** — **v0.5.0** closure notes and verify commands.
- **`docs/ENGINE_DYNAMICS_CANONICAL_NAMING_v0.5.md`** — vocabulary: multiscale chain, modules, E2E counts.
- **`specs/CANONICAL_INDEX.md`** — **Tier-1 binding spec index** (Task 3).
- **`specs/canon/README.md`** — loader hub + redirects (`spec/` symlink).
- **`spec/`** — symlink to **`specs/canon/`** (compat for loaders/tests that still use the `spec/` path).

## Repository topology (Task 2 — shape & boundaries)

- **`REPO_STRUCTURE_POLICY.md`** — what each top-level tree is for; what is forbidden there.
- **`EXTENSION_STATUS.yaml`** — extension registry (`dynamics`, `triz`, `clinical_tfp`).
- **`GENERATED_ARTIFACT_POLICY.md`** — generated output location (`outputs/` vs reviewed `assets/`).
- **Extensions (Python):** `hesperia.extensions.dynamics`, `hesperia.extensions.triz`.
- **Experimental TFP/clinical:** `research.clinical_tfp` — **not** baseline product engine surface.

## Product boundary (Task 4 — runtime surface)

- **`docs/PUBLIC_PRODUCT_SURFACE.md`** — internal vs projection vs public; HTTP/CLI; capabilities; E2E split.
- **Projection gate:** `hesperia.engine.projection.project_to_public` — product paths must not bypass it (see `runtime.services.analysis_service`, `runtime.artifact_writer`).
- **Capabilities:** `hesperia/system/capabilities.yaml` + `hesperia.system.capabilities` (env: `HESPERIA_PRODUCT_SURFACE`, `HESPERIA_EXPOSE_TRIZ`, `HESPERIA_EXPOSE_VERSION`).
- **Product E2E:** `python3 -m runtime.pipeline.run_e2e_product` — minimal input → projection → schema check (full internal E2E remains `run_e2e_all`).

## Release seal (Task 5 — v0.5.0 baseline)

- **`release/v0.5.0/`** — full audit package: `README.md`, `manifest.json`, `build_info.json`, `checksums.txt`, `capabilities.yaml`, `specs_index.json`, `test_report.json`, **`audit_report.json`**, **`determinism_report.json`**, **`schema_validation_report.json`**, `e2e_reference_output.json`, `schema.json`.
- **Canonical input fixture:** `tests/fixtures/release_v0_5_0/canonical_input.txt`.
- **Builder:** `python3 tools/release/build_release_audit_v0_5_0.py` (exit **0** only if all gates pass, including **clean git**). Set `HESPERIA_RELEASE_BUILD_TIMESTAMP` for bitwise-stable `e2e_reference_output.json`.
- **Tag:** `git tag -a v0.5.0 -m "…"` only when `audit_report.json` → `seal_decision.may_tag_v0_5_0` is **true** (automation does not tag).
- **Task 6 execution order:** `docs/CODEX_EXECUTION_CHECKLIST_v0_5_0_SEAL.md` (Phase 0 inventory: `tools/seal_phase0_inventory.py`; validators: `tools/validate_version_consistency.py`, `tools/audit_public_surface.py`, `tools/build_specs_index.py`, `tools/doc_authority_scan.py`).
- **Final gate file:** `release/v0.5.0/final_gate_status.json` (`sealed`, `critical_checks`).

## System awareness (further development)

- **`docs/HESPERIA_SYSTEM_AWARENESS.md`** — placement inspector, public projection, evidence/trust, TRIZ/KME; TFP/clinical as domain plug-in.
- **`docs/research/HESPERIA_RAD_DEEP_RESEARCH_2026-03-18.md`** — long-form synthesis.
- **`docs/HESPERIA_*.md`** — repository map, dependency graph, variable catalog, product lines/stack.
- **`docs/specs/README.md`** — spec hub (Ethan dynamics, calibration, Grace triage).
- **Dynamics:** **`PHASE2`–`PHASE4`** (L5/L4/L8) + **`HEX_CAP`**; proceed log `ETHAN-OPEN-WORKFLOW-PROCEED.md`.
- **Calibration:** `specs/dynamics/HESPERIA_DYNAMICS_CALIBRATION_SPEC_v0_1.md`.
- **Grace triage:** `docs/specs/TRIAGE_TASK_GRACE.md` → output `docs/specs/triage/GRACE_TRIAGE_REPORT.md`.
- **Cursor open workflow (this repo):** `docs/CURSOR_OPEN_WORKFLOW.md` — OPEN queue + proceed order; global orchestrator may live on another host.

## Release version

- **Engine Dynamics v0.5.0:** `pyproject.toml` → `version`; `hesperia.__version__`; sealed builds refresh `runtime/shipping/version_info.py`.

## Pre-push and GitHub sync (Cursor)

- **`docs/CURSOR_REPO_AND_RELEASE_BEST_PRACTICES.md`** — validators, tests, release audit before `git push`; what to commit vs ignore.
- **Seal order:** **`docs/CODEX_EXECUTION_CHECKLIST_v0_5_0_SEAL.md`**.
- **Contributor entry:** **`CONTRIBUTING.md`** (links to the above).

## Path/Command Hygiene

- Keep examples and commands aligned to active modules.
- Use `python3 -m runtime.pipeline.run_l1_through_l9` for the L1→L9 pipeline entrypoint.
- Use `python3 -m runtime.semantic_field.run_semantic_field --config … --output …` for **semantic field equations** (see `runtime/configs/semantic_field_example.json`, `runtime/semantic_field/README.md`).
- Use `python3 -m runtime.semantic_field.run_field_calibration --config … --output …/run_output_e2e_field_calibration.json` for **HCI parameter grid calibration** (writes `*_best.json`, `*_topk.json`; see `runtime/configs/field_calibration_example.json`, `specs/dynamics/HSPR_CALIBRATION_INDEX_v1.md`).
- Keep pytest references pointed at `tests/`.

## Scope

These rules apply to the full repository rooted at this directory.
