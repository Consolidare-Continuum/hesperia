# Module data layout — `tfp_v1/` (canonical)

**Task:** TFP-DATA-T03 (Sophia). **Charter:** `docs/governance/working/ETHAN-TFP-MODULE-ONLY-DICT-SSOT-2026-03-28.md`.

**Rule:** Under `hesperia/modules/tfp/data/`, operational dict/corpus/provenance data lives only under **`tfp_v1/`**. **No** calibration pack IDs, wave IDs, or `v052_*`-style names **inside** `tfp_v1/` — those belong under **`assets/calibration/dicts/<pack>/`** until loader promotion maps them here.

## Directory tree (target)

```text
hesperia/modules/tfp/data/tfp_v1/
  MANIFEST.yaml              # checksums, corpus hashes, optional generator version
  corpus/
    original/
      ru/                    # raw / source-of-truth text files (as migrated)
      en/
    sessions/                # clinical session transcripts (.md); ingest: tools/noone_sessions_ingest.py
    normalized/              # normalized text mirrors if distinct from original tree
  dict_a/
    candidates/              # dict_a_candidates.jsonl (and stage equivalents)
    normalized/              # dict_a_normalized.jsonl lineage
    proposals/               # proposal / draft JSONL not yet frozen
    runtime/                 # single canonical dict_a.jsonl face for module-first loads
  dict_b/
    seed.jsonl               # or subdirs if multiple artifacts required; no version folder names
    tfp.jsonl                # aligned / merged faces as needed (names per Ethan/Gena)
  provenance/
    api/
      runs/                  # per-run directories: openai request/response JSON (redacted)
      batch_ids/             # optional batch metadata index
  nlp/                       # optional: lexical assets previously under research for nlp.basic
```

## `MANIFEST.yaml` (required keys)

- `layout_version`: e.g. `1`
- `generated_at`: ISO-8601 UTC
- `corpus`: paths + `sha256` per bundle or per top-level corpus dir
- `dict_a_runtime`: `sha256` of `dict_a/runtime/dict_a.jsonl` when present

## Migration notes

- Initial population: **T-04** migration script; do not hand-edit `research/` as source after cutover (T-09, T-10).
- Large or sensitive API dumps: follow **T-18** (PII, `.gitignore`, LFS).

`SIGNED: Cursor (Sophia lane delivery) | TFP-DATA-T03 | 2026-03-28`
