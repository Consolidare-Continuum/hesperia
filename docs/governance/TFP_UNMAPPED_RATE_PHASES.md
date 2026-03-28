# TFP unmapped token rate — phased caps

**Metric:** `compute_lexical_unmapped_token_rate` (tokens with no overlap vs accepted dict_a spans).

| Phase | Default cap | Role |
|-------|-------------|------|
| 2 (CI baseline) | **`HESPERIA_REL_REAL_UNMAPPED_RATE_MAX=0.65`** | Meaningful gate; corpus `tests/fixtures/tfp_rel_real_corpus.txt` must pass |
| 3 (production) | **&lt; 0.40** (domain-dependent) | Ethan / Grace waiver if corpus requires |

Phase 1 (0.95) was mechanism-only and is **retired** as default.

---

`SIGNED: Grace packet TFP-TIGHT-01 | 2026-03-28`
