# TMX-18: Risk Review — PII Parity with Inspector PII Gate on Export

**Owner**: Sophia (risk/security review)  
**Tier**: T3 (research context — no production PII gate exists yet)  
**Status**: 2026-05-11 — risk review completed; no blockers for current TMX wave.

---

## Scope

Timeline Matrix viewer (`output_views/hex_matrix_viewer`) + `/inspector/tfp-corpus/compose` endpoint export surface.

## Current export surface

| Surface | Data exported | PII risk |
|---------|--------------|----------|
| `hex_matrix_viewer` (browser SPA) | Hex state JSON (area_scores, dominance, stability, activation, contradiction) | **None** — all derived numeric scores; no raw text, no session identifiers by default |
| `dataset.relations` | Area drift floats, optional `theme_marker` string | **Low** — theme markers are generated labels, not patient text |
| `dataset.appear_disappear` | Signal labels, frame indices, dominance peaks | **Low** — labels are family/area identifiers, not personal |
| `/inspector/tfp-corpus/compose` | Chroma chunks from `tfp_corpus_ru` (reference corpus) | **None** — corpus is published RU TFP methodology; no patient data |
| `?data=<url>` parameter | Loads external JSON dataset | **Operator responsibility** — if dataset contains session_id with real patient identifiers, operator must strip before exposing |

## PII gate parity assessment

The Session Inspector (if/when it exists as a web app) should enforce a PII gate before exporting any bundle. The TMX viewer currently:
- Does **not** expose raw text from any session
- Does **not** embed patient identifiers in the gold fixture or mock data
- Uses structural numeric features only
- `session_id` field in `/inspector/tfp-corpus/compose` is operator-supplied; no validation that it's anonymized

## Recommendations

1. **session_id**: Add a regex guard in `TfpCorpusComposeBody` to reject IDs matching real date patterns (`\d{1,2}-\d{2}-\d{4}`) if operator requires anonymization. Currently not enforced.
2. **`?data=` URL parameter**: Document in the viewer README that datasets loaded via URL must be anonymized before sharing; no server-side check is possible.
3. **theme_marker strings**: T3 generated labels — confirm they do not leak therapist/patient names in future implementations.
4. **Chroma corpus retrieval**: `tfp_corpus_ru` is a published methodology corpus — no PII. If `reference_literature` layer is added, verify corpus is de-identified before ingest.

## Verdict

**No PII breach in current TMX wave deliverables.** Parity with inspector PII gate: N/A (inspector web app not built). Recommendations logged for when a full inspector is implemented.

SIGNED: Security (Sophia) | Hesperia TMX-18 PII risk review | 2026-05-11 | timeline matrix + compose endpoint
