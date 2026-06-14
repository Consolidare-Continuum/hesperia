#!/usr/bin/env bash
# alunel — clone Hesperia canonical repo (if missing) + venv + requirements (run as igareosh).
# Does not create .env or pip install -e . (use PYTHONPATH — see cluster/alunel/HESPERIA-DEV.md).
set -euo pipefail
REPO_DIR="${HESPERIA_REPO:-/data/workspaces/atomic-commit-hesperia}"
PY312="${HOME}/.pyenv/versions/3.12.8/bin/python3.12"
SSH_KEY="${GIT_SSH_KEY:-$HOME/.ssh/github_key}"

if [ "$(id -u)" -eq 0 ]; then
  echo "FAIL: run as igareosh, not root." >&2
  exit 1
fi

if [ ! -x "$PY312" ]; then
  echo "FAIL: missing $PY312 — run scripts/alunel-python/02-install-pyenv-and-runtimes.sh" >&2
  exit 1
fi

sudo mkdir -p /data/workspaces
sudo chown "$(id -un):$(id -gn)" /data/workspaces

if [ ! -d "$REPO_DIR/.git" ]; then
  GIT_SSH_COMMAND="ssh -i ${SSH_KEY} -o IdentitiesOnly=yes" \
    git clone git@github.com:Atomic-Commits-Team/hesperia.git "$REPO_DIR"
fi

if [ ! -x "$REPO_DIR/.venv/bin/python3" ]; then
  "$PY312" -m venv "$REPO_DIR/.venv"
fi
"$REPO_DIR/.venv/bin/pip" install -U pip
"$REPO_DIR/.venv/bin/pip" install -r "$REPO_DIR/requirements.txt"

echo "OK: $REPO_DIR — source scripts/alunel-hesperia-dev-env.sh before python -m hesperia.run …"
