<!--
Ethan — post-integration option → execution tasks (≤30).
Maps the 20 “post-integration options” into a Codex-style matrix: option, modules, difficulty, gain, deps, acceptance.
Practical merge order preserved as waves.
-->

# Ethan — DLCR post-options task matrix (30 tasks)

**Status:** **IN PROGRESS** (wave 1–8 partially implemented 2026-03-20; not all 30 rows closed)  
**Parent narrative:** 20 post-integration options + **5 plain-language outcomes** + **safe integration order** (normalization → Dict A → Dict B → resolver → audit → hex → smoothing → family/area adapter → regression → domain packs).

### Implementation snapshot (repo)

| IDs | Delivered (high level) |
|-----|-------------------------|
| PO-01 | `prepare_structural_analysis_text` + wired into `build_structural_internal_from_multiscale` (`text_preprocess` diagnostics) |
| PO-03–04 | Matcher longest-span ordering + `max_accepted` + `HESPERIA_DICT_A_MAX_ACCEPTED` |
| PO-05 | `disambiguation_notes` on Dict B schema (optional field) |
| PO-06–09 | Resolver input_context overlap, coherence boost, specificity tie-break, `audit` block + schema |
| PO-10 | `tools/dump_dlcr_trace.py` |
| PO-11–12 | **`HESPERIA_CONCEPT_EVIDENCE_GUARD=observe`** → `semantic_evidence` on `markers_to_concept_activation`; **`=strict`** → skip Dict-A direct hits but **retry b0** when the token exists in merged Dict B (`B0_fallback`, `b_fallback_after_a_excluded`); diagnostics `semantic_path_guards.semantic_evidence` |
| PO-13–14 | `dlcr_policy.yaml` + `domain_packs.yaml` + `load_dlcr_policy`; clinical role fold env |
| PO-15–18 | Execution Flow: policy-driven smoothing, co-occurrence token pairs, segment hex drift/persistence, cross-family sketch |
| PO-19 | `neighbor_ring_symbols` (index-adjacency stub) |
| PO-22 | `core.lexical.cooccurrence` token pair counts |
| PO-23 | Sequential association coefficient in policy (**default 0** for gold consistency) |
| PO-24–25 | `cross_family_relation_sketch` in execution_flow output |
| PO-26 | `POST /hesperia/internal/dlcr_trace` when `HESPERIA_API_INSTRUMENTATION=1` |
| PO-27 | [ETHAN-DLCR-INSTRUMENTATION-TEMPLATE.md](ETHAN-DLCR-INSTRUMENTATION-TEMPLATE.md) |
| PO-28–29 | Regression still `check_dlcr_regression.py`; CONTRIBUTING note for dict bumps |
| PO-30 | `domain_packs.yaml` + `HESPERIA_DLCR_DOMAIN_PACK` |
| PO-02 | **`HESPERIA_ANALYZE_DLCR_EVIDENCE=1`** → `analyze()` extended **`lexical_evidence_dlcr`**: fingerprint, hits, **`evidence_spans`** (bounded, resolver-stable keys), schema fragment `schemas/lexical_concept/analyze_lexical_evidence_dlcr.schema.json` |

**Difficulty:** S = small, M = medium, L = large.

---

## Waves (safe route)

| Wave | Options covered (roughly) | Task IDs |
|------|---------------------------|----------|
| W1 | 1, 2, 4 | PO-01 — PO-04 |
| W2 | 3, 5 | PO-05 — PO-08 |
| W3 | 6, 7 | PO-09 — PO-12 |
| W4 | 8, 9 | PO-13 — PO-14 |
| W5 | 10, 11, 12, 13, 15 | PO-15 — PO-19 |
| W6 | 14, 16 | PO-20 — PO-23 |
| W7 | 17, 18 | PO-24 — PO-27 |
| W8 | 19, 20 | PO-28 — PO-30 |

---

## Task matrix

| ID | Option # | What gets integrated | Modules touched | D | Expected gain | Depends on | Acceptance test |
|----|----------|----------------------|-----------------|---|---------------|------------|-----------------|
| PO-01 | **1** | Normalization-only: single **preprocessing** contract before structural + session measurement (shared entry). | `core.lexical.normalization`, `runtime.services.analysis_service`, `runtime.pipeline.analyze`, `hesperia.nlp.*` entrypoints | M | Stable token/phrase boundaries; fewer run-to-run diffs from noise | — | Golden: same semantic text, varied punctuation/casing → **identical** `canonical_text` / hash used downstream. |
| PO-02 | **2** | Dict A as **formal lexical evidence layer** in the main analyze path (not only DLCR sidecar). | `core.lexical.matcher`, `lexicon/curated` + `assets/data/engine_dynamics_v060/dict_a`, extended analyze payload | L | Governed wording capture; candidates not pseudo-classes | PO-01 | `validate_dict_a` CI + analyze `extended` contains **evidence spans** with schema-stable keys. |
| PO-03 | **4** | **Phrase-first** matching: longest-span priority, explicit ordering rules. | `core.lexical.matcher`, specs `SPEC__Dict_A` / resolver | M | Multiword units first-class; less shredded clinical phrases | PO-02 | Unit tests: overlapping phrases resolve to **longest** winning span; no duplicate consume. |
| PO-04 | **4** | Token fallback + **match caps** (anti-noise) documented and enforced. | `core.lexical.matcher` | S | Bounded cost; less garbage hits | PO-03 | Tests: cap triggers + deterministic tie when cap hit. |
| PO-05 | **3** | Dict B as **true inventory**: stable `concept_id`, defs, family/area membership, **exclusions**, **disambiguation** fields, anchor hex refs. | `schemas/lexical_concept/dict_b.schema.json`, `tools/validate_dict_b_dlcr.py`, dict_b packs | M | Real semantic middle layer | PO-02 | Validator + sample rows for exclusions/disambiguation; schema version bump recorded. |
| PO-06 | **5** | **Deterministic resolver** core: **exact > lemma > stem** priority frozen in code + spec. | `core.resolver`, `SPEC__Resolver` | M | Winner + reason reproducible | PO-05 | Resolver golden files: priority inversions impossible without semver bump. |
| PO-07 | **5** | **Context** + **coherence** scoring (deterministic features only). | `core.resolver`, optional `core/lexical` features | L | Better competition on ambiguous spans | PO-06 | Fixed-input_context fixtures; scores stable across platforms. |
| PO-08 | **5** | **Specificity bias** + **fixed tie-break** table (documented order). | `core.resolver`, canon doc | M | Ends “category theater” ties | PO-07 | Table mirrored in spec + test for each tie class. |
| PO-09 | **6** | **Audit-trace** in execution_flow output: normalized span, candidates, scores, rule ids, **rejected** alts. | `hesperia.engine.lexical_concept.execution_flow`, `resolver_output.schema.json` | M | Inspectable decisions; CI/human trust | PO-06 | Full trace validates against schema; snapshot on corpus line. |
| PO-10 | **6** | Debug / **instrumentation JSON** channel (internal envelope) for spans + competition log. | `runtime` diagnostics, `tools/*` writers | S | Codex-friendly dumps | PO-09 | `python3 -m …` or flag writes debug JSON; size bounded. |
| PO-11 | **7** | **Ban direct word→family** on default path: structural aggregation consumes **resolved concept evidence** only. | `sphere.execution_flow` / structural stages, `analysis_service`, guards | L | Family drift drops | PO-06 | Default run: no family activation without concept_id path; **degraded** if fallback used. |
| PO-12 | **7** | **Degraded / fallback** mode explicit in payload (`degraded_path: word_to_family` etc.). | `hesperia.system.capabilities`, projection | S | Auditable shortcuts | PO-11 | Schema-safe flags; product surface unchanged unless allowed. |
| PO-13 | **8** | **Controlled scientific mode** profile: tighter dict slice, stricter phrase priority, less smoothing. | Policy YAML + matcher/resolver params | M | High precision on technical text | PO-03, PO-08 | Profile switch test + corpus precision fixture. |
| PO-14 | **9** | **Speech/clinical mode** profile: stronger transcript norm, more phrase/input_context, smoothing, trajectory coefficient. | Policy YAML + `core.sequence` | M | Messy speech tractable | PO-13 | TFP smoke: profile `clinical_speech` improves bounded metric vs scientific on same transcript. |
| PO-15 | **10** | **Concept→hex projection** on primary structural path (DLCR not optional-only for dev). | `core.hexmap.projection`, `run_dlcr_pipeline`, bridge to structural | L | Hex substrate does real work | PO-09 | E2E: hex state non-empty for anchored concepts; aligns with `SPEC__72k_Phased_Scale`. |
| PO-16 | **11** | **Microstructure inside families**: anchor neighborhoods, variant niches in registry. | `assets/.../anchors`, `core.hexmap.topology` | L | Families not flat buckets | PO-15 | Topology tests: neighbor sets deterministic; no full 72k claim. |
| PO-17 | **12** | **Local smoothing / denoising** over adjacency in hex dynamics (tunable, deterministic). | `core.hexmap.dynamics` | M | Less jumpy classifications | PO-15 | Before/after smoothing: variance ↓ on seeded noise fixture. |
| PO-18 | **13** | **State geometry metrics**: persistence, drift, transition detection (deterministic). | `core.hexmap` analytics component | L | Measures field **shape**, not only counts | PO-17 | Metric vectors match golden on fixed sequence. |
| PO-19 | **15** | **Deterministic semantic locality**: neighbor rings, distance to anchors, sparse cross-family bridges (governed). | `core.hexmap.topology`, canon | L | Locality is formal, not decorative | PO-16 | Invariants doc + tests for distance symmetry on registry graph. |
| PO-20 | **14** | **Trajectory** across **segments** (turn/window/paragraph) in session-oriented flows. | `core.sequence`, `run_dlcr_pipeline`, clinical TFP wiring | M | Dialogue evolution visible | PO-15 | `session_dlcr_bundles` or sidecar includes segment trajectory summary. |
| PO-21 | **14** | Segment **taxonomy** + deterministic boundaries (speaker turns vs paragraphs). | `core.sequence.segmentation` | M | Comparable trajectories across parsers | PO-20 | Unit: same transcript, stable segment count under policy. |
| PO-22 | **16** | **Co-occurrence / PMI** support layer: deterministic association edges from fixed corpus window. | New `core/lexical` or `core/graph` helper (no ML) | L | Richer concept relations | PO-05 | Edge list reproducible from pinned corpus + semver. |
| PO-23 | **16** | Resolver **optional association hints** (bounded influence, logged). | `core.resolver` | M | Disambiguation without probability soup | PO-22 | Case: hint shifts winner with audit line. |
| PO-24 | **17** | **Family/area rollup adapter** from hex state as **preferred** upper raw_text when DLCR path active. | `core.hexmap.aggregate`, sealed / structural adapters | L | Upper architecture preserved, inputs cleaner | PO-15 | Vector sums match hex-derived rollup within ε on fixtures. |
| PO-25 | **17** | **Cross-family relation summaries** derived from spatial state (deterministic rules). | `core.hexmap.aggregate` or sibling | M | Structural summary beyond flat vectors | PO-24 | Golden JSON for relation sketch. |
| PO-26 | **18** | **API/CLI instrumentation**: flags for spans, hex field, transitions, consistency metrics. | `runtime.api`, shipping guards, CLI | L | Operators see real instrumentation | PO-09 | Integration test: flag returns non-empty trace fields. |
| PO-27 | **18** | **Reports** include competition log + dominant regions + transition path (template). | `runtime` artifact writers / templates | M | Human-readable explainability | PO-26 | Sample report artifact in `assets/artifacts/` or `tests/fixtures`. |
| PO-28 | **19** | **Regression suite** expansion: phrase-priority, ambiguity, **drift** after dict edits. | `tools/check_dlcr_regression.py`, corpora | M | Maintainable semantics | PO-03 | CI fails with **corpus + case id** on regression. |
| PO-29 | **19** | **Semver / pin gate**: dict or rule bump requires explicit regression approval artifact. | `tools/release/*` or CI job | M | No silent behavior wreck | PO-28 | Release checklist references pin + report file. |
| PO-30 | **20** | **Domain packs** productized: TFP, psychodynamic, scientific as **switchable** resource bundles + registry. | `assets/data/engine_dynamics_v060`, `assets/version_registry.yaml`, loader | L | One engine, many verticals | PO-13, PO-14 | E2E: switch pack → different concept coverage, same spine modules. |

---

## Option → task coverage (20 → 30)

| Option # | Title | Task IDs |
|----------|-------|----------|
| 1 | Normalization-only | PO-01 |
| 2 | Dict A formal layer | PO-02 |
| 3 | Dict B concept inventory | PO-05 |
| 4 | Phrase-first matcher | PO-03, PO-04 |
| 5 | Deterministic resolver | PO-06, PO-07, PO-08 |
| 6 | Audit-trace | PO-09, PO-10 |
| 7 | Ban direct word→family | PO-11, PO-12 |
| 8 | Scientific mode | PO-13 |
| 9 | Speech/clinical mode | PO-14 |
| 10 | Concept→hex | PO-15 |
| 11 | Microstructure in families | PO-16 |
| 12 | Local smoothing | PO-17 |
| 13 | State geometry | PO-18 |
| 14 | Trajectory | PO-20, PO-21 |
| 15 | Deterministic locality | PO-19 |
| 16 | Co-occurrence / PMI | PO-22, PO-23 |
| 17 | Family/area rollup adapter | PO-24, PO-25 |
| 18 | Instrumentation outputs | PO-26, PO-27 |
| 19 | Regression discipline | PO-28, PO-29 |
| 20 | Domain packs | PO-30 |

---

## Plain-language outcomes (checklist)

After executing waves in order, expect:

1. **Real semantic bridge** — PO-02, PO-05, PO-06, PO-11  
2. **72k substrate purpose** — PO-15 — PO-19 (within phased-scale contract)  
3. **Noisy text consistency** — PO-01, PO-14, PO-17  
4. **Explainability** — PO-09, PO-10, PO-26, PO-27  
5. **Extensibility** — PO-30 (+ PO-13/PO-14)

---

## Related docs

- Closed integration spine: [ETHAN-DLCR-INTEGRATION-20-v0_6_0.md](ETHAN-DLCR-INTEGRATION-20-v0_6_0.md)  
- Runbook: [ETHAN-DLCR-INTEGRATION-RUNBOOK.md](ETHAN-DLCR-INTEGRATION-RUNBOOK.md)  
- Canon hub: `specs/canon/lexical_concept/README.md`  
- Scale note: `specs/canon/lexical_concept/SPEC__72k_Phased_Scale_v0_6_0.md`
