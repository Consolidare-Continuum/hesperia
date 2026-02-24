# HESPERIA — Runnable entry points (Cursor / pre-test)

All commands assume **current directory = `CLIENTS/hesperia`** (this repo root). Use `.venv_v040/bin/python` if you use the v040 venv.

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
- **Full pass**: `python3 -m sphere_rag.layers.run_l1_through_l9 --out docs/layer_runs/latest_L1_L9_output.json` (from CLIENTS/hesperia; `mkdir -p docs/layer_runs` first). Output log dir: [docs/layer_runs/](docs/layer_runs/).
- **L1+L2**: `python3 -m sphere_rag.layers.run_l1_l2`; **L1+L2+L3**: `python3 -m sphere_rag.layers.run_l1_l2_l3`. See [docs/NEXT_STEPS_MATH_INTEGRATION.md](docs/NEXT_STEPS_MATH_INTEGRATION.md).

## Traversal order (Cursor)

1. `scripts/run_hesperia_pre_test.py` — whole pre-test.
2. `sphere_rag/build_v040.py` — v0.4.0 pipeline.
3. `sphere_rag/build_v041.py` — v0.4.1 Dict B.
4. `sphere_rag/hesperia_v03_core_math.py test` — core math.
5. `sphere_rag/run_simulation.py` — full/chroma/serve.
6. `sphere_rag/layers/run_l1_through_l9.py` — full L1–L9 pass; L1/L1+L2/L1+L2+L3 runners in same package.
7. `sphere_rag/tests/` — pytest.
