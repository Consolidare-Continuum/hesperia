# Hesperia repo structure

**Canonical repo**: git@github.com:Atomic-Commits-Team/hesperia.git (old igareosh/hesperia unlinked)

**Repo-wide ORDER:** See **[ORDER.md](ORDER.md)** — naming (4 words + version), specs at root, Python in one place, artifacts in subfolders.

- **Root** — Specs (numbered `NN_*_vX_Y`), ORDER.md, AGENTS.md, high-level docs. All specs findable from root.
- **artifacts/** — All produced outputs: `e2e/`, `layer_runs/`, `calibration/`, `lex/`. No run outputs in docs/ or root.
- **sphere_rag/** — Core Python (analyze, attribution, layers, guards, R1–R4). Single place for engine code.
- **api/** — Service entrypoints.
- **scripts/** — One-off / ops scripts (guards, calibration, verify).
- **hesperia_lex/** — Lexical builds; scripts under `hesperia_lex/scripts/`.
- **governance/** — Team governance: waterline principle, state-now, core-mode, operator interface, loop safeguard, RAG daemon, semantic engine, tasks, context RAG schema.
- **project/** — CONTEXT-PACKET, RELEASE-V1-FIXED-POINT, observability extension, charter, scope.
- **specs/** — README pointing to root specs; optional future specs with same naming rule.
