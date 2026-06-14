#!/usr/bin/env bash
# Dev pytest gate for Ethan inspection re-runs (HINS-11).
# Run from brain repo on alunel via ssh.
set -euo pipefail

echo "=== verify-hesperia-dev-pytest ==="

ssh alunel bash -s <<'REMOTE'
set -euo pipefail
FAIL=0

check() {
  local label="$1"
  shift
  if "$@"; then
    echo "OK: $label"
  else
    echo "FAIL: $label"
    FAIL=1
  fi
}

HES_DEV=/data/workspaces/atomic-commit-hesperia
TER=/data/workspaces/tersagor

if [[ ! -x "$HES_DEV/.venv/bin/python" ]]; then
  echo "FAIL: dev clone venv missing at $HES_DEV/.venv"
  exit 1
fi
if [[ ! -x "$TER/.venv/bin/python" ]]; then
  echo "FAIL: tersagor venv missing at $TER/.venv"
  exit 1
fi

cd "$TER"
check "tersagor KSI subset" \
  .venv/bin/python -m pytest tests/test_ksi_*.py tests/test_hesperia_engine_bridge.py -q --tb=no

cd "$HES_DEV"
check "hesperia fast subset" \
  .venv/bin/python -m pytest tests/test_determinism.py tests/test_bundle_schema_validation.py -q --tb=no --maxfail=3

if [[ "$FAIL" -ne 0 ]]; then
  echo "verify-hesperia-dev-pytest: FAIL"
  exit 1
fi
echo "verify-hesperia-dev-pytest: OK"
REMOTE
