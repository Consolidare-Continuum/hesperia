#!/usr/bin/env bash
# TFP-GATE-C-SMOKE + TFP-ENF-04/05: precheck, wave, metrics gate, pytest slice, wall-clock cap.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"
export PYTHONHASHSEED=0
export PYTHONPATH=.
START_TIME=$SECONDS
bash tools/run_tfp_env_precheck.sh
bash tools/run_b_cd_wave_after_a.sh
python3 tools/check_metrics_gate.py
python3 -m pytest tests/test_tfp_module_main_run.py tests/test_env_determinism.py \
  tests/test_tfp_concept_invariants_enf.py tests/test_tfp_cd_delta_enf.py tests/test_tfp_unmapped_gate_enf.py \
  -q --tb=short
elapsed=$((SECONDS - START_TIME))
max=${HESPERIA_PHASE_C_SMOKE_MAX_SEC:-120}
if (( elapsed > max )); then
  echo "FAIL: phase C wall time ${elapsed}s > max ${max}s" >&2
  exit 1
fi
echo "OK: TFP phase C smoke (${elapsed}s <= ${max}s): precheck + wave + metrics gate + ENF pytest slice."
