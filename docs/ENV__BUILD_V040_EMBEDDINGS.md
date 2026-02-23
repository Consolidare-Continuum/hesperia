# Environment hardening notes — `sphere_rag.build_v040`

This note documents deterministic environment setup constraints for the optional v0.4.0 embedding/surface build.

## Observed failure

Current environment failure (as observed in build attempts):

- `transformers` backend dispatch error with TensorFlow backend path
- message fragment: **"Offending backend: tf"**

This blocks embedding-based artifact generation such as `surface_map_v040.json`.

## Deterministic hardening guidance

> Important: these are known fix paths and repo-aligned constraints, not a claim that every host is identical.

1. **Pin compatible embedding stack versions together**
   - Use coordinated pins for:
     - `sentence-transformers`
     - `transformers`
     - `torch`
   - Source of truth should be a lockfile or dedicated build requirements file.
   - This repo currently includes broad ranges in `requirements_v041.txt`; a build-specific lock is recommended.

2. **Isolate build dependencies from runtime dependencies**
   - Create a dedicated file such as `requirements-build-embeddings.txt` (or use uv/poetry lock if preferred).
   - Install build deps into a clean virtual environment before running `python -m sphere_rag.build_v040`.

3. **Backend selection hardening**
   - If TensorFlow import paths trigger backend mismatch, run build with explicit environment backend restrictions only when validated by local tooling policy.
   - Do not add ad-hoc hacks in code; keep backend policy in environment/bootstrap docs/scripts.

4. **Fail loudly with actionable errors**
   - Preserve exact dependency/backend errors in build logs.
   - Treat missing embedding env as a build-time artifact issue, not runtime engine corruption.

## Scope impact

- This environment issue affects optional build artifacts (`dict_b_v040`, `surface_map_v040`, related reports).
- Runtime attribution/traversal remains deterministic and functional with frozen artifacts (Dict A + B0 fallback + legacy assets).
