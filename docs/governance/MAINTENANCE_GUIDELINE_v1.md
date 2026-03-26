# Long-term maintenance guideline v1

**Status:** Active  
**Purpose:** When new features are added in development, follow this sequence. The release process remains identical.

---

## When adding new features

1. **Implement internally.**  
   New logic, metrics, or execution_flow steps live inside the sealed core. Public entry points (CLI/API) do not gain new commands or endpoints unless the surface is explicitly extended with a version bump (see PUBLIC_API_SURFACE_FREEZE_v1.md).

2. **Verify projection hides internal structures.**  
   Any new output that can reach the public path must go through the projection layer. Ensure no new keys or values leak internal geometry, layer names, or topology. Run the projection test (e.g. via release gate or regression tests).

3. **Run sealing scan.**  
   After code or doc changes, run `tools/sealing_scan.py`. The public tree must remain free of forbidden terms (or only explicitly waived paths). Fix or move any new hits.

4. **Update schema if necessary.**  
   If the public output shape changes (new fields, removed fields, changed types), update `assets/public/public_output_schema.json` and increment `schema_version` for incompatible changes. Document in release notes.

5. **Rebuild sealed runtime.**  
   Run `./release_sealed_runtime.sh`. Ensure the gate reports `HESPERIA SEALED RUNTIME: PASS`. No artifact may be distributed from a manual build or a failed gate.

---

## Release process (unchanged)

- Single path: `./release_sealed_runtime.sh`.
- Gate summary: `HESPERIA SEALED RUNTIME: PASS`.
- Manual steps (clean machine, reflection audit, performance) as in SEALED_RUNTIME_RELEASE_PROCESS_v1.md.
- Regression: run tests in `tests/test_sealed_runtime_regression.py` and corpus in `tests/sealed_runtime_inputs/` (analyze each, compare pairs, batch-analyze; verify deterministic output, schema validity, no forbidden keys).

---

## Summary

| Step | Action |
|------|--------|
| Develop | Implement internally; no bypass of projection → schema_guard → serializer. |
| Verify | Projection hides internals; sealing scan passes; schema updated if output changed. |
| Ship | Only via `./release_sealed_runtime.sh` and PASS. Regression test set and gate must pass. |

---

*See SHIPPING_PATH_POLICY_v1.md, PROJECTION_SERIALIZATION_CHAIN_v1.md, and SEALED_RUNTIME_RELEASE_PROCESS_v1.md.*
