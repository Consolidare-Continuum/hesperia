<!--
HESPERIA — Reference Architecture Definition (RAD)
Copyright © 2026 igareosh.com — Platonov Igor (aka @igareosh). All rights reserved.
Restricted Research Disclosure License. Inspection and reference only.
See LEGAL_NOTICE.md for full terms.
-->

# Ethan spec — semantic field dynamics (hex-grounded lattice on fixed topology)

**Status:** specification for **future wiring** into Hesperia. **Not fully implemented** as a single coupled solver. Existing pieces: icosahedral **area** propagation (`sphere/`), family/hex geometry in topology invariants, KME/TRIZ contradiction signals. This document is the **canonical math target**.

**Related:** [DYNAMICS_EQUATION_INDEX.md](DYNAMICS_EQUATION_INDEX.md) (compact ↔ extended ↔ phases) · **[SEMANTIC_FIELD_EQUATIONS_v1.md](SEMANTIC_FIELD_EQUATIONS_v1.md)** (closed family-field \(\mathbf{F}\) PDE + observables; `semantic_field_v1`) · [TASK-GRACE-ETHAN-DYNAMICS-IMPLEMENTATION-TEAM.md](governance/TASK-GRACE-ETHAN-DYNAMICS-IMPLEMENTATION-TEAM.md) · [ETHAN-OPEN-WORKFLOW-PROCEED.md](governance/ETHAN-OPEN-WORKFLOW-PROCEED.md) (Phase 2–3 proceed log) · [TOPOLOGY_INVARIANTS.md](../TOPOLOGY_INVARIANTS.md) · [HESPERIA_DYNAMICS_CALIBRATION_SPEC_v0_1.md](HESPERIA_DYNAMICS_CALIBRATION_SPEC_v0_1.md) (**calibration by design**: Class A/B/C parameters, constraints, objectives, scenarios, search, profiles) · [HESPERIA_VARIABLE_CATALOG.md](../HESPERIA_VARIABLE_CATALOG.md) · [HESPERIA_SYSTEM_AWARENESS.md](../HESPERIA_SYSTEM_AWARENESS.md)

---

# Part A — Full layer wire (L0–L10) & compact dynamics index

## A.1 Core principle: measurement vs state transition

**Current Hesperia (mostly):**

```text
text → extraction → activation → topology mapping → propagation → metrics → guards → output
```

Each run ≈ **stateless measurement** on a document.

**Dynamic Hesperia:**

```text
input stream over time
  → state injection
  → local field update
  → family update
  → area update
  → contradiction update
  → graph/tension update
  → guard check
  → dynamic output
```

Each run ≈ **state transition**. The **old pipeline stays**; the difference is carrying **State(t)** forward.

**Formal:**

\[
\mathsf{State}(t+1) = F\bigl(\mathsf{State}(t),\, \mathsf{Input}(t),\, \mathsf{Topology},\, \Theta\bigr)
\]

Single document ⇒ dynamics **degenerates to one step**; static mode preserved.

---

## A.2 Full layer wire (canonical L0–L10)

| Layer | Name | Role |
|-------|------|------|
| **L0** | Input / event-time | Stream, timestamps, batching; produces \(u_i(t)\), time-indexed injection |
| **L1** | Dict A marker activation | Lexical excitations \(s_m(t)\); optional marker persistence \(s_m^*(t+1)=(1-\lambda_m)s_m^*+\mathrm{input}_m\) |
| **L2** | Dict B concept activation | Stateful concepts \(c_i(t)\); first true dynamic semantic layer |
| **L3** | Concept graph dynamics | \(G_i, Q_i, H_g, T_g, \Xi\); graph as interaction medium, not static description |
| **L4** | Hex field dynamics | Local field \(x_h\), hex pressure \(p_h\); diffusion on \(H_{hk}\); **active subgraph first** |
| **L5** | Family dynamics | Meso: aggregate from hex \(\hat{X}_f\), intra-family spread, area feedback |
| **L6** | Area dynamics | Macro public field \(a_a\); icosahedral diffusion |
| **L7** | Contradiction dynamics | Coupled pressure \(p_f, p_a\) + **resolution** \(R\) (coherence, bridges, TRIZ) — not a side metric |
| **L8** | Global graph / cluster dynamics | Cluster mass, gravity, velocity; narrative attractors, fronts |
| **L9** | Trust / stability / guards | Stab, Osc, boundedness, no runaway contradiction; Sigma/Gamma/Theta doctrine |
| **L10** | Public projection / dynamic outputs | Narrow, time-aware exports; **still strip reserved internals** |

**Semantic spine:** L0→L1→L2→**L3**→**L4**→L5→L6→**L7**→L8→L9→L10.

---

## A.3 Layer-by-layer integration (summary)

**L0 — Input / event-time**  
Inputs: document stream, timestamp, source id, corpus id, optional actor/channel/domain tags.  
Output per \(t\): \(u_i(t)\), event batch, rolling window. **Rule:** one document ⇒ single-step update.

**L1 — Dict A**  
Markers as instantaneous excitations \(s_m(t)\); inject into concept path. Evidence spans unchanged in static trace; dynamics adds **marker activation / persistence vectors**.

**L2 — Dict B**  
\(c_i(t+1)=\mathrm{clip}[(1-\lambda_c)c_i+\alpha_{\mathrm{in}}\hat u_i+\alpha_g\sum_j W_{ji}c_j-\alpha_p\sum_j K_{ij}c_ic_j]\).  
Outputs: concept state, velocity, persistence, contradiction load. **Wires to** current activations, relation graph, KME/TRIZ.

**L3 — Concept graph dynamics**  
\(G_i(t)=\sum_j W_{ji}c_j\), \(Q_i=\sum_j K_{ij}c_ic_j\), \(H_g=\sum_{ij}W_{ij}c_ic_j\), \(T_g=\sum_{ij}K_{ij}c_ic_j\), \(\Xi=T_g-\omega_h H_g\).  
Sits where **graph-derived primitives / derived metrics** already live.

**L4 — Hex field**  
\(x_h\) update + \(p_h\) update (§Part B). Propagation on **local cells before** family/area aggregation. Outputs: active hex subgraph, hotspots, gradients, fronts, contradiction pockets — **active hex subset only** initially.

**L5 — Family**  
\(\hat{X}_f\) from hexes; \(f_f\) update with \(\beta_x,\beta_{\mathrm{intra}},\beta_{\mathrm{area}},\beta_{pf}\). Bridge **lattice → macro topology**.

**L6 — Area**  
\(a_a\) from \(\hat{F}_a\), neighbor \(Q_a\); plugs into **current public area vector** behavior.

**L7 — Contradiction dynamics**  
\(p_f, p_a\) with memory, spillover, **\(R_a=\mathrm{coherence}_a+\mathrm{bridge}_a+\mathrm{triz\_res}_a\)**. **Real TRIZ wire** inside Hesperia, not isolated.

**L8 — Cluster dynamics**  
\(\mathrm{Mass}_k,\mathrm{Density}_k,\mathrm{Radius}_k,\mathrm{Gravity}_k,V_k\); dominant attractors, growth/decay, migration, penetration fronts.

**L9 — Trust / guards**  
\(\mathrm{Stab}_a,\mathrm{Stab},\mathrm{Osc}_a\); checks: boundedness, monotonic safety, no negative fields, no explosive contradiction, topology invariants, deterministic replay. Trust from evidence, coverage, contradiction overload, instability, oscillation, low resolution rate.

**L10 — Public projection**  
Static + dynamic: area/family state, dominants, propagated state, contradiction pressure, \(\Xi\), stability, oscillation, narrative penetration, cluster gravity, velocity, trust, evidence. **Time-aware:** `state_t`, `delta_t`, `trend_window`, `pressure_window`, `stability_window`. **Dynamics must not leak internal ontology mechanics.**

---

## A.4 Compact equation wire (H0–H9)

| ID | Name | Equation |
|----|------|----------|
| **H0** | Input injection | \(I_i(t)=\alpha_{\mathrm{in}}\hat u_i(t)\) |
| **H1** | Concept dynamics | \(c_i(t+1)=\mathrm{clip}[(1-\lambda_c)c_i+I_i+\alpha_g\sum_j W_{ji}c_j-\alpha_p\sum_j K_{ij}c_ic_j]\) |
| **H2** | Hex dynamics | \(x_h(t+1)=\mathrm{clip}[(1-\lambda_h)x_h+\theta_c\hat C_h+\theta_d\frac{1}{\deg h}\sum_k H_{hk}x_k-\theta_p p_h-r_h]\) |
| **H3** | Hex contradiction | \(p_h(t+1)=(1-\mu_h)p_h+\delta_h S_h+\eta_h\frac{1}{\deg h}\sum_k H_{hk}p_k-\rho_h R_h\) |
| **H4** | Family dynamics | \(f_f(t+1)=\mathrm{clip}[(1-\lambda_f)f_f+\beta_x\hat X_f+\beta_{\mathrm{intra}}\sum_g B_{fg}f_g+\beta_{\mathrm{area}}a_{\mathrm{area}(f)}-\beta_{pf}p_f]\) |
| **H5** | Family contradiction | \(p_f(t+1)=(1-\mu_f)p_f+\delta_f S_f-r_f R_f\) |
| **H6** | Area dynamics | \(a_a(t+1)=\mathrm{clip}[(1-\lambda_a)a_a+\gamma_f\hat F_a+\gamma_q\frac{1}{\deg a}\sum_b A_{ab}a_b-\gamma_p p_a-\rho_a]\) |
| **H7** | Area contradiction | \(p_a(t+1)=(1-\mu_a)p_a+\delta_a S_a+\eta_a\sum_b A_{ab}p_b-r_a R_a\) |
| **H8** | Global graph tension | \(\Xi(t)=\sum_{ij}K_{ij}c_ic_j-\omega_h\sum_{ij}W_{ij}c_ic_j\) |
| **H9** | Stability | \(\mathrm{Stab}(t)=1-\frac{1}{|A|}\sum_a|a_a(t+1)-a_a(t)|\) |

**Part B** below expands hex sources \(\hat C_h, S_h\), resolution terms, gradients, and **hex cluster gravity** (supplements L8 when clusters are hex-lattice–based).

---

## A.5 Mapping to existing Hesperia artifacts

Dynamics **does not replace** the stack. It **reuses**:

| Existing | Dynamic use |
|----------|-------------|
| Dict A / B activation | L1/L2 injection & state |
| Concept relation graph | \(W,K\), L3 |
| Topology mapping | \(Z,Y,N,A,H\) |
| Area/family aggregation | L5/L6 targets |
| Propagation metrics | L4/L6 diffusion |
| Contradiction / TRIZ | L7 pressure + resolution |
| Trust / guards | L9 |
| E2E JSON, deterministic export | L10 time-indexed series |

Convert **per-run metrics** → **state variables** + **update equations** + **time-indexed outputs**.

---

## A.6 Implementation order (inside existing stack)

| Phase | Wire |
|-------|------|
| **1** | **Minimal closed loop:** L0 (time) + L2 concept state + **L6 area** + **L7 area contradiction** \(p_a\) + **L9** stability/guards |
| **2** | **L5** family state + family pressure \(p_f\) |
| **3** | **L4** hex activation + hex contradiction on **active hex subgraph only** |
| **4** | **L8** cluster gravity, global fronts, narrative attractor migration |

Do **not** enable all layers at once. Part B “Phase A–D” (compressed → full hex grid) aligns: Phase 1 here ≈ compressed area+contradiction; Phase 3 = active hex.

**Calibration:** Class **B** dynamics parameters (decays, gains, penalties, spillover, resistance, thresholds) are tuned **sequentially by layer** with **hard constraints first**; Class **A** fixed; Class **C** outputs never used as knobs. See [HESPERIA_DYNAMICS_CALIBRATION_SPEC_v0_1.md](HESPERIA_DYNAMICS_CALIBRATION_SPEC_v0_1.md).

---

# Part B — Hex-grounded lattice & extended dynamics IDs

## 0. Positioning sentence

**Hexagons are Hesperia’s local semantic field cells.** They are the **micro-dynamic layer** where activation diffuses, contradiction accumulates, and narrative fronts form **before** aggregation into families and areas. Family is **meso**; area is **macro**; **hex is the smallest spatial unit** for proper field physics—not optional if the engine is to be a true **lattice dynamics** system rather than only hierarchical scoring.

---

## 1. Canonical stack (hex in the middle)

Correct ordering:

```text
Concepts  (semantic particles / sources)
    ↓
Hexagons  (local field cells — lattice nodes)
    ↓
Families  (mesoscopic compartments)
    ↓
Areas     (macroscopic domains)
```

**Not** concept → family → area **only**; that stack is a **compressed** model. Full physics uses **hex as the real local semantic cell** (finite spatial element, local pressure pockets, gradients, fronts).

| Scale | Role |
|-------|------|
| **Area** | Too coarse alone for local diffusion |
| **Family** | Meso-structure; not the finest spatial unit |
| **Hex** | Micro-topology: local concentration, spread, gradients, contradiction hotspots |

Without hex, propagation jumps between abstract groups and **weakens the physics analogy**.

---

## 2. Core thesis (master form)

Discrete-time semantic field:

\[
X(t+1) = F\bigl(X(t),\, U(t),\, G,\, T,\, \Theta\bigr)
\]

\(T\) now includes **hex adjacency** \(H_{hk}\), **concept→hex** \(Z_{ih}\), **hex→family** \(Y_{hf}\), plus **family→area** \(N_{fa}\) and **area adjacency** \(A_{ab}\).

---

## 3. State variables

### 3.1 Concept layer

\(c_i(t) \in [0,1]\) — concept \(i\) activation.

### 3.2 Hex layer (micro-field)

For each hex \(h\) (index in operational or full grid per implementation):

| Variable | Domain | Meaning |
|----------|--------|---------|
| \(x_h(t)\) | \([0,1]\) | Local semantic activation |
| \(p_h(t)\) | \(\geq 0\) | Local **contradiction pressure** |
| \(r_h(t)\) | \(\geq 0\) | Local **propagation resistance** |
| \(v_h(t)\) | \(\mathbb{R}\) | \(x_h(t) - x_h(t-1)\) — local velocity |

### 3.3 Family layer

\(f_f(t) \in [0,1]\); optional \(p_f(t)\) for meso pressure (aggregated from hex or parallel).

### 3.4 Area layer

\(a_a(t) \in [0,1]\); \(p_a(t)\) for macro pressure (optional uplink from hex/family).

---

## 4. Fixed structures

### 4.1 Concept → hex

\(Z_{ih} \in [0,1]\) — concept \(i\) contributes to hex \(h\) (binary or weighted). **Injection path:** Dict A/B placement into \((A,F,H)\) induces \(Z\).

### 4.2 Hex adjacency

\(H_{hk} \in \{0,1\}\) — hex \(h\) adjacent to hex \(k\). **Local diffusion graph.** Degree \(\deg(h)\).

### 4.3 Hex → family

\(Y_{hf} \in \{0,1\}\) — hex \(h\) belongs to family \(f\) (each hex in exactly one family in standard grid).

### 4.4 Family → area

\(N_{fa} \in \{0,1\}\) — family \(f\) in area \(a\).

### 4.5 Area adjacency

\(A_{ab} \in \{0,1\}\) — 12-area icosahedral graph ([TOPOLOGY_INVARIANTS.md](../TOPOLOGY_INVARIANTS.md)).

### 4.6 Concept graph (unchanged)

\(W_{ij}\) support; \(K_{ij} \geq 0\) contradiction strength.

---

## 5. External injection

As before: \(\hat{u}_i(t)\), \(I_i(t) = \alpha_{\mathrm{in}}\hat{u}_i(t)\). Concepts may also inject **directly into hex** via \(Z_{ih}\) when updating \(C_h(t)\) below.

---

## 6. Equation set H1–H9 (hex-grounded)

### H1 — Concept activation equation

**Hex-primary path** (concepts couple to graph and contradictions; family feedback optional):

\[
c_i(t+1) = \mathrm{clip}\Bigl[
(1-\lambda_c)\, c_i(t)
+ I_i(t)
+ \alpha_g \sum_j W_{ji}\, c_j(t)
- \alpha_p \sum_j K_{ij}\, c_i(t)\, c_j(t)
\Bigr]
\]

**Extended path** (legacy hierarchical coupling): add \(+ \alpha_f \sum_f M_{if}\, f_f(t)\) when running **compressed** mode without explicit hex dynamics.

---

### H2 — Hex activation equation (local field)

Concept influx into hex \(h\):

\[
C_h(t) = \sum_i Z_{ih}\, c_i(t), \qquad
\hat{C}_h(t) = \frac{C_h(t)}{\max(1,\,\sum_i Z_{ih})}
\]

Neighbor diffusion:

\[
D_h(t) = \frac{1}{\deg(h)} \sum_k H_{hk}\, x_k(t)
\]

**Update:**

\[
x_h(t+1) = \mathrm{clip}\Bigl[
(1-\lambda_h)\, x_h(t)
+ \theta_c\, \hat{C}_h(t)
+ \theta_d\, D_h(t)
- \theta_p\, p_h(t)
- r_h(t)
\Bigr]
\]

| Param | Role |
|-------|------|
| \(\lambda_h\) | Hex decay |
| \(\theta_c\) | Concept→hex gain |
| \(\theta_d\) | Hex diffusion gain |
| \(\theta_p\) | Contradiction penalty |
| \(r_h(t)\) | Local resistance (§10) |

---

### H3 — Hex contradiction pressure equation

Local contradiction source (pairs co-located on hex):

\[
S_h(t) = \sum_{i,j} Z_{ih}\, Z_{jh}\, K_{ij}\, c_i(t)\, c_j(t)
\]

**Pressure update:**

\[
p_h(t+1) = (1-\mu_h)\, p_h(t)
+ \delta_h\, S_h(t)
+ \eta_h\, \frac{1}{\deg(h)} \sum_k H_{hk}\, p_k(t)
- \rho_h\, R_h(t)
\]

| Param | Role |
|-------|------|
| \(\mu_h\) | Dissipation |
| \(\delta_h\) | Accumulation |
| \(\eta_h\) | Pressure spillover on hex graph |
| \(R_h(t)\) | **Local resolution force** (coherence / bridges / TRIZ resolution at hex or lifted from family) |

**Contradiction hotspots** emerge at hex scale first; family/area pressure can **aggregate** \(\sum_{h\in f} p_h\) or \(\sum_{h\in a} p_h\).

---

### H4 — Family aggregation equation (from hex field)

Hex mass per family:

\[
X_f(t) = \sum_h Y_{hf}\, x_h(t), \qquad
\hat{X}_f(t) = \frac{X_f(t)}{\max(1,\,\sum_h Y_{hf})}
\]

\[
f_f(t+1) = \mathrm{clip}\Bigl[
(1-\lambda_f)\, f_f(t)
+ \beta_x\, \hat{X}_f(t)
+ \beta_{\mathrm{intra}} \sum_g B_{fg}\, f_g(t)
+ \beta_{\mathrm{area}}\, a_{\mathrm{area}(f)}(t)
- \beta_{pf}\, p_f(t)
\Bigr]
\]

Family state is **meso-aggregation of local field states**—cleaner than concept-only family sums when hex dynamics are on.

**Compressed fallback:** \(\hat{C}_f\) from concepts only (previous spec) when hex layer disabled.

---

### H5 — Area propagation equation

\[
F_a(t) = \sum_f N_{fa}\, f_f(t), \qquad
\hat{F}_a(t) = \frac{F_a(t)}{\max(1,\,\text{\#families in }a)}
\]

\[
Q_a(t) = \frac{1}{\deg(a)} \sum_b A_{ab}\, a_b(t)
\]

\[
a_a(t+1) = \mathrm{clip}\Bigl[
(1-\lambda_a)\, a_a(t)
+ \gamma_f\, \hat{F}_a(t)
+ \gamma_q\, Q_a(t)
- \gamma_p\, p_a(t)
- \rho_a(t)
\Bigr]
\]

\(\hat{F}_a\) is now **downstream of hex-grounded** family field → **spatially grounded** macro dynamics.

---

### H6 — Resolution equation (multi-scale)

\[
R_h(t) = \mathrm{coherence}_h(t) + \mathrm{bridge}_h(t) + \mathrm{triz\_res}_h(t)
\]

Similarly \(R_f\), \(R_a\) for family/area pressure equations when used. **Without resolution, pressure diverges**—mandatory for long horizons.

---

### H7 — Hex spatial derivatives (gradient, front, turbulence)

**Local gradient** (sharp semantic boundaries):

\[
\mathrm{grad}_h(t) = \max_{k \in \mathcal{N}(h)} \bigl| x_h(t) - x_k(t) \bigr|
\]

**Propagation front** (narrative expansion): flag when \(x_h(t+1) - x_h(t) > \tau_v\) coordinated with neighbor cluster motion.

**Local turbulence:**

\[
\mathrm{turb}_h(t) = \bigl| x_h(t+1) - 2x_h(t) + x_h(t-1) \bigr|
\]

High \(\mathrm{turb}_h\) ⇒ unstable local semantics.

---

### H8 — Hex narrative cluster gravity

Cluster \(m\) = connected component of **actively** high hexes on graph \(H\):

\[
\mathrm{Mass}_m(t) = \sum_{h \in m} x_h(t)
\]

\(\mathrm{Density}_m\) = active edges / possible internal edges; \(\mathrm{Radius}_m\) = mean graph distance from centroid on **hex lattice**.

\[
\mathrm{Gravity}_m(t) = \frac{\mathrm{Mass}_m(t)\cdot \mathrm{Density}_m(t)}{1 + \mathrm{Radius}_m(t)}
\]

**Stronger than concept-only clustering**—respects micro-topology.

---

### H9 — Global graph tension & stability

\[
T_g(t) = \sum_{i,j} K_{ij}\, c_i(t)\, c_j(t), \quad
H_g(t) = \sum_{i,j} W_{ij}\, c_i(t)\, c_j(t), \quad
\Xi(t) = T_g(t) - \omega_h H_g(t)
\]

**Stability** (hex or area): \(\mathrm{Stab}_h(t) = 1 - |x_h(t+1)-x_h(t)|\); global hex stability average. **Oscillation** on hex: same second-difference form as §H7 turbulence.

---

## 7. Hex resistance (primary locus)

Resistance is **strongest at hex level**:

\[
r_h(t) = r_{0h} + r_{1h}\, p_h(t) + r_{2h}\, x_h(t)
\]

- Structurally hard hexes: higher \(r_{0h}\)  
- Contradiction raises resistance  
- Saturation raises resistance → prevents runaway spread  

Area resistance \(\rho_a\) remains optional macro term in H5.

---

## 8. Multi-scale mental model

| Layer | Physics role |
|-------|----------------|
| Concepts | Semantic particles / sources |
| Hexes | Local field cells |
| Families | Mesoscopic compartments |
| Areas | Macroscopic domains |

**Multi-scale lattice dynamics**, not only hierarchical aggregation.

---

## 9. Implementation doctrine (do not simulate 72 000 hexes on day one)

1. **Phase A — compressed:** area-only (and/or family-only) dynamics — workable, **compressed** model.  
2. **Phase B — family dynamics** with area coupling.  
3. **Phase C — active hex subgraph:** dynamics **only on hexes touched by current activation** (sparse \(h\) where \(\sum_i Z_{ih}c_i > \epsilon\) or neighbor closure), **not** the full 72 000 grid every step.  
4. **Phase D — full hex field** only if product requires planet-scale lattice resolution.

**Correct order:** bounded active region first; full universe simulation last.

---

## 10. Phased summary table (Part B lattice focus)

Aligns with **Part A.6** implementation order.

| Phase | What runs |
|-------|-----------|
| A | Area-level proxy; \(F_a\) from concept/family if hex off |
| B | Family + area (Part A Phase 2) |
| C | **Concept → hex → family → area** on **active hex set** + hex gradients (Part A Phase 3) |
| D | Full hex grid if ever required |

**Part A Phase 1** = L0+L2+L6+L7 area+L9 (minimal dynamics **before** full Part B stack).

---

## 11. Public outputs (dynamics layer)

Add hex-level series where implemented:

`hex_state` \(x_h\), `hex_pressure` \(p_h\), `hex_velocity` \(v_h\), `hex_gradient`, `hex_turbulence`, `contradiction_hotspot_map`, `hex_cluster_gravity`, plus existing `area_state`, `family_state`, `concept_state`, \(\Xi\), stability indices.

---

## 12. Implementation notes (repo alignment)

| Structure | Source |
|-----------|--------|
| \(H_{hk}\), hex registry | `assets`/topology — must define adjacency on operational 60k hex graph |
| \(Y_{hf}\), \(N_{fa}\) | Family–hex–area from ontology / `sphere/topology` family structure |
| \(Z_{ih}\) | From placement pipeline \((A,F,H)\) per activated concept |
| Solver | New module e.g. `hesperia/engine/field_dynamics/` or `core/` layer — **deterministic** update order |

**Projection:** public API may expose **aggregated** hex metrics (hotspots, max gradient) without leaking full reserved hex indices.

---

## 13. Two equation index schemes

**A — Compact wire (Part A.4): H0–H9** — single implementation checklist: injection → concept → hex → hex \(p\) → family → family \(p\) → area → area \(p\) → \(\Xi\) → Stab.

**B — Extended lattice IDs (below):** use when coding **resolution**, **hex spatial derivatives**, **hex-lattice cluster gravity** separately from the compact row.

| Ext ID | Name |
|--------|------|
| **H1** | Concept activation (same as A **H1**) |
| **H2** | Hex field activation (same as A **H2**) |
| **H3** | Hex contradiction (same as A **H3**) |
| **H4** | Family from hex (same as A **H4**) |
| **H5** | Area propagation (same as A **H6**) |
| **H6** | Resolution \(R_h,R_f,R_a\) (feeds A **H3,H5,H7**) |
| **H7** | Hex gradient / front / turbulence |
| **H8** | Hex narrative cluster gravity |
| **H9** | Global \(\Xi\) + stability (maps to A **H8,H9**) |

---

## 14. Full stack (Part B extended)

```text
H1  c_i   ← H0 + graph + K penalty
H2  x_h   ← Z·c + hex diffusion − p_h − r_h
H3  p_h   ← S_h + spillover − R_h (H6)
H4  f_f   ← Y·x + intra-family + area − p_f
H5  a_a   ← N·f + area diffusion − p_a − ρ_a  [A wire: H6]
H6  R_*   resolution (L7)
H7  grad, front, turb
H8  hex cluster gravity (L8 hex-native)
H9  Ξ, Stab  [A wire: H8, H9]
```

L-layer pipeline: **Part A §A.2**.

---

*Ethan spec v3 — L0–L10 wire + H0–H9 compact index + hex lattice (Part B).*
