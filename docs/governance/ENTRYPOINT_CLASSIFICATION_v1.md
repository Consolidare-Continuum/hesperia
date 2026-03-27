# ENTRYPOINT CLASSIFICATION v1

**Status:** Active  
**Purpose:** Every runner and CLI has a declared status and allowed runtime mode. Public bundle exposes only product-shaped commands.

---

## 1. Public entry points (exposed in release; façade-only)

| Entry point | Component | Allowed mode | Description |
|-------------|--------|--------------|-------------|
| Structural measurement (full) | runtime.pipeline.run_l1_through_l9 | public_runtime, internal_review, internal_debug | Single-text measurement; optional profile, dossier, validation. |
| Structural measurement (canonical) | runtime.runners.run_reference_pipeline | public_runtime | Same as above; canonical CLI. |
| L1+L2 only | runtime.pipeline.run_l1_l2 | public_runtime | Reduced stages. |
| L1+L2+L3 only | runtime.pipeline.run_l1_l2_l3 | public_runtime | Reduced stages. |
| Values output | runtime.pipeline.run_sphere_math_values | public_runtime | One JSON per run. |
| Batch (100 sentences) | runtime.pipeline.run_sphere_math_100_sentences | public_runtime | Multiple texts, one JSON. |
| E2E all | runtime.pipeline.run_e2e_all | internal_review, internal_debug | Runs multiple E2E flows; uses service for L1–L9 and domain_metrics. |

All of the above **must** import only **core.services**, **core.projection**, **runtime.artifact_writer**, **runtime.dossier**, **runtime.provenance** (no direct core.layers, sphere.execution_flow, core.attribution).

---

## 2. Internal-review entry points (excluded from public package or not documented as primary)

| Entry point | Component | Reason |
|-------------|--------|--------|
| Analyze (attribution + R1–R4) | runtime.pipeline.analyze | Uses core.attribution, core.math, core.propagation; not yet migrated to a service. |
| R1–R4 execution_flow | runtime.pipeline.r1_r4_pipeline | Uses core.attribution, core.layers, core.propagation. |
| Batch runner | runtime.pipeline.batch_runner | Uses core.layers.load_defaults; used by internal flows. |
| Reading scales | runtime.pipeline.reading_scales | Uses core.layers; internal calibration tooling. |
| Corpus benchmark | runtime.pipeline.run_corpus_benchmark | Uses sphere.execution_flow; benchmark only. |

These are **excluded** from the import-boundary check (EXCLUDED_FILES in tools/check_import_boundary.py). They must **not** be listed as primary public commands in release docs or help.

---

## 3. Internal debug / dev-only

| Entry point | Component | Notes |
|-------------|--------|--------|
| E2E sentence | runtime.pipeline.run_e2e_sentence | Calls analyze(); internal. |
| E2E R1–R4 | runtime.pipeline.run_r1_r4_pipeline | Internal. |
| Run R1–R4 execution_flow | runtime.pipeline.run_r1_r4_pipeline | Internal. |

---

## 4. Allowed mode summary

- **public_runtime:** Only façade-based runners; no internal layer orchestration; all writes via artifact_writer; projection applied.
- **internal_review:** May run E2E and internal runners; still no raw internal writes in default config unless explicitly enabled.
- **internal_debug:** Full visibility; internal docs and traces allowed.

---

## 5. Release content policy (alignment)

Per RELEASE_CONTENT_POLICY_v1: the public/sealed runtime package must **exclude** internal-review and internal debug entry points from the advertised entry-point list and from default help. Packaging exclude list should include any script that is not in the “Public entry points” table above as a primary command (or document them as “advanced/internal” only).

---

## 6. Done condition

Every runner has a declared status (public / internal-review / internal debug). Public bundle exposes only product-shaped commands; reflective runners are internal-only or hidden from release.
