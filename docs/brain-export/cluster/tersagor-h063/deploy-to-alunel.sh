#!/usr/bin/env bash
# Deploy H063 tersagor patch from brain repo to alunel workspace.
set -euo pipefail
SRC="${1:-/data/workspaces/cursor/cluster/tersagor-h063}"
DEST="${2:-/data/workspaces/tersagor}"
cp -a "$SRC/schemas/"*.json "$DEST/schemas/"
cp -a "$SRC/src/tersagor_agent/hesperia/"*.py "$DEST/src/tersagor_agent/hesperia/"
cp -a "$SRC/tests/test_irc_teacher_v063.py" "$DEST/tests/"
# version_registry flags
python3 << 'PY'
from pathlib import Path
p = Path("$DEST/src/tersagor_agent/hesperia/version_registry.py")
PY
echo "H063 deploy: schemas + modules + tests copied to $DEST"
