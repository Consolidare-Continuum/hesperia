<!--
Ethan — TFP testing grounds: what must exist on disk vs optional DLCR plane (2026-03-20+).
-->

# Ethan — TFP runnable: dictionary / asset wiring

**Status:** OPEN — operator checklist; **not** canonical Engine Dynamics product (see `docs/HESPERIA_v0_5_ENGINE_DYNAMICS.md` §2).  
**Context (“news of today”):** DLCR-HP **v0.6.0** merged **JSONL** packs under `assets/data/engine_dynamics_v060/` are **orthogonal** to the **frozen 288-family** attribution bundle under `lexicon/` used by the sealed multiscale / `analyze` path. TFP smoke uses **both** families of assets depending on the step.

---

## 1. Three planes (do not conflate)

| Plane | Role in TFP flows | Primary paths | Validators / notes |
|-------|-------------------|---------------|-------------------|
| **A — Frozen lexicon (288)** | `run_structural_analysis_batch`, `run_sealed_multiscale_stack`, `analyze()` attribution when `HESPERIA_ATTRIBUTION_MODE=v06` | `lexicon/curated/v0_5_0/` **or** `lexicon/frozen/v0_5_0/` (same layout): **`dict_a_v06.jsonl`**, **`family_prior_v06.json`**; optional surface maps alongside curated | E2E step 10 passes `assets_root=lexicon/curated`. Missing files → batch errors or empty structural rows. |
| **B — Session NLP ontology (YAML)** | `hesperia.nlp.session_parser.analyze_session` → markers, concept/family/area scores, TFP stage hints | **`hesperia/ontology/dictA/*.yaml`**, **`hesperia/ontology/dictB/*.yaml`** (in repo) | No separate “wire-up” beyond clone; Russian/English marker coverage is **source data**, not DLCR JSONL. |
| **C — DLCR v0.6.0 packs (JSONL)** | Optional: `HESPERIA_TFP_DLCR=1` → `session_dlcr_bundles` in `run_output_e2e_tfp_smoke.json`; `run_dlcr_pipeline` everywhere | **`assets/data/engine_dynamics_v060/dict_a/dict_a_seed.jsonl`** + **`dict_a_tfp.jsonl`**; **`dict_b/dict_b_seed.jsonl`** + **`dict_b_tfp.jsonl`**; **`anchors/concept_hex_anchors.json`** (or controlled degradation); **`VERSION.yaml`**, **`dlcr_policy.yaml`**, **`domain_packs.yaml`** | `python3 tools/validate_dict_a.py` · `python3 tools/validate_dict_b_dlcr.py` · `python3 tools/check_dlcr_regression.py` |

**Rule:** **Plane C does not replace Plane A** for default structural batch. **Plane B** drives session-stage narrative; **Plane A** drives multiscale hex/family pipeline inputs.

---

## 2. Minimal “TFP smoke runs” checklist

| # | Requirement | Verify |
|---|-------------|--------|
| 1 | **Frozen bundle** present where E2E points (`lexicon/curated/v0_5_0/` recommended) | `dict_a_v06.jsonl`, `family_prior_v06.json` exist |
| 2 | **TFP topology embedding** for propagation-rich session parsing | `load_family_embedding_tfp()` resolves **`specs/canon/family_embedding_tfp.yaml`** (or repo `spec/` symlink) — fixed 2026-03-20 in `sphere/topology/family_embedding.py` |
| 3 | **Smoke transcripts** (optional file) | `tests/fixtures/clinical_tfp/tfp_kernberg/session_transcripts_smoke_english.json` — otherwise E2E uses inline English strings |
| 4 | **Run** | `python3 -m runtime.pipeline.run_e2e_all --out-dir /tmp/e2e` produces **`run_output_e2e_tfp_smoke.json`** |

---

## 3. Optional: DLCR on TFP sessions (“today’s” packs)

| Env | Effect |
|-----|--------|
| `HESPERIA_TFP_DLCR=1` | TFP smoke attaches **`session_dlcr_bundles`** (per session summary from `run_dlcr_pipeline`) |
| `HESPERIA_DLCR_DOMAIN_PACK=tfp` | Merges **`domain_packs.yaml`** pack **`tfp`** into DLCR policy (`dict_a_max_accepted`, `hex_smooth_alpha`, …) — **does not** swap JSONL files; TFP **lexical** rows still come from merged **seed + tfp** JSONL on disk |
| `HESPERIA_ANALYZE_DLCR_EVIDENCE=1` | `analyze()` adds **`lexical_evidence_dlcr`** (PO-02) — still uses DLCR pipeline under repo root |

**TFP-specific JSONL:** use tracked **`dict_a_tfp.jsonl`** / **`dict_b_tfp.jsonl`** for clinical/RU-oriented rows **in addition to** seeds (pipeline merges both by default).

---

## 4. What you do **not** need for baseline TFP smoke

- **`schemas/public/*`** mutation for TFP (testing collateral).
- **Replacing** `dict_a_v06.jsonl` with DLCR `dict_a_*.jsonl` — different formats and consumers.
- **PO-30 “domain packs”** alone — YAML pack only **overrides numeric policy**; it does not create missing JSONL.

---

## 5. Suggested next tasks (Ethan)

1. **CI / clone docs:** Document frozen lexicon sync in `CONTRIBUTING.md` or client runbook (if `lexicon/curated` is partial in some clones).  
2. **Benchmark:** `pytest tests/experimental/clinical_tfp/test_dlcr_benchmark_sessions.py` when `benchmark_sessions.yaml` defines `expected.dlcr`.  
3. **Single command card:** keep [ETHAN-DLCR-INTEGRATION-RUNBOOK.md](ETHAN-DLCR-INTEGRATION-RUNBOOK.md) as the operator entry; this file is the **dictionary delimitation** reference.

---

## Related

- `EXTENSION_STATUS.yaml` → `clinical_tfp` (experimental).  
- `runtime/pipeline/run_e2e_all.py` → `run_e2e_tfp_smoke`, `run_e2e_hex_microstructure_tfp`.  
- [ETHAN-DLCR-POST-OPTIONS-TASKS-30.md](ETHAN-DLCR-POST-OPTIONS-TASKS-30.md) — PO-14 / PO-30 overlap with **clinical_speech** / **tfp** packs.
