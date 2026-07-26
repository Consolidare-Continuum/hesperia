#!/usr/bin/env bash
# alunel — Hesperia dev environment (source this file, do not execute).
# Sets PYTHONPATH for the canonical clone; activates .venv (pyenv 3.12.8 per PYTHON-STANDARD).
# Ref: cluster/alunel/HESPERIA-DEV.md
# shellcheck disable=SC1091
HESPERIA_REPO="${HESPERIA_REPO:-/data/workspaces/atomic-commit-hesperia}"
export HESPERIA_REPO
export PYTHONPATH="${HESPERIA_REPO}${PYTHONPATH:+:${PYTHONPATH}}"
if [ -f "${HESPERIA_REPO}/.venv/bin/activate" ]; then
  # shellcheck source=/dev/null
  source "${HESPERIA_REPO}/.venv/bin/activate"
else
  echo "WARN: ${HESPERIA_REPO}/.venv missing — create with pyenv 3.12.8; see cluster/alunel/HESPERIA-DEV.md" >&2
fi
