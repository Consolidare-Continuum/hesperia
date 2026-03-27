#!/usr/bin/env bash
# Copy corpus + dict artifacts into hesperia/modules/tfp/data/ for interim module-local work.
# Does not modify research/ (read-only rsync from source).
# Repo root = directory containing tools/ and hesperia/.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
DEST="${ROOT}/hesperia/modules/tfp/data"
CALIB_VER="${HESPERIA_CALIB_DICT_VERSION:-v0_6_0_clr_v052_1}"

mkdir -p "${DEST}/corpus" "${DEST}/dicts/calibration" "${DEST}/dicts"

if [[ -d "${ROOT}/research/_noone_local/2_cleaned" ]]; then
  mkdir -p "${DEST}/corpus/ru_2_cleaned"
  rsync -a --delete "${ROOT}/research/_noone_local/2_cleaned/" "${DEST}/corpus/ru_2_cleaned/"
  echo "Synced ru_2_cleaned -> ${DEST}/corpus/ru_2_cleaned"
else
  echo "SKIP: ${ROOT}/research/_noone_local/2_cleaned not present"
fi

if [[ -d "${ROOT}/research/_noone_local/english_2_cleaned" ]]; then
  mkdir -p "${DEST}/corpus/en_2_cleaned"
  rsync -a --delete "${ROOT}/research/_noone_local/english_2_cleaned/" "${DEST}/corpus/en_2_cleaned/"
  echo "Synced english_2_cleaned -> ${DEST}/corpus/en_2_cleaned"
else
  echo "SKIP: ${ROOT}/research/_noone_local/english_2_cleaned not present"
fi

if [[ -d "${ROOT}/assets/calibration/dicts/${CALIB_VER}" ]]; then
  mkdir -p "${DEST}/dicts/calibration/${CALIB_VER}"
  rsync -a --delete "${ROOT}/assets/calibration/dicts/${CALIB_VER}/" "${DEST}/dicts/calibration/${CALIB_VER}/"
  echo "Synced calibration ${CALIB_VER} -> ${DEST}/dicts/calibration/${CALIB_VER}"
else
  echo "SKIP: ${ROOT}/assets/calibration/dicts/${CALIB_VER} not present"
fi

if [[ -d "${ROOT}/assets/data/engine_dynamics_v060" ]]; then
  mkdir -p "${DEST}/dicts/engine_dynamics_v060"
  rsync -a --delete "${ROOT}/assets/data/engine_dynamics_v060/" "${DEST}/dicts/engine_dynamics_v060/"
  echo "Synced engine_dynamics_v060 -> ${DEST}/dicts/engine_dynamics_v060"
else
  echo "SKIP: ${ROOT}/assets/data/engine_dynamics_v060 not present"
fi

echo "DONE: TFP module data mirror under ${DEST}"
