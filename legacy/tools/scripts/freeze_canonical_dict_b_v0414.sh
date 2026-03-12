#!/usr/bin/env bash

# HESPERIA — Reference Architecture Definition (RAD)
# Copyright © 2026 igareosh.com — Platonov Igor (aka @igareosh). All rights reserved.
# Restricted Research Disclosure License. Inspection and reference only.
# No reproduction, redistribution, or use without explicit written permission from the author.
# See LEGAL_NOTICE.md for full terms.

# Historical reference (pre-refactor)
# Freeze Dict B (B1) v0.4.1.4: write assets/v0414/CANONICAL_DICT_B_V0414.txt.
# Run only after: (1) B1 build succeeded (frozen surface matched), (2) validation OK.
# From this moment Dict B (B1) is immutable; any hash change = version bump.
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
OUT_DIR="${OUT_DIR:-${ROOT_DIR}/assets/v0414}"
CANONICAL_SURFACE="${ROOT_DIR}/assets/v040/CANONICAL_SURFACE_V040.txt"
B1_JSON="${ROOT_DIR}/hesperia_lex/frozen/B1_SIDE_TO_FAMILY_v0_4_1_4.json"
B1_SHA="${ROOT_DIR}/hesperia_lex/frozen/B1_SIDE_TO_FAMILY_v0_4_1_4.sha256"
CANONICAL_TXT="${OUT_DIR}/CANONICAL_DICT_B_V0414.txt"

if [[ ! -f "${CANONICAL_SURFACE}" ]]; then
  echo "ERROR: CANONICAL_SURFACE_V040.txt not found at ${CANONICAL_SURFACE}. Freeze surface first." >&2
  exit 1
fi
if [[ ! -f "${B1_JSON}" ]] || [[ ! -f "${B1_SHA}" ]]; then
  echo "ERROR: B1 artifact or .sha256 not found. Run B1 build first." >&2
  exit 1
fi

# Parse canonical surface (one key: value per line)
get_val() {
  local key="$1"
  grep -E "^${key}:" "${CANONICAL_SURFACE}" | sed -E 's/^[^:]+:[[:space:]]*//' | tr -d '\n\r'
}
surface_sha="$(get_val surface_map_sha256)"
model_name="$(get_val model_name)"
model_revision="$(get_val model_revision)"
dict_a_sha="$(get_val dict_a_sha256)"

if [[ -z "${surface_sha}" ]] || [[ "${surface_sha}" == "UNSET" ]]; then
  echo "ERROR: surface_map_sha256 not found in canonical surface." >&2
  exit 1
fi
if [[ -z "${dict_a_sha}" ]] || [[ "${dict_a_sha}" == "UNSET" ]]; then
  echo "ERROR: dict_a_sha256 not found in canonical surface." >&2
  exit 1
fi

commit_hash="$(cd "${ROOT_DIR}" && git rev-parse HEAD | tr -d '\n\r')"
dict_b_sha="$(awk '{print $1}' "${B1_SHA}" | tr -d '\n\r')"
model_name="${model_name:-sentence-transformers/all-mpnet-base-v2}"
model_revision="${model_revision:-UNSET}"

mkdir -p "${OUT_DIR}"
{
  printf '%s\n' "HESPERIA Dict B (B1) v0.4.1.4 — frozen ownership"
  printf '%s\n' ""
  printf '%s\n' "canonical_git_commit: ${commit_hash}"
  printf '%s\n' "dict_b_sha256: ${dict_b_sha}"
  printf '%s\n' "surface_map_sha256: ${surface_sha}"
  printf '%s\n' "model_name: ${model_name}"
  printf '%s\n' "model_revision: ${model_revision}"
  printf '%s\n' "dict_a_sha256: ${dict_a_sha}"
  printf '%s\n' ""
  printf '%s\n' "Dict B (B1) is immutable. Any hash change = version bump. No silent rebuilds."
} > "${CANONICAL_TXT}"
echo "Wrote ${CANONICAL_TXT}"
echo "Dict B (B1) locked: ${dict_b_sha}"
