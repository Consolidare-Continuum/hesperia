<!--
HESPERIA — Reference Architecture Definition (RAD)
Copyright © 2026 igareosh.com — Platonov Igor (aka @igareosh). All rights reserved.
Restricted Research Disclosure License. Inspection and reference only.
No reproduction, redistribution, or use without explicit written permission.
See LEGAL_NOTICE.md for full terms.
-->

# Historical reference (pre-refactor)

# HESPERIA PoC Boot Sequence (Canonical v0.4.x)

This is the deterministic startup sequence for a clean clone.

## 1) Environment

- Python: **3.10+** recommended for baseline compatibility.
- From repo root:

```bash
python --version
pip install -r requirements.txt
```

## 2) Build

```bash
python build_v040.py \
  --model-revision v040 \
  --assets-root hesperia_lex/curated \
  --out-dir artifacts/build_v040 \
  --allow-small-build
```

## 3) Test

```bash
pytest
```

## 4) Run layer pipeline

```bash
python -m sphere_rag.layers.run_l1_through_l9
```

## 5) Run API

```bash
uvicorn api.main:app
```
