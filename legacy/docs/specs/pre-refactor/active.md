<!--
HESPERIA — Reference Architecture Definition (RAD)
Copyright © 2026 igareosh.com — Platonov Igor (aka @igareosh). All rights reserved.
Restricted Research Disclosure License. Inspection and reference only.
No reproduction, redistribution, or use without explicit written permission.
See LEGAL_NOTICE.md for full terms.
-->

# Historical reference (pre-refactor)

# Active tasks — Hesperia project

**Purpose:** Task rows assigned by Grace. Update when tasks are added, reassigned, or closed. **Ref:** [CONTEXT-PACKET.md](CONTEXT-PACKET.md) §2.

---

## R1–R4 reading-scale spec (Grace 2026-02-27)

| # | Owner | Task | Status | Link |
|---|--------|------|--------|------|
| 1 | Ethan | Freeze and persist R1–R4 defaults (Δ_expected, ε, Σ bounds, R3 typing, SCI, trust tier, shadow rule); fix and document N (top-N, e.g. N=3) constant across R-levels | **DONE** | [TASK-GRACE-R1-R4-READING-SPEC-TRIAGE.md](../governance/TASK-GRACE-R1-R4-READING-SPEC-TRIAGE.md) |
| 2 | Ethan | Contradiction graph C ⊂ F×F; persist artifact; document CP (Part B.5) contract | **DONE** | Same |
| 3 | Gena | Segmenters (R2/R3/R4); segmenter contract | **DONE** | Same |
| 4 | Gena | L1–L9 → Unit mapping; validate with Part C schemas | **DONE** | Same |
| 5 | Gena | Pipeline end-to-end: segment → L1–L9 → Unit → aggregation → BookProfile; validate schema | **DONE** | Same |
| 6 | — | Corpus calibration (Δ_expected, ε; ESM v1.1) | DEFERRED | When corpus available |
| 7 | Ethan | Band/decision_code mapping: lock per deployment; code set (e.g. SIGMA_FAIL_LEAK, GAMMA_DRIFT) and band rules; document | **DONE** | Same |

**Triage:** [governance/TASK-GRACE-R1-R4-READING-SPEC-TRIAGE.md](../governance/TASK-GRACE-R1-R4-READING-SPEC-TRIAGE.md). **Deliverable rule:** JSON per schema only; no table-fill from spec. **Context rule:** sphere_math 100-sentence output — use `--limit N` or single run, not full file.

**Workflow progress:** Task 1 — ESM defaults + doc + loader. Task 2 — C + CP contract + loader. Task 3 — segmenters (R1–R4). Task 4 — L1–L9 → Unit. Task 5 — full pipeline (R1–R4, scale_deltas, optional --validate). Task 7 — band/decision_code doc. **Grace check:** [GRACE-CHECK-GENA-R1-R4-DONES.md](../governance/GRACE-CHECK-GENA-R1-R4-DONES.md) — Gena 3, 4, 5 signed DONE.

---

## R1–R4 integration (Grace 2026-02-27)

| # | Owner | Task | Status | Link |
|---|--------|------|--------|------|
| I1 | Ethan | R1–R4 integration contract: entry points, inputs/outputs, where consumed (analyze, context_rag, API), guard integration | **DONE** | [R1_R4_INTEGRATION_CONTRACT.md](../docs/R1_R4_INTEGRATION_CONTRACT.md) |
| I2 | Gena | Wire R1–R4 into analyze (optional per contract) | **DONE** | [analyze() r1_r4=True](../sphere_rag/analyze.py); [R1_R4_INTEGRATION_CONTRACT.md](../docs/R1_R4_INTEGRATION_CONTRACT.md) §3.1 |
| I3 | Gena | API / context_rag exposure for BookProfile (optional per contract) | **DONE** | [api/main.py](../api/main.py): response `{ result, extended }`; body `r1_r4: true` → `extended.r1_r4` |

**Triage:** [governance/TASK-GRACE-R1-R4-INTEGRATION-SPEC-TRIAGE.md](../governance/TASK-GRACE-R1-R4-INTEGRATION-SPEC-TRIAGE.md).
