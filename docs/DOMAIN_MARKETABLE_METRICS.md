# HESPERIA — Marketable Derived Metrics (14)

**Purpose:** Define the subset of derived metrics used for **dashboards, reports, and external users**. The full engine computes 35 derived metrics; this document describes the 14 chosen for **market-facing** use.

**Reference:** Full technical definitions and formulas: `docs/DOMAIN_METRICS_REFERENCE.md` (§3 Derived Metrics, §4 Marketable subset). Code list: `core/domain/fingerprint.py` → `MARKETABLE_DERIVED_ORDER`.

---

## Selection criteria

From the 35 derived metrics, only a subset is realistically **usable and marketable**. Criteria:

1. **Interpretability** — Non-technical users understand it quickly.
2. **Non-redundancy** — Avoid obvious algebraic duplicates.
3. **Business meaning** — Useful for comparing texts, theories, or domains.
4. **Dashboard clarity** — Each metric answers a distinct question.

**Summary:** 14 strong market-facing metrics. The remaining 21 are **engineering diagnostics**: useful internally, not required for external storytelling.

---

## Summary by category

| Category | Metrics | Count |
|----------|---------|-------|
| **Knowledge Structure** | KDI, KNS, KCR, KBS | 4 |
| **Concept Spread & Coverage** | CSI, TBI, CDD | 3 |
| **Theory Quality** | TDS, TCI, SSS | 3 |
| **Knowledge Dynamics** | IDE, SPS | 2 |
| **Domain Character** | SPI, DCI | 2 |
| **Total market-facing** | | **14** |

---

## The 14 metrics (definitions)

### Knowledge Structure

- **KDI — Knowledge Density Index**  
  Measures how structurally dense and coherent the knowledge representation is.

- **KNS — Knowledge Network Strength**  
  Measures the overall structural strength of the concept network activated by the text.

- **KCR — Knowledge Compression Ratio**  
  Measures how efficiently logical structure is expressed per concept used.

- **KBS — Knowledge Balance Score**  
  Measures whether conceptual breadth and structural coherence are balanced.

### Concept Spread & Coverage

- **CSI — Concept Spread Index**  
  Measures how widely the text activates concepts across the domain.

- **TBI — Theory Breadth Index**  
  Measures the overall conceptual breadth achieved through propagation.

- **CDD — Concept Distribution Density**  
  Measures how densely concepts populate the conceptual space reached by propagation.

### Theory Quality

- **TDS — Theory Depth Score**  
  Measures how deeply ideas are developed through conceptual propagation.

- **TCI — Theory Cohesion Index**  
  Measures how tightly conceptual concentration and coherence bind the theory together.

- **SSS — Structural Stability Score**  
  Measures whether the conceptual structure holds together under expansion.

### Knowledge Dynamics

- **IDE — Idea Diffusion Efficiency**  
  Measures how effectively ideas propagate through the concept network.

- **SPS — Semantic Propagation Strength**  
  Measures how strongly coherence supports idea propagation.

### Domain Character

- **SPI — Specialization Index**  
  Measures how specialized the text is within a conceptual region.

- **DCI — Domain Complexity Index**  
  Measures how structurally complex the conceptual system expressed in the text is.

---

## Using the 14 in code and product

- **Dashboard / API:** Filter `DerivedMetrics` or `DomainFingerprint.derived_map` to keys in `MARKETABLE_DERIVED_ORDER` so only these 14 are shown.
- **Reports:** Use the category labels above for sectioning (Knowledge Structure, Concept Spread, etc.).
- **Tooltips / help:** Use the one-line definitions in this document.

All 14 are in **[0, 1]** and use the same formulas as in the full 35; they are a **subset**, not a different computation.
