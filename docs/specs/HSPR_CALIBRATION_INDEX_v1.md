<!--
HESPERIA — Reference Architecture Definition (RAD)
Copyright © 2026 igareosh.com — Platonov Igor (aka @igareosh). All rights reserved.
Restricted Research Disclosure License. Inspection and reference only.
See LEGAL_NOTICE.md for full terms.
-->

# HSPR_CALIBRATION_INDEX_v1

**Status:** Draft for lock-in  
**Purpose:** Define one bounded composite calibration score for the semantic field layer.

**Implementation:** `hesperia.engine.field_dynamics.calibration` · **Runtime:** `python3 -m runtime.semantic_field.run_field_calibration` · **Spec:** [SEMANTIC_FIELD_EQUATIONS_v1.md](SEMANTIC_FIELD_EQUATIONS_v1.md)

---

## 1. Definition

The **HSPR Calibration Index (HCI)** is the canonical bounded scalar that summarizes the quality of a semantic-field parameter set.

It measures whether a chosen parameter set produces a field that is:

- stable,
- source-aligned,
- low-energy (when non-negative),
- low-contradiction,
- low-fragmentation (diffusion load),
- resistance-efficient.

The index is bounded:

\[
0 \le \mathrm{HCI} \le 1
\]

**Higher is better.**

---

## 2. Formula

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

with normalized terms in \([0,1]\):

| Symbol | Meaning |
|--------|---------|
| \(\Sigma\) | Stability score |
| \(\hat Q\) | Normalized source alignment |
| \(\hat E\) | Normalized energy quality |
| \(\hat K\) | Normalized contradiction quality |
| \(\hat D\) | Normalized diffusion quality |
| \(\hat R\) | Normalized resistance quality |

Weights must **sum to 1** (implementation renormalizes if needed).

---

## 3. Components

### 3.1 Stability

\[
\Sigma = \frac{1}{1+\|\mathbf{F}_{t+1}-\mathbf{F}_t\|_2}
\]

(clipped to \([0,1]\)). Higher is better.

### 3.2 Source alignment

\[
Q = \mathbf{S}^T \mathbf{F}
\]

\[
\hat Q = \frac{Q}{Q+\kappa_Q}
\]

\(\kappa_Q > 0\) (default 1). Higher is better.

### 3.3 Energy quality

\[
\hat E = \frac{1}{1+\max(E,0)}
\]

Higher is better (penalizes large positive energy).

### 3.4 Contradiction quality

\[
K = \mathbf{F}^T C \mathbf{F}
\]

\[
\hat K = \frac{1}{1+K}
\]

Higher is better.

### 3.5 Diffusion quality

\[
D = \mathbf{F}^T L_F \mathbf{F}
\]

\[
\hat D = \frac{1}{1+D}
\]

Higher is better.

### 3.6 Resistance quality

\[
R_{\mathrm{load}} = \mathbf{F}^T R_F \mathbf{F}
\]

\[
\hat R = \frac{1}{1+R_{\mathrm{load}}}
\]

Higher is better.

---

## 4. Default weights

| Component | Weight |
|-----------|--------|
| stability | 0.25 |
| source_alignment | 0.25 |
| energy | 0.15 |
| contradiction | 0.15 |
| diffusion | 0.10 |
| resistance | 0.10 |

---

## 5. Interpretation bands

| HCI | Band |
|-----|------|
| 0.85–1.00 | Very strong calibration |
| 0.70–0.85 | Usable / strong |
| 0.50–0.70 | Weak / unstable / underfit |
| &lt; 0.50 | Poor calibration |

---

## 6. Normative use

HCI is the **canonical ranking score** for parameter search in semantic-field calibration (e.g. grid search). The best candidate is the one with highest HCI; tie-breakers may use convergence flags and energy.

**Artifacts:** full report JSON, `*_best.json`, `*_topk.json` (see `runtime/semantic_field/run_field_calibration.py`).

---

## 7. Non-claim

HCI does **not** prove truth, correctness, or domain validity. It only summarizes **internal dynamical quality** of a parameterized semantic field run under the given topology, sources, and matrices.

---

## 8. Assessment

This supports **structured search**: grid search, deterministic scoring, ranked calibration output. It is **not** automatic learning in the stronger sense; it is governed, explainable, and reproducible.
