# TFP v1 — API provenance privacy and storage (TFP-DATA-T18)

**Path:** `hesperia/modules/tfp/data/tfp_v1/provenance/api/`

- **No secrets:** Strip API keys, tokens, and auth headers before copy into repo; never commit `.env`.
- **PII:** Session/corpus-derived payloads may contain personal data — default **do not commit** raw dumps; operator-only storage or redacted excerpts in governance/working only with igareosh approval.
- **Git:** `runs/` and `batch_ids/` contents are **gitignored** by default; use **Git LFS** if a small redacted reference set must live in-tree.
- **Large JSON:** Prefer out-of-band archive (cluster backup path) per Abelard runbook.

`SIGNED: Cursor (Ava lane) | TFP-DATA-T18 | 2026-03-28`
