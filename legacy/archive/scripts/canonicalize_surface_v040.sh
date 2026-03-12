#!/usr/bin/env bash

# HESPERIA — Reference Architecture Definition (RAD)
# Copyright © 2026 igareosh.com — Platonov Igor (aka @igareosh). All rights reserved.
# Restricted Research Disclosure License. Inspection and reference only.
# No reproduction, redistribution, or use without explicit written permission from the author.
# See LEGAL_NOTICE.md for full terms.

set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
DICT_A_PATH="${DICT_A_PATH:-${ROOT_DIR}/hesperia_lex/curated/A_CORE_STAR_MAP_v0_4_1_3.json}"
ASSETS_ROOT="${ASSETS_ROOT:-${ROOT_DIR}/hesperia_lex/curated}"
OUT_DIR="${OUT_DIR:-${ROOT_DIR}/assets/v040}"
MODEL_REVISION="${MODEL_REVISION:-}"
EXPECTED_FILE="${EXPECTED_FILE:-${ROOT_DIR}/assets/v040/surface_map_v040.json.sha256}"

if [[ -z "${MODEL_REVISION}" ]]; then
  echo "ERROR: MODEL_REVISION is required for canonical v0.4.0 build." >&2
  exit 1
fi

mkdir -p "${OUT_DIR}"

(
  cd "${ROOT_DIR}"
  python -m sphere_rag.build_v040 \
    --dict-a "${DICT_A_PATH}" \
    --assets-root "${ASSETS_ROOT}" \
    --out-dir "${OUT_DIR}" \
    --mode balanced \
    --model-revision "${MODEL_REVISION}"
)

(
  cd "${ROOT_DIR}"
  python -m sphere_rag.validate_surface_map_v040 "${OUT_DIR}/surface_map_v040.json"
)

if [[ ! -f "${OUT_DIR}/surface_map_v040.json" ]]; then
  echo "ERROR: missing generated surface map at ${OUT_DIR}/surface_map_v040.json" >&2
  exit 1
fi

generated_line="$(sha256sum "${OUT_DIR}/surface_map_v040.json" | awk '{print $1 "  surface_map_v040.json"}')"
expected_hash=""
if [[ -f "${EXPECTED_FILE}" ]]; then
  expected_hash="$(awk '{print $1}' "${EXPECTED_FILE}")"
fi

if [[ -z "${expected_hash}" || "${expected_hash}" == "UNSET" ]]; then
  printf '%s\n' "${generated_line}" > "${EXPECTED_FILE}"
  echo
  echo "============================================================"
  echo "Expected checksum set. Commit this change."
  echo "Wrote: ${EXPECTED_FILE}"
  echo "============================================================"
  exit 0
fi

"${ROOT_DIR}/scripts/verify_surface_map_v040_checksum.sh" \
  "${OUT_DIR}/surface_map_v040.json" \
  "${EXPECTED_FILE}"

