# Hesperia — B and CD after green A (execution wave)

**Date:** 2026-03-28  
**Status:** **ACTIVE** — Dict **A** frozen + validators **green** (`v0_6_0_clr_v052_1`). Proceed **without** OpenAI for this wave.

**Ethan ruling (locked):** **B before CD.** Do not treat CD as a concept factory ahead of B; CD rows annotate stable `concept_id`s from B. See Hesperia **`docs/governance/working/ETHAN-DICT-LAYER-ORDER-AFTER-A.md`**.

## Chain (canonical)

Per `docs/governance/cd_v1/MODEL_CARD_CD_PIPELINE.md` (Hesperia repo):

`A` (lexical) → `B` (concept identity / resolver) → **`CD`** (Concept Dictionary) → **`C_agg`** → **Topology**

- **A:** done — calibration `dict_a.jsonl` + engine merge; do not re-run LLM extract/normalize/propose unless intentionally refreshing A.
- **B:** `dict_b.jsonl` + links/metrics in the same calibration version; resolver/DLCR truth. Keep `validate_dict_b_dlcr.py` + `validate_tfp_ru_pack.py` + `check_dlcr_regression.py` green when changing B.
- **CD:** `assets/data/engine_dynamics_v060/concept_dict/concept_dict_cd.jsonl` (or `HESPERIA_CD_JSONL`). Opt-in at runtime: `HESPERIA_CD_ENABLED=1`, phase `HESPERIA_CD_PHASE` (default 1). Tests: `tests/concept_dictionary/test_cd_executor.py`.
- **Rest:** `C_agg` / hex aggregation and topology already follow CD in `lexical_concept/pipeline.py`; **HC** control-layer tasks (Ethan packet 2026-03-27) for competition/modifiers/hooks as that program unblocks.

## One-shot script (Hesperia repo root)

```bash
chmod +x tools/run_b_cd_wave_after_a.sh   # once
./tools/run_b_cd_wave_after_a.sh
```

Optional: `HESPERIA_CALIB_DICT_VERSION=v0_6_0_clr_v052_1` (default in script).

## Optional B growth (human-gated)

Idempotent Dict B TFP row append only when product asks for more `TFP_*` inventory:

`python3 tools/gen_tfp_ru_dict_pack.py --write` — see `docs/governance/working/ETHAN-TFP-RU-DICT-12TASKS.md`.

## Related

- **Ethan 10-task dict / calibration program:** [ETHAN-10-TASKS-DICTS-CALIB-2026-03-28.md](ETHAN-10-TASKS-DICTS-CALIB-2026-03-28.md) (same packet mirrored under Hesperia `docs/governance/working/`).

## Implementation log

| Date | Note |
|------|------|
| 2026-03-28 | Ethan: locked **B → CD** order; added `ETHAN-DICT-LAYER-ORDER-AFTER-A.md` in Hesperia; operational packet aligned. |
| 2026-03-28 | Ethan: **10 tasks** dict finish + calibration check packet (cursor + Hesperia working). |

---

`SIGNED: Architect (Ethan) | B+CD wave after green A | 2026-03-28 | cursor operational + Hesperia working`
