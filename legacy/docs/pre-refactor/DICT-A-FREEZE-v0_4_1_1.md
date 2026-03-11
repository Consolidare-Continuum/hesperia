# Historical reference (pre-refactor)

# Dict A freeze v0.4.1.1 (semantic)

**Tag**: `v0.4.1.1-semantic-freeze`  
**Frozen file**: `hesperia_lex/frozen/A_CORE_STAR_MAP_v0_4_1_1.json`  
**Checksum**: `hesperia_lex/frozen/A_CORE_STAR_MAP_v0_4_1_1.json.sha256`

## Freeze conditions (satisfied)

- 288/288 families covered
- ≥8 real semantic anchors per family (≤4 structural)
- ≥3 weight tiers per family
- Label anchors ≤4 per family
- κ PASS
- Determinism verified (two full builds)
- Semantic density report: `assets/v0411/semantic_density_report.txt`

## Build command

```bash
cd CLIENTS/hesperia
.venv_v040/bin/python -m sphere_rag.build_v040 \
  --dict-a hesperia_lex/curated/A_CORE_STAR_MAP_v0_4_1_1.json \
  --assets-root hesperia_lex/curated \
  --out-dir assets/v0411 \
  --mode balanced
```

## Source

- Curated semantic pools: `hesperia_lex/scripts/build_dict_a_v0411_semantic.py`
- Base: v0.4.1-dictA-freeze (frozen file immutable)
- Output: `hesperia_lex/curated/A_CORE_STAR_MAP_v0_4_1_1.json` then copied to frozen

## Post-freeze

Same policy as v0.4.1: no anchor deletion in v0.4.x; additions via new minor version, full rebuild + gates + κ.
