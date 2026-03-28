# TFP latency + metrics gate (TFP-GATE-METRICS)

**Reference:** prichindel-class host, 2026-03-28.

| Command | Wall time (approx) | Notes |
|---------|-------------------|--------|
| `bash tools/run_tfp_phase_c_smoke.sh` | ~5 s | precheck + B+CD wave + `test_tfp_module_main_run` + `test_env_determinism` |

**Alert rule:** If wall time **> 50 s** on same class host without intentional scope expansion, investigate CI/cache and wave subprocess cost.

**Enforcement:** `tools/run_tfp_phase_c_smoke.sh` records wall time and **fails** if `elapsed > HESPERIA_PHASE_C_SMOKE_MAX_SEC` (default **120**). Override for slow CI if needed; do not raise default without Grace/Ethan note.

**Ratio (TFP-REL-05):** `tools/tfp_phase_c_latency_baseline_seconds.txt` holds reference seconds; fail if `elapsed > baseline * HESPERIA_PHASE_C_LATENCY_RATIO_MAX` (default **25**).

**`metrics.json` / `calibration_release_gate`:** Pack-level thresholds and pass/fail are enforced by `tools/calibration_release_gate.py` and `tests/test_calibration_release_gate.py` (see `sealed-runtime-gate.yml` CI bundle). TFP bundle runs should include gate evaluation on the same `metrics.json` that ships under `assets/calibration/dicts/<pack>/`.

---

`SIGNED: Cursor (workflow) | TFP-GATE-METRICS | 2026-03-28`
