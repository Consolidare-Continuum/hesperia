<!--
HESPERIA — Hesperia Engine Dynamics
Copyright © 2026 igareosh.com — Platonov Igor (aka @igareosh). All rights reserved.
Restricted Research Disclosure License. See LEGAL_NOTICE.md.
-->

# Changelog

All notable releases of **Hesperia Engine Dynamics** are documented here.  
**Master index:** [docs/HESPERIA_v0_5_ENGINE_DYNAMICS.md](docs/HESPERIA_v0_5_ENGINE_DYNAMICS.md)  
**Release tags:** `v0.5.0` · `hesperia-engine-dynamics-v0.5.0` (same commit; use product tag for GitHub Release name).

## Unreleased — Task 3 (spec hierarchy)

- **Tier-1 index:** `specs/CANONICAL_INDEX.md` · **inventory:** `specs/INVENTORY.md` · **governance:** `specs/system/versioning_and_governance.md`.
- **Core specs:** `specs/core/{system_architecture,hex_microphysics_canon,family_aggregation,area_aggregation,product_observables}.md`.
- **Single dynamics file:** `specs/dynamics/semantic_field_dynamics.md` (former `SEMANTIC_FIELD_EQUATIONS_v1` prose merged); redirect stub kept at `SEMANTIC_FIELD_EQUATIONS_v1.md`.
- **Calibration / HSPR / TRIZ / schema:** `specs/calibration/*`, `specs/triz/*`, `specs/schema/public_output_schema.md`.
- **`specs/canon/*.md` math files** → redirects to `core/` / `calibration/` (YAML assets unchanged).

## Unreleased — Task 2 (repo topology)

- **Clinical/TFP:** `hesperia/clinical/` → **`research/clinical_tfp/`** (experimental; import `research.clinical_tfp`).
- **Extensions:** `hesperia/engine/field_dynamics` → **`hesperia/extensions/dynamics`**; `hesperia/engine/triz` → **`hesperia/extensions/triz`**.
- **Specs:** normative tree under **`specs/`** (`canon/`, `dynamics/`, `release/`, `schemas/`, `calibration/`); **`spec/README.md`** redirects from old `spec/`.
- **Schemas:** **`schemas/public/public_output_schema.json`** (symlink at `assets/public/`).
- **Examples:** **`demo/`** → **`examples/triz_demo/`**; **`outputs/`** for local generated runs (gitignored).
- **Policy:** `REPO_STRUCTURE_POLICY.md`, `EXTENSION_STATUS.yaml`, `GENERATED_ARTIFACT_POLICY.md`.

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

### Verify

```bash
python3 -m runtime.pipeline.run_e2e_all
pytest tests/test_e2e_flows.py -v
```

### Repo layout (hygiene)

- Example JSON configs → **`runtime/configs/`** (was root `configs/`).
- Python requirements → **`requirements/*.txt`**; root **`requirements.txt`** includes `runtime.txt`.
- **`docs/research/`** — deep-research report from root; **`VERSION_POLICY.md`** → **`docs/VERSION_POLICY.md`**.
- Local scratch → **`docs/research/_noone_local/`** (gitignored; former root `noone/`).

### Version surfaces

- **`pyproject.toml`** — `[project].version` = `0.5.0` (provenance via `runtime.provenance`).
- **`hesperia.__version__`**, **`hesperia.engine.release_meta`**, API OpenAPI **`0.5.0`**, shipping **`version_info.py`** (overwritten on sealed build).

### Documentation

- Release narrative: [specs/release/HESPERIA_v0_5_ENGINE_DYNAMICS_RELEASE.md](specs/release/HESPERIA_v0_5_ENGINE_DYNAMICS_RELEASE.md)
- Canonical naming: [docs/ENGINE_DYNAMICS_CANONICAL_NAMING_v0.5.md](docs/ENGINE_DYNAMICS_CANONICAL_NAMING_v0.5.md)

---

*Prior history: see `docs/archive/` and legacy release notes.*
