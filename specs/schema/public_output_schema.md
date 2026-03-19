---
spec_version: "1.0"
system_version: "0.5.0"
status: canonical
id: HES-SPEC-SCHEMA-PUBLIC-OUT
---

# Public output schema — canonical (normative mirror)

**Machine-readable source of truth:** `schemas/public/public_output_schema.json` (JSON Schema draft 2020-12).  
**Legacy path:** `assets/public/public_output_schema.json` → symlink to the same file.

If this markdown disagrees with the JSON file, **the JSON file wins** and this document must be updated in the same change set.

## 1. Root object

- **type:** object; `additionalProperties` allowed for forward-compatible payloads.
- **schema_version** (root meta): `1.1` in JSON `$comment` sense; public trace id is field **`schema_version`** below.

## 2. Trace & envelope (required for shipped JSON)

| Field | Type | Constraint |
|-------|------|------------|
| `system_version` | string | Must match `VERSION.yaml` `system_version` |
| `build_id` | string | Build/run trace |
| `schema_version` | string | e.g. `v1` from `VERSION.yaml` `schema.public_output` |
| `calibration_profile` | string | e.g. `v0_5_0` |
| `pipeline_version` | string | optional on some surfaces |
| `run_id` | string | optional |
| `modules_used` | array of string | optional |
| `payload` | any | optional wrapper for list roots |

## 3. Projected structural fields (when present)

| Field | Type | Constraint |
|-------|------|------------|
| `macro_domain_vector` | array number | length **10**, values in **[0,1]** |
| `policy_family_counts` | array number | length **240**, ≥ 0 |
| `dominant_macro_domain` | integer | 0–9 |
| `dominant_policy_family` | integer | 0–239 |
| `propagated_macro_domain_vector` | array number | length 10, **[0,1]** |
| `propagated_policy_family_counts` | array number | length 240, ≥ 0 |
| `entropy`, `coverage`, `tension`, `loopability`, `confidence` | number | — |
| `trust_tier` | string | — |
| `evidence` | array object | entries: `matched_span`, `concept_or_family_label`, `confidence_band`, `document_location` (strings) |

## 4. Forbidden in public keys/values

Sealed-runtime guard forbids leaking internal topology tokens (hex, side_id, internal layer ids, etc.) — see `runtime/shipping/schema_guard.py` and product vocabulary maps.

## 5. Version linkage

Any incompatible change to required trace fields or projected arrays → bump `VERSION.yaml` `schema.public_output` and `schema_version` in the JSON artifact per [../system/versioning_and_governance.md](../system/versioning_and_governance.md).
