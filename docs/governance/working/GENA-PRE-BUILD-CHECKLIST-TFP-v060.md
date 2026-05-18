<!--
Gena — pre-flight before TFP dict build / calibration runs (post v0.5.1 seal).
-->

# Gena — 10 pre-build checks (TFP v0.6.0 plane)

Run these **before** `run_tfp_dict_build_full_artifacts_v060.py --write` or heavy calibration so you don’t hit obvious walls.

| # | Task | What “pass” looks like |
|---|------|-------------------------|
| **1** | **Corpus source exists** | `research/_noone_local/2_cleaned/` is a directory with expected `.md` (or agreed) inputs; not empty after last sync. |
| **2** | **Output root writable** | `assets/data/engine_dynamics_v060/` exists; you can create `corpora/`, `dict_a/_raw/`, `dict_b/`, `_artifacts/` (no permission / read-only FS). |
| **3** | **Python runs from repo root** | `cd` to repo root; `python3 --version` works; no import errors on `python3 -c "import json, pathlib"` (sanity). |
| **4** | **Dict B merge inputs present** | `assets/data/engine_dynamics_v060/dict_b/dict_b_seed.jsonl` exists; after any stack build, `dict_b_tfp_ru_v060.jsonl` exists; `dict_b_tfp.jsonl` exists (may be large — B_A10 + TFP rows). |
| **5** | **Schema validators (current tree)** | `validate_dict_b_dlcr.py` on `dict_b/dict_b_tfp.jsonl` → **OK**; `validate_dict_a.py` with **no args** validates **all** `*.jsonl` under `dict_a/` (includes `dict_a_tfp_ru_aligned.jsonl` when present) → **OK** (run whenever Dict A JSONL changed). |
| **6** | **TFP RU pack + DLCR regression** | `python3 tools/validate_tfp_ru_pack.py` → **OK**; `python3 tools/check_dlcr_regression.py` → **OK** (same merged Dict A list as runtime expectations). |
| **7** | **Dry-run expansion (optional, fast signal)** | `python3 tools/expand_dict_b_tfp_controlled.py` (no `--write`) completes exit **0**; JSON report prints (no traceback). |
| **8** | **Spec path for TFP topology** | `specs/canon/family_embedding_tfp.yaml` resolvable (and `spec/` → `specs/canon/` if loaders use `spec/`). Prevents “missing embedding” walls in TFP smoke. |
| **9** | **E2E TFP smoke (engine, not dict write)** | Full: `python3 -m runtime.pipeline.run_e2e_all --out-dir /tmp/e2e_gena_check` → `run_output_e2e_tfp_smoke.json` present. **DLCR on smoke only** (faster): `HESPERIA_TFP_DLCR=1 python3 -c "from pathlib import Path; from runtime.pipeline.run_e2e_all import run_e2e_tfp_smoke; run_e2e_tfp_smoke(Path('/tmp/tfp_smoke.json'))"` → JSON has non-empty `session_dlcr_bundles`. Optional pytest: `pytest tests/test_e2e_flows.py::test_e2e_tfp_smoke_artifact_shape tests/test_e2e_flows.py::test_e2e_tfp_smoke_with_dlcr_bundles -q`. |
| **10** | **Scope / git awareness** | You know whether this build is **TFP assets only** (dirty `git` OK) vs **release seal** (needs clean tree + `tools/release/build_release_audit_v0_5_1.py`). Don’t mix the two workflows. |

---

## Last verification (Gena / agent sweep)

| Field | Value |
|-------|--------|
| **Date** | 2026-03-20 |
| **Result** | All 10 checks **PASS** (example run) |
| **Notes** | Corpus `2_cleaned/`: 20 files; E2E full `run_e2e_all` ~80–90s typical; `HESPERIA_TFP_DLCR=1` on `run_e2e_tfp_smoke`: `session_dlcr_bundles` present (e.g. len 2). **Runtime merge:** `dict_a_tfp_ru_aligned.jsonl` is appended **last** in default `dict_a_paths` (first-wins on `normalized_form`; aligned layer fills gaps). Promote from `outputs/dict_calibration/.../dict_a_tfp_ru_aligned.jsonl` → `assets/.../dict_a/`. |

---

## One-liner sweep (after checks 1–4)

```bash
cd /path/to/hesperia
python3 tools/validate_dict_b_dlcr.py assets/data/engine_dynamics_v060/dict_b/dict_b_tfp.jsonl
python3 tools/validate_dict_a.py
python3 tools/validate_tfp_ru_pack.py
python3 tools/check_dlcr_regression.py
python3 tools/expand_dict_b_tfp_controlled.py
```

## Full dict + artifacts build (when ready)

```bash
python3 tools/run_tfp_dict_build_full_artifacts_v060.py --write
```

## File → engine artifacts (TFP + main Hesperia paths)

After dict assets are valid, run a **user transcript or JSON sessions** through structural batch, session/TFP stages, hex microstructure, **full DLCR**, sealed multiscale, and `analyze()`:

```bash
python3 tools/gena_tfp_bundle_run.py -i path/to/input.md
```

Writes under `outputs/tfp/runs/tfp_gena_<stem>/` by default (`00`–`06`, plus `10_calibration_audit.json`, `11_calibration_release_gate.json`). Use `-o outputs/tfp/runs/my_run` to pin the directory. For **pipeline only** (no audit/gate): `python3 tools/gena_tfp_bundle_run.py -i path/to/input.md -o outputs/tfp/runs/my_run --pipeline-only`, or `python3 -m runtime.pipeline.run_tfp_file_pipeline -i … -o …`.

See [ETHAN-TFP-RUNNABLE-DICT-WIRING.md](ETHAN-TFP-RUNNABLE-DICT-WIRING.md) §3a for flags (`--with-kme`, `--with-triz`, `--with-topology` → flat `12_<session>_*.json` in `--out-dir`, `--with-gold`, skips). TRIZ-from-topology spec: [TRIZ_TOPOLOGY_ACTIVATION_PIPELINE_v1.md](../specs/TRIZ_TOPOLOGY_ACTIVATION_PIPELINE_v1.md).

## Related docs

- [ETHAN-TFP-RU-CODEX-STACK.md](ETHAN-TFP-RU-CODEX-STACK.md) — stack + expand + `_artifacts/`.  
- [ETHAN-TFP-RUNNABLE-DICT-WIRING.md](ETHAN-TFP-RUNNABLE-DICT-WIRING.md) — planes A/B/C, env vars, smoke paths.  
- [CURSOR_REPO_AND_RELEASE_BEST_PRACTICES.md](../CURSOR_REPO_AND_RELEASE_BEST_PRACTICES.md) — when a “build” is a **release** vs research assets.
