# Hesperia — Post v0.1 checkpoint: formal definitions (Ethan)

**Purpose**: After observability extension v0.1 checkpoint, define **formal governance equation**, **obstacleScore composition**, **decision state machine**, or **analyze risks of premature control**. Definition and analysis only; no implementation or behaviour change until approved. **Owner**: Ethan. **Baseline**: [projects/hesperia/HESPERIA_OBSERVABILITY_EXTENSION_v0_1.md](../projects/hesperia/HESPERIA_OBSERVABILITY_EXTENSION_v0_1.md) (done). **Date**: 2026-02-18.

**Refs**: [ETHAN-HESPERIA-LOOP-SAFEGUARD.md](ETHAN-HESPERIA-LOOP-SAFEGUARD.md), [ETHAN-HESPERIA-OPERATOR-INTERFACE-SPEC.md](ETHAN-HESPERIA-OPERATOR-INTERFACE-SPEC.md) §3 (obstacle FSM), [RELEASE-V1-FIXED-POINT-2026-02-18.md](../projects/hesperia/RELEASE-V1-FIXED-POINT-2026-02-18.md).

---

## 1. Checkpoint

- **Observability v0.1**: Done. Packet has `observability` (loopability_band, entropy_metric, border_passings_count, direction, ring_distance_from_start, safeguard_events_count). Wrapper only; kernel untouched.
- **Discipline**: No geometry/traversal/safeguard core change. Next step = **formal definitions** on paper, not in engine.

---

## 2. Four directions (Ethan — choose one or more)

| # | Direction | Deliverable | Note |
|---|-----------|-------------|------|
| **A** | **Define formal governance equation now** | Single equation or small set that ties: loopability, safeguard trigger, observability signals, and (when present) tension/obstacle. No free-form prose only; formal expression (e.g. predicate, inequality, or state invariant). | Makes “when do we stop / when do we allow” explicit and auditable. |
| **B** | **Define obstacleScore composition** | How **obstacleScore** is composed from: hop_result (1/0), obstacle type (CONTRADICTION, DRIFT, UNSAT, …), optional weights, and how it relates to fail_count and SAFEGUARD_STOP. Formula or state update rules. | Complements existing obstacle FSM (§3 operator spec); no change to current three-fail rule until this is approved. |
| **C** | **Define decision state machine** | Explicit **decision** FSM: states (e.g. CONTINUE, PAUSE, BRANCH, STOP), inputs (observability fields, obstacle state, governance equation output), transitions. Separate from obstacle FSM; this is “what does the controller decide to do” given signals. | Clarifies control surface; avoids ad-hoc branching in callers. |
| **D** | **Analyze risks of premature control** | Short report: risks of introducing governance equation, obstacleScore, or decision FSM **before** observability and usage are stable. When does formal control become premature? Mitigations (e.g. advisory-only, feature flags, no wiring into traversal). | Informs whether to do A/B/C now or defer. |

---

## 3. Constraints

- **Definition only**: Deliverables are specs, equations, or reports. No code change to matrix_run, safeguard, or traversal kernel from this task.
- **Compatibility**: Any new equation or FSM must be consistent with Safeguard State Machine Spec v0.1 (three consecutive failures → stop; valid_streak ≥ 2 resets fail_count).
- **Observability first**: New formal objects may **consume** observability fields (loopability_band, entropy_metric, safeguard_events_count); they do **not** replace or bypass them.

---

## 4. Outputs

- **A**: Governance equation doc (or section in this file): predicate(s) / invariant(s) + interpretation.
- **B**: ObstacleScore composition spec: formula or state-update rules; link to obstacle FSM and loop safeguard.
- **C**: Decision state machine spec: states, inputs, transition table or rules.
- **D**: Risk analysis report: premature control risks + recommendations (proceed / defer / advisory-only).

Ethan may deliver one, several, or all; Grace may triage follow-on implementation tasks after review.

---

## 5. Delivered: D — Risk analysis (premature control)

**Risks of introducing governance equation / obstacleScore / decision FSM before observability is stable:**

| Risk | Description | Mitigation |
|------|--------------|------------|
| **Overfitting to few runs** | Equation or FSM tuned on current usage; breaks when traversal patterns or callers change. | Keep definitions **advisory-only** until observability has been logged over many runs and reviewed. |
| **Tight coupling** | Wiring equation into traversal or safeguard adds a new failure mode and complicates rollback. | Do **not** wire into matrix_run or safeguard kernel; policy layer or caller only. |
| **Threshold creep** | obstacleScore or decision FSM invites tuning thresholds (e.g. 3 → 2) without formal review. | Lock thresholds in spec; change only via governance (e.g. Ethan + Grace). |
| **Second control loop** | Decision FSM plus obstacle FSM = two state machines; deadlocks or unclear precedence. | Define decision FSM as **consumer** of obstacle state and observability; single authority (safeguard) still owns STOP. |

**When is formal control premature?** When (1) observability is not yet consumed by any operator or product, (2) no agreed “normal” vs “abnormal” band from the field, or (3) equation/FSM would be changed again soon after first use.

**Recommendation:** Proceed with **definitions on paper** (A, B, C) now. **Do not wire** governance equation or decision FSM into traversal or safeguard until Grace/Ethan agree that observability is stable and a control policy is approved. Use **advisory-only**: packet and logs carry the signals; callers may choose to restrict (e.g. “if loopability_band == unstable then do not enable chord jumps”) without kernel change.

---

## 6. Delivered: A — Formal governance equation (v0.1)

**Symbols (observability + safeguard):**

- **L** ∈ [0, 1] — loopability (L_full when present; else undefined).
- **band** ∈ { stable, transitional, unstable, unknown } — loopability_band from packet.
- **fc** ∈ ℕ — fail_count (consecutive logical failures in current traversal context).
- **se** ∈ ℕ — safeguard_events_count (observability; e.g. number of failures recorded toward STOP).
- **GO** — predicate: governance equation says “allow continuation” (true) or “do not allow” (false).

**Invariant (safeguard; already in force):**

```text
INV_safeguard:  (fc ≥ 3)  ⇒  STOP
```

No new behaviour; this is the current spec.

**Governance predicate (advisory; not wired into kernel):**

```text
GO(L, band, fc, se)  ≡  (fc < 3)  ∧  (band ≠ "unstable"  ∨  L > 0.4)
```

**Interpretation:**

- **Allow continuation** only if: (1) safeguard has not fired (fc < 3), and (2) either band is not unstable, or L_full is above 0.4 (transitional or stable).
- **Advisory use:** External caller or policy layer may restrict actions when ¬GO (e.g. disable chord jumps when band == unstable and L ≤ 0.4). Kernel does not evaluate GO.

**Inequality form (equivalent):**

- **Continue allowed** ⟺ fc < 3 ∧ (band = stable ∨ band = transitional ∨ band = unknown ∨ (band = unstable ∧ L > 0.4)).

**No tension/obstacle in v0.1:** Tension and obstacle state are not yet in the equation; they can be added in a later revision when tension layer is in scope.

---

## 7. Status

- **D (Risk analysis):** Delivered §5. Recommendation: definitions now, advisory-only; no wiring until observability stable and policy approved.
- **A (Governance equation):** Delivered §6. GO(L, band, fc, se); compatible with INV_safeguard; advisory use only.
- **B (obstacleScore):** Deferred; can be added in same doc when needed.
- **C (Decision state machine):** Deferred; can be added when control surface is approved.

---

**SIGNED: Architecture (Ethan) | Post v0.1 formal definitions — governance equation, obstacleScore, decision FSM, or risk analysis | 2026-02-18 | governance**
