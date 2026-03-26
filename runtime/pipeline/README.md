<!--
HESPERIA — Reference Architecture Definition (RAD)
Copyright © 2026 igareosh.com — Platonov Igor (aka @igareosh). All rights reserved.
Restricted Research Disclosure License. Inspection and reference only.
No reproduction, redistribution, or use without explicit written permission.
See LEGAL_NOTICE.md for full terms.
-->

# runtime/pipeline — Execution flow helpers & E2E

**Canonical structural path:** `runtime.services.analysis_service.run_structural_analysis` →
`hesperia.engine.sealed_multiscale_stack.run_sealed_multiscale_stack` → `hesperia.engine.projection.project_to_public`.

**Reference CLI:** `python3 -m runtime.runners.run_reference_pipeline` (wraps `run_structural_analysis` execution flow).

Legacy `sphere.pipeline.run_pipeline` is **dev/test only** (`HESPERIA_SPHERE_PIPELINE_DEV=1`); do not use for shipping runtime.

## Entrypoints

- **run_l1_through_l9.py** — `run_pipeline_for_text()` calls `run_structural_analysis(..., stages="full")` and tags `run` as `L1_through_L9` for E2E contracts.
- **run_sphere_math_values.py** — writes one public JSON via `run_structural_analysis`.
- **run_e2e_all.py**, **batch_runner.py**, **reading_scales.py**, **run_corpus_benchmark.py**, **analyze.py** — batch, calibration, benchmarks, and sentence-level flows.
- **run_e2e_full_stack.py** — one encompassing run: `run_e2e_all` + product JSON + physics validation + system seal + **`run_output_e2e_full_stack_manifest.json`** (artifact index). See `docs/E2E_RUN_ORDER.md` § “Full encompassing pipe”.

## Sphere execution flow (archived / dev)

Layer orchestration for `sphere.pipeline.pipeline_runner` lives under `sphere/pipeline/` (`layer_registry`, `pipeline_state`). It is gated off in production; pytest sets `HESPERIA_SPHERE_PIPELINE_DEV=1` for determinism tests that still import it.
