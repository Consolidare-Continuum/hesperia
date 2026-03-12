<!--
HESPERIA — Reference Architecture Definition (RAD)
Copyright © 2026 igareosh.com — Platonov Igor (aka @igareosh). All rights reserved.
Restricted Research Disclosure License. Inspection and reference only.
No reproduction, redistribution, or use without explicit written permission.
See LEGAL_NOTICE.md for full terms.
-->

# Historical reference (pre-refactor)

# Dict B Freeze v0.4.1.4

## Coverage and topology truth

**This is not a geometric surface.** At ~1.27% coverage (5,473 sides of 432,000), the current artifact is a **sparse semantic activation layer** — a **selective anchor mesh**, not a filled topology. You are not building a filled topology; you are building a selective anchor mesh.

**"Hesperia covers the whole sphere" would be false.** Do not claim full coverage.

**Current state (honest):**

- Dict A drives intent.
- B0 maps tokens to families.
- B1 aligns only a tiny subset of surface.
- Runtime does not traverse B1 yet.

## Overview

v0.4.1.4 splits Dict B into two explicit layers:

1. **B0 token→family fallback** (current deterministic fallback).
2. **B1 side(surface)→family alignment** (real Dict B target, hard-gated by surface source availability).

## B0 — Token Fallback (from Dict A)

Canonical files:

- `hesperia_lex/frozen/B0_TOKEN_TO_FAMILY_v0_4_1_4_from_A_v0_4_1_3.json`
- `hesperia_lex/frozen/B0_TOKEN_TO_FAMILY_v0_4_1_4_from_A_v0_4_1_3.sha256`

Purpose:

- deterministic fallback for token landing when Dict A exact lemma miss occurs;
- derived from frozen Dict A v0.4.1.3 anchors (token/stem normalization only, no embeddings).

Limitations:

- no side-level attribution;
- no surface constraints;
- no embedding confidence.

## B1 — Surface Alignment (real Dict B target)

Canonical files:

- `hesperia_lex/frozen/B1_SIDE_TO_FAMILY_v0_4_1_4.json`
- `hesperia_lex/frozen/B1_SIDE_TO_FAMILY_v0_4_1_4.sha256`
- audit: `assets/v0414/b1_surface_alignment_audit_report.txt`
- **Freeze record**: `assets/v0414/CANONICAL_DICT_B_V0414.txt` (git commit, dict_b_sha256, surface_sha256, model, dict_a_sha256)
- **Sanity summary**: `assets/v0414/DICT_B_SANITY_SUMMARY_V0414.txt` (counts + top 10 area/family; prevents "built but garbage")

Purpose:

- stable, frozen side-level mapping (`side_id -> familyGlobal`) extracted from a **real** committed surface artifact.
- **From freeze onward: Dict B (B1) is immutable.** Any hash change = version bump. Procedure: [CANONICAL_DICT_B_V0414_PROCEDURE.md](CANONICAL_DICT_B_V0414_PROCEDURE.md).

Required inputs:

- primary target: `assets/v040/surface_map_v040.json`;
- otherwise another committed artifact containing explicit surface/side structure discoverable by script search.

Hard gate:

- if no real surface source exists, **B1 build cannot run** by design;
- builder exits non-zero and writes explicit missing-dependency audit report.

## Runtime landing policy

Deterministic order:

1. Dict A exact lemma match wins.
2. If no A hit:
   - use B1 only when runtime token→side mapping exists;
   - else use B0 token→family fallback.
3. Legacy `B_SURFACE_LEX_FIELD_v1.json` remains supported as compatibility fallback.

## B1 runtime state (explicit “not wired” until mapping exists)

**B1 exists and is frozen.** The B1 artifact (side→family) is built and canonical; the sanity summary and validation reports record coverage and checksums.

**Runtime currently uses A + B0 only.** Attribution uses B1 only when a **token→side** mapping is available at runtime (`assets/token_to_side_id_v040.json` or equivalent). That artifact does not exist yet, so `b1_runtime_enabled` is false and B1 does not participate in attribution — do not assume B1 is used.

**B1 activation** requires: (1) a **token→side mapping artifact** (builder that produces it, freeze record, and gate so runtime loads it when present); (2) runtime attribution wired to use B1 when the mapping exists. Until then, B1 remains build-time only and the sanity summary must state `b1_runtime_enabled: false`.

## Validators

- `hesperia_lex/scripts/validate_b0_dict_b_v0414.py`
- `hesperia_lex/scripts/validate_b1_dict_b_v0414.py`

Reports:

- `assets/v0414/b0_dict_b_validation_report.txt`
- `assets/v0414/b1_dict_b_validation_report.txt`
