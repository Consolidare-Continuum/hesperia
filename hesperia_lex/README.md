# HESPERIA lexical stack (v0.3)

Controlled lexical authority layer for Dict A (core star map) and Dict B (surface lex field).
**No scraping. No gray zone.** Raw sources immutable; all updates version-bumped and CI-validated.

## Structure

```
hesperia_lex/
├── raw/           # Immutable downloads (WordNet, SCOWL, Wiktionary)
├── processed/     # Machine-usable JSON from preprocessing
├── curated/       # A_CORE_STAR_MAP, B_SURFACE_LEX_FIELD, checksums
├── logs/          # Run logs
├── scripts/       # download_sources.sh, preprocess_*.py, validate_lexical.py, sync_curated_to_assets.sh, ci_lexical.sh, ingest_lexical_to_chroma.py
└── README.md
```

**Download/install** (raw, processed, assets are gitignored): see [INSTALL-LEXICAL.md](INSTALL-LEXICAL.md).

## Commands

| Step | Command |
|------|--------|
| Phase 1 | `bash hesperia_lex/scripts/download_sources.sh` |
| Phase 2 | `python3 hesperia_lex/scripts/preprocess_oewn.py` (+ preprocess_scowl.py, preprocess_wiktionary.py) |
| Phase 5 | `python3 hesperia_lex/scripts/validate_lexical.py --curated hesperia_lex/curated` |
| Sync to assets | `bash hesperia_lex/scripts/sync_curated_to_assets.sh` |
| CI | `bash hesperia_lex/scripts/ci_lexical.sh` (from hesperia root) |
| Chroma ingest | `CHROMA_SERVER_URL=... python3 hesperia_lex/scripts/ingest_lexical_to_chroma.py` (Abelard when stack updated) |

## Integration

- **assets/** (hesperia root): A_CORE_STAR_MAP_v1.json, B_SURFACE_LEX_FIELD_v1.json.
- **sphere_rag/lexical_loader.py**: `load_dict_a()`, `load_dict_b()`, `load_and_validate()` — Spec 20, no hot reload.
- **Chroma**: layer=hesperia_lex (ingest via ingest_lexical_to_chroma.py).

## Phases

- **Phase 0** — Workspace (this structure).
- **Phase 1** — Download: Open English WordNet, SCOWL, Wiktionary dump.
- **Phase 2** — Preprocess: OEWN → synsets, SCOWL → tiers, Wiktionary → lemmas.
- **Phase 3** — Dict A: manual + assisted → A_CORE_STAR_MAP_v1.json.
- **Phase 4** — Dict B: B_SURFACE_LEX_FIELD_v1.json (alias grades A/B/C).
- **Phase 5** — Validation: side_id in 72k/432k set, no family/area in A, checksums.
- **Phase 6** — Integration: assets/ in hesperia, loader with Spec 20 validation.
- **Phase 7** — CI: schema, invariants, books-off A/B.
- **Phase 8** — Freeze: tag, version record, no automatic updates.

Ref: 19_SPEC (Two-Dictionary Lexical), 20_SPEC (Authority Separation), 22_SPEC (Core Math Contract).
