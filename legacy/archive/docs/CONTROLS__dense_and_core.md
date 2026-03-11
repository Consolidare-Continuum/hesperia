# HESPERIA — Primary contrast and core controls

Single reference for dense-layer sharpness, shadow, core energy, tension, and reduction. Tweak in order; do not change everything at once.

---

## 1. PRIMARY CONTRAST CONTROLS (Dense layer)

Control semantic sharpness. Order in pipeline: dense projection → **temperature sharpen** (with **gamma**) → **topK** (optional) → shadow perturb → reduce_288_to_5 → core.

### 1.1 HESPERIA_TEMPERATURE

| Item | Value |
|------|--------|
| **Current working** | 0.02 |
| **Range to explore** | 0.015 – 0.03 |
| **Source** | Env `HESPERIA_TEMPERATURE`; default in code 0.15 |

**Rules:**
- entropy_norm > 0.85 → lower T
- entropy_norm < 0.65 → raise T

### 1.2 gamma_contrast (HESPERIA_GAMMA)

Power on magnitudes before softmax: `m_f = |v_f|^gamma`.

| Item | Value |
|------|--------|
| **Suggested** | 1.5 – 2.5 |
| **Default** | 2.0 |
| **Source** | Env `HESPERIA_GAMMA`; clamped 1.0–3.0 |

**Effect:** Increases contrast without extreme temperature collapse.

### 1.3 topK_truncation (HESPERIA_TOP_K)

After sharpening: keep only top K families by |value|; zero the rest.

| Item | Value |
|------|--------|
| **Suggested** | 12 – 25 (0 = off) |
| **Default** | 0 (off) |
| **Source** | Env `HESPERIA_TOP_K`; clamped 0–288 |

**Effect:** Structural sparsity, higher tension potential, lower entropy.

---

## 2. SHADOW LAYER CONTROLS

### 2.1 k_shadow_perturb

| Item | Value |
|------|--------|
| **Current** | 0.04 (default); config 0.06 |
| **Try** | 0.06 – 0.12 |
| **Source** | `guard_config_v1.json` → `shadow.k_shadow_perturb`; env `HESPERIA_K_SHADOW_PERTURB` (0–0.5) |

**Rules:**
- shadow_delta_magnitude < 0.001 → increase
- shadow delta explodes → reduce

### 2.2 shadow_spread_factor

Not implemented. If added: control how widely perturbation diffuses; range 0.2–0.5; higher = more cross-family bleed.

---

## 3. CORE ENERGY CONTROLS

Determines how much the dense seed affects traversal.

| Param | Role | Range | Default | Source (env override) |
|-------|------|--------|--------|------------------------|
| **alpha** | Fusion weight (seed vs L) | 0.6 – 0.8 | 0.65 | `fusion.alpha`; `HESPERIA_ALPHA` |
| **lambda** | Energy damping | 0.4 – 0.65 | 0.55 | `traversal.lambda`; `HESPERIA_LAMBDA` |
| **eta** | Energy transfer / activation threshold | 0.02 – 0.08 | 0.02 | `centroid.activation_threshold_eta`; `HESPERIA_ETA` |
| **decay** | Energy decay | 0.02 – 0.06 | 0.04 | `traversal.decay`; `HESPERIA_DECAY` |

**Notes:** Higher alpha = stronger influence of initial seed. Lower lambda = more volatile traversal. Higher eta = stronger propagation (too high = unstable). Lower decay = energy persists longer.

---

## 4. TENSION CONTROLS

Tension is often ≈ 0; these amplify opposing polarity and dispersion.

| Param | Role | Range | Default | Source (env override) |
|-------|------|--------|--------|------------------------|
| **delta_gap** | Gap sensitivity (ambiguity) | 0.05 – 0.12 | 0.08 | `ambiguity.delta_gap`; `HESPERIA_DELTA_GAP` |
| **k_guard** | Guard penalty weight | 0.3 – 0.5 | 0.30 | `guard_penalty.k_guard`; `HESPERIA_K_GUARD` |
| **k_disp** | Dispersion coefficient | 0.25 – 0.45 | 0.25 | `dispersion.penalty_k`; `HESPERIA_K_DISP` |

**Obstacle weighting:** `obstacle_score.w_guard` (≈ k_guard_obs), `w_shadow`; range 0.3–0.5. Config only (no env in current impl).

---

## 5. REDUCTION LAYER (288 → 5)

`reduce_288_to_5`: bucket by index ranges; sum |family_vector| per bucket; L1-normalize. No per-bucket weights yet.

**If buckets are uniform:** consider rebalancing by family count per bucket or average anchor strength (future).

---

## 6. Practical rebalance plan

Do not tweak everything at once.

1. **Lock** temperature: `HESPERIA_TEMPERATURE=0.02`.
2. **Add** gamma: default 2.0 (`HESPERIA_GAMMA` or omit).
3. **Measure:** entropy_norm, top5_mass (and top1_mass if available).
4. **If still flat** → set `HESPERIA_TOP_K=20`.
5. **Only then** adjust shadow: increase `k_shadow_perturb` (e.g. 0.06–0.10) if shadow_delta < 0.001.
6. **Only after** shadow shows real movement, touch core: alpha, eta (and optionally lambda, decay).

---

## 7. Important

**If entropy remains high** after T=0.02 and gamma=2 (and optionally topK=20):
→ The issue is **anchor/centroid overlap**, not parameters.
→ No parameter will fix bad centroids. Improve anchors/centroids.

---

## 8. Target metrics (healthy dense regime)

| Metric | Target |
|--------|--------|
| entropy_norm | ≈ 0.65 – 0.80 |
| top1_mass | ≈ 0.05 – 0.12 |
| top5_mass | ≈ 0.20 – 0.40 |
| shadow_delta_magnitude | ≈ 0.001 – 0.01 |
| tension_energy | Non-zero on adversarial sentences |

---

## 9. Env override summary

| Env | Config key | Clamp / note |
|-----|------------|--------------|
| HESPERIA_TEMPERATURE | (dense layer) | 1e-6 – 10 |
| HESPERIA_GAMMA | (dense layer) | 1.0 – 3.0 |
| HESPERIA_TOP_K | (dense layer) | 0 – 288 |
| HESPERIA_ALPHA | alpha | 0 – 1 |
| HESPERIA_ETA | eta | 0.001 – 0.2 |
| HESPERIA_LAMBDA | lambda | 0.01 – 1 |
| HESPERIA_DECAY | decay | 0 – 0.5 |
| HESPERIA_DELTA_GAP | delta_gap | 0.01 – 0.5 |
| HESPERIA_K_GUARD | k_guard | 0 – 1 |
| HESPERIA_K_DISP | k_disp | 0 – 1 |
| HESPERIA_K_SHADOW_PERTURB | k_shadow_perturb | 0 – 0.5 |

Config file: `guard_config_v1.json` (Hesperia root). Env overrides applied after loading JSON.
