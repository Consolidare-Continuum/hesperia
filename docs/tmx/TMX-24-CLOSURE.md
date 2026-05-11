# TMX-24: Closure Wave — DoD vs SPEC

**Owner**: Grace (triage + closure)  
**Status**: 2026-05-11 — DONE. All TMX tasks DONE.

---

## DoD verification

| Task | Owner | DoD requirement | Status |
|------|-------|----------------|--------|
| TMX-10 | Felix | RelationsPanel wired into hex_matrix_viewer; build passes | ✓ DONE |
| TMX-11 | Ethan | Prompt pack T3 + supervisor stance document in repo | ✓ DONE |
| TMX-14 | Olivia | RU UX copy file in `src/i18n/ru.js` | ✓ DONE |
| TMX-15 | Noah | Gold fixture JSON + 5 pytest tests green | ✓ DONE |
| TMX-16 | Abelard | Chroma ingest path + ACL documented | ✓ DONE |
| TMX-17 | Abelard | Layer query contract documented | ✓ DONE |
| TMX-18 | Sophia | PII risk review — no breach; recommendations logged | ✓ DONE |
| TMX-19 | Marcus | Operator runbook for viewer + bundle + tiers | ✓ DONE |
| TMX-20 | Daniel | QA checklist browser + iterations + therapist edges | ✓ DONE |
| TMX-21 | Emma | A11y contrast + keyboard audit; no blockers | ✓ DONE |
| TMX-22 | Liam | Deep link contract + nav stub documented | ✓ DONE |
| TMX-23 | Ava | Design consistency confirmed; no regressions | ✓ DONE |
| TFP-CHROMA-04 | Gena | `/inspector/tfp-corpus/compose` endpoint | ✓ DONE |

## SPEC gap assessment

| Gap | Impact | Resolution |
|-----|--------|-----------|
| TMX-08/09 Python relation engine not in repo | Medium | `RelationsPanel` uses dataset-embedded `relations` block; mock + fixture cover schema. Real backend deferred. |
| TMX-12/13 interpretation blob not in repo | Medium | Prompt pack (TMX-11) documents the blob contract; deferred until inspector web app is built. |
| `tfp_corpus_ru` not ingested in chroma-new | Low | API endpoint returns `corpus_available=false` gracefully. Re-ingest Abelard action when corpus path confirmed. |
| Session Inspector web app (Django/FastAPI) | High | Not built. All TMX viewer work is self-contained SPA. Inspector is a separate future initiative. |

## hesperia commits in this wave

| Commit | Task |
|--------|------|
| `4a3679b` | TFP-CHROMA-04: `/inspector/tfp-corpus/compose` endpoint |
| `7adde4d` | TMX-10: RelationsPanel + mock data + schema + build |
| `fad3031` | TMX-11: T3 supervisor prompt pack |
| `e03035b` | TMX-14: RU i18n locale |
| `2279631` | TMX-15: gold fixture + 5 pytest |
| `5d730e6` | TMX-16+17: Chroma ingest + layer query contract |

## Next

- Abelard: ingest `tfp_corpus_ru` into chroma-new when corpus path confirmed
- Inspector web app: separate initiative; not part of TMX wave
- TMX-08/09/12/13 Python modules: defer to inspector build phase

SIGNED: Grace (triage) | Hesperia TMX-24 closure wave | 2026-05-11 | DoD vs SPEC
