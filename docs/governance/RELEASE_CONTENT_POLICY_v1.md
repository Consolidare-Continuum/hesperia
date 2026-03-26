# RELEASE CONTENT POLICY v1

**Status:** Active  
**Purpose:** Building the public/sealed runtime package must not include internal knowledge by accident.

---

## 1. Packaging Exclusion Rules

The following must **never** be included in the packaged/runtime-distributed artifact:

- **Internal docs:** docs/internal/ (MATH_LAYER_REGISTRY, PIPELINE_LAYER_REGISTRY, etc.)
- **Internal registries:** assets/reserve/ (reserved_areas, reserved_families, reserved_hex) — or ship only as data with no schema that reveals structure
- **Debug tooling:** Any script or component whose sole purpose is to dump layer state, propagation path, or bridge internals
- **Reflective specs:** Specs that describe layer order, formulas, topology geometry (e.g. legacy specs under legacy/docs/specs_history that teach the model)
- **Raw topology helpers:** core/topology/invariant_catalog.py — or ship only in a form that does not export AREA_FAMILY_MAP, CANONICAL_AREA_SET to public
- **Development-only scripts:** One-off migration scripts, internal calibration builders (unless explicitly needed for operator)

---

## 2. What the Release Bundle May Include

- **runtime/** — Entry points, artifact_writer, public_reports, dossier (with projection), provenance
- **core/projection/** — Public projection layer
- **core/services/** — Service façades
- **core/topology/reserve_loader** — For projection filtering only; no export of topology names
- **assets/public/** — public_ontology_map, public_output_schema, public_metric_profiles, public_audit_manifest.schema
- **docs/public/** (if created) — User-facing docs only (narrative, calibration, API)
- **Selected governance docs** — PUBLIC_VOCABULARY_MAP, PUBLIC_PIPELINE_NARRATIVE, PUBLIC_AUDIT_POLICY (no internal registries)

---

## 3. Packaging Manifest / Exclusion Config

Use an exclusion list (e.g. in packaging script or pyproject.tools):

```
exclude:
  - docs/internal/
  - legacy/docs/specs_history/
  - assets/reserve/   # or include with no schema doc
  - legacy/
  - tools/sealing_scan.py  # optional: dev-only
  - tools/check_import_boundary.py  # optional: dev-only
```

Include only:

- runtime/ (excluding __pycache__, *.pyc)
- core/projection/, core/services/, core/topology/reserve_loader.py (and deps as needed)
- assets/public/
- docs/public/ (if present)
- Optional: selected docs/governance/*.md (public-facing only)

---

## 4. Done Condition

Building the public/sealed runtime package does not include internal knowledge by accident. Exclusion rules and release content policy are documented and applied in the build.
