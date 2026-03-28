# TFP-DATA-T02 — Research inventory index (Noah)

**Artifact:** [`TFP_DATA_T02_research_inventory.json`](TFP_DATA_T02_research_inventory.json) (machine-readable).

**Contains:**

- Recursive scan of `research/_noone_local/` — file counts, total bytes, per top-level dir + heuristic `purpose_tag` (`corpus` / `dict_a_lineage` / `scratch`).
- Reference map: repo files under `tools/`, `hesperia/`, `runtime/`, `tests/`, `docs/`, `.github/` whose text matches `research/_noone_local` or broader `research/...` path-like strings.

Regenerate after large moves: `python3 tools/gen_tfp_data_t02_inventory.py` from repo root.

`SIGNED: Cursor (Noah lane delivery) | TFP-DATA-T02 | 2026-03-28`
