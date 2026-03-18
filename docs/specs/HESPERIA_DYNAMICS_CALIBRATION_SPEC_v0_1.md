<!--
HESPERIA — Reference Architecture Definition (RAD)
Copyright © 2026 igareosh.com — Platonov Igor (aka @igareosh). All rights reserved.
Restricted Research Disclosure License. Inspection and reference only.
See LEGAL_NOTICE.md for full terms.
-->

# HESPERIA Dynamics Calibration Spec v0.1

**Status:** design doctrine + implementation blueprint for calibrating **dynamic** Hesperia (L0–L10, H0–H9). Companion: [ETHAN_SEMANTIC_FIELD_DYNAMICS_SPEC.md](ETHAN_SEMANTIC_FIELD_DYNAMICS_SPEC.md).

**Core doctrine (one sentence):**  
**Calibration by design** = bounded parameter architecture + layered objective functions + hard structural constraints + deterministic automated search + **governed** profile freezing — *automation proposes; governance accepts.*

---

## 1. Parameter classes

### 1.1 What “calibration” means here

Choosing parameter values so the system stays **structurally valid, stable, interpretable, and empirically useful** across known corpora.

**Not:** random hyperparameter search, opaque ML fitting, endless manual tweaking, “looks good on this sample.”

Calibration must be: **bounded · layered · deterministic · test-driven · automatable** — formula by formula, hard structural limits first.

### 1.2 Class A — Fixed structural constants (never tuned)

| Kind | Examples |
|------|----------|
| Topology | 12 areas, icosahedral adjacency, operational family/hex counts per [TOPOLOGY_INVARIANTS.md](../TOPOLOGY_INVARIANTS.md) |
| Membership | Family→area, hex→family, allowed propagation paths |
| Boundaries | Reserved vs public indices, projection rules |

These are **spec constants**, not calibration targets.

### 1.3 Class B — Controlled dynamic parameters (calibrated)

| Symbol family | Role |
|---------------|------|
| \(\lambda_c,\lambda_h,\lambda_f,\lambda_a\) | Decay rates |
| \(\alpha_{\mathrm{in}},\alpha_g,\theta_c,\theta_d,\beta_x,\gamma_f,\gamma_q\) | Gains |
| \(\alpha_p,\theta_p,\beta_{pf},\gamma_p\) | Contradiction penalties |
| \(\mu_h,\mu_f,\mu_a\) | Pressure dissipation |
| \(\delta_h,\delta_f,\delta_a\) | Pressure accumulation |
| \(\eta_h,\eta_a\) | Pressure spillover |
| \(r_0,r_1,r_2\) | Resistance coefficients |
| Trust / stability / oscillation | Thresholds for L9 |

### 1.4 Class C — Derived values (never tuned as knobs)

Area velocity, graph tension \(\Xi\), contradiction pressure fields, cluster gravity, stability index, narrative penetration — **outputs only**. Tuning outputs directly makes the math **fake**.

---

## 2. Allowed ranges (design before search)

Every Class B parameter gets a **justified interval** — search only inside lawful space.

| Group | Intent | Example bounds |
|-------|--------|----------------|
| Decay | Prevent dead or frozen field | \(\lambda_c \in [0.05,0.30]\), \(\lambda_f \in [0.03,0.20]\), \(\lambda_a \in [0.01,0.15]\) |
| Propagation gains | No diffusion explosion | e.g. \(\gamma_q \in [0, 0.5]\) |
| Contradiction penalties | Suppress, not annihilate | e.g. \(\gamma_p \in [0, 0.6]\) |
| Stability thresholds | From **test distributions**, not whim | |

Ranges are **versioned** with the parameter registry.

---

## 3. Constraint registry (hard checks)

**Before** any score optimization, candidates must pass:

| Constraint | Check |
|------------|--------|
| Bounds | \(0 \leq c_i,x_h,f_f,a_a \leq 1\); \(p_h,p_f,p_a \geq 0\) |
| No explosion | \(\max_t \max_a a_a(t) \leq 1\) (and analogs for other layers) |
| Oscillation cap | \(\mathrm{Osc}(t) < \mathrm{Osc}_{\max}\) |
| Zero-input decay | If \(U(t)=0\) over long window, \(p_a\) (and peers) **decay** — no runaway contradiction without input |
| Topology invariants | Unchanged adjacency / membership semantics |
| Deterministic replay | Same seed + params → **identical state hash** |

Failures → **discard immediately** (constraint-first calibration).

---

## 4. Objective registry

### 4.1 Objective groups

| Group | Targets |
|-------|---------|
| **A — Structural validity** | Bounded states, no invalid transitions, invariants, replay match |
| **B — Dynamical behavior** | Propagation under continuity, damping when input stops, contradiction growth with conflict, stabilization with resolution, no explosive oscillation under normal inputs |
| **C — Interpretability** | Dominant area not flipping without cause; small input → bounded macro change; pressure explainable by contradiction density; outputs aligned with evidence |
| **D — Task usefulness** | On benchmark corpora: narrative drift detection, contradiction hotspots, propagation path realism, temporal clustering, change-point detection — **specific** metrics, not vague “accuracy” |

### 4.2 Composite score (example)

\[
J(\theta) = w_1 S_{\mathrm{stab}} + w_2 S_{\mathrm{interp}} + w_3 S_{\mathrm{drift}} + w_4 S_{\mathrm{contradict}} + w_5 S_{\mathrm{det}}
- w_6 P_{\mathrm{explode}} - w_7 P_{\mathrm{osc}} - w_8 P_{\mathrm{noise}}
\]

\(\theta\) = Class B vector. Weights \(w_*\) are **governance-chosen**, not silently learned.

### 4.3 Example scorecard (reporting)

```
Structural validity:     1.00
Determinism:             1.00
Propagation realism:     0.82
Contradiction realism:   0.79
Resolution realism:      0.74
Noise robustness:        0.88
Stability:               0.91
Interpretability:        0.86
Composite:               0.85
```

---

## 5. Scenario suite (datasets by design)

| Class | Purpose | Examples |
|-------|---------|----------|
| **A — Synthetic control** | Known ground truth | Single-theme propagation; injected contradiction; resolution injection; gradual drift; regime shift |
| **B — Toy topology** | Isolate math | One area; two adjacent areas; cross-family contradiction; bridge concept |
| **C — Gold temporal** | Real relevance | Policy revisions, media windows, debates, incident logs (expert labels where available) |
| **D — Adversarial** | Fragility | Marker spam, high contradiction noise, alternating themes, sparse evidence, false bridge |

Without (D), calibration **lies**.

---

## 6. Automated search procedure

### 6.1 Architecture pipeline

```text
Parameter registry
  → scenario generator / dataset loader
  → simulation runner (deterministic)
  → metric evaluator
  → constraint validator
  → search / selection engine
  → report generator
  → approved parameter profile
```

Each run records: candidate \(\theta\), constraint pass/fail, objective scores, sensitivity summary, vs baseline, **reproducible hash**.

### 6.2 Search phases (staged)

| Phase | Method | Use |
|-------|--------|-----|
| 1 | Grid or Latin hypercube (low-D) | Concept layer; area-only dynamics |
| 2 | Constrained random / evolutionary | Medium interaction |
| 3 | Local refinement | Nelder–Mead, **coordinate descent**, bounded hill climb |

**Recommended for Hesperia doctrine:** **hierarchical constrained coordinate calibration** — calibrate one layer, **freeze**, calibrate next, recheck upstream, freeze release profile. Not full joint black-box first.

### 6.3 Sequential calibration order (layers)

| Stage | Layer | Calibrate | Goal |
|-------|-------|-----------|------|
| 1 | Concept | \(\alpha_{\mathrm{in}},\alpha_g,\lambda_c,\alpha_p\) | Stable activation; no runaway; not dead |
| 2 | Hex | \(\theta_c,\theta_d,\lambda_h,\theta_p\) | Local spread; hotspots; bounded diffusion |
| 3 | Family | \(\beta_x,\beta_{\mathrm{intra}},\lambda_f,\beta_{pf}\) | Readable patterns; not noisy/flat |
| 4 | Area | \(\gamma_f,\gamma_q,\lambda_a,\gamma_p\) | Clear stable macro field |
| 5 | Trust/guards | Trust, stability, oscillation, unsafe cutoffs | Correct governance response |

**Do not** calibrate the whole stack jointly first — fast path to garbage.

### 6.4 Sensitivity (automatic)

Per parameter \(\theta_k\): e.g. \(S_k \approx \frac{J(\theta_k+\varepsilon)-J(\theta_k-\varepsilon)}{2\varepsilon}\). Classify: low / medium / high / **dangerous**. High-sensitivity → tighter ranges, stricter governance.

---

## 7. Release profile governance

### 7.1 Named profiles (not one “best”)

Examples: `profile_static_safe`, `profile_temporal_conservative`, `profile_temporal_balanced`, `profile_temporal_research`.

Each profile ships: parameter set, calibration evidence, pass/fail matrix, **intended use scope**, version id, **checksum**.

### 7.2 Promotion rules

Promote only if: score improves vs baseline, **all** constraints pass, replay deterministic, sensitivity acceptable. **Human/governance sign-off** on promotion.

### 7.3 Never automate blindly

Automation **must not** freely modify: topology, ontology mappings, family membership, contradiction **definitions**, public/reserved boundaries, trust **semantics**, evidence rules. Those are **governance artifacts**. Automation optimizes **numbers** inside registry ranges only.

---

## 8. Calibration-by-design architecture (governed artifact)

```text
Spec constants (Class A)
  ↓
Parameter registry (Class B + ranges)
  ↓
Calibration scenarios
  ↓
Objective tests + constraints
  ↓
Search (staged)
  ↓
Approved parameter set
  ↓
Frozen release profile
```

---

## 9. Minimal engineering package (concrete paths)

| Artifact | Suggested path |
|----------|----------------|
| Parameter registry | `assets/calibration/dynamics_parameter_registry.yaml` (or `docs/specs/calibration/…` until implemented) |
| Scenarios | `calibration_scenarios.yaml` |
| Constraints | `calibration_constraints.yaml` |
| Objectives | `calibration_objectives.yaml` |
| Approved profiles | `approved_profiles/*.yaml` |
| Reports | `reports/calibration/` |

| Module | Role |
|--------|------|
| `simulate_dynamics.py` | Deterministic roll-forward |
| `evaluate_dynamics.py` | Metrics + constraints |
| `search_parameters.py` | Staged search |
| `sensitivity_analysis.py` | Finite-diff sensitivity |
| `freeze_profile.py` | Checksum + manifest |

**Outputs:** profile YAML/JSON, scorecard, pass/fail matrix, parameter deltas, deterministic hash.

---

## 10. Hard truth

Full auto-calibration can produce mathematically “good” but **semantically ugly** parameter sets. **Rule:** automation proposes; **governance accepts**.

**Final doctrine:** Calibrate **upstream → downstream**, one layer at a time; automation is a **disciplined search instrument**, not a substitute for system understanding.

---

*HESPERIA Dynamics Calibration Spec v0.1 — Ethan / governance alignment. Revise when `dynamics_parameter_registry.yaml` is seeded.*
