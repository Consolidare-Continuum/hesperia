#!/usr/bin/env bash
# Historical reference (pre-refactor)
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
DICT_A_PATH="${DICT_A_PATH:-${ROOT_DIR}/hesperia_lex/curated/A_CORE_STAR_MAP_v0_4_1_3.json}"
ASSETS_ROOT="${ASSETS_ROOT:-${ROOT_DIR}/hesperia_lex/curated}"
MODEL_REVISION="${MODEL_REVISION:-}"

# Venv-agnostic: prefer .venv_v040_build/bin/python if present, else PYTHON_BIN, else python3
if [[ -x "${ROOT_DIR}/.venv_v040_build/bin/python" ]]; then
  PYTHON_BIN="${PYTHON_BIN:-${ROOT_DIR}/.venv_v040_build/bin/python}"
else
  PYTHON_BIN="${PYTHON_BIN:-python3}"
fi
echo "Using python: ${PYTHON_BIN}"

if [[ -z "${MODEL_REVISION}" ]]; then
  echo "ERROR: MODEL_REVISION is required for repeatability check." >&2
  exit 1
fi

tmp1="$(mktemp -d)"
tmp2="$(mktemp -d)"
cleanup() {
  rm -rf "${tmp1}" "${tmp2}"
}
trap cleanup EXIT

build_once() {
  local out_dir="$1"
  (
    cd "${ROOT_DIR}"
    "${PYTHON_BIN}" -m sphere_rag.build_v040 \
      --dict-a "${DICT_A_PATH}" \
      --assets-root "${ASSETS_ROOT}" \
      --out-dir "${out_dir}" \
      --mode balanced \
      --model-revision "${MODEL_REVISION}"
  )
}

build_once "${tmp1}"
build_once "${tmp2}"

sha1="$(sha256sum "${tmp1}/surface_map_v040.json" | awk '{print $1}')"
sha2="$(sha256sum "${tmp2}/surface_map_v040.json" | awk '{print $1}')"

if [[ "${sha1}" != "${sha2}" ]]; then
  echo "Non-deterministic surface build detected: sha differs across two runs." >&2
  echo "run1=${sha1}" >&2
  echo "run2=${sha2}" >&2
  exit 1
fi

echo "Repeatability check passed: ${sha1}"
