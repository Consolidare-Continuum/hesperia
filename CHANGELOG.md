<!--
HESPERIA — Hesperia Engine Dynamics
Copyright © 2026 igareosh.com — Platonov Igor (aka @igareosh). All rights reserved.
Restricted Research Disclosure License. See LEGAL_NOTICE.md.
-->

# Changelog

All notable releases of **Hesperia Engine Dynamics** are documented here.  
**Master index:** [docs/HESPERIA_v0_5_ENGINE_DYNAMICS.md](docs/HESPERIA_v0_5_ENGINE_DYNAMICS.md)  
**Release tags:** `v0.5.5` · `hesperia-engine-dynamics-v0.5.5` (current modular TFP mainline seal), `v0.5.4` · `hesperia-engine-dynamics-v0.5.4` (previous deterministic system seal), `v0.5.3` · `hesperia-engine-dynamics-v0.5.3` (previous modular seal line), `v0.5.2` · `hesperia-engine-dynamics-v0.5.2` (previous technical release line); historical **`v0.5.1`** / **`v0.5.0`** remain on prior baselines.

### output_views — iteration segment + Kernberg prompt pack (2026-04-07)

- **`iteration_segment_openai_v1`:** JSON Schema at `output_views/schemas/iteration_segment_openai_v1.schema.json`; Python package `output_views/segment/` (`build_session_inspector_v1`, `extract_iteration_segment`, `finalize_segment_openai_v1`, `validate_iteration_segment_openai_v1`).
- **Prompts:** `output_views/prompts/kernberg_iteration_review_system_v1.txt`, `kernberg_iteration_review_user_v1.jinja` (`prompt_pack_id` = `kernberg_iteration_review_v1`).
- **Docs:** [docs/output_views/FIELD_GLOSSARY.md](docs/output_views/FIELD_GLOSSARY.md); fixture `output_views/tests/fixtures/session_inspector_min.json`.
- **Deps:** `jsonschema`, `Jinja2` in `requirements/output_views.txt`.

## v0.5.5 — Modular TFP mainline seal (2026-03-26)

### Scope (v0.5.5)

- Promoted version authority to **0.5.5** across canonical/versioned runtime surfaces.
- Sealed engine/module wiring where calibrated dict version resolution is handled in mainline via `HESPERIA_CALIB_DICT_VERSION`.
- Kept release scope to module/main-engine code only; calibration dict artifacts remain uncommitted.
- **Interim module data mirror:** `hesperia/modules/tfp/data/README.md`, `.gitignore` for mirrored `corpus/` and `dicts/`, and `tools/sync_tfp_module_data.sh` — copies RU/EN cleaned corpus and calibration + `engine_dynamics_v060` bundles from `assets/` plus corpus from `research/_noone_local/` (read-only rsync; does not modify `research/`). Runtime still resolves `assets/` until full pipe wires dict state under module architecture.
- **Dict calibration defaults (pre–full C/CD/HC pipe):** `tools/dict_calibration/env_defaults.py` — `HESPERIA_DICT_CALIB_OFFLINE=1` sets mock OpenAI + worker default 4; `HESPERIA_DICT_CALIB_WORKERS` (default **4**) drives anchor/link/eval/error pools in `run_pipeline.py` and `run_dict_calibration_clearance.py`; `require_openai_key()` is a no-op when `HESPERIA_CALIB_MOCK_OPENAI=1`.
- **B + CD wave after green A:** `tools/run_b_cd_wave_after_a.sh` — validates dict B + TFP RU pack + DLCR regression, runs `test_cd_executor`, then `hesperia.run` with `HESPERIA_CALIB_DICT_VERSION` (default `v0_6_0_clr_v052_2`) and `HESPERIA_CD_ENABLED=1`. Doc: `docs/HESPERIA_TFP_MODULE_DICTS.md` §After A is green.
- **Calibration pack `v0_6_0_clr_v052_2` (DICT-CAL-02):** successor to sealed `v052_1` — **append-only** `dict_b.jsonl` (+66 `concept_id` rows from engine `dict_b_tfp.jsonl`); engine `TFP_CLUSTER_*` **hex_anchor** **HX-2609**–**HX-2615**; default env + CI + `sync_tfp_module_data.sh` updated; `v052_1` directory unchanged.
- **Ethan dict order after A:** `docs/governance/working/ETHAN-DICT-LAYER-ORDER-AFTER-A.md` — locked **B before CD**; `MODEL_CARD_CD_PIPELINE.md` cross-link; anti-pattern CD-before-B recorded.
- **Ethan dict / calibration framework (rev. 2):** `docs/governance/working/ETHAN-10-TASKS-DICTS-CALIB-2026-03-28.md` — tiered **H/S/V/Y** IDs: hard ship gates (H1–H6), structural + control laws (S1–S6: CD mandatory, CD Δ smoke, competition/dominance, length invariance, modifiers, unmapped loop), system (V1–V2: TFP bundle, cross-plane), hygiene (Y1). Mirror: cursor `operational/assignments/`.
- **Ethan seal — freeze `v0_6_0_clr_v052_1`:** `docs/governance/working/ETHAN-DICT-A-NORM-PROPOSE-ANCHOR-LOCK-2026-03-28.md` — Dict A + normalized + proposal/draft + anchored B/links/metrics directory **locked**; mutation only with **igareosh** direct permission or superseding Ethan note; pointers in `HESPERIA_TFP_MODULE_DICTS.md`, `tools/dict_calibration/README.md`.
- **TFP module v1 roundup (2026-03-28):** Scope + env audit + release runbook + schema freeze notes + metric registry gap waiver + boundary review + version pins + product N/A waiver + ops SKIP doc + seal checklist under `docs/governance/TFP_MODULE_V1_*.md` / related; `tfp_module_v1` block in `VERSION.yaml`; seal hook `hesperia/modules/tfp/seal.py` + `HESPERIA_TFP_MODULE_SEALED`; public exports in `hesperia.modules.tfp`; gold tests `tests/test_tfp_module_v1_dlcr_golds.py`; CI path workflow `.github/workflows/tfp-module-v1-paths.yml`; `HESPERIA_SHIPPING_ENV_STRICT` for fail-closed unknown env keys at shipping API startup.
- **TFP-DATA-T04–T20 (2026-03-28):** Module `tfp_v1/` tree + `migrate_research_tfp_to_module_tfp_v1.sh` + `sync_tfp_module_data.sh` (no `research/`); `gen_tfp_v1_manifest.py`; dict calibration corpus guard + default corpus under `tfp_v1/corpus/original/`; `check_research_noone_local_literals.py` in CI; ADR loader doc + provenance policy + closure checklist; `tfp_module_v1.data_layout` in `VERSION.yaml`; `tests/test_tfp_v1_data_layout.py`.
- **TFP-DATA-T07 (provenance mirror):** `tools/copy_dict_calibration_provenance_to_tfp_v1.py` mirrors `outputs/dict_calibration/**` into `tfp_v1/provenance/api/runs/outputs_dict_calibration_mirror/` (gitignored bulk); committed trace `tfp_v1/provenance/api/COPY_MANIFEST_DICT_CALIBRATION.json` after each run.
- **TFP module session corpus:** `research/_noone_local/sessions/` → **`tfp_v1/corpus/sessions/`** — `migrate_research_tfp_to_module_tfp_v1.sh` rsyncs; `noone_sessions_ingest.py` writes module path; `tfp_v1_paths.default_corpus_sessions()`; `gen_tfp_v1_manifest.py` adds `corpus.sessions_md_sha256`; release bundle excludes `tfp_v1/corpus/sessions`.
- **E2E + TFP wiring:** `run_e2e_tfp_smoke` prepends `e2e_primary` from the same `--text` as the rest of E2E; speaker-aware smoke can use that transcript (`speaker_aware_source: e2e_primary`). Added **`hesperia/tfp`** lazy shim (stages from `hesperia.modules.tfp.math_v1`; clinical APIs lazy). **`hesperia.nlp.session_topology`** now exposes `segment_session_text`, `compute_topology_dynamics`, wrapped `analyze_session_segments` / `run_session_topology` for NLP tests.
- **R1–R4 Russian / clinical transcripts:** `tokenize_with_spans()` in `core/attribution/attribution_shared.py` — character spans per token match `tokenize()` when punctuation is stripped inside a word (e.g. `02.38` → `0238`). Fixes `sum(R1 token_count) != total_tokens` and duplicate sentence assignment. Tests: `tests/test_r1_r4_token_spans.py`.
- **Cold recovery layout:** `docs/governance/working/GENA-HESPERIA-APOCALYPTIC-ARCHIVE-TRIAGE-2026-03-28.md` + `tools/mirror_sister_workflows_into_hesperia_data.sh` — mirror sister `workflows` tree into `/data/hesperia/workflows-mirror/` (Grace triage; `WORKFLOWS_SRC` path TBD on host).

### Verify (v0.5.5)

```bash
python3 tools/validate_version_consistency.py
python3 -m pytest tests/test_release_version.py tests/test_tfp_module_main_run.py -q
HESPERIA_CALIB_DICT_VERSION=v0_6_0_clr_v052_2 python3 -m hesperia.run /tmp/hes_in1.txt --config configs/pipeline.yaml --out /tmp/dossier.json --manifest-out /tmp/run_manifest.json
```

## v0.5.4 — Deterministic pipeline system seal (2026-03-26)

### Scope (v0.5.4)

- Replaced linear module execution with phase-aware DAG execution and cycle hard-fail checks.
- Added strict module contracts: factory loading, output schemas, capability/phase requirements, and guarded write/read isolation.
- Added reproducibility system primitives: immutable phase snapshots, deterministic per-phase hashes, version manifest, and run manifest.
- Added system operations entrypoints: `python -m hesperia.run`, `python -m hesperia.batch`, `tools/compare_runs.py`, and determinism/contract test coverage.
- Added aggregation/conflict controls with module weight/priority strategy handling and tolerant/strict failure containment.

### Verify (v0.5.4)

```bash
python3 tools/validate_version_consistency.py
python3 -m pytest tests/test_engine_api_v1.py tests/test_engine_language_contract.py tests/test_determinism.py -q
python3 -m hesperia.test_module tfp
python3 -m hesperia.run /tmp/hes_in1.txt --config configs/pipeline.yaml --out /tmp/dossier.json --manifest-out /tmp/run_manifest.json
```

## v0.5.3 — Sealed modular TFP onboard release (2026-03-26)

### Scope (v0.5.3)

- Version authority bumped to **0.5.3** (`VERSION.yaml`, `hesperia/VERSION.yaml`, `pyproject.toml`, runtime version outputs).
- Added module execution kernel `hesperia.engine.core.HesperiaEngine` with config-driven module loading.
- Added first-class `tfp.v1` module in `hesperia/modules/tfp/` with copied TFP math from `.research` into module-local `math_v1.py`.
- Main runtime now supports module-based one-line load through `configs/pipeline.yaml`.

### Verify (v0.5.3)

```bash
python3 tools/validate_version_consistency.py
python3 -m runtime.pipeline.run_e2e_all
python3 -m runtime.pipeline.run_e2e_full_stack
```

## v0.5.2 — Technical terminology propagation release (2026-03-26)

### Scope

- Version authority bumped to **0.5.2** (`VERSION.yaml`, `hesperia/VERSION.yaml`, `pyproject.toml`, runtime version outputs).
- Canonical naming propagation continued across runtime/core/docs with compatibility mirrors preserved.
- Dedicated release audit entrypoint added: `tools/release/build_release_audit_v0_5_2.py`.

### Verify (v0.5.2)

```bash
python3 tools/validate_version_consistency.py
python3 -m runtime.pipeline.run_e2e_product
python3 tools/release/build_release_audit_v0_5_2.py --quick
```

## v0.5.1 — Governed enforcement baseline (2026-03-19)

**Not a feature release.** First line where **architecture, boundaries, and product-path behavior** are enforced by automated gates (CI + tests + audit bundle), not by convention alone.

### Structural

- **Quarantine / layout:** `legacy/assets/data/{v040,v0413,v0414}`; active bundle `assets/data/engine_dynamics_v050/`; `legacy/docs/{specs_history,refactor_notes}`; research reports → `research/reports/`; governance memos → `docs/governance/{working,project}/`.
- **Optional / experimental paths:** TRIZ under `benchmarks|examples|deploy/extensions/`; clinical tests under `tests/experimental/clinical_tfp/` + fixtures `tests/fixtures/clinical_tfp/`; code remains `research/clinical_tfp/`.
- **Maps / policy:** `repo_refresh_manifest.yaml`, `ACTIVE_STACK_MAP`, `REPO_LIFECYCLE_MAP`, `PATH_OWNERSHIP_MATRIX`, `REPO_STRUCTURE_POLICY.md`, `EXTENSION_STATUS.yaml`, `GENERATED_ARTIFACT_POLICY.md`.
- **Spec tree (Tasks 2–3):** normative `specs/` hierarchy (`CANONICAL_INDEX`, `specs/core/*`, `specs/canon/*` redirects, `schemas/public/public_output_schema.json`).

### Enforcement

- **Runtime spine doc + CI:** `docs/RUNTIME_EXECUTION_SPINE_v0_5_0.md`; import graphs `docs/IMPORT_GRAPH_v0_5_0.md`, `docs/IMPORT_GRAPH_ENGINE_v0_5_0.md` with `tools/gen_import_graph_doc.py` diff in GitHub Actions.
- **Forbidden zones:** `tools/check_forbidden_zone_imports.py` (no `research`/`legacy` in strict trees).
- **Shipping surface:** `runtime/shipping/shipping_import_allowlist.yaml`, `tools/validate_shipping_surface.py`, `tools/audit_shipping_allowlist.py` (strict unused + prefix creep cap), byte lock in `tests/test_tool_contracts_locked.py`.
- **Spine exclusivity:** `tests/test_runtime_spine_integrity.py` — `run_sealed_multiscale_stack` via bridge, `apply_public_projection`, **no** `sphere.execution_flow.run_pipeline` on the canonical product path; bridge wiring + `inspect.signature` locks.
- **Engine projection rule:** `tools/check_engine_projection_boundary.py` — `core.projection` only under `hesperia/engine/projection/`.
- **Sealing scan:** `tools/sealing_scan.py` skips versioned audit trees `release/v0.5.0`, `release/v0.5.1`.

### Stability

- **Public schema drift:** `schemas/public_api_v0_5_1.snapshot.json` (byte-identical to canonical `schemas/public/public_output_schema.json` for this seal — **no normative schema change** vs v0.5.0), `tools/verify_public_api_snapshot.py`.
- **Semantic / magnitude contract:** `tests/test_semantic_output_signature.py`, `tests/support/public_output_contract.py` (contrasting inputs + bounds).
- **Dead weight:** `docs/DEAD_WEIGHT_BASELINE.txt` with `MAX_UNREFERENCED`, `RECORDED_COUNT`, `MAX_INCREASE_FROM_RECORDED`; `tools/check_dead_weight_budget.py`.
- **Anti test-weakening:** `tests/test_guard_invariants_locked.py`, `tests/test_tool_contracts_locked.py`.
- **Sealed-runtime corpus:** `tests/test_sealed_runtime_regression.py` — forbidden-term scan uses **word-boundary** rules for `sphere` / `hex` / `bridge` so approved tokens such as `hex_microcell` do not false-positive.

### Seal / artifacts

- **Audit tree:** `release/v0.5.1/` — regenerate with `python3 tools/release/build_release_audit_v0_5_1.py` (full pytest, determinism triplicate, system seal, schema validation). **`BUILD_PROVENANCE.json`** records builder metadata.
- **Version authority:** `VERSION.yaml` · `pyproject.toml` · `hesperia.__version__` · `hesperia.engine.release_meta` · `runtime/shipping/version_info.py` · API version strings → **0.5.1** (lockstep).

### Product E2E (justified delta)

- **`python3 -m runtime.pipeline.run_e2e_product`** output updates **`assets/artifacts/e2e/run_output_e2e_product_surface.json`**: envelope fields (`system_version`, `build_id`) now reflect **0.5.1** and the seal timestamp policy — **payload shape and schema version unchanged** (same `schemas/public/public_output_schema.json`).

### Verify (v0.5.1)

```bash
python3 tools/validate_version_consistency.py
python3 -m runtime.pipeline.run_e2e_product
python3 tools/verify_public_api_snapshot.py
python3 tools/release/build_release_audit_v0_5_1.py
```

## v0.5.0 — Canonical Dynamics Release (2026-03-18)

**Product line:** Hesperia Engine Dynamics — sealed multiscale semantic physics (concept → hex → family → area → product signals → HSPR).

### Shipped

- **Hex layer:** microphysics (`hex_dynamics`), hex→family bridge (`hex_family_bridge`), `hex_outputs/`, calibration weights `data/topology/hex_family_weights.json`.
- **Sealed stack:** `hesperia.engine.sealed_multiscale_stack` — deterministic one-shot chain to family/area activations, product signals, **HSPR** system scalar.
- **Observables / product signals:** `observables.py`, `product_signals.py`, `hspr_index.py`; specs under `specs/canon/*.md`.
- **E2E:** `run_e2e_all` produces **19** baseline JSON artifacts (+ **20th** with `HESPERIA_FIELD_DYNAMICS=1`). See [docs/E2E_RUN_ORDER.md](docs/E2E_RUN_ORDER.md), [assets/artifacts/e2e/E2E_OUTPUTS.md](assets/artifacts/e2e/E2E_OUTPUTS.md).

### Explicitly not the v0.5 product definition

- **TFP testing grounds** (`assets/testing/tfp_kernberg/`, TFP-heavy E2E steps) — CI / regression collateral, not canonical Engine Dynamics spec core.
- **legacy/** — archival only.

### Sealed shipping build (2026-03-18)

- `./build_shipping.sh all` — Docker API image + `release/manifest.json` + checksums.
- `./tools/run_release_gate.sh` — **HESPERIA SEALED RUNTIME: PASS**
- Record: [release/RELEASE_v0.5.0_BUILD.md](release/RELEASE_v0.5.0_BUILD.md)

### Verify (v0.5.0)

```bash
python3 -m runtime.pipeline.run_e2e_all
pytest tests/test_e2e_flows.py -v
```

### Repo layout (hygiene)

- Example JSON configs → **`runtime/configs/`** (was root `configs/`).
- Python requirements → **`requirements/*.txt`**; root **`requirements.txt`** includes `runtime.txt`.
- *(Superseded by 2026-03-19 refresh: reports → **`research/reports/`**, stub → **`docs/research/README.md`**, scratch → **`research/reports/_noone_local/`**.)* Previously: **`docs/research/`** for deep-research; **`VERSION_POLICY.md`** → **`docs/VERSION_POLICY.md`**.

### Version surfaces

- **`pyproject.toml`** — `[project].version` = `0.5.0` (provenance via `runtime.provenance`).
- **`hesperia.__version__`**, **`hesperia.engine.release_meta`**, API OpenAPI **`0.5.0`**, shipping **`version_info.py`** (overwritten on sealed build).

### Documentation

- Release narrative: [specs/release/HESPERIA_v0_5_ENGINE_DYNAMICS_RELEASE.md](specs/release/HESPERIA_v0_5_ENGINE_DYNAMICS_RELEASE.md)
- Canonical naming: [docs/ENGINE_DYNAMICS_CANONICAL_NAMING_v0.5.md](docs/ENGINE_DYNAMICS_CANONICAL_NAMING_v0.5.md)

---

*Prior history: see `docs/archive/` and legacy release notes.*
