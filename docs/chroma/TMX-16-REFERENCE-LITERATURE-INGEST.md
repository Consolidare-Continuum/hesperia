# TMX-16: Chroma ingest path for reference literature

**Owner**: Abelard  
**Layer**: `reference_literature` (new; complements `tfp_corpus_ru`, `operational`, `books`)  
**Status**: 2026-05-11 — runbook + config documented. Corpus not yet ingested (no source path designated).

---

## Purpose

Ingest reference literature (academic papers, clinical guidelines, methodology sources) into Chroma with layer metadata, aligned with existing TFP corpus triage policy.

## Layer metadata spec

| Field | Value |
|-------|-------|
| `layer` | `reference_literature` |
| `corpus_pack` | source collection identifier (e.g. `clinical_refs_2026`) |
| `source` | filename (relative path from corpus root) |
| `language` | `ru` or `en` |
| `doc_type` | `paper` \| `guideline` \| `methodology` \| `other` |

## Ingest procedure (Abelard)

```bash
# 1. Set source path
export REF_LIT_PATH=/data/hesperia/reference_literature   # designate when corpus ready

# 2. Set Chroma target
export CHROMA_SERVER_URL=http://127.0.0.1:8002

# 3. Run ingest (adapt ingest_tfp_corpus_ru.py or ingest_books.py pattern)
LAYER=reference_literature \
CORPUS_PACK=clinical_refs_2026 \
python3 cluster/chroma-server/ingest_books_general.py "$REF_LIT_PATH"

# 4. Verify
python3 -c "
import chromadb
c = chromadb.HttpClient(host='localhost', port=8002)
col = c.get_collection('knowledge')
res = col.get(where={'layer': 'reference_literature'}, limit=3, include=['metadatas'])
print(f'Count check: {len(res[\"metadatas\"])} docs sampled')
for m in res['metadatas']: print(m)
"
```

## ACL (chroma-policy.json)

Add to `cluster/trustmaster/imirc-mcp-host/chroma-policy.json`:
```json
"#agents-ingest": ["operational", "reference_literature"],
"#agents-ops":    ["operational", "books", "reference_literature"]
```

## Alignment with TFP triage

- TFP corpus triage: `tfp_corpus_ru` layer (14987 chunks, 94 files, ingested 2026-04-07 into chroma-old; **not yet in chroma-new**)
- Reference literature: new layer, separate corpus pack; do not mix with TFP chunks
- Chunk size: 1200 chars max (same as TFP)
- Delete guard: `SKIP_REF_DELETE=1` on add-only passes

## Blocker

`tfp_corpus_ru` not yet ingested into `chroma-new` (port 8002). Both layers should be migrated / re-ingested together when the corpus source path is confirmed. Ref: `cluster/chroma-server/ingest-tfp-corpus-ru.sh`.

SIGNED: DevOps (Abelard) | Hesperia TMX-16 Chroma ingest path | 2026-05-11 | reference_literature layer
