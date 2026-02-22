# Hesperia repo structure

**Canonical repo**: git@github.com:Atomic-Commits-Team/hesperia.git (old igareosh/hesperia unlinked)

- **Root** — Specs, docs, data from cursor `CLIENTS/hesperia` (brain/canonical source).
- **governance/** — Team governance: waterline principle, state-now, core-mode, operator interface, loop safeguard, RAG daemon, semantic engine, tasks, context RAG schema. Source: cursor `governance/*HESPERIA*`, `CONTEXT-RAG-PACKET-SCHEMA`.
- **project/** — Project folder: CONTEXT-PACKET, RELEASE-V1-FIXED-POINT, observability extension, charter, scope. Source: cursor `projects/hesperia/`.
- **scripts/** — Hesperia logic, matrix_run, context_rag, ingest, safeguard stress test, and Σ/Γ/Θ guard modules (`sigma_guard.py`, `gamma_guard.py`, `theta_gate.py`). Source: cursor `cluster/chroma-server/`.
