<!--
HESPERIA — Reference Architecture Definition (RAD)
Copyright © 2026 igareosh.com — Platonov Igor (aka @igareosh). All rights reserved.
Restricted Research Disclosure License. Inspection and reference only.
No reproduction, redistribution, or use without explicit written permission.
See LEGAL_NOTICE.md for full terms.
-->

# Historical reference (pre-refactor)

# Task: Grace — R1–R4 reading-scale spec triage and team tasking

**Purpose:** Grace proceeds on triage and tasks the team with R1–R4 reading-scale spec work. Deliverables are **JSON per schema only** (no table-fill from spec); context and agent use follow [ETHAN-HESPERIA-R1-R4-DELIVERABLE-CONTEXT-FIX.md](ETHAN-HESPERIA-R1-R4-DELIVERABLE-CONTEXT-FIX.md). **Owner:** Grace. **Added:** 2026-02-27.

**Spec:** [docs/SPEC__Reading_Scale_Levels_R1_R4_Structural_Audit_v1_0.md](../docs/SPEC__Reading_Scale_Levels_R1_R4_Structural_Audit_v1_0.md) — R1–R4 (sentence→paragraph→chapter→book), Unit/BookProfile/SI_metrics schemas (Part C), ESM (Part D), guard integration (Σ/Γ/Θ).

**Refs:** [ETHAN-HESPERIA-R1-R4-DELIVERABLE-CONTEXT-FIX.md](ETHAN-HESPERIA-R1-R4-DELIVERABLE-CONTEXT-FIX.md), [schema/](../schema/), [AVOID__R1_R4_Spec_Until_Reasonable.md](../docs/AVOID__R1_R4_Spec_Until_Reasonable.md).

---

## 1. Triage (Grace)

- **Proceed:** Team may proceed on R1–R4 reading spec per implementation plan in spec §Implementation Plan.
- **Constraint:** All pipeline outputs **must** be JSON conforming to Part C schemas (Unit, BookProfile, SI_metrics). No task shall require the model or tooling to emit/fill the spec’s markdown tables; tables are reference only. For sphere_math run outputs used as context, use `--limit N` or single-sentence run; do not attach full 100-sentence file.
- **Task rows:** Added to [project/active.md](../project/active.md) with owners and links.

---

## 2. Team tasking (Grace)

| # | Owner | Task | Deliverable / note |
|---|--------|------|--------------------|
| 1 | **Ethan** | Freeze and persist R1–R4 defaults (Δ_expected, ε, drift baseline, Σ bounds, R3 typing, SCI, trust tier, shadow rule) as canonical v1.0 config; **fix and document N (top-N for leakage) constant across R-levels** (spec §2.2; recommend N=3); document location and version. | Config artifact + short doc (e.g. in `sphere_rag` or versioned config). |
| 2 | **Ethan** | Define or import contradiction graph C ⊂ F×F; persist versioned artifact; document contract for CP computation (Part B.5). | C artifact + integration note. |
| 3 | **Gena** (or implementation) | Segmenters: implement or integrate paragraph, chapter, book/part segmenters for R2/R3/R4; document segmenter contract (input: full text or token stream; output: span or token ranges per unit). | [sphere_rag/r1_r4_segmenters.py](../sphere_rag/r1_r4_segmenters.py) (R1 sentences, R2 paragraphs, R3 chapters, R4 book) + contract doc. |
| 4 | **Gena** (or implementation) | L1–L9 → Unit mapping: for each segment (R1–R4), run L1–L9 (or minimal L1, L8 for SI_*); map outputs into Unit.schema.json; validate with Part C schemas. | [sphere_rag/r1_r4_unit.py](../sphere_rag/r1_r4_unit.py) (build_unit from L1–L7 + hits). |
| 5 | **Gena** (or implementation) | Pipeline end-to-end: segment → per-segment L1–L9 → Unit objects → aggregation (weighted means/variances) → scale_deltas → Δ_dev, turning points, BookProfile; validate BookProfile against schema. | [sphere_rag/r1_r4_pipeline.py](../sphere_rag/r1_r4_pipeline.py), [sphere_rag/run_r1_r4_pipeline.py](../sphere_rag/run_r1_r4_pipeline.py) (R1 pipeline; BookProfile output). |
| 6 | **Optional** | Corpus calibration: when corpus exists, compute Δ_expected and ε (and drift baseline) per metric/transition; replace defaults; re-version ESM (e.g. v1.1). | Deferred until corpus available. |
| 7 | **Ethan** | **Band/decision_code mapping** (spec §B.9, Gaps table): lock per deployment; final code set for flags.decision_code (e.g. SIGMA_FAIL_LEAK, GAMMA_DRIFT, THETA_SHADOW_DEV, OK) and band rules (stable|spiky|fragmented|coherent); document. | Mapping table or enum doc; lock for implementation. |

Grace may assign different owners or split (e.g. Ethan for 1–2, Gena for 3–5); update active.md when assigned.

---

## 2a. Grace check (triage vs spec)

**Check:** Implementation Plan + Gaps table (spec §Reflection on Gaps, §Implementation Plan) vs task list.

- **Task 1:** Added **fix and document N (top-N for leakage)** constant across R-levels (spec §2.2; recommend N=3). Required by spec; was missing.
- **Task 7 (new):** **Band/decision_code mapping** — spec §B.9 and Gaps table require "lock per deployment"; final code set (e.g. SIGMA_FAIL_LEAK, GAMMA_DRIFT) and band rules. Added; owner Ethan.

All other Implementation Plan items (1–6) already covered. Optional: theoretical_smoothing_change (analytic) — not added; spec says optional, add later if needed.

---

## 3. Links

- **Spec:** [docs/SPEC__Reading_Scale_Levels_R1_R4_Structural_Audit_v1_0.md](../docs/SPEC__Reading_Scale_Levels_R1_R4_Structural_Audit_v1_0.md)
- **Schemas:** [schema/Unit.schema.json](../schema/Unit.schema.json), [schema/BookProfile.schema.json](../schema/BookProfile.schema.json), [schema/SI_metrics.schema.json](../schema/SI_metrics.schema.json)
- **Deliverable fix:** [ETHAN-HESPERIA-R1-R4-DELIVERABLE-CONTEXT-FIX.md](ETHAN-HESPERIA-R1-R4-DELIVERABLE-CONTEXT-FIX.md)
- **Task rows:** [project/active.md](../project/active.md)
- **Grace check (Gena dones):** [GRACE-CHECK-GENA-R1-R4-DONES.md](GRACE-CHECK-GENA-R1-R4-DONES.md) — tasks 3, 4, 5 signed DONE.
- **Integration spec tasking:** [TASK-GRACE-R1-R4-INTEGRATION-SPEC-TRIAGE.md](TASK-GRACE-R1-R4-INTEGRATION-SPEC-TRIAGE.md) — I1 (contract), I2 (analyze wire), I3 (API/context_rag).

### 3a. Workflow deliverables (as added)

| Task | Deliverable |
|------|-------------|
| 1 | [sphere_rag/r1_r4_esm_defaults_v1_0.json](../sphere_rag/r1_r4_esm_defaults_v1_0.json), [docs/R1_R4_ESM_DEFAULTS_v1_0.md](../docs/R1_R4_ESM_DEFAULTS_v1_0.md), [sphere_rag/r1_r4_esm_defaults.py](../sphere_rag/r1_r4_esm_defaults.py) (loader) |
| 2 | [sphere_rag/r1_r4_contradiction_graph_v1_0.json](../sphere_rag/r1_r4_contradiction_graph_v1_0.json), [docs/R1_R4_CP_CONTRACT_Part_B5.md](../docs/R1_R4_CP_CONTRACT_Part_B5.md), [sphere_rag/r1_r4_contradiction_graph.py](../sphere_rag/r1_r4_contradiction_graph.py) (loader + CP) |
| 3 | [sphere_rag/r1_r4_segmenters.py](../sphere_rag/r1_r4_segmenters.py) (segment_by_sentences/paragraphs/chapters/book) + contract doc |
| 4 | [sphere_rag/r1_r4_unit.py](../sphere_rag/r1_r4_unit.py) (build_unit); [sphere_rag/r1_r4_pipeline.py](../sphere_rag/r1_r4_pipeline.py) (run_r1_pipeline) |
| 5 | [sphere_rag/r1_r4_pipeline.py](../sphere_rag/r1_r4_pipeline.py), [sphere_rag/run_r1_r4_pipeline.py](../sphere_rag/run_r1_r4_pipeline.py) |
| 7 | [docs/R1_R4_BAND_DECISION_CODE_MAPPING_v1_0.md](../docs/R1_R4_BAND_DECISION_CODE_MAPPING_v1_0.md) (locked mapping) |

---

**SIGNED: Product (Grace) | R1–R4 reading spec triage and team tasking | 2026-02-27 | governance**
