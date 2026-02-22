# Context packet — hesperia

**Purpose**: Single place for project context. **Mandatory and gate-bound**: Grace creates; Ethan approves with WBS. No task division until approved. Ref: [OPERATIONAL-LAYER.md](../../OPERATIONAL-LAYER.md).

---

## 1. Project summary

- **One sentence**: Hesperia is the prichindel.com semantic-substrate product (HESPERIA specs, sphere, RAG, indexing, families); owned by igareosh; from 0 to hero under prichindel.com brand.
- **State now (what it is / what it does)**: Hesperia is a **geometry-safe semantic traversal kernel** (deterministic semantic traversal and validation core). It already provides: fixed geometry, deterministic ring traversal, border tracking, context packet with adjacency hints, logic layer + safeguard, apple coverage; context governor, path validation, coverage verification. Structure-only; no semantic reasoning yet. Full statement: [governance/ETHAN-HESPERIA-STATE-NOW-ASSESSMENT.md](../../governance/ETHAN-HESPERIA-STATE-NOW-ASSESSMENT.md).
- **Owner (product)**: Grace (triage); **authority**: igareosh (Platonov Igor).
- **Architecture**: Ethan (WBS, boundaries when execution starts).

## 2. Scope (what's in / out)

- **In scope**: Specs and codebase in CLIENTS/hesperia/ and /data/workspaces/atomic-commit-hesperia/; project governance in projects/hesperia/; task rows in active.md when Grace assigns; delivery and IP under prichindel.com / igareosh.
- **Out of scope**: Transfer of ownership or brand rights; external client handover without explicit approval.

### 2.1 Sync in repo (current phase)

- **Sync in repo** = **documentation, description, and scripting only**. What gets synced (workspace → brain / repo): numbered specs, DOC_INDEX, AGENTS, WORKSPACE, sphere_rag scripts, runbooks, description docs — **not** book content.
- **Exclude from sync**: **Book .md files in `syzif/` folder** (book markdowns stay in workspace only; do not sync into cursor repo / brain as part of hesperia repo content).
- **Semantic layer**: **Not in scope yet.** No semantic layer (RAG, semantic engine, indexing, families ingestion) for now — documentation and scripting only.
- **Agents use of matrix (cursor repo)**: Use of Hesperia matrix in the cursor repo (Chroma layer hesperia_families, matrix_run, schema) for Albina and Cursor agents is **cursor-repo scope**, not the Hesperia product semantic layer. Ref: [governance/HESPERIA-AGENTS-PATH-ETHAN-REPORT.md](../../governance/HESPERIA-AGENTS-PATH-ETHAN-REPORT.md).
- **Reference**: [SCOPE-AND-SYNC.md](SCOPE-AND-SYNC.md) in this folder.

## 3. Key decisions and refs

- **ARCH-DECISION**: [ARCH-DECISION.md](ARCH-DECISION.md) — added 2026-02-16; WBS = APPROVED.
- **Day context (2026-02-17)**: [governance/NARRATIVE-HESPERIA-TASKS-2026-02-17.md](../../governance/NARRATIVE-HESPERIA-TASKS-2026-02-17.md) — narrative of wire-to-FPF, apple scripts, multiple loop runs, self-analysis, informatics plan, boundaries.
- **INTEGRATION-CONTRACT**: N/A unless external integration introduced.
- **Design/code**: [CLIENTS/hesperia/](../../CLIENTS/hesperia/) (brain), [CLIENTS/hesperia/WORKSPACE.md](../../CLIENTS/hesperia/WORKSPACE.md), workspace `/data/workspaces/atomic-commit-hesperia/`.

## 4. Roles / owners (this project)

| Area         | Lead   | Note                          |
|--------------|--------|-------------------------------|
| Product      | Grace  | Scope, triage, release       |
| Architecture| Ethan  | WBS, CONTEXT-PACKET approval  |
| Backend      | Olivia | After WBS + schema + freeze  |
| Frontend     | Ava    | After API frozen             |
| Database     | Marcus | Schema, policy               |
| DevOps       | Sophia | Infra duration, deploy       |
| Automation  | Liam   | Scripts, runbooks            |
| Security     | Daniel | Baseline, release gate       |
| AI          | Noah   | If applicable                |
| Integration  | Emma   | If external API              |

Execution starts only after gates (CONTEXT-PACKET approved, Infra Duration filled).

## 5. Key links

- Project folder: `projects/hesperia/`
- **Start from here (fixed point)**: [RELEASE-V1-FIXED-POINT-2026-02-18.md](RELEASE-V1-FIXED-POINT-2026-02-18.md) — V1 fixed point 2026-02-18; Cursor main invoker of Hesperia; consolidated state; backup in `archive/hesperia-fixed-point-20260218/`. All new Hesperia work starts from this baseline.
- **Observability extension (safe evolution)**: [HESPERIA_OBSERVABILITY_EXTENSION_v0_1.md](HESPERIA_OBSERVABILITY_EXTENSION_v0_1.md) — loopability band, entropy, observability fields only; no geometry/traversal/safeguard/core refactor. Ethan. 2026-02-18.
- **Post v0.1 (Ethan)**: [governance/ETHAN-HESPERIA-POST-V01-FORMAL-DEFINITIONS.md](../../governance/ETHAN-HESPERIA-POST-V01-FORMAL-DEFINITIONS.md) — formal governance equation, obstacleScore composition, decision state machine, or risk analysis of premature control. Definition only.
- **Waterline principle (capacity doctrine)**: [governance/ETHAN-HESPERIA-WATERLINE-PRINCIPLE.md](../../governance/ETHAN-HESPERIA-WATERLINE-PRINCIPLE.md) — waterLevel equation and above‑water cut rule; governance/decision layer above v0.1; definition only (no kernel wiring).
- **State now (what it is, what it does)**: [governance/ETHAN-HESPERIA-STATE-NOW-ASSESSMENT.md](../../governance/ETHAN-HESPERIA-STATE-NOW-ASSESSMENT.md) — geometry-safe traversal kernel; deterministic validation core; do not touch list; fork A/B/C/D; lock one spec. Ethan. 2026-02-18.
- **Mid-stage product report (internal and external)**: [HESPERIA-MID-STAGE-PRODUCT-REPORT.md](HESPERIA-MID-STAGE-PRODUCT-REPORT.md) — consolidation of done, needed, and direction. Grace. 2026-02-18.
- Charter: [PROJECT-CHARTER.md](PROJECT-CHARTER.md)
- Handoff: [HANDOFF-CHECKLIST.md](HANDOFF-CHECKLIST.md)
- Brain: [CLIENTS/hesperia/](../../CLIENTS/hesperia/)
- Workspace: /data/workspaces/atomic-commit-hesperia/ (prichindel)
- **Agents-oriented path (Ethan)**: [governance/TASK-ETHAN-HESPERIA-AGENTS-PATH.md](../../governance/TASK-ETHAN-HESPERIA-AGENTS-PATH.md) — address Gena developments, consolidate opinion, propose realistic deployable agents path per foundations.

---

## Approval (gate-bound)

- [x] **CONTEXT-PACKET approved** (Ethan, with WBS). Date: 2026-02-16
- **Rule**: No task division until this box is checked and WBS = APPROVED in ARCH-DECISION.
