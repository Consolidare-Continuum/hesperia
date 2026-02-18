# ARCH-DECISION — hesperia

**Purpose**: Project boundary, artifact scope, WBS for task division. One per project. Ref: [ROLE-RESOLUTIONS.md](../../ROLE-RESOLUTIONS.md) (Ethan).

---

**Decision**: Hesperia project boundary = governance (projects/hesperia/) + design anchor (CLIENTS/hesperia/) + canonical codebase (/data/workspaces/hesperia/). No new service boundary, DB, or API model in this project — specs and code live in brain and workspace; project folder holds charter, context, and task linkage only. Task division (Grace) may proceed for work on specs, doc sync, or code in CLIENTS/hesperia and workspace.

**Reason**: Hesperia is prichindel.com product (charter); execution = doc updates, spec alignment, or code per assigned leads; no separate deployable service boundary in repo.

**Impact**: Leads work in CLIENTS/hesperia/ or /data/workspaces/hesperia/ as assigned; ARCH-DECISION does not introduce DB/API/integration scope unless a later change adds it.

**Approved**: Ethan  2026-02-16

---

## WBS Boundary Approval

**Status**: APPROVED

**Approved by**: Ethan

**Date**: 2026-02-16

**Rule**: No lead assignment (task division) before this section = APPROVED. Grace may now divide tasks for hesperia when execution is requested.

---

## Integration contract (if integration exists)

N/A — no integration scope in this project.
