---
spec_version: "1.0"
system_version: "0.5.0"
status: canonical
id: HES-SPEC-CORE-PRODUCT-OBS
---

# Product observables (hex-level narrative signals) — canonical

**Code:** `hesperia.engine.product_signals`, `hesperia.engine.hex_outputs`.

Equations below are **binding** for dashboard / product semantics. **Innovation potential I** is **not** defined here — see [../triz/innovation_metrics.md](../triz/innovation_metrics.md).

## 1. Narrative hotspot

For hex cell **h** with activation **A_h** and neighbor set **N(h)**:

\[
\text{Hotspot}(h) = A_h + \lambda \sum_{n \in N(h)} A_n
\]

**λ ≥ 0** is calibration (default from registry / code constants).

## 2. Contradiction pressure (**P**)

Scalar summary of incompatible active pairs at hex scope: structural proxy from family contradiction matrix on active families, or **TRIZ contradiction engine** output when that path is active — detection rules in [../triz/contradiction_engine.md](../triz/contradiction_engine.md).

## 3. Propagation strength (**v**)

\[
v = \frac{1}{N_\text{cells}} \sum_h \frac{|A_h(t+\Delta t) - A_h(t)|}{\Delta t}
\]

(or equivalent mean |ΔA| across active hexes).

## 4. Narrative density (**D**)

\[
D = \frac{\sum_h A_h}{\max(N_\text{active}, 1)}
\]

where **N_active** counts hexes with **A_h > θ** (θ from calibration).

## 5. Pipeline order (binding)

Hex activation → (optional dynamics) → product signals → HSPR system index ([../calibration/hspr_index.md](../calibration/hspr_index.md)).
