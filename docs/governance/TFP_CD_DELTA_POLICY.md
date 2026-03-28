# CD delta policy (TFP-GATE-CD-DELTA)

**Rule:** CD dict changes (`concept_dict_cd.jsonl`) require **explicit** review: line-count / schema diff vs baseline; wave precheck (`run_b_cd_wave_after_a.sh`) must pass; links baseline tolerance (`HESPERIA_LINKS_LINE_TOLERANCE`) documented when non-zero.

**Baseline file:** `assets/calibration/dicts/<pack>/.links_line_count_baseline`

---

`SIGNED: Cursor (workflow) | TFP-GATE-CD-DELTA | 2026-03-28`
