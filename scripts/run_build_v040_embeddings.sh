#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
VENV_DIR="${VENV_DIR:-${ROOT_DIR}/.venv_v040_build}"
PYTHON_BIN="${PYTHON_BIN:-python3}"
OUT_DIR="${OUT_DIR:-${ROOT_DIR}/assets/v040}"
DICT_A_PATH="${DICT_A_PATH:-${ROOT_DIR}/hesperia_lex/curated/A_CORE_STAR_MAP_v0_4_1_3.json}"
CANDIDATES_PATH="${CANDIDATES_PATH:-}"
MODE="${MODE:-balanced}"

if [[ ! -f "${DICT_A_PATH}" ]]; then
  echo "ERROR: Dict A file not found: ${DICT_A_PATH}" >&2
  exit 1
fi

if [[ -n "${CANDIDATES_PATH}" ]] && [[ ! -f "${CANDIDATES_PATH}" ]]; then
  echo "ERROR: Candidates file not found: ${CANDIDATES_PATH}" >&2
  exit 1
fi

if [[ ! -d "${VENV_DIR}" ]]; then
  "${PYTHON_BIN}" -m venv "${VENV_DIR}"
fi

# shellcheck disable=SC1091
source "${VENV_DIR}/bin/activate"
python -m pip install -r "${ROOT_DIR}/requirements-build-embeddings.txt"

# Keep build strictly on PyTorch. TensorFlow is not used for this build pipeline.
export USE_TF=0
export TRANSFORMERS_NO_TF=1
export TRANSFORMERS_NO_FLAX=1

mkdir -p "${OUT_DIR}"

CMD=(python -m sphere_rag.build_v040
  --dict-a "${DICT_A_PATH}"
  --assets-root "${ROOT_DIR}/hesperia_lex/curated"
  --out-dir "${OUT_DIR}"
  --mode "${MODE}")

if [[ -n "${CANDIDATES_PATH}" ]]; then
  CMD+=(--candidates "${CANDIDATES_PATH}")
fi

( cd "${ROOT_DIR}" && "${CMD[@]}" )

for artifact in \
  "${OUT_DIR}/surface_map_v040.json" \
  "${OUT_DIR}/dict_b_v040.json" \
  "${OUT_DIR}/build_manifest_v040.json"
do
  if [[ ! -f "${artifact}" ]]; then
    echo "ERROR: Expected artifact missing: ${artifact}" >&2
    exit 1
  fi
  sha256sum "${artifact}"
done
