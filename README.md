# HESPERIA (HSPR)

**Version**: v0.3.0 (tag `hesperia-v0.3.0`)  
**Status**: Release approved. Deterministic core + lexical stack. Freeze: do not change core math without version bump.

## What v0.3 is

- **Deterministic** surface-energy pipeline: fusion (Dict A + Dict B → E0), centroid selection, base traversal, aggregation → dominant family/area, penalties, metrics.
- **Controlled** lexical layer: Dict A (core star map), Dict B (surface lex field); Spec 20 (side_id only in A); validation and CI.
- **Stub topology** only: 72 sides, 12 areas, 6 families/area; no adjacency or membership from Chroma unless explicitly ingested (see TOPOLOGY-STORAGE-CONTRACT).
- **Books non-voting**: Evidence retrieval after resolution only; I-Q2 enforced (metrics unchanged with/without books).

No big dict files in repo: `raw/`, `processed/`, `assets/` are gitignored. Curated A/B (small JSON) are in `hesperia_lex/curated/`. Install: [hesperia_lex/INSTALL-LEXICAL.md](hesperia_lex/INSTALL-LEXICAL.md).

## Entry points

| Item | Path |
|------|------|
| Core math contract | [22_SPEC__V0_3_Core_Math_Contract_v1_0.md](22_SPEC__V0_3_Core_Math_Contract_v1_0.md) |
| Config | [guard_config_v1.json](guard_config_v1.json) |
| Full run (stub) | [sphere_rag/full_run_simulation.py](sphere_rag/full_run_simulation.py) |
| Chroma books validation | [sphere_rag/chroma_books_validation_run.py](sphere_rag/chroma_books_validation_run.py) |
| Run entry | [sphere_rag/run_simulation.py](sphere_rag/run_simulation.py) (`full` / `chroma`) |
| Lexical stack | [hesperia_lex/README.md](hesperia_lex/README.md) |
| Topology contract | [hesperia_lex/TOPOLOGY-STORAGE-CONTRACT.md](hesperia_lex/TOPOLOGY-STORAGE-CONTRACT.md) |
| Release gate report | [docs/HESPERIA_V03_RELEASE_GATE_REPORT.md](docs/HESPERIA_V03_RELEASE_GATE_REPORT.md) |
| Doc index | [DOC_INDEX.md](DOC_INDEX.md) |

## Next (v0.4 territory)

Expanding lexical size, adjacency ingestion, scaling Chroma topology — structural invariants tested for real. Not in v0.3 scope.
