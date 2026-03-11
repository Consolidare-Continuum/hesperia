# Historical reference (pre-refactor)

# Canonical Dict B (B1) v0.4.1.4 — procedure and immutability

## Prerequisites

- Frozen surface: `assets/v040/CANONICAL_SURFACE_V040.txt` exists and surface is locked.
- B1 build is **hard-gated** by surface checksum: if expected surface SHA is recorded and current `surface_map_v040.json` SHA differs, B1 build exits with `HARD_FAIL_SURFACE_CHECKSUM_MISMATCH`.

## Procedure

1. **Run B1 Dict B build** (against frozen surface):
   - From repo root (hesperia tree):
     `PYTHONPATH=. python3 hesperia_lex/scripts/build_b1_dict_b_surface_alignment_v0414.py --repo-root .`
   - Expect: success when surface SHA matches canonical; **hard-fail** when it does not.

2. **Produce artifact + reports**:
   - Artifact: `hesperia_lex/frozen/B1_SIDE_TO_FAMILY_v0_4_1_4.json` + `.sha256`
   - Audit: `assets/v0414/b1_surface_alignment_audit_report.txt`
   - Validation: `PYTHONPATH=. python3 hesperia_lex/scripts/validate_b1_dict_b_v0414.py` → `assets/v0414/b1_dict_b_validation_report.txt`

3. **Sanity summary** (prevents "it built but it's garbage"):
   - `PYTHONPATH=. python3 hesperia_lex/scripts/build_dict_b_sanity_summary_v0414.py`
   - Output: `assets/v0414/DICT_B_SANITY_SUMMARY_V0414.txt`
     Counts: total_tokens_considered, mapped_a_hit, mapped_b0_hit, mapped_b1_hit, skipped_unknown, collisions.
     Per-area and per-family distribution (top 10).

4. **Freeze Dict B**:
   - `bash scripts/freeze_canonical_dict_b_v0414.sh`
   - Writes: `assets/v0414/CANONICAL_DICT_B_V0414.txt`
     Fields: `canonical_git_commit`, `dict_b_sha256`, `surface_map_sha256`, `model_name`, `model_revision`, `dict_a_sha256`.

## From this moment: Dict B is immutable

- **Any hash change to the B1 artifact = version bump.** No silent rebuilds.
- Changes (surface change, Dict A change, or B1 logic change) require a new version and a new canonical record.

## B1 runtime vs build

B1 is **built and frozen**; **runtime currently uses A + B0 only**. B1 participates in attribution only when a token→side mapping artifact exists (see [DICT-B-FREEZE-v0_4_1_4.md](DICT-B-FREEZE-v0_4_1_4.md) § B1 runtime state). The sanity summary records `b1_runtime_enabled: false` until that artifact is added and wired.

## Reference

- B1 builder: `hesperia_lex/scripts/build_b1_dict_b_surface_alignment_v0414.py`
- Freeze script: `scripts/freeze_canonical_dict_b_v0414.sh`
- Sanity summary: `hesperia_lex/scripts/build_dict_b_sanity_summary_v0414.py`
- Freeze doc: [DICT-B-FREEZE-v0_4_1_4.md](DICT-B-FREEZE-v0_4_1_4.md)
