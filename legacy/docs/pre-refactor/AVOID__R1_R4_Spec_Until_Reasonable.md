<!--
HESPERIA — Reference Architecture Definition (RAD)
Copyright © 2026 igareosh.com — Platonov Igor (aka @igareosh). All rights reserved.
Restricted Research Disclosure License. Inspection and reference only.
No reproduction, redistribution, or use without explicit written permission.
See LEGAL_NOTICE.md for full terms.
-->

# Historical reference (pre-refactor)

# R1–R4 spec and sphere_math — reason isolated, mitigated (usual mode)

**Status:** Mitigated. Reason isolated; common efforts in place (Ethan deliverable fix, Grace triage/tasking). We proceed in usual mode under these rules.

**Background:** Cursor decoding loop was tied to this spec (table-fill) and large sphere_math output. See `docs/FINDINGS__Cursor_Decoding_Loop_2026-02-27.md` and **AGENTS.md §5a**.

**When using R1–R4 or sphere_math:**

- **R1–R4 spec** (`docs/SPEC__Reading_Scale_Levels_R1_R4_Structural_Audit_v1_0.md`): Outputs = JSON per schema only; do not ask model to fill or emit spec tables (reference only). Generate tables from JSON if needed.
- **sphere_math_100_sentences:** Do not attach full file as context; use `--limit N`, single-sentence run, or summary.

**Deliverable fix (Ethan):** [governance/ETHAN-HESPERIA-R1-R4-DELIVERABLE-CONTEXT-FIX.md](../governance/ETHAN-HESPERIA-R1-R4-DELIVERABLE-CONTEXT-FIX.md). **Team tasking:** [TASK-GRACE-R1-R4-READING-SPEC-TRIAGE.md](../governance/TASK-GRACE-R1-R4-READING-SPEC-TRIAGE.md), [project/active.md](../project/active.md).
