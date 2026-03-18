<!--
HESPERIA — RAD. Cursor agent entry: what is OPEN and how to proceed.
-->

# Cursor — open workflow (Hesperia repo)

## Two workflows

| Scope | What it is | How to proceed |
|-------|------------|----------------|
| **Global (multi-repo)** | Prichindel automation: `workflow_orchestrator.py` / `workflow_driver.py`, `governance/active.md`, heartbeat | Runbook: `scripts/SCRIPT-RUNBOOK-workflow-orchestrator.md` (may live outside this clone). MCP **get_current_step** can show another workspace’s row. |
| **This repo (Hesperia)** | Specs + code tasks tracked in **docs**, not `active.md` | Follow **§2 OPEN queue** below. Saying *“Cursor proceed open workflow”* in this project = **pick the next Hesperia row** and execute or scaffold. |

---

## 1. MCP note

**Pipeline status / current step** reads `workflow_driver_current.txt` from the configured repo. If you see a non-Hesperia task (e.g. another project), treat **§2** as authoritative for **this** workspace.

---

## 2. Hesperia OPEN queue (proceed order)

| Priority | Item | Location | Next action |
|----------|------|----------|-------------|
| **P1** | Ethan **post-A.6** | [TASK-GRACE-ETHAN-DYNAMICS-IMPLEMENTATION-TEAM.md](specs/governance/TASK-GRACE-ETHAN-DYNAMICS-IMPLEMENTATION-TEAM.md) | Feed **Ξ** into L7; `REPORT-ETHAN-DYNAMICS-IMPLEMENTATION.md`; optional full-hex H7/H8 |
| **P2** | Calibration registry | [assets/calibration/dynamics_parameter_registry.yaml](assets/calibration/dynamics_parameter_registry.yaml) | Expand when Phase 2 Θ added |
| **P2** | Observability extension | [TASK-GRACE-HESPERIA-OBSERVABILITY-EXTENSION.md](specs/governance/TASK-GRACE-HESPERIA-OBSERVABILITY-EXTENSION.md) | Rows in external `active.md` if used |
| **P3** | Context RAG §4.6 (L_full) | Other clone / chroma stack | Blocked on activation data unless stubbed |

**Done / reference:** Grace triage → [GRACE_TRIAGE_REPORT.md](specs/triage/GRACE_TRIAGE_REPORT.md); equation index → [DYNAMICS_EQUATION_INDEX.md](specs/DYNAMICS_EQUATION_INDEX.md).

---

## 3. Cursor proceed checklist

1. Confirm workspace = **Hesperia** root (`hesperia.engine`, `runtime/`, `docs/specs/`).  
2. Read current row in **§2** (top incomplete).  
3. Implement or document; keep **default E2E unchanged** unless task explicitly gates on env flag.  
4. Run targeted tests + `python3 -m pytest tests/ -q --tb=no -x` for smoke (adjust scope as needed).  
5. Update the task doc **Status** or a one-line **Progress** when a phase lands.

---

*Cursor open workflow — Hesperia RAD.*
