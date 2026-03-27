# Ethan — 10 tasks: finish dictionaries, calibrate, check

**Date:** 2026-03-28  
**Role:** Architect (Ethan)  
**Precondition:** Lexical **A** green and frozen (`HESPERIA_CALIB_DICT_VERSION`, e.g. `v0_6_0_clr_v052_1`). **Order:** **B → CD → C_agg → Topology** — see [ETHAN-DICT-LAYER-ORDER-AFTER-A.md](ETHAN-DICT-LAYER-ORDER-AFTER-A.md). No OpenAI required for tasks below unless you explicitly refresh A/B LLM passes.

| # | Task | Owner (default) | Acceptance |
|---|------|-----------------|------------|
| **1** | **B inventory audit** — every `concept_id` that appears in calibration `links.jsonl` / engine merge has a **dict_b** line (same calibration dir + merged engine paths). | Gena + clinical spot-check | `validate_dict_b_dlcr.py` OK; spot list of orphan link targets empty or ticketed. |
| **2** | **B gap closure (human-gated)** — for missing `TFP_*` or thin rows, use `tools/gen_tfp_ru_dict_pack.py --write` **or** manual JSONL edits; no auto-bibliography mining. | Gena | Diff reviewed; `validate_tfp_ru_pack.py` OK; merged_b count matches expectation doc note. |
| **3** | **Links ↔ engine consistency** — `dict_a_engine.jsonl` / frozen `links.jsonl` align with `dict_a.jsonl` for the same `HESPERIA_CALIB_DICT_VERSION`. | Gena | No duplicate `normalized_form` conflicts; `check_dlcr_regression.py` OK after changes. |
| **4** | **CD registry pass** — extend `concept_dict_cd.jsonl` for high-traffic `concept_id`s (or rely on `*` defaults + explicit exceptions only where product needs requires/excludes/activation tweaks). | Ethan + Gena | `pytest tests/concept_dictionary/test_cd_executor.py` OK; double-run determinism preserved. |
| **5** | **CD-on runtime smoke** — pipeline with `HESPERIA_CD_ENABLED=1` (and optional `HESPERIA_CD_PHASE`) on representative RU/EN snippets; compare off vs on for sanity (no crash, plausible weight shaping). | Abelard or Gena | `./tools/run_b_cd_wave_after_a.sh` green; one logged before/after snippet in `operational/` or `tmp/` note (no secrets). |
| **6** | **Calibration metrics review** — read `metrics.json` for the freeze version; set pass thresholds (coverage, error rate) as **gate constants** in docs or `tools/calibration_release_gate.py` profile if already used. | Ethan | Written thresholds + “pass/fail” for current `metrics.json`; Grace can triage if fail. |
| **7** | **Gold / span regression** — grow or lock `corpora/tfp_ru_gold/` + `gold_tfp_ru.jsonl` (and related) so DLCR regression is not only synthetic; minimum **N** new segments agreed with clinical (e.g. 10–20). | Noah + Gena | `check_dlcr_regression.py` includes new cases or doc says why deferred; no silent shrink of coverage. |
| **8** | **TFP file pipeline calibration audit** — on a real `.md` transcript: `tools/gena_tfp_bundle_run.py` or `run_tfp_file_pipeline` → `tfp_calibration_audit.py` + optional `calibration_release_gate.py --profile internal_review`. | Gena | One bundle dir artifact set checked in CI or `tests/fixtures` path documented; gate JSON pass or waived with Ethan note. |
| **9** | **Version pin discipline** — `assets/data/engine_dynamics_v060/VERSION.yaml` + calibration dir name + `CHANGELOG` / `validate_version_consistency.py` stay aligned when any dict/CD asset bumps. | Abelard | `validate_version_consistency.py` OK after change; one-line release note when version bumps. |
| **10** | **Module mirror + CI hook** — after asset changes, `./tools/sync_tfp_module_data.sh`; add or document **one** CI job step: `run_b_cd_wave_after_a.sh` **or** equivalent `pytest` + validators on PRs touching `assets/calibration/dicts/` or `concept_dict/`. | Daniel + Abelard | CI green on sample PR; runbook line in CI README or `docs/governance/working/`. |

## One-liners (repo root)

```bash
./tools/run_b_cd_wave_after_a.sh
python3 tools/validate_dict_a.py && python3 tools/validate_dict_b_dlcr.py && python3 tools/validate_tfp_ru_pack.py && python3 tools/check_dlcr_regression.py
python3 tools/validate_version_consistency.py
```

## References

- [ETHAN-DICT-LAYER-ORDER-AFTER-A.md](ETHAN-DICT-LAYER-ORDER-AFTER-A.md)  
- [ETHAN-TFP-RU-DICT-12TASKS.md](ETHAN-TFP-RU-DICT-12TASKS.md)  
- [MODEL_CARD_CD_PIPELINE.md](../cd_v1/MODEL_CARD_CD_PIPELINE.md)  
- Cursor operational: `ETHAN-HESPERIA-B-CD-AFTER-A-GREEN.md` (brain repo `operational/assignments/`).

---

`SIGNED: Architect (Ethan) | 10-task dict finish + calibration check | 2026-03-28 | Hesperia governance/working`
