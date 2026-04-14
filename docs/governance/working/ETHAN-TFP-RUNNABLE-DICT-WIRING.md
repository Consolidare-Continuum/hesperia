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

## 3a. Gena — file-in → artifacts-out (full TFP + main engine paths)

**One-shot (pipeline + audit + schema + release gate):**

```bash
python3 tools/gena_tfp_bundle_run.py -i path/to/transcript.md
# default out: outputs/tfp/runs/tfp_gena_<file_stem>/
# optional: -o outputs/my_run  --with-kme --with-triz --with-topology  --with-gold  --relax-discipline
```

Lower-level entry (pipeline only):

```bash
python3 -m runtime.pipeline.run_tfp_file_pipeline \
  --input path/to/transcript.md \
  --out-dir outputs/my_tfp_run
```

- **Input:** `.json` with `{"sessions":[{"session_id","text"},…]}` (same shape as `tests/fixtures/clinical_tfp/tfp_kernberg/session_transcripts_smoke_english.json`), or any other file treated as one session (stem = `session_id`).
- **Default artifacts:** `00_manifest.json`, `01_structural_batch.json`, `02_session_tfp_stages.json` (+ optional speaker-aware block when text looks like dialogue), `03_hex_microstructure_tfp.json`, `04_dlcr_full.json` (full `run_dlcr_pipeline`, not the short E2E summary), `05_sealed_multiscale.json`, `06_product_analyze.json`.
- **Optional:** `--with-kme`, `--with-triz`, `--with-topology`, `--with-r1-r4`; skip flags `--skip-structural`, `--skip-dlcr`, etc. **`--with-topology`** also writes flat **`12_<session_id>_*.json`** TRIZ-from-topology artifacts in the same `--out-dir` (coactivation → contradictions → metrics) unless **`--skip-triz-activation`**; exit **3** on `TRIZ_DEAD_LAYER` or activation write failure. Spec: `docs/specs/TRIZ_TOPOLOGY_ACTIVATION_PIPELINE_v1.md`.
- Sets `HESPERIA_DLCR_DOMAIN_PACK=tfp` unless `--no-dlcr-domain-pack`. Module: `runtime/pipeline/run_tfp_file_pipeline.py`.
- **Calibration audit (Task 4):** `python3 tools/tfp_calibration_audit.py --bundle-dir outputs/<run>` → `10_calibration_audit.json` (consistency score, alarms). Spec: `docs/specs/output_calibration_contract_v1.md`.
- **Goldset (Task 6):** `python3 tools/run_tfp_calibration_goldset.py --bundle-dir outputs/<run> -v` — `tests/gold/tfp_calibration_goldset_v1.json`. **CI** uses synthetic bundle `tests/fixtures/tfp_calibration_bundle_ci/` (see `docs/benchmarks/tfp_calibration_goldset_v1.md`).
- **Schema subset (Task 9):** `python3 tools/validate_tfp_bundle_schemas.py --bundle-dir outputs/<run>`.
- **Release gate (Task 10):** `PYTHONPATH=. python3 tools/calibration_release_gate.py --bundle-dir outputs/<run> --profile internal_review` → `11_calibration_release_gate.json`.

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
- `runtime/pipeline/run_tfp_file_pipeline.py` → file-in / multi-session → artifact bundle (§3a).  
- [ETHAN-DLCR-POST-OPTIONS-TASKS-30.md](ETHAN-DLCR-POST-OPTIONS-TASKS-30.md) — PO-14 / PO-30 overlap with **clinical_speech** / **tfp** packs.
