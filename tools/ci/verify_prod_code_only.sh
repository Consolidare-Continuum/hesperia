#!/usr/bin/env bash
# Verify Hesperia prod clone has no forbidden documentation/chat paths.
# Policy: governance/ETHAN-POLICY-HESPERIA-DEV-PROD-CONTENT.md
set -euo pipefail

ROOT="${1:-/data/hesperia/hesperia}"
if [[ ! -d "$ROOT" ]]; then
  echo "FAIL: not a directory: $ROOT" >&2
  exit 1
fi

cd "$ROOT"
FAIL=0

check_path() {
  local p="$1"
  if [[ -e "$p" ]]; then
    echo "FORBIDDEN: $p"
    FAIL=1
  fi
}

check_path ".cursor"
check_path "docs"
check_path "_release_tmp"
check_path "AGENTS.md"
check_path "ROLLBACK-LINE-2026-05-18.md"
check_path "task_gena_v0_6_0.md"
check_path "REPO_STRUCTURE_POLICY.md"
check_path "GENERATED_ARTIFACT_POLICY.md"
check_path "docs/governance"
# research/ may contain Python; reference markdown belongs on dev
while IFS= read -r f; do
  [[ -z "$f" ]] && continue
  echo "FORBIDDEN: $f"
  FAIL=1
done < <(find research -name '*.md' -type f 2>/dev/null)

# Runtime / tools narrative markdown (deploy prose lives on igareosh/hesperia)
while IFS= read -r f; do
  [[ -z "$f" ]] && continue
  echo "FORBIDDEN: $f"
  FAIL=1
done < <(find runtime tools \( -name 'README.md' -o -name 'GPT-ACTIONS-SETUP.md' -o -name 'README_ACTIONS.md' \) 2>/dev/null)

for f in CURSOR_OPEN_WORKFLOW.md CURSOR_REPORT_7_TASKS_GENA.md CURSOR_REPO_AND_RELEASE_BEST_PRACTICES.md; do
  check_path "docs/$f"
done

# Root narrative md except minimal legal
while IFS= read -r -d '' f; do
  base="$(basename "$f")"
  case "$base" in
    LICENSE|LEGAL_NOTICE.md) continue ;;
    README.md)
      lines=$(wc -l <"$f" 2>/dev/null || echo 0)
      if [[ "$lines" -gt 15 ]]; then
        echo "FORBIDDEN: README.md too long ($lines lines); prod pointer only"
        FAIL=1
      fi
      continue
      ;;
  esac
  if [[ "$f" == ./*/*.md ]] && [[ "$(dirname "$f")" == "." ]]; then
    echo "FORBIDDEN: root markdown $f"
    FAIL=1
  fi
done < <(find . -maxdepth 1 -name '*.md' -print0 2>/dev/null)

if [[ "$FAIL" -ne 0 ]]; then
  echo "verify-hesperia-prod-code-only: FAIL ($ROOT)"
  exit 1
fi

echo "verify-hesperia-prod-code-only: OK ($ROOT)"
exit 0
