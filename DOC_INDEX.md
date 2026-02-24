# HESPERIA (HSPR) — Documentation Index

This index explains the structure and naming of the documentation files
in this repository. Numbers are ordered reading paths, not priorities.

## 0. Personas and Recommended Paths

For quick onboarding, choose the path that matches your role.

- **Backend / Systems Engineer (Java, Python)**
  1. `10_MASTER_SPEC__HESPERIA_v1_0.txt`
  2. `11_BLUEPRINT__HESPERIA_v4_5_full.txt`
  3. `12_SPEC__Semantic_Engine_v0_4.txt`
  4. `13_SPEC__Indexing_and_Coordinates_v1_0.txt`
  5. `15_SPEC__Data_and_Schema_v0_1.txt`
  6. `14_SPEC__Services_and_APIs_v0_1.txt`
  7. `sphere_rag/README.md`

- **Math / Research / Formal Methods**
  1. `10_MASTER_SPEC__HESPERIA_v1_0.txt`
  2. `21_MATH__HESPERIA_formalization_v1_java.txt`
  3. `20_GEOMETRY__formalized_structure_java.txt`
  4. `40_POLICY__Loopability_and_traversal.txt`
  5. `41_POLICY__Operational_additions_v0_1.txt`

- **Ontology / Knowledge Engineering**
  1. `10_MASTER_SPEC__HESPERIA_v1_0.txt`
  2. `30_FAMILIES__HESPERIA_hex_canonical_v1_0.txt`
  3. `31_FAMILIES__area_family_table_full.txt` (canonical table)
  4. `32_FAMILIES__concise_spec_v2_1.txt`
  5. `50_DATA__120_books_authors_raw.txt` / `51_DATA__areas_120_authors_books.csv`

- **Product / Narrative / Investment (RU)**
  1. `01_CONCEPT__HESPERIA_project_RU.txt`
  2. `02_DESCRIPTION__HESPERIA_extended_RU.txt`
  3. `03_DESCRIPTION__HESPERIA_investment_RU.txt`
  4. `04_IDEOLOGY__*` through `09_PROJECT__*` (ideology, identity, product, operating model, agent workflow, file naming — see §1a).

## 1. Entry Points

- `README.md`
  High-level overview of the project and current code.

- `01_CONCEPT__HESPERIA_project_RU.txt`
  Conceptual / narrative project description (RU).

- `02_DESCRIPTION__HESPERIA_extended_RU.txt`
  Extended descriptive / investment-technical dossier (RU).

- `03_DESCRIPTION__HESPERIA_investment_RU.txt`
  Investment-focused description (RU).

## 1a. Ideology, Identity, Product, Project (04–09)

- `04_IDEOLOGY__Aequitas_et_cognitio_invictae_*.md`
  Ideology and positioning.
- `05_IDENTITY__Motto_and_Seal_*.md`
  Identity, motto, seal.
- `06_PRODUCT__Properties_and_Blind_Spots_*.md`
  Product properties and blind spots.
- `07_PROJECT__Operating_Model_and_Documentation_Coherence_*.md`
  Operating model and doc coherence.
- `08_PROJECT__Agent_Workflow_and_RAG_Reality_*.md`
  Agent workflow and RAG reality.
- `09_PROJECT__File_Naming_Java_Style_Best_Practices_*.md`
  File naming and Java-style best practices.

## 2. Core System Specs

- `10_MASTER_SPEC__HESPERIA_v1_0.txt`
  Master spec — unified, friendly definition of all core mechanics.

- `10_MASTER_SPEC__HESPERIA_v1_0.docx`
  Same content in Word format (for editing/printing).

- `11_BLUEPRINT__HESPERIA_v4_8_full.txt`
  Blueprint v4.8 — integrated system blueprint with Semantic Stability Control extension.

- `11_BLUEPRINT__HESPERIA_v4_7_full.txt`
  Blueprint v4.7 — prior best-practices baseline, kept for historical continuity.

- `11_BLUEPRINT__HESPERIA_v4_5_full.txt`
  Earlier integrated prototype v0.4 + engineering pipeline (kept for history).

- `12_SPEC__Semantic_Engine_v0_4.txt`
  Semantic attribution and evolution engine spec (word → sentence → statement).

- `13_SPEC__Indexing_and_Coordinates_v1_0.txt`
  Canonical indexing and coordinate spec for Areas/Families/Hexes/Sides.

- `15_SPEC__Data_and_Schema_v0_1.txt`
  Relational schema and vector DB layout; DB‑centric ingestion/query view.

- `19_SPEC__Semantic_Stability_Control_v1_0.txt`
  Semantic stability control layer spec: reliability, integrity, decay, and forecast logic.

- `22_SPEC__V0_3_Core_Math_Contract_v1_0.md`
  **v0.3 canonical (implementation contract)**: SurfaceEnergy fusion, traversal (base + shadow), resolution (dominant family/area), metrics, penalties, invariants (I-R2, I-R3), books non-voting. Refs: 19 (two-dictionary), 20 (authority separation), 21 (books evidence non-voting). Config: `guard_config_v1.json`.

- `14_SPEC__Services_and_APIs_v0_1.txt`
  Service/API surfaces for implementations (main contract
  for microservices and module boundaries).

- `16_SPEC__Families_Passes_and_Safety_v0_1.txt`
  Families, passes, and safety.
- `17_SPEC__Family_Matrices_description_v0_1.txt`
  Family matrices description.
- `18_SPEC__MySQL_integration_and_ingestion_v0_1.txt`
  MySQL integration and ingestion.

## 3. Math, Geometry, Prototypes

- `20_GEOMETRY__formalized_structure_java.txt`
  Formalized geometric structure and lattice (Java-style math).

- `21_MATH__HESPERIA_formalization_v1_1_java.txt`
  Full mathematical formalization (v1.1) with semantic stability control equations.

- `21_MATH__HESPERIA_formalization_v1_java.txt`
  Earlier mathematical formalization baseline (v1), kept unchanged for history.

- `22_PROTOTYPE__HESPERIA_v0_2_spec.txt`
  Prototype spec v0.2 (text + math). Superseded by 10 + 11 but kept for history.

- `23_PROTOTYPE__HESPERIA_v0_3_formalized_java.txt`
  Prototype v0.3, unified math backbone (Java-style). Superseded by 10 + 11.

## 4. Ontology / Families / Ring

- `30_FAMILIES__HESPERIA_hex_canonical_v1_0.txt`
  Canonical 24 families per Area + ring behavior.

- `31_FAMILIES__area_family_table_full.txt`
  Tabular mapping: Area name + Family names. **Canonical table**.

- `docs/TASK__v0412_FAMILIES_DEFINITION_CANONICAL_FILE.md` + `hesperia_lex/definitions/v0412/families.yaml`
  **v0.4.1.2.** Single canonical definition source (no pool semantics). Validate/build: see `hesperia_lex/definitions/v0412/README.md`.

- `docs/TASK__v0413_FAMILIES_SEMANTIC_CANONICALIZATION.md` + `hesperia_lex/definitions/v0413/families.yaml`
  **v0.4.1.3.** Semantic canonicalization layer (single YAML, overlap controls, mirror checks, semantic audit report). Validate/build: see `hesperia_lex/definitions/v0413/README.md`.

- `docs/CANONICAL_SURFACE_V040_PROCEDURE.md`
  **Canonical surface v0.4.0.** Procedure: produce surface (explicit MODEL_REVISION + Dict A) → prove determinism (two builds, same SHA) → freeze ownership (CANONICAL_SURFACE_V040.txt) → lock (surface immutable). Dict B B1 fails if surface checksum mismatches. No UNSET; no silent rebuilds.

- `docs/DICT-B-FREEZE-v0_4_1_4.md`
  Dict B v0.4.1.4 freeze split: B0 token fallback vs B1 surface alignment (hard-gated by surface source).

- `32_FAMILIES__concise_spec_v2_1.txt`
  Concise family spec v2.1 with borders and edge families.

- `33_FAMILIES__Passes_and_Stops_description_v0_1.txt`
  Passes and stops description.

## 5. Operations, Loopability, Governance

- `40_POLICY__Loopability_and_traversal.txt`
  Loopability reasoning, ring traversal, multi-pass logic.

- `41_POLICY__Operational_additions_v0_2.txt`
  Operational policy extensions including GovernanceProfile stability parameters and stability vector.

- `41_POLICY__Operational_additions_v0_1.txt`
  Earlier operational metrics baseline (v0.1), kept for history.

- `42_POLICY__Guard_Layer_Sigma_Gamma_Theta_v1_0.txt`
  Guard-layer technical spec for invariant enforcement (Σ static, Γ dynamic, Θ governance) and release gating.

- `24_SPEC__Shadow_Layer_v1_0.txt`
  Shadow Layer v1.0 (Core + ΓΘ Addon): degraded-mode traversal plane, topology-preserving, risk R, mass decay, constrained hops, abuse detection, failure codes. v0.4 remains read-only diagnostic.

- `25_SPEC__Safeguard_State_Machine_v0_1.txt`
  **Locked (Grace 2026-02-18).** Safeguard State Machine v0.1: three consecutive logical-fail (hop_result=0) → SAFEGUARD_STOP; fail_count, valid_streak per traversal context; CONSECUTIVE_FAIL_THRESHOLD=3, VALID_STREAK_RESET=2. Canonical: ETHAN-HESPERIA-LOOP-SAFEGUARD.md; stress-test: GENA-HESPERIA-SAFEGUARD-STRESS-TEST-RESULTS.md.

- `28_SPEC__v0_4_0_Embedding_Based_DictB_and_Surface_Siding.txt`
  **Normative (v0.4.0).** Full build stack: Dict A → embedding model → Dict B (frozen) → Surface Map (hybrid terrain L/T/S/R, lexical sides, token buckets). Covers normalization, candidate filtering, anchor construction, similarity (τ, δ, μ, K), κ/F_min_covered, surface siding quotas and hex constraints (L≤3, T≥1), reports, failure conditions, §18 common traps. Runtime uses only frozen artifacts.
- `28_SPEC__EBFCL_v0_4_0_draft.txt`
  Superseded by 28_SPEC__v0_4_0_Embedding_Based_DictB_and_Surface_Siding.txt (kept for history).

- `29_SPEC__HESPERIA_v0_4_1_DictB_Embedding_Classification.txt`
  **Normative (build-time only).** v0.4.1 Dict B: token → preferred_family + possible_relaxed_family (optional). Similarity vs family vectors (mean of Dict A anchors); τ, δ_min_primary, τ_relaxed, δ_max_secondary, FCS_min, family_overlap_cap; density governance (κ, secondary caps); runtime dict_b_v041.json + audit; surface uses preferred only; possible_relaxed runtime-inert. Depends: 27 (attribution), 28 (embedding/surface), surface role spec.

## 5a. Releases

- `RELEASE_NOTES__v0_2_1.txt`
  Release notes for v0.2.1 (semantic stability control integration, backward-compatible).

## 6. Data / Experiments / Mappings

- `50_DATA__120_books_authors_raw.txt`
  Raw list of 120 books and authors.

- `51_DATA__areas_120_authors_books.csv`
  Mapping of books/authors into Areas (CSV).

## 7. Code and Reference Implementation

- `docs/ENV__BUILD_V040_EMBEDDINGS.md`
  Deterministic environment hardening guidance for optional embedding/surface build path (`sphere_rag.build_v040`).

- `RUNNABLE.md`
  All runnable entry points: one-shot pre-test, v0.4.0/v0.4.1 builds, core_math, run_simulation modes, pytest. Cursor-traversable.
- `scripts/run_hesperia_pre_test.py`
  Pre-test whole run (small): v0.4.0 build → v0.4.1 build → core_math test → pytest (if installed). Use from repo root: `python scripts/run_hesperia_pre_test.py` or `python sphere_rag/run_simulation.py pretest`.
- `sphere_rag/`
  Python prototype package:
  - geometry, indexing, and coordinates (aligned with `13_SPEC__Indexing_and_Coordinates_v1_0.txt`)
  - attribution, traversal, and governance pipeline for RAG.
  - `shadow_layer.py`: Shadow Layer v1.0 (Γ enter/exit, Θ gate, failure codes; spec `24_SPEC__Shadow_Layer_v1_0.txt`).
  - `run_simulation.py`: modes `full`, `chroma`, `serve`, `pretest`.

## 8. Legacy / Drafts

- `60_LEGACY__prototype_notes_v0.txt`
- `61_LEGACY__prototype_notes_v0_2.txt`
- `legacy/` directory
  Contains older or duplicated formalization drafts kept for reference.
