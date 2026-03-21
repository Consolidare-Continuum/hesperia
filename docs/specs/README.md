<!--
HESPERIA — Reference Architecture Definition (RAD)
Copyright © 2026 igareosh.com — Platonov Igor (aka @igareosh). All rights reserved.
Restricted Research Disclosure License. Inspection and reference only.
See LEGAL_NOTICE.md for full terms.
-->

# Specs hub (under `docs/specs/`)

**Task 2 split:** **binding** specifications now live under repo-root **`specs/`** (`specs/canon/`, `specs/dynamics/`, `specs/release/`, …).  
This directory keeps **process, triage, governance, and project** notes (descriptive / workflow — not core math canon).

## Where to look first

| Need | Location |
|------|-----------|
| v0.5 normative canon (math + YAML) | **[specs/canon/](../../specs/canon/README.md)** |
| Dynamics / calibration long-form | **[specs/dynamics/](../../specs/dynamics/)** |
| Release narratives | **[specs/release/](../../specs/release/)** |
| R1–R4 JSON schemas | **[specs/schemas/r1_r4/](../../specs/schemas/r1_r4/)** |
| Calibration examples | **[specs/calibration/](../../specs/calibration/)** |
| Repo topology policy | **[REPO_STRUCTURE_POLICY.md](../../REPO_STRUCTURE_POLICY.md)** |
| Multi-plane output calibration (TFP bundle) | **[output_calibration_contract_v1.md](output_calibration_contract_v1.md)** · [migration](output_calibration_migration_v1.md) |

**Engine Dynamics v0.5 index:** [HESPERIA_v0_5_ENGINE_DYNAMICS.md](../HESPERIA_v0_5_ENGINE_DYNAMICS.md) · [canonical naming](../ENGINE_DYNAMICS_CANONICAL_NAMING_v0.5.md).

## Moved dynamics docs (same filenames)

| Doc | New path |
|-----|----------|
| ETHAN_SEMANTIC_FIELD_DYNAMICS_SPEC.md | [specs/dynamics/ETHAN_SEMANTIC_FIELD_DYNAMICS_SPEC.md](../../specs/dynamics/ETHAN_SEMANTIC_FIELD_DYNAMICS_SPEC.md) |
| FIELD_MATRIX_BUILDERS_v1.md | [specs/dynamics/FIELD_MATRIX_BUILDERS_v1.md](../../specs/dynamics/FIELD_MATRIX_BUILDERS_v1.md) |
| HSPR_CALIBRATION_INDEX_v1.md | [specs/dynamics/HSPR_CALIBRATION_INDEX_v1.md](../../specs/dynamics/HSPR_CALIBRATION_INDEX_v1.md) |
| semantic_field_dynamics.md (canonical) | [specs/dynamics/semantic_field_dynamics.md](../../specs/dynamics/semantic_field_dynamics.md) |
| DYNAMICS_EQUATION_INDEX.md | [specs/dynamics/DYNAMICS_EQUATION_INDEX.md](../../specs/dynamics/DYNAMICS_EQUATION_INDEX.md) |
| HESPERIA_DYNAMICS_CALIBRATION_SPEC_v0_1.md | [specs/dynamics/HESPERIA_DYNAMICS_CALIBRATION_SPEC_v0_1.md](../../specs/dynamics/HESPERIA_DYNAMICS_CALIBRATION_SPEC_v0_1.md) |

## Still under `docs/specs/` (workflow / triage only)

Governance task logs and project memos were moved to **`docs/governance/working/`** and **`docs/governance/project/`** so this tree stays triage-centric.

| Doc | Role |
|-----|------|
| [TRIAGE_TASK_GRACE.md](TRIAGE_TASK_GRACE.md) | Grace triage task |
| [triage/GRACE_TRIAGE_REPORT.md](triage/GRACE_TRIAGE_REPORT.md) | Triage report |
| [TRIAGE_CHECKLIST.md](TRIAGE_CHECKLIST.md) | Optional checklist |

**Ethan / Grace working docs:** [docs/governance/working/](../governance/working/) (e.g. `TASK-GRACE-ETHAN-DYNAMICS-IMPLEMENTATION-TEAM.md`, `ETHAN-OPEN-WORKFLOW-PROCEED.md`).

**Hub:** [HESPERIA_SYSTEM_AWARENESS.md](../HESPERIA_SYSTEM_AWARENESS.md) · **Cursor proceed:** [CURSOR_OPEN_WORKFLOW.md](../CURSOR_OPEN_WORKFLOW.md).
