# Ethan — Assessment: STABILIZE `v052_3` → `v052_4` (balanced semantic state)

**Date**: 2026-03-30  
**Repo scope**: Brain = `cursor`; engine + sealed dicts = `/data/hesperia/hesperia`.  
**CSP**: From: general Cursor execution | To: Ethan (governance / gate / model contract) | Reason: Operator brief for v052_4 stabilization | What changes: Authority = interpret brief vs **measured** artifacts; outputs = corrected targets + gate policy + single execution row; no dict row edits in this artifact.

---

## 0) Objective (aligned)

Move from **structurally correct but imbalanced** to **stable, coverage-complete, phrase-first** engine — **accepted**, provided metrics and baselines are **defined against current sealed data**, not mixed definitions.

---

## 1) Ground truth vs compressed narrative (mandatory corrections)

| Topic | Narrative in brief | **Measured current state** |
|--------|-------------------|----------------------------|
| Concepts in links | “216 → 191” | **Confirmed**: `links.jsonl` distinct `concept_id`: **v052_2 = 216**, **v052_3 = 191**. Delta **−25** (no new concepts in v052_3 vs v052_2). |
| `dict_b` | “B bloated 62k / 283 concepts” | **Confirmed**: **62 316** rows, **283** distinct `concept_id` in both v052_2 and v052_3 — **unchanged**; bloat is **row duplication / structure**, not concept count drop. |
| “Concept usage dropped” | Same as links | **Clarify**: Drop is **link coverage of concepts** (191/283 ≈ **67.5%**), not loss of concepts from `dict_b`. |
| REPORT `used_concepts_count` | Sometimes conflated with 216/191 | **Not the same metric**: On `hprom_03_report_eval_v6` **3-line** fixture, **v052_2 = 10**, **v052_3 = 9** — **tiny-corpus activation**, not inventory. **Do not** use fixture count as proof of 210+ recovery. |
| Phrase dominance | “0.45–0.60” after R2 pain at 0.75 | **Current v052_3 REPORT**: `concept_activation_from_c_ratio` ≈ **0.182**, `phrase_hit_ratio` ≈ **0.182** — **below** the band. v052_4 work must **raise** phrase-channel share into band — **opposite direction** from HPROM-R2 (which **reduced** C over-dominance). Plan phases must not re-apply R2-only logic blindly. |
| Dict A | “Over-cut” | **Confirmed**: v052_3 **10 155** rows vs v052_2 **75 371** — large reduction; selective restoration **only** underfed concepts is consistent with HDR-A7 preservation intent. |

**Lost concepts (25)** — present in v052_2 `links` edges, **absent** from v052_3 `links` (sample):  
`B_A10_F10_004`, `B_A10_F10_005`, `B_A10_F12_006`, `B_A10_F13_006`, `B_A10_F16_005`, `B_A10_F18_005`, `B_A10_F1_004`, `B_A10_F1_005`, `B_A10_F20_006`, `B_A10_F23_005`, `B_A10_F24_005`, `B_A10_F24_006`, `B_A10_F2_003`, `B_A10_F3_004`, `B_A10_F4_006`, `B_A10_F5_004`, `B_A10_F6_005`, `B_A1_F10_005`, `B_A1_F11_006`, `B_A1_F12_006`, `B_A1_F14_005`, `B_A1_F15_003`, `B_A1_F17_005`, `B_A1_F1_004`, `B_A1_F20_005`.

---

## 2) Target corrections (bind before build)

1. **Concepts recovered ≥210**  
   - Interpret as **distinct `concept_id` appearing in combined `links.jsonl`** for the sealed version (not REPORT fixture count).  
   - **210 / 283 = 74.3%**. Your **≥75% “concept usage ratio”** implies **≥212** linked concepts at denominator 283 — state this explicitly or relax one bound.

2. **Dict C 20k–24k (from ~28.8k)**  
   - **Aligned** with further prune + rebalance; **~22k** mid-target is consistent with Phase 2.

3. **Dict A 10k–15k**  
   - Current **10 155** already in band. Phase 3 cap **+2k tokens** → **≤12 155** — still inside **15k** if discipline holds.

4. **Phrase dominance / phrase hit 0.45–0.60**  
   - Must be measured on **agreed corpus** (at minimum: current REPORT fixture + **expanded** Russian eval set — recommend **explicit** in Olivia gate doc; 3 lines alone are **not** enough to prove band stability).

5. **Noise ↓ vs v052_3**  
   - Baseline for comparison = **v052_3 post-R2** (`noise_ratio` in `hprom_03_report_eval_v6`). Any regression vs that row **blocks** WARN promotion.

6. **B light compression 62k → 45–50k**  
   - Feasible only with **dedup rules** that preserve **`concept_id` stability** and pass `validate_dict_b_dlcr` — scope as **optional** sub-phase inside the same sealed build, not a second project.

---

## 3) Phase mapping — feasibility + guardrails

| Phase | Verdict | Guardrail |
|-------|---------|-----------|
| **1 Concept recovery** | **Mandatory** | Prefer **C phrase triggers (2–5)** per lost concept; A tokens only for gaps. **Must** restore **≥210** linked concepts without breaking schema. |
| **2 C prune + balance** | **Mandatory** | Enforce **phrases_per_concept** min/max with **deterministic** tie-breaks; trim **top-heavy** concepts 15–30% as stated. **Do not** violate C token-count {2,3} schema. |
| **3 Selective A restore** | **Allowed** | **+2k max**; only for **underfed** / **&lt;20 lexical entries** concepts — aligns with Ethan **HDR-A7** (no blind re-expansion of frozen API-calibrated bulk). |
| **4 Link normalization** | **Mandatory** | Rebuild `links` from final A/C + `dict_b`; enforce max links per entry; **no** legacy `lexical`-only rows. |
| **5 B compression** | **Optional** | Dedup-only; **no** concept ID churn. |

---

## 4) Validation + gates (Ethan)

- **Mandatory**: New `hprom_report_metrics` run (or successor) on **same + extended** fixture set; archive as `hprom_04` or bump `run` label.  
- **Acceptance**: All **strict** criteria in your brief **on defined metrics** — plus **no structural regressions** (validators, C-first order, blocking).  
- **Gate**: On success → **REPORT → WARN** (operator brief). **FAIL** remains **out** until **2 stable runs** on agreed corpus — consistent with **HPROM-06** (Ethan **PAUSED** until evidence).  
- **After v052_4**: Operator directive to **stop restructuring** → **stability + invariants + audit hardening** — **endorsed** as governance posture.

---

## 5) Execution form (single flow — repo contract)

- **One** sealed outcome: `assets/calibration/dicts/v0_6_0_clr_v052_4/` (or successor name Ethan/Noah lock).  
- **One** active row (see `active.md`): **single owner** **Noah** for artifact generation, **Olivia** REPORT + gate note, **Gena** on runtime/evidence edge cases if resolver thresholds move — **without** splitting into parallel HPROM-Rx micro-rows (operator: one row, one handoff chain).

---

## 6) Bottom line

The brief is **directionally correct**; it **must** be **tightened** on: (1) **metric definitions** (links coverage vs REPORT fixture), (2) **phrase band** — **increase** from current **0.18**, not repeat R2-only reduction, (3) **75% usage** vs **210** concepts — align arithmetic or relax. With those bindings, **STABILIZE v052_3 → v052_4** is **coherent** and **gate-ready** under **WARN** after evidence.

`SIGNED: Ethan (governance / gates) | Hesperia calibration stabilization | 2026-03-30 | assessment + corrected targets`
