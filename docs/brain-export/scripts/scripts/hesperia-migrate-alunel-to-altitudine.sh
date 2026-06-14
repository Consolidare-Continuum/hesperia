#!/usr/bin/env bash
# One-time: migrate /data/hesperia from alunel hypervisor → altitudine VM (holy cow policy).
# Ref: governance/ALUNEL-HOLY-COW-POLICY.md, cluster/altitudine/HESPERIA-DEV.md
set -euo pipefail
REPO_ROOT="${REPO_ROOT:-$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)}"
APPLY=0
while [[ $# -gt 0 ]]; do
  case "$1" in
    --apply) APPLY=1; shift ;;
    -h|--help)
      echo "Usage: $0 [--apply]"
      echo "  Dry-run rsync alunel:/data/hesperia → altitudine:/data/hesperia; --apply executes + tombstones alunel tree."
      exit 0
      ;;
    *) echo "Unknown: $1" >&2; exit 2 ;;
  esac
done

RSYNC_FLAGS=(-aH --info=stats2)
[[ $APPLY -eq 0 ]] && RSYNC_FLAGS+=(--dry-run)

echo "=== Hesperia data root migration (alunel hypervisor → altitudine VM) ==="
ssh altitudine 'sudo mkdir -p /data/hesperia && sudo chown igareosh:igareosh /data/hesperia'

echo "Source: alunel:/data/hesperia/"
echo "Target: altitudine:/data/hesperia/"
ssh alunel "rsync ${RSYNC_FLAGS[*]} /data/hesperia/ altitudine:/data/hesperia/"

if [[ $APPLY -eq 0 ]]; then
  echo "DRY_RUN complete. Re-run with --apply to execute and tombstone alunel tree."
  exit 0
fi

echo "Verify on altitudine..."
ssh altitudine 'test -d /data/hesperia/hesperia/.venv && /data/hesperia/hesperia/.venv/bin/python --version'

TOMB="/data/hesperia.migrated-to-altitudine-$(date +%Y%m%d)"
echo "Tombstone alunel: mv /data/hesperia → $TOMB"
ssh alunel "sudo mv /data/hesperia $TOMB && sudo mkdir -p /data/hesperia && sudo chown igareosh:igareosh /data/hesperia"
ssh alunel "echo 'Migrated to altitudine:/data/hesperia on $(date -Iseconds). Do not restore dev here — holy cow policy.' | sudo tee /data/hesperia/README_MIGRATED.txt"

echo "Install analyze dev unit on altitudine (not hypervisor)..."
ssh altitudine "sudo cp $REPO_ROOT/cluster/alunel/systemd/hesperia-analyze-dev.service /etc/systemd/system/ 2>/dev/null || sudo cp /data/altitudine/prichindel.com/cluster/alunel/systemd/hesperia-analyze-dev.service /etc/systemd/system/"
ssh altitudine 'sudo systemctl daemon-reload && sudo systemctl enable --now hesperia-analyze-dev.service && systemctl is-active hesperia-analyze-dev'

echo "Holy cow audit on alunel..."
ssh alunel "cd /data/workspaces/cursor && bash scripts/alunel-holy-cow-audit.sh --local" || true

echo "DONE. Dev root: altitudine:/data/hesperia/hesperia"
