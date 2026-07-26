#!/usr/bin/env bash
# HESPERIA — Push to origin and backup mirror. Run after significant releases.
# Copyright © 2026 igareosh.com. See LEGAL_NOTICE.md.
#
# Prerequisites:
#   - origin: GitHub main repo (Atomic-Commits-Team/hesperia)
#   - backup: GitHub mirror (igareosh/hesperia-dev-backup, private, no init)
#
# Usage: from repo root, ./tools/push_mirrors.sh

set -e
REPO="$(cd "$(dirname "$0")/.." && pwd)"
cd "$REPO"

echo "=== Push to origin ==="
git push origin main
git push origin --tags

echo ""
echo "=== Push to backup mirror (full mirror: branches, tags, refs) ==="
git push backup --mirror

echo ""
echo "Done. origin + backup mirror updated."
