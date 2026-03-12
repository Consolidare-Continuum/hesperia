<!--
HESPERIA — Reference Architecture Definition (RAD)
Copyright © 2026 igareosh.com — Platonov Igor (aka @igareosh). All rights reserved.
Restricted Research Disclosure License. Inspection and reference only.
No reproduction, redistribution, or use without explicit written permission.
See LEGAL_NOTICE.md for full terms.
-->

# Handoff checklist — hesperia

**Purpose**: No handoff without artifact + stored + READY + **signed** + approved. Ref: [OPERATIONAL-LAYER.md](../../OPERATIONAL-LAYER.md) §I, [governance/ARTIFACT-SIGNATURE-POLICY.md](../../governance/ARTIFACT-SIGNATURE-POLICY.md).

**Signature**: Every handoff artifact must end with: `SIGNED: ROLE (Name) | Context | YYYY-MM-DD | Scope`.

When all leads mark **READY-FOR-REVIEW**, Grace creates RELEASE-CHECKLIST.md.

---

## Gates (no assignment until)

- [x] CONTEXT-PACKET approved (Ethan, with WBS). Date: 2026-02-16
- [x] WBS Boundary Approval (Ethan) — ARCH-DECISION.md. Date: 2026-02-16
- [ ] Scope Approved (Grace)
- [ ] Schema Ready (Marcus) — if applicable
- [x] Infra Duration filled (Sophia) — SCHEDULE-BASELINE ## Infra Duration Estimate. Date: 2026-02-16
- [ ] Integration contract FROZEN (Ethan) — if applicable

---

## Handoffs

| From | To | Artifact | Created | Stored | Signed | Approved | Date |
|------|-----|----------|---------|--------|--------|----------|------|
| Grace | Ethan | Scoped project | ☐ | ☐ | ☐ | ☐ | |
| Ethan | Olivia | ARCH-DECISION, API | ☐ | ☐ | ☐ | ☐ | |
| Ethan | Marcus | DB selection, WBS data | ☐ | ☐ | ☐ | ☐ | |
| Ethan | Noah | Arch boundaries | ☐ | ☐ | ☐ | ☐ | |
| Ethan | Sophia | Infra requirements | ☐ | ☐ | ☐ | ☐ | |
| Marcus | Olivia | Schema, migration | ☐ | ☐ | ☐ | ☐ | |
| Olivia | Ava | API contract (frozen) | ☐ | ☐ | ☐ | ☐ | |
| Ava | Sophia | Build, env vars, runtime | ☐ | ☐ | ☐ | ☐ | |
| Leads | Sophia | Build artifacts | ☐ | ☐ | ☐ | ☐ | |
| Daniel | Grace | Security cleared | ☐ | ☐ | ☐ | ☐ | |
| Sophia | You | RELEASE-NOTICE | ☐ | ☐ | ☐ | ☐ | |

(Add rows as needed for this project.)
