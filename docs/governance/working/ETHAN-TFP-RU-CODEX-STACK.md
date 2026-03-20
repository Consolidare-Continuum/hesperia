<!--
Ethan — alignment with CODEX TASK BUILD__DICT_A_DICT_B_FROM_CORPUS__RU_TFP__V060
-->

# Ethan — RU-TFP dictionary stack (Codex task) — repo implementation

**Driver:** `python3 tools/build_ru_tfp_dictionary_stack.py --write`  
**Report:** `assets/data/engine_dynamics_v060/_build_report.json`  
**Validate:** `python3 tools/validate_tfp_ru_pack.py` · `python3 tools/check_dlcr_regression.py`

**Controlled Dict B expansion (corpus → concepts, capped):**  
`python3 tools/expand_dict_b_tfp_controlled.py` (dry-run) · `python3 tools/expand_dict_b_tfp_controlled.py --write`  
**Report:** `assets/data/engine_dynamics_v060/_dict_b_expansion_report.json`  
**Updates:** `dict_b/dict_b_tfp.jsonl` — appends `TFP_CLUSTER_*` rows; **strips prior `TFP_CLUSTER_*`** on each `--write` for idempotent rebuild.  
**Schema:** `hex_anchor` may be JSON `null` until human assignment (`dict_b.schema.json` allows `string|null`).  
**Aliases:** mapped shorthand ids (`TFP_DEVALUATION`, `TFP_OBJECT_RELATIONS`, …) resolve to sealed `concept_id`s in-tool (`CORPUS_CONCEPT_ALIASES` in `expand_dict_b_tfp_controlled.py`).

**Full build + expansion + inspection artifacts (Codex `RUN__TFP_DICT_BUILD…__V060`):**  
`python3 tools/run_tfp_dict_build_full_artifacts_v060.py --write`  
- Ingest: `research/_noone_local/2_cleaned/` via stack builder.  
- Merges **Dict B** `dict_b_seed.jsonl` → `dict_b_tfp_ru_v060.jsonl` → `dict_b_tfp.jsonl` (first-wins), then runs **expand**.  
- Writes **`assets/data/engine_dynamics_v060/_artifacts/`**: `top_phrases.json`, `sample_core.json`, `sample_speech.json`, `unmapped_entries.json`, `concepts_summary.json`, `concept_examples.json`, `concept_clusters.json`, `rejected_clusters.json`, `negative_matches.json`, `build_summary.json`, `conflicts.json`, `multi_candidate_entries.json`, `weak_core_entries.json`.  
- Flags: `--skip-build` (reuse RAW/ACTIVE), `--skip-expand`, `--artifacts-only` (regenerate `_artifacts/` from disk + `_dict_b_expansion_report.json`).

---

## Principles (spec)

| Rule | Implementation |
|------|----------------|
| RAW ≠ ACTIVE | `dict_a/_raw/*.jsonl` is **not** loaded by `run_dlcr_pipeline`; only promoted files + legacy `dict_a_tfp.jsonl`. |
| No deletion of corpus | Source markdown stays in `research/_noone_local/2_cleaned/`; outputs are additive/overwritten **build artifacts** only. |
| No black-box scores | `confidence_hint` = deterministic function of keyword-root overlap; thresholds are **named constants** in the builder. |
| Dict B seed scope | **`dict_b/dict_b_tfp_ru_v060.jsonl`** — exactly **9** concepts (spec list; `TFP_IDEALIZATION` = idealization defense). Legacy `dict_b_tfp.jsonl` **retained**; merge is first-wins by `concept_id`. |

---

## Phases → paths

| Phase | Output |
|-------|--------|
| 1 Ingest | `corpora/tfp_ru_sentences.jsonl` — `{ "text", "source" }` per line |
| 2 Raw n-grams | `dict_a/_raw/dict_a_ru_full_corpus.jsonl` — freq ≥ `MIN_RAW_FREQ` (default **2**); max **300k** rows, sorted by `(-frequency, normalized_form)` |
| 3 Tagged | `dict_a/_raw/dict_a_ru_full_tagged.jsonl` — adds `class_hint` |
| 4 Dict B | `dict_b/dict_b_tfp_ru_v060.jsonl` |
| 5 Mapped | `dict_a/_raw/dict_a_ru_mapped.jsonl` — `candidate_concept_ids`, `confidence_hint` (non-final audit layer) |
| 6 Promote | `dict_a/dict_a_tfp_ru_{core,variants,speech}.jsonl` |
| 7 Negative | `dict_a/dict_a_tfp_ru_negative.jsonl` |
| 9 Report | `_build_report.json` |

**Schema note:** JSON uses `alt_labels` (not `alt_labels_ru`) to match `dict_b.schema.json`.

---

## Merge order (resolver)

**Dict A:** `dict_a_seed` → **`dict_a_tfp.jsonl` (legacy)** → stack `core` → `variants` → `speech` → `negative`.  
First wins on `normalized_form` so **`gold_tfp_ru` / B_A10** phrases stay stable.

**Dict B:** `dict_b_seed` → **`dict_b_tfp_ru_v060.jsonl`** → `dict_b_tfp.jsonl`.

---

## 10-minute calibration checklist

1. Open `_build_report.json` — sanity on `core_entries` / `variant_entries` / `speech_entries`.  
2. Spot-check `dict_a/_raw/dict_a_ru_mapped.jsonl` for a few high-`frequency` rows — `candidate_concept_ids` sensible?  
3. `python3 tools/validate_tfp_ru_pack.py` — must pass.  
4. `python3 tools/check_dlcr_regression.py` — must pass.  
5. Edit **thresholds** at top of `tools/build_ru_tfp_dictionary_stack.py` (`FREQ_HIGH_*`, `CONF_*`, `MIN_RAW_FREQ`, `MAX_RAW_ENTRIES`) and re-run `--write`.

---

## Manual audit — Dict B expansion (~10 min)

After `expand_dict_b_tfp_controlled.py --write`:

1. `_dict_b_expansion_report.json` — `accepted_new_concepts` should stay **well below** `max_new_cap` (no explosion); `rejected_clusters` non-zero is healthy.  
2. Grep `dict_b_tfp.jsonl` for `TFP_CLUSTER_` — scan **definitions** and **related_concept_ids** (must reference real `concept_id`s only).  
3. **`hex_anchor: null`** — expect Ethan/hex layer degradation flags until anchors are assigned.  
4. `python3 tools/validate_dict_b_dlcr.py` · `validate_tfp_ru_pack.py` · `check_dlcr_regression.py` — all pass.  
5. Optional: tighten `MERGE_TOKEN_OVERLAP` / cluster thresholds in the expand tool if merges into existing TFP rows stay at 0 but bundles are clearly duplicate theory.

---

## Supersedes / legacy tools

- `tools/build_tfp_ru_corpus_clean.py` → optional; canonical sentences are **`tfp_ru_sentences.jsonl`** from the stack builder.  
- `tools/gen_tfp_ru_dict_pack.py` → **deprecated** for production; use stack builder.

---

## Related

- [ETHAN-TFP-RU-DICT-12TASKS.md](ETHAN-TFP-RU-DICT-12TASKS.md) (earlier 12-task note; partial overlap)  
- [ETHAN-DLCR-INTEGRATION-RUNBOOK.md](ETHAN-DLCR-INTEGRATION-RUNBOOK.md)
