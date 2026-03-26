# PUBLIC PIPELINE NARRATIVE v1

**Status:** Active  
**Purpose:** Public-facing documentation stays product-shaped, not engine-shaped. No 10 explicit internal stages, no bridge specifics, no layer propagation model, no topology synthesis sequence.

---

## 1. Public Narrative (Only This)

The system is described in public docs and API as follows:

1. **Ingest text** — User supplies text, paragraph, or corpus.
2. **Structural measurement** — The engine performs ontology-grounded structural measurement (no further detail).
3. **Evidence extraction** — Matched concepts and evidence-backed relation modeling produce evidence.
4. **Comparison / divergence evaluation** — Structural comparison and divergence metrics are computed.
5. **Report generation** — Public reports, evidence trace, and selected metrics are produced.

---

## 2. What Must Not Appear in Public Docs

- Ten explicit internal stages or layer names (L1–L10).
- Bridge layer specifics (hit-to-node, relation synthesis rules, adjacency).
- Layer propagation model or transformation chain.
- Topology synthesis sequence or coordinate system.
- Math-layer dependency graph or formula list.
- Reserved areas, family count 288, area count 12 (internal only).

---

## 3. Wording Allowed

- “Ontology-grounded structural mapping.”
- “Evidence-backed relation modeling.”
- “Structural measurement,” “evidence extraction,” “comparison,” “report generation.”
- “Calibration profile,” “report profile,” “public metric profile.”

---

## 4. Acceptance Criterion

Public-facing documentation stays product-shaped, not engine-shaped. A reader cannot reconstruct the full transformation chain or internal execution_flow from public docs.
