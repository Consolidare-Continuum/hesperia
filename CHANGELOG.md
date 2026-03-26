<!--
HESPERIA — Hesperia Engine Dynamics
Copyright © 2026 igareosh.com — Platonov Igor (aka @igareosh). All rights reserved.
Restricted Research Disclosure License. See LEGAL_NOTICE.md.
-->

# Changelog

All notable releases of **Hesperia Engine Dynamics** are documented here.  
**Master index:** [docs/HESPERIA_v0_5_ENGINE_DYNAMICS.md](docs/HESPERIA_v0_5_ENGINE_DYNAMICS.md)  
**Release tags:** `v0.5.2` · `hesperia-engine-dynamics-v0.5.2` (current technical release line), `v0.5.1` · `hesperia-engine-dynamics-v0.5.1` (previous seal); historical **`v0.5.0`** / **`hesperia-engine-dynamics-v0.5.0`** remain on the prior baseline commit.

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
