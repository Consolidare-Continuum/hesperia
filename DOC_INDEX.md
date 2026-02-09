# HESPERIA (HSPR) — Documentation Index

This index explains the structure and naming of the documentation files
in this repository. Numbers are ordered reading paths, not priorities.

## 0. Personas and Recommended Paths

For quick onboarding, choose the path that matches your role.

- **All Contributors (doctrine first)**  
  1. `04_IDEOLOGY_Aequitas_et_cognitio_invictae_v0_2.md`  
  2. `06_PRODUCT_Properties_and_Blind_Spots_v0_1.md`  
  3. `07_PROJECT_Operating_Model_and_Documentation_Coherence_v0_1.md`  
  4. `08_PROJECT_Agent_Workflow_and_RAG_Reality_v0_1.md`  
  5. `05_IDENTITY_Motto_and_Seal_v0_1.md`  
  6. `10_MASTER_SPEC__HESPERIA_v1_0.txt`  
  7. `11_BLUEPRINT__HESPERIA_v4_7_full.txt`

- **Backend / Systems Engineer (Java, Python)**  
  0. `04_IDEOLOGY_Aequitas_et_cognitio_invictae_v0_2.md`  
  1. `10_MASTER_SPEC__HESPERIA_v1_0.txt`  
  2. `11_BLUEPRINT__HESPERIA_v4_7_full.txt`  
  3. `12_SPEC__Semantic_Engine_v0_4.txt`  
  4. `13_SPEC__Indexing_and_Coordinates_v1_0.txt`  
  5. `15_SPEC__Data_and_Schema_v0_1.txt`  
  6. `14_SPEC__Services_and_APIs_v0_1.txt`  
  7. `sphere_rag/README.md`

- **Math / Research / Formal Methods**  
  0. `04_IDEOLOGY_Aequitas_et_cognitio_invictae_v0_2.md`  
  1. `10_MASTER_SPEC__HESPERIA_v1_0.txt`  
  2. `21_MATH__HESPERIA_formalization_v1_java.txt`  
  3. `20_GEOMETRY__formalized_structure_java.txt`  
  4. `40_POLICY__Loopability_and_traversal.txt`  
  5. `41_POLICY__Operational_additions_v0_1.txt`

- **Ontology / Knowledge Engineering**  
  0. `04_IDEOLOGY_Aequitas_et_cognitio_invictae_v0_2.md`  
  1. `10_MASTER_SPEC__HESPERIA_v1_0.txt`  
  2. `30_FAMILIES__HESPERIA_hex_canonical_v1_0.txt`  
  3. `31_FAMILIES__area_family_table_full.txt` (canonical table)  
  4. `32_FAMILIES__concise_spec_v2_1.txt`  
  5. `16_SPEC__Families_Passes_and_Safety_v0_1.txt`  
  6. `17_SPEC__Family_Matrices_description_v0_1.txt`  
  7. `33_FAMILIES__Passes_and_Stops_description_v0_1.txt`  
  8. `50_DATA__120_books_authors_raw.txt` / `51_DATA__areas_120_authors_books.csv`

- **Product / Narrative / Investment (RU)**  
  0. `04_IDEOLOGY_Aequitas_et_cognitio_invictae_v0_2.md`  
  1. `01_CONCEPT_HESPERIA_project_RU.txt`  
  2. `02_DESCRIPTION_HESPERIA_extended_RU.txt`  
  3. `03_DESCRIPTION_HESPERIA_investment_RU.txt`

## 1. Entry Points

- `README.md`  
  High-level overview of the project and current code.

- `04_IDEOLOGY_Aequitas_et_cognitio_invictae_v0_2.md`  
  Motto, thesis, doctrine, oath, and negative manifesto (binding constraints).

- `05_IDENTITY_Motto_and_Seal_v0_1.md`  
  Motto usage rules and seal specification (encoding, absences, style constraints).

- `06_PRODUCT_Properties_and_Blind_Spots_v0_1.md`  
  Operational properties, deliberate limitations, and known blind spots (internal decision surface).

- `07_PROJECT_Operating_Model_and_Documentation_Coherence_v0_1.md`  
  Operating model for maintaining coherence: document taxonomy, change control, roles, gates, red flags, and development borders.

- `08_PROJECT_Agent_Workflow_and_RAG_Reality_v0_1.md`  
  Agent-facing constraints: workflow traps, determinism boundary in RAG, provenance requirements.

- `09_PROJECT_File_Naming_Java_Style_Best_Practices_v0_1.md`  
  Consolidated file naming rules for Java-style projects (source, tests, resources, modules).

- `01_CONCEPT_HESPERIA_project_RU.txt`  
  Conceptual / narrative project description (RU).

- `02_DESCRIPTION_HESPERIA_extended_RU.txt`  
  Extended descriptive / investment-technical dossier (RU).

- `03_DESCRIPTION_HESPERIA_investment_RU.txt`  
  Investment-focused description (RU).

## 2. Core System Specs

- `10_MASTER_SPEC__HESPERIA_v1_0.txt`  
  Master spec — unified, friendly definition of all core mechanics.

- `11_BLUEPRINT__HESPERIA_v4_7_full.txt`  
  Blueprint v4.7 — best-practices, human-oriented description of the whole system.

- `11_BLUEPRINT__HESPERIA_v4_5_full.txt`  
  Earlier integrated prototype v0.4 + engineering pipeline (kept for history).

- `12_SPEC__Semantic_Engine_v0_4.txt`  
  Semantic attribution and evolution engine spec (word → sentence → statement).

- `13_SPEC__Indexing_and_Coordinates_v1_0.txt`  
  Canonical indexing and coordinate spec for Areas/Families/Hexes/Sides.

- `15_SPEC__Data_and_Schema_v0_1.txt`  
  Relational schema and vector DB layout; DB‑centric ingestion/query view.

- `14_SPEC__Services_and_APIs_v0_1.txt`  
  Service/API surfaces for implementations (main contract
  for microservices and module boundaries).

- `18_SPEC__MySQL_integration_and_ingestion_v0_1.txt`  
  MySQL integration for books/chunks/statements + semantic schema wiring and examples.

## 3. Math, Geometry, Prototypes

- `20_GEOMETRY__formalized_structure_java.txt`  
  Formalized geometric structure and lattice (Java-style math).

- `21_MATH__HESPERIA_formalization_v1_java.txt`  
  Full mathematical formalization of the HESPERIA dynamics (Java-style).

- `22_PROTOTYPE__HESPERIA_v0_2_spec.txt`  
  Prototype spec v0.2 (text + math). Superseded by 10 + 11 but kept for history.

- `23_PROTOTYPE__HESPERIA_v0_3_formalized_java.txt`  
  Prototype v0.3, unified math backbone (Java-style). Superseded by 10 + 11.

## 4. Ontology / Families / Ring

- `30_FAMILIES__HESPERIA_hex_canonical_v1_0.txt`  
  Canonical 24 families per Area + ring behavior.

- `31_FAMILIES__area_family_table_full.txt`  
  Tabular mapping: Area name + Family names. **Canonical table**.

- `32_FAMILIES__concise_spec_v2_1.txt`  
  Concise family spec v2.1 with borders and edge families.

- `16_SPEC__Families_Passes_and_Safety_v0_1.txt`  
  Layered spec for family-level passes, safety control stops, and their counts.

- `17_SPEC__Family_Matrices_description_v0_1.txt`  
  Numerical description of family-level matrices (base links, passes matrix, full graph).

- `33_FAMILIES__Passes_and_Stops_description_v0_1.txt`  
  Narrative description of the first explicit family linking (passes + stops).

## 5. Operations, Loopability, Governance

- `40_POLICY__Loopability_and_traversal.txt`  
  Loopability reasoning, ring traversal, multi-pass logic.

- `41_POLICY__Operational_additions_v0_1.txt`  
  Operational metrics: evidence quality, provenance, multi-scale retrieval, etc.

## 6. Data / Experiments / Mappings

- `50_DATA__120_books_authors_raw.txt`  
  Raw list of 120 books and authors.

- `51_DATA__areas_120_authors_books.csv`  
  Mapping of books/authors into Areas (CSV).

- `HESPERIA_FAMILIES_SETUP_V0.1.txt`  
  Canonical 288-family setup table with internal and area-hop neighbours.

- `HESPERIA_FAMILIES_PASSES_v0_3.csv`  
  Family passes along the ring + special CONTROL/DECEIT/TRUTH borders (v0.3).

- `HESPERIA_FAMILIES_PASSES_control_stops_v0_1.csv`  
  Safety control-stop links between high-risk and stabilizing families.

- `HESPERIA_FAMILIES_PASSES_matrix_v0_1.csv`  
  Combined PASS/STOP family edge matrix (external semantics only).

- `HESPERIA_FAMILIES_BASE_links_v0_1.csv`  
  Base family links (INTERNAL_PRE/NEXT and AREA_HOP_PRE/NEXT per family).

- `HESPERIA_FAMILIES_FULL_matrix_v0_1.csv`  
  Full family graph matrix (all internal links + all passes + all stops).

## 7. Code and Reference Implementation

- `sphere_rag/`  
  Python prototype package:
  - geometry, indexing, and coordinates (aligned with `13_SPEC__Indexing_and_Coordinates_v1_0.txt`)
  - attribution, traversal, and governance pipeline for RAG.
  - MySQL ingestion and attribution helpers:
    - `mysql_loader.py` — load books/chunks into HSPR.
    - `attribution_helper.py` — DB bridge: source statements → semantic statements → sides.
    - `example_attribution_flow.py` — end‑to‑end attribution/placement demo (dummy engine).

## 8. Legacy / Drafts

- `60_LEGACY__prototype_notes_v0.txt`  
- `61_LEGACY__prototype_notes_v0_2.txt`  
- `legacy/` directory  
  Contains older or duplicated formalization drafts kept for reference.
