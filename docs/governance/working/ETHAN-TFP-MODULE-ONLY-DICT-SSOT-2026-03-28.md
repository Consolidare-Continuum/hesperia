# Ethan — Charter: TFP / NLP dict operations — module `tfp_v1` only (research evicted)

**Date:** 2026-03-28  
**Status:** Active governance for packet **TFP-DATA-T01..T20** (brain: `operational/assignments/ETHAN-TFP-NLP-MODULE-ONLY-RESEARCH-EVICTION-T20-2026-03-28.md`).

## 1. Single source of truth (operational)

- All **ongoing** TFP and NLP **dictionary, corpus, calibration lineage, and API/OpenAI provenance** work for the modular TFP line is rooted at **`hesperia/modules/tfp/data/tfp_v1/`** (layout: **`TFP_V1_LAYOUT.md`**, task T-03).
- **`research/`**, including **`research/_noone_local/`**, is **not** an operational source for this line after migration completes: **no** default sync, **no** default corpus path in tools, **no** new authoritative copies living only under `research/` for TFP/NLP dicts.

## 2. Naming inside the module

- Under **`hesperia/modules/tfp/data/`**, the **only** operational product directory name is **`tfp_v1/`**. **No** `v052_*`, `wave_*`, or calibration **pack IDs** as folder names **inside** `tfp_v1/`.
- **`assets/calibration/dicts/<pack_id>/`** may remain for **CI / sealed promotion** until the loader ADR (T-13) maps `tfp_v1` → assets without duplicating version semantics inside `tfp_v1/`.

## 3. Dict A invariant

- **Dict A** is the **authoritative lexical plane** produced by the **API pipeline** (extract → normalize → propose → anchor → …).
- **Preserve in `tfp_v1/`:** original corpus, normalized corpus, **all** intermediate JSONL (candidates, normalized, proposals/drafts, engine-ready), the **frozen runtime** `dict_a.jsonl`, and **raw API/OpenAI JSON** outputs under **`tfp_v1/provenance/api/`** (no secrets, no API keys in tree).

## 4. Loader and env (forward)

- **`HESPERIA_TFP_MODULE_DATA_ROOT`** defaults to module data root; resolution order and fallbacks are defined in the loader ADR (T-13), not in this charter.

## 5. Closure

- Task **TFP-DATA-T20** records formal closure: tooling defaults, docs, and rows **DONE**; optional git tag per packet.

---

`SIGNED: Ethan (architect) | module-only dict SSoT | 2026-03-28 | TFP-DATA-T01`
