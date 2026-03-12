<!--
HESPERIA — Reference Architecture Definition (RAD)
Copyright © 2026 igareosh.com — Platonov Igor (aka @igareosh). All rights reserved.
Restricted Research Disclosure License. Inspection and reference only.
No reproduction, redistribution, or use without explicit written permission.
See LEGAL_NOTICE.md for full terms.
-->

# HESPERIA Testing Framework

Deterministic test suite for layer contracts, topology, propagation, logic engine, and pipeline reproducibility.

## Layout

- **`layers/`** — Layer unit tests (L1–L9: semantic, dict activation, structural, topology, metrics, dynamism, propagation, shadow, logic)
- **`topology/`** — Area adjacency matrix (12×12), family–area mapping (288), topology loader
- **`propagation/`** — Propagation/diffusion outputs (propagated area vector length 12, family counts 288)
- **`logic/`** — Rule parser (Prolog-style), rule runtime, rule engine, trigger registry
- **`determinism/`** — Pipeline determinism, USF serialization determinism
- **`golden/`** — Golden USF output (optional lock when `fixtures/golden_usf.json` exists)
- **`fixtures/`** — `sample_texts.json`, `metrics_vectors.json`, `logic_cases.json`, `propagation_vectors.json`

## Commands

```bash
# Quick run (quiet, short tracebacks)
pytest -q

# CI-style (fail fast, no warnings)
pytest --maxfail=1 --disable-warnings

# With coverage (optional; requires pytest-cov)
pytest --cov=sphere --cov=core --cov-report=term-missing
```

## Coverage targets (reference)

| Component           | Target  |
|--------------------|---------|
| metrics layer       | ≥ 95%   |
| topology loader     | ≥ 95%   |
| propagation engine  | ≥ 90%   |
| logic engine        | ≥ 90%   |
| pipeline runner     | ≥ 85%   |
| guards              | ≥ 85%   |

## Golden USF

To lock canonical pipeline output, run the pipeline once on the canonical text and save the USF to `tests/fixtures/golden_usf.json`. The test `tests/golden/test_golden_usf_outputs.py` then compares fingerprint and structural sections; it is skipped if the file is absent.
