---
spec_version: "1.0"
system_version: "0.5.0"
status: canonical
id: HES-SPEC-CORE-HEX-MICRO
---


# Hex microphysics — canonical specification

**Engine Dynamics v0.5 index (non-binding):** [docs/HESPERIA_v0_5_ENGINE_DYNAMICS.md](../../docs/HESPERIA_v0_5_ENGINE_DYNAMICS.md).  
**Hierarchy:** Concept → **Hex** → Family → Area (see [system_architecture.md](system_architecture.md)).  
**Code:** `hesperia.engine.hex_dynamics`, `hesperia.engine.hex_matrix_builders`, `hesperia.engine.hex_outputs`.  
**Related:** [semantic_field_dynamics.md](../dynamics/semantic_field_dynamics.md) · `docs/TOPOLOGY_INVARIANTS.md` · `core/topology/invariant_catalog.py`.

### Closure (what this task fixes)

| Risk (before) | Seal (after) |
|---------------|--------------|
| Hex outputs optional / non-structural | Hex microphysics is **normative** for multiscale physics; family mesostate **F** is **defined** as **F = P_HF H** under Option A. |
| Family vs hex dynamics drift | Single substrate **H**; **F** is aggregation, not an independent competing state. |
| Product cannot claim full multiscale semantics | Observable stack (§10) + **G_F** exposes drift if a parallel **F** disagrees with **P_HF H**. |

**Official stack:** Concept → **Hex** ( **S_H = P_CH A** ) → evolve **H** → **F = P_HF H** → Area. Family remains the **main public field level**; hex is the **microphysical** explanation of local structure.

---

## 1. Role of the hex layer

| Scale | Object | Role |
|-------|--------|------|
| Concept | **A** ∈ ℝ^Nc | Evidence from Dict-A (and upstream). |
| **Hex** | **H** ∈ ℝ^Nh | **Microphysical substrate** — local semantic cells. |
| Family | **F** ∈ ℝ^Nf | **Mesoscopic aggregate** of hexes (Nf = 288). |
| Area | **A_area** | Macro projection of **F** (12 areas). |

**Option A (canonical, locked first):** Hex evolves; **F = P_HF H** (family field is derived).  

**Option B (reserved, coupled):** Hex and family co-evolve with cross-coupling:

d**H**/dt = −α_H **L_H** **H** − β_H **R_H** **H** − γ_H (**H** ⊙ (**C_H** **H**)) + δ_H **S_H** + μ_H **P_FH** **F**  

d**F**/dt = −α_F **L_F** **F** − β_F **R_F** **F** − γ_F (**F** ⊙ (**C_F** **F**)) + δ_F **S_F** + μ_F **P_HF** **H**

**P_FH** maps family → hex (e.g. uniform split per family); **P_HF** maps hex → family (aggregation). Heavier calibration; not implemented in baseline engine.

---

## 2. Geometry constants and Nh

- **Nf** = 288 families  
- **Hexes per family** = 250  
- **Nh (full canon)** = Nf × 250 = **72 000** — total hex cells in the closed topology (linear index u = 0…Nh−1).

**Active hex cells:** In sparse or capped execution, the **active** set is the subset of indices where **H** is evolved (e.g. families with support). The same symbols **L_H**, **W_H** apply on the **induced subgraph** on active nodes; full-grid and active-subgrid modes are calibration choices, not different physics.

**Public operational subset:** 240 × 250 = **60 000** hexes for public-facing outputs; reserved families remain in the full **Nf×250** grid for internal consistency where needed.

---

## 3. Hex state

**H** ∈ ℝ^Nh, **H_u** ≥ 0 — activation of hex u.

**Hex → family incidence** **P_HF** ∈ {0,1}^{Nf × Nh}:  
(P_HF)_{m,u} = 1 iff hex u belongs to family m (exactly one 1 per column).

**Family aggregate:**

**F** = **P_HF H**  (F_m = Σ_{u ∈ family m} H_u).

---

## 4. Concept → hex injection (normative)

Concept evidence **must not** be the sole input to a freestanding family field if the deployment claims **structural** multiscale physics. **Normative path:** **S_H** = **P_CH A** with **P_CH** ∈ ℝ^{Nh × Nc}.

**Legacy / non-structural path:** injecting **S** = **P_CF A** only at family level skips local hex structure; acceptable only when explicitly documented as **legacy** or fast proxy.

**Production (v0.5+):** governed sparse **P_CH** (`assets/matrices/pch/P_CH_v1.npz`, manifest `P_CH_manifest.json`), loaded via `hesperia.engine.pch_loader.load_pch`, applied with `hesperia.engine.hex_matrix_builders.apply_pch_to_concept_activation` and `hex_dynamics.hex_source_from_concept_family_injection` / `run_option_a_hex_primary`. Columns are L1-normalized; uniform per-family spread is **forbidden** in production (dev-only behind `HESPERIA_PCH_UNIFORM_INJECTION_DEV=1`: `concept_family_weights_to_hex_source`, `family_source_to_hex_uniform`).

---

## 5. Hex adjacency and Laplacian

**W_H** ∈ {0,1}^{Nh × Nh} — undirected adjacency on hex cells.

**D_H** = diag(Σ_j W_H(i,j)), **L_H** = **D_H** − **W_H**.

**Baseline implementation:** **intra-family ring** — within each family, hex indices 0…249 form a cycle (neighbors i±1 mod 250). No cross-family hex edges in v1 (blocks are decoupled for diffusion); cross-family coupling is carried by **family-level** dynamics after aggregation. Full icosahedral / lattice W_H may extend this spec without changing symbols.

---

## 6. Hex contradiction matrix

**C_H** ∈ ℝ^{Nh × Nh}, non-negative, zero diagonal (after lifting).

**Minimal rule:**

(C_H)_{u,v} = C_F(φ(u), φ(v))

where φ(u) is the family of hex u and **C_F** is the family contradiction matrix (Nf × Nf).

**Implication:** For family sums **S_m** = Σ_{u∈m} H_u,

**(C_H H)_u** = Σ_n C_F[φ(u), n] · S_n = (**C_F S**)_m for all u ∈ family m.

Nonlinear term: **H** ⊙ (**C_H H**) is well-defined without forming dense **C_H**.

---

## 7. Hex resistance

**R_H** = diag(r_u), r_u ≥ 0 — local inertia (sparse support, isolation, confidence, governance zones). Default: uniform scalar per hex or per family.

---

## 7b. Local discrete microphysics (per-cell update)

For hex **h** with neighbors **N(h)** and scalars **R_h**, **C_h** (contradiction pressure at **h**):

**A_h(t+1) = A_h(t) + α Σ_{n∈N(h)} (A_n − A_h) − β R_h A_h − γ C_h**

| Term | Role |
|------|------|
| Neighbor sum | Diffusion toward local equilibrium |
| −β R A | Resistance damping |
| −γ C | Contradiction suppression |

Implemented as **`step_hex_local_microphysics`** on the **(Nf × Nh)** grid with ring **N(h)** within each family; **C_h** lifted from **(C_F S)_m** for all hexes in family **m**. See `hesperia.engine.hex_dynamics`.

---

## 8. Canonical hex field equation (continuous / full field)

d**H**/dt = −α_H **L_H** **H** − β_H **R_H** **H** − γ_H (**H** ⊙ (**C_H** **H**)) + δ_H **S_H**

| Term | Meaning |
|------|---------|
| 1 | Diffusion along W_H |
| 2 | Local resistance |
| 3 | Contradiction pressure (family-lifted) |
| 4 | Source injection |

Coefficients α_H, β_H, γ_H, δ_H ≥ 0 (calibration).

---

## 9. Family field from hex — official bridge (Option A)

**F** = **P_HF** **H** is the **only** canonical definition of the family mesostate after hex microphysics. This **seals** Family ↔ Hex: **F** is not a separate floating object; it is the aggregate of **H**.

Downstream family-field dynamics (e.g. **L_F**, **C_F** on **F**) may run **after** this aggregation in hybrid pipelines; any **F** not equal to **P_HF H** must be labeled **non-canonical** or triggers **G_F** drift (§10).

---

## 10. Hex observables

| Symbol | Name | Formula |
|--------|------|---------|
| E_H | Hex energy | ½ **H**ᵀ **L_H** **H** |
| K_H | Hex contradiction load | **H**ᵀ **C_H** **H** = **S**ᵀ **C_F** **S**, **S** = **P_HF** **H** |
| R_H,load | Hex resistance load | **H**ᵀ **R_H** **H** |
| G_H | Hex gradient intensity | ‖**L_H** **H**‖₂ |
| Comp | Cluster compactness | (Σ_i \|C_i\|²) / (Σ_i \|C_i\|)² on activated components of W_H |
| G_F | Family grounding score | 1 − ‖**F** − **P_HF** **H**‖ / (‖**F**‖ + ε) → 1 when **F** matches aggregate |

---

## 11. Multiscale consistency

- **G_F ≈ 1** when the declared family vector equals the hex aggregate.  
- Drift indicates optional **Option B** coupling or calibration mismatch.

---

## 12. Determinism

Fixed **P_CH**, **W_H**, **C_F**, **R_H**, coefficients, and dt yield deterministic **H**(t) and derived **F**, observables, and **G_F** for given **A**.
