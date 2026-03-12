<!--
HESPERIA — Reference Architecture Definition (RAD)
Copyright © 2026 igareosh.com — Platonov Igor (aka @igareosh). All rights reserved.
Restricted Research Disclosure License. Inspection and reference only.
No reproduction, redistribution, or use without explicit written permission.
See LEGAL_NOTICE.md for full terms.
-->

# Historical reference (pre-refactor)

# Canonical Surface v0.4.0 — Procedure and Lock

**Run on a real machine** (not a constrained container). The v0.4.0 embedding build requires a full Python + PyTorch + sentence-transformers environment.

## 1. Produce the canonical surface

- **Explicit MODEL_REVISION** (required): exact commit or tag for `sentence-transformers/all-mpnet-base-v2`.
- **Explicit Dict A**: e.g. `hesperia_lex/frozen/A_CORE_STAR_MAP_v0_4_1_3.json` or `hesperia_lex/curated/...`.
- **Clean environment**: use `scripts/run_build_v040_embeddings.sh` (venv + pinned deps + backend guards).

```bash
export MODEL_REVISION="<exact_revision>"
export DICT_A_PATH="hesperia_lex/frozen/A_CORE_STAR_MAP_v0_4_1_3.json"
scripts/run_build_v040_embeddings.sh
```

**Required outputs** (no UNSET in provenance):

- `assets/v040/surface_map_v040.json`
- `assets/v040/surface_map_v040.json.sha256`
- `assets/v040/BUILD_PROVENANCE_v040.json`

## 2. Prove determinism

Run two clean builds (same MODEL_REVISION, same Dict A). Compare surface SHA.

```bash
scripts/check_repeatability_surface_v040.sh
```

- If SHA **differs**: stop, investigate, fix (env, ordering, non-determinism).
- If SHA **identical**: surface build is deterministic; proceed.

## 3. Freeze ownership

Record the canonical surface in `assets/v040/CANONICAL_SURFACE_V040.txt`:

```bash
scripts/freeze_canonical_surface_v040.sh
```

This writes:

- `canonical_git_commit`
- `surface_map_sha256`
- `model_revision`
- `dict_a_sha256`

**No UNSET** in that file after this step. v0.4.0 surface is now the single source of truth.

## 4. Lock the surface

From this moment:

- **surface_map_v040.json is immutable.**
- Any hash change = version bump (do not replace in place).
- No silent rebuilds; any new build that changes the file must be a new version/artifact name.

## 5. Only then build Dict B (B1)

Dict B (B1 surface alignment) must:

- Depend on the canonical surface.
- **Fail if surface checksum mismatches** the value in `CANONICAL_SURFACE_V040.txt` or `surface_map_v040.json.sha256`.
- Be fully deterministic.
- Emit its own checksum and validation report.

The B1 builder (`hesperia_lex/scripts/build_b1_dict_b_surface_alignment_v0414.py`) enforces the checksum gate: if an expected surface SHA is recorded and the current file’s SHA differs, the build exits with `HARD_FAIL_SURFACE_CHECKSUM_MISMATCH`.

## Scripts summary

| Script | Purpose |
|--------|---------|
| `scripts/run_build_v040_embeddings.sh` | Canonical build (MODEL_REVISION + Dict A required). |
| `scripts/check_repeatability_surface_v040.sh` | Two builds; exit 1 if surface SHA differs. |
| `scripts/freeze_canonical_surface_v040.sh` | Write CANONICAL_SURFACE_V040.txt from provenance + git. |
| `scripts/verify_surface_map_v040_checksum.sh` | Verify current surface file matches expected SHA. |
| `scripts/canonicalize_surface_v040.sh` | Build + validate + set/verify expected checksum. |
