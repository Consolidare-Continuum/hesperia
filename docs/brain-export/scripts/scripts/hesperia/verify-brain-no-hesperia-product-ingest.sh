#!/usr/bin/env bash
# Brain (cursor) repo must not contain Hesperia product trees or dev-repo ingest.
# Policy: governance/ETHAN-POLICY-HESPERIA-BRAIN-DEV-LINK.md
set -euo pipefail

ROOT="${1:-.}"
cd "$ROOT"
FAIL=0

forbid_path() {
  if [[ -e "$1" ]]; then
    echo "FORBIDDEN: $1 (Hesperia product ingest in brain)"
    FAIL=1
  fi
}

forbid_path "hesperia"
forbid_path "atomic-commit-hesperia"
forbid_path "output_views"
forbid_path "assets/calibration"

# Top-level product markers
for p in pyproject.toml setup.py; do
  if [[ -f "$p" ]] && grep -q 'hesperia' "$p" 2>/dev/null && [[ -d hesperia ]]; then
    : # ok if not actually a product root
  fi
done

if [[ -d hesperia/engine || -d hesperia/modules ]]; then
  echo "FORBIDDEN: hesperia/ looks like product code in brain"
  FAIL=1
fi

# Brain must not be a git submodule of hesperia
if [[ -f .gitmodules ]] && grep -q hesperia .gitmodules 2>/dev/null; then
  echo "FORBIDDEN: .gitmodules references hesperia"
  FAIL=1
fi

if [[ "$FAIL" -ne 0 ]]; then
  echo "verify-brain-no-hesperia-product-ingest: FAIL ($ROOT)"
  exit 1
fi
echo "verify-brain-no-hesperia-product-ingest: OK ($ROOT)"
exit 0
