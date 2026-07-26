#!/usr/bin/env bash
# Run ON prichindel. Backs up dev .md to dev repo via rsync over SSH, then deletes from prod.
set -euo pipefail

PROD="${PROD_ROOT:-/data/hesperia/hesperia}"
DEV_HOST="${DEV_HOST:-alunel}"
DEV_ROOT="${DEV_ROOT:-/data/workspaces/atomic-commit-hesperia}"
BACKUP="docs/backup/prod-immaculate-2026-05-18"
GIT="-c user.email=igareosh@igareosh.com -c user.name=igareosh"

is_allowed_md() {
  local f="${1#./}"
  case "$f" in
    README.md|LEGAL_NOTICE.md) return 0 ;;
    tests/fixtures/dict_calibration/corpus/sample.md) return 0 ;;
    hesperia/modules/tfp/data/corpus/*) return 0 ;;
    hesperia/modules/tfp/data/tfp_v1/corpus/*) return 0 ;;
    hesperia/modules/tfp/data/tfp_v1/inspector_exports/*) return 0 ;;
  esac
  [[ "$f" == hesperia/modules/tfp/data/*/corpus/* ]] && return 0
  return 1
}

cd "$PROD"
mapfile -t REMOVE < <(
  find . -name '*.md' ! -path './.git/*' ! -path './.pytest_cache/*' 2>/dev/null | while read -r f; do
    is_allowed_md "$f" || echo "$f"
  done
)

echo "Removable md files: ${#REMOVE[@]}"
[[ ${#REMOVE[@]} -gt 0 ]] && printf '  %s\n' "${REMOVE[@]}"

if [[ ${#REMOVE[@]} -gt 0 ]]; then
  TMP=$(mktemp -d)
  for f in "${REMOVE[@]}"; do
    [[ -f "$f" ]] || continue
    mkdir -p "$TMP/$(dirname "$f")"
    cp -a "$f" "$TMP/$f"
  done
  printf '%s\n' "${REMOVE[@]}" > "$TMP/MANIFEST.txt"
  tar -C "$TMP" -czf /tmp/prod-immaculate-backup.tar.gz .
  rsync -az /tmp/prod-immaculate-backup.tar.gz "${DEV_HOST}:${DEV_ROOT}/"
  ssh "$DEV_HOST" "bash -s" <<REMOTE
set -euo pipefail
cd "$DEV_ROOT"
mkdir -p "$BACKUP"
tar -xzf prod-immaculate-backup.tar.gz -C "$BACKUP"
rm -f prod-immaculate-backup.tar.gz
git $GIT add "$BACKUP"
git $GIT commit -m "docs(dev): backup prod dev-notes before immaculate sweep (${#REMOVE[@]} files)"
git $GIT push dev main
echo "dev pushed: \$(git rev-parse --short HEAD)"
REMOTE
  rm -rf "$TMP" /tmp/prod-immaculate-backup.tar.gz

  for f in "${REMOVE[@]}"; do rm -f "$f"; done
fi

grep -q '^outputs/\*\*/\*\.md$' .gitignore 2>/dev/null || printf '\noutputs/**/*.md\n' >> .gitignore
git ls-files 'outputs/**/*.md' 2>/dev/null | while read -r f; do git rm -f --cached "$f" 2>/dev/null || true; done

scp -q tools/ci/verify_prod_code_only.sh "${PROD}/tools/ci/" 2>/dev/null || true
cp /data/altitudine/prichindel.com/scripts/verify-hesperia-prod-code-only.sh tools/ci/verify_prod_code_only.sh 2>/dev/null || true

if git status --porcelain | grep -q .; then
  git $GIT add -A
  git $GIT commit -m "chore(prod): immaculate sweep — dev notes removed (backup on igareosh/hesperia)"
  git $GIT push origin main
fi

chmod +x tools/ci/verify_prod_code_only.sh
git $GIT add tools/ci/verify_prod_code_only.sh
git $GIT diff --cached --quiet || git $GIT commit -m "ci(prod): immaculate verifier (corpus md allowlist only)"
git $GIT push origin main

bash tools/ci/verify_prod_code_only.sh .
echo "prod HEAD: $(git rev-parse --short HEAD)"
