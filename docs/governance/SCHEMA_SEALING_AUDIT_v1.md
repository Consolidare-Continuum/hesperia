# SCHEMA SEALING AUDIT v1

**Status:** Complete  
**Purpose:** Ensure public schemas do not teach internal geometry. A schema reader cannot infer internal structure.

---

## 1. Audited Artifacts

| Artifact | Role | Geometry-revealing? | Action |
|----------|------|----------------------|--------|
| `specs/canon/usf_schema.json` | Internal USF shape (raw metrics) | Yes: area_vector, family_counts, dominant_area, dominant_family, propagated_*, max lengths imply 12/288 | **Internal-only.** Do not expose to public API. Public output must conform to `assets/public/public_output_schema.json` instead. |
| `specs/schemas/r1_r4/Unit.schema.json` | R1–R4 unit output | Yes: top_areas, top_families, area_id (A\d+), family_id (F\d+), maxItems 12, 288 | **Internal / protected.** For public API use public vocabulary: top_macro_domains, top_policy_families, macro_domain_id, policy_family_id, maxItems 10, 240. |
| `specs/schemas/r1_r4/BookProfile.schema.json` | Book profile composite | Partial: structural_signature.stable_families pattern F\d+ | For public: use policy_family_id or opaque labels; cap at 240. |
| `specs/schemas/r1_r4/SI_metrics.schema.json` | Scalar metrics | No | **Safe.** No topology; keep as-is for public. |

---

## 2. Public Schema Definition

- **`assets/public/public_output_schema.json`** — Defines the allowed public output shape:
  - `macro_domain_vector` (length 10), `policy_family_counts` (length 240)
  - `dominant_macro_domain` (0–9), `dominant_policy_family` (0–239)
  - Propagated variants same; no area_vector, family_counts, side_id, or 12/288 semantics
  - Evidence: matched_span, concept_or_family_label, confidence_band, document_location only

- **`assets/public/public_ontology_map.json`** — Key mapping and forbidden terms; used by projection layer.

---

## 3. Rules Going Forward

- Any **public** API response or report schema must reference `public_output_schema.json` or use only public vocabulary (see PUBLIC_VOCABULARY_MAP_v1.md).
- Internal schemas (USF raw, Unit with 12/288) remain in use for pipeline internals but must not be exposed as the contract for external consumers.
- New schemas: if they describe output visible to operators or API consumers, they must use public vocabulary and public counts (10 macro-domains, 240 policy families).

---

## 4. Acceptance Criterion

**A schema reader cannot infer internal geometry.** Public schemas do not mention area count 12, family count 288, side_id, hex, sphere, topology, or coordinate semantics. Public output schema uses only macro_domain_*, policy_family_*, and scalar metrics.
