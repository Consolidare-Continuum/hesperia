#!/usr/bin/env bash
# Ingest HESPERIA academic theory pack into CHROMA-1 (layer=project, project_name=hesperia_study_theory).
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
THEORY="${ROOT}/user_documents/hesperia_study_research_and aplication_romanian/theory"
export CHROMA_SERVER_URL="${CHROMA_SERVER_URL:-http://chroma-1.prichindel.local:8002}"
PY="${CHROMA_PYTHON:-/data/chroma/venv/bin/python}"
if [[ ! -d "$THEORY" ]]; then
  echo "ERROR: theory dir missing: $THEORY" >&2
  exit 1
fi
export PYTHONPATH="${ROOT}"
exec "$PY" "${ROOT}/cluster/chroma-server/ingest_project_repo.py" hesperia_study_theory "$THEORY"
