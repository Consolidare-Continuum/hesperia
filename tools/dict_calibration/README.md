# Dictionary calibration execution_flow (Ethan)

Closed loop: **corpus → lexical candidates → OpenAI (propose/normalize) → Hesperia DLCR (truth)** → metrics → errors → patch → repeat.

OpenAI proposes; **Hesperia matching, resolver, anchors, and evaluation are authoritative.**

**Dict A — API chapter closed:** RU / alignment work that needed the model is **done**; canonical Dict A for runtime is the **frozen calibration pack** (e.g. `assets/calibration/dicts/v0_6_0_clr_v052_1/dict_a.jsonl` + engine merge), not a live OpenAI loop. **Do not** re-run `extract` → `normalize` → `propose` / `ru-tfp-align` on production workdirs unless you intentionally refresh A; **proceed** with local stages (anchor / links / eval / errors / freeze already applied), validators, DLCR, and **C / CD / HC** tracks **without** requiring `OPENAI_API_KEY`.

**Sealed freeze (operator permission):** The whole tree `assets/calibration/dicts/v0_6_0_clr_v052_1/` (Dict A, normalized, proposals/draft, anchored dict_b, links, metrics) is **locked** — **no edits without direct permission from igareosh**. See **`docs/governance/working/ETHAN-DICT-A-NORM-PROPOSE-ANCHOR-LOCK-2026-03-28.md`**.

## Install (optional extras)

```bash
pip install -e ".[dict-calibration]"
python -m spacy download ru_core_news_sm   # optional: dependency pairs on RU text
python -m spacy download en_core_web_sm   # optional: EN fallback
```

Set `OPENAI_API_KEY`. Model: `HESPERIA_CALIB_OPENAI_MODEL` (default `gpt-4o-mini`).

**Until full C / CD / HC dict pipeline:** default **4** parallel workers for anchor / links / eval / errors (`HESPERIA_DICT_CALIB_WORKERS`, default `4`; clamped 1–64). **One-shot offline:** `HESPERIA_DICT_CALIB_OFFLINE=1` sets `HESPERIA_CALIB_MOCK_OPENAI=1` and workers `4` if unset.

**No API (deterministic mock):** `HESPERIA_CALIB_MOCK_OPENAI=1` or `yaml-markers-llm --mock-llm` — `chat_json` never calls the network; `require_openai_key()` is skipped in mock mode. Returns rule-based / empty JSON so pipelines and tests run offline. **No real LLM alignment** in that mode (proposals are empty or identity echo for normalize/propose stubs).

**LEVEL-4 YAML markers (LLM draft):** proposes `lexical_markers`-shaped rows from `hesperia/ontology/dictB/concept_nodes.yaml` + corpus phrase pool; writes **`lexical_markers_llm_proposed.yaml`** under `--workdir` for human review (not canonical until you copy/freeze).

```bash
# Wiring check only (zero proposals)
python3 tools/dict_calibration/run_pipeline.py yaml-markers-llm --mock-llm \
  --corpus research/_noone_local/2_cleaned \
  --workdir outputs/dict_calibration/yaml_markers_llm_dry --pilot

# Real run (needs OPENAI_API_KEY)
python3 tools/dict_calibration/run_pipeline.py yaml-markers-llm \
  --corpus research/_noone_local/2_cleaned \
  --workdir outputs/dict_calibration/yaml_markers_llm_run1
```

**After cold coverage (`ru-tfp-extract-cold`):** standalone script with **prompts in-file** + `PROMPT_SNAPSHOT.md` audit trail:

```bash
python3 tools/post_cold_lexical_markers_align.py \
  --cold-pack outputs/dict_calibration/ru_tfp_align_run2/cold_pack \
  --corpus research/_noone_local/2_cleaned \
  --workdir outputs/dict_calibration/post_cold_markers_run1
# or: --coverage-report …/coverage_report.json
# optional: --seed-yaml hesperia/ontology/dictA/lexical_markers.yaml
```

**Small credit line:** use `run-all --budget` — caps normalize rows (~240), propose batches, catalog lines, eval sample size, and patch payload so one pass stays on the order of tens of API calls (not thousands).

**Human loop with Ethan:** each iteration run `wave` (loads API key from repo `.env`, writes `outputs/dict_calibration/wave_NNN/` + `WAVE_HANDOFF.md`), then paste metrics / issues in chat for the next adjustment.

**Batch coverage:** `waves --count 20` runs 20 finite passes; wave *k* LLM-normalizes only slice *k/20* of the **filtered** candidate list (by frequency), then the usual propose → anchor → … Each wave is still finite; total cost ≈ **20×** one `wave` (use `--skip-llm` to dry-run the slice logic).

**Full 283 TFP concepts (Russian corpus alignment):** `ru-tfp-align` builds `dict_a_tfp_ru_aligned.jsonl`. Default **`--align-mode concept_batch`**: each call is **~14 concepts** + **≤150** phrases; the model is capped at **40** `links` per response. If JSON is still invalid/truncated, the tool **bisects the phrase list** and retries. With `max_phrases=6000`, expect on the order of **21 × ⌈2000/150⌉ × 3 ≈ 840** API calls (plus occasional splits). **`--phrase-sub-batch 0`** = one phrase block per concept batch (often truncates). **`openai_json.chat_json`**: default **`max_tokens=16384`**; no useless retry when `user` is huge. Legacy **`--align-mode phrase_chunk`** is not recommended. Outputs: `coverage_report.json`, `phrase_pool.json`, per-pass summaries.

```bash
python3 tools/dict_calibration/run_pipeline.py ru-tfp-align \
  --corpus research/_noone_local/2_cleaned \
  --workdir outputs/dict_calibration/ru_tfp_align_run1
```

**Cold concepts (zero links):** `coverage_report.json` lists them in `concepts_with_zero_links`. Materialize IDs + Dict B rows for review:

```bash
python3 tools/dict_calibration/run_pipeline.py ru-tfp-extract-cold \
  --coverage-report outputs/dict_calibration/ru_tfp_align_run2/coverage_report.json \
  --out-dir outputs/dict_calibration/ru_tfp_align_run2/cold_pack
```

Writes `cold_concept_ids.txt`, `cold_concepts.json`, and **`stayed_cold_readable.md`** (human table: id, label, definition excerpt, areas). **Second pass** only on those IDs while keeping prior phrase mappings:

```bash
python3 tools/dict_calibration/run_pipeline.py ru-tfp-align \
  --corpus research/_noone_local/2_cleaned \
  --workdir outputs/dict_calibration/ru_tfp_cold_pass \
  --only-zero-from outputs/dict_calibration/ru_tfp_align_run2/coverage_report.json \
  --seed-dict-a outputs/dict_calibration/ru_tfp_align_run2/dict_a_tfp_ru_aligned.jsonl
```

Append `dict_a_tfp_ru_aligned.jsonl` last in `dict_a_paths` when running DLCR.

## Layout

| Artifact | Task |
|----------|------|
| `dict_a_candidates.jsonl` | 1 — deterministic extraction |
| `dict_a_normalized.jsonl` | 2 — LLM normalization |
| `dict_b_draft.jsonl` | 3 — LLM concept proposals |
| `dict_b_anchored.jsonl` / `dict_b_rejected.jsonl` | 4 — bind to existing Dict B + hex |
| `dict_a_to_b_links.jsonl` + `dict_a_engine.jsonl` | 5 — DLCR-ready Dict A |
| `evaluation_run.json` | 6 — `run_dlcr_pipeline` metrics |
| `dict_errors.jsonl` | 7 — error surface |
| `dict_patch.json` | 8 — LLM patch (applied deterministically to links) |
| `assets/calibration/dicts/v…/` | 10 — reviewed freeze (see `freeze` command) |

Default workdir: `outputs/dict_calibration/run1` (gitignored).

## Two-script OpenAI entrypoints

Thin wrappers around Tasks 2–3 (same behavior as ``run_pipeline normalize`` / ``propose``):

```bash
PYTHONPATH=. python3 tools/openai_calibration_1_normalize.py \
  --workdir outputs/dict_calibration/my_run --corpus research/_noone_local/2_cleaned

PYTHONPATH=. python3 tools/openai_calibration_2_propose.py \
  --workdir outputs/dict_calibration/my_run --limit 120
```

Run 1 can omit ``--corpus`` if ``dict_a_candidates.jsonl`` already exists. Use ``--dry-run`` or ``HESPERIA_CALIB_MOCK_OPENAI=1`` to avoid the API.

## Commands

From repository root:

```bash
# Numbered waves (auto picks wave_001, wave_002, …); budget on by default
python3 tools/dict_calibration/run_pipeline.py wave --corpus research/_noone_local/2_cleaned

# Twenty sequential waves (different candidate slices per wave)
python3 tools/dict_calibration/run_pipeline.py waves --corpus research/_noone_local/2_cleaned --count 20 \
  --base-dir outputs/dict_calibration/ethan_auto

# One frugal end-to-end pass (fixed workdir)
python3 tools/dict_calibration/run_pipeline.py run-all \
  --corpus research/_noone_local/2_cleaned --workdir outputs/dict_calibration/run1 --budget

# Full stack (use --skip-llm for extraction + anchoring skeleton without API)
python3 tools/dict_calibration/run_pipeline.py extract \
  --corpus research/_noone_local/2_cleaned --out outputs/dict_calibration/run1

python3 tools/dict_calibration/run_pipeline.py normalize --workdir outputs/dict_calibration/run1
python3 tools/dict_calibration/run_pipeline.py propose --workdir outputs/dict_calibration/run1 --limit 80
python3 tools/dict_calibration/run_pipeline.py anchor --workdir outputs/dict_calibration/run1
python3 tools/dict_calibration/run_pipeline.py links --workdir outputs/dict_calibration/run1
python3 tools/dict_calibration/run_pipeline.py eval --workdir outputs/dict_calibration/run1 \
  --corpus research/_noone_local/2_cleaned
python3 tools/dict_calibration/run_pipeline.py errors --workdir outputs/dict_calibration/run1 \
  --corpus research/_noone_local/2_cleaned
python3 tools/dict_calibration/run_pipeline.py patch --workdir outputs/dict_calibration/run1
python3 tools/dict_calibration/run_pipeline.py loop --workdir outputs/dict_calibration/run1 \
  --corpus research/_noone_local/2_cleaned
python3 tools/dict_calibration/run_pipeline.py freeze --workdir outputs/dict_calibration/run1 \
  --version-dir assets/calibration/dicts/v0.0.1-cal
```

## Design constraints

- **Dict B explosion**: anchoring maps drafts onto **existing** `concept_id`s via label similarity; unmatched drafts go to `dict_b_rejected.jsonl`.
- **Dict A noise**: raise `--min-freq`, cap `--propose-limit`, tighten fuzzy thresholds in `build_links.py` if needed.
- **Determinism**: LLM steps are non-deterministic; all merges, matching, evaluation, and patch application are deterministic given fixed inputs.

## Regression tests

`pytest tests/test_dict_calibration_pipeline.py` (no API calls).
