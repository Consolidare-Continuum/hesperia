# FPF pin — Hesperia vs brain

**Date:** 2026-07-19  
**Owner:** Gena (Main developer) · pin policy Ethan HAND SPEC §5  
**Status:** **Converged target `1.5.0`**

---

## Current pins

| Track | Pin | Location |
|-------|-----|----------|
| **Brain / team MCP** | `fpf-thinking-map==1.5.0` | brain `requirements-thinking-map.txt` |
| **Hesperia runtime** | `fpf-thinking-map==1.5.0` | `requirements/router.txt` · `requirements/calibration.txt` |
| **Inspect expect** | `fpf-thinking-map==1.5.0` | `sphere/fpf_inspect/constants.py` `FPF_PIN_EXPECTED` |

Hesperia **targets 1.5.0**, converging with brain soak. Do not document a dual-runtime story as normal.

---

## Rules

1. **Say which pin a binary runs** — GapReport `fpf_pin`, venv `pip show`, CI lockfile.  
2. **No silent upgrade path** — no autodoc “latest”; no unattended `pip install -U fpf-thinking-map`. Bump = explicit PR + CI green (Felix PRE07-01 / MWI-05).  
3. **Collision** → fix Hesperia **or** upstream library (operator owns both); do not freeze forever on `1.2.1` as safety theater.  
4. Stale docs still saying `1.2.1` (e.g. old envelope draft) are **wrong for runtime** — correct to `1.5.0` when touched.

---

## Verify

```bash
# Brain
grep fpf-thinking-map /data/altitudine/prichindel.com/requirements-thinking-map.txt
# Hesperia
grep fpf-thinking-map /data/workspaces/atomic-commit-hesperia/requirements/router.txt
pip show fpf-thinking-map | grep Version
```

---

`SIGNED: Main developer (Gena) | Hesperia↔brain pin | 2026-07-19 | 1.5.0 converge; no silent upgrade`
