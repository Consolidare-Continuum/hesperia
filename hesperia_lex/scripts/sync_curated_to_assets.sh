#!/usr/bin/env bash
# Copy validated curated Dict A/B to hesperia/assets/. Run after validate_lexical.py.
set -e
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
LEX_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
HESPERIA_ROOT="$(cd "$LEX_ROOT/.." && pwd)"
ASSETS="$HESPERIA_ROOT/assets"
mkdir -p "$ASSETS"
for f in A_CORE_STAR_MAP_v1.json B_SURFACE_LEX_FIELD_v1.json; do
  if [ -f "$LEX_ROOT/curated/$f" ]; then
    cp "$LEX_ROOT/curated/$f" "$ASSETS/$f"
    echo "Copied $f to $ASSETS"
  fi
done
