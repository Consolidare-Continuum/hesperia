#!/usr/bin/env bash
# Sync Upcelerator participation materials into Hesperia docs (reference only; non-binding).
# Operator source of truth on LAMAITA: C:\Users\igare\OneDrive\Desktop\UPCELERATOR
# Staging on alunel: /data/hesperia/Upcelerator2026 (refresh from Desktop before run).
set -euo pipefail
SRC=/data/hesperia/Upcelerator2026
DEV=/data/workspaces/atomic-commit-hesperia/docs/reference/upcelerator2026
DEST=/data/hesperia/hesperia/docs/reference/upcelerator2026
mkdir -p "$DEV" "$DEST"
for f in \
  Assignment-1_Motivation-Vision-Mission.docx \
  Assignment-2A_Business-Model-Canvas.pptx \
  Assignment-2B1_Market-Definition.txt \
  Assignment-2B2_Market-Size.txt \
  Assignment-2B3_PESTLE-Analysis.txt \
  Assignment-2C1_Competitors-Description.txt \
  Assignment-2C2_Competitors-Grading.xlsx \
  Assignment-2C3_Competitors-Detailed-Analysis.txt \
  Assignment-2C4_Competitive-Advantage.txt \
  Assignment-2D_Pitch-Deck.pptx \
  Assignment-2D_Pitch-Deck-Script.txt; do
  cp -a "$SRC/$f" "$DEV/"
  cp -a "$SRC/$f" "$DEST/"
done
rm -rf "$DEV/more" "$DEST/more"
cp -a "$SRC/more" "$DEV/more"
cp -a "$SRC/more" "$DEST/"
for md in README.md PARTICIPATION-INSIGHTS.md; do
  [ -f "$DEV/$md" ] && cp -a "$DEV/$md" "$DEST/$md"
done
echo "OK: dev=$DEV data=$DEST ($(find "$DEV" -type f | wc -l) files)"
