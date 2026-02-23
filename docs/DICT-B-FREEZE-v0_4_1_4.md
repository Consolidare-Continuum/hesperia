# Dict B Freeze v0.4.1.4

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

Purpose:

- stable, frozen side-level mapping (`side_id -> familyGlobal`) extracted from a **real** committed surface artifact.

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

## Validators

- `hesperia_lex/scripts/validate_b0_dict_b_v0414.py`
- `hesperia_lex/scripts/validate_b1_dict_b_v0414.py`

Reports:

- `assets/v0414/b0_dict_b_validation_report.txt`
- `assets/v0414/b1_dict_b_validation_report.txt`
