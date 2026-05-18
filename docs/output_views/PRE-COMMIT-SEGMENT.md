# Optional: validate golden `iteration_segment_openai_v1` (T53)

**Golden file:** `output_views/tests/fixtures/golden/iteration_segment_openai_v1_iter0.json`

**When prompts or segment layout change**, regenerate:

```bash
cd output_views
python3 scripts/validate_golden_segment.py regenerate
```

**Verify** (exit 0 = match):

```bash
cd output_views
python3 scripts/validate_golden_segment.py verify
```

**Hook (optional):** add to your local `.pre-commit-config.yaml`:

```yaml
  - repo: local
    hooks:
      - id: hesperia-segment-golden
        name: output_views golden segment
        entry: bash -c 'cd output_views && python3 scripts/validate_golden_segment.py verify'
        language: system
        files: ^output_views/(segment/|prompts/|schemas/).*
```

The Hesperia repo does **not** ship a root `.pre-commit-config.yaml` by default; this is **opt-in**.

`SIGNED: Gena | Hesperia | 2026-04-07 | T53`
