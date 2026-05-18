#!/usr/bin/env bash
# Verify Hesperia prod clone: no Cursor/Hesperia dev docs, specs, or tasking.
# Corpus (sessions, books, normalization trees) is OUT OF SCOPE — leave as-is.
# Policy: governance/ETHAN-POLICY-HESPERIA-DEV-PROD-CONTENT.md
set -euo pipefail

ROOT="${1:-/data/hesperia/hesperia}"
if [[ ! -d "$ROOT" ]]; then
  echo "FAIL: not a directory: $ROOT" >&2
  exit 1
fi

cd "$ROOT"
FAIL=0

# Product corpus / sealed lexical data — never flag
is_corpus_or_sealed_data() {
  local f="$1"
  case "$f" in
    ./hesperia/modules/tfp/data/*) return 0 ;;
    ./assets/calibration/dicts/*) return 0 ;;
    */corpus/*|*/corpora/*) return 0 ;;
    */dict_a/_raw/*|*/dict_c/*|*/dict_b/*|*/links/*) return 0 ;;
  esac
  return 1
}

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
check_path "legacy"
# specs/ may contain yaml/json config — forbid only markdown under specs/
while IFS= read -r f; do
  [[ -z "$f" ]] && continue
  echo "FORBIDDEN: $f"
  FAIL=1
done < <(find specs -name '*.md' -type f 2>/dev/null)
check_path "AGENTS.md"
check_path "ROLLBACK-LINE-2026-05-18.md"
check_path "task_gena_v0_6_0.md"
check_path "REPO_STRUCTURE_POLICY.md"
check_path "GENERATED_ARTIFACT_POLICY.md"

# Team / Cursor / Hesperia dev markdown outside corpus trees
while IFS= read -r f; do
  [[ -z "$f" ]] && continue
  is_corpus_or_sealed_data "$f" && continue
  case "$f" in
    ./LEGAL_NOTICE.md|./README.md) continue ;;
    ./research/*.md|./research/*/*.md) echo "FORBIDDEN: $f"; FAIL=1 ;;
  esac
done < <(find research -name '*.md' -type f 2>/dev/null)

while IFS= read -r f; do
  [[ -z "$f" ]] && continue
  is_corpus_or_sealed_data "$f" && continue
  echo "FORBIDDEN: $f"
  FAIL=1
done < <(find runtime tools lexicon/build/notes output_views examples/extensions legacy \
  -type f \( -name '*.md' -o -name 'ARCHITECTURE.md' \) 2>/dev/null)

while IFS= read -r f; do
  [[ -z "$f" ]] && continue
  is_corpus_or_sealed_data "$f" && continue
  base="$(basename "$f")"
  case "$base" in
    README.md|*_REPORT*.md|*HANDOFF*|*PROMPT_SNAPSHOT*|RELEASE_NOTES.md|E2E_OUTPUTS.md)
      echo "FORBIDDEN: $f"
      FAIL=1
      ;;
  esac
done < <(find assets release deploy -type f -name '*.md' 2>/dev/null)

while IFS= read -r f; do
  [[ -z "$f" ]] && continue
  is_corpus_or_sealed_data "$f" && continue
  echo "FORBIDDEN: $f"
  FAIL=1
done < <(find tools -type f -name '*.md' 2>/dev/null)

while IFS= read -r f; do
  [[ -z "$f" ]] && continue
  is_corpus_or_sealed_data "$f" && continue
  case "$f" in
    ./hesperia/modules/tfp/README.md|./hesperia/modules/tfp/ENTRYPOINTS.md)
      echo "FORBIDDEN: $f"
      FAIL=1
      ;;
  esac
done < <(find hesperia/ontology -name 'README.md' 2>/dev/null)

# Root narrative md except minimal legal + prod pointer README
while IFS= read -r -d '' f; do
  base="$(basename "$f")"
  case "$base" in
    LICENSE|LEGAL_NOTICE.md) continue ;;
    README.md)
      lines=$(wc -l <"$f" 2>/dev/null || echo 0)
      if [[ "$lines" -gt 15 ]]; then
        echo "FORBIDDEN: README.md too long ($lines lines)"
        FAIL=1
      fi
      continue
      ;;
  esac
  if [[ "$(dirname "$f")" == "." ]]; then
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
