# Seal B5 — Packaging verification

**Block:** B — Sealing integrity  
**Goal:** Build the release bundle and inspect contents. Ensure absence of internal artifacts; verify presence of only allowed runtime, core/services, core/projection, assets/public, and governance subset.

---

## Procedure

1. **Build release bundle** using the project’s packaging process (e.g. `python -m build`, or a script that assembles the distributable tree). Use the same exclusion list as in release/packaging_exclude.txt (or equivalent).

2. **Inspect contents** of the built package (e.g. unpack the sdist/wheel or copy of the release tree).

3. **Ensure absence of:**
   - **docs/internal/** — Internal registries, math/execution_flow docs, topology details.
   - **Internal registries** — Any file under docs/internal or paths that expose MATH_LAYER_REGISTRY, PIPELINE_LAYER_REGISTRY, or full topology.
   - **Topology helpers** — Raw topology modules or scripts intended only for internal use (e.g. invariant_catalog used from public API); core/topology may be present only if no public API exposes it.
   - **Debug tooling** — Scripts or entry points that dump internal state, layer intermediates, or bridge internals.
   - **Spec history** — Draft or internal-only governance/spec documents that reveal method (e.g. internal-only policy docs).

4. **Verify presence of (allowed):**
   - **runtime/** — Public runners, artifact_writer, public_reports, dossier (as defined in release content policy).
   - **core/services/** — Measurement, calibration, report façades.
   - **core/projection/** — Public projection layer (no raw topology exposure).
   - **assets/public/** — Public ontology map, public output schema, public metric profiles, public audit manifest schema.
   - **Governance subset** — Only governance docs that are safe for the release audience (e.g. PUBLIC_* policies, VOCABULARY_MAP, ENTRYPOINT_CLASSIFICATION); not docs/internal or internal-only registries.

5. **Optional:** Cross-check against **release/packaging_exclude.txt** and **RELEASE_CONTENT_POLICY_v1**: excluded paths must not appear in the bundle; included paths must be present as intended.

---

## Expected summary

- Bundle does **not** contain: docs/internal, internal registries, topology helpers (in exposed form), debug tooling, internal spec history.
- Bundle **does** contain: runtime (public surface), core/services, core/projection, assets/public, and the intended governance subset.

---

## Failure interpretation

| Symptom | Action |
|--------|--------|
| docs/internal in bundle | Add to packaging exclude list; ensure build excludes that tree. |
| Internal registries or topology in bundle | Extend exclusion list; or move to install-time internal-only path not shipped. |
| Missing core/services or core/projection | Fix packaging to include required modules for public runtime. |

---

## Pass criterion

Release bundle excludes internal artifacts and includes only runtime, core/services, core/projection, assets/public, and governance subset. No remediation required.
