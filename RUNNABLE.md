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

## Traversal order (Cursor)

1. `scripts/run_hesperia_pre_test.py` — whole pre-test.
2. `sphere_rag/build_v040.py` — v0.4.0 pipeline.
3. `sphere_rag/build_v041.py` — v0.4.1 Dict B.
4. `sphere_rag/hesperia_v03_core_math.py test` — core math.
5. `sphere_rag/run_simulation.py` — full/chroma/serve.
6. `sphere_rag/tests/` — pytest.
