# API / OpenAI provenance (`tfp_v1/provenance/api/`)

**TFP-DATA-T07:** Historical dict-calibration outputs are mirrored from `outputs/dict_calibration/**` into **`runs/outputs_dict_calibration_mirror/`** (run `python3 tools/copy_dict_calibration_provenance_to_tfp_v1.py` from repo root after calibration work). Summary: **`COPY_MANIFEST_DICT_CALIBRATION.json`** in this directory (committed when refreshed).

**TFP-DATA-T18:** Do not commit raw secrets; the copy tool applies best-effort redaction. Bulk mirror under `runs/` stays **gitignored**; see `docs/governance/TFP_V1_PROVENANCE_API_POLICY.md`.
