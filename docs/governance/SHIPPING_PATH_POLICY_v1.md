# Shipping path policy v1

**Status:** Mandatory  
**Purpose:** Define the only allowed path for producing distributable artifacts.

---

## Single rule

**No artifact may be distributed unless:**

1. It was produced by:
   ```bash
   ./release_sealed_runtime.sh
   ```
2. The automated gate reported:
   ```
   HESPERIA SEALED RUNTIME: PASS
   ```

Anything built manually (e.g. `./build_shipping.sh all` without running the gate, or ad-hoc packaging) is **non-release** and must not be distributed to evaluators, customers, or partners.

---

## Rationale

- Ensures the gate (import-boundary, sealing scan, projection test, binary/container checks, manifest) is never skipped.
- Single entry point reduces human error and keeps documentation unambiguous.
- Manual builds are for development and verification only.

---

## Enforcement

- Release checklist and release process documents reference this policy.
- **CI:** `.github/workflows/sealed-runtime-gate.yml` runs `tools/check_import_boundary.py` and `tools/sealing_scan.py` on push/PR to `main`. If either fails, merges are blocked. This prevents reflective terms or boundary violations from landing. The sealing scan targets evaluator-facing trees (`runtime/shipping`, `assets/public`, `examples`, `release`); it excludes the versioned audit bundle under `release/v0.5.0/` and `examples/extensions/triz_demo/` (see `tools/sealing_scan.py` → `SCAN_SKIP_DIR_PREFIXES`).
- Distributable bundles (tarballs, images) must be built from a run of `release_sealed_runtime.sh` that resulted in PASS.

---

*Policy version: v1. See SEALED_RUNTIME_RELEASE_GATE_v1.md and SEALED_RUNTIME_RELEASE_PROCESS_v1.md.*
