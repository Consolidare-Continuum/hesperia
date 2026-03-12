<!--
HESPERIA — Reference Architecture Definition (RAD)
Copyright © 2026 igareosh.com — Platonov Igor (aka @igareosh). All rights reserved.
Restricted Research Disclosure License. Inspection and reference only.
No reproduction, redistribution, or use without explicit written permission.
See LEGAL_NOTICE.md for full terms.
-->

# Historical reference (pre-refactor)

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
  - and an explicit `--model-revision` pin (required)
- writes artifacts under `assets/v040` by default
- fails loudly if required inputs or expected outputs are missing
- prints `sha256` checksums for key artifacts

### 3) TensorFlow backend issue resolution strategy

The fix is environment-level, not code-hack based:

- deterministic package pins with a known good `sentence-transformers` + `transformers` + `torch` combination
- explicit runtime env vars to keep transformers on the PyTorch path and avoid TF backend registration/import

No runtime engine behavior is changed, and no TensorFlow dependency is required.

## Model revision pinning (mandatory)

`sphere_rag.build_v040` now requires:

- `--model-revision <exact_sha_or_tag>`

Build execution fails fast if revision is missing or floating (`UNKNOWN`, `UNSET`, `latest`).
This ensures provenance and manifest records are truthful and reproducible.

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


## Deterministic artifact controls (v0.4.0)

The build now enforces deterministic serialization for `surface_map_v040.json`:

- writer: `sphere_rag.io_deterministic_json.write_json_deterministic`
- JSON policy: `ensure_ascii=False`, `sort_keys=True`, `separators=(",", ":")`, newline at EOF
- no default `json.dump/json.dumps` path is used for this artifact

### Checksum + provenance outputs

On successful build, the output directory includes:

- `surface_map_v040.json`
- `surface_map_v040.json.sha256` (format: `<sha256>  surface_map_v040.json`)
- `BUILD_PROVENANCE_v040.json` (deterministic JSON; separate governance record that does not define the surface artifact hash)

`BUILD_PROVENANCE_v040.json` captures:

- git commit, python/platform/machine
- `USE_TF`, `TRANSFORMERS_NO_TF`, `TRANSFORMERS_NO_FLAX`
- `pip freeze`
- versions for `torch`, `transformers`, `sentence_transformers`, `huggingface_hub`, `numpy`
- input Dict A path + SHA256 + model metadata
- output artifact paths + SHA256 values

### Checksum verification gate

Expected checksum file (repo-tracked):

- `assets/v040/surface_map_v040.json.sha256`

Placeholder value in clean environments may be:

- `UNSET  surface_map_v040.json`

In that state, verification intentionally fails until the canonical checksum is set.

Verify locally:

```bash
scripts/verify_surface_map_v040_checksum.sh
```

Or verify an explicit generated artifact path:

```bash
scripts/verify_surface_map_v040_checksum.sh assets/v040/surface_map_v040.json assets/v040/surface_map_v040.json.sha256
```

Policy: if checksum changes, treat it as an artifact contract change and bump the artifact version (`v0.4.1+`) with release notes before updating `assets/v040/surface_map_v040.json.sha256`.

## Surface schema validation

Schema validator module:

- `sphere_rag.validate_surface_map_v040`

Validation gates:

- artifact file exists
- top-level is a JSON object
- top-level keys are side ids (`str`/`int`)
- each value is a list (non-empty)
- each list item is either:
  - token string (non-empty), or
  - `[anchor_id, score]` where `anchor_id` is `str/int` and `score` is finite numeric
- no NaN/Infinity float values are accepted

Build integration: the v0.4.0 build now validates `surface_map_v040.json` immediately after writing it and fails non-zero on schema error.

## Float policy

Current `surface_map_v040.json` schema is token lists (`side_id -> [token, ...]`), so no floats are present in canonical output. Quantization is therefore not applicable for the surface artifact at this time.

## Canonical surface workflow

Use:

```bash
MODEL_REVISION=<exact_revision> scripts/canonicalize_surface_v040.sh
```

Workflow behavior:

- runs v0.4.0 surface build with explicit `--dict-a`, `--assets-root`, `--out-dir`, and `--model-revision`
- runs strict schema validator
- applies checksum gate behavior:
  - if expected checksum is `UNSET`, writes generated SHA into `assets/v040/surface_map_v040.json.sha256` and prints: **"Expected checksum set. Commit this change."**
  - if expected checksum is already set, verifies exact match and fails on mismatch

## Repeatability check (same machine)

Use:

```bash
MODEL_REVISION=<exact_revision> scripts/check_repeatability_surface_v040.sh
```

The check builds surface artifacts twice in clean temp output directories and compares SHA256 values. Failure message is:

- `Non-deterministic surface build detected: sha differs across two runs.`

## Go/No-Go for Dict B generation

### GO (all required)

- `surface_map_v040.json` exists (real artifact, not placeholder)
- `sphere_rag.validate_surface_map_v040` passes
- expected checksum is set (non-`UNSET`) and `scripts/verify_surface_map_v040_checksum.sh` passes
- repeatability check passes (two clean runs produce same SHA)
- provenance records include:
  - non-`UNKNOWN` `model_revision`
  - correct Dict A SHA256

### NO-GO

If any GO criterion fails, do **not** proceed with Dict B governance/release generation. Surface must be canonical first.
