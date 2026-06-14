#!/usr/bin/env bash
# Hesperia: one repo at /data/hesperia. Move prichindel + sphere as subdirs; remove their .git; init single repo.
# Prichindel cluster has no involvement. CONFIRM before running.
# Usage: ./move-to-hesperia.sh [--dry-run]

set -euo pipefail
DRY_RUN=false
[[ "${1:-}" == "--dry-run" ]] && DRY_RUN=true

SOURCE_PRICHINDEL="${SOURCE_PRICHINDEL:-/home/igareosh/prichindel}"
SOURCE_SPHERE="${SOURCE_SPHERE:-/home/igareosh/sphere}"
DEST="${DEST:-/data/hesperia}"

echo "Hesperia single repo at $DEST"
echo "Source prichindel: $SOURCE_PRICHINDEL"
echo "Source sphere:     $SOURCE_SPHERE"
echo "Dry run:           $DRY_RUN"
echo "---"
if [[ "$DRY_RUN" == true ]]; then
  echo "[dry-run] Would: mkdir $DEST, mv prichindel and sphere (strip .git), git init at $DEST."
  exit 0
fi

if [[ ! -d "$DEST" ]]; then
  if mkdir -p "$DEST" 2>/dev/null; then
    echo "[+] Created $DEST"
  else
    echo "Create $DEST (e.g. sudo mkdir -p $DEST && sudo chown \$USER \$DEST), then re-run."
    exit 1
  fi
fi

# Move prichindel (drop .git for single repo)
if [[ -d "$SOURCE_PRICHINDEL" ]] && [[ ! -d "$DEST/prichindel" ]]; then
  mv "$SOURCE_PRICHINDEL" "$DEST/"
  rm -rf "$DEST/prichindel/.git"
  echo "[+] Moved prichindel/ (deprecated .git removed)"
elif [[ -d "$DEST/prichindel" ]]; then
  rm -rf "$DEST/prichindel/.git" 2>/dev/null || true
  echo "[!] $DEST/prichindel exists; ensured no .git."
else
  echo "[!] Source $SOURCE_PRICHINDEL not found."
fi

# Move sphere (drop .git)
if [[ -d "$SOURCE_SPHERE" ]] && [[ ! -d "$DEST/sphere" ]]; then
  mv "$SOURCE_SPHERE" "$DEST/"
  rm -rf "$DEST/sphere/.git"
  echo "[+] Moved sphere/ (deprecated .git removed)"
elif [[ -d "$DEST/sphere" ]]; then
  rm -rf "$DEST/sphere/.git" 2>/dev/null || true
  echo "[!] $DEST/sphere exists; ensured no .git."
else
  echo "[!] Source $SOURCE_SPHERE not found."
fi

# One repo at /data/hesperia
if [[ ! -d "$DEST/.git" ]]; then
  (cd "$DEST" && git init)
  echo "[+] git init at $DEST"
fi

echo "[+] Done. Add remote: git -C $DEST remote add origin <hesperia-github-url>; then commit, push. Open workspace $DEST."
