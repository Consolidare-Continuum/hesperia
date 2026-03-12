#!/usr/bin/env bash

# HESPERIA — Reference Architecture Definition (RAD)
# Copyright © 2026 igareosh.com — Platonov Igor (aka @igareosh). All rights reserved.
# Restricted Research Disclosure License. Inspection and reference only.
# No reproduction, redistribution, or use without explicit written permission from the author.
# See LEGAL_NOTICE.md for full terms.

# Freeze ownership: write assets/v040/CANONICAL_SURFACE_V040.txt from BUILD_PROVENANCE and git.
# Run only after: (1) canonical build produced surface_map_v040.json + .sha256 + BUILD_PROVENANCE_v040.json,
#                 (2) determinism proven (two builds, same SHA).
# From this moment surface_map_v040.json is immutable; any hash change = version bump.
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
OUT_DIR="${OUT_DIR:-${ROOT_DIR}/assets/v040}"
PROVENANCE="${OUT_DIR}/BUILD_PROVENANCE_v040.json"
SURFACE_SHA_FILE="${OUT_DIR}/surface_map_v040.json.sha256"
CANONICAL_TXT="${OUT_DIR}/CANONICAL_SURFACE_V040.txt"

if [[ ! -f "${PROVENANCE}" ]]; then
  echo "ERROR: BUILD_PROVENANCE_v040.json not found at ${PROVENANCE}. Run canonical build first." >&2
  exit 1
fi
if [[ ! -f "${SURFACE_SHA_FILE}" ]]; then
  echo "ERROR: surface_map_v040.json.sha256 not found at ${SURFACE_SHA_FILE}. Run canonical build first." >&2
  exit 1
fi

# Trim to one line each (no embedded newline/carriage return)
commit_hash="$(cd "${ROOT_DIR}" && git rev-parse HEAD | tr -d '\n\r')"
surface_sha="$(awk '{print $1}' "${SURFACE_SHA_FILE}" | tr -d '\n\r')"
model_revision="$(python3 -c "
import json
with open('${PROVENANCE}') as f:
    p = json.load(f)
print(p.get('inputs', {}).get('model_revision', 'UNSET'), end='')
")"
model_revision="$(printf '%s' "${model_revision}" | tr -d '\n\r')"
dict_a_sha="$(python3 -c "
import json
with open('${PROVENANCE}') as f:
    p = json.load(f)
print(p.get('inputs', {}).get('dict_a_sha256', 'UNSET'), end='')
")"
dict_a_sha="$(printf '%s' "${dict_a_sha}" | tr -d '\n\r')"

if [[ "${model_revision}" == "UNSET" ]] || [[ "${dict_a_sha}" == "UNSET" ]]; then
  echo "ERROR: Provenance has UNSET; rebuild with explicit MODEL_REVISION and Dict A." >&2
  exit 1
fi

mkdir -p "${OUT_DIR}"
# One key/value per line, explicit newline after each (parsers and B1 reader depend on it)
{
  printf '%s\n' "HESPERIA v0.4.0 canonical surface — frozen ownership"
  printf '%s\n' ""
  printf '%s\n' "canonical_git_commit: ${commit_hash}"
  printf '%s\n' "surface_map_sha256: ${surface_sha}"
  printf '%s\n' "model_name: sentence-transformers/all-mpnet-base-v2"
  printf '%s\n' "model_revision: ${model_revision}"
  printf '%s\n' "dict_a_sha256: ${dict_a_sha}"
  printf '%s\n' ""
  printf '%s\n' "Surface is immutable. Any hash change = version bump. No silent rebuilds."
} > "${CANONICAL_TXT}"
echo "Wrote ${CANONICAL_TXT}"
echo "Surface locked: ${surface_sha}"
