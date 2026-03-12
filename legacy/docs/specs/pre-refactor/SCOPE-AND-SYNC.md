<!--
HESPERIA — Reference Architecture Definition (RAD)
Copyright © 2026 igareosh.com — Platonov Igor (aka @igareosh). All rights reserved.
Restricted Research Disclosure License. Inspection and reference only.
No reproduction, redistribution, or use without explicit written permission.
See LEGAL_NOTICE.md for full terms.
-->

# Historical reference (pre-refactor)

# Hesperia — scope and sync (Grace)

**Purpose**: What is synced into repo and what is in scope for the current phase. Single place for sync and scope rules. **Owner**: Grace.

**Updated**: 2026-02-16

---

## Current phase: documentation and scripting only

- **Sync in repo** = **documentation, description, and scripting only**.
  - **Include**: Numbered specs (01_*–51_*, etc.), DOC_INDEX.md, AGENTS.md, WORKSPACE.md, ACADEMIC.md; sphere_rag/ (scripts, runbooks); description and ideology/identity/product docs; tool scripts. All of that may be synced workspace ↔ brain (CLIENTS/hesperia/) as needed.
  - **Exclude**: **Book .md files in `syzif/` folder.** Book markdowns (e.g. book-named .md in workspace `syzif/` or equivalent) are **not** synced into the cursor repo / brain as hesperia content. They remain in the workspace only.
- **Semantic layer**: **Not in scope yet.** No semantic layer (RAG, semantic engine, indexing, families ingestion, Chroma for hesperia content) for this phase. Documentation and scripting only.
- **Agents use of matrix (cursor repo)**: Use of Hesperia matrix in the **cursor repo** (Chroma layer hesperia_families, matrix_run, schema) for Albina and Cursor agents is **cursor-repo scope**, not the Hesperia product semantic layer. Product semantic layer remains not in scope. Ref: [governance/HESPERIA-AGENTS-PATH-ETHAN-REPORT.md](../../governance/HESPERIA-AGENTS-PATH-ETHAN-REPORT.md).

---

## When this changes

Grace updates this file and CONTEXT-PACKET §2.1 when scope or sync rules change (e.g. when semantic layer or book ingestion is added).
