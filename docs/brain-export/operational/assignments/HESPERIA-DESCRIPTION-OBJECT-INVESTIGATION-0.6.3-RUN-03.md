# Hesperia Description Object Investigation — Run 03 of 05

**Title:** Sealed multiscale stack — concept → hex → microphysics → family → area → signals → HSPR  
**Version:** Hesperia 0.6.3 (description object investigation)  
**Product SHA:** `e9eaa07`  
**Index:** [HESPERIA-DESCRIPTION-OBJECT-INVESTIGATION-0.6.3-INDEX.md](HESPERIA-DESCRIPTION-OBJECT-INVESTIGATION-0.6.3-INDEX.md) · **Prior:** [RUN-01](HESPERIA-DESCRIPTION-OBJECT-INVESTIGATION-0.6.3-RUN-01.md), [RUN-02](HESPERIA-DESCRIPTION-OBJECT-INVESTIGATION-0.6.3-RUN-02.md)

**Scope note:** Study is **not capped at 2000 lines** — Run 03 is expanded for full formula + numeric trace coverage.

---

## Abstract

Run 03 documents **Spine B** canonical shipping math: `run_sealed_multiscale_stack` in `hesperia/engine/sealed_multiscale_stack.py`. The pipeline lifts lexical concept hits through sparse **P_CH** into a hex tensor **A_hex**, applies one **energy-controlled local microphysics step**, aggregates to **288-family** vector **F** and **12-area** vector, computes **hex-causal product signals** (contradiction, propagation, narrative density), and derives **HSPR_sys**. Family and area vectors are **projection outputs only** — signal formulas read **A0/A1** exclusively (Engine Dynamics v0.5 seal).

---

## 1. Orchestrator — `run_sealed_multiscale_stack`

**File:** `hesperia/engine/sealed_multiscale_stack.py`  
**Entry:** `build_structural_internal_from_multiscale` → `run_sealed_multiscale_stack(text, assets_root, …)`  
**Constants:** `NUM_FAMILIES=288`, `NUM_AREAS=12`, `FAM_PER_AREA=24`, `HEXES_PER_FAMILY_CANON=250` (from `core/topology/invariant_catalog.py`).

### 1.1 Ordered transformation stages

| Step | Block / function | Input state | Output state |
|------|------------------|-------------|--------------|
| S0 | `markers_to_concept_activation` | raw `text`, `assets_root` | `a_concept_counts[288]`, trace metadata |
| S1 | prior fallback | `h_raw.sum()` | uniform `h = 1/288` if zero mass |
| S2 | `load_pch` + `apply_pch_to_concept_activation` | `a_concept`, sparse **P_CH** | **A0** `(288, 250)` |
| S3 | `build_uniform_hex_resistance` + adaptive term | `A0` | **R** `(288, 250)` |
| S4 | `load_production_matrices` | manifest | **C_F** `(288, 288)` |
| S5 | `build_ring_laplacian(250)` | — | **L_ring** `(250, 250)` |
| S6 | `step_hex_local_microphysics` | A0, R, C_F, S_H=A0 | **A1** `(288, 250)` |
| S7 | `compute_family_activation` | A1, overrides | **F** `(288,)` |
| S8 | `_area_from_family` | F | **area** `(12,)` |
| S9 | `compute_product_signals(A0, A1, C_F)` | hex pair | signal dict |
| S10 | `field_state_from_hex_stack` + `compute_hspr_index` | A1, signals | **hspr_index** |
| S11 | optional contradiction / DLCR / TRIZ sidecars | env flags | extra keys |

**Iteration count (default):** one local hex step (`apply_local_step=True`); multi-step Euler path exists in `hex_dynamics.run_hex_microphysics` for dev/E2E, not default sealed stack.

### 1.2 Return dict (selected keys → downstream)

| Key | Shape / type | Consumer |
|-----|--------------|----------|
| `hex_activation_map` | `{shape, sample_ring_slice, total_mass}` | `multiscale_product_bridge`, public projection |
| `family_activation_vector` | list len 288 | macro domain, L1 fallback |
| `area_activation_vector` | list len 12 | trust tier, dominant area |
| `product_signals` | dict scalars | diagnostics, HSPR components |
| `hspr_index` | float [0,1] | L7 trust, 0.6.3 envelope |
| `contradiction_pressure`, `propagation_strength`, … | top-level mirrors | IRC / operator JSON |

---

## 2. Stage S0 — concept activation

**File:** `hesperia/extensions/dynamics/e2e_bridge.py` — `markers_to_concept_activation`

**Purpose:** Canonical **markers → concepts → A_concept** (288-d hit counts aligned with concept registry).

**Block flow:**

```python
tokens = tokenize(normalize(text))
matched, metrics = attribute(tokens, dict_a, dict_b, exclude_landing_sources=...)
hits = [0] * nc   # nc = n_concept_canon() == 288
for ci, _alt in matched:
    hits[ci] += 1
```

**Outputs used by sealed stack:**

| Field | Role |
|-------|------|
| `a_concept_counts` | `hits` list → numpy `h_raw` |
| `marker_concept_trace` | interpretability (cap 64 in stack output) |
| `registry_version`, `n_concept` | provenance in `concept_layer` |

**Env:** `HESPERIA_CONCEPT_EVIDENCE_GUARD=strict` excludes Dict A-only landings without Dict B fallback.

**Fallback (S1):** if `marker_concept_mass <= 0`:

```python
h = np.ones(NUM_FAMILIES) / NUM_FAMILIES  # uniform prior
uniform_concept_prior_fallback_used = True
```

Ensures hex layer never receives empty injection in production — diffuse prior preserves microphysics mass (see energy line-search mass floor in §4).

---

## 3. Stage S2 — P_CH projection (concept → hex)

**Files:** `hesperia/engine/pch_loader.py`, `hesperia/engine/hex_matrix_builders.py`

### 3.1 Load P_CH

`load_pch()` reads `assets/matrices/pch/P_CH_v1.npz` + manifest; validates column normalization, VERSION.yaml binding (`HESPERIA_PCH_DIR` override allowed).

### 3.2 Apply

```python
flat = P_CH @ a_concept   # sparse (72000 × 288) @ (288,)
A0 = flat.reshape(n_families, n_hex_per_family)  # (288, 250)
```

**Production rule:** uniform family→hex spreading is **forbidden** unless `HESPERIA_PCH_UNIFORM_INJECTION_DEV=1` (tests only).

**Interpretation:** Each concept index injects mass into a **sparse subset** of hex cells per governed **P_CH** columns — not a dense 72k×288 weight matrix shipped in code.

---

## 4. Stage S3–S6 — resistance, coupling, local step

### 4.1 Resistance field R

```python
R = build_uniform_hex_resistance(288, 250, 0.35) + 0.15 / (A0 + 0.08)
```

Per-cell: base 0.35 plus **activation-dependent** damping — higher A0 → lower extra resistance term.

### 4.2 Family coupling C_F

From `load_production_matrices()` → `assets/matrices/production/` (`L_F`, `C_F`, `R_F` bundles). **C_F** used in:

- local step contradiction pressure per family row
- `contradiction_pressure_hex` Gram lift

### 4.3 Ring Laplacian (within each family row)

`build_ring_laplacian(n_hex=250)` — cycle graph:

\[
L = D - W,\quad W_{i,(i\pm 1)\bmod n} = 1
\]

Used in **energy** bookkeeping, not directly in the §7b discrete update (which uses explicit neighbor sum).

### 4.4 Local microphysics step

**File:** `hesperia/engine/hex_dynamics.py`

**Default coefficients** (`LocalHexMicrophysicsParams`):

| Param | Default | Role |
|-------|---------|------|
| α (`alpha`) | 0.08 | ring diffusion strength |
| β (`beta`) | 0.05 | resistance damping |
| γ (`gamma`) | 0.06 | family coupling pressure |

**Raw update** (`_step_hex_local_microphysics_raw`) for each family row \(m\), hex slot \(k\):

Let \(A_{m,k}\) be activation, \(R_{m,k}\) resistance, \(S_m = \sum_k A_{m,k}\), \((C_F @ S)_m\) family pressure.

Ring neighbors: \(A_{m,k-1}, A_{m,k+1}\) (periodic within row).

Discrete Laplacian-style term: \(\text{lap} = A_{m,k-1} + A_{m,k+1} - 2A_{m,k}\)

\[
\Delta A_{m,k} = \alpha \cdot \text{lap} - \beta R_{m,k} A_{m,k} - \gamma (C_F @ S)_m
\]
\[
A'_{m,k} = A_{m,k} + \Delta A_{m,k}
\]

**Implementation note:** coupling term uses **same** \((C_F @ S)_m\) for all \(k\) in family row \(m\) (family-level pressure on each hex in row).

### 4.5 Energy-controlled acceptance

**File:** `hesperia/engine/energy.py`

Hex energy functional:

\[
E(H) = \sum_m h_m^\top L_{\text{ring}} h_m + \lambda\, S^\top C_F S - \langle S_H, H\rangle
\]

where \(S_m = \sum_k H_{m,k}\), \(\lambda =\) `lam_contra` (default 1.0), \(S_H = A0\) reference source in sealed stack.

**Line search:** `EnergyControlParams(mode=soft, epsilon_energy_soft=1e-4)` tries \(\eta \in \{1, 0.5, 0.25, …\}\):

\[
A_{\text{trial}} = \max(0,\; A + \eta (A_{\text{raw}} - A))
\]

Accept if \(E(A_{\text{trial}}) \le E(A) + \epsilon_{\text{soft}}\). Reject trials that annihilate mass below `min_mass_floor`.

**Trace:** `hex_energy_trace = [e0, e1]` before/after step stored in output.

### 4.6 Upstream fallback

If `sum(A1) <= 0` but `sum(A0) > 0`: `A1 = max(A0, 0)`; flag `hex_upstream_fallback_used`.

---

## 5. Stage S7–S8 — family and area aggregation

### 5.1 Family activation

**File:** `hesperia/engine/hex_family_bridge.py` — `compute_family_activation`

**Default (singleton) aggregation:**

\[
F_j = \sum_{h \in \text{hexes of family } j} A_{1,j,h}
\]

Flat index \(u = j \cdot n_h + h_\text{local}\); default assigns all mass in column to owning family \(j = u // n_h\).

**Optional overrides:** `data/topology/hex_family_weights.json` — sparse exemplar hex ids (`A3_F12_H05`) → split weights across families (normalized per hex).

### 5.2 Area aggregation

**File:** `sealed_multiscale_stack._area_from_family`

\[
A_{\text{area}[a]} = \sum_{j = 24a}^{24a+23} F_j
\]

12 areas × 24 families each = 288 total.

**Purpose:** macro domain vector for public payload — **not** an input to product signal formulas.

---

## 6. Stage S9 — product signals (hex-causal)

**File:** `hesperia/engine/product_signals.py`

**Invariant:** all KPIs from **A_hex** tensors only; **F** and area vectors must not enter these formulas (v0.5 seal).

### 6.1 Narrative hotspot mean (on A0)

For each cell \((m,k)\), ring neighbors sum \( \text{nbr} = A_{m,k-1} + A_{m,k+1}\):

\[
\text{hotspot}_{m,k} = A_{m,k} + \lambda_{\text{hot}} \cdot \text{nbr},\quad \lambda_{\text{hot}} = 0.45
\]

Return **mean** over all \(288 \times 250\) cells.

### 6.2 Propagation strength

\[
v = \frac{\text{mean}(|A_1 - A_0|)}{\Delta t},\quad \Delta t = 1.0
\]

Measures how much the local step **moved** mass across hex grid.

### 6.3 Narrative density (on A1)

\[
\rho = \frac{\sum A_1}{|\{(m,k): A_{1,m,k} > \theta\}|},\quad \theta = 10^{-9}
\]

### 6.4 Contradiction pressure (Gram lift)

\[
G = A_1 A_1^\top \quad (288 \times 288 \text{ from row dots})
\]
\[
P = \sum_{i,j} C_F[i,j] \cdot G[i,j]
\]

Elementwise multiply **C_F** with Gram matrix, sum all entries — quadratic coupling on hex rows without pre-aggregating to F.

### 6.5 Spatial entropy

On flattened mass \(p_u = A_{1,\text{flat},u} / \sum A_1\):

\[
H = -\sum_u p_u \log p_u,\quad \text{normalized by } \log(n_u)
\]

### 6.6 Innovation potential

\[
\text{contradiction\_density} = \frac{P}{\max(\|A_1\|_1^2, \epsilon)}
\]
\[
\text{innovation} = \clip(\text{contradiction\_density} \times H,\ 0,\ 100)
\]

### 6.7 `compute_product_signals` bundle

Returns dict:

```python
{
    "narrative_hotspot_mean": ...,
    "contradiction_pressure": P,
    "propagation_strength": v,
    "narrative_density": ρ,
    "innovation_potential": ...,
    "spatial_entropy_hex": H,
    "novelty_index": H,  # alias
}
```

**Optional:** `try_triz_contradiction_pressure(text)` when `use_triz_contradiction=True` (dev extension path).

---

## 7. Stage S10 — HSPR system index

**File:** `hesperia/engine/hspr_index.py`

### 7.1 Field state

```python
activation_energy = sum(A_1 ** 2)   # Frobenius-style Σ A_h²
propagation_strength = sig["propagation_strength"]
contradiction_pressure = sig["contradiction_pressure"]
narrative_density = sig["narrative_density"]
```

### 7.2 Hat transform

For raw scalar \(x\) and scale \(s\):

\[
\hat{x} = \frac{x}{x + s},\quad \text{clipped to } [0,1]
\]

Default scales: activation 500, propagation 0.05, contradiction 5.0, narrative density 0.02.

### 7.3 HSPR_sys

Weights \((a_1, a_2, a_3, a_4) = (0.28, 0.24, 0.26, 0.22)\):

\[
\text{HSPR} = \frac{a_1 \hat{E} + a_2 \hat{v} + a_3 \hat{P} + a_4 \hat{\rho}}{a_1 + a_2 + a_3 + a_4}
\]

**Not** the same as `calibration.hspr_field` on 1D family field (historical naming overlap — docstring warns refactor may rename).

### 7.4 Trust mapping (bridge layer)

`multiscale_product_bridge` maps HSPR to L7 tags:

| HSPR | OUTPUT_TRUST_TAG | TRUST_TIER |
|------|------------------|------------|
| ≥ 0.7 | HIGH | 3 |
| ≥ 0.4 | MED | 2 |
| else | LOW | 1 |

---

## 8. Multiscale contradiction sidecar (optional)

When `contradiction_package` passed (TRIZ / segment loads):

**Function:** `_sealed_multiscale_contradiction_fields`

| Output | Meaning |
|--------|---------|
| `fine_mid_agreement`, `mid_coarse_agreement`, `global_alignment` | cross-scale consistency |
| `contradiction_load_by_scale` | fine / mid / coarse loads |
| `sealed_conflict_trace.persistent_conflict` | ≥2 segments with load > 0.28 |
| `conflict_collapses_under_aggregation` | fine_m > coarse + 0.18 |

Coarse load damped by HSPR distance from 0.5: `hs_n = |hspr - 0.5| * 2`.

---

## 9. Numeric toy trace (pedagogical grid)

**Note:** Production uses **288×250**; below uses **2×4** grid with hand-set numbers to show **formula mechanics** (not calibrated clinical output).

### 9.1 Setup

- `n_families=2`, `n_hex=4`
- Concept hits only on index 0 → after P_CH stub, suppose:

**A0** (initial hex):

```
Family 0: [1.0, 0.5, 0.0, 0.0]
Family 1: [0.0, 0.0, 0.8, 0.2]
```

- Uniform R = 0.35 everywhere
- **C_F** = `[[0, 0.1], [0.1, 0]]` (weak cross-family coupling)
- α=0.08, β=0.05, γ=0.06

### 9.2 One raw step — family 0, hex k=1

\(A_{0,1}=0.5\), neighbors \(A_{0,0}=1.0\), \(A_{0,2}=0\).

\(\text{lap} = 1.0 + 0 - 2(0.5) = 0\)

\(S_0 = 1.5\), \((C_F @ S)_0 = 0.1 \cdot S_1\) — with \(S_1=1.0\): pressure term \(0.1\)

\[
\Delta A = 0 - 0.05 \cdot 0.35 \cdot 0.5 - 0.06 \cdot 0.1 = -0.00875 - 0.006 = -0.01475
\]
\[
A'_{0,1} \approx 0.485
\]

(Same loop runs for all \((m,k)\); then clip + energy line search in production.)

### 9.3 Family aggregate

\(F_0 = \sum_k A'_{0,k}\), \(F_1 = \sum_k A'_{1,k}\)

### 9.4 Area (toy 2 families → 1 area each)

With 2 families only: area[0] = F_0, area[1] = F_1.

### 9.5 Propagation strength

If mean \(|A_1 - A_0| \approx 0.012\) → `propagation_strength ≈ 0.012`.

### 9.6 Contradiction pressure

Compute \(G = A_1 A_1^\top\) (2×2), multiply elementwise with C_F, sum — yields scalar **P** used in HSPR.

**Takeaway:** even one step **diffuses** mass along rings, **damps** via R, **couples** families through C_F; signals read **before/after** pair (A0, A1).

---

## 10. File-level map (Run 03 scope)

| File | Blocks | Purpose |
|------|--------|---------|
| `sealed_multiscale_stack.py` | `run_sealed_multiscale_stack`, `_area_from_family`, `_sealed_multiscale_contradiction_fields` | Orchestrator |
| `e2e_bridge.py` | `markers_to_concept_activation` | S0 concept hits |
| `pch_loader.py` | `load_pch` | Governed sparse P_CH |
| `hex_matrix_builders.py` | `apply_pch_to_concept_activation`, `build_ring_laplacian`, `build_uniform_hex_resistance` | S2–S5 builders |
| `matrix_loader.py` | `load_production_matrices` | C_F, L_F, R_F |
| `hex_dynamics.py` | `_step_hex_local_microphysics_raw`, `step_hex_local_microphysics` | S6 step |
| `energy.py` | `compute_energy_hex_2d`, `energy_acceptable`, `EnergyControlParams` | Energy gate |
| `hex_family_bridge.py` | `compute_family_activation`, `load_hex_family_overrides` | S7 |
| `product_signals.py` | all `*_hex` functions, `compute_product_signals` | S9 |
| `hspr_index.py` | `field_state_from_hex_stack`, `compute_hspr_index` | S10 |
| `multiscale_product_bridge.py` | `build_structural_internal_from_multiscale` | Adapter to L1–L7 public layers |

---

## 11. States and parameters (Spine B)

### 11.1 Persistent tensors through one request

```
text
  → a_concept (288)
  → A0 (288×250)
  → A1 (288×250)
  → F (288)
  → area (12)
  → signals {P, v, ρ, …}
  → hspr_index
```

### 11.2 Env knobs (selected)

| Variable | Effect on Spine B |
|----------|-------------------|
| `HESPERIA_ASSETS_ROOT` | dict_a/b paths |
| `HESPERIA_PCH_DIR` | P_CH location |
| `HESPERIA_PRODUCTION_MATRICES_DIR` | C_F bundle |
| `HESPERIA_CONCEPT_EVIDENCE_GUARD` | strict attribution |
| `HESPERIA_SEALED_DLCR_SIDECAR` | clinical_resolution_sidecar |
| `HESPERIA_FIELD_DYNAMICS*` | dev/E2E extensions (not default shipping) |

Full allowlist: brain [HESPERIA-TFP-RUNTIME-VARIABLES-TABLE.md](../../HESPERIA-TFP-RUNTIME-VARIABLES-TABLE.md).

### 11.3 Relation to modular Spine A (Run 02)

| Aspect | Spine A (modules) | Spine B (sealed) |
|--------|-------------------|------------------|
| Family dimension | 24 (metrics.base) | 288 |
| Hex layer | absent | **required** |
| TFP module | explicit `tfp.v1` | not in this stack |
| Shipping `/analyze` | no | **yes** |
| 0.6.3 IRC Teacher | indirect via HTTP | **yes** |

---

## 12. Concomitant paths inside one analyze call

Within `run_structural_analysis` (Run 04 detail):

1. **Sealed stack** (sync) — this run.
2. **Optional DLCR** — if `structural_dlcr_allowed()`, `run_dlcr_pipeline` merges `lexical_resolution` into public payload **after** projection (concomitant second lexical pass, not alternate hex math).
3. **Optional TRIZ** — only if `use_triz_contradiction=True` in stack call (default **False** on shipping service).

No threads: DLCR and sealed stack run **sequentially** in the same request handler.

---

## 13. Run 03 summary

| Stage | Formula family | Output parameters for next stage |
|-------|----------------|----------------------------------|
| S0–S1 | token attribution, hit counts | `a_concept` |
| S2 | sparse P_CH @ concept | **A0** |
| S6 | §7b local update + energy gate | **A1** |
| S7–S8 | sum over hex / block sum | **F**, **area** |
| S9 | hotspot, Gram lift, entropy | signal dict |
| S10 | hat + weighted HSPR | `hspr_index`, trust |

---

## NEXT (Colombo)

1. [ ] **Run 04** — `analysis_service`, `project_to_public`, FastAPI `/analyze`, ENGINE-ANALYZE `trace[]` iteration — owner: **Colombo**
2. [ ] **Run 05** — 0.6.3 IRC Teacher full RU trace, MySQL, parameter tables, bibliography — owner: **Colombo**
3. [ ] Optional: promote condensed "sealed stack spec" to `docs/specs/` on dev — owner: **Felix** after Grace triage

**Verified exists:** all cited files @ `e9eaa07`; invariant_catalog 288×250; energy + product_signals formulas match source  
**Still unverified:** live prichindel sidecar field names for `ksi`, `interior_pov` on `/analyze` (Run 04)

---

SIGNED: Research (Colombo) | Hesperia description object investigation Run 03 | 2026-06-14 | v0.6.3
