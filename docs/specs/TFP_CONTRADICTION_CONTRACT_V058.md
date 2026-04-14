# TFP Contradiction Contract v0.5.8

Purpose: define one canonical contradiction contract across activation/topology/DLCR/multiscale/product/inspector so v0.5.8 does not drift into ad hoc field semantics.

## Scope

- Pipeline artifacts: `04_dlcr_full.json`, `05_sealed_multiscale.json`, `06_product_analyze.json`, `09_session_topology.json`, `20_main_engine_full_context.json`, `99_tfp_bundle_inspect.json`, consolidation manifest (`CONSOLIDATION_MANIFEST.json` or `00_manifest.json` compatibility path).
- Contract validator: `hesperia/extensions/triz/contradiction_contract.py`.
- Inspector authority: `tools/inspect_tfp_bundle_output.py`.

## Canonical field groups

### A) Core contradiction metrics

- `raw_contradiction_load`
- `effective_contradiction_load`
- `contradiction_confidence_mean`
- `global_contradiction_load`
- `cross_area_contradiction_mass`

No synonyms are allowed for these meanings.

### B) Structural contradiction metrics

- `area_contradiction_pressure`
- `family_contradiction_pressure`
- `family_fragmentation_summary`
- `family_cross_area_bridge_mass`
- `family_intra_area_conflict_mass`

### C) Dynamic contradiction metrics

- `segment_contradiction_loads`
- `transition_pressure`
- `activation_conflict_load`
- `latent_conflict_load`

### D) Qualification metrics

- `uncertainty_adjusted_conflict_index`
- `lexical_semantic_conflict_split`
- `runtime_vs_calibration_conflict_split`
- `contradiction_mode_summary`

### E) Product/governance metrics

- `conflict_integrity_score`
- `promotion_conflict_verdict`
- `release_conflict_gates`
- `conflict_release_summary`

## Field ownership model

For all canonical core/structural/dynamic/qualification fields:

- **Authoritative producer:** `hesperia/extensions/triz/crossplane_contradiction.py` (exported in `04_dlcr_full.json` under `crossplane_contradiction_package`, mirrored in `20_main_engine_full_context.json` under `crossplane_contradiction_by_session`).
- **Primary machine integration artifact:** `20_main_engine_full_context.json`.
- **Secondary derived consumers:** `runtime/pipeline/analyze.py`, `tools/inspect_tfp_bundle_output.py`, `hesperia/extensions/triz/conflict_release_gating.py`.
- **Required status:** required when `contradiction_coupling_active=true`; optional (shape may remain sparse) when `false`.

For product/governance fields:

- **Authoritative producer:** `tools/inspect_tfp_bundle_output.py`.
- **Primary authority artifact:** `99_tfp_bundle_inspect.json`.
- **Derived summary allowed in:** `20_main_engine_full_context.json`, `00_manifest.json`/`CONSOLIDATION_MANIFEST.json`.

`06_product_analyze.json` is explicitly consumer-facing summary and is not authoritative for canonical core field values.

## Artifact responsibilities

- `04_dlcr_full.json`: carries contradiction package (`crossplane_contradiction_package`) and DLCR alignment.
- `05_sealed_multiscale.json`: carries multiscale contradiction trace (`sealed_conflict_trace`) and derived consistency.
- `06_product_analyze.json`: carries condensed product-level contradiction interpretation (including `release_conflict_readiness`), no canonical core authority.
- `09_session_topology.json`: topology/dynamics authority (`segment_contradiction_loads`, `transition_pressure`, segment fragmentation summaries).
- `20_main_engine_full_context.json`: canonical integration surface for contradiction package + release summary + contract summary.
- `99_tfp_bundle_inspect.json`: release interpretation authority (`PASS`/`QUALIFIED_PASS`/`FAIL`) plus contract validation outputs.
- `CONSOLIDATION_MANIFEST.json` / `00_manifest.json`: bundle-level declaration of contradiction contract version and status.

## Validation rules

Validator entry point: `validate_contradiction_contract(bundle_payloads: dict)`.

Checks:

- required artifacts present;
- required canonical fields present when coupling active;
- deprecated/forbidden synonym fields;
- authority conflicts for canonical values across artifacts;
- product artifact attempting canonical authority.

Inspector exports:

- `contradiction_contract_valid`
- `missing_required_contradiction_fields`
- `deprecated_contradiction_fields_found`
- `authority_conflicts`
- `contract_recommended_action`

## Release gating interaction

- Contract validation is anti-drift governance.
- Conflict integrity gating (`conflict_integrity_score`, `promotion_conflict_verdict`, `release_conflict_gates`) remains release decision semantics.
- Both are required for clean promotion in v0.5.8.

## Backward compatibility

1. If `contradiction_coupling_active=false`, contradiction sections may be sparse/empty, but artifact shape remains valid.
2. Older bundles without v0.5.8 contract fields return `contract_valid=false` with compatibility notes (no parser crash).
3. Field names must not be silently renamed.
4. Any contradiction-field change must update spec version, field registry, and validator.

## Deprecation policy

- Forbidden aliases: `conflict_score`, `tension_score`, `semantic_conflict_score`, `conflict_pressure`, `contradiction_pressure`, `semantic_tension`.
- New aliases are not allowed unless explicitly added to the registry with temporary migration window and explicit removal version.

## Example manifest block

```json
{
  "contradiction_contract": {
    "spec_version": "v0.5.8",
    "contract_valid": true,
    "authoritative_artifact": "20_main_engine_full_context.json",
    "inspection_artifact": "99_tfp_bundle_inspect.json"
  }
}
```

