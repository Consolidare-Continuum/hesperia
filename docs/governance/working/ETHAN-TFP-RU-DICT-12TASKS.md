<!--
Ethan — Russian TFP DLCR dictionary build (12 tasks) — status vs repo.
-->

# Ethan — TFP RU dictionaries (TASK 1–12) — implementation note

**Status:** **PARTIAL SHIP** — scaffold + **starter pack** landed; counts below **targets** require corpus-driven expansion (manual + assisted).  
**Spec alignment:** `task.txt` (DLCR-HP), `schemas/lexical_concept/*`, [ETHAN-TFP-RUNNABLE-DICT-WIRING.md](ETHAN-TFP-RUNNABLE-DICT-WIRING.md).

---

## Locked scope (TASK 1) — files

| Path | Role |
|------|------|
| `dict_a/dict_a_tfp_ru_core.jsonl` | Core **phrase-first** Russian triggers → `TFP_*` |
| `dict_a/dict_a_tfp_ru_variants.jsonl` | Paraphrases / short forms / clue tokens |
| `dict_a/dict_a_tfp_ru_speech.jsonl` | Longer “messy” **pattern** rows (starter) |
| `dict_a/dict_a_tfp_ru_negative.jsonl` | **Blocking** phrases (`negative_patterns`, empty `candidate_concept_ids`) |
| `dict_b/dict_b_tfp.jsonl` | **Appended** `TFP_*` inventory (legacy `B_A10_*` rows retained) |
| `anchors/concept_hex_anchors_tfp.json` | **Extended** with `TFP_*` → `HX-25xx` |
| `corpora/tfp_ru_cleaned_sentences.jsonl` | TASK 2 output (~16k sentences from `research/_noone_local/2_cleaned/`) |
| `corpora/tfp_ru_gold/` | Starter `sample_*.json` (expected concepts) — grow to 20–50 |

**Merge order (pipeline + regression):** `dict_a_seed` → RU four files → `dict_a_tfp.jsonl`. **Dedup:** first wins on `normalized_form` (non-negative); RU layers **override** legacy collisions.

---

## Engine changes

- **`core/lexical/matcher.py`:** `negative_patterns` entries define **blocked spans**; positives overlapping blocks are dropped.
- **`schemas/lexical_concept/dict_a.schema.json`:** `candidate_concept_ids` may be **empty** only with `negative_patterns`.
- **`tools/validate_dict_a.py`:** enforces “empty candidates ⇒ negatives”.
- **`hesperia/engine/lexical_concept/pipeline.py`:** default `dict_a_paths` includes four RU files.
- **`tools/check_dlcr_regression.py`:** `tfp_ru` suite merges the same `dict_a` list.

---

## TASK 2 — corpus cleaner

```bash
python3 tools/build_tfp_ru_corpus_clean.py --write
```

Removes obvious bibliography/OCR-ish lines; lowercases; sentence split. **Review** before using as sole source for gold.

---

## TASK 3–7 — current counts vs targets

| Target (user) | Landed (starter) | Next step |
|---------------|-------------------|-----------|
| Core 100–300 | **33** phrases | Mine `tfp_ru_cleaned_sentences.jsonl` + manuals |
| Variants +200–500 | **66** | Paraphrase pass on high-frequency n-grams |
| Speech layer | **33** | Real transcript clauses only |
| Negatives | **12** | Ambiguity mining (“перенос”, “объект”, …) |
| Dict B 100–150 | **33** `TFP_*` | Split sub-concepts with clinician review |

**Regenerator (idempotent append for Dict B):**

```bash
python3 tools/gen_tfp_ru_dict_pack.py --write   # appends only missing TFP_* concept_ids
```

---

## TASK 11–12 — validation / freeze

```bash
python3 tools/validate_dict_a.py
python3 tools/validate_dict_b_dlcr.py
python3 tools/validate_tfp_ru_pack.py
python3 tools/check_dlcr_regression.py
```

**Version pins:** `assets/data/engine_dynamics_v060/VERSION.yaml` → `dict_a.tfp_ru` / `dict_b.tfp_ru` = **`v0.6.0_ru_tfp`**.

---

## Reality check (user warnings)

| Shortcut | Risk |
|----------|------|
| Auto phrase extract without review | **Garbage** in Dict B (legacy file had bibliography noise — do not repeat) |
| Skip negatives | **Drift** on polysemy (`расщепление атома`, `перенос данных`, …) |
| Skip speech layer | Weak coverage on messy Russian clinical speech |
| Skip gold | **No regression** beyond `gold_tfp_ru.jsonl` span suite |

---

## Related

- [ETHAN-TASK-TXT-DICTIONARY-CONSULT.md](ETHAN-TASK-TXT-DICTIONARY-CONSULT.md)  
- [ETHAN-DLCR-INTEGRATION-RUNBOOK.md](ETHAN-DLCR-INTEGRATION-RUNBOOK.md)
