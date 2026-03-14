# Release content verification v1

**Status:** Active  
**Purpose:** Run package content inspection against the exclusion list. Confirm no source, no internal docs, no mixed runners, no debug tools in the release bundle.

---

## 1. What the bundle must contain only

- CLI binary (hesperia-cli.bin or hesperia-cli/ directory).
- API image tar (hesperia-api-image.tar).
- Examples (e.g. examples/*.json).
- Public schema (e.g. assets/public/public_output_schema.json or copy).
- Quickstart (release/README.md or equivalent).
- Limitations statement.
- Manifest (release/manifest.json).
- Checksums (release/checksums.txt).

---

## 2. Exclusion list (verify absent)

Run this checklist against the unpacked bundle or the contents of the zip/tarball:

| Item | Expected |
|------|----------|
| **Source code** | No full repo; no Python source tree (e.g. no core/, runtime/ as editable source). CLI is a binary; API is in the image. |
| **Internal docs** | No docs/internal/; no MATH_LAYER_REGISTRY, PIPELINE_LAYER_REGISTRY. |
| **Mixed runners** | No scripts named run_l1_l2, run_e2e_all, run_sphere_math_values, etc. as part of the bundle. (If a tarball includes repo copy by mistake, those must not be advertised.) |
| **Debug tools** | No layer dumps, trace scripts, *_dump_*.py, debug_*.py. |
| **Specs history** | No docs/archive/specs_history/ or internal method specs in bundle. |
| **Raw dictionaries** | No unprojected Dict A/B or ontology build artifacts. |
| **Topology helpers as public API** | No doc or schema that exposes AREA_FAMILY_MAP, area/family counts. |
| **Math registries** | No doc that lists layer formulas or transformation chain. |

---

## 3. Procedure

1. Build the release (./build_shipping.sh all).
2. Unpack or list the evaluator bundle (e.g. contents of release/ + dist/ + examples/).
3. For each exclusion item, confirm it is absent (or not advertised).
4. Record PASS/FAIL per item.

---

## 4. Done condition

**Done when:** No source, no internal docs, no mixed runners, no debug tools in the release bundle. Package content inspection passes against the exclusion list.
