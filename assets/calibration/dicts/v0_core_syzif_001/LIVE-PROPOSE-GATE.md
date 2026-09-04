# Live propose gate (when OpenAI key returns)

**Do not** run full-corpus propose at extract `min_freq=2` (~3.6M rows → ~90k batches @40).

## Required before first live call

1. Export `OPENAI_API_KEY` from trustmaster custody only (never commit).
2. Unset or ignore `HESPERIA_CALIB_MOCK_OPENAI` for the live pass.
3. Raise extract floor — recommended start: **`min_freq >= 20`** (re-measure batches; target << 5k calls unless budget approved).
4. Cap phrases: area/family waves; checkpoint every batch (`raw_checkpoint_path`).
5. Dry fixture propose (051) with key once before full pass.
6. After propose → anchor → merge → Stage8 evidence → **then** face=core before/after.
7. Dict D weight flip only after Stage8 + inert D load verified.

**Offline seal (current):** mock propose + D artifact; `coherence_empirical_weight=0`.
