# Historical reference (pre-refactor)

# Task: Grace — R1–R4 integration spec triage and tasking

**Purpose:** After Gena’s R1–R4 pipeline dones (tasks 3, 4, 5), Grace tasks the team on **integration**: how the R1–R4 pipeline, Units, and BookProfile plug into existing analyze, context_rag, API, and guard flow. **Owner:** Grace. **Added:** 2026-02-27.

**Refs:** [GRACE-CHECK-GENA-R1-R4-DONES.md](GRACE-CHECK-GENA-R1-R4-DONES.md), [TASK-GRACE-R1-R4-READING-SPEC-TRIAGE.md](TASK-GRACE-R1-R4-READING-SPEC-TRIAGE.md), [docs/NEXT_STEPS_MATH_INTEGRATION.md](../docs/NEXT_STEPS_MATH_INTEGRATION.md).

---

## 1. Scope (Grace)

- **Integration** = contract and/or wiring of R1–R4 pipeline (Units, BookProfile) with:
  - **analyze** (e.g. `sphere_rag/analyze.py`, `analyze_v033`): optional R1–R4 path or callback.
  - **context_rag** (if present): whether BookProfile or level_averages are exposed in context packet.
  - **API** (e.g. `api/main.py`): optional endpoint or response field for reading-scale output.
  - **Guards (Σ/Γ/Θ):** how Unit.flags.decision_code / SI_metrics feed into guard pipeline (reference only or wired).
- **Deliverable:** Integration spec (short doc: contract, entry points, optional wiring tasks). No mandatory code change until tasks are assigned and implemented.

---

## 2. Team tasking (Grace)

| # | Owner | Task | Deliverable |
|---|--------|------|-------------|
| I1 | **Ethan** | **R1–R4 integration contract** — One-page spec: entry points (run_full_pipeline, run_r1_pipeline), inputs (text, book_id, levels), outputs (Units, BookProfile); where they may be consumed (analyze, context_rag, API); guard integration (Σ/Γ/Θ) as reference or wire. | **Done:** [docs/R1_R4_INTEGRATION_CONTRACT.md](../docs/R1_R4_INTEGRATION_CONTRACT.md) |
| I2 | **Gena** (or implementation) | **Wire R1–R4 into analyze (optional)** — If integration contract specifies an analyze path: add optional flag or mode to run R1–R4 pipeline and attach Units/BookProfile to result or to a dedicated key. Document in analyze/runbook. | Code + short doc, or “deferred” if contract says optional. |
| I3 | **Gena** (or implementation) | **API / context_rag (optional)** — If contract specifies API or context_rag: add optional response field or context block for BookProfile or level_averages; or document “not wired” and leave for later. | Code or doc note. |

Grace may assign different owners or collapse I2/I3; update [project/active.md](../project/active.md) when assigned.

---

## 3. Links

- Gena dones check: [GRACE-CHECK-GENA-R1-R4-DONES.md](GRACE-CHECK-GENA-R1-R4-DONES.md)
- R1–R4 triage: [TASK-GRACE-R1-R4-READING-SPEC-TRIAGE.md](TASK-GRACE-R1-R4-READING-SPEC-TRIAGE.md)
- Pipeline: [sphere_rag/r1_r4_pipeline.py](../sphere_rag/r1_r4_pipeline.py), [sphere_rag/run_r1_r4_pipeline.py](../sphere_rag/run_r1_r4_pipeline.py)
- Task rows: [project/active.md](../project/active.md) (§ R1–R4 integration)

---

**SIGNED: Product (Grace) | R1–R4 integration spec tasking | 2026-02-27 | governance**
