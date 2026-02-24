# HESPERIA (HSPR)

**Version**: v0.4.0 (tag `hesperia-v0.4.0`)
**Status**: v0.4 consolidation. First full L1–L9 stack; run → output → logged → reportable. Deterministic core + lexical stack. Freeze: do not change core math without version bump.

**Release notes**: [RELEASE_NOTES__v0_4.txt](RELEASE_NOTES__v0_4.txt) | [releases/hesperia-v0.4.md](releases/hesperia-v0.4.md)

**Releases:** [v0.4.0](https://github.com/Atomic-Commits-Team/hesperia/releases/tag/hesperia-v0.4.0) (current on main).

## What v0.4 is

- **Full layer stack L1–L9** (34_SPEC … 42_SPEC): instrumentation → geometric traversal → shadow divergence → book evidence → counter-evidence + trig → conceptual math → cross-layer aggregates → units/i18n → human reference & brand. Standard: run layer math → output → logged → reportable.
- **Deterministic** surface-energy pipeline (v0.3): fusion (Dict A + Dict B → E0), centroid selection, base traversal, aggregation → dominant family/area, penalties, metrics.
- **Controlled** lexical layer: Dict A (core star map), Dict B (surface lex field); Spec 20 (side_id only in A); validation and CI.
- **Stub topology** only: 72 sides, 12 areas, 6 families/area; no adjacency or membership from Chroma unless explicitly ingested (see TOPOLOGY-STORAGE-CONTRACT).
- **Books non-voting**: Evidence retrieval after resolution only; I-Q2 enforced (metrics unchanged with/without books).

No big dict files in repo: `raw/`, `processed/`, `assets/` are gitignored. Curated A/B (small JSON) are in `hesperia_lex/curated/`. Install: [hesperia_lex/INSTALL-LEXICAL.md](hesperia_lex/INSTALL-LEXICAL.md).

## How to build

From `CLIENTS/hesperia` (this directory). Python 3.9+. For v0.4.0/v0.4.1 lexical builds: `pip install -r requirements_v040.txt` (or use `.venv_v040`). Layer stack needs no separate build.

- **v0.4.0**: `python -m sphere_rag.build_v040 --assets-root hesperia_lex/curated --out-dir assets/v040 --allow-small-build`
- **v0.4.1**: `python -m sphere_rag.build_v041 --assets-root assets --out-dir assets/v041 --allow-small-build`
- **Pre-test**: `python scripts/run_hesperia_pre_test.py` or `python sphere_rag/run_simulation.py pretest`

See [RUNNABLE.md](RUNNABLE.md) and [RELEASE_NOTES__v0_4.txt](RELEASE_NOTES__v0_4.txt).

## How to use

- **Full L1–L9 pass**: `mkdir -p docs/layer_runs` then  
  `python3 -m sphere_rag.layers.run_l1_through_l9 --out docs/layer_runs/latest_L1_L9_output.json`
- **L1+L2 / L1+L2+L3**: `python3 -m sphere_rag.layers.run_l1_l2` / `run_l1_l2_l3` (see RUNNABLE.md).
- **Core math**: `python sphere_rag/hesperia_v03_core_math.py` or `... test`
- **Simulation / API**: `python sphere_rag/run_simulation.py full|chroma|serve [options]`; serve: `python sphere_rag/serve_v033.py`

## What's expected

- **Determinism**: Same inputs (attribution, topology, defaults) → same L1–L9 outputs. No LLM in layer math.
- **Output**: Full pass → one JSON (all layers) in `docs/layer_runs/`; L7 status/tag and L9 brand words are reportable.
- **Stub run**: Without retrieval (R_B/R_S empty), L4/L5 evidence zero, L9 may show FRAGILE/UNSUPPORTED — expected. With Dict A/B and Chroma, values populate.

## Core (consolidated)

**Core** = 22_SPEC (resolution) + 34–42 (L1–L9) + LAYER_1_9_PREDEFINED_DEFAULTS + frozen Dict A/B; guard_config for pipeline. [docs/CORE_CONSOLIDATION.md](docs/CORE_CONSOLIDATION.md).

## Entry points

| Item | Path |
|------|------|
| **Core consolidation** (what is core, config map, frozen manifest) | [docs/CORE_CONSOLIDATION.md](docs/CORE_CONSOLIDATION.md) |
| Governance charter (canonical) | [00_GOVERNANCE_CHARTER__HESPERIA_v1_0.txt](00_GOVERNANCE_CHARTER__HESPERIA_v1_0.txt) |
| Core math contract | [22_SPEC__V0_3_Core_Math_Contract_v1_0.md](22_SPEC__V0_3_Core_Math_Contract_v1_0.md) |
| L1–L9 predefined defaults (thresholds, topology) | [LAYER_1_9_PREDEFINED_DEFAULTS_v1_0.txt](LAYER_1_9_PREDEFINED_DEFAULTS_v1_0.txt), [layer_1_9_predefined_defaults_v1_0.json](layer_1_9_predefined_defaults_v1_0.json) |
| Layer-1 instrumentation (v0.4.x) | [34_SPEC__V0_4_Layer1_Instrumentation_25_Variables_v1_0.txt](34_SPEC__V0_4_Layer1_Instrumentation_25_Variables_v1_0.txt) |
| Layer-2 geometric traversal (v0.4.x) | [35_SPEC__V0_4_Layer2_Geometric_Traversal_25_Variables_v1_0.txt](35_SPEC__V0_4_Layer2_Geometric_Traversal_25_Variables_v1_0.txt) |
| Layer-3 shadow divergence (v0.4.x) | [36_SPEC__V0_4_Layer3_Shadow_Divergence_25_Variables_v1_0.txt](36_SPEC__V0_4_Layer3_Shadow_Divergence_25_Variables_v1_0.txt) |
| Layer-4 book evidence (v0.4.x) | [37_SPEC__V0_4_Layer4_Book_Evidence_25_Variables_v1_0.txt](37_SPEC__V0_4_Layer4_Book_Evidence_25_Variables_v1_0.txt) |
| Layer-5 counter-evidence + trig reality (v0.4.x) | [38_SPEC__V0_4_Layer5_Counter_Evidence_Trig_Reality_25_Variables_v1_0.txt](38_SPEC__V0_4_Layer5_Counter_Evidence_Trig_Reality_25_Variables_v1_0.txt) |
| Layer-6 conceptual math & dynamic function (v0.4.x) | [39_SPEC__V0_4_Layer6_Conceptual_Math_Dynamic_Function_25_Variables_v1_0.txt](39_SPEC__V0_4_Layer6_Conceptual_Math_Dynamic_Function_25_Variables_v1_0.txt) |
| Layer-7 cross-layer interactions & aggregates (v0.4.x) | [40_SPEC__V0_4_Layer7_Cross_Layer_Interactions_Limits_Aggregates_25_Variables_v1_0.txt](40_SPEC__V0_4_Layer7_Cross_Layer_Interactions_Limits_Aggregates_25_Variables_v1_0.txt) |
| Layer-8 units, normalization, i18n (v0.4.x) | [41_SPEC__V0_4_Layer8_Units_Normalization_I18n_25_Variables_v1_0.txt](41_SPEC__V0_4_Layer8_Units_Normalization_I18n_25_Variables_v1_0.txt) |
| Layer-9 human reference & brand (v0.4.x) | [42_SPEC__V0_4_Layer9_Human_Reference_Brand_Treatment_25_Variables_v1_0.txt](42_SPEC__V0_4_Layer9_Human_Reference_Brand_Treatment_25_Variables_v1_0.txt) |
| Pipeline config (22_SPEC) | [guard_config_v1.json](guard_config_v1.json) |
| Full run (stub) | [sphere_rag/full_run_simulation.py](sphere_rag/full_run_simulation.py) |
| Chroma books validation | [sphere_rag/chroma_books_validation_run.py](sphere_rag/chroma_books_validation_run.py) |
| Run entry | [sphere_rag/run_simulation.py](sphere_rag/run_simulation.py) (`full` / `chroma`) |
| Lexical stack | [hesperia_lex/README.md](hesperia_lex/README.md) |
| Topology contract | [hesperia_lex/TOPOLOGY-STORAGE-CONTRACT.md](hesperia_lex/TOPOLOGY-STORAGE-CONTRACT.md) |
| Release gate report | [docs/HESPERIA_V03_RELEASE_GATE_REPORT.md](docs/HESPERIA_V03_RELEASE_GATE_REPORT.md) |
| Doc index | [DOC_INDEX.md](DOC_INDEX.md) |

## Next (v0.5 territory)

Expanding lexical size, adjacency ingestion, scaling Chroma topology — structural invariants tested for real. Not in v0.4 scope.
