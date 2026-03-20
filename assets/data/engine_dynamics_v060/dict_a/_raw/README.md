# dict_a `_raw` JSONL (local / CI-generated)

Large intermediate dumps (`dict_a_ru_*.jsonl`) are **not committed** — they exceed GitHub’s per-file size limit.

Regenerate the full v0.6.0 pack (including this folder):

```bash
python3 tools/run_tfp_dict_build_full_artifacts_v060.py --write
```

Smaller derived artifacts under `assets/data/engine_dynamics_v060/` remain tracked.
