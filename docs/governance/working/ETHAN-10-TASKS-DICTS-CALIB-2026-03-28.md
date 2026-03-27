# Ethan — Dict / calibration release framework (rev. 2)

**Date:** 2026-03-28 (rev. 2 — control laws + tiering)  
**Role:** Architect (Ethan)  
**Precondition:** Lexical **A** green; **B → CD → C_agg → Topology** — [ETHAN-DICT-LAYER-ORDER-AFTER-A.md](ETHAN-DICT-LAYER-ORDER-AFTER-A.md).

Rev. 1 was ~70% right: **missing control laws + invariant enforcement**. This revision adds **competition/dominance**, **length invariance**, **modifier checks**, **unmapped closed loop**, **cross-plane agreement**, and splits **hard ship gates** vs **structural** vs **system** vs **hygiene**.

---

## 1) Hard gates — **cannot ship without** (determinism + mapping correctness)

Wrong here → garbage downstream.

| ID | Gate | Why | Acceptance (minimum) |
|----|------|-----|----------------------|
| **H1** | **B inventory audit** | If B coverage is wrong, everything downstream lies. | `validate_dict_b_dlcr.py` OK; orphan link targets from `links.jsonl` / merge **empty or ticketed**. |
| **H2** | **B gap closure** | Audit without closure is useless. **Human-gated** — do not automate blindly. | Reviewed diffs (`gen_tfp_ru_dict_pack.py --write` and/or manual JSONL); `validate_tfp_ru_pack.py` OK. |
| **H3** | **Links ↔ engine alignment** | Frozen **links** = reproducibility; **engine dict_a** = consistency with calibration **A**. Miss → non-repeatable outputs. | Same `HESPERIA_CALIB_DICT_VERSION`; no `normalized_form` collisions; `check_dlcr_regression.py` OK. |
| **H4** | **Metrics gate** | No thresholds = no system. **Explicit pass/fail**, not “looks good.” | Written numeric thresholds + recorded verdict on current `metrics.json` / gate profile; fail → no ship without Grace/Ethan waiver. |
| **H5** | **Gold / span regression** | Only protection against **silent drift**. | Real segments in suite (not synthetic-only); `check_dlcr_regression.py` extended or **documented deferral** (no silent shrink). |
| **H6** | **Mirror + CI** | Without CI, dictionaries **rot** immediately. | `./tools/sync_tfp_module_data.sh` after asset moves; CI runs `run_b_cd_wave_after_a.sh` **or** equivalent validators on PRs touching `assets/calibration/dicts/` / `concept_dict/`. |

---

## 2) Structural correctness — **engine behaves like a model**, not a lookup mess

Without CD, **B is just labels** — no competition, no normalization in the CD sense. **CD is not optional** for a sealed semantic engine claim.

| ID | Item | Why | Acceptance (minimum) |
|----|------|-----|----------------------|
| **S1** | **CD registry pass** | Prior failure mode: skipping CD. | `concept_dict_cd.jsonl` complete for policy (explicit rows + `*`); `pytest tests/concept_dictionary/test_cd_executor.py` OK; determinism double-run holds. |
| **S2** | **CD-on validation** | Not only “runs.” Need **Δ vs no-CD** + **activation distribution** sanity. | Logged pairs (off/on) + short stats (e.g. min/mean/max active weights); blind CD deploy rejected. |
| **S3** | **Concept competition / dominance** | Otherwise: **spread instead of meaning**. Explicit **dominance** (top concept/family) + **suppression of near-equals**. | ADR or CD Phase 2 policy wired per **HC-02** / [CO_OCCURS_MATH_PHASE2.md](../cd_v1/CO_OCCURS_MATH_PHASE2.md); tests or gate artifact proves single-winner policy where required. |
| **S4** | **Length invariance** | Same meaning, longer text → **same distribution** (within tolerance). Else = **sum of words**. | Fixture or test: paraphrase/expand same semantic content → bounded drift on chosen metrics (document tolerance). |
| **S5** | **Modifier propagation** | TFP-critical: **negation**, **intensity**, **direction**. Untested → false signals. | Binding path per **HC-ETHAN-01** / **HC-03**; tests or gold segments proving expected flip/damp—not only happy path. |
| **S6** | **Unmapped token closed loop** | Partial audit is not enough. **Top-N unmapped** → **systematic candidate path into A** (triage, not silent drop). | Ranked report (**HC-08** style) + **documented ingest rule** into candidates/normalize queue; coverage stagnation flagged in metrics gate. |

---

## 3) System validation — **product-level** (real behavior, not mechanics only)

| ID | Item | Why | Acceptance (minimum) |
|----|------|-----|----------------------|
| **V1** | **TFP bundle calibration audit** | Only **domain reality check**. Without real transcript = tuning **noise**, not behavior. | Real `.md` → `gen_tfp_bundle_run` / `run_tfp_file_pipeline` → `tfp_calibration_audit.py` (+ `calibration_release_gate.py` as profiled); artifact path recorded. |
| **V2** | **Cross-plane agreement** | If claimed: structural / multiscale / topology must **agree on a comparable schema** — or **retract the claim**. | **HC-09** contract: pass/warn/fail + example JSON; or explicit doc that product does not assert cross-plane numeric agreement yet. |

---

## 4) Hygiene / stability — **important, not ship blockers alone**

| ID | Item | Acceptance |
|----|------|------------|
| **Y1** | **Version pins** | `VERSION.yaml`, calibration dir name, `CHANGELOG`, `validate_version_consistency.py` aligned after any dict/CD bump. |

---

## Minimal checklist (non-bloated)

**Core gates:** H1 H2 H3 H4 H5 H6  
**Structural + control laws:** S1 S2 S3 S4 S5 S6  
**System:** V1 V2  
**Hygiene:** Y1  

---

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
- Control layer: HC-02, HC-03, HC-08, HC-09 — cursor `operational/assignments/ETHAN-HESPERIA-CONTROL-LAYER-V1-TASKING-2026-03-27.md`

---

`SIGNED: Architect (Ethan) | dict/calibration framework rev. 2 | 2026-03-28 | Hesperia governance/working`
