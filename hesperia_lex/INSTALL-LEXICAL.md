# Download, install, and ingest lexical dicts (Hesperia)

**Separation**

- **Runtime install** (required for v0.3): Curated Dict A/B only. Sync to `assets/` so the engine can start. No raw downloads needed.
- **Lexical rebuild** (optional): OEWN, SCOWL, Wiktionary. Only needed if you are rebuilding or extending the lexical stack from sources. Not required for running the engine.

**Gitignored** (not pushed): `raw/`, `processed/`, `assets/`. Curated A/B may be in repo (small).

---

## Runtime install (required for engine)

Production runtime depends on **assets/** being populated. If `assets/A_CORE_STAR_MAP_v1.json` or `assets/B_SURFACE_LEX_FIELD_v1.json` is missing, the loader fails startup with: *Run sync_curated_to_assets.sh*.

1. Ensure curated A/B exist in `hesperia_lex/curated/` (in repo or restored).
2. Validate and sync:

```bash
cd CLIENTS/hesperia
bash hesperia_lex/scripts/ci_lexical.sh
bash hesperia_lex/scripts/sync_curated_to_assets.sh
```

3. (Optional) Ingest to Chroma: see § Chroma ingest below.

**Required for v0.3 lexical stack:** Curated A/B only. No OEWN/SCOWL/Wiktionary for runtime.

---

## Lexical rebuild (optional)

Only if you are rebuilding or extending Dict A/B from raw sources.

### Download raw sources (all optional)

- **OEWN** — Open English WordNet (for synsets / lemma building).
- **SCOWL** — word lists (for tiers).
- **Wiktionary** — dump (large); for lemma/definition hints.

```bash
bash CLIENTS/hesperia/hesperia_lex/scripts/download_sources.sh
```

- Puts files in `hesperia_lex/raw/`. Wiktionary is large (~400MB+); to skip: `WIKT_URL=""` or remove the wget block.
- Override URLs: `OEWN_URL=...`, `SCOWL_URL=...`, `WIKT_URL=...`.

### Preprocess

```bash
cd CLIENTS/hesperia
python3 hesperia_lex/scripts/preprocess_oewn.py
python3 hesperia_lex/scripts/preprocess_scowl.py
# python3 hesperia_lex/scripts/preprocess_wiktionary.py  # optional, heavy
```

Output in `hesperia_lex/processed/`. Then curate A/B into `hesperia_lex/curated/` and run validate + sync as in § Runtime install.

---

## Chroma ingest

Chroma: books + lexical (Dict A/B). Topology (membership/adjacency) is **not** in Chroma for current runs; traversal uses stub. See TOPOLOGY-STORAGE-CONTRACT.md.

- **Dev**: If `CHROMA_SERVER_URL` unset or chromadb not installed → script skips ingest, exit 0.
- **CI/prod**: Use `--strict` → fail non-zero if Chroma not reachable or chromadb missing.

```bash
cd CLIENTS/hesperia
export CHROMA_SERVER_URL=http://HOST:8002
python3 hesperia_lex/scripts/ingest_lexical_to_chroma.py [--strict]
```

Requires `pip install chromadb` and a running Chroma server for ingest.

---

## Reference

- **Curated** source of truth: `hesperia_lex/curated/A_CORE_STAR_MAP_v1.json`, `B_SURFACE_LEX_FIELD_v1.json`.
- **Loader**: `sphere_rag/lexical_loader.py` reads from `hesperia/assets/` (after sync). Fails startup if assets missing.
- **Topology**: TOPOLOGY-STORAGE-CONTRACT.md. Chroma run = stub traversal + Chroma books validation; topology-from-Chroma when membership/adjacency are ingested.
