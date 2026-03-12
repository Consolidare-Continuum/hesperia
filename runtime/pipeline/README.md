<!--
HESPERIA — Reference Architecture Definition (RAD)
Copyright © 2026 igareosh.com — Platonov Igor (aka @igareosh). All rights reserved.
Restricted Research Disclosure License. Inspection and reference only.
No reproduction, redistribution, or use without explicit written permission.
See LEGAL_NOTICE.md for full terms.
-->

# runtime/pipeline — Legacy Pipeline Modules

**Canonical entrypoint:** `sphere.pipeline.run_pipeline`  
**Reference CLI:** `runtime/runners/run_reference_pipeline.py` (calls sphere)

This package is **legacy**. New code should use:

- **Run the pipeline:** `from sphere.pipeline import run_pipeline` then `run_pipeline(raw_text, config, ...)`
- **CLI:** `python3 -m runtime.runners.run_reference_pipeline [--text ...] [--out path.json]`

## What lives here (legacy)

- **run_l1_through_l9.py** — Compatibility wrapper. `run_pipeline_for_text()` delegates to `sphere.pipeline.run_pipeline` when no profile is used; when a profile is provided, runs the legacy L1→L9 loop locally. `main()` remains for `python3 -m runtime.pipeline.run_l1_through_l9`.
- **layer_registry.py** — Still used by the canonical sphere pipeline runner (L1–L9 module list). Do not remove; it is shared infrastructure.
- **pipeline_state.py** — Still used by the canonical sphere pipeline runner. Do not remove; it is shared infrastructure.
- **batch_runner.py**, **reading_scales.py**, **run_e2e_all.py**, **analyze.py**, etc. — Legacy scripts; they may call `run_pipeline_for_text` or other entrypoints.

## Contract validation

Pipeline contract validation runs inside `sphere.pipeline.pipeline_runner` (contract_validation, isolation_validation). The canonical pipeline enforces layer contracts and isolation.
