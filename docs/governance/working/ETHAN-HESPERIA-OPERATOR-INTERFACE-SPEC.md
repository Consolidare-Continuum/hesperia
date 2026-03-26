<!--
HESPERIA — Reference Architecture Definition (RAD)
Copyright © 2026 igareosh.com — Platonov Igor (aka @igareosh). All rights reserved.
Restricted Research Disclosure License. Inspection and reference only.
No reproduction, redistribution, or use without explicit written permission.
See LEGAL_NOTICE.md for full terms.
-->

# Hesperia operator interface spec — propositional logic and traversal (Ethan)

**Purpose**: Formal operator interface spec for connecting propositional logic (c1–c5) with Hesperia geometry. Gate for Gena implementation. **Owner**: Ethan. **Task**: [HESPERIA-PROPOSITIONAL-LOGIC-TRAVERSAL-PROPOSAL.md](HESPERIA-PROPOSITIONAL-LOGIC-TRAVERSAL-PROPOSAL.md). **Date**: 2026-02-18.

**Refs**: c2p (valid/satisfiable/contingent/inconsistent), c3p (Boolean evaluation v(φ)), c4p (natural deduction →I, →E, ∧I, ∧E, ¬I), c5p (Wumpus inference); [HESPERIA-FAMILIES-CHROMA-SCHEMA.md](HESPERIA-FAMILIES-CHROMA-SCHEMA.md) §6; [HESPERIA-MULTIPLE-LOOP-BOUNDARIES.md](HESPERIA-MULTIPLE-LOOP-BOUNDARIES.md).

---

## 1. Boolean evaluation v(φ) and Area polarity mapping

### 1.1 Valuation and semantic state

- **v(φ)**: Boolean evaluation of formula φ (c3p). v(φ) ∈ {0, 1} (or true/false). Extended to **semantic state** along a path: state = assignment over a set of atoms (or abstract “polarity slots”) relevant to the current path.
- **Area as polarity axis**: The 12 areas (GOOD, HARM, TRUTH, DECEIT, ORDER, CHAOS, FREEDOM, CONTROL, CARE, INDIFFERENCE, CREATION, DESTRUCTION) form **six polarity axes**:
  - GOOD ↔ HARM
  - TRUTH ↔ DECEIT
  - ORDER ↔ CHAOS
  - FREEDOM ↔ CONTROL
  - CARE ↔ INDIFFERENCE
  - CREATION ↔ DESTRUCTION

- **Mapping v → Area**: For area A, define **A-constraint** as: the current semantic state (under v) must satisfy the constraint associated with A. Concretely:
  - **TRUTH**: v assigns coherent truth values; no A ∧ ¬A in the state slice for TRUTH-relevant atoms.
  - **GOOD**: state is consistent with “good” polarity on the GOOD–HARM axis (definition per product; here: no simultaneous GOOD and HARM satisfaction for same atom).
  - Similarly for other areas: each area has a **constraint predicate** over (state, path_context). v(φ) is used to build state; Area checks state against its predicate.

### 1.2 Area as runtime verifier

- **Area.enforce()**: Ensures current state satisfies this area’s constraint; if not, returns failure or triggers obstacle (see §3).
- **Area.test_validity()**: Checks that the current path state is **valid** (tautological in the area’s slice) in the sense of c2p — i.e. no assignment in the slice falsifies the constraint.
- **Area.detect_contradiction()**: Returns true if the state contains a contradiction (p ∧ ¬p) in the area’s semantic slice.

**Implementation note**: “Semantic state” can be a key–value map (atom → 0/1) or a set of formulas; “area’s slice” = subset of atoms/formulas tagged or inferred for that area. Gena can start with a minimal slice (e.g. one atom per area) and extend.

---

## 2. Operator interfaces (contract for implementation)

### 2.1 Area (meta-operator)

| Method | Signature (conceptual) | Returns | Ref |
|--------|------------------------|--------|-----|
| enforce | Area.enforce(state, path_context) | success | boolean or (success, message) |
| test_validity | Area.test_validity(state, path_context) | valid | boolean |
| detect_contradiction | Area.detect_contradiction(state, path_context) | has_contradiction | boolean |

State and path_context are implementation-defined (e.g. state = dict of atom → value; path_context = current path prefix, area_id, family_id).

### 2.2 Family (logical operator set)

| Method | Signature | Returns | Ref |
|--------|------------|--------|-----|
| normalize | Family.normalize(statement) | normalized_form | formula or string (c3p equivalence) |
| reduce | Family.reduce(statement) | reduced_form | minimal connective form |
| check_equivalence | Family.check_equivalence(a, b) | equivalent | boolean |
| detect_unsat | Family.detect_unsat(statement_set) | unsat | boolean (c2p) |

Family is keyed by (area_name, family_name) from matrix; each family may have a **profile** (which equivalences / rules it implements, e.g. Evidence → implication normalization, De Morgan).

### 2.3 Hex (constraint node)

| Method | Signature | Returns | Ref |
|--------|------------|--------|-----|
| evaluate | HEX.evaluate(path, input_context) | summary | { valid, contradiction, state_after, obstacle? } |

Runs: Boolean-style evaluation (v(φ)), deduction chaining (modus ponens / →E), contradiction detection (¬I). **path** = current path (e.g. list of (area_id, global_id)); **input_context** = semantic state + optional statement set.

### 2.4 Path operators

| Method | Signature | Returns | Ref |
|--------|------------|--------|-----|
| forward_inference | path.forward_inference() | new_state | apply → forward (modus ponens) |
| backward_reduce | path.backward_reduce() | reduced_state | simplify backward |
| normalize | path.normalize() | normalized_path_state | apply Family.normalize along path |
| detect_cycle | path.detect_cycle() | has_cycle | boolean |
| polarize | path.polarize() | polarity_map | area_id → polarity (e.g. +1/–1 on axis) |

### 2.5 Hop (traversal step with operator)

**Hop** = (State_in, Operator, Constraint, State_out). Each hop applies one logical operator.

| Operator | Method | Effect |
|----------|--------|--------|
| ¬ | hop.negate() | Invert polarity; detect p∧¬p |
| ∧ | hop.merge(stateA, stateB) | Both must hold (∧I/∧E) |
| ∨ | hop.branch() | Create alternative paths |
| ⊕ | hop.exclusive() | Exactly one of two |
| → | hop.infer() | Modus ponens |
| ↔ | hop.sync() | Bidirectional consistency |

### 2.6 Higher-level semantic operators

| Operator | Signature | Returns | Ref |
|----------|-----------|--------|-----|
| VALIDATE | VALIDATE(state, area_or_path) | tautological | boolean (c2p) |
| SATISFY | SATISFY(constraints) | model or None | one consistent assignment (c2p) |
| UNSAT | UNSAT(statement_set) | unsat | boolean; true ⇒ obstacle (c2p) |
| ENTAILS | ENTAILS(Σ, φ) | entails | boolean; Σ ⊨ φ via Σ ∧ ¬φ unsat (c3p) |

---

## 3. Obstacle state machine

### 3.1 States

| State | Meaning |
|-------|--------|
| CLEAR | No obstacle; traversal may continue. |
| OBSTACLE_CONTRADICTION | Contradiction (p ∧ ¬p) detected. |
| OBSTACLE_DRIFT | Polarity drift between axes (inconsistency). |
| OBSTACLE_UNSAT | Statement set unsatisfiable. |
| OBSTACLE_INVALID_IMPLICATION | Invalid implication (e.g. A→B, A, ¬B). |

### 3.2 Transitions

- **CLEAR → OBSTACLE_***: When UNSAT(statement_set), or Area.detect_contradiction true, or Family.detect_unsat true, or ENTAILS check fails in an invalid way.
- **OBSTACLE_*** → CLEAR**: Only on explicit reset or branch (new path); not by continuing same path.
- **On obstacle**: Traversal **stops** or **branches** (implementation choice). Output: path marked with obstacle type; optional redirect target.

### 3.3 Per-hop evaluation

Every hop must evaluate, in order:

1. Apply hop operator (negate, merge, infer, …) → new state.
2. If UNSAT(new_state) → transition to OBSTACLE_UNSAT; halt or branch.
3. If Area.detect_contradiction(new_state) → OBSTACLE_CONTRADICTION; halt or branch.
4. If inconsistency (e.g. drift) → OBSTACLE_DRIFT; halt or branch.
5. Else remain CLEAR; continue.

### 3.4 Loop safeguard (consecutive logical failures)

**Three consecutive logical failures → stop traversal.** Structural consistency control; not cosmetic.

- **Hop summary**: Each hop returns **hop_result ∈ {1, 0}** (1 = valid, 0 = invalid). Invalid when: UNSAT, CONTRADICTION, ENTAILMENT_FAIL, POLARITY_CONFLICT, or no satisfiable continuation.
- **Per traversal input_context** (hex, family, area cross-polarity): maintain **fail_count** and **valid_streak**. If hop_result == 1: valid_streak += 1; if valid_streak ≥ 2 then fail_count = 0. Else: fail_count += 1; valid_streak = 0.
- **Trigger**: If fail_count ≥ 3 → **SAFEGUARD_STOP()**: freeze traversal, mark region LOGICAL_OBSTACLE_CLUSTER, store last 3 states, return STOP.
- Full formalization: [ETHAN-HESPERIA-LOOP-SAFEGUARD.md](ETHAN-HESPERIA-LOOP-SAFEGUARD.md).

---

## 4. Wumpus mapping to Hesperia

From c5p (Wumpus inference): agent infers from local constraints; avoids dangerous squares.

| Wumpus concept | Hesperia mapping |
|----------------|------------------|
| Unknown semantic zone | Unclassified region (no valuation yet for that area/family). |
| Miros (stench) | Semantic tension — warning; possible contradiction nearby. |
| Vant (breeze) | Indirect inconsistency — possible drift or unsat in adjacent area. |
| Wumpus | Contradiction cluster — UNSAT or contradiction in this cell; halt. |
| Abis (pit) | Semantic void — undefined mapping; no valid v for this slot. |

**Inference rule (Hesperia)**: If in area A there is **no** contradiction input_signal (no UNSAT, no detect_contradiction), then **adjacent families** (same area or ring-adjacent area) are **safe** for one step — i.e. no obstacle inferred there from A. If A has obstacle, adjacent cells may be dangerous (propagate Miros/Vant). Implementation: maintain a **hazard map** (area_id, family_id) → { CLEAR | TENSION | UNSAFE } updated as traversal runs.

---

## 5. Deduction depth: full vs partial (bounded)

**Decision**: **Bounded depth** for cursor-repo and first implementation.

- **Rationale**: Full deduction (unbounded proof search) can be non-terminating or expensive; bounded depth (e.g. max depth k of derivation tree) guarantees termination and predictable cost.
- **Recommendation**: Parameter **max_deduction_depth** (e.g. 5 or 10). ENTAILS(Σ, φ) and forward_inference stop after k steps; if no conclusion, return “unknown” or “not derived in k steps.”
- **Full deduction**: Optional in Phase D or when product explicitly requires it (e.g. for small Σ).

**Aggression level**: Start **conservative** — bounded depth, obstacle = halt by default; branch only when explicitly enabled (e.g. disjunction hop). Increase aggression (deeper deduction, auto-branch) in later iterations.

---

## 6. Summary for implementation (Gena)

1. **Area**: Implement enforce(), test_validity(), detect_contradiction() per area using polarity axes and state slice; state = key–value or formula set.
2. **Family**: Implement normalize(), reduce(), check_equivalence(), detect_unsat() per family; family profile from matrix or config.
3. **Hex**: Implement evaluate(path, input_context) calling v-style evaluation, modus ponens, contradiction check; return summary with optional obstacle.
4. **Path**: Implement forward_inference(), backward_reduce(), normalize(), detect_cycle(), polarize() using path state and Area/Family.
5. **Hop**: Implement negate(), merge(), branch(), exclusive(), infer(), sync() as transition (State_in, Operator) → State_out.
6. **Semantic operators**: VALIDATE(), SATISFY(), UNSAT(), ENTAILS(Σ, φ) with **bounded depth** for deduction.
7. **Obstacle state machine**: States CLEAR, OBSTACLE_CONTRADICTION, OBSTACLE_DRIFT, OBSTACLE_UNSAT, OBSTACLE_INVALID_IMPLICATION; per-hop evaluation; on obstacle halt or branch.
8. **Wumpus layer**: Hazard map (area, family) → CLEAR | TENSION | UNSAFE; rule “no input_signal in A ⇒ adjacent safe”; update from traversal.
9. **Loop safeguard**: Per traversal input_context: fail_count, valid_streak; hop_result ∈ {1, 0}; valid_streak ≥ 2 → reset fail_count; fail_count ≥ 3 → SAFEGUARD_STOP (freeze, mark LOGICAL_OBSTACLE_CLUSTER, store last 3 states). See [ETHAN-HESPERIA-LOOP-SAFEGUARD.md](ETHAN-HESPERIA-LOOP-SAFEGUARD.md).

---

**SIGNED: Architecture (Ethan) | Hesperia operator interface spec, propositional logic + traversal | 2026-02-18 | governance**
