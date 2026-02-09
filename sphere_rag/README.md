# `sphere_rag` — Python Prototype Package

This directory contains a minimal Python implementation of the Sphere
geometry, attribution, traversal, and governance pipeline.

It is intended as:
- A reference implementation for the specs.
- A sandbox for experiments and integration with LLMs and vector DBs.

## Prototype reality (avoid false assumptions)

Some modules are intentionally placeholders. Do not build downstream authority on placeholder outputs.

- `attribution.py` currently returns a fixed Area/Family (prototype stub).
- `pipeline.py` retrieves external evidence but (currently) does not place it into the Region.
- `traversal.py` and `governance.py` return simple deterministic placeholder metrics/decisions.

For agent workflow constraints and RAG determinism boundaries, see:

- `07_PROJECT_Operating_Model_and_Documentation_Coherence_v0_1.md`
- `08_PROJECT_Agent_Workflow_and_RAG_Reality_v0_1.md`

## Mapping to Specs and Glossary

- Geometry and Indexing  
  - `geometry.py`  
    - Implements the hex sphere lattice and side indexing.  
    - Aligned with:
      - `13_SPEC__Indexing_and_Coordinates_v1_0.txt`
      - `11_BLUEPRINT__HESPERIA_v4_7_full.txt`
      - geometry/indexing term definitions in `ACADEMIC.md`

- Semantic Attribution  
  - `attribution.py`  
    - Defines `SentenceAttribution` and `StatementAttribution`.  
    - Prototype `AttributionService` aligned conceptually with:
      - `12_SPEC__Semantic_Engine_v0_4.txt`.
      - attribution term definitions in `ACADEMIC.md`

- Traversal  
  - `traversal.py`  
    - Implements a simple loop traversal and metrics.  
    - To be aligned more deeply with:
      - `40_POLICY__Loopability_and_traversal.txt`
      - `21_MATH__HESPERIA_formalization_v1_java.txt`.
      - metrics/loopability term definitions in `ACADEMIC.md`

- Governance  
  - `governance.py`  
    - Converts traversal metrics into allow/forbid/require-correction
      decisions for LLM usage.  
    - Connects to ideas in:
      - `41_POLICY__Operational_additions_v0_1.txt`.
      - governance term definitions in `ACADEMIC.md`

- End-to-End Pipeline  
  - `pipeline.py`  
    - Wires a generic Retriever, Attribution, Geometry, Traversal,
      and Governance into a single `SphereRAGPipeline`.  
    - Mirrors the query pipeline in:
      - `11_BLUEPRINT__HESPERIA_v4_7_full.txt`.

- MySQL Integration and Attribution Helpers  
  - `mysql_loader.py`  
    - Connects to a MySQL instance (HSPR DB) using `MYSQL_*` env vars or `.env`.  
    - Loads authors, books, and text chunks from JSON files such as  
      `text_chunks/HSPR_CHUNKED_2_TMS_AS.json` into normalized tables.  
  - `attribution_helper.py`  
    - Inserts semantic `statement` rows, links them back to source  
      `statements` rows, and upserts `side` coordinates once attribution  
      and geometry have been computed.  
  - `example_attribution_flow.py`  
    - Demonstrates an end-to-end flow using a dummy attribution engine:  
      picks a chunk, creates a source statement, runs placeholder  
      attribution, inserts a semantic statement, and assigns a side.

## Who Works Here

- Backend / Python engineers:
  - Extend these modules with real logic from the specs.
  - Integrate with concrete vector DBs and LLM APIs.

- Researchers / Ontology experts:
  - Can use this package to test how families/areas and policies behave
    in practice, using the definitions from docs 30/31/32 and 40/41.
