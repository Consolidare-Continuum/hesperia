# Run HESPERIA from scratch

Minimal steps to get the repo and run the pipeline and tests on a clean machine.

**To build shipping artifacts (CLI binary, Docker API, manifest)** see [BUILD_FROM_SCRATCH.md](BUILD_FROM_SCRATCH.md).

---

## 1. Clone

```bash
git clone https://github.com/Atomic-Commits-Team/hesperia.git
cd hesperia
```

(Or your fork / preferred remote.)

---

## 2. Python

Use **Python 3.10 or 3.11**. Check:

```bash
python3 --version
```

---

## 3. Virtual environment (recommended)

```bash
python3 -m venv .venv
source .venv/bin/activate   # Linux/macOS
# or:  .venv\Scripts\activate   # Windows
```

---

## 4. Dependencies

From the repo root:

```bash
pip install -r requirements.txt
```

This pulls `requirements_surface.txt` (sentence-transformers, torch, etc.). First run may download the embedding model.

---

## 5. Run from repo root

All commands below are run with the repo root as current directory (so `core`, `runtime`, `sphere`, etc. are on the path).

**Full E2E (all flows, 6 artifacts):**

```bash
python3 -m runtime.pipeline.run_e2e_all
```

Outputs go to `assets/artifacts/e2e/`. Optional: `--out-dir PATH`, `--text "..."`.

**L1–L9 single run:**

```bash
python3 -m runtime.pipeline.run_l1_through_l9 --out out.json
```

**Tests:**

```bash
python3 -m pytest tests/ -q
```

E2E and sealed regression only:

```bash
python3 -m pytest tests/test_e2e_flows.py tests/test_sealed_runtime_regression.py -v
```

---

## 6. Sealed CLI (optional)

Analyze one text, compare two, or batch-analyze:

```bash
python3 -m runtime.shipping.cli_main analyze --text "Your sentence here."
python3 -m runtime.shipping.cli_main compare --text1 "First." --text2 "Second."
python3 -m runtime.shipping.cli_main batch-analyze --paths path/to/*.txt
```

---

## 7. API server (optional)

Sealed API (analyze, compare, batch-analyze):

```bash
python3 -m runtime.shipping.api_main
```

Then e.g. `curl http://127.0.0.1:8000/health` and `POST /analyze` with JSON `{"text": "..."}`.

Or the legacy API module:

```bash
pip install uvicorn  # if not already installed
uvicorn runtime.api.main:app --host 127.0.0.1 --port 8000
```

---

## 8. Data

- **Lexicon:** The repo expects `lexicon/curated/` (and optionally `lexicon/frozen/`) with Dict A/B and related assets. If you have a minimal or custom layout, point entry points to it via `--assets` or the `assets_root` used by the pipeline.
- **E2E:** No extra data is required; the E2E runner uses built-in sample text.

---

## Quick reference

| Goal              | Command |
|-------------------|---------|
| Install           | `pip install -r requirements.txt` |
| Full E2E          | `python3 -m runtime.pipeline.run_e2e_all` |
| L1–L9             | `python3 -m runtime.pipeline.run_l1_through_l9 --out out.json` |
| All tests         | `python3 -m pytest tests/ -q` |
| Sealed CLI        | `python3 -m runtime.shipping.cli_main analyze --text "..."` |
| Sealed API        | `python3 -m runtime.shipping.api_main` |
