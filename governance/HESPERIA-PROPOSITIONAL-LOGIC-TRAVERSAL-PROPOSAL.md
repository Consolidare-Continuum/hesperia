# Hesperia — propositional logic and traversal (team tasks)

**Purpose**: Connect formal propositional logic (c1–c5 material) with Hesperia geometry. Operators inside the sphere; no classification-only. Direction for dev: Area as meta-operator, Family as logical operator set, Hex as constraint node, obstacle mode, Wumpus inference layer; logical operators embedded in traversal hops. **Triage**: Grace. **Date**: 2026-02-18.

**Sources (PDFs)**: Boolean evaluation v(φ) (c3p); valid/satisfiable/contingent/inconsistent (c2p); natural deduction rules →I, →E, ∧I, ∧E, ¬I (c4p); semantic reasoning & Wumpus inference model (c5p).

---

## I. AREA as Meta-Operator (Semantic Field Operator)

Each AREA = field constraint operator.

- **Instead of**: "Area: TRUTH" (tagging).
- **Allow**: `TRUTH.enforce()`, `TRUTH.test_validity()`, `TRUTH.detect_contradiction()`.
- **What it does**: Validity/satisfiability checks across a path; internal consistency (logical consistency); drift between polarity axes.
- **Why**: "This semantic object satisfies TRUTH constraints under evaluation function v." TRUTH becomes a runtime verifier.

## II. FAMILY as Logical Operator Set

Families = operator clusters (not only taxonomic).

- **Example**: Family Evidence (TRUTH domain): implication normalization (p → q ≡ ¬p ∨ q), contradiction detection, De Morgan, minimal connective reduction (c3p).
- **Interfaces**: `Evidence.normalize(statement)`, `Evidence.reduce()`, `Evidence.check_equivalence(a,b)`, `Evidence.detect_unsat()`.
- Families become transformation engines.

## III. HEX as Constraint Node

Hex = semantic constraint surface; each side = directional constraint (logical polarity).

- **Interface**: `HEX.evaluate(path, context)` — runs Boolean-style evaluation (v(φ)), deduction chaining (modus ponens / →E), contradiction detection (¬I) (c4p).

## IV. Obstacle Mode

Hex / Family / Area can act as obstacle operators.

- **Example**: Path TRUTH → Evidence → Causality; statements A→B, A, ¬B → unsatisfiable set (contradiction p∧¬p, c2p). Path becomes **OBSTACLE: CONTRADICTION**; traversal stops or branches.

## V. Wumpus Model as Semantic Navigation Layer

Wumpus (c5p) → Hesperia: agent infers from local constraints; avoids dangerous squares.

- **Map**: Unknown semantic zones = unclassified regions; "Miros" = semantic tension; "Vant" = indirect inconsistency; "Wumpus" = contradiction cluster; "Abis" = semantic void.
- **Rule**: If no contradiction signal in area, adjacent families safe. Inferential semantic navigation.

## VI. Semantic Operators to Implement

1. **VALIDATE()** — tautology check under polarity mapping.
2. **SATISFY()** — one consistent semantic configuration.
3. **UNSAT()** — structural contradiction (obstacle trigger).
4. **ENTAILS(Σ, φ)** — Σ ⊨ φ via Σ ∧ ¬φ unsatisfiable (c3p). Families = reasoning modules.

## VII. Path Operators

- `path.forward_inference()`, `path.backward_reduce()`, `path.normalize()`, `path.detect_cycle()`, `path.polarize()`.
- Sphere computes; not static.

## VIII. Benefits

- Prevent semantic drift; detect contradiction numerically; deterministic entailment; obstacle-based traversal; safe inference navigation (Wumpus); classification → computation; preparation for Phase D semantic product layer.

## IX. Strategic

- LLM generates; sphere evaluates. Sphere can: block invalid inference, redirect traversal, flag inconsistency, compute entailment confidence. Architectural upgrade.

## X. Traversal Hops = Computation

**Current**: Hex_A → Hex_B → Hex_C (movement).

**Upgraded**: Hop = (State_in, Operator, Constraint, State_out). Traversal = S0 --∧--> S1 --→--> S2 --¬--> S3. Every hop applies a logical operator.

### Core logical operators in traversal (c3p, c4p)

| Operator | In traversal | Benefit |
|----------|--------------|---------|
| **¬** (negation) | hop.negate(); inverts polarity; contradiction p∧¬p | Drift analysis, boundary enforcement |
| **∧** (conjunction) | hop.merge(stateA, stateB); ∧I/∧E | Structural coherence, multi-axis clusters |
| **∨** (disjunction) | hop.branch() | Ambiguity, forked traversal |
| **⊕** (XOR) | hop.exclusive() | Decision enforcement, conflict detection |
| **→** (implication) | hop.infer(); modus ponens | Forward inference, causal chain |
| **↔** (equivalence) | hop.sync() | Bidirectional consistency |

### Higher-level in traversal (c2p)

- **VALIDATE()** — tautological in area.
- **SATISFIABLE()** — at least one consistent configuration.
- **UNSAT()** — contradiction → obstacle, halt.
- **ENTAILS(Σ, φ)** — reasoning closure.

### Obstacle integration

- Every hop: if UNSAT → obstacle; if inconsistency → block; if contradiction → freeze path (Wumpus-style, c5p).

### Outcome

- Sphere = geometry-driven propositional constraint engine. Not tagging/embedding/vector retrieval; actual reasoning substrate. SAT-style semantic validation; obstacle-aware reasoning.

---

## Team tasks (active.md)

1. **Ethan**: Formalize operator interface spec — boolean evaluation v(φ) → Area polarity mapping; obstacle state machine; deduction depth (full vs partial); Wumpus mapping to Hesperia. Deliverable: spec doc. Gate for implementation. **DONE**: [ETHAN-HESPERIA-OPERATOR-INTERFACE-SPEC.md](ETHAN-HESPERIA-OPERATOR-INTERFACE-SPEC.md) (2026-02-18).
2. **Gena**: When Ethan spec ready: implement Area/Family/Hex as semantic operators (enforce, test_validity, detect_contradiction; normalize, reduce, check_equivalence, detect_unsat; evaluate(path, context)); obstacle mode; path operators (forward_inference, backward_reduce, normalize, detect_cycle, polarize); hop operators (negate, merge, branch, exclusive, infer, sync); VALIDATE, SATISFY, UNSAT, ENTAILS. Ref: this proposal, [ETHAN-HESPERIA-OPERATOR-INTERFACE-SPEC.md](ETHAN-HESPERIA-OPERATOR-INTERFACE-SPEC.md), c1–c5 material.

---

**SIGNED: Product (Grace) | Hesperia propositional logic + traversal proposal, team tasks | 2026-02-18 | governance**
