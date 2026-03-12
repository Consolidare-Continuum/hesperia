<!--
HESPERIA — Reference Architecture Definition (RAD)
Copyright © 2026 igareosh.com — Platonov Igor (aka @igareosh). All rights reserved.
Restricted Research Disclosure License. Inspection and reference only.
No reproduction, redistribution, or use without explicit written permission.
See LEGAL_NOTICE.md for full terms.
-->

# Historical reference (pre-refactor)

# Hesperia workspace — examination report

**Context**: Grace. Examination in hesperia workspace requested by boss.
**Date**: 2026-02-16.
**Scope**: Brain (CLIENTS/hesperia/), canonical workspace (/data/workspaces/atomic-commit-hesperia/), alignment and gaps.

---

## 1. Summary

| Item | Status |
|------|--------|
| **Brain (CLIENTS/hesperia/)** | Present; 51 files; v0.1 legacy + numbered specs 01–03, 10–51. DOC_INDEX, AGENTS.md, WORKSPACE.md in place. |
| **Workspace (/data/workspaces/atomic-commit-hesperia/)** | Present; git repo; last modified Feb 2026. Specs, sphere_rag, markdown (book files), statements, syzif, text_chunks, legacy, images. |
| **active.md** | No OPEN hesperia task. |
| **prichindel subfolder** | **Absent** in workspace. Docs say “ingest from …/hesperia/prichindel”; prichindel content was moved to cursor repo (prichindel/) on 2026-02-09 — ingest path likely obsolete. |
| **Doc drift (brain vs workspace)** | Brain DOC_INDEX **does not list** workspace-only docs: 04_IDEOLOGY–09_PROJECT, 16_SPEC–18_SPEC, 33_FAMILIES. Brain is behind. |

---

## 2. Brain (CLIENTS/hesperia/)

- **Location**: Repo `CLIENTS/hesperia/` (design anchor; feed Gena from here + workspace).
- **Contents**: v0.1/ (legacy HISPERIA naming), statements/, archive/, numbered specs 01–03, 10–15, 20–23, 30–32, 40–41, 50–51; ACADEMIC.md, DOC_INDEX.md, AGENTS.md, WORKSPACE.md.
- **DOC_INDEX**: Persona paths (Backend, Math, Ontology, Product RU); entry points; core specs; legacy. Does **not** reference 04–09, 16–18, 33 present in workspace.

---

## 3. Workspace (/data/workspaces/atomic-commit-hesperia/)

- **Path**: `/data/workspaces/hesperia` (prichindel; canonical).
- **Git**: Yes; remote TBD (see cluster/GITHUB-REPOS.md).
- **Root**: Specs 01–23, 30–33, 40–41, 50–51; **04_IDEOLOGY–09_PROJECT** (ideology, identity, product, operating model, agent workflow, file naming); ACADEMIC.md, DOC_INDEX.md, AGENTS.md, README.md, VARIABLES.md; .env; CSV matrices; tools script; HISPERIDES.png.
- **Dirs**: markdown/ (book-named .md), sphere_rag/, statements/, syzif/, text_chunks/, legacy/, images/.
- **prichindel**: Not present. Ingest note in WORKSPACE.md/CLIENTS.md refers to `/data/workspaces/atomic-commit-hesperia`; prichindel was moved into cursor repo 2026-02-09 — update or drop that ingest note.

---

## 4. Findings (triage)

| # | Finding | Severity | Action |
|---|---------|----------|--------|
| 1 | Brain DOC_INDEX missing 04–09, 16–18, 33 | Medium | Update DOC_INDEX (and persona paths if needed) so brain matches workspace. |
| 2 | Ingest “from hesperia/prichindel” obsolete | Low | Update WORKSPACE.md and CLIENTS.md: remove or replace with “prichindel in cursor repo”. |
| 3 | No OPEN hesperia task in active.md | Info | If work is planned, Grace to add row after triage. |
| 4 | .env at workspace root; docs cite sphere/hesperia/.env | Low | Confirm canonical key location (root vs sphere/hesperia); update GITHUB-REPOS / ABELARD_QUICK_OPS if root is canonical. |

---

## 5. Recommendations (Grace)

1. **Sync brain to workspace**: Assign (e.g. Gena or Cursor) to update CLIENTS/hesperia/DOC_INDEX.md (and optional ACADEMIC/AGENTS) so that 04–09, 16–18, 33 are reflected; optionally ingest new spec text into brain from workspace where useful.
2. **Docs cleanup**: Update WORKSPACE.md and CLIENTS.md: prichindel ingest path — either remove or point to cursor repo prichindel/.
3. **Tasking**: If boss wants a dedicated hesperia task (e.g. “Hesperia: sync brain DOC_INDEX and ingest notes”), Grace adds one row to active.md and assigns owner.

---

**SIGNED: Product/Triage (Grace) | hesperia workspace examination | 2026-02-16 | CLIENTS/hesperia**
