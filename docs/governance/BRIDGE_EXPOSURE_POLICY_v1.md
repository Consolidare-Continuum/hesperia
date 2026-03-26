# BRIDGE EXPOSURE POLICY v1

**Status:** Active  
**Purpose:** The bridge can be used through service calls but not learned from exposed materials. Prevent reflection on how semantic material becomes structural form.

---

## 1. Must Be Hidden

- **Hit-to-node construction doctrine** — How matched tokens become graph nodes or concept hits.
- **Relation synthesis rules** — How relations are derived from matches or structure.
- **Adjacency/expansion logic** — How the graph is expanded or traversed.
- **Structural compression/expansion steps** — Any internal reshape or aggregation.
- **Bridge heuristics** — Tie-breaking, placement, or scoring details that reveal method.

---

## 2. May Be Public (Wording Only)

- “Ontology-grounded structural mapping.”
- “Evidence-backed relation modeling.”
- High-level only: “structural measurement,” “concept activation,” “evidence extraction.” No implementation detail.

---

## 3. Enforcement

- **No public artifact** (report, API response, log, schema, or doc) may describe or expose bridge internals.
- **Service façade** — Public runtime calls `run_structural_analysis` or equivalent; the bridge is invoked inside the sealed core and never exposed by name or by intermediate state.
- **Serialization** — Bridge outputs (hit-to-node map, relation synthesis intermediates) are never written in public mode; see RUNTIME_MODE_POLICY and MATH_SERIALIZATION_POLICY.

---

## 4. Acceptance Criterion

The bridge can be used through service calls but not learned from exposed materials. No document or artifact teaches hit-to-node doctrine, relation synthesis rules, or adjacency/expansion logic.
