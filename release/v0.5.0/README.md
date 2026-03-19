# HESPERIA Engine Dynamics — **v0.5.0** sealed release audit

This directory is the **Task 5 audit package**: proof of deterministic behavior, schema validation, capability boundaries, version alignment, and frozen public reference output.

## Regenerate

```bash
# Bitwise-stable reference JSON + hashes (recommended for a real seal):
export HESPERIA_RELEASE_BUILD_TIMESTAMP=2026-03-19T12:00:00Z

# Full test suite (required before `git tag v0.5.0`):
python3 tools/release/build_release_audit_v0_5_0.py

# Fast iteration (subset tests — not sufficient alone for tagging):
python3 tools/release/build_release_audit_v0_5_0.py --quick
```

**Canonical input:** `tests/fixtures/release_v0_5_0/canonical_input.txt` (UTF-8). Do not change without a version bump and full re-audit.

**Exit code:** `0` only if **all gates pass** (including **clean git tree**). Otherwise **do not tag** — see `audit_report.json` → `seal_decision.reasons_fail` and **`final_gate_status.json`** (`sealed`, `critical_checks`).

**Task 6 execution order:** `docs/CODEX_EXECUTION_CHECKLIST_v0_5_0_SEAL.md`.

---

## What HESPERIA v0.5.0 is (this release)

A **deterministic structural inspection / placement engine** with:

- Sealed **public projection** (internal geometry, raw Dict A/B dumps, calibration coefficients, and adjacency do not appear on product surfaces).
- **Evidence-bearing** public payloads where designed (schema + sanitizer).
- **Auditable** build: manifest, checksums, determinism and schema reports, pytest log.

It is **not** a general research distribution, notebook product, or unconstrained API.

---

## What is included (product / runtime)

| Area | Role |
|------|------|
| `core/` | Math, layers, propagation internals (not exposed raw). |
| `hesperia/engine/` | KME, hex outputs, dynamics hooks, **projection package**. |
| `hesperia/engine/projection/` | Mandatory `project_to_public` gate. |
| `runtime/shipping/` | Sealed API + CLI entry. |
| `runtime/services/analysis_service.py` | Single façade; always projects before return. |
| `schemas/public/public_output_schema.json` | Canonical JSON Schema (copied here as `schema.json`). |
| `VERSION.yaml` + `pyproject.toml` | Version authority (must agree at `0.5.0`). |

---

## What is excluded (product image / seal scope)

| Area | Status |
|------|--------|
| `research/` | Not copied in product Dockerfiles; excluded from product baseline. |
| Clinical / TFP stacks | Experimental; not baseline Engine Dynamics product. |
| Notebooks, demos | Not shipping artifacts. |
| TRIZ HTTP | Optional; off under strict product surface (Task 4). |

---

## Public surface (shipping API)

- `POST /analyze`, `/compare`, `/batch` (alias `/batch-analyze`), `GET /health`.
- OpenAPI/docs **disabled** on the shipping app.
- Optional `GET /version` only when explicitly enabled (capabilities / env — not part of the minimal three verbs).

GPT-style app (`runtime.api.main`) uses `/hesperia/*` paths but the same projection path through `run_structural_analysis`.

---

## Schema

- **Normative prose:** `specs/schema/public_output_schema.md`
- **Machine JSON Schema:** `schema.json` in this folder (copy of repo `schemas/public/public_output_schema.json`)

`schema_validation_report.json` records **jsonschema** validation of:

- frozen **analyze** reference (`e2e_reference_output.json`),
- **compare** envelope,
- **batch** envelope,

plus **schema_guard** tree walk (forbidden internal key terms).

---

## Determinism

`determinism_report.json` records **three** identical runs on the canonical fixture:

- Same input file, same code path (`run_structural_analysis` → projected envelope).
- Canonical JSON: **sorted keys**, UTF-8, floats **rounded to 10** decimal places before hashing.
- **Requirement:** SHA256 run1 == run2 == run3.
- `raw_byte_identical_across_runs` is also recorded (pre-rounding JSON may differ in float text; hash gate is authoritative).

---

## Limitations (no future promises)

- **Not** a performance benchmark or penetration test; sanity checks only.
- **Not** a guarantee of clinical or domain certification.
- **Spec ↔ code** full formal proof is not automated beyond tier-1 spec file presence + implementation path hints (`audit_report.json`).
- **Calibration “magic numbers”** deep audit is manual; named profiles in `VERSION.yaml` are required and recorded in the manifest.

---

## Audit artifacts (checklist)

| File | Purpose |
|------|---------|
| `README.md` | This lock document. |
| `manifest.json` | Release record: version, commit, modules, determinism, calibration profile, seal status. |
| `build_info.json` | Python, platform, dependency fingerprint, commands. |
| `checksums.txt` | SHA256 of files in this directory (except `checksums.txt` itself). |
| `capabilities.yaml` | Copy of `hesperia/system/capabilities.yaml`. |
| `specs_index.json` | All `specs/**/*.md` and `spec/**/*.md` with hashes. |
| `test_report.json` | Pytest command, exit code, summary. |
| `audit_report.json` | **Master pass/fail:** projection, leaks, endpoints, modules, specs, calibration, security, **seal_decision**. |
| `determinism_report.json` | Triplicate hash proof. |
| `system_seal.json` | **Task 11:** GO/NO-GO over pipeline, matrices, P_CH, energy, concepts, topology, calibration, physics_validation, schema. |
| `schema_validation_report.json` | Per-artifact schema + leak scan. |
| `final_gate_status.json` | **Phase 7 summary:** `sealed`, per-domain `critical_checks` (includes **`system_seal`**), `reasons_fail`. |
| `e2e_reference_output.json` | **Regression anchor** for post-0.5.0 comparison. |
| `schema.json` | Frozen public JSON Schema used for validation. |

---

## Tagging (operator only if `seal_decision.may_tag_v0_5_0` is true)

```bash
git tag -a v0.5.0 -m "Hesperia Engine Dynamics v0.5.0 sealed baseline"
git push origin v0.5.0
```

---

## Canonical statement

**v0.5.0 is the canonical baseline for dynamic HESPERIA** — only when `manifest.json` has `seal_status: "PASS"` and `audit_report.json` lists no `reasons_fail`.

---

*See also: `docs/PUBLIC_PRODUCT_SURFACE.md`, `docs/HESPERIA_v0_5_ENGINE_DYNAMICS.md`, `docs/ENGINE_TASKS_1_11_INTEGRATION.md`, `AGENTS.md`.*
