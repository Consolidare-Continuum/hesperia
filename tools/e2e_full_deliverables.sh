#!/usr/bin/env bash
# HESPERIA — Full E2E with all dynamics deliverables (Gena + Ethan stack).
# Steps 1–10 (incl. TFP smoke) + field_dynamics: L4+L8+L5+L6, TRIZ→c_sig, Ξ proxy when rows exist.
# Usage: ./tools/e2e_full_deliverables.sh [OUT_DIR] ["session text..."]
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"
export HESPERIA_FIELD_DYNAMICS=1
export HESPERIA_FIELD_DYNAMICS_PHASE2=1
export HESPERIA_FIELD_DYNAMICS_PHASE3=1
export HESPERIA_FIELD_DYNAMICS_PHASE4=1
export HESPERIA_FIELD_DYNAMICS_TRIZ=1
export HESPERIA_FIELD_DYNAMICS_XI=1
export HESPERIA_E2E_MULTISCALE=1
OUT="${1:-assets/artifacts/e2e_full_deliverables}"
shift || true
TEXT="${*:-Patient reports severe anxiety when considering work deadlines but also feels guilty resting. The team demands faster delivery while quality must not slip. Internal conflict between autonomy and compliance.}"
python3 -m runtime.pipeline.run_e2e_all --out-dir "$OUT" --text "$TEXT"
