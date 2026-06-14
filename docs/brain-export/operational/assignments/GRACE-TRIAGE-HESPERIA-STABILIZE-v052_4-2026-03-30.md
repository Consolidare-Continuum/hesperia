# Grace triage — STABILIZE `v052_3` → `v052_4` (Balanced Semantic State)

**Date**: 2026-03-30  
**Brain repo**: `cursor` — this packet. **Engine + sealed dicts**: `/data/hesperia/hesperia`.

## Discipline (operator directive)

- **Single sealed outcome**: `assets/calibration/dicts/v0_6_0_clr_v052_4/` (name locked with Noah).
- **Do not** split into parallel micro-task rows per phase; **one** execution owner (**Noah**) runs the flow; **Olivia** is **handoff** REPORT/gate only; **Ethan** gate policy already in [ETHAN-HESPERIA-v052_4-STABILIZE-ASSESSMENT-2026-03-30.md](reports/ETHAN-HESPERIA-v052_4-STABILIZE-ASSESSMENT-2026-03-30.md) + **HPROM-06** (WARN/FAIL).

## Metric bindings (do not conflate)

Per Ethan assessment:

| Metric | Definition for acceptance |
|--------|---------------------------|
| Concepts ≥210 | **Distinct `concept_id` in v052_4 `links.jsonl`**, not REPORT `used_concepts_count` on the 3-line fixture alone. |
| Concept usage ≥75% | At denominator **283** (`dict_b` concepts): requires **≥212** linked concepts — or relax % / 210 bound explicitly. |
| Phrase dominance / phrase hit 0.45–0.60 | **Raise** from current v052_3 REPORT ~**0.18** into band — not R2-style suppression only. |
| Noise ↓ | vs **v052_3** baseline in `hprom_03_report_eval` successor run. |

## Phases (single flow — execution order)

1. **Concept recovery (mandatory)** — `lost_concepts` = v052_2 − v052_3 links (**25**); restore **≥210** linked concepts via **Option A** (2–5 C phrases) preferred, **Option B** (1–2 A tokens) fallback.
2. **Dict C** — **28.8k → ~20–24k** (target ~22k); drop low-info / near-dup / weak phrases; **phrases_per_concept** min ~20 / max ~120–150; trim top-10 concept clusters **15–30%**.
3. **Dict A selective restore** — underfed / **&lt;20** lexical entries; **+2k tokens max**; respect HDR-A7 (no blind bulk restore).
4. **Links** — rebuild; max links per entry; reduce multi-concept ambiguity; no legacy-only link rows.
5. **Dict B (optional)** — light dedup **62k → ~45–50k**; **`concept_id` stable**.

## Validation (mandatory)

- Run REPORT pipeline (extend eval corpus vs 3-line-only as needed — see Ethan doc).
- Check: coverage **≥210** linked concepts, phrase metrics in band, noise ↓ vs v052_3, entropy stable/↑, **validators + C-first + blocking** — no structural regressions.

## Gate

- On success: **REPORT → WARN** (not FAIL). **FAIL** only after **2 stable runs** — **Ethan** / **HPROM-06**.

## After v052_4

- **Stop restructuring** → stability, invariants, audit hardening (operator).

## active.md rows (Grace)

| Row | Owner | Status | Role |
|-----|-------|--------|------|
| STABILIZE-v052_4 | **Noah** | **OPEN** | Single-flow sealed build |
| STABILIZE-v052_4 REPORT | **Olivia** | **PAUSED** | REPORT + gate note when v052_4 exists |

`SIGNED: Grace (triage) | Hesperia STABILIZE v052_4 | 2026-03-30 | packet + team rows`
