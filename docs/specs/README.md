<!--
HESPERIA — Reference Architecture Definition (RAD)
Copyright © 2026 igareosh.com — Platonov Igor (aka @igareosh). All rights reserved.
Restricted Research Disclosure License. Inspection and reference only.
No reproduction, redistribution, or use without explicit written permission.
See LEGAL_NOTICE.md for full terms.
-->

# Specs — findable from root

**Canonical specs** live at **repo root** with the pattern:

- `NN_CATEGORY__Title_vX_Y.txt` (or `.md`)
- Example: `10_MASTER_SPEC__HESPERIA_v1_0.txt`, `42_POLICY__Guard_Layer_Sigma_Gamma_Theta_v1_0.txt`

**Naming rule (see [ORDER.md](../ORDER.md)):** Human-readable, **up to 4 words** in the title part, plus version `_vX_Y`.

**This folder** can hold future specs if you want them under one tree; same naming rule. Do not add specs without a version.

| Doc | Role |
|-----|------|
| [ETHAN_SEMANTIC_FIELD_DYNAMICS_SPEC.md](ETHAN_SEMANTIC_FIELD_DYNAMICS_SPEC.md) | **Part A:** L0–L10 pipeline wire, **H0–H9** compact equations, phases 1–4, artifact map. **Part B:** hex lattice, extended IDs, active subgraph doctrine. |
| [DYNAMICS_EQUATION_INDEX.md](DYNAMICS_EQUATION_INDEX.md) | **Implementer cheat sheet:** compact H0–H9 ↔ extended IDs ↔ L-layers ↔ phased rollout. |
| [governance/TASK-GRACE-ETHAN-DYNAMICS-IMPLEMENTATION-TEAM.md](governance/TASK-GRACE-ETHAN-DYNAMICS-IMPLEMENTATION-TEAM.md) | **Grace + team:** phased implementation of Ethan dynamics (Phases 1–4), roles, acceptance, deliverables. |
| [governance/ETHAN-OPEN-WORKFLOW-PROCEED.md](governance/ETHAN-OPEN-WORKFLOW-PROCEED.md) | **Ethan:** open-workflow proceed (Phase 2+ shipped items). |
| [HESPERIA_DYNAMICS_CALIBRATION_SPEC_v0_1.md](HESPERIA_DYNAMICS_CALIBRATION_SPEC_v0_1.md) | **Calibration by design:** Class A/B/C, ranges, constraints, objectives, scenario suite, staged search, sensitivity, release profiles; automation proposes, governance accepts. |
| [calibration/](calibration/) | Example registry fragment + README for future YAML suites. |
| [TRIAGE_TASK_GRACE.md](TRIAGE_TASK_GRACE.md) | **Grace:** triage task for the spec corpus (dynamics, calibration, product maps, awareness). |
| [triage/](triage/) | Triage report landing — [GRACE_TRIAGE_REPORT.md](triage/GRACE_TRIAGE_REPORT.md). |
| [TRIAGE_CHECKLIST.md](TRIAGE_CHECKLIST.md) | Optional checkbox tracker for the Grace corpus. |

**Hub:** [HESPERIA_SYSTEM_AWARENESS.md](../HESPERIA_SYSTEM_AWARENESS.md) — system & product awareness. **Root numbered specs:** [ORDER.md](../ORDER.md). **Cursor proceed:** [CURSOR_OPEN_WORKFLOW.md](../CURSOR_OPEN_WORKFLOW.md).
