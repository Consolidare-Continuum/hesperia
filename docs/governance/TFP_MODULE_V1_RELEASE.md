# RUNBOOK — TFP module v1 release chain

**Owner slice (TFP-V1-07):** single ordered chain before tagging / seal handoff. Run from **Hesperia repo root** with `PYTHONPATH=.` (or export `PYTHONPATH=$PWD`).

## 1. Environment

- Optional: `HESPERIA_CALIB_DICT_VERSION` — must match a pack under `assets/calibration/dicts/<pack>/` when testing pinned packs (see [`HESPERIA_TFP_MODULE_DICTS.md`](../HESPERIA_TFP_MODULE_DICTS.md)).
- Optional: `HESPERIA_SHIPPING_ENV_STRICT=1` — fail-closed on unknown `HESPERIA_*` at shipping API startup.

## 2. Version authority

```bash
python3 tools/validate_version_consistency.py
```

Confirms `VERSION.yaml` ↔ `pyproject.toml`, mirror `hesperia/VERSION.yaml`, public schema keys, calibration pack pin, and `tfp_module_v1` alignment.

## 3. B + CD wave (when calibration JSONL present)

```bash
bash tools/run_b_cd_wave_after_a.sh
```

If large artifacts are missing locally, CI may SKIP this step; do not treat local SKIP as release-ready unless dict pack is intentionally absent.

## 4. Phase-C TFP smoke (latency-capped)

```bash
bash tools/run_tfp_phase_c_smoke.sh
```

Precheck + wave + metrics gate + pytest slice (`test_tfp_module_main_run`, determinism, TFP ENF/REL tests). Override `HESPERIA_PHASE_C_SMOKE_MAX_SEC` only with governance note.

## 5. Module v1 spot checks

```bash
python3 -m pytest tests/test_tfp_module_v1_dlcr_golds.py tests/test_tfp_module_v1_public_surface.py -q --tb=short
python3 tools/validate_tfp_bundle_schemas.py --bundle-dir tests/fixtures/tfp_calibration_bundle_ci
```

## 6. Seal

Follow [`TFP_MODULE_V1_SEAL_CHECKLIST.md`](TFP_MODULE_V1_SEAL_CHECKLIST.md) (Ethan TFP-V1-15).

`SIGNED: Liam (runbook) | TFP module v1 | 2026-03-28 | TFP-V1-07`
