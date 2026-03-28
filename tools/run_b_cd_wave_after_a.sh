#!/usr/bin/env bash
# After Dict A is frozen and validators green: exercise B line + CD executor + one CD-on runtime smoke.
# No OpenAI. Uses HESPERIA_CALIB_DICT_VERSION (default v0_6_0_clr_v052_2).
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"
export PYTHONPATH=.

CALIB="${HESPERIA_CALIB_DICT_VERSION:-v0_6_0_clr_v052_2}"

echo "=== B pack validators (resolver / DLCR dict_b) ==="
python3 tools/validate_dict_b_dlcr.py
python3 tools/validate_tfp_ru_pack.py
python3 tools/check_dlcr_regression.py

echo "=== CD (Concept Dictionary) unit tests ==="
python3 -m pytest tests/concept_dictionary/test_cd_executor.py -q

TMP_IN="$(mktemp)"
TMP_OUT="$(mktemp)"
TMP_MAN="$(mktemp)"
cleanup() { rm -f "$TMP_IN" "$TMP_OUT" "$TMP_MAN"; }
trap cleanup EXIT
echo 'clinical language borderline splitting identity diffusion' >"$TMP_IN"

echo "=== Runtime smoke: HESPERIA_CALIB_DICT_VERSION=$CALIB HESPERIA_CD_ENABLED=1 ==="
HESPERIA_CALIB_DICT_VERSION="$CALIB" HESPERIA_CD_ENABLED=1 \
  python3 -m hesperia.run "$TMP_IN" --config configs/pipeline.yaml --out "$TMP_OUT" --manifest-out "$TMP_MAN"

echo "DONE: B+CD wave after green A (see docs/governance/cd_v1/MODEL_CARD_CD_PIPELINE.md: A→B→CD→C_agg→Topology)."
