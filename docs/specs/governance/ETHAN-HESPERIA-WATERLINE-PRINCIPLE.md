Hesperia waterline principle — capacity doctrine (Ethan)

(c) prichindel.com

**Purpose**: Formalize the **WATERLINE PRINCIPLE — HESPERIA CAPACITY DOCTRINE** as a governance layer **above v0.1 observability**. Define when the sphere must **stop reasoning**, how to mark an **underwater region**, and how to cut to an **above‑water decision surface**. Definition only; no traversal/safeguard core change. **Owner**: Ethan. **Date**: 2026-02-18.

---

## 1. Core thesis

- The sphere **must not reason infinitely**. Infinite loopability = semantic drift, even if locally true.
- Depth must be **bounded**; saturation must be treated as **structural overload**.
- HESPERIA must **preserve future reasoning space** — bounded cognition, not omniscience.

---

## 2. Waterline concept

- Loop traversal accumulates **semantic mass**.
- Each loop increases internal density: activation + tension + entropy (and related scores).
- When density crosses a threshold the sphere **sinks**: **sinkage = loss of operational reasoning surface**.
- **Above water** = decision space.
  **Below water** = archival / latent semantic mass (underwater region).

---

## 3. Flood point and thresholds

Define **waterLevel ∈ [0,1]** with qualitative anchors:

- 0.0 → fresh surface state.
- 0.6 → caution threshold.
- 0.7 → hard stop.
- 1.0 → full semantic overload.

Operational gate:

- **Caution** when `waterLevel ≥ 0.60`.
- **Hard stop recommended** when `waterLevel ≥ 0.65` (or 0.70 for stricter cut).
- Beyond hard stop: loop traversal forbidden; governance escalates; decision must be made.

This sits in **Governance → Decision**, **not** in geometry or safeguard core.

---

## 4. Sinkage function — conceptual variables

Water level **increases** with:

- loop count (passes),
- entropy over areas `entropy(A_vec)`,
- tension energy (polarization on bipolar axes),
- contradictionScore,
- saturation,
- **decrease** in loopability.

Water level does **not** depend on truth magnitude alone: true but over‑processed regions still sink.

---

## 5. Underwater region

**Underwater** region = parts of R that are **temporarily suppressed** for decision clarity:

- Areas below activation threshold after cutoff.
- Families below relative dominance.
- Low‑coherence clusters.
- Redundant loops.

Underwater **≠ false**. Underwater = “out of current decision surface”.

---

## 6. Cut mechanism (conceptual)

At flood point (hard stop):

1. **Sort areas** by activation strength `A_vec[a]` descending.
2. Keep the **smallest set S** such that the cumulative activation mass reaches a keep fraction:

   - `Σ_{a∈S} A_vec[a] ≥ M_keep`, e.g. `M_keep = 0.50` (keep top 50% mass).

3. Define:

   - `R_active = R ∩ Areas(S)`
   - `R_submerged = R \ R_active`

4. Remove associated families and sides in submerged areas from **active traversal region**.

Only **R_active** is used for **current decision**; R_submerged remains stored.

---

## 7. Re‑analysis after cut

After truncation:

1. **Recompute on R_active**:
   - `T(R_active)` (e.g. tension),
   - `C(R_active)` (coherence),
   - `X_A` (area‑level metrics),
   - entropy,
   - scaleConsistency,
   - contradictionScore.
2. **Renormalize** `A_vec` over remaining areas:

   - `A'_vec[a] = A_vec[a] / Σ_{i∈S} A_vec[i]` for `a ∈ S`, else 0.

This is a **semantic compression event**: decision surface shrinks but remains coherent.

---

## 8. Machine memory policy

- **Underwater region** is **stored**, not deleted.
- Not used for **current** decision, but remains available for future retrieval (e.g. via embeddings).
- Human analogue: “You forget for now, but memory exists.”

---

## 9. Structural consequences

This doctrine enforces:

- bounded cognition,
- forced convergence,
- decision pressure,
- anti‑rumination constraint,
- finite semantic bandwidth.

It prevents:

- infinite refinement loops,
- perfect but unusable reasoning,
- over‑optimization collapse.

---

## 10. Governance integration

- **Placement**: `Context → Governance (waterline) → Decision`.
- Not geometry; not part of traversal or loop safeguard kernel.
- Waterline is a **cognitive capacity constraint**, not a truth function.

---

## 11. Formal waterLevel equation (v0.1, definition only)

Inputs from **ContextSnapshot** (existing or planned variables):

- `p` — pass index (1..MAX_PASSES).
- `L` — loopability (0..1).
- `H_A` — area entropy `entropy(A_vec)` (≥0).
- `E_t` — tension energy over bipolar axes (≥0).
- `C_sc` — contradictionScore(R) (≥0).
- `Q_e` — evidenceQuality(R) (0..1).
- `C_R` — coherence C(R) (0..1).
- Optional: `Φ` — coveragePhi (0..1).

Normalize each term to [0,1] with **hard caps** (deterministic, no learning):

- `H_cap = ln(12)` (max entropy for 12 areas).
- `Et_cap` — chosen cap for tensionEnergy (start 1.0; tune later).
- `Cs_cap` — chosen cap for contradictionScore (start 1.0; tune later).

Derived normalized variables:

- `h = clamp01(H_A / H_cap)`
- `t = clamp01(E_t / Et_cap)`
- `c = clamp01(C_sc / Cs_cap)`
- `e = 1 - Q_e`  (weak evidence ↑ waterLevel)
- `k = 1 - C_R`  (low coherence ↑ waterLevel)
- `u = clamp01((p - 1) / (MAX_PASSES - 1))` (loop depth pressure)
- Optional coverage term `v` from Φ if used.

Core waterLevel (weighted sum + clamp):

```text
waterLevel = clamp01(
    w_u*u +
    w_h*h +
    w_t*t +
    w_c*c +
    w_e*e +
    w_k*k +
    w_l*(1 - L)
)
```

Recommended starting weights (sum = 1):

- `w_u = 0.15` (depth / passes)
- `w_h = 0.15` (entropy spread)
- `w_t = 0.15` (polarization / tension)
- `w_c = 0.20` (contradiction)
- `w_e = 0.15` (evidence weakness)
- `w_k = 0.10` (fragmentation via low coherence)
- `w_l = 0.10` (non‑productive looping: 1 − L)

**Policy**:

- **Caution**: `waterLevel ≥ 0.60`.
- **Hard stop**: `waterLevel ≥ 0.70` (or ≥ 0.65 per stricter doctrine).

At hard stop:

- freeze traversal (no further loops in this governance step),
- execute deterministic **above‑water cut** (S, R_active, R_submerged),
- proceed to decision on **R_active** only.

All of the above is **governance / decision‑layer math**. Kernel and safeguard remain unchanged until a dedicated implementation phase (Phase D) explicitly wires this doctrine.

---

## 12. Implementation gates (Phase and safety)

- **Phase**: Waterline is **Phase D** material (capacity doctrine). It may be **documented now** but not wired into traversal or safeguard while Hesperia is in infrastructure hardening (direction A).
- **No dynamic control yet**: waterLevel and cut rules are **not** to be used as dynamic modulation of traversal in current phase; they are used only for analysis or offline decision support.
- **Entry point**: When implemented, waterline must run **after ContextSnapshot** and **before Decision**, never mid‑traversal in the kernel.

---

## 13. Loop limit doctrine (logical 3‑fails with capacity)

You asked for **“logical 3 fails, loopable with sinkage and capacity”**. The loop limit doctrine combines:

- existing **loop safeguard** (three consecutive logical failures → STOP), and
- **capacity fail** from waterLevel (sinkage and cut).

### 13.1 Pass bounds (pressure only)

Deterministic pass limits:

- `maxPasses = 100` (absolute upper bound on passes in one decision cycle),
- `softWarning = 60`,
- `hardCapacityStop = 70`.

**But** real stop is **not** based on pass count alone:

- Pass count **only increases pressure** (via `u` in waterLevel).
- **Capacity fail** is triggered by **waterLevel**, not by `p` directly.

### 13.2 Capacity fail rule

Capacity failure condition:

```text
CapacityFail  ⇔  waterLevel ≥ 0.70
```

This may occur:

- even if `p = 20` (few passes but very dense / tense / contradictory), or
- even if `p = 200` (if maxPasses were larger).

Pass count contributes via `u`, but **waterLevel decides** when capacity is exceeded.

### 13.3 Behaviour after capacity fail

On **first** CapacityFail in a decision cycle:

1. **Freeze** current ContextSnapshot.
2. Execute **cut** of underwater areas (50% mass rule from §6):
   - keep minimal S with `Σ_{a∈S} A_vec[a] ≥ M_keep` (M_keep ≈ 0.50),
   - define `R_active`, `R_submerged` and renormalize `A_vec` on S.
3. **Recompute** metrics on `R_active` only (per §7).
4. **Resume traversal** with a reduced pass budget:

   - `reducedMaxPasses = 20` (single post‑cut allowance).

Guarantee:

- Only **one compression event per decision cycle**.

On **second** CapacityFail in the same decision cycle:

```text
Second CapacityFail  ⇒  ForceDecision  (no more loops)
```

No further loops are allowed; system must make a decision on the current `R_active`.

### 13.4 Clean system state machine

At governance/decision layer, per iteration:

```text
Context → Governance → CheckFails:

if StructuralFail → STOP
if EpistemicFail  → STOP
if CapacityFail   → CUT → ResumeOnce
else              → ContinueLoop
```

Where:

- **StructuralFail** = geometry / invariant violation.
- **EpistemicFail** = logic-level failure (e.g. UNSAT, contradiction) per safeguard policy.
- **CapacityFail** = `waterLevel ≥ 0.70` (plus “only once per decision cycle” rule).

This produces a loop that is:

- **deterministic** (no randomness, fixed thresholds),
- **finite** (bounded passes, single compression, forced decision),
- **controlled** (no infinite rumination, no perfection‑seeking collapse).

---

**SIGNED: Architecture (Ethan) | Hesperia waterline principle — capacity doctrine, waterLevel equation, and loop limit doctrine (definition only) | 2026-02-18 | governance**
