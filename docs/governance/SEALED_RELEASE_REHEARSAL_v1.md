# SEALED RELEASE REHEARSAL v1

**Status:** Dry run checklist  
**Purpose:** A third party using the runtime cannot reconstruct the method from the shipped bundle and emitted artifacts.

---

## 1. What Is Included (Check)

- [ ] **Files included** — List all files in the release bundle. Verify no docs/internal/, no MATH_LAYER_REGISTRY, no PIPELINE_LAYER_REGISTRY, no raw invariant_catalog export to public.
- [ ] **Entry points visible** — Only: run_structural_analysis (via core.services), run_l1_through_l9, run_reference_pipeline, run_e2e_all, etc. No entry point that exposes compute_L* or bridge directly.
- [ ] **Outputs emitted** — Every JSON/file write goes through write_public_json or apply_public_projection. No raw L1–L9 dict in any artifact. Audit manifest only has public-safe keys.
- [ ] **Logs** — No log line in the default path that prints layer names, topology, or formula ids. Stderr from runners may mention "output written to" path only.
- [ ] **Schemas exposed** — Only assets/public/*.json (public_output_schema, public_audit_manifest.schema, public_ontology_map, public_metric_profiles). No spec that teaches 12 areas, 288 families, or layer order.
- [ ] **Docs exposed** — Only public narrative (ingest → structural analysis → evidence → comparison → report). No internal pipeline registry or math registry.

---

## 2. Rehearsal Steps

1. Build the release bundle per RELEASE_CONTENT_POLICY (exclusion list applied).
2. Unpack in a clean directory; list every file. Check no internal doc or registry is present.
3. Run one entry point (e.g. run_l1_through_l9 --text "sample") and capture stdout + written file. Confirm output contains no area_vector, family_counts, L1…L9 raw keys, side_id, or 12/288 semantics.
4. Run run_e2e_all (or subset); confirm all artifact files are projected (macro_domain_vector, policy_family_counts, etc.).
5. Inspect logs (if any) for reflective strings; confirm none.

---

## 3. Done Condition

A third party using the runtime cannot reconstruct the method from the shipped bundle and emitted artifacts. Rehearsal checklist is executed and signed off (or gaps recorded for fix).
