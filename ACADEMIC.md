# HESPERIA (HSPR) — ACADEMIC GLOSSARY (Draft)

Purpose: provide a **single point of truth** for terminology, using
university‑style (academic) definitions and then explaining how each term
is used inside this project. This file is for everyone: researchers,
engineers, and AI assistants.

- Each entry has:
  - **Academic definition** — neutral, textbook‑style meaning.
- **Project usage** — how the term is instantiated in HESPERIA.
  - **Used in** — main specs / code files where it lives.
- When variables or constants appear (e.g. `AREAS`, `tau[s]`), we hashtag
  them as **#AREAS**, **#tau_s** to keep a stable naming surface.

The “system” in this document means the **CLI pipeline**:
user input → attribution → aggregation → traversal/governance → CLI output.
APIs and microservices are secondary evolutions and must be justified
relative to this core path.

---

## 0. PIPELINE AND SYSTEM

### System (HESPERIA core pipeline)
- **Academic definition**  
  A system is a set of components and processes that transform inputs
  into outputs according to defined rules.
- **Project usage**  
  The **HESPERIA system** is the end‑to‑end CLI pipeline:
  text input → semantic attribution → placement in the hex-sphere lattice →
  region construction → loop traversal → structured decision/output.
  For now, “system” does **not** mean user‑facing APIs or microservices;
  those are implementation choices around this core.
- **Used in**  
  `10_MASTER_SPEC__HESPERIA_v1_0.txt`,  
  `11_BLUEPRINT__HESPERIA_v4_7_full.txt`,  
  `14_SPEC__Services_and_APIs_v0_1.txt`.

### User Input / System Output
- **Academic definition**  
  - Input: data supplied to a system for processing.  
  - Output: data produced by the system as a result.
- **Project usage**  
  - **User input** is natural language text, given via CLI.  
  - **System output** is a structured `HESPERIAResult` object: dominant
    Areas/Families, metrics (e.g. #loopability, #tensionEnergy), full
    coordinates and tau for relevant sides, governance decision, and
    supporting statements. This can be printed for humans and passed to
    an external LLM for commentary or adjustments.
  This input–output behavior is the canonical reference for interpreting
  all internal variables.
- **Used in**  
  `10_MASTER_SPEC__HESPERIA_v1_0.txt` (overview),  
  `11_BLUEPRINT__HESPERIA_v4_7_full.txt` (query pipeline),  
  `sphere_rag/pipeline.py`.

### Retrieval (RAG retrieval)
- **Academic definition**  
  Retrieval is the process of finding and selecting relevant documents, passages, or records from a corpus in response to a query, using lexical, semantic, or hybrid search methods.
- **Project usage**  
  In HESPERIA, retrieval is evidence selection. It returns candidates (chunks/statements) with stable identifiers and provenance so that downstream placement and governance can remain inspectable.
  Retrieval is not meaning by itself; it is input into constraint evaluation.
- **Used in**  
  `10_MASTER_SPEC__HESPERIA_v1_0.txt`,  
  `11_BLUEPRINT__HESPERIA_v4_7_full.txt`,  
  `15_SPEC__Data_and_Schema_v0_1.txt`,  
  `18_SPEC__MySQL_integration_and_ingestion_v0_1.txt`,  
  `sphere_rag/pipeline.py`,  
  `08_PROJECT_Agent_Workflow_and_RAG_Reality_v0_1.md`.

### RAG (retrieval-augmented generation)
- **Academic definition**  
  Retrieval-augmented generation (RAG) is an architecture in which a generative model conditions its output on information retrieved from an external corpus at inference time.
- **Project usage**  
  In HESPERIA, RAG is treated as three separable roles:
  retrieval (evidence selection), constraint evaluation (admissibility/governance), and generation (external, replaceable LLM adapter).
  The project avoids collapsing these roles into a single “speaking system”.
- **Used in**  
  `sphere_rag/README.md`,  
  `sphere_rag/pipeline.py`,  
  `06_PRODUCT_Properties_and_Blind_Spots_v0_1.md`,  
  `08_PROJECT_Agent_Workflow_and_RAG_Reality_v0_1.md`.

### Retriever (retrieval backend)
- **Academic definition**  
  A retriever is a component that implements a retrieval function from a query to a ranked list of candidates, often returning both content and metadata for scoring and traceability.
- **Project usage**  
  In HESPERIA, a retriever must return evidence with machine-resolvable provenance (IDs, paths, offsets when available). It is an interchangeable backend (vector DB, BM25, hybrid).
- **Used in**  
  `sphere_rag/pipeline.py`,  
  `08_PROJECT_Agent_Workflow_and_RAG_Reality_v0_1.md`.

### Generator (LLM adapter; external generation)
- **Academic definition**  
  A generator is a model or subsystem that produces natural language output conditioned on input prompts and (optionally) retrieved context.
- **Project usage**  
  In HESPERIA, the generator is external and replaceable. HESPERIA outputs structural signals and constraints that the generator must respect; it does not become a primary authority source.
- **Used in**  
  `04_IDEOLOGY_Aequitas_et_cognitio_invictae_v0_2.md`,  
  `06_PRODUCT_Properties_and_Blind_Spots_v0_1.md`,  
  `08_PROJECT_Agent_Workflow_and_RAG_Reality_v0_1.md`.

### Context (retrieved context; context window)
- **Academic definition**  
  Context is information supplied alongside a query that influences interpretation or generation; a context window is the bounded amount of context a model can condition on at one time.
- **Project usage**  
  In HESPERIA RAG workflows, “context” refers to retrieved evidence items (chunks/statements) plus their provenance. Context is treated as inspectable input to admissibility evaluation and generation, not as implicit background.
- **Used in**  
  `sphere_rag/pipeline.py`,  
  `18_SPEC__MySQL_integration_and_ingestion_v0_1.txt`.

### Chunk (text chunk)
- **Academic definition**  
  A chunk is a segmented unit of a larger document used for indexing, retrieval, and processing (for example, a paragraph-sized passage).
- **Project usage**  
  In HESPERIA ingestion, chunks are stored as source text units in MySQL (`chunks` table) with stable IDs mirrored from JSON inputs. Chunks can be promoted into source-layer `statements` for attribution and placement.
- **Used in**  
  `18_SPEC__MySQL_integration_and_ingestion_v0_1.txt`,  
  `sphere_rag/mysql_loader.py`,  
  `sphere_rag/example_attribution_flow.py`.

### Embedding (vector representation)
- **Academic definition**  
  An embedding is a mapping from objects (words, sentences, documents) to vectors in a continuous space such that similarity in vector space corresponds (approximately) to similarity in the original domain.
- **Project usage**  
  HESPERIA uses embeddings for deterministic lexical grounding (via fixed versions of models/thresholds) and for retrieval backends. Embeddings must be versioned; similarity is not semantic identity.
- **Used in**  
  `12_SPEC__Semantic_Engine_v0_4.txt`,  
  `11_BLUEPRINT__HESPERIA_v4_7_full.txt`,  
  `14_SPEC__Services_and_APIs_v0_1.txt`.

### Vector database (vector store)
- **Academic definition**  
  A vector database stores embeddings and supports nearest-neighbor search, often using approximate indexing structures for speed.
- **Project usage**  
  HESPERIA uses a vector DB as an interchangeable retrieval backend for words and statements. Stable identifiers must be mirrored between SQL and the vector store; retrieval parameters should be recorded for reproducibility.
- **Used in**  
  `11_BLUEPRINT__HESPERIA_v4_7_full.txt`,  
  `14_SPEC__Services_and_APIs_v0_1.txt`,  
  `15_SPEC__Data_and_Schema_v0_1.txt`,  
  `08_PROJECT_Agent_Workflow_and_RAG_Reality_v0_1.md`.

### Approximate nearest neighbor (ANN) retrieval
- **Academic definition**  
  Approximate nearest neighbor search returns high-similarity candidates without guaranteeing exact nearest neighbors, trading accuracy and determinism for performance.
- **Project usage**  
  ANN retrieval can introduce non-determinism across runs (index updates, compaction, concurrency). HESPERIA treats this as a determinism boundary: for repeatability, record embedding versions, index settings, and retrieval parameters, and keep stable IDs for evidence.
- **Used in**  
  `08_PROJECT_Agent_Workflow_and_RAG_Reality_v0_1.md`,  
  `06_PRODUCT_Properties_and_Blind_Spots_v0_1.md`.

### Provenance (source trace)
- **Academic definition**  
  Provenance is metadata that records the origin, history, and transformation path of data, enabling auditability and reproducibility.
- **Project usage**  
  In HESPERIA, provenance binds semantic placements to source-layer items (books/chunks/statements) via stable identifiers and file paths. Provenance is required for admissibility to be auditable.
- **Used in**  
  `18_SPEC__MySQL_integration_and_ingestion_v0_1.txt`,  
  `41_POLICY__Operational_additions_v0_1.txt`,  
  `06_PRODUCT_Properties_and_Blind_Spots_v0_1.md`.

### Grounding (evidence-linked output)
- **Academic definition**  
  Grounding is the practice of constraining outputs to be supported by referenced evidence or a defined world model, reducing unsupported generation.
- **Project usage**  
  HESPERIA grounds downstream generation by requiring evidence-linked structure: coordinates, metrics, and provenance links. Unsupported continuity is treated as inadmissible or refused.
- **Used in**  
  `06_PRODUCT_Properties_and_Blind_Spots_v0_1.md`,  
  `08_PROJECT_Agent_Workflow_and_RAG_Reality_v0_1.md`.

### Motto (Aequitas et cognitio invictae)
- **Academic definition**  
  A motto is a short phrase expressing a guiding principle, constraint, or pledge for a group, institution, or project.
- **Project usage**  
  The HESPERIA motto is not branding; it is a design constraint:
  the system must preserve **structural equity** (aequitas) and **testable understanding** (cognitio) under pressure, contradiction, and time (invictae).
  It is invoked when deciding whether a feature belongs, whether a metric is acceptable, and whether a subsystem is allowed to speak with authority.
- **Used in**  
  `README.md`,  
  `04_IDEOLOGY_Aequitas_et_cognitio_invictae_v0_2.md`,  
  `05_IDENTITY_Motto_and_Seal_v0_1.md`.

### Aequitas (equity; structural proportionality)
- **Academic definition**  
  Equity is the principle of fairness as proportionality: outcomes, resources, and obligations are distributed according to relevant differences, constraints, and rules (distinct from equal treatment in all cases).
- **Project usage**  
  In HESPERIA, **aequitas** is not sentiment. It is structural proportionality enforced by geometry and metrics:
  no concept dominates without cost; no claim gains weight without evidence; polarity axes remain explicit; influence is bounded and measurable.
- **Used in**  
  `04_IDEOLOGY_Aequitas_et_cognitio_invictae_v0_2.md`,  
  `05_IDENTITY_Motto_and_Seal_v0_1.md`.

### Cognitio (understanding; testable structure)
- **Academic definition**  
  Cognition (and cognate terms like “cognitio”) refers to processes of knowing: perception, learning, memory, reasoning, and comprehension.
- **Project usage**  
  In HESPERIA, **cognitio** means localized, testable understanding:
  meaning has coordinates; it has neighbors and boundaries; it can cohere or fragment under traversal; its stability is measured rather than asserted.
- **Used in**  
  `04_IDEOLOGY_Aequitas_et_cognitio_invictae_v0_2.md`,  
  `05_IDENTITY_Motto_and_Seal_v0_1.md`.

### Invictae (undefeated; drift resistance)
- **Academic definition**  
  “Invictus/invicta/invictae” expresses the idea of being unconquered or undefeated, i.e., not overcome by force or adversity.
- **Project usage**  
  In HESPERIA, **invictae** is resistance to semantic erosion:
  conclusions must survive re-ordering, counter-context, traversal changes, and time. Drift is detected; failure is visible; refusal is allowed.
- **Used in**  
  `04_IDEOLOGY_Aequitas_et_cognitio_invictae_v0_2.md`,  
  `05_IDENTITY_Motto_and_Seal_v0_1.md`,  
  `41_POLICY__Operational_additions_v0_1.txt`.

### Custodial role (stewardship; custodianship)
- **Academic definition**  
  Stewardship is responsible oversight and maintenance of a system or resource, focused on preservation of integrity and continuity rather than ownership or personal authorship.
- **Project usage**  
  In HESPERIA, contributors are defined as custodians:
  curators of structure, maintainers of balance, auditors of drift, and recorders of decisions.
  Personal imprint is minimized; continuity is maximized.
- **Used in**  
  `04_IDEOLOGY_Aequitas_et_cognitio_invictae_v0_2.md`.

### Time discipline (change management; slow time)
- **Academic definition**  
  Change management is a governance process that controls what changes are allowed, when they occur, and how they are validated, to preserve stability and prevent uncontrolled drift.
- **Project usage**  
  HESPERIA uses slow time: ontology and doctrine do not change rapidly.
  Updates occur only when structural inconsistency is proven, long-term drift is measured, and backward compatibility is preserved.
- **Used in**  
  `04_IDEOLOGY_Aequitas_et_cognitio_invictae_v0_2.md`.

### Ideological drift (principle drift; narrative drift)
- **Academic definition**  
  Drift is gradual deviation from a reference state. In organizations, principle drift occurs when language, incentives, and practices slowly move away from a founding constraint set.
- **Project usage**  
  In HESPERIA, ideological drift is detected by changes in internal language and output posture:
  emotional language, reduced refusals without metric justification, longer explanations without new structure, and increased confidence without support.
  When detected, changes are rolled back and the doctrine is re-applied.
- **Used in**  
  `04_IDEOLOGY_Aequitas_et_cognitio_invictae_v0_2.md`.

### Naming constraints (non-agentic language)
- **Academic definition**  
  Naming constraints are rules restricting how systems, components, and outputs may be labeled, to avoid misleading connotations and to keep a stable interpretive surface.
- **Project usage**  
  HESPERIA avoids names implying agency, omniscience, conquest, or intelligence claims.
  Naming should reflect constraint and measurement (not action or authority).
- **Used in**  
  `04_IDEOLOGY_Aequitas_et_cognitio_invictae_v0_2.md`,  
  `05_IDENTITY_Motto_and_Seal_v0_1.md`,  
  `06_PRODUCT_Properties_and_Blind_Spots_v0_1.md`.

### Structural admissibility (admissible / inadmissible)
- **Academic definition**  
  Admissibility is whether an object (claim, argument, evidence, inference) is acceptable under a defined set of rules, constraints, and evaluation criteria.
- **Project usage**  
  In HESPERIA, admissibility is a structural verdict: a claim/output is admitted only if it can be placed into the semantic geometry and remains valid under metrics (coherence, contradiction handling, evidence quality, stability).
  Admissibility is not “truth”; it is legitimacy under a declared constraint regime.
- **Used in**  
  `06_PRODUCT_Properties_and_Blind_Spots_v0_1.md`,  
  `04_IDEOLOGY_Aequitas_et_cognitio_invictae_v0_2.md`,  
  `sphere_rag/governance.py`.

### Semantic invariant (meaning identity across contexts)
- **Academic definition**  
  An invariant is a property that remains unchanged under a set of transformations. In semantics, an invariant is meaning that remains stable across rephrasing, context shifts, or equivalent representations.
- **Project usage**  
  HESPERIA treats meaning stability as a system property to be enforced and tested: the same claim should retain identity across traversal, ordering changes, and time, or fail visibly.
  Stability is measured rather than assumed.
- **Used in**  
  `06_PRODUCT_Properties_and_Blind_Spots_v0_1.md`,  
  `04_IDEOLOGY_Aequitas_et_cognitio_invictae_v0_2.md`,  
  `41_POLICY__Operational_additions_v0_1.txt`.

### Authority (structural legitimacy)
- **Academic definition**  
  Authority is legitimate power or accepted right to influence beliefs or decisions; epistemic authority is authority grounded in knowledge and justification.
- **Project usage**  
  HESPERIA denies authority derived from fluency, repetition, or scale.
  Structural legitimacy is admitted only when a claim occupies stable coordinates, aligns with adjacent regions, and survives traversal without fragmentation; otherwise authority is denied or the system refuses.
- **Used in**  
  `06_PRODUCT_Properties_and_Blind_Spots_v0_1.md`,  
  `04_IDEOLOGY_Aequitas_et_cognitio_invictae_v0_2.md`.

### Epoch (semantic epoch; versioned reference interval)
- **Academic definition**  
  An epoch is a bounded interval in which a reference frame is fixed and comparable; changes across epochs are explicit and tracked.
- **Project usage**  
  A semantic epoch is a versioned interval where core coordinates and polarity axes remain fixed.
  Changes that would shift reference are treated as epoch boundaries and require explicit versioning and migration/interpretability support.
- **Used in**  
  `06_PRODUCT_Properties_and_Blind_Spots_v0_1.md`,  
  `04_IDEOLOGY_Aequitas_et_cognitio_invictae_v0_2.md`.

### Doctrine (binding constraints)
- **Academic definition**  
  A doctrine is a set of principles treated as authoritative within a system of practice, constraining what is permissible and providing a basis for interpretation and governance.
- **Project usage**  
  In HESPERIA, doctrine is the non-negotiable constraint layer that governs scope, tone, admissibility posture, refusal legitimacy, and drift handling.
  Doctrine is versioned and treated as a correctness reference for implementations.
- **Used in**  
  `04_IDEOLOGY_Aequitas_et_cognitio_invictae_v0_2.md`,  
  `07_PROJECT_Operating_Model_and_Documentation_Coherence_v0_1.md`.

### Specification (spec; normative definition)
- **Academic definition**  
  A specification is a precise statement of requirements, interfaces, and constraints that defines expected behavior and enables consistent implementation and verification.
- **Project usage**  
  HESPERIA specs define normative mechanics (geometry, indexing, attribution, schema, services). Code and datasets are expected to align with specs, and changes that alter reference require explicit versioning.
- **Used in**  
  `10_MASTER_SPEC__HESPERIA_v1_0.txt`,  
  `11_BLUEPRINT__HESPERIA_v4_7_full.txt`,  
  `12_SPEC__Semantic_Engine_v0_4.txt`,  
  `13_SPEC__Indexing_and_Coordinates_v1_0.txt`,  
  `07_PROJECT_Operating_Model_and_Documentation_Coherence_v0_1.md`.

### Policy (governance policy; operational constraints)
- **Academic definition**  
  A policy is a rule or set of rules that guides decisions and actions under defined conditions, often operationalizing high-level principles into thresholds and procedures.
- **Project usage**  
  In HESPERIA, policy operationalizes doctrine via measurable metrics and thresholds (loopability, obstacle score, evidence quality, refusal conditions). Policy is inspectable and versioned when it changes decision behavior.
- **Used in**  
  `40_POLICY__Loopability_and_traversal.txt`,  
  `41_POLICY__Operational_additions_v0_1.txt`,  
  `07_PROJECT_Operating_Model_and_Documentation_Coherence_v0_1.md`.

### Change control (controlled evolution; change governance)
- **Academic definition**  
  Change control is a process that evaluates, approves, documents, and tracks changes to preserve integrity, traceability, and compatibility over time.
- **Project usage**  
  HESPERIA change control enforces slow time: ontology/reference changes are versioned; migration/interpretability notes are recorded; refusal and governance thresholds are treated as policy decisions rather than tuning knobs.
- **Used in**  
  `07_PROJECT_Operating_Model_and_Documentation_Coherence_v0_1.md`,  
  `04_IDEOLOGY_Aequitas_et_cognitio_invictae_v0_2.md`,  
  `06_PRODUCT_Properties_and_Blind_Spots_v0_1.md`.

---

## 1. GEOMETRY AND INDEXING

### Area (#AREAS)
- **Academic definition**  
  In geometry or topology, an “area” is often a region of space with
  shared properties; in semantics, it can denote a broad conceptual
  domain (e.g. ethics, control, freedom).
- **Project usage**  
  An **Area** is one of 12 fixed semantic macro‑regions on a ring.
  #AREAS = 12. Each Area groups 24 Families and corresponds to a
  high‑level polarity theme (e.g. GOOD, HARM, ORDER, CHAOS).
- **Used in**  
  `10_MASTER_SPEC__HESPERIA_v1_0.txt`,  
  `11_BLUEPRINT__HESPERIA_v4_5_full.txt` (Section 1),  
  `13_SPEC__Indexing_and_Coordinates_v1_0.txt`,  
  `30_FAMILIES__HESPERIA_hex_canonical_v1_0.txt`,  
  `sphere_rag/geometry.py`.

### Family (#FAMILIES_PER_AREA, #TOTAL_FAMILIES)
- **Academic definition**  
  A semantic “family” is a cluster of related concepts sharing common
  meaning or function (e.g. altruism, protection).
- **Project usage**  
  A **Family** is a fixed semantic cluster within an Area. Each Area
  has #FAMILIES_PER_AREA = 24, giving #TOTAL_FAMILIES = 288.
  Families are labeled (e.g. “Altruism”, “Control/Surveillance”) and
  serve as the primary classification units for words and statements.
- **Used in**  
  `10_MASTER_SPEC__HESPERIA_v1_0.txt`,  
  `30_FAMILIES__HESPERIA_hex_canonical_v1_0.txt`,  
  `31_FAMILIES__area_family_table_full.txt`,  
  `12_SPEC__Semantic_Engine_v0_4.txt`,  
  `13_SPEC__Indexing_and_Coordinates_v1_0.txt`.

### Hex, Side, and Side ID (#HEXES_PER_FAMILY, #SIDES_PER_HEX, #sideId)
- **Academic definition**  
  - Hexagon: a polygon with six sides.  
  - A “side” is an edge of a polygon.  
  - An index is a numeric identifier for an element in a set.
- **Project usage**  
  - Each Family contains #HEXES_PER_FAMILY = 250 hexagons.  
  - Each hex has #SIDES_PER_HEX = 6 sides.  
  - A **Side** is the atomic truth slot; it is addressed by:
    - `area`, `familyLocal`, `hexIndex`, `sideIndex` (4D coordinate) and  
    - a linear **#sideId** ∈ [0..431_999] used for arrays like #tau_s.  
  Indexing rules are defined canonically in `13_SPEC__Indexing_and_Coordinates_v1_0.txt`.
- **Used in**  
  `20_GEOMETRY__formalized_structure_java.txt`,  
  `13_SPEC__Indexing_and_Coordinates_v1_0.txt`,  
  `21_MATH__HESPERIA_formalization_v1_java.txt`,  
  `sphere_rag/geometry.py`.

### Family Graph and Matrices (#familyBaseLinks, #familyPassesMatrix, #familyFullMatrix)
- **Academic definition**  
  A graph is a set of nodes with edges between them; an adjacency matrix or edge list encodes which nodes are connected. A subgraph can represent connectivity at a higher abstraction level (here: families rather than individual hexes or sides).
- **Project usage**  
  - #familyBaseLinks encodes canonical family neighbours from geometry: 288 families, each with 4 directed links (2 internal ring neighbours and 2 area‑hop neighbours), for 1,152 links total.  
  - #familyPassesMatrix encodes 89 directed external edges of type PASS or STOP between families (no internal ring links).  
  - #familyFullMatrix encodes the full directed family graph: 576 internal ring links plus the 89 external PASS/STOP edges, for 665 links total.  
  These matrices sit one level above the 72,000‑hex / 432,000‑side lattice and are used for traversal math, safety overlays, and diagnostics at the family level.
- **Used in**  
  `16_SPEC__Families_Passes_and_Safety_v0_1.txt`,  
  `17_SPEC__Family_Matrices_description_v0_1.txt`,  
  `HESPERIA_FAMILIES_BASE_links_v0_1.csv`,  
  `HESPERIA_FAMILIES_PASSES_matrix_v0_1.csv`,  
  `HESPERIA_FAMILIES_FULL_matrix_v0_1.csv`.

### Region (#Region)
- **Academic definition**  
  In graph theory and spatial analysis, a region is a set of connected
  elements (nodes, cells, or areas) considered as a unit.
- **Project usage**  
  A **Region** is a connected set of sides (truth slots) on the sphere
  that together form the context used for reasoning and retrieval.
  Regions are built from retrieved statements and used to compute
  structural metrics (e.g. coherence, alignment, fragmentation).
- **Used in**  
  `20_GEOMETRY__formalized_structure_java.txt` (T(R), C(R), X_A(R)),  
  `21_MATH__HESPERIA_formalization_v1_java.txt`,  
  `11_BLUEPRINT__HESPERIA_v4_5_full.txt` (region construction),  
  `sphere_rag/geometry.py`, `sphere_rag/traversal.py`.

---

## 2. SEMANTIC ATTRIBUTION

### Word Attribution
- **Academic definition**  
  Assigning a word to one or more semantic classes using dictionaries,
  statistical models, or embeddings.
- **Project usage**  
  The **word attribution pipeline** deterministically maps each lemma
  into a Family (and thus Area), using 5 stages:
  1) dictionary match, 2) nearest neighbors in embedding space,
  3) family centroids, 4) polarity axes, 5) phrase/sentence overrides.
  This yields #familyId and #areaId per token.
- **Used in**  
  `12_SPEC__Semantic_Engine_v0_4.txt` (Section 1),  
  `11_BLUEPRINT__HESPERIA_v4_5_full.txt` (Sections 5–7).

### Dictionary & Embeddings (#dictWordToFamily, #embedWord, #embedFamily, #embedArea)
- **Academic definition**  
  A dictionary is a mapping from lexical items to structured meanings; embeddings are numerical vector representations of words or concepts in a continuous space.
- **Project usage**  
  - #dictWordToFamily maps lemmas to Family IDs.  
  - #familyToArea maps Families to Areas.  
  - #embedWord, #embedFamily, #embedArea store dense vectors for words, family centroids, and area centroids used in similarity computations.  
  Together they provide deterministic grounding of words into the sphere geometry.
- **Used in**  
  `12_SPEC__Semantic_Engine_v0_4.txt` (Section 0),  
  `11_BLUEPRINT__HESPERIA_v4_5_full.txt` (Sections 3–4).

### Thresholds (#THRESH_DICT, #THRESH_NN, #THRESH_FAM, #THRESH_AXIS)
- **Academic definition**  
  A threshold is a cutoff value that determines when a criterion is satisfied in a decision or classification rule.
- **Project usage**  
  - #THRESH_DICT enforces priority of curated dictionary matches.  
  - #THRESH_NN filters nearest neighbors in embedding space.  
  - #THRESH_FAM regulates when family centroids override neighbors.  
  - #THRESH_AXIS controls when polarity alignment is considered valid.  
  Collectively they keep word attribution stable and auditable.
- **Used in**  
  `12_SPEC__Semantic_Engine_v0_4.txt` (Thresholds section),  
  `11_BLUEPRINT__HESPERIA_v4_5_full.txt`.

### Sentence Attribution (#SentenceAttribution)
- **Academic definition**  
  Aggregating word‑level semantics to characterize the meaning of a
  sentence as a distribution over classes.
- **Project usage**  
  #SentenceAttribution stores:
  - `F_sentence[288]` — Family distribution,  
  - `A_sentence[12]` — Area distribution,  
  - dominant family and area.  
  It is computed by aggregating word attributions and normalizing.
- **Used in**  
  `12_SPEC__Semantic_Engine_v0_4.txt` (Section 2),  
  `sphere_rag/attribution.py`.

### Statement Attribution (#StatementAttribution)
- **Academic definition**  
  Representation of the meaning of a multi‑sentence unit (paragraph,
  claim) as a structured vector and label.
- **Project usage**  
  #StatementAttribution aggregates several #SentenceAttribution objects
  and combines them with an embedding of the full text. It yields:
  - `F_statement`, `A_statement`,  
  - final family/area,  
  - inward/outward vectors over Areas.  
  This object is the main semantic handle passed into geometry.
- **Used in**  
  `12_SPEC__Semantic_Engine_v0_4.txt` (Section 3),  
  `11_BLUEPRINT__HESPERIA_v4_5_full.txt` (forward pipeline),  
  `sphere_rag/attribution.py`.

### Inward / Outward Semantics (#familyInward, #familyOutward)
- **Academic definition**  
  Cross‑domain influence measures describing how one semantic region
  reinforces or references another.
- **Project usage**  
  - #familyInward[f][A] measures how much Family *f* strengthens Area *A*.  
  - #familyOutward[f][A] measures legitimate references from Family *f*
    into Area *A*.  
  Used to detect overreach, domain crossings, and to control dictionary
  evolution (backward pipeline).
- **Used in**  
  `12_SPEC__Semantic_Engine_v0_4.txt` (Sections 4–5),  
  `11_BLUEPRINT__HESPERIA_v4_5_full.txt`.

---

## 3. METRICS, LOOPABILITY, GOVERNANCE

### Truth Weight (#tau_s)
- **Academic definition**  
  A scalar weight in [0,1] representing confidence or degree of truth
  assigned to a proposition or observation.
- **Project usage**  
  Each side has #tau_s ∈ [0,1], stored in `tau[sideId]`. A value near 1
  means “strongly supported / very true” in the current corpus and
  evaluation regime. Regional metrics #T_R, #C_R, etc. are functions of
  #tau_s over subsets of sides.
- **Used in**  
  `20_GEOMETRY__formalized_structure_java.txt` (truth representation),  
  `21_MATH__HESPERIA_formalization_v1_java.txt`,  
  `11_BLUEPRINT__HESPERIA_v4_5_full.txt` (tables `side`, `statement`).

### Loopability (#loopability)
- **Academic definition**  
  (Project‑specific term.) The ability of a system to traverse its state
  space in stable loops that converge or reach meaningful fixed points.
- **Project usage**  
  #loopability is a scalar metric describing whether semantic ring
  traversal over a Region leads to stable, interpretable paths instead
  of chaotic wandering. High loopability means the system can perform
  multiple passes without fragmenting meaning. Used for governance
  decisions and to detect when to stop traversal.
- **Used in**  
  `40_POLICY__Loopability_and_traversal.txt`,  
  `21_MATH__HESPERIA_formalization_v1_java.txt`,  
  `sphere_rag/traversal.py`, `sphere_rag/governance.py`.

### Obstacle Score (#obstacleScore, #O_obstacle)
- **Academic definition**  
  A scalar indicator that some region of a state space is unsafe,
  unreliable, or unsuitable for continuation of a process.
- **Project usage**  
  #obstacleScore (or #O_obstacle) ∈ [0,1] marks how “blocked” a Region
  is due to contradictions, low evidence quality, safety policy hits,
  or unknown territory. High obstacle leads traversal to stop and
  governance to forbid or require correction.
- **Used in**  
  `11_BLUEPRINT__HESPERIA_v4_5_full.txt` (loop traversal),  
  `40_POLICY__Loopability_and_traversal.txt`,  
  `41_POLICY__Operational_additions_v0_1.txt`,  
  `sphere_rag/traversal.py`, `sphere_rag/governance.py`.

### Structural Metrics (#T_R, #T_norm, #C_R, #fragIndex, #areaEntropy)
- **Academic definition**  
  Structural metrics quantify how information is distributed and connected in a graph or lattice, measuring magnitude, coherence, and fragmentation.
- **Project usage**  
  - #T_R is total truth magnitude in a Region (sum of #tau_s).  
  - #T_norm is truth density normalized by capacity.  
  - #C_R measures coherence as the size of the largest connected cluster over active sides.  
  - #fragIndex quantifies how many clusters exist relative to active sides.  
  - #areaEntropy measures how evenly active sides are spread across Areas.  
  These metrics drive traversal choices and diagnostics.
- **Used in**  
  `20_GEOMETRY__formalized_structure_java.txt`,  
  `21_MATH__HESPERIA_formalization_v1_java.txt`,  
  `11_BLUEPRINT__HESPERIA_v4_5_full.txt`.

### Spreads and Weights (#AREA_SPREAD, #FAMILY_SPREAD)
- **Academic definition**  
  A spread parameter is a scalar that scales how much influence a step or hop contributes to an aggregate metric; it is often measured in the same units as the underlying quantity (here, truth mass).
- **Project usage**  
  - #AREA_SPREAD is a multiplier for internal hops at the Area level; it controls how much within‑Area movement contributes to cumulative activation and loopability metrics.  
  - #FAMILY_SPREAD is a multiplier per family hop, measured in points of truth (tau units), used to scale how much each family‑level hop contributes when aggregating or propagating activation across the family graph.  
  Both are policy parameters: set to 1.0 in the base policy and tunable for alternative traversal behaviours.
- **Used in**  
  `40_POLICY__Loopability_and_traversal.txt`,  
  `16_SPEC__Families_Passes_and_Safety_v0_1.txt`.

### Activation Vectors & Coverage (#A_vec, #F_vec, #coveragePhi)
- **Academic definition**  
  An activation vector represents a probability or intensity distribution over a discrete set; coverage is the fraction of elements that are significantly activated or visited.
- **Project usage**  
  - #A_vec[12] encodes Area activations over the ring.  
  - #F_vec[288] encodes Family activations.  
  - #coveragePhi is the fraction of Areas visited during loop traversal.  
  Together they summarize where meaning is concentrated and how widely the system has explored the ring.
- **Used in**  
  `10_MASTER_SPEC__HESPERIA_v1_0.txt` (Variables),  
  `21_MATH__HESPERIA_formalization_v1_java.txt` (Section 6),  
  `40_POLICY__Loopability_and_traversal.txt`.

### Hops and Link Types (#internalHop, #areaHop, #passEdge, #stopEdge)
- **Academic definition**  
  In graph theory, a hop is a single step along an edge; different edge types can encode different semantics (for example, neutral transitions vs safety‑critical redirects).
- **Project usage**  
  - #internalHop is a directed move between neighbouring families within the same Area (ring prev/next).  
  - #areaHop is a directed move between families in neighbouring Areas on the ring (area‑hop prev/next).  
  - #passEdge (PASS) is a semantically chosen cross‑Area edge used for normal traversal and loopability.  
  - #stopEdge (STOP) is a safety/control edge that redirects from high‑risk families (e.g., harm, destruction, deceit) toward stabilizing families (e.g., good, truth, freedom, order).  
  All hop and edge types share the same family‑graph geometry but have different weights and roles in traversal and safety logic.
- **Used in**  
  `16_SPEC__Families_Passes_and_Safety_v0_1.txt`,  
  `17_SPEC__Family_Matrices_description_v0_1.txt`,  
  `40_POLICY__Loopability_and_traversal.txt`.

### Polarity Axes & Tension (#axisPos, #axisNeg, #bipolarAxes, #tensionEnergy)
- **Academic definition**  
  Polarity axes model opposing semantic dimensions (e.g. good vs harm); tension energy measures the squared magnitude of these polarizations.
- **Project usage**  
  - #axisPos and #axisNeg store embedding vectors for six bipolar axes: GOOD/HARM, TRUTH/DECEIT, ORDER/CHAOS, FREEDOM/CONTROL, CARE/INDIFFERENCE, CREATION/DESTRUCTION.  
  - #bipolarAxes(A_vec) computes signed differences between paired Areas.  
  - #tensionEnergy sums squared axis values to quantify polarization.  
  These values inform safety, contradiction, and governance signals.
- **Used in**  
  `10_MASTER_SPEC__HESPERIA_v1_0.txt` (Six‑axis polarity model),  
  `12_SPEC__Semantic_Engine_v0_4.txt` (Section 1.4),  
  `21_MATH__HESPERIA_formalization_v1_java.txt` (Sections 6–7).

### Evidence & Provenance (#credibility, #recency, #consensus, #evidenceQuality)
- **Academic definition**  
  Evidence quality measures how trustworthy and recent information is, often combining credibility, recency, and agreement into a single score.
- **Project usage**  
  - #credibility_s, #recency_s, #consensus_s ∈ [0,1] are per‑side factors.  
  - #provenanceWeight_s is their product.  
  - #evidenceQuality_R is a tau‑weighted average of provenance weights in a Region.  
  This controls how strongly a Region should influence decisions.
- **Used in**  
  `41_POLICY__Operational_additions_v0_1.txt` (Section 1),  
  `10_MASTER_SPEC__HESPERIA_v1_0.txt` (decisionIntegrity).

### Temporal Dynamics (#timestamp, #tau_t, #temporalStability, #cumulativeDrift)
- **Academic definition**  
  Temporal dynamics describe how signals decay or change over time and how stable a process is across timesteps.
- **Project usage**  
  - #timestamp_s records when a side was last updated.  
  - #tau_t_s is a time‑decayed truth value using exponential decay.  
  - #temporalStability_R measures variance in timestamps inside a Region.  
  - #cumulativeDrift compares area activation distributions across time.  
  These capture how stale or unstable the semantic state has become.
- **Used in**  
  `11_BLUEPRINT__HESPERIA_v4_5_full.txt` (truth model),  
  `21_MATH__HESPERIA_formalization_v1_java.txt` (Section 8),  
  `41_POLICY__Operational_additions_v0_1.txt` (Section 3).

### Utility, Risk, and Causality (#goalVector, #riskProfile, #utility, #actionScore, #causal, #causalCoherence)
- **Academic definition**  
  Utility functions, risk profiles, and causal graphs describe how desirable outcomes are, how costly risks are, and how actions propagate effects through a system.
- **Project usage**  
  - #goalVector encodes target Area profiles; #riskProfile encodes per‑Area risk costs.  
  - #utility(A_vec) is cosine similarity to the goal.  
  - #actionScore subtracts risk‑weighted penalties from utility.  
  - #causal[a][b] is a causal influence matrix; #causalPush and #causalCoherence measure how actions align with causal structure.  
  These feed into #strategicScore and governance for action‑like queries.
- **Used in**  
  `41_POLICY__Operational_additions_v0_1.txt` (Sections 5–6, 13),  
  `10_MASTER_SPEC__HESPERIA_v1_0.txt` (strategicScore).

### Saturation and Pressure (#gradient, #pressure, #saturation)
- **Academic definition**  
  Saturation and pressure describe how concentrated and redundant information is, often via gradients and similarity in high‑dimensional spaces.
- **Project usage**  
  - #gradient_s is average |tau_s − tau_neighbor| over adjacency.  
  - #pressure_R is the average gradient in a Region, marking sharp changes.  
  - #saturation_R captures redundancy among side embeddings.  
  High saturation and pressure indicate over‑explained or unstable regions.
- **Used in**  
  `20_GEOMETRY__formalized_structure_java.txt` (adjacency and clusters),  
  `21_MATH__HESPERIA_formalization_v1_java.txt` (adjacencyCorrelation),  
  `41_POLICY__Operational_additions_v0_1.txt` (Section 7).

### Composite Scores (#decisionIntegrity, #strategicScore)
- **Academic definition**  
  Composite scores are scalar functions combining several metrics into a single evaluation of the quality or suitability of a decision.
- **Project usage**  
  - #decisionIntegrity combines #evidenceQuality, #scaleConsistency, #temporalStability, and (1 − #contradictionScore) to rate reliability of a Region.  
  - #strategicScore multiplies #actionScore, #causalCoherence, (1 − #saturation), and #evidenceQuality to rate action‑level proposals.  
  These guide whether the system should proceed, abstain, or request more information.
- **Used in**  
  `10_MASTER_SPEC__HESPERIA_v1_0.txt` (System metrics & decision mechanics),  
  `41_POLICY__Operational_additions_v0_1.txt` (Section 13).

### Governance Decision
- **Academic definition**  
  A decision rule mapping observations and metrics to allowed,
  disallowed, or modified system actions.
- **Project usage**  
  A governance decision is the final control output of the system over
  an LLM: allow answering, ask for clarification / correction, or
  forbid execution. It is a function of loopability, obstacle score,
  tension, evidence quality, and other metrics.
- **Used in**  
  `41_POLICY__Operational_additions_v0_1.txt`,  
  `14_SPEC__Services_and_APIs_v0_1.txt` (roles),  
  `sphere_rag/governance.py`, `sphere_rag/pipeline.py`.

### Refusal (abstention; right of refusal)
- **Academic definition**  
  Refusal (or abstention) is a decision outcome in which an agent declines to act or conclude due to insufficient information, unacceptable risk, invalid premises, or violated constraints.
- **Project usage**  
  In HESPERIA, refusal is a first-class correctness outcome: the system may decline to conclude when structure is insufficient, the region is contradictory, or governance thresholds are hit.
  Suppressing refusal is treated as system corruption because it replaces measurable limits with rhetorical continuity.
- **Used in**  
  `04_IDEOLOGY_Aequitas_et_cognitio_invictae_v0_2.md`,  
  `41_POLICY__Operational_additions_v0_1.txt`,  
  `sphere_rag/governance.py`.

---

## 4. OPEN ITEMS FOR EXPANSION

This glossary now covers most core variables and metrics in the current
specs. Remaining useful additions would be:

- More precise operational description of embeddings:
  - dimensionality, normalization, and typical model choices.
- Concrete numeric examples for:
  - one full forward pass (word → sentence → statement → side → region),
  - one loop traversal with #loopability and #coveragePhi.
- Any domain‑specific vocabularies you decide to introduce later
  (e.g. legal, medical, financial Areas/Families).

If you list new terms, domains, or variables you introduce,
they should be added here with the same pattern:
academic definition + project usage + “Used in” references.
