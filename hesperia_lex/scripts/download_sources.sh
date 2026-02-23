#!/usr/bin/env bash
# Phase 1 — Download lexical sources. Run from hesperia_lex/ (or pass LEX_ROOT).
# No scraping. Direct, legal download URLs only.

set -e
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
LEX_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
RAW="$LEX_ROOT/raw"
mkdir -p "$RAW"
cd "$RAW"

echo "Lexical raw dir: $RAW"

# 1) Open English WordNet (OEWN) — json.gz preferred
# Latest release URL; adjust version from https://github.com/globalwordnet/english-wordnet/releases
OEWN_JSON="english-wordnet-2023.json.gz"
OEWN_URL="${OEWN_URL:-https://github.com/globalwordnet/english-wordnet/releases/download/v2023.1/english-wordnet-2023.json.gz}"
if [ ! -f "$OEWN_JSON" ] && [ ! -f "${OEWN_JSON%.gz}" ]; then
  echo "Downloading Open English WordNet (json)..."
  wget -q --show-progress -O "$OEWN_JSON" "$OEWN_URL" || true
  [ -f "$OEWN_JSON" ] && gunzip -k -f "$OEWN_JSON" 2>/dev/null || true
fi

# 2) SCOWL
SCOWL_TAR="scowl-2020.12.07.tar.gz"
SCOWL_URL="${SCOWL_URL:-http://wordlist.aspell.net/scowl-2020.12.07.tar.gz}"
if [ ! -f "$SCOWL_TAR" ] && [ ! -d "scowl-2020.12.07" ]; then
  echo "Downloading SCOWL..."
  wget -q --show-progress -O "$SCOWL_TAR" "$SCOWL_URL" || true
  [ -f "$SCOWL_TAR" ] && tar -xzf "$SCOWL_TAR" || true
fi

# 3) Wiktionary dump (large)
WIKT_BZ2="enwiktionary-latest-pages-articles.xml.bz2"
WIKT_URL="${WIKT_URL:-https://dumps.wikimedia.org/enwiktionary/latest/enwiktionary-latest-pages-articles.xml.bz2}"
if [ ! -f "$WIKT_BZ2" ] && [ ! -f "${WIKT_BZ2%.bz2}" ]; then
  echo "Downloading Wiktionary dump (optional, large)..."
  wget -q --show-progress -O "$WIKT_BZ2" "$WIKT_URL" || true
  [ -f "$WIKT_BZ2" ] && bunzip2 -k -f "$WIKT_BZ2" 2>/dev/null || true
fi

echo "Phase 1 done. Raw files in $RAW"
