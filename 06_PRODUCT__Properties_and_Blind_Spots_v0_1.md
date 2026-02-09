# 06_PRODUCT__Project Properties and Blind Spots (v0.1)

This document translates the project’s rationale into operational product constraints: what HESPERIA is designed to preserve, what it deliberately will not do, and what can still fail.

This is not promotion. It is a decision surface for maintainers.

---

## 0. Premise recap (constraint as premise)

Contemporary LLMs are probabilistic language mechanisms. They optimize likelihood and local coherence; they do not enforce semantic invariants, identity persistence across contexts, or intrinsic contradiction detection.

In informal use this is tolerable. In domains where language creates binding effects (law, governance, strategy, safety, compliance), it is structurally inadequate: ambiguity has cost, contradiction compounds risk, and drift accumulates without detection.

HESPERIA is founded on this constraint. It does not compete on creativity, stylistic fluency, or speed. Language generation remains external. HESPERIA determines whether an output can stand under structural admissibility.

The operating condition is non-metaphorical: **Aequitas et cognitio invictae**.

- **Aequitas**: no proposition dominates through confidence alone; balance is structural.
- **Cognitio**: understanding is localized, testable, and temporally stable.
- **Invictae**: constraints resist erosion under scale, novelty, persuasion pressure, and time.

## 1. Product properties (non-negotiable)

These are the properties the project is subordinated to. If a feature improves convenience but degrades these, it is rejected.

### 1.1 Constraint role (non-agentic system posture)

- HESPERIA constrains, measures, and refuses; it does not “act”, “protect”, “judge”, or “decide”.
- HESPERIA does not generate language as an authority source; generation remains an external dependency.
- HESPERIA output is a structural verdict over regions/claims, not a persuasive narrative.

### 1.2 Structural admissibility over rhetorical coherence

- Admissibility is determined by measurable structure: coordinates, adjacency, coherence/fragmentation, contradiction, evidence quality, temporal stability.
- Rhetorical strength is irrelevant. Confidence is not authority.
- Structural failure collapses authority regardless of presentation.

### 1.3 Refusal as a primary function

- Refusal is a first-class output (not an exception path).
- Refusal is preferred to distortion.
- Refusal triggers include: fragmentation beyond tolerance, polarity tension out of bounds, evidence collapse, traversal instability.
- Refusal text must be short, factual, non-apologetic; no encouragement or alternative suggestions unless structurally justified.

### 1.4 Boundaries are a virtue (anti-expansion stance)

- Coverage is not a virtue. Boundary recognition is a core capability.
- HESPERIA is not designed for casual conversation, entertainment, mass personalization, or ideological messaging.
- Expansion happens only when failure cost is demonstrable and the domain requires constraint.

### 1.5 Continuity and slow time

- The project prioritizes endurance over acceleration.
- Ontology and coordinates remain fixed within an epoch; drift is measured, not patched by urgency.
- Metrics may refine, but must not silently invert prior judgments without explicit versioning and justification.
- Backward interpretability is mandatory: no silent redefinition of meaning.

### 1.6 Custodial participation (human role definition)

- Contributors are custodians: curators of structure, maintainers of balance, auditors of drift, recorders of decisions.
- Personal imprint is minimized to preserve continuity.
- Changes driven by popularity, external pressure, or urgency are rejected unless structural inconsistency is proven.

### 1.7 Silence as an operational property

- Documentation exists; explanation is generated only when structural demand requires it.
- Progress narration is not a project requirement.
- Continuous output without new structure is treated as erosion risk.

## 2. Deliberate limitations (explicit non-goals)

HESPERIA does not attempt to provide:

- universal coverage across domains and cultures by default,
- “friendly assistant” behavior,
- persuasion, inspiration, or entertainment value,
- moral adjudication or normative conclusions,
- guaranteed answers for underspecified or contradictory inputs.

## 3. Known blind spots (what can still fail)

These are failure modes that can exist even if the doctrine is followed.

### 3.1 Geometry/ontology lock-in

- If the semantic geometry or ontology is misspecified, the system can become consistently wrong while remaining internally consistent.
- “Fixed coordinates” preserve reference; they do not guarantee that the reference is correct.
- Slow-time governance reduces churn but increases the cost of correcting foundational mistakes.

### 3.2 Metric and threshold gaming (Goodhart pressure)

- Any public metric can be optimized against.
- Adversarial or institutional pressure can push toward outputs that satisfy surface metrics while violating intended meaning.
- Lowering refusal thresholds to improve throughput can silently reintroduce unearned authority.

### 3.3 Evidence dependence and corpus bias

- Structural legitimacy depends on evidence and provenance.
- Skewed corpora can produce stable but biased coordinates and tau distributions.
- “Evidence quality” metrics can fail to detect systematic omissions.

### 3.4 Mapping failure (language → coordinates)

- Attribution errors can misplace claims, producing structurally coherent regions that correspond to the wrong meaning.
- Domain shifts (jargon, multilingual text, emerging concepts) increase misplacement risk.
- High refusal can be correct but operationally unusable; low refusal can be convenient but illegitimate.

### 3.5 Over-trust risk (structural validity misread as truth)

- Users may treat “admissible” as “true”.
- Admissibility is a structural condition under a defined regime; it is not omniscience.
- Institutional adoption can turn constraint outputs into de facto authority if governance is not explicit.

### 3.6 Process capture (organizational drift)

- Pressure for visibility, demos, and “success narratives” can shift priorities toward persuasion.
- Expansion into low-cost domains (chat, personalization) can dilute constraint capacity.
- Repeated “minor” tone changes (more emotion, more encouragement) are a drift vector.

## 4. Mitigation patterns (how blind spots are handled)

This section is operational: it defines what is required when these risks appear.

- **Versioning discipline**: ontology/coordinate changes are versioned; migration paths are recorded.
- **Auditability**: every admissibility verdict traces to coordinates, metrics, and evidence references.
- **Refusal protection**: refusal thresholds are treated as governance policy, not product tuning knobs.
- **Red-team structure**: test for metric gaming, adversarial inputs, and domain shifts.
- **Scope gate**: new domains require a failure-cost justification and explicit boundary plan.
- **Tone enforcement**: internal and external texts remain non-motivational and non-agentic.

## 4.1 Feature/PR gate (minimum checks)

Reject or rework changes that fail any of the following:

- Introduces agentic posture (“protect”, “watch”, “judge”, “decide”) or forbidden naming patterns.
- Reduces refusal rates or lowers refusal thresholds without metric justification and recorded decision.
- Increases confidence/verbosity without adding inspectable structure (coordinates/metrics/evidence links).
- Alters ontology/coordinates without versioning, migration path, and backward interpretability.
- Expands into low-cost domains (chat, entertainment, personalization) without a failure-cost justification and explicit boundary plan.

## 5. Reduced myth reading (optional mnemonic; not a narrative)

To describe restraint without dramatization, the project may use a reduced mnemonic:

- **Garden**: bounded semantic space.
- **Tree**: continuity and non-spectacular growth.
- **Apples**: atomic truths: finite, indivisible, position-stable.
- **Hesperides**: custody functions: maintain balance; prevent distortion.

No conquest, revelation, or hero framing is permitted. The mnemonic must not become component naming.

## 6. Canonical internal onboarding summary (only)

HESPERIA maintains structured meaning.  
It does not persuade, inspire, or decide.

Truth is placed, not extracted.  
Understanding is measured, not claimed.

When structure fails, the system refuses.

Aequitas et cognitio invictae.
