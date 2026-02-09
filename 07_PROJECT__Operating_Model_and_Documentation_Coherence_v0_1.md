# 07_PROJECT__Operating Model and Documentation Coherence (v0.1)

Purpose: maintain coherence of terms, scope, and change over time by translating doctrine into an IT-style operating model: roles, artifacts, gates, red flags, and development borders.

This document is internal. It is a constraint surface for maintainers.

---

## 0. Canonical references (single sources of truth)

When conflicts appear, resolve by reference order:

1. **Doctrine**: `04_IDEOLOGY__Aequitas_et_cognitio_invictae_v0_2.md`
2. **Product properties / blind spots**: `06_PRODUCT__Properties_and_Blind_Spots_v0_1.md`
3. **Identity (motto + seal)**: `05_IDENTITY__Motto_and_Seal_v0_1.md`
4. **Core system specs**: `10_MASTER_SPEC__HESPERIA_v1_0.txt` and `11_BLUEPRINT__HESPERIA_v4_7_full.txt`
5. **Component specs**: `12_SPEC__Semantic_Engine_v0_4.txt`, `13_SPEC__Indexing_and_Coordinates_v1_0.txt`, `14_SPEC__Services_and_APIs_v0_1.txt`, `15_SPEC__Data_and_Schema_v0_1.txt`, `18_SPEC__MySQL_integration_and_ingestion_v0_1.txt`
6. **Policies**: `40_POLICY__Loopability_and_traversal.txt`, `41_POLICY__Operational_additions_v0_1.txt`
7. **Glossary (terms)**: `ACADEMIC.md`

If code behavior conflicts with (1–3), code is considered drifting.

## 1. Term coherence rules (project vocabulary)

### 1.1 Canonical terms (use these)

- **Constraint system**: HESPERIA constrains and evaluates; it does not “act”.
- **Admissibility**: structural legitimacy under declared constraints (not truth).
- **Region**: structured semantic subset used for metrics/traversal.
- **Refusal**: correct abstention under insufficient structure (first-class output).
- **Evidence / provenance**: what ties structure to sources.
- **Epoch**: versioned interval with fixed coordinates/poles.

### 1.2 Disallowed synonyms (avoid these in docs and interfaces)

Avoid language that implies agency, omniscience, conquest, or intelligence claims.

- Disallowed posture verbs: protect, guard, watch, judge, decide, conquer.
- Disallowed names (examples): “Oracle”, “Sentinel”, “Guardian”, “Watcher”, “Engine of Truth”.

Prefer: constrain, measure, expose, refuse, admit/inadmissible, trace.

### 1.3 Term mapping (reduce ambiguity)

Use this mapping when writing specs and tickets:

- “Claim” (informal) → **Statement** (spec) → **Placed structure** (coordinates + relations).
- “Answer” (informal) → **Region verdict** (admissible / inadmissible / refuse) + trace.
- “Safety” (informal) → **Governance** (metrics + thresholds + refusal).
- “Consistency” (informal) → **Stability** (rotation-resistance + temporal checks).

If a new term is introduced, it must be added to `ACADEMIC.md` with a definition and “Used in” references.

## 2. Documentation operating model (IT-style)

### 2.1 Artifact types (what each doc is allowed to do)

- **Doctrine** (04): non-negotiable constraints; defines what the project must not become.
- **Product properties** (06): operational properties, deliberate limitations, blind spots, gates.
- **Identity** (05): motto usage rules; seal encoding constraints.
- **Specs** (10–18): normative mechanics, schemas, and interfaces.
- **Policies** (40–41): metric/governance behavior and traversal logic.
- **Glossary** (ACADEMIC): definition surface for terms and variables.

Do not mix artifact types. If a spec becomes ideological, it drifts. If doctrine becomes technical, it dilutes.

### 2.2 Versioning rule

- Stable, referenced docs are versioned forward (e.g. `..._v0_2`) instead of rewritten.
- Reference-hygiene fixes (broken file references, stale line pointers, typos) may be applied in place when they do not change semantic meaning.
- Any change that shifts semantic reference (coordinates/poles/ontology meaning) is an **epoch boundary** and requires explicit migration/interpretability notes.

### 2.3 Change proposal format (minimum)

Any proposed change that affects meaning placement, metrics, refusal, or scope must include:

- **Problem**: what structural inconsistency or measured drift exists.
- **Constraint impact**: which doctrine/product properties it touches.
- **Proposed change**: what is modified (ontology/metric/threshold/process).
- **Backward interpretability**: what remains comparable; what requires versioning.
- **Failure modes**: what can go wrong and how it will be detected.

If the change cannot be stated in this format, it is likely narrative-driven.

## 3. Development borders (what is in-bounds)

### 3.1 In-bounds (allowed directions)

- Deterministic placement surfaces (attribution improvements that are auditable).
- Metric computation, governance thresholds, drift detection, and refusal behavior.
- Provenance and evidence-quality instrumentation.
- Ingestion pipelines and schemas that preserve traceability.
- Interfaces that expose structure (regions/coordinates/metrics) without persuasion.

### 3.2 Out-of-bounds (rejected directions)

- Personality layers, motivational output, “friendly assistant” behaviors.
- Features optimized primarily for engagement, satisfaction, or persuasion.
- Unbounded “answer generation” presented as authority.
- Silent suppression of refusal or contradictions.
- Expansion into low-cost domains (chat, entertainment, mass personalization) without failure-cost justification.

If a feature’s primary benefit is “it feels better”, it is out of scope by default.

## 4. Red flags (drift indicators)

Treat the following as drift signals requiring rollback or redesign:

- Documentation tone becomes motivational, urgent, or moralizing.
- Outputs become longer without new structure (coordinates/metrics/evidence links).
- Refusal rates decline without metric justification and recorded decision.
- Confidence increases without corresponding evidence/structure support.
- Naming implies agency, omniscience, conquest, or intelligence claims.
- UI/visuals imply invitation, reward, or authority-by-warmth.
- Ontology changes occur without versioning and migration notes.

Drift handling rule: revert first, then justify with structure. Intent does not override the motto.

## 5. Roles and responsibilities (custodial, not authorial)

Roles are functions, not identities:

- **Curator of structure**: maintains ontology definitions and mappings; enforces versioning.
- **Maintainer of balance**: evaluates equity impacts across semantic poles; reviews metric weights.
- **Auditor of drift**: monitors refusal rates, stability metrics, and documentation tone drift.
- **Recorder of decisions**: ensures changes have problem/impact/migration records and doc references.

These roles can be held by the same person, but the functions must be explicitly performed.

## 6. Quality gates (checklists)

### 6.1 Documentation gate (for any doc change)

Reject changes that:

- introduce agentic or persuasive language outside of “avoid”/“forbidden” lists,
- add new terms without adding them to `ACADEMIC.md`,
- change scope without updating `DOC_INDEX.md` entry paths,
- replace versioning with silent rewrites of referenced documents.

### 6.2 Implementation gate (for code/features)

Reject changes that:

- reduce refusal thresholds without measured justification,
- hide contradictions behind narrative smoothing,
- create untraceable authority (“model said so” without structure),
- break backward interpretability without explicit version boundary.

## 7. Communication constraints (coercion boundary)

Internal and external communication must remain:

- factual,
- constraint-oriented,
- record-like.

Avoid:

- motivational language,
- hype,
- urgency signaling,
- moral pressure.

Refusal messaging must remain short and non-apologetic. The system does not persuade; it constrains.
