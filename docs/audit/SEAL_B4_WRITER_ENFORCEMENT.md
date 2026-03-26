# Seal B4 — Artifact writer enforcement

**Block:** B — Sealing integrity  
**Goal:** Verify that (1) in `HESPERIA_RUNTIME_MODE=public_runtime`, `write_internal_json` does not write any file; (2) `write_public_json` always applies projection.

---

## Procedure

### 1. Internal write blocked in public mode

1. Set environment: `export HESPERIA_RUNTIME_MODE=public_runtime`
2. From Python (or a small script), call:
   - `from runtime.artifact_writer import write_internal_json`
   - `write_internal_json("/tmp/seal_b4_internal_test.json", {"internal": "data", "side_id": 12345})`
3. **Check:** File `/tmp/seal_b4_internal_test.json` must **not** be created (or must not exist after the call). `write_internal_json` is a no-op in public_runtime mode.
4. Unset or reset mode for subsequent tests if needed.

### 2. Public write applies projection

1. Call `write_public_json(path, data)` with a payload that contains internal-only keys or values (e.g. `side_id`, `hex`, or a 12-element area vector).
2. **Check:** The file written at `path` must contain only projected/public-safe content:
   - No `side_id` key (or key stripped/remapped).
   - No internal topology keys (e.g. no raw `area_id` 10 or 11, no 288-family list in public form).
   - Vector lengths and key names conform to public ontology (e.g. macro_domain_vector length 10, policy_family_counts length 240).
3. **Check:** Projection is applied automatically (no need to pre-call apply_public_projection before write_public_json); the writer applies it internally.

---

## Expected summary

- **public_runtime + write_internal_json:** No file written; internal data never persisted.
- **write_public_json:** File content is projected; internal-only keys/values absent; projection applied inside the writer.

---

## Failure interpretation

| Symptom | Action |
|--------|--------|
| File created by write_internal_json in public mode | Enforce mode check in write_internal_json; no-op when mode is public_runtime. |
| Internal keys in file after write_public_json | Ensure write_public_json calls apply_public_projection/sanitize_public_trace before write. |

---

## Pass criterion

In public_runtime mode, internal writes are blocked; public writes always produce projected content. No remediation required.
