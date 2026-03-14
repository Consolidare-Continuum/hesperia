# PUBLIC METRIC EXPOSURE POLICY v1

**Status:** Active  
**Purpose:** Keep full math internally; expose only curated projection. External users never see the complete internal math picture.

---

## 1. Metric Classes

| Class | Purpose | Exposed to |
|-------|---------|------------|
| **Internal full metric set** | All L1–L9 variables, bridge outputs, topology-derived. | Internal only; never public. |
| **Analyst subset** | Curated metrics for internal analysts (more detail than commercial). | Internal / protected. |
| **Demo subset** | Safe metrics for demos and trials. | Public (demo/commercial profile). |
| **Commercial subset** | Minimal set for product: concentration, spread, divergence, confidence, evidence count. | Public. |
| **Calibration-visible subset** | Bounded knobs (thresholds, sensitivity) without revealing formulas. | Public calibration UI only. |

---

## 2. Rules

- **Public metric profiles** (assets/public/public_metric_profiles.json) define the subsets. Each profile lists metric ids and optional display names; only these may appear in public reports and API responses.
- **Projection layer** maps internal outputs to public metric ids when emitting. Internal-only metrics are never projected.
- **No complete map** of internal math (dependency graph, layer order, formula list) is ever exposed in public artifacts or docs.

---

## 3. Acceptance Criterion

External users never see the complete internal math picture. They see only selected interpretable outputs under public metric profiles.
