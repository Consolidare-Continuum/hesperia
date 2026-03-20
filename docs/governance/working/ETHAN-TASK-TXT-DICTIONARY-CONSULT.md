<!--
Ethan consult: task.txt (DLCR draft spec) + repo wiring + external methodology notes.
-->

# Ethan consult — `task.txt`: which dictionaries to add, and how

**Sources:** repo root [`task.txt`](../../../task.txt) (DLCR-HP v0.6.0-draft1 plain spec), in-tree wiring [ETHAN-TFP-RUNNABLE-DICT-WIRING.md](ETHAN-TFP-RUNNABLE-DICT-WIRING.md), [ETHAN-DLCR-INTEGRATION-RUNBOOK.md](ETHAN-DLCR-INTEGRATION-RUNBOOK.md).  
**External (internet, high level):** psychotherapy transcript work stresses **therapy-specific labels**, **dialogue acts**, **multi-utterance context**, and **transparent / reproducible** pipelines; much published work uses **supervised or LLM-assisted** labeling — Hesperia’s **task.txt** instead mandates **deterministic, versioned, auditable** resources (no hidden services, no black-box primary disambiguation).

---

## 1. What `task.txt` says you must have (normative)

| Dictionary | Role | Normative content (summary) |
|------------|------|-----------------------------|
| **Dict A** | L1 lexical evidence | `entry_id`, `surface_form`, `normalized_form`, `language`, `match_type`, `candidate_concept_ids`, `priority`, `version`; phrase-first; proposes concepts, **does not** pick family/area |
| **Dict B** | L2 concept layer | `concept_id`, `preferred_label`, `definition`, `family_ids`, `area_ids`, `specificity_rank`, `status`, `version`; links to hex anchor policy; **family/area follow concept** |
| **Anchors / topology** | L3–L4 | Concept → hex anchors (+ optional footprint), registry under `assets/.../anchors/` per spec §14–15 |
| **Corpora** | Regression | Gold / ambiguity / phrase-priority / speech-noise cases (§24) |

**Phase 2 guidance in `task.txt` (§25):** first bounded pack **TFP / clinical** — order of magnitude **100–300 concepts**, **5–15 lexical forms each**, explicit **exclusions**, frozen **score formula** (already reflected in seed + `dict_*_tfp.jsonl` direction).

---

## 2. What the repo already maps this to (implementation)

| Spec notion | On-disk home (today) | Validators / gates |
|-------------|----------------------|-------------------|
| Dict A (JSONL) | `assets/data/engine_dynamics_v060/dict_a/dict_a_seed.jsonl` + `dict_a_tfp.jsonl` | `python3 tools/validate_dict_a.py` |
| Dict B (JSONL) | `dict_b/dict_b_seed.jsonl` + `dict_b_tfp.jsonl` | `python3 tools/validate_dict_b_dlcr.py` |
| Schemas | `schemas/lexical_concept/dict_a.schema.json`, `dict_b.schema.json`, `resolver_output.schema.json` | lexical_concept tests |
| Anchors | `assets/data/engine_dynamics_v060/anchors/concept_hex_anchors.json` (+ hex map as loaded) | degradation flags if missing |
| Version pins | `assets/data/engine_dynamics_v060/VERSION.yaml`, `assets/version_registry.yaml` | run metadata / audits |
| Policy / modes | `dlcr_policy.yaml`, `domain_packs.yaml` | `HESPERIA_DLCR_DOMAIN_PACK` |

**Separate from DLCR JSONL (do not merge formats):**

- **Frozen 288 attribution:** `lexicon/.../v0_5_0/dict_a_v06.jsonl` + `family_prior_v06.json` — structural / sealed path.  
- **Session ontology (YAML):** `hesperia/ontology/dictA/*`, `dictB/*` — `analyze_session` / TFP narrative layer.

---

## 3. What you still “add” in practice (gaps vs ambition)

From `task.txt` §7–8 **recommended** fields (lemma, scope_rules, negative_patterns, alt_labels, resolver_clues, hex_footprint_policy, …): many are **optional in JSON Schema** but **should be populated** as the clinical pack grows.

Concrete additions operators care about:

1. **More Dict A rows** — surface/phrase triggers → existing `candidate_concept_ids` (validated, phrase-first matcher).  
2. **More Dict B rows** — stable `concept_id`, family/area linkage, `specificity_rank`, optional `disambiguation_notes` / exclusions.  
3. **Anchor coverage** — new concepts need entries in `concept_hex_anchors.json` (or explicit degraded path).  
4. **Gold / benchmark lines** — `assets/data/engine_dynamics_v060/corpora/` + `tools/check_dlcr_regression.py` + optional `tests/experimental/clinical_tfp/benchmark_sessions.yaml` `expected.dlcr`.  
5. **VERSION.yaml / CONTRIBUTING** — bump pins when semantics change; note in [CONTRIBUTING.md](../../../CONTRIBUTING.md) if present.

---

## 4. How we add them (procedure)

1. **Author** new lines in JSONL (copy shape from existing rows in `dict_a_tfp.jsonl` / `dict_b_tfp.jsonl`).  
2. **Validate:**  
   `python3 tools/validate_dict_a.py`  
   `python3 tools/validate_dict_b_dlcr.py`  
3. **Regression:**  
   `python3 tools/check_dlcr_regression.py`  
4. **Unit tests:** extend `tests/lexical_concept/` or experimental TFP tests when behavior is contract-critical.  
5. **Bump** `VERSION.yaml` / registry notes if pack semantics or pins change.  
6. **Never** replace frozen `dict_a_v06.jsonl` (288 format) with DLCR JSONL — different consumers (see TFP wiring doc).

---

## 5. External methodology (internet) — fit to Hesperia

- Literature emphasizes **domain-specific annotation** (e.g. dialogue acts in therapy) and **session-level dynamics** (therapist timing, responsiveness). That aligns with `task.txt` **speech/clinical mode**, **segment trajectory**, and **audit-rich** outputs — but Hesperia adds **hard** requirements: deterministic resources, stable tie-breaks, CI regression, no unversioned overrides.  
- If borrowing ideas from papers or LLM-assisted curation, **downstream artifact must still be** frozen JSONL/YAML checked into repo and passing validators — not a live model call in L0/L2 primary path (`task.txt` §9 N2, §11 C5).

---

## 6. One-line Ethan answer

**Add:** more **Dict A** and **Dict B** JSONL (plus anchors + gold corpus lines) under `assets/data/engine_dynamics_v060/`, following **schemas** and **task.txt** field discipline; **how:** edit JSONL → `validate_dict_*` → `check_dlcr_regression` → pytest → version pin. Keep **frozen lexicon** and **ontology YAML** on their own planes for TFP/multiscale.

---

## Related

- Canon hub: `specs/canon/lexical_concept/README.md`  
- Post-options matrix: [ETHAN-DLCR-POST-OPTIONS-TASKS-30.md](ETHAN-DLCR-POST-OPTIONS-TASKS-30.md)
