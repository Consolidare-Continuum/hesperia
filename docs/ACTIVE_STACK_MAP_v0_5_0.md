<!--
HESPERIA — Reference Architecture Definition (RAD)
-->

# Active stack map (v0.5.0 baseline · v0.5.1 repo refresh)

Single-page map of **what runs**, **what ships**, and **what is intentionally out of the product spine**.

## Entrypoints

| Purpose | Command / module |
|--------|-------------------|
| L1→L9 pipeline | `python3 -m runtime.pipeline.run_l1_through_l9` |
| Full internal E2E | `python3 -m runtime.pipeline.run_e2e_all` |
| Product E2E | `python3 -m runtime.pipeline.run_e2e_product` |
| Full stack (manifest + seal hooks) | `python3 -m runtime.pipeline.run_e2e_full_stack` |
| Shipping CLI | `python3 -m runtime.shipping.cli_main` (see `pyproject.toml` `[project.scripts]`) |

## Execution spine (runtime-critical)

- **`core/`** — layers, topology, math, propagation.
- **`hesperia/`** — KME, engine, projection, extensions (`hesperia.extensions.dynamics`, `hesperia.extensions.triz`).
- **`runtime/`** — pipelines, services, shipping API, semantic field runners.
- **`sphere/`** — structural / USF / internal graph helpers (not public marketing vocabulary).
- **`lexicon/`** — dictionaries and build-time lexical artifacts.
- **`schemas/`** — shared schema files consumed by tooling and runtime.

## Public / product surface

- Projection gate: `hesperia.engine.projection` — see `docs/PUBLIC_PRODUCT_SURFACE.md`.
- Capabilities: `hesperia/system/capabilities.yaml`, `hesperia.system.capabilities`.

## Binding specs (normative)

- Repo root **`specs/`** (with **`spec/`** → `specs/canon` symlink).
- **`docs/specs/`** — triage and workflow only; governance task notes live under **`docs/governance/working/`** and **`docs/governance/project/`**.

## Excluded / non-spine trees

| Tree | Role |
|------|------|
| **`research/`** | Experiments, prototypes, **`research/reports/`** long-form writeups. |
| **`legacy/`** | Historical code (`legacy/deprecated/`, `legacy/sphere_rag/`, …), **`legacy/assets/data/`** frozen dumps, **`legacy/docs/specs_history`**, refactor notes. |
| **`tests/experimental/`** | Clinical/TFP and other non-product test harnesses. |
| **`outputs/`**, **`tmp/`** | Generated / local only (`GENERATED_ARTIFACT_POLICY.md`). |

## Current vs historical data bundles

- **Active:** `assets/data/` — domain constants, operational bundles (e.g. `engine_dynamics_v050/`).
- **Historical:** `legacy/assets/data/v040|v0413|v0414/`.

## Optional TRIZ extension layout

- Corpora: `benchmarks/extensions/triz/`
- Demo scripts: `examples/extensions/triz_demo/`
- MVP deploy: `deploy/extensions/triz_mvp/`
- CLIs: `tools/triz/`

See also **`repo_refresh_manifest.yaml`**, **`docs/REPO_LIFECYCLE_MAP.md`**, **`docs/PATH_OWNERSHIP_MATRIX.md`**, **`docs/RUNTIME_EXECUTION_SPINE_v0_5_0.md`**, **`docs/IMPORT_GRAPH_v0_5_0.md`**, **`docs/IMPORT_GRAPH_ENGINE_v0_5_0.md`**, **`docs/VERSIONING_GATE_v0_5_1.md`**, **`schemas/public_api_v0_5_1.snapshot.json`**, **`tools/check_forbidden_zone_imports.py`**, **`tools/validate_shipping_surface.py`**, **`tests/test_runtime_spine_integrity.py`**, **`tests/test_semantic_output_signature.py`**.
