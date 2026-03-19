# SHIPPING EXCLUSION LOCK v1

**Status:** Locked  
**Purpose:** Explicit exclusion list for the release bundle. Checklist is exact, not vague.

---

## 1. Excluded material (must never be in the release bundle)

| Category | Path / content | Rule |
|----------|----------------|------|
| **Internal docs** | docs/internal/ | No MATH_LAYER_REGISTRY, PIPELINE_LAYER_REGISTRY, or any doc under docs/internal/. |
| **Specs history** | legacy/docs/specs_history/, any draft or historical spec that describes internal geometry, formulas, or pipeline order | No specs history in bundle. |
| **Internal review runners** | Scripts/modules: analyze.py, r1_r4_pipeline.py, batch_runner.py, reading_scales.py, run_corpus_benchmark.py, run_e2e_all, run_l1_l2, run_l1_l2_l3, run_sphere_math_values, run_reference_pipeline | Not advertised; not present as primary entry points in bundle. CLI binary has no source; image has no advertised entry point for these. |
| **Debug tools** | Layer dumps, propagation path export, internal trace scripts, *_dump_*.py, debug_*.py | None in bundle. |
| **Raw dictionaries** | Unprojected Dict A / Dict B or build artifacts that expose family placement, ontology construction | None in bundle. |
| **Topology helpers** | core/topology/invariant_catalog (as public API), AREA_FAMILY_MAP, CANONICAL_AREA_SET, or any module that exports internal area/family counts to callers | Not exposed in bundle. Image may contain code for runtime but no docs or schemas that expose topology. |
| **Math registries** | docs/internal/MATH_LAYER_REGISTRY*, PIPELINE_LAYER_REGISTRY*, or any doc that lists layer formulas, dependency graph, or transformation chain | None in bundle. |
| **Reflective governance** | Governance docs that describe internal method (layer count, topology, bridge, propagation) and are not meant for release | Only public-facing governance (e.g. PUBLIC_VOCABULARY_MAP, quickstart, limitations) in bundle. |

---

## 2. Release bundle checklist (exact)

Before tagging or shipping, verify:

- [ ] **docs/internal/** — Not in bundle. (Bundle has no source tree; if any doc is included, it is not from docs/internal.)
- [ ] **Specs history** — Not in bundle.
- [ ] **Internal review runners** — Not advertised; not present as entry points in CLI help or API docs.
- [ ] **Debug tools** — Not in bundle.
- [ ] **Raw dictionaries** — Not in bundle.
- [ ] **Topology helpers** — Not exposed (no public API or doc that exposes AREA_FAMILY_MAP, area/family counts).
- [ ] **Math registries** — Not in bundle.
- [ ] **Reflective governance** — Only release-intended governance in bundle; no internal method docs.

---

## 3. Docker build exclusion

When building the API image (Dockerfile.shipping), use .dockerignore so that the build context does not send:

- docs/
- legacy/
- tests/
- tools/
- .git/

Final image must not contain build toolchain or docs tree. Copy only runtime, core, lexicon, assets as in Dockerfile.shipping.

---

## 4. Done condition

**Done when:** Release bundle checklist is exact and verified; no source, no internal docs, no mixed runners, no debug tools, no raw dicts, no topology helpers, no math registries, no reflective governance not meant for release.
