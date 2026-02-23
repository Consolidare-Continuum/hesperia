# Environment hardening notes — `sphere_rag.build_v040`

This document defines a deterministic, build-only environment for generating v0.4.0 embedding artifacts (`dict_b_v040`, `surface_map_v040`, reports, and manifest).

## Observed failure before hardening

In an unpinned environment, `transformers` initialization could fail with:

- `ValueError: Backend should be defined in the BACKENDS_MAPPING. Offending backend: tf`

This blocked `python3 -m sphere_rag.build_v040` and therefore blocked generation of `surface_map_v040.json`.

## What is now implemented

### 1) Pinned build-only dependency set

A dedicated requirements file now pins the embedding stack used only for build tasks:

- `requirements-build-embeddings.txt`
  - `sentence-transformers==2.7.0`
  - `transformers==4.41.2`
  - `torch==2.2.2`
  - `numpy==1.26.4`
  - `huggingface-hub==0.23.5`

This avoids broad version ranges and keeps the build reproducible.

### 2) Deterministic runner script

Use:

- `scripts/run_build_v040_embeddings.sh`

The runner:

- creates/uses a dedicated virtualenv (`.venv_v040_build` by default)
- installs pinned versions from `requirements-build-embeddings.txt`
- sets backend guards:
  - `USE_TF=0`
  - `TRANSFORMERS_NO_TF=1`
  - `TRANSFORMERS_NO_FLAX=1`
- runs `python -m sphere_rag.build_v040` with an explicit Dict A input:
  - `hesperia_lex/curated/A_CORE_STAR_MAP_v0_4_1_3.json`
- writes artifacts under `assets/v040` by default
- fails loudly if required inputs or expected outputs are missing
- prints `sha256` checksums for key artifacts

### 3) TensorFlow backend issue resolution strategy

The fix is environment-level, not code-hack based:

- deterministic package pins with a known good `sentence-transformers` + `transformers` + `torch` combination
- explicit runtime env vars to keep transformers on the PyTorch path and avoid TF backend registration/import

No runtime engine behavior is changed, and no TensorFlow dependency is required.

## Verification commands

Run from repository root:

```bash
scripts/run_build_v040_embeddings.sh
```

Expected outputs:

- `assets/v040/surface_map_v040.json`
- `assets/v040/dict_b_v040.json`
- `assets/v040/build_manifest_v040.json`

The runner prints checksums; verify explicitly if needed:

```bash
sha256sum assets/v040/surface_map_v040.json \
          assets/v040/dict_b_v040.json \
          assets/v040/build_manifest_v040.json
```
