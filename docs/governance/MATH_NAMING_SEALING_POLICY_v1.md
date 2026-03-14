# MATH NAMING SEALING POLICY v1

**Status:** Active  
**Purpose:** Do not leak conceptual method through names. A public metric name must not reveal internal mathematical construction.

---

## 1. Principle

Internal math layers use names that reflect implementation (e.g. spatial_density_l3, propagation_dispersion_l5, vector_divergence_l7). **Public-facing outputs** must use only **public-safe names** that describe the concept, not the layer or formula.

---

## 2. Internal → Public Name Mapping (Examples)

| Internal / method-bearing | Public-safe |
|---------------------------|-------------|
| spatial_density_l3 | concentration_score |
| propagation_dispersion_l5 | relation_spread_score |
| vector_divergence_l7 | structural_divergence_score |
| area_vector, family_counts | macro_domain_vector, policy_family_counts |
| CROSS_AREA_RATIO | (expose as leakage/relation_spread in public profile only; no "area") |
| SHADOW_DEVIATION_SCORE | deviation_score or omit in public subset |
| LYAPUNOV_ESTIMATE | stability_indicator or omit |
| SI_* (internal codes) | Public metric profile ids only (concentration_score, etc.) |

---

## 3. Rules

- **Public metric profiles** (see assets/public/public_metric_profiles.json) define the only metric identifiers and display names that may appear in public reports, API responses, or calibration UIs.
- No public artifact may contain internal variable names that reveal layer index (L1–L9), formula structure, or topology (sphere, hex, area, side_id).
- When adding new internal metrics, assign a public-facing alias in the appropriate profile (analyst / demo / commercial) or mark as internal-only.

---

## 4. Acceptance Criterion

A public metric name does not reveal internal mathematical construction (no layer suffix, no formula hint, no topology term).
