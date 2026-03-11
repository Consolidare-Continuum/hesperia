# HESPERIA Dossier Schema v1.0 (HSD_v1.0)

This document defines the canonical structure of HESPERIA dossier artifacts. Dossiers are deterministic, checksummed JSON outputs suitable for reproducibility, comparison, and audit.

## Top-level structure

A dossier is a JSON object with one of two shapes: **single-run** (one pipeline execution) or **multiscale** (R1–R4 reading scales). Both share metadata and governance-related fields where present.

### Common / multiscale top-level keys

| Key | Type | Required | Description |
|-----|------|----------|-------------|
| **meta** | object | yes (when writing) | Metadata block (see below). Required for written dossiers; must include engine_version and generation_timestamp. |
| **schema_version** | string | yes (after write) | Schema identifier, e.g. `"HSD_v1.0"`. |
| **dossier_checksum** | string | yes (after write) | SHA256 hex (64 chars) of canonical JSON with this field empty. |
| **R1** | array | multiscale only | Segment entries at reading scale R1 (sentences). |
| **R2** | array | multiscale only | Segment entries at reading scale R2 (paragraphs). |
| **R3** | array | multiscale only | Segment entries at reading scale R3 (sections). |
| **R4** | array | multiscale only | Segment entries at reading scale R4 (document). |
| **global_structure** | object | multiscale only | Aggregated structural summary (see below). |
| **governance** | object | optional | Summary of governance/decision fields (e.g. L7/L9) for reporting. |

### Single-run top-level keys

| Key | Type | Required | Description |
|-----|------|----------|-------------|
| **run** | string | yes | Run identifier, e.g. `"L1_through_L9"`. |
| **text_preview** | string | yes | Short preview of input text. |
| **L1** … **L9** | object | yes | Layer output objects (34_SPEC–42_SPEC). |
| **diagnostics** | object | yes | Per-layer and Δ stability diagnostics. |

---

## Meta

When present (inline or under `meta`). For written dossiers, **meta** is required and must include **engine_version** and **generation_timestamp**.

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| **schema_version** | string | yes | `"HSD_v1.0"`. |
| **dossier_checksum** | string | yes (after write) | SHA256 of canonical payload (checksum field empty). |
| **generation_timestamp** | string | yes | ISO 8601 UTC timestamp when dossier was generated (e.g. `2026-03-11T14:32:05Z`). |
| **engine_version** | string | yes | HESPERIA engine version (from pyproject.toml or git commit). |
| **pipeline_version** | string | no | Pipeline identifier, e.g. `"L1-L9"`. |
| **python_version** | string | no | Python version at generation time. |
| **run_manifest** | object | no (yes when written) | Execution parameters for reproducibility (see below). |
| **dossier_id** | string | no (yes after write) | Content-addressed id: first 12 hex chars of dossier_checksum (e.g. `a9f4c2d91b73`). Excluded from checksum input. |

### meta.run_manifest

When present (written dossiers), records how the run was invoked:

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| **policy_mode** | string | yes | Π interpretation policy mode used. |
| **profile_id** | string | no | L1 structure profile identifier if profile was loaded. |
| **assets_root** | string | no | Path to lexicon/assets root. |
| **defaults_used** | object | no | Copy of defaults dict (F, A, eps, etc.) used for the run. |
| **cli_arguments** | object | no | Serialized CLI args (text, out, profile, policy_mode, write_dossier, validate_dossier). |

---

## Global structure (multiscale)

Required when dossier is multiscale. All fields are required within `global_structure`.

| Field | Type | Description |
|-------|------|-------------|
| **dominant_area_distribution** | object | Map area id (string) → ratio (number). Proportion of segments per dominant area. |
| **stable_family_core** | array of number | Family IDs that appear as dominant in >25% of segments. |
| **tension_axes** | array of number | Distinct dominant area IDs (axes of variation). |
| **confidence_profile** | object | Contains `mean_confidence`, `min_confidence`, `max_confidence` (numbers), `trust_tag_distribution` (object). |
| **document_anomaly** | number | Mean of segment Δ stability layer `anomaly_score`. |

---

## Segment entry schema (R1–R4 elements)

Each element in **R1**, **R2**, **R3**, **R4** is an object with:

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| **L1** | object | yes | Layer 1 output (34_SPEC). |
| **L2** | object | yes | Layer 2 output (35_SPEC). |
| **L3** | object | yes | Layer 3 output (36_SPEC). |
| **L4** | object | yes | Layer 4 output (37_SPEC). |
| **L5** | object | yes | Layer 5 output (38_SPEC). |
| **L6** | object | yes | Layer 6 output (39_SPEC). |
| **L7** | object | yes | Layer 7 output (40_SPEC). |
| **L8** | object | yes | Layer 8 output (41_SPEC). |
| **L9** | object | yes | Layer 9 output (42_SPEC). |
| **diagnostics** | object | yes | Per-layer diagnostics and `stability` (Δ) when present. |

Optional: **run**, **text_preview** for compatibility with single-run segment shape.

---

## Canonical serialization

- **Deterministic JSON**: `sort_keys=True`, `indent=2`, `ensure_ascii=False`.
- **Checksum**: SHA256 of the UTF-8 encoding of the canonical JSON with `dossier_checksum` set to `""`.

---

## Version

- **Schema version**: HSD_v1.0
- **Document**: dossier_schema_v1.md
