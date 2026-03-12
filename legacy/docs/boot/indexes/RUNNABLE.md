<!--
HESPERIA — Reference Architecture Definition (RAD)
Copyright © 2026 igareosh.com — Platonov Igor (aka @igareosh). All rights reserved.
Restricted Research Disclosure License. Inspection and reference only.
No reproduction, redistribution, or use without explicit written permission.
See LEGAL_NOTICE.md for full terms.
-->

# Historical reference (pre-refactor)

# HESPERIA — Runnable entry points (Cursor / pre-test)

All commands assume **current directory = this repo root**. Use `.venv_v040/bin/python` if you use the v040 venv.

---

## One-shot pre-test (small, no big builds)

Runs v0.4.0 build → v0.4.1 build → core_math test → pytest.

```bash
python scripts/run_hesperia_pre_test.py
# or
.venv_v040/bin/python scripts/run_hesperia_pre_test.py
# or via run_simulation (from CLIENTS/hesperia):
python sphere_rag/run_simulation.py pretest
```

---

## Builds (small / test only)

**v0.4.0** (Dict A → anchors → Dict B → surface + §8A affinity):

```bash
python -m sphere_rag.build_v040 --assets-root hesperia_lex/curated --out-dir assets/v040 --allow-small-build
```

**v0.4.1** Dict B (preferred + possible_relaxed, needs v040 artifacts):

```bash
python -m sphere_rag.build_v041 --assets-root assets --out-dir assets/v041 --allow-small-build
```

---

## v0.3 core and simulation

**Core math demo:**

```bash
python sphere_rag/hesperia_v03_core_math.py
```

**Core math tests:**

```bash
python sphere_rag/hesperia_v03_core_math.py test
```

**Simulation modes** (single entry):

```bash
python sphere_rag/run_simulation.py full [--S path] [--L path] [--out path]
python sphere_rag/run_simulation.py chroma [--no-books-check] [--out path]
python sphere_rag/run_simulation.py serve [port]
```

---

## Tests (pytest)

```bash
python -m pytest sphere_rag/tests -v --tb=short
# subset (quick):
python -m pytest sphere_rag/tests/test_attribution_v033.py sphere_rag/tests/test_invariant_v03.py -v --tb=short
```

---

## API server (v0.3.3)

```bash
python sphere_rag/serve_v033.py
# or
python sphere_rag/run_simulation.py serve 8080
```

---

## Dependency

- **v0.4.x builds**: `pip install -r requirements_v040.txt` (or use `.venv_v040`). Model downloaded on first run.
- **pytest**: `pip install pytest` (optional, for pre-test script).

---

## Layer stack (L1–L9, v0.4.x)

- **L1–L9** implemented: `sphere_rag/layers/layer_1.py` … `layer_9.py` (34_SPEC … 42_SPEC). Use `sphere_rag.layers.load_defaults()` for F, A, eps and predefined config.
- **Full pass**: `python3 -m sphere_rag.layers.run_l1_through_l9 --out artifacts/layer_runs/latest_L1_L9_output.json` (from repo root; `mkdir -p artifacts/layer_runs` first). Output log dir: [artifacts/layer_runs/](artifacts/layer_runs/).
- **With L1 profile**: `--profile profiles/STRUCTURE_PROFILE__UNIFORM_ENVELOPE__v1.json` (or any canonical profile from [profiles/](profiles/); see [profiles/TAXONOMY_v1.md](profiles/TAXONOMY_v1.md)).
- **L1+L2**: `python3 -m sphere_rag.layers.run_l1_l2`; **L1+L2+L3**: `python3 -m sphere_rag.layers.run_l1_l2_l3`. See [docs/NEXT_STEPS_MATH_INTEGRATION.md](docs/NEXT_STEPS_MATH_INTEGRATION.md).

## Traversal order (Cursor)

1. `scripts/run_hesperia_pre_test.py` — whole pre-test.
2. `sphere_rag/build_v040.py` — v0.4.0 pipeline.
3. `sphere_rag/build_v041.py` — v0.4.1 Dict B.
4. `sphere_rag/hesperia_v03_core_math.py test` — core math.
5. `sphere_rag/run_simulation.py` — full/chroma/serve.
6. `sphere_rag/layers/run_l1_through_l9.py` — full L1–L9 pass; L1/L1+L2/L1+L2+L3 runners in same package.
7. `sphere_rag/tests/` — pytest.

## v0.6 calibration (optional)

```bash
PYTHONPATH=. python scripts/run_calibration_v06.py
PYTHONPATH=. python scripts/verify_v06_operational.py
PYTHONPATH=. python scripts/calibration_metrics_v06.py [--output path] [--csv path]
```

Use `.venv_v040_build/bin/python` for scripts that need sentence-transformers (e.g. build).

## Build Dict A (v0.6)

```bash
PYTHONPATH=. .venv_v040_build/bin/python sphere_rag/build_dict_a.py [--assets hesperia_lex/frozen] [--save-calibration-stats] [--stability-guards]
PYTHONPATH=. python sphere_rag/validate_dict_a.py
PYTHONPATH=. python sphere_rag/audit_dict_a_runtime.py [--v06-dir assets/v06]
```

## API

```bash
# From repo root or CLIENTS/hesperia; ensure PYTHONPATH includes CLIENTS/hesperia
uvicorn api.main:app --host 0.0.0.0 --port 8000
```

## Core math (no attribution)

```bash
python sphere_rag/core_math.py
python sphere_rag/core_math.py test
```

## Layer math (L1–L9)

Code: `sphere_rag/layers/layer_1.py` … `layer_9.py`. Use `from sphere_rag.layers import compute_L1, …`.  
Runner scripts (L1–L9 full pass, L1+L2, etc.) are in [archive/layer_runners/](archive/layer_runners/).

## Archive

Deprecated entry points: [archive/ARCHIVE_MANIFEST.md](archive/ARCHIVE_MANIFEST.md).
