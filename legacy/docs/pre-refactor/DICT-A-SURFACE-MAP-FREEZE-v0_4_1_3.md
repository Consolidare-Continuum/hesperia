# Historical reference (pre-refactor)

# Dict A Surface Map — v0.4.1.3 (freeze-time artifact)

## Purpose

Maps **user-facing tokens** (e.g. `altruism`, `trust`) to **structural Dict A keys** (e.g. `altruism_1_10`, `trust_22_10`). Runtime resolves normalized token via this map before Dict A lookup. No structural IDs exposed to users; no underscore dependence; tokenizer unchanged.

Ref: [FINDING__Dict_A_Lemma_vs_Surface_2026-02-24.md](FINDING__Dict_A_Lemma_vs_Surface_2026-02-24.md).

## Artifacts

- `hesperia_lex/curated/DICT_A_SURFACE_MAP_v0_4_1_3.json` (build output)
- `hesperia_lex/frozen/DICT_A_SURFACE_MAP_v0_4_1_3.json` (copy for deploy)
- `hesperia_lex/frozen/DICT_A_SURFACE_MAP_v0_4_1_3.sha256`

## Shape

```json
{
  "altruism": "altruism_1_10",
  "trust": "trust_22_10",
  ...
}
```

## Build (at freeze time, after Dict A v0.4.1.3)

From repo root:

```bash
python3 CLIENTS/hesperia/hesperia_lex/scripts/build_dict_a_surface_map_v0413.py
```

Then copy to frozen and checksum:

```bash
cp CLIENTS/hesperia/hesperia_lex/curated/DICT_A_SURFACE_MAP_v0_4_1_3.json CLIENTS/hesperia/hesperia_lex/frozen/
sha256sum CLIENTS/hesperia/hesperia_lex/frozen/DICT_A_SURFACE_MAP_v0_4_1_3.json | awk '{print $1}' > CLIENTS/hesperia/hesperia_lex/frozen/DICT_A_SURFACE_MAP_v0_4_1_3.sha256
```

## Runtime

- `sphere_rag/attribution_v033.load_dict_a_surface_map_v033()` loads from assets, then `hesperia_lex/curated/`, then `hesperia_lex/frozen/`.
- `attribute(..., surface_map=...)` resolves each token: `key = surface_map.get(t, t)` then Dict A lookup by `key`.
- `run_attribution_pipeline()` loads surface map and passes it to `attribute()`. API path uses it automatically.

## Do not

- Change tokenizer (underscore remains stripped).
- Allow underscores in user input for matching.
- Expose structural IDs to users.
