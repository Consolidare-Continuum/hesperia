---
spec_version: "1.0"
system_version: "0.5.0"
status: canonical
id: HES-SPEC-CAL-HSPR
---

# HSPR / HCI — canonical scalars

This spec defines **two** bounded scalars used in Engine Dynamics v0.5. Names are **not** interchangeable.

## 1. HSPR_sys — multiscale system KPI

**Purpose:** Single global score for corpus / run comparison (dashboard, drift).  
**Code:** `hesperia.engine.hspr_index.compute_hspr_index`  
**Distinct from:** field-level HSPR on **F** in `hesperia.engine.calibration.hspr_field` (family observables Σ̂, Ê, …).

### Definition

\[
\text{HSPR}_{sys} = \tilde{a}_1 \tilde{E}_{act} + \tilde{a}_2 \tilde{v} + \tilde{a}_3 \tilde{P} + \tilde{a}_4 \tilde{D}
\]

Hatted terms are components normalized to **[0,1]**:

| Symbol | Meaning |
|--------|---------|
| \(E_{act}\) | `activation_energy` = \(\sum_h A_h^2\) |
| \(v\) | `propagation_strength` — mean \(\|\Delta A\|\) per step |
| \(P\) | `contradiction_pressure` |
| \(D\) | `narrative_density` |

**\(\tilde{a}_i\)** default positive; after normalization \(\sum_i \tilde{a}_i = 1\) so **HSPR_sys ∈ [0,1]**.

### Input contract

`field_state` dict with keys: `activation_energy`, `propagation_strength`, `contradiction_pressure`, `narrative_density` (and optional `scales`).

---

## 2. HCI — HSPR Calibration Index (parameter quality)

**Purpose:** Canonical **ranking** score for semantic-field **parameter sets** (grid search).  
**Code:** `hesperia.extensions.dynamics.calibration` · **Runner:** `python3 -m runtime.semantic_field.run_field_calibration`

### Definition

\[
\mathrm{HCI}
=
w_\Sigma \Sigma
+
w_Q \hat Q
+
w_E \hat E
+
w_K \hat K
+
w_D \hat D
+
w_R \hat R
\]

with each normalized term in \([0,1]\), weights **sum to 1** (implementation renormalizes).

| Term | Formula (binding) |
|------|-------------------|
| \(\Sigma\) | \(1 / (1 + \|\mathbf{F}_{t+1}-\mathbf{F}_t\|_2)\) clipped to \([0,1]\) |
| \(Q\) | \(\mathbf{S}^T \mathbf{F}\); \(\hat Q = Q/(Q+\kappa_Q)\) |
| \(\hat E\) | \(1/(1+\max(E,0))\) |
| \(K\) | \(\mathbf{F}^T C \mathbf{F}\); \(\hat K = 1/(1+K)\) |
| \(D\) | \(\mathbf{F}^T L_F \mathbf{F}\); \(\hat D = 1/(1+D)\) |
| \(R_{load}\) | \(\mathbf{F}^T R_F \mathbf{F}\); \(\hat R = 1/(1+R_{load})\) |

### Default weights

| stability | source_alignment | energy | contradiction | diffusion | resistance |
|-----------|------------------|--------|-----------------|-----------|------------|
| 0.25 | 0.25 | 0.15 | 0.15 | 0.10 | 0.10 |

### Interpretation bands

| HCI | Band |
|-----|------|
| 0.85–1.00 | Very strong |
| 0.70–0.85 | Usable / strong |
| 0.50–0.70 | Weak / unstable |
| &lt; 0.50 | Poor |

**Non-claim:** HCI does not prove external truth; it scores **internal dynamical quality** under fixed topology and sources.

---

## 3. Related

- Product observables feeding **HSPR_sys**: [../core/product_observables.md](../core/product_observables.md)  
- Field dynamics: [../dynamics/semantic_field_dynamics.md](../dynamics/semantic_field_dynamics.md)  
- Calibration law: [calibration_system.md](calibration_system.md)  
