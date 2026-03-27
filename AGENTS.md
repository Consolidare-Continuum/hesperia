<!--
HESPERIA — Reference Architecture Definition (RAD)
Copyright © 2026 igareosh.com — Platonov Igor (aka @igareosh). All rights reserved.
Restricted Research Disclosure License. Inspection and reference only.
No reproduction, redistribution, or use without explicit written permission.
See LEGAL_NOTICE.md for full terms.
-->

# AGENT GUIDELINES — HESPERIA **Engine Dynamics v0.5.1** (governed enforcement baseline)

This repository is the **Hesperia Engine Dynamics** codebase — **Canonical sealed line v0.5.1** (concept → hex → family → area → signals → HSPR): architecture, boundaries, and product-path behavior are enforced by CI, integrity tests, and `release/v0.5.1/` (see `CHANGELOG.md`). Historical payloads and read-only archives live under `legacy/` (`repo_refresh_manifest.yaml`). Prior frozen baseline: **`release/v0.5.0/`** (do not overwrite). Align with the current top-level layout; avoid legacy-era roots as active architecture.

## Canonical Top-Level Structure

**Active spine** (small and obvious):

- `core/` — deterministic computation layers (L1–L9), topology, propagation
- `hesperia/` — engine (including `hesperia.engine.kme` — Knowledge Metrics Engine)
- `runtime/` — execution flows, orchestration, API
- `sphere/` — structural / USF / prolog-adjacent compute (internal; not public product vocabulary)
- `lexicon/` — dictionary systems and lexical tooling
- `schemas/` — JSON/schema artifacts consumed by runtime and tooling
- `specs/` — **binding** specifications (canon, dynamics, release narratives)
- `tests/` — active engine and product tests (`tests/experimental/` = non-product experimental)
- `tools/` — developer utilities and diagnostics
- `assets/` — **current** runtime/static inputs (historical version dumps under `legacy/assets/data/`)
- `release/` — sealed release bundles (**current:** `release/v0.5.1/`; historical: `release/v0.5.0/`)
- `docs/` — architecture, operator docs, **`docs/governance/`** policy set
- `examples/` — only supported, runnable examples (optional TRIZ under `examples/extensions/`)
- `deploy/` — current deployment paths (optional TRIZ MVP under `deploy/extensions/`)

**Clearly separated:**

- `research/` — non-product experiments and long-form reports (`research/reports/`)
- `legacy/` — historical code, frozen data, specs history, refactor notes — **not** the active execution stack
- `outputs/`, `tmp/` — local/generated (see `GENERATED_ARTIFACT_POLICY.md`)

Do not use or reintroduce old roots such as `sphere_rag/`, `hesperia_lex/`, `scripts/`, `api/`, top-level `governance/`, or `project/` as active top-level architecture.

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
  - **`docs/HESPERIA_SYSTEM_AWARENESS.md`** — end-to-end system & product awareness for agents (placement engine, projection, GTM, risks). Deep research archive: **`research/reports/`** (see `docs/research/README.md` redirect).

- `legacy/`
  - Archived historical code and references.
  - Not part of the active execution stack.

## Knowledge Metrics Engine (KME)

- **Short identifier:** KME. **Component path:** `hesperia.engine.kme`.
- **Purpose:** Deterministic structural knowledge metrics and fingerprints (6 primitives, 35 derived, 41-value fingerprint, domain profile). Integrated into main E2E execution_flow.
- **Structure:** `hesperia/engine/kme/` with subpackages `primitives/`, `derived/`, `fingerprint/`, `profiling/`, `validation/`; plus `models`, `extractor`, `loader`, `active_graph`, `bridge`, `execution_flow`.
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
- **`CHANGELOG.md`** — **v0.5.1** seal notes + **v0.5.0** history; verify commands per release section.
- **`repo_refresh_manifest.yaml`** — machine-readable active / optional / research / legacy path contract.
- **`docs/ACTIVE_STACK_MAP_v0_5_0.md`** — one-page spine, entrypoints, excluded trees.
- **`docs/RUNTIME_EXECUTION_SPINE_v0_5_0.md`** — product vs E2E execution map (exact modules / call order).
- **`docs/IMPORT_GRAPH_v0_5_0.md`** — static imports from public `runtime/*` + `runtime/services` (regenerate: `python3 tools/gen_import_graph_doc.py --write`; CI diff).
- **`docs/IMPORT_GRAPH_ENGINE_v0_5_0.md`** — static imports from `hesperia/engine/` (regenerate: `python3 tools/gen_import_graph_doc.py --write --profile engine`; CI diff).
- **`runtime/shipping/shipping_import_allowlist.yaml`** + **`tools/validate_shipping_surface.py`** — explicit allowlist for `runtime/shipping` imports.
- **`tools/check_forbidden_zone_imports.py`** — blocks `research.*` / `legacy.*` in `runtime/services`, `runtime/shipping`, `runtime/api`, `hesperia/engine`, and `runtime/execution_flow` except `run_e2e_all.py`.
- **`schemas/public_api_v0_5_1.snapshot.json`** — byte-identical freeze of `schemas/public/public_output_schema.json` for the v0.5.1 line (`tools/verify_public_api_snapshot.py`). Historical: `schemas/public_api_v0_5_0.snapshot.json`.
- **`docs/VERSIONING_GATE_v0_5_1.md`** — structural vs behavioral gate (fulfilled by the v0.5.1 seal).
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
- **Product E2E:** `python3 -m runtime.pipeline.run_e2e_product` — minimal raw_text → projection → schema check (full internal E2E remains `run_e2e_all`).

## Release seal (Task 5 — v0.5.1 current · v0.5.0 frozen)

- **`release/v0.5.1/`** — **current** full audit package: `README.md`, `manifest.json`, `build_info.json`, `BUILD_PROVENANCE.json`, `checksums.txt`, `capabilities.yaml`, `specs_index.json`, `test_report.json`, **`audit_report.json`**, **`determinism_report.json`**, **`schema_validation_report.json`**, **`system_seal.json`**, `e2e_reference_output.json`, `schema.json`, **`final_gate_status.json`** (`sealed`, `critical_checks` including **`system_seal`**).
- **`release/v0.5.0/`** — **historical** frozen baseline (unchanged after v0.5.1 tag).
- **Canonical raw_text fixture:** `tests/fixtures/release_v0_5_0/canonical_input.txt`.
- **Builder (v0.5.1):** `python3 tools/release/build_release_audit_v0_5_1.py` (exit **0** only if all gates pass, including **clean git**). Set `HESPERIA_RELEASE_BUILD_TIMESTAMP` for bitwise-stable `e2e_reference_output.json`.
- **Builder (v0.5.0, historical):** `python3 tools/release/build_release_audit_v0_5_0.py` — do not re-run to mutate the frozen tree.
- **Tag:** `git tag -a v0.5.1 -m "…"` only when `release/v0.5.1/audit_report.json` → `seal_decision.may_tag_v0_5_1` is **true** (automation does not tag).
- **Task 6 execution order:** `docs/CODEX_EXECUTION_CHECKLIST_v0_5_0_SEAL.md` (same discipline; v0.5.1 uses the v0.5.1 builder above).
- **System seal (Task 11):** `python3 -m tools.system_seal.run_system_seal` — writes `release/v{VERSION.yaml system_version}/system_seal.json` (e.g. `v0.5.1`). Optional API: `HESPERIA_REQUIRE_SYSTEM_SEAL=1` on shipping app startup.
- **Task integration map:** `docs/ENGINE_TASKS_1_11_INTEGRATION.md` — one table: tasks → code → seal keys.

## System awareness (further development)

- **`docs/HESPERIA_SYSTEM_AWARENESS.md`** — placement inspector, public projection, evidence/trust, TRIZ/KME; TFP/clinical as domain plug-in.
- **`research/reports/HESPERIA_RAD_DEEP_RESEARCH_2026-03-18.md`** — long-form synthesis.
- **`docs/HESPERIA_*.md`** — repository map, dependency graph, variable catalog, product lines/stack.
- **`docs/specs/README.md`** — spec hub (Ethan dynamics, calibration, Grace triage).
- **Dynamics:** **`PHASE2`–`PHASE4`** (L5/L4/L8) + **`HEX_CAP`**; proceed log `docs/governance/working/ETHAN-OPEN-WORKFLOW-PROCEED.md`.
- **Calibration:** `specs/dynamics/HESPERIA_DYNAMICS_CALIBRATION_SPEC_v0_1.md`.
- **Grace triage:** `docs/specs/TRIAGE_TASK_GRACE.md` → output `docs/specs/triage/GRACE_TRIAGE_REPORT.md`.
- **Cursor open workflow (this repo):** `docs/CURSOR_OPEN_WORKFLOW.md` — OPEN queue + proceed order; global orchestrator may live on another host.

## Release version

- **Engine Dynamics v0.5.1:** `pyproject.toml` → `version`; `hesperia.__version__` (from `VERSION.yaml`); shipping **`runtime/shipping/version_info.py`** aligned at seal. **Current** audit bundle: **`release/v0.5.1/`**. **Historical:** `release/v0.5.0/`.

## Pre-push and GitHub sync (Cursor)

- **`docs/CURSOR_REPO_AND_RELEASE_BEST_PRACTICES.md`** — validators, tests, release audit before `git push`; what to commit vs ignore.
- **Seal order:** **`docs/CODEX_EXECUTION_CHECKLIST_v0_5_0_SEAL.md`**.
- **Contributor entry:** **`CONTRIBUTING.md`** (links to the above).

## Path/Command Hygiene

- Keep examples and commands aligned to active modules.
- Use `python3 -m runtime.pipeline.run_l1_through_l9` for the L1→L9 execution flow entrypoint.
- Use `python3 -m runtime.pipeline.run_e2e_full_stack` for the **single encompassing E2E** (all `run_e2e_all` outputs + product surface + physics validation + system seal + manifest); `docs/E2E_RUN_ORDER.md`.
- Use `python3 -m runtime.semantic_field.run_semantic_field --config … --output …` for **semantic field equations** (see `runtime/configs/semantic_field_example.json`, `runtime/semantic_field/README.md`).
- Use `python3 -m runtime.semantic_field.run_field_calibration --config … --output …/run_output_e2e_field_calibration.json` for **HCI parameter grid calibration** (writes `*_best.json`, `*_topk.json`; see `runtime/configs/field_calibration_example.json`, `specs/dynamics/HSPR_CALIBRATION_INDEX_v1.md`).
- Keep pytest references pointed at `tests/`.
- Drift / mass control: `python3 tools/verify_public_api_snapshot.py`; `python3 tools/gen_import_graph_doc.py | diff -q docs/IMPORT_GRAPH_v0_5_0.md -`; `python3 tools/gen_import_graph_doc.py --profile engine | diff -q docs/IMPORT_GRAPH_ENGINE_v0_5_0.md -`; `python3 tools/check_forbidden_zone_imports.py`; `python3 tools/validate_shipping_surface.py`; `python3 tools/find_unreferenced_files.py` (heuristic).
- Spine / behavior: `pytest tests/test_runtime_spine_integrity.py tests/test_semantic_output_signature.py`.

## Scope

These rules apply to the full repository rooted at this directory.
