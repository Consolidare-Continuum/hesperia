# HESPERIA (HSPR) — ACADEMIC GLOSSARY (Draft)

Purpose: provide a **single point of truth** for terminology, using
university‑style (academic) definitions and then explaining how each term
is used inside this project. This file is for everyone: researchers,
engineers, and AI assistants.

Version note: updated for Semantic Stability Control integration (v0.2.1).

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
  `11_BLUEPRINT__HESPERIA_v4_5_full.txt`,  
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
  `11_BLUEPRINT__HESPERIA_v4_5_full.txt` (query pipeline),  
  `sphere_rag/pipeline.py`.

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


### Guard Layer (ΣΓΘ)
- **Academic definition**
  A guard layer is a formal invariant-enforcement boundary that validates
  whether a system state is admissible before execution continues.
- **Project usage**
  HESPERIA applies a three-tier guard stack: **Σ** for static topology and
  indexing invariants, **Γ** for runtime and structure-dynamics coherence, and
  **Θ** for governance legitimacy before publication. The ordered gate
  `Σ → Γ → Θ` upgrades the pipeline from semantic modeling to controlled
  semantic operation with typed failures (`HALT`, `ROLLBACK`, `CORRECT`,
  `REQUIRE_REVIEW`).
- **Used in**
  `42_POLICY__Guard_Layer_Sigma_Gamma_Theta_v1_0.txt`,
  `40_POLICY__Loopability_and_traversal.txt`,
  `41_POLICY__Operational_additions_v0_1.txt`.

### Structural Integrity / Dynamic Stability / Governance Legitimacy
- **Academic definition**
  Respectively: preservation of formal structure constraints, bounded and
  coherent temporal behavior, and procedurally authorized decision release.
- **Project usage**
  - **Structural integrity (Σ):** constant/cardinality/indexing/topology
    correctness checks executed at boot, migration, and pre-traversal.
  - **Dynamic stability (Γ):** loop-time checks for drift, fragmentation,
    coherence, and polarization control.
  - **Governance legitimacy (Θ):** final publish gate for hash-locked config,
    override discipline, and non-empty publishable outputs.
- **Used in**
  `42_POLICY__Guard_Layer_Sigma_Gamma_Theta_v1_0.txt`,
  `14_SPEC__Services_and_APIs_v0_1.txt`.

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

### Context Integrity (#contextIntegrity)
- **Academic definition**  
  Context integrity is the degree to which a semantic state remains coherent, complete, and resistant to drift under current constraints.
- **Project usage**  
  #contextIntegrity is a bounded [0,1] control metric combining region reliability, loopability, obstacle pressure, normalized tension, and evidence quality. It is used as a governance signal for correction thresholds.
- **Used in**  
  `19_SPEC__Semantic_Stability_Control_v1_0.txt`,  
  `21_MATH__HESPERIA_formalization_v1_1_java.txt`,  
  `41_POLICY__Operational_additions_v0_2.txt`.

### Stability Vector (#stabilityVector)
- **Academic definition**  
  A stability vector is a compact state representation grouping control-relevant indicators for monitoring and decisioning.
- **Project usage**  
  #stabilityVector aggregates regionReliability, contextIntegrity, decayRate, and short-horizon forecast integrity values. It is logged for governance replay and release-quality diagnostics.
- **Used in**  
  `19_SPEC__Semantic_Stability_Control_v1_0.txt`,  
  `41_POLICY__Operational_additions_v0_2.txt`.

### Decay Rate (#decayRate)
- **Academic definition**  
  Decay rate is the per-step loss factor in a dynamic system that quantifies expected degradation over time.
- **Project usage**  
  #decayRate models expected semantic degradation per turn from obstacle pressure, tension, fragmentation, and loopability compensation. It powers deterministic k-step integrity forecasts.
- **Used in**  
  `19_SPEC__Semantic_Stability_Control_v1_0.txt`,  
  `21_MATH__HESPERIA_formalization_v1_1_java.txt`,  
  `41_POLICY__Operational_additions_v0_2.txt`.

### Semantic Control Layer
- **Academic definition**  
  A semantic control layer is a supervisory component that monitors semantic state variables and adjusts decision policy without altering foundational representation geometry.
- **Project usage**  
  The Semantic Stability Control Layer is a non-blocking advisory module that computes reliability, integrity, and decay forecasts, then maps them into governance outcomes (`ALLOW`, `REQUIRE_CORRECTION`, `FORBID`).
- **Used in**  
  `11_BLUEPRINT__HESPERIA_v4_8_full.txt`,  
  `19_SPEC__Semantic_Stability_Control_v1_0.txt`,  
  `41_POLICY__Operational_additions_v0_2.txt`.

