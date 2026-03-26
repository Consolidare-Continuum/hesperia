<!--
HESPERIA — Reference Architecture Definition (RAD)
Copyright © 2026 igareosh.com — Platonov Igor (aka @igareosh). All rights reserved.
Restricted Research Disclosure License. Inspection and reference only.
No reproduction, redistribution, or use without explicit written permission.
See LEGAL_NOTICE.md for full terms.
-->

# Hesperia loop safeguard — logic-based structural consistency (Ethan)

**Purpose**: Formalize the **logic-based loop safeguard**: three consecutive logical failures → stop traversal. Not cosmetic; structural consistency control. **Owner**: Ethan. **Date**: 2026-02-18.

**Refs**: [ETHAN-HESPERIA-OPERATOR-INTERFACE-SPEC.md](ETHAN-HESPERIA-OPERATOR-INTERFACE-SPEC.md) §3 (obstacle state machine), [HESPERIA-PROPOSITIONAL-LOGIC-TRAVERSAL-PROPOSAL.md](HESPERIA-PROPOSITIONAL-LOGIC-TRAVERSAL-PROPOSAL.md).

---

## I. Definition: “0 output” (hop logical failure)

A **hop** returns **0** (invalid / logical failure) when any of the following holds:

| Condition | Meaning |
|-----------|--------|
| **UNSAT()** | Statement set unsatisfiable (c2p). |
| **CONTRADICTION()** | Area.detect_contradiction or p ∧ ¬p in state. |
| **ENTAILMENT_FAIL()** | ENTAILS(Σ, φ) required but Σ ⊭ φ (e.g. Σ ∧ ¬φ satisfiable). |
| **POLARITY_CONFLICT()** | Polarity drift between axes (e.g. same atom satisfies both GOOD and HARM). |
| **No satisfiable semantic continuation** | SATISFY(constraints) returns None. |

This is **not** a runtime error. It is a **logical failure state**.

**Hop summary type**:

- **hop_result ∈ { 1, 0 }**
  - **1** = valid (hop satisfied; traversal may continue).
  - **0** = invalid (one of the conditions above; logical failure).

**Extended (optional)**:

- **hop_result ∈ { +1, 0, -1 }**
  - **+1** = stable (valid).
  - **0** = soft fail (e.g. ambiguity, no conclusion in bounded depth).
  - **-1** = contradiction (hard failure).

Then: accumulate **fail_score**; if **fail_score ≤ -3** → STOP (nuanced variant).

---

## II. Consecutive logical-fail counter

**State**:

- **fail_count** = 0 (integer, per traversal input_context).

**Per hop**:

```text
if hop_result == 1:
    fail_count = 0   # reset on valid hop
else:
    fail_count += 1
```

**Rule**:

```text
if fail_count >= 3:
    SAFEGUARD_STOP()
```

Only **three consecutive** failures trigger the safeguard.

---

## III. Why 3 (not 1, not unbounded)

| Threshold | Rationale |
|-----------|-----------|
| **1** | Too sensitive; traversal becomes fragile; single noise triggers stop. |
| **2** | Still can be branch ambiguity or transient. |
| **3** | Indicates **structural dead zone**: semantic region inconsistent, path logically blocked, inference direction wrong, or input_context injection flawed. Three failures = **pattern**, not noise. |

---

## IV. SAFEGUARD_STOP — behaviour

**Not** just break loop. It must:

1. **Freeze traversal** (no further hops in this input_context).
2. **Mark region** as **LOGICAL_OBSTACLE_CLUSTER** (hazard map: UNSAFE or equivalent).
3. **Store last 3 states** (fail trace for diagnosis or backtrack).
4. **Backtrack or escalate** (implementation: return STOP; caller may backtrack or report).

**Pseudo**:

```text
def safeguard_stop(state, input_context):
    mark_obstacle(input_context.region)      # e.g. hazard_map[(area_id, family_id)] = UNSAFE
    store_fail_trace(last_3_hops)     # append state/hop to trace; keep last 3
    return STOP                       # enum or constant; traversal loop exits
```

**Output**: Traversal returns with **status = SAFEGUARD_STOP**; optional **fail_trace** (last 3 hop states); **obstacle_region** marked.

---

## V. Where to attach

Attach to **each traversal input_context** independently:

- **Hex traversal** (per-hex hop sequence).
- **Family traversal** (per-family hop sequence).
- **Area cross-polarity jump** (when crossing polarity axis).

**NOT** a single global loop. Each **traversal input_context** (e.g. one path through hexes, or one family sequence, or one area-bound run) has its **own** fail_count and valid_streak. So: one counter per (path_id or context_id), not one per process.

---

## VI. Cooldown reset — valid streak

**Requirement**: Reset fail_count only when **VALID_PATH_STREAK ≥ 2**. Otherwise a single valid hop could reset the pattern too easily after two failures.

**State**:

- **valid_streak** = 0 (integer).

**Per hop**:

```text
if hop_result == 1:
    valid_streak += 1
    if valid_streak >= 2:
        fail_count = 0
else:
    fail_count += 1
    valid_streak = 0
```

**Constants** (recommended):

- **CONSECUTIVE_FAIL_THRESHOLD** = 3
- **VALID_STREAK_RESET** = 2

---

## VII. Benefits

- Prevents **infinite logical loops**.
- Prevents **oscillation** between contradictory hexes.
- Detects **semantic dead ends**.
- Protects against **LLM-driven drift**.
- Forces **deterministic termination**.
- Creates **measurable consistency metric** (fail_count, valid_streak, safeguard_stop count).
- Improves **reproducibility**.

**Without it**: risk of endless inferential bouncing, drift amplification, silent contradictions.

---

## VIII. Strategic view

This turns Hesperia traversal into a **bounded logical inference engine** with:

- Forward inference
- Contradiction detection
- **Loop safeguard** (structural consistency control)

---

## IX. Summary for implementation (Gena)

1. **Hop summary**: Every hop evaluation returns **hop_result ∈ {1, 0}** (or +1/0/-1). Map UNSAT, CONTRADICTION, ENTAILMENT_FAIL, POLARITY_CONFLICT, no satisfiable continuation → 0 (or -1 in extended).
2. **Per traversal input_context**: Maintain **fail_count**, **valid_streak**; **CONSECUTIVE_FAIL_THRESHOLD = 3**, **VALID_STREAK_RESET = 2**.
3. **Update rule**: If hop_result == 1: valid_streak += 1; if valid_streak >= 2: fail_count = 0. Else: fail_count += 1; valid_streak = 0.
4. **Trigger**: If fail_count >= 3: call **SAFEGUARD_STOP(state, input_context)**.
5. **SAFEGUARD_STOP**: Freeze traversal; mark region LOGICAL_OBSTACLE_CLUSTER; store last 3 states (fail_trace); return STOP.
6. **Attachment**: One (fail_count, valid_streak) per traversal input_context (hex traversal, family traversal, area cross-polarity). Not global.

---

**SIGNED: Architecture (Ethan) | Hesperia loop safeguard — structural consistency control | 2026-02-18 | governance**
