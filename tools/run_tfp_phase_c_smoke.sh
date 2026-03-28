#!/usr/bin/env bash
# TFP-GATE-C-SMOKE: one chain with set -e — precheck, B+CD wave, small pytest slice, version check.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"
export PYTHONHASHSEED=0
export PYTHONPATH=.
bash tools/run_tfp_env_precheck.sh
bash tools/run_b_cd_wave_after_a.sh
python3 -m pytest tests/test_tfp_module_main_run.py tests/test_env_determinism.py -q --tb=short
echo "OK: TFP phase C smoke (precheck + wave + tfp_module + determinism tests)."
