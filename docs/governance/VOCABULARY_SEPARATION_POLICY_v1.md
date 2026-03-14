# VOCABULARY SEPARATION POLICY v1

**Status:** Active  
**Purpose:** Prevent future leaks by habit. Every repo zone has an allowed vocabulary class.

---

## 1. Three Vocabulary Classes

### A. Internal vocabulary

- **Definition:** Real architecture language (sphere, hex, hexagon, area, family, side_id, topology, 3D, coordinate map, area lattice, propagation surface, etc.).
- **Where allowed:** Internal docs (marked internal-only), sealed core code, internal-only modules, internal debug tooling.
- **Where forbidden:** Public API, public docs, configs, schemas, reports, logs visible to operators, calibration review outputs (unless internal-only mode).

### B. Protected engineering vocabulary

- **Definition:** Neutral but still technical (structural node, macro-domain, policy family, relation structure, structural position, relation spread, directional structural signal).
- **Where allowed:** Limited engineering surfaces (e.g. internal config for experts, internal schemas, internal dashboards). Not for end-user product copy.
- **Where forbidden:** End-user-facing API field names, public reports, marketing or product docs.

### C. Public vocabulary

- **Definition:** Pure product-facing language. Concepts only: evidence, confidence, concept match, emphasis, similarity, divergence, contradiction, implementation gap. No structural or geometric hints.
- **Where allowed:** API responses, public docs, reports, config help text, operator-facing logs (when not debugging), schemas exposed to consumers.
- **Where forbidden:** Must never contain internal or protected-engineering terms that reveal topology (e.g. "macro-domain" may be allowed in some public contexts; "area" or "hex" never).

---

## 2. Zone → Allowed Vocabulary

| Zone | Allowed vocabulary |
|------|---------------------|
| `core/` (sealed internals) | Internal only |
| `hesperia/engine/kme/` (sealed) | Internal only |
| `runtime/` (API surface) | Public only at boundary; internal in implementation |
| Public API response bodies | Public only |
| Public JSON schemas (API, report) | Public only |
| Config files (user/operator editable) | Public only |
| Report generators output | Public only (after projection) |
| `docs/` (public-facing) | Public only |
| `docs/` (internal-only subdir or marked files) | Internal or protected engineering |
| `assets/public/` | Public only |
| `assets/reserve/` | Internal only (not exposed) |
| Logs (external/operator) | Public only |
| Logs (internal debug) | Internal allowed |
| Calibration review (external) | Public only |
| Evidence trace (public) | Public only; see PUBLIC_EVIDENCE_TRACE_POLICY |

---

## 3. Forbidden Crossovers

The following must never appear in the stated context:

| Forbidden | Context |
|-----------|---------|
| "hex", "hexagon", "cell" | Public schemas, API fields, reports |
| "sphere" | Public reports, configs, docs |
| "12 areas", "area count", "288 families" | Public comments, docs, API descriptions |
| "side_id" | Public artifacts (unless renamed to e.g. "internal_relation_id" and abstracted so semantics are opaque) |
| "topology", "geometry", "lattice" | Public API, reports, config keys |
| "propagation" (as internal mechanism) | Public output; use "relation spread" or omit |
| Raw internal indices (area 10/11, family 240–287) | Any public artifact |
| "coordinate", "adjacency" | Public schemas and outputs |
| Layer names (L1–L9 as internal pipeline) | Public API or report fields |
| "reserved area", "reserve" | Public ontology or outputs |

---

## 4. Enforcement

- **Code review:** Check that any new public-facing field or doc uses PUBLIC_VOCABULARY_MAP and this policy.
- **Projection layer:** All data that leaves the sealed core for public consumption must pass through the public projection layer; no raw internal indices or internal terms in output.
- **Schema audit:** Public schemas must be audited (and re-audited on change) to ensure no geometry-revealing names or descriptions.

---

## 5. Acceptance Criterion

Every repo zone has a defined allowed vocabulary class. No public-facing artifact may use internal vocabulary; no internal-only artifact is required to use public vocabulary.
