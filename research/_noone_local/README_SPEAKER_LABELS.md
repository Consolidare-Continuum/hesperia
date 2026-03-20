# Speaker labels (top-level session transcripts)

**Scope:** Markdown files **directly** in `_noone_local/` (not `2_cleaned/`, `background/`, etc.).

**Convention:** Dialogue turns use explicit prefixes:

- `Терапевт: …`
- `Пациент: …`

**Engine alignment:** Canonical internal roles are English (`patient` / `therapist`). Surface strings are centralized in code:

- `hesperia/nlp/transcript_speaker_labels.py` — `LABEL_PATIENT_EN`, `LABEL_PATIENT_RU`, `LABEL_THERAPIST_*`, `ROLE_*`, `SPEAKER_PATTERN`, `SPEAKER_ALIASES`
- `hesperia/nlp/session_structure.py` — `parse_session_dialogue()` accepts **both** `Patient:`/`Therapist:` and `Пациент:`/`Терапевт:`
- `hesperia/nlp/transcript_parser.py` — turn segmentation uses the same module

**Tool:** Re-normalize after manual edits:

```bash
python3 tools/normalize_noone_local_speaker_prefixes.py        # dry-run
python3 tools/normalize_noone_local_speaker_prefixes.py --write
```

**Notes:**

- Abbreviation **т.е.** at line start stays as `Т.е.` (not turned into a therapist label).
- Inline merges (`…? П. …`, timestamp + `Т. …`) are fixed manually when found; re-scan after big edits.

**Stack ingest:** Promote copies into `2_cleaned/` before `build_ru_tfp_dictionary_stack.py` if the pipeline should consume normalized text.
