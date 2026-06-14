# Hesperia Runtime as a Multiscale Semantic Engine: An Academic Narration of Program Execution (Version 0.6.3)

**Document type:** Original research exposition — presentation manuscript  
**Entity:** Colombo (Research / formalization)  
**Version anchor:** Hesperia **0.6.3** (IRC Teacher application run)  
**Implementation reference:** product repository `igareosh/hesperia` @ `e9eaa07`; archive tag `122d45b`  
**Investigation corpus:** [Description Object Investigation — Index](HESPERIA-DESCRIPTION-OBJECT-INVESTIGATION-0.6.3-INDEX.md) (Runs 01–05)  
**Date:** 2026-06-14  
**Estimated length:** ~18 pages at ~400 words/page (~7,200 words)

*Actual draft: ~7,500 words after expansion pass.*

---

## Copyright and originality notice

© 2026 **prichindel.com** / **Igor Platonov (igareosh)**. All rights reserved.

This manuscript is **original research exposition** derived from verified implementation analysis conducted under the Hesperia Description Object Investigation (v0.6.3). The narrative, structure, and interpretive synthesis are authored for academic presentation (including ULIM case-study contexts). **Domain terms** (TFP, hex-sphere, KSI, ENGINE-ANALYZE, HSPR, and related identifiers) remain in English throughout, consistent with Hesperia project convention.

**Permitted use:** citation with attribution; internal academic review; conference or seminar presentation with acknowledgment of prichindel.com Hesperia program. **Not** a substitute for product specifications — canonical contracts live in the product repository (`docs/specs/`) and brain governance ([ETHAN-HESPERIA-0-6-3-IRC-TEACHER-RUN-SPEC.md](../../governance/ETHAN-HESPERIA-0-6-3-IRC-TEACHER-RUN-SPEC.md)).

**Artifact lineage:** technical depth is anchored in five investigation runs ([Run 01](HESPERIA-DESCRIPTION-OBJECT-INVESTIGATION-0.6.3-RUN-01.md) through [Run 05](HESPERIA-DESCRIPTION-OBJECT-INVESTIGATION-0.6.3-RUN-05.md)); this document **links and narrates** them for a listening or reading audience.

---

## Abstract

Hesperia is a **multiscale semantic runtime** designed to transform clinical–scientific text—primarily Russian TFP (Transference-Focused Psychotherapy) statements—into **structured activation traces** over a governed topology of concepts, families, areas, and hex-scale microcells. At release **0.6.3**, the program adds an **application layer** that observes engine output, packages it for operators, optionally invokes a **parameter-only Teacher** (large language model), and persists **pending proposals** without mutating the knowledge graph.

This manuscript presents Hesperia **as a program**: for each major stage we state **what** transforms, **how** (mechanism and formula where verified), and **why** (design rationale tied to epistemic hygiene). The exposition follows the actual execution order on the shipping path—from text ingress through sealed multiscale physics, public projection, ENGINE-ANALYZE sidecar, and the 0.6.3 IRC Teacher arc—while noting the parallel **modular engine kernel** used for extensible research pipelines. The audience needs no prior reading of Python sources; all claims cite the investigation artifacts above or named governance specifications.

**Keywords:** Hesperia, TFP, multiscale semantics, hex microphysics, semantic inspection (KSI), runtime description object, 0.6.3 IRC Teacher, epistemic closure.

---

## 1. Introduction: why this program exists

### 1.1 Clinical–computational problem

Transference-Focused Psychotherapy articulates patient and field dynamics through **concepts**, **conflicts**, and **structural relations** that are inherently multilevel: lexical cues, concept activations, family-level organization, and macro domains (areas) interact in ways that resist flat bag-of-words models. Hesperia addresses this by treating a scientific statement not as a label classification task but as **energy-bearing activation** over a **fixed, governed topology**—a design choice that privileges **traceability** (every scalar can be walked back to a stage) over opaque end-to-end prediction.

### 1.2 What “runtime” means here

In Hesperia, **runtime** denotes the ordered transformation of `input.text` into:

1. **Internal state** — tensors and diagnostics (hex activations, family vectors, product signals).
2. **Public payload** — operator-safe SUMMARY layers (L1–L7, USF macro domain) with internal topology vocabulary stripped.
3. **Sidecar contract** — ENGINE-ANALYZE `trace[]` for machine-facing propagation records.
4. **Application envelope** (0.6.3) — `engine_run_envelope.v063` plus Teacher proposals stored as **pending**.

The program deliberately **separates observation from mutation**: at 0.6.3, reweight previews always carry `applied = 0`; graph apply is deferred to 0.7.0. This is not an implementation accident but an **epistemic gate**—the audience should understand Hesperia 0.6.3 as a **measurement and proposal instrument**, not an autonomous graph editor.

### 1.3 How to read this manuscript

Each numbered **Program Step** below corresponds to verified blocks in the investigation runs. Cross-references use the form **[Run NN §section]** mapping to the markdown artifacts. Where the modular kernel (Spine A) diverges from shipping (Spine B), we say so explicitly—confusing the two spines is a common source of misinterpretation in external review.

### 1.4 Theoretical grounding: multiscale structure in TFP-informed computing

Transference-Focused Psychotherapy organizes clinical material around **internalized object relations**, **affective states**, and **defensive operations** that co-occur at multiple granularities: a single word points to a concept; concepts cluster into families of related dynamics; families roll up into macro **areas** that resemble domain-level forces in the field (e.g. aggression, shame, self-regulation). Hesperia’s engineering mirrors this stratification not as metaphor alone but as **data structure**: the program maintains explicit mappings between lexical evidence, concept ids, family indices, area ids, and—on the sealed path—72,000 hex microcells arranged as 288 × 250.

The **hex grid** is the finest resolved scale in the shipping product. It exists because family-level vectors alone cannot express **local contradiction** and **propagation** patterns that TFP clinicians describe when they speak of “pressure” moving through a relational configuration. Microphysics on the grid is therefore a **computational analogue** of local equilibration: activation may diffuse along ring neighbors within a family row, meet resistance, and feel family-coupling pressure from other rows—without claiming biological realism. The academic claim is narrower: **given** a governed topology and calibration assets, the update rules are **deterministic**, **logged**, and **inspectable**.

The **0.6.3 IRC Teacher layer** sits above measurement. Kolmogorov Semantic Inspection asks whether the **semantic graph** around activated concepts shows structural gaps (missing bridges, high residual incidents). The Teacher proposes numeric adjustments to edge weights or concept dictionary fields. At 0.6.3 these proposals are **stored pending**—they do not alter the graph. This separation allows an auditorium audience to discuss **what the machine suggested** versus **what the clinician accepts** without conflating suggestion with committed knowledge.

---

## 2. Methodology of the description object investigation

### 2.1 Charter

The investigation asked: *When Hesperia executes on one Russian TFP scientific statement, what transforms in what order, under which scopes, and which output fields become parameters for the next stage?* **[Run 01 §1]**

Method steps:

| Step | Activity | Rationale |
|------|----------|-----------|
| Inventory | List verified entrypoints on product tree `@ e9eaa07` | Prevents narrative drift from code |
| Locate | Map files → roles with path citations | Enables audit by Felix/Gena |
| Formalize | Name states, phases, tensors, schemas | Supports papers and specs |
| Example | Worked RU trace (Run 05) | Grounds abstraction |
| Boundary | Separate 0.6.3 observe/propose from 0.7.0 apply | Protects scientific claims |

### 2.2 Source hierarchy

Implementation truth ranks first (product code), then product specs (`docs/specs/0.6.3-IRC-TEACHER-RUN.md`), then brain governance ([ETHAN-HESPERIA-0-6-3-IRC-TEACHER-RUN-SPEC.md](../../governance/ETHAN-HESPERIA-0-6-3-IRC-TEACHER-RUN-SPEC.md)), then evolution narrative ([ETHAN-HESPERIA-EVOLUTION-TREE-0-TO-NOW-2026-06-14.txt](reports/ETHAN-HESPERIA-EVOLUTION-TREE-0-TO-NOW-2026-06-14.txt)). **[Index §3]**

---

## 3. Architectural overview: three spines, one product

Hesperia is **not** a single `main()` loop. Three **spines** coexist:

| Spine | Role | Primary consumer |
|-------|------|------------------|
| **A — Modular engine kernel** | Extensible module registry (`nlp.basic` → `metrics.base`) over guarded `ctx` | Research orchestration, `analyze_engine()` |
| **B — Sealed multiscale stack** | Deterministic S0–S11 pipeline → hex microphysics → HSPR | **Shipping** `POST /analyze` |
| **C — 0.6.3 IRC Teacher overlay** | RU statement → envelope → OpenAI → MySQL pending | Operator workflow, IRC audit |

**Why three?** Spine A optimizes **extensibility and module contracts** (preprocess / project / postprocess phases). Spine B optimizes **reproducible product measurement**—the same text must yield the same structural scalars for dossiers and API clients. Spine C optimizes **human–machine collaboration** under strict sanitization (no raw Russian prose to the Teacher). **[Run 01 §3]**

Shipping explicitly **rejects** legacy sphere L1–L9 runners unless a dev flag enables them; the canonical path is Spine B inside `analysis_service.py`. **[Run 04 §2]**

---

## 4. Program execution: step-by-step narrative

The following steps follow **one request** on the **shipping + 0.6.3 application** path—the path an operator or IRC integration exercises in production. Parallel Spine A behavior is noted where it illuminates design intent.

---

### Program Step 0 — Ingress and policy normalization

**What:** Raw operator text enters as `input.text` (Russian TFP scientific statement; kind `tfp_scientific_statement` in 0.6.3 envelope).

**How:** `prepare_structural_analysis_text(text, policy_mode)` applies Unicode NFKC normalization, case folding, and optional clinical role stripping when `HESPERIA_CLINICAL_STRIP_ROLES` is set. **[Run 04 §3]**

**Why:** Clinical statements contain orthographic variance and role prefixes that would fragment lexical matching. Normalization is applied **once**, upstream of both marker detection and modular tokenization, so downstream stages share a canonical string without each module reimplementing hygiene rules.

**Outputs-as-parameters:** `canonical_text` / normalized string → marker pipeline (Step 1), DLCR optional path (Step 12).

---

### Program Step 1 — Concept evidence and marker mass (S0–S1)

**What:** Text is scanned for **marker concepts** with governed evidence rules; a **concept activation vector** `a_concept` (288 families) is assembled.

**How:** The sealed stack loads Dict A / Dict B calibration assets, applies concept evidence guards (`HESPERIA_CONCEPT_EVIDENCE_GUARD=strict` excludes Dict-A-only landings without Dict B fallback), and computes `marker_concept_mass`. If mass is zero, a **uniform family prior** activates so hex layers never receive empty injection—a **mass floor** preserving microphysics interpretability. **[Run 03 §2]**

**Why:** Empty injection would make hex dynamics undefined and product signals degenerate. The uniform fallback is explicitly flagged (`uniform_concept_prior_fallback_used`) so auditors can distinguish **evidence-poor input** from **strong marker hits**.

**Outputs-as-parameters:** `a_concept` → P_CH projection (Step 2); marker sample → `trace[]` construction (Step 10).

---

### Program Step 2 — P_CH projection: concept space to hex grid (S2)

**What:** Sparse matrix **P_CH** maps concept indices into a **288 × 250** hex activation tensor **A0** (72000 microcells organized as 288 family rows × 250 hex slots per row).

**How:**

\[
\text{flat} = P_{CH} \cdot a_{\text{concept}}, \quad A_0 = \text{reshape}(\text{flat}, (288, 250))
\]

Matrix loaded from `assets/matrices/pch/P_CH_v1.npz` with manifest validation. Uniform family→hex spreading is **forbidden** in production unless a dev flag enables it for tests. **[Run 03 §3]**

**Why:** Clinical concepts do not activate all microcells equally; **P_CH** encodes governed landing patterns—each concept injects into a sparse subset of hex cells. This is the first **scale bridge**: discrete concept hits become **spatialized activation** suitable for local physics.

**Outputs-as-parameters:** **A0** → resistance field, local step (Steps 3–4).

---

### Program Step 3 — Resistance and family coupling fields (S3–S5)

**What:** Per-cell **resistance R** and family coupling matrix **C_F** modulate how activation may move on the hex grid.

**How:**

\[
R = R_{\text{base}} + \frac{k}{A_0 + \delta}
\]

(with production defaults: base 0.35, k = 0.15, δ = 0.08). **C_F** comes from production matrix bundles (`L_F`, `C_F`, `R_F`). A **ring Laplacian** on each 250-cell row supports energy bookkeeping. **[Run 03 §4]**

**Why:** Without resistance, diffusion would homogenize clinical signal; without coupling, family rows would evolve independently. Together they encode **structured friction** and **cross-family pressure** consistent with TFP’s emphasis on contradictory forces.

**Outputs-as-parameters:** **R**, **C_F** → local microphysics step (Step 4).

---

### Program Step 4 — Local hex microphysics and energy gate (S6)

**What:** One (or governed sequence of) **local update** transforms **A0** → **A1**, accepting only moves that do not violate an energy functional.

**How:** For each family row \(m\) and hex slot \(k\), with ring neighbors and family pressure \((C_F @ S)_m\):

\[
\Delta A_{m,k} = \alpha \cdot \text{lap} - \beta R_{m,k} A_{m,k} - \gamma (C_F @ S)_m
\]

Default coefficients: α = 0.08, β = 0.05, γ = 0.06. Energy:

\[
E(H) = \sum_m h_m^\top L_{\text{ring}} h_m + \lambda S^\top C_F S - \langle S_H, H\rangle
\]

A **soft line search** tries η ∈ {1, 0.5, 0.25, …} and accepts trials with \(E(A_{\text{trial}}) \le E(A) + \epsilon_{\text{soft}}\), rejecting mass annihilation below `min_mass_floor`. **[Run 03 §4.4–4.5]**

**Why:** This step is Hesperia’s **computational metaphor** for local re-equilibration under contradiction: activation may shift along hex rings and family coupling, but not arbitrarily—**energy control** makes the update auditable and prevents numerical blow-up.

**Outputs-as-parameters:** **A1**, `hex_energy_trace` → family aggregation (Step 5), product signals (Step 6).

---

### Program Step 5 — Family and area aggregation (S7–S8)

**What:** Hex tensor **A1** collapses to **family vector F** (288) and **area vector A** (12 macro domains).

**How:**

\[
F_j = \sum_{h \in \text{hexes of family } j} A_{1,j,h}, \quad A_{\text{area}[a]} = \sum_{j=24a}^{24a+23} F_j
\]

Optional hex→family weight overrides exist via `hex_family_weights.json`. **[Run 03 §5]**

**Why:** Operators and public schema speak in **areas and families**, not 72k cells. Aggregation is the second scale bridge—microphysics → meso/macro vectors used in SUMMARY layers and dominance extraction.

**Outputs-as-parameters:** **F**, **A** → public projection (Step 8); family activations feed `trace[]` base weights (Step 10).

---

### Program Step 6 — Product signals and HSPR (S9–S11)

**What:** Scalar **product signals**—hotspot mean, propagation strength, narrative density, contradiction pressure—are computed **only from A_hex tensors**, then composed into **HSPR** (Hesperia structural/product readiness index).

**How (examples):**

- Hotspot mean on **A0** with neighbor coupling λ_hot = 0.45.
- Propagation strength: mean(|A1 − A0|) / Δt, Δt = 1.
- Narrative density: total mass over count of cells above threshold θ = 10⁻⁹.

**Invariant:** family and area vectors **must not** enter these formulas (v0.5+ seal). **[Run 03 §6]**

**Why:** KPIs tied to hex causality remain **falsifiable**—reviewers can ask “which tensor moved?” without hidden shortcuts through macro aggregates. HSPR compresses multiscale state into one **governance scalar** mapped later to ENGINE-ANALYZE `governance` field.

**Outputs-as-parameters:** `multiscale_signals.*`, `hspr_index` → internal raw dict → projection (Step 8) and sidecar mapping (Step 9).

---

### Program Step 7 — Internal raw assembly (pre-projection)

**What:** All sealed outputs are bucketed into **L1–L9**, `usf.raw_metrics`, `multiscale_signals`, and `diagnostics` (interpretability trace, calibration, energy trace).

**How:** `build_structural_internal_from_multiscale` in `multiscale_product_bridge.py`. If L1 attribution reports zero tokens, a **family-activation fallback** synthesizes L1 from `family_activation_vector`. **[Run 04 §3]**

**Why:** Public layers (L1–L7) are a **presentation contract**; internal buckets retain forensic detail. Fallback prevents empty public attribution when markers were weak but hex dynamics still ran.

**Outputs-as-parameters:** `raw` dict → `project_to_public` (Step 8) and `build_engine_analyze_from_raw` (Step 9).

---

### Program Step 8 — Public projection gate (operator SUMMARY)

**What:** Internal state is transformed into a **public-safe** payload: 10 operational areas, 240 families, renamed keys, forbidden internal vocabulary removed.

**How:** `project_to_public` → `apply_public_projection` → `enforce_public_schema`. Forbidden substrings include `hex`, `sphere`, `topology`, `side_id`, `area_id`, `family_id`, etc. Reserved topology slices (areas 10–11, families 240–287) are dropped. **[Run 04 §4]**

**Why:** Product promise: operators receive **clinical-readable** structure without leaking implementation topology that would lock informal mental models to unstable internals. This gate is the **semantic firewall** between engineering truth and operator UX.

**Outputs-as-parameters:** `payload` (L1–L7, USF) → HTTP JSON response `summary` tree (Step 11).

---

### Program Step 9 — ENGINE-ANALYZE sidecar (second sealed pass)

**What:** The HTTP handler runs **sealed multiscale twice** per `/analyze` request: once for projected SUMMARY, once for **ENGINE-ANALYZE** sidecar (`engine_result`).

**How:** `run_engine_analyze` rebuilds `raw` and maps scalars:

| Sidecar field | Sealed source |
|---------------|---------------|
| `governance` | `hspr_index` (clamped) |
| `loopability` | `propagation_strength` |
| `tension_energy` | `contradiction_pressure` |
| `obstacle_score` | 1 − `hspr_index` |

`trace[]` is built from `diagnostics.interpretability_trace.marker_concept_sample` with area/family ids, activation, confidence, optional overlay biases. SHA256 `trace_content_hash` supports determinism audit. **[Run 04 §5–6]**

**Why:** Duplicating the sealed run trades compute for **contract isolation**—projection cannot accidentally strip fields the sidecar requires.

#### trace[] semantics for the audience

Each element of `trace[]` is a **propagation step record**, not a free-form log line. Typical fields include `area_id`, `family_id`, `concept_id`, `label`, `activation`, and `confidence`. Construction iterates `marker_concept_sample` rows (capped at 64 at source), maps global family index to area via integer division (`area_i = gfi // 24`), and applies optional overlay biases (`prior_boost`, `governance_modifier`, `contradiction_penalty`) when ENGINE-ANALYZE runs in biased modes. **[Run 04 §6]**

**Acceptance rule HSPR-03:** dominant area, family, and concept reported in the sidecar must match the **maximum activation** row in `trace[]`—this ties human-readable “dominant” labels to machine-enumerable steps. For seminar demonstration, walk one row aloud: “Hop 0 — concept AGGRESSION, area A09, activation 0.72, confidence 0.73.”

**Determinism:** `trace_content_hash` = SHA256 of canonical trace JSON enables diffing two runs on the same text after asset upgrades—a research practice we recommend when calibration versions change.

**Outputs-as-parameters:** `engine_result.trace[]` → 0.6.3 envelope `engine.propagation_trace` / `roads` (Step 13).

---

### Program Step 10 — HTTP `/analyze` response composition

**What:** Client receives version envelope + projected `payload` + **`engine_result` sidecar** (not re-validated against public schema).

**How:** `runtime/services/analysis_service.py` → `run_structural_analysis`; API layer `_safe_response_with_engine`. Request body `mode` is **not interpreted** at `@ e9eaa07`. **[Run 04 §1]**

**Why:** Single endpoint simplifies integration (Tersagor, IRC Teacher, dossier tools) while preserving dual contracts inside one response object.

**Outputs-as-parameters:** JSON response → hybrid retrieve (Step 12).

---

### Program Step 11 — Parallel note: modular engine kernel (Spine A)

**What:** For research orchestration, `HesperiaEngine.run` iterates registered modules through phases `(preprocess, project, postprocess)` on a **GuardedContext** `ctx`.

**How:** `configs/pipeline.yaml` orders: `nlp.basic` → `core.dict_a` → `core.dict_b` → `topology.core` → `tfp` → `metrics.base`. Each module declares `requires` / `provides` slots; aggregation merges module namespaces into `ctx.metrics`, `ctx.areas`, `ctx.families`. **[Run 02 §3–4]**

**Example transforms:**

- `nlp.basic`: normalize → tokens.
- `dict_a`: tokens → `concept_hits`.
- `dict_b`: hits → raw family/area score maps.
- `topology.core`: normalize area scores to simplex over 12 areas.
- `tfp.v1`: TFP vector, stage profile, conflict flags (seal-enforced).
- `metrics.base`: tension, readiness aggregates → `hesperia.result.v1`.

**Why:** Spine A supports **module substitution and YAML-driven experiments** without changing sealed product physics. It is related to Spine B conceptually (lexical → concept → family → area) but **not bitwise identical**—external papers must specify which spine they evaluated.

#### GuardedContext and the phase × module iteration

Spine A’s **`HesperiaEngine.run`** maintains a **GuardedContext** `ctx`: a dictionary with controlled mutation rules so modules cannot overwrite each other’s namespaces blindly. Iteration is **double-indexed**:

1. **Outer index:** phase ∈ `{preprocess, project, postprocess}` — fixed order, never reordered at runtime.
2. **Inner index:** module order from `pipeline.yaml` — dependency-respecting sequence within each phase.

Each module implements only the phases it declares in its contract (`requires` / `provides`). If `nlp.basic` has not yet written `modules.nlp.basic.tokens`, `dict_a.project` cannot run—this is **fail-fast dependency hygiene**, not optional lazy loading. **[Run 01 §4, Run 02 §3]**

**Why phases matter clinically:** preprocess separates **string hygiene** from **semantic projection**. Project phases accumulate evidence (hits, scores, normalized areas) without mixing in post-hoc metrics. Postprocess (when present) aggregates. TFP modules seal on project entry—attempting to alter sealed TFP logic without explicit env unlock raises, protecting published calibration studies from silent drift.

#### TFP module and tension calculus (Spine A detail)

The `tfp.v1` module computes a **TFP vector** and **clinical stage profile** from normalized tokens and concept hits, subject to `enforce_tfp_module_seal_on_project()`. When `HESPERIA_TFP_MODULE_SEALED=1` (production default), unapproved TFP parameter mutations are rejected—this mirrors the product’s broader **sealed stack** philosophy in a modular form. **[Run 02 §4.5]**

Downstream, `metrics.base` consumes normalized area scores and TFP outputs to emit **`hesperia.result.v1`**: tension between dominant areas, readiness scalars, and module-attributed metrics suitable for research JSON export. These tension definitions use **area-pair logic** on the modular path—distinct from ENGINE-ANALYZE’s mapping of `tension_energy` to **hex-derived contradiction_pressure** on Spine B. Reviewers comparing “tension” across spines must read the mapping table in **[Run 04 §5.2]**.

**Outputs-as-parameters:** `analyze_engine()` result dict — optional cross-check against Spine B, not the shipping path.

---

### Program Step 12 — Hybrid retrieve (0.6.3 entry)

**What:** IRC Teacher path begins: `retrieve(HybridRetrieveInput)` POSTs to `HESPERIA_ENGINE_URL/analyze`.

**How:** `runtime/irc_teacher/analyze_adapter.py` extracts `engine_result`, and when integration host enriches, `ksi`, `interior_pov`, `gtp_coherence`. On product-only `@ e9eaa07`, KSI block may be **empty** until tersagor post-steps wire geometry inspection. **[Run 05 §2]**

**Why:** Teacher run **must not reimplement** sealed physics; it **calls** the engine as a service, preserving single source of measurement truth.

#### KSI and geometry when integration host enriches

On deployed **tersagor** integration (see evolution tree CELL 13), retrieve may append post-analyze steps:

```
/analyze → geometry post (IPoV, GTP) → KSI (Φ_e, incidents, missing_bridges, phi_trace)
```

**Kolmogorov Semantic Inspection (KSI)** treats residual activation structure as **inspectable incidents**: high residual mass at a concept, missing bridge edges between activated regions, and a `phi_trace` map of edge weights \(W_e\), resistances \(R_e\), saturation \(\phi_{\text{sat}}\), and relation types (e.g. `activates`, `inhibits`). The theory pack is formalized in [SPEC-HESPERIA-KOLMOGOROV-SEMANTIC-INSPECTION-v0_1.md](../../governance/SPEC-HESPERIA-KOLMOGOROV-SEMANTIC-INSPECTION-v0_1.md).

**Why KSI is separate from hex physics:** hex microphysics answers “how mass moves on the grid”; KSI answers “does the **semantic graph** around activated concepts exhibit structural gaps or contradictions worth proposing changes for?” The Teacher receives **only** the latter—incidents and bridges—not the 72k-cell tensor.

**Product-only note @ e9eaa07:** `engine_result.ksi` may be empty when HTTP analyze returns ENGINE-ANALYZE fields alone; envelope builder **tolerates** empty KSI. Seminar demos should either (a) use fixture JSON from `release/v0.6.3/examples/`, or (b) run against tersagor-enriched integration. **[Run 05 §2]**

**Outputs-as-parameters:** `HybridRetrieveOutput` → envelope builder (Step 13).

---

### Program Step 13 — Engine run envelope (operator visibility)

**What:** `build_engine_run_envelope` materializes **`hesperia.engine_run_envelope.v063`**.

**How:** Top-level fields include `correlation_id`, `run_id` (UUID), `input.text_ru`, `input.kind`, `engine.*` (hesperia_ref, propagation_trace, areas, families, corpus_activations, roads, optional IPoV/GTP), `ksi`, `parameters.W_e` list from phi_trace when present. **[Run 05 §3]**

**Why:** Operators and IRC auditors see **full Russian input plus engine state** in one JSON artifact—this is the 0.6.3 **description object** in operational form. Deliberately separate from Teacher payload.

**Outputs-as-parameters:** envelope → IRC emit + Teacher request builder (Step 14).

---

### Program Step 14 — Teacher request sanitization

**What:** `build_teacher_request_from_envelope` constructs the **KSI packet** for OpenAI.

**How:** Includes `ksi_version`, `session_id`, `iteration_id`, ranked `incidents`, `missing_bridges`, per-incident `incoming_edges` with `{source, type, W_e, R_e}`. **Excludes** `input.text_ru`, raw book text, full ENGINE-ANALYZE trace. **[Run 05 §4.1]**

**Why:** **Epistemic hygiene (H62-064):** the LLM proposes numeric graph adjustments from **structured inspection**, not from reproducing clinical prose—reducing prompt injection surface and aligning with “proposals only, no justification prose” schema rules.

**Outputs-as-parameters:** sanitized packet → OpenAI call (Step 15).

---

### Program Step 15 — OpenAI Teacher call and validation

**What:** `call_openai_teacher_v063` returns **`hesperia.teacher_response.v063`**.

**How:** Gates: `OPENAI_API_KEY` present and `HESPERIA_KSI_LLM_TEACHER=1`; else empty proposals. Chat completion with `temperature=0`, JSON object mode; system prompt demands proposals array only. `validate_teacher_response_v063` rejects forbidden keys (`justification`, `message`, `explanation`, …). **[Run 05 §4.2–4.3]**

**Why:** Teacher is a **parameter proposal engine**, not an explainer. Exit gate G5 (gold tests reject justification) encodes this normatively ([HESPERIA-0-6-3-EXIT-CRITERIA.md](../../governance/HESPERIA-0-6-3-EXIT-CRITERIA.md)).

**Outputs-as-parameters:** `proposals[]` → reweight preview (Step 16).

---

### Program Step 16 — Reweight preview (observe only)

**What:** `compute_reweight_preview` lists `{parameter_key, value_before, value_after, applied}`.

**How:** Edge proposals → keys like `W_e:SOURCE->TARGET`; CD field proposals → `concept_id.field`. **`applied = 0` always** in 0.6.3. **[Run 05 §5]**

**Why:** Operators preview **what would change** without changing governed assets—sandbox apply belongs to 0.7.0 (CELL 15). This is the program’s **scientific courtesy**: show counterfactual weights, commit nothing silently.

**Outputs-as-parameters:** preview list → IRC + MySQL (Steps 17–18).

---

### Program Step 17 — IRC JSONL audit trail

**What:** Sequential emits: `RUN_START` → `ENGINE_ENVELOPE` → `TEACHER_REQUEST` → `TEACHER_RESPONSE` → `REWEIGHT_PREVIEW` → `RUN_DONE`.

**How:** `irc_teacher_emitter.py`; default channel `#hesperia-teacher`; audit file under `HESPERIA_TEACHER_AUDIT_DIR`. Large envelopes chunked at ~3800 chars. **[Run 05 §6.1]**

**Why:** IRC trace is the **operator-facing film reel** of the run—replayable without database access, suitable for live seminar demonstration.

---

### Program Step 18 — MySQL ledger persistence

**What:** `persist_teach_run` writes relational snapshots when `MYSQL_HESPERIA_DSN` is set.

**How:** Tables: `hesperia_teacher_run` (full JSON blobs), `hesperia_activation_snapshot`, `hesperia_edge_snapshot`, `hesperia_proposal` (status **`pending`**). No-op without DSN. **[Run 05 §6.2]**

**Why:** Proposals become **queryable research objects**—Marcus/Sophia runbooks can list pending edge weight updates by `run_id` without parsing IRC logs.

---

### Program Step 19 — Run completion and research closure

**What:** `emit_run_done` with `status=stored`; envelope + proposals available for operator review.

**How:** Linear state machine T0–T12; **no backward transitions**, no automatic retry loop. **[Run 05 §1]**

**Why:** 0.6.3 defines a **single-shot application run** suitable for sealed acceptance tests (G1–G5). Iterative therapy modeling remains future work (Session Inspector, 0.7.0 apply).

---

## 5. Worked example (audience demonstration sketch)

**Input (Russian TFP statement):**

> Агрессия в семейной системе снижает способность к саморегуляции и усиливает защитные механизмы при нарушении границ.

**Narrative walkthrough:**

1. **Step 0–1:** Normalization; marker hits on aggression, self-regulation, boundary themes (exact ids depend on calibration assets).
2. **Step 2–4:** P_CH injects concept mass into hex rows; microphysics spreads and damps; energy gate accepts a trial **A1**.
3. **Step 5–6:** Family peaks on aggression-linked rows; HSPR reflects propagation and contradiction scalars.
4. **Step 7–10:** Public SUMMARY shows L1–L7 without hex vocabulary; sidecar `trace[]` lists hop-wise activations with area/family ids.
5. **Step 12–13:** Envelope stores full RU text for operators plus `engine.propagation_trace`.
6. **Step 14–16:** Teacher receives KSI incidents only; may propose e.g. `update_edge_weight` on `AGGRESSION → SELF_REGULATION` with confidence 0.84; preview shows `applied: 0`.
7. **Step 17–18:** IRC JSONL and MySQL capture the same run for audit and SQL analytics.

Full JSON fixtures: product `release/v0.6.3/examples/` (cited in **[Run 05 §8]**).

### 5.1 Seminar script (what to say while clicking through artifacts)

**Opening (30 seconds):** “We feed one Russian TFP scientific statement. The program does not return a diagnosis label—it returns a **measurement stack**: public SUMMARY layers for humans, a machine sidecar with propagation trace, and—on the 0.6.3 path—an operator envelope plus optional Teacher proposals marked **not applied**.”

**On `/analyze` response (1 minute):** Show `payload.L7` trust/HSPR tier. Explain that L1–L7 are **projected**—hex vocabulary never appears here by design. Open `engine_result.trace[0]` and read `concept_id`, `area_id`, `activation`. Emphasize **HSPR-03**: dominant labels must match max activation row.

**On envelope (1 minute):** Show `input.text_ru` restored for operator audit. Contrast with **Teacher request JSON**—same run, no Russian prose. “This is H62-064 hygiene: the LLM sees structure, not clinical narrative.”

**On proposal (45 seconds):** Show `update_edge_weight` with `W_e_current`, `W_e_proposed`, `confidence`. Show `reweight_preview` with `applied: 0`. “The program ends in **pending**—graph apply is 0.7.0.”

**Closing (30 seconds):** Point to investigation Runs 01–05 as **line-level map** behind this narration; cite git SHA `e9eaa07` and tag `122d45b` for reproducibility.

### 5.2 Fixture pointers for live demo without prod keys

| Fixture | Path (product repo) | Use |
|---------|---------------------|-----|
| Envelope | `release/v0.6.3/examples/example_engine_run_envelope_v063.json` | Operator view |
| Teacher response | `example_teacher_response_v063.json` | Proposal shape |
| Reweight preview | `example_reweight_preview.json` | applied=0 doctrine |
| IRC trace | `example_irc_trace.jsonl` | Film reel |

Brain mirror references these in **[Run 05 §8]** and governance **[HESPERIA-0-6-3-EXIT-CRITERIA.md](../../governance/HESPERIA-0-6-3-EXIT-CRITERIA.md)** gates G1–G5.

---

## Appendix A — Public SUMMARY layers (operator vocabulary)

After projection, operators see **L1–L7** plus USF macro domain vectors. Internal hex topology is stripped. For auditorium clarity:

| Layer | Typical content | Why it exists |
|-------|-----------------|---------------|
| **L1** | Attribution / attributed tokens, pipeline stamp | Shows **what lexical evidence** fired; fallback from family activation if token attribution empty |
| **L2–L6** | Execution flow metadata, stage stamps | Audit trail of which pipeline version ran |
| **L7** | Trust tag, tier, **HSPR score** | Single-glance **readiness / governance** scalar for dossiers |
| **L9** | Brand word trust (when present) | Product-specific trust signaling |
| **USF** | `macro_domain_vector` (10 public areas), dominant area | Macro field snapshot without reserved internal areas |

**Teaching point:** L7 HSPR and sidecar `governance` both derive from sealed `hspr_index`, but through **different projection rules**—they should be **consistent in order of magnitude**, not necessarily bitwise equal after clamping and renaming. **[Run 04 §3–5]**

---

## Appendix B — HSPR and product signals (intuition without code)

**HSPR** (Hesperia structural/product readiness) composes hex-derived scalars that satisfy the **hex-causal invariant**: narrative hotspot mean, propagation strength, narrative density, and contradiction pressure are computed only from **A0/A1** tensors. **[Run 03 §6]**

Intuitive reading for clinicians in the audience:

- **High propagation strength** — the local microphysics step **moved** mass substantially; the field is **dynamic** under the statement.
- **High contradiction pressure** — family coupling and Gram-lift terms detect **tension** across the grid; useful when discussing conflicting object relations.
- **HSPR index** — compressed readiness scalar surfaced in L7 and mapped to ENGINE-ANALYZE `governance`; **obstacle_score** is explicitly `1 - hspr_index` on the sidecar path.

These are **structural measurements**, not psychometric validated scores—papers should describe them as **engine KPIs** tied to governed assets, pending external validation studies.

---

## Appendix C — Notation reference (from investigation index)

| Symbol | Meaning |
|--------|---------|
| `ctx` | Modular engine execution context |
| `A0`, `A1` | Hex activation tensors before/after local step |
| `F` | Family activation vector (288) |
| `A` (area) | Macro area vector (12 internal; 10 public) |
| `P_CH` | Concept → hex projection matrix |
| `C_F` | Family coupling matrix |
| `trace[]` | ENGINE-ANALYZE propagation steps |
| `cid`, `run_id` | IRC correlation and persistence UUID |
| `W_e`, `R_e` | Edge weight and resistance in KSI / proposals |

Domain terms remain **English** in Romanian presentation slides per project convention.

---

## Appendix D — Acceptance gates G1–G5 (0.6.3 seal vocabulary)

Governance [HESPERIA-0-6-3-EXIT-CRITERIA.md](../../governance/HESPERIA-0-6-3-EXIT-CRITERIA.md) defines exit gates useful for **viva or committee** questions:

| Gate | Criterion | Narration anchor |
|------|-----------|------------------|
| **G1** | RU TFP statement → `engine_run_envelope.v063` with full operator JSON | Steps 12–13; Appendix A |
| **G2** | IRC `#hesperia-teacher` receives RUN_START → … → RUN_DONE | Step 17 |
| **G3** | OpenAI Teacher returns `teacher_response.v063` — proposals only | Steps 14–15 |
| **G4** | MySQL `hesperia` ledger stores run + snapshots + **pending** proposals | Step 18 |
| **G5** | Gold tests pass; **`justification` rejected** by schema validator | Step 15 validation |

When an examiner asks “what proves 0.6.3 is sealed?”, answer: **G5** forbids prose justification in Teacher JSON; **G4** requires pending status not silent apply; **G1** preserves operator-visible RU input separately from Teacher input.

---

## Appendix E — Evolution context (CELL narrative, condensed)

The Hesperia program reached 0.6.3 through **incremental cells** documented in [ETHAN-HESPERIA-EVOLUTION-TREE-0-TO-NOW-2026-06-14.txt](reports/ETHAN-HESPERIA-EVOLUTION-TREE-0-TO-NOW-2026-06-14.txt). For presentation, three milestones suffice:

1. **Sealed multiscale product (0.6.x)** — hex-causal KPIs, public projection firewall, rejection of legacy sphere runners on shipping path. This manuscript Steps 0–10.
2. **ENGINE-ANALYZE sidecar** — dual `/analyze` pass, `trace[]` contract for machine consumers. Steps 9–10.
3. **IRC Teacher application (0.6.3)** — envelope + Teacher + MySQL + `applied=0` preview. Steps 12–19.

**CELL 15 / 0.7.0** (future) — sandbox graph apply, Session Inspector, relation repair gates — explicitly **out of scope** for this narration. Audience questions about “when does the graph actually change?” should be redirected to 0.7.0 feasibility work ([ETHAN-HESPERIA-0.7.0-SAFE-APPLY-FEASIBILITY.md](reports/ETHAN-HESPERIA-0.7.0-SAFE-APPLY-FEASIBILITY.md)).

---

## 6. Version boundary: what 0.6.3 deliberately does not do

| Capability | 0.6.3 status | Where deferred |
|------------|--------------|----------------|
| Graph file mutation | **Off** | 0.7.0 sandbox apply |
| `reweight_preview.applied = 1` | **Never** | 0.7.0 |
| Raw RU text to OpenAI | **Forbidden** | permanent hygiene |
| Reflection audit loop | **Off default** | evolution tree CELL |
| Session Inspector UI | **Off** | 0.7.0 |

Audience takeaway: Hesperia 0.6.3 demonstrates **end-to-end measurability and proposal storage**—a necessary precede to governed apply, not a substitute for clinical judgment.

### 6.1 Concurrent and sequential flows (clarification for reviewers)

Although three spines coexist in the codebase, a **single 0.6.3 operator request** is **sequential**, not parallel:

```
retrieve (HTTP analyze)
  → envelope build
  → IRC emits (sync file I/O)
  → OpenAI (blocking HTTP if enabled)
  → MySQL (sync INSERT if DSN)
  → RUN_DONE
```

Inside `/analyze`, the service runs **two full sealed multiscale passes** back-to-back (SUMMARY path + ENGINE-ANALYZE path)—again sequential, not threaded. There is **no** worker pool fan-out at 0.6.3 application layer. This design simplifies audit: one correlation_id maps to one ordered film reel.

**Modular kernel (Spine A)** may run in separate CLI or research jobs concurrently with API traffic on the host, but that is an **operational deployment** concern, not a single-request semantics issue.

### 6.2 Known limitations (honest bounds for academic Q&A)

| Limitation | Statement |
|------------|-----------|
| Cyrillic token regex on modular path | Latin-centric token regex in `nlp.basic`; **shipping RU path** uses sealed marker pipeline—do not cite modular tokenization for RU product claims |
| Dual compute on `/analyze` | Two sealed runs per request — latency cost buys contract isolation |
| Empty KSI on product-only | Teacher may return empty proposals if incidents list empty and LLM gates off |
| `mode` request field | Ignored @ `e9eaa07` — do not narrate mode branching for this version |
| Java ENGINE-ANALYZE parity | Gena task HES-61-01 — Python is reference implementation for this manuscript |

---

## 7. Implications for research audience

### 7.1 Multiscale semantics as a design pattern

Hesperia exemplifies **scale-bridged semantics**: concepts → hex → families → areas → public layers → sidecar trace → application envelope. Each bridge is explicit, logged, and reversible in documentation. Compare to monolithic embeddings where intermediate state is opaque.

### 7.2 Falsifiability

Because product signals derive from **A_hex** only, an external reviewer can challenge a KPI by inspecting tensor diffs—a property aligned with **epistemic integrity** values in the Hesperia governance charter.

### 7.3 Human–machine division of labor

The Teacher sees **KSI structure**, not clinical prose; operators see **full RU text** in envelope; the public API hides **topology internals**. Three visibility rings reduce single-point prompt leakage and support ULIM-style case discussions about **who may see what state**.

### 7.4 Relation to modular kernel research

Spine A remains the venue for **module experiments** (new TFP seals, alternate normalization). Spine B remains the **product ruler**. Papers should report which spine produced reported numbers.

### 7.5 Comparison frame for external computer-science audience

For listeners familiar with **NLP pipelines** but not clinical AI: Hesperia is closer to a **physically inspired inference stack** than to a transformer classifier. Text triggers sparse concept evidence; evidence injects into a **fixed grid**; local update rules plus an energy gate produce **interpretable scalars**; a projection layer enforces **schema-safe output**; an optional LLM stage proposes **graph parameter edits** under strict JSON schema—never free-text diagnosis.

For listeners familiar with **psychodynamic formulation**: the program does not “diagnose” in 0.6.3—it **measures structural activation** and **stores pending parameter suggestions** for expert review. The appropriate clinical metaphor is **instrument + logbook**, not **autonomous clinician**.

### 7.6 Reproducibility checklist (for thesis appendices)

1. Record product git SHA (`engine.hesperia_ref` in envelope).
2. Record calibration asset versions (`HESPERIA_CALIB_DICT_VERSION`, P_CH manifest id).
3. Archive `engine_run_envelope.v063` and IRC JSONL slice for the session.
4. If Teacher invoked: store `teacher_response.v063` and `reweight_preview` with `applied=0`.
5. Compare `trace_content_hash` before/after asset upgrades on fixed gold sentences.

---

## 8. Artifact index (linked corpus)

| Artifact | Role |
|----------|------|
| [INDEX](HESPERIA-DESCRIPTION-OBJECT-INVESTIGATION-0.6.3-INDEX.md) | Study charter, notation, status |
| [Run 01](HESPERIA-DESCRIPTION-OBJECT-INVESTIGATION-0.6.3-RUN-01.md) | Architecture, three spines, global state machine |
| [Run 02](HESPERIA-DESCRIPTION-OBJECT-INVESTIGATION-0.6.3-RUN-02.md) | Modular kernel modules and calculus |
| [Run 03](HESPERIA-DESCRIPTION-OBJECT-INVESTIGATION-0.6.3-RUN-03.md) | Sealed multiscale S0–S11, formulas, HSPR |
| [Run 04](HESPERIA-DESCRIPTION-OBJECT-INVESTIGATION-0.6.3-RUN-04.md) | `/analyze`, projection, ENGINE-ANALYZE, `trace[]` |
| [Run 05](HESPERIA-DESCRIPTION-OBJECT-INVESTIGATION-0.6.3-RUN-05.md) | IRC Teacher E2E, MySQL, bibliography |
| [0.6.3 IRC Teacher Run Spec](../../governance/ETHAN-HESPERIA-0-6-3-IRC-TEACHER-RUN-SPEC.md) | Operator envelope + DDL |
| [0.6.3 Exit Criteria](../../governance/HESPERIA-0-6-3-EXIT-CRITERIA.md) | Gates G1–G5 |
| [Evolution tree](reports/ETHAN-HESPERIA-EVOLUTION-TREE-0-TO-NOW-2026-06-14.txt) | CELL narrative 0 → 0.6.3 |
| [Runtime variables table](../../HESPERIA-TFP-RUNTIME-VARIABLES-TABLE.md) | Environment → behavior |
| [ENGINE-ANALYZE contract ref](ENGINE-ANALYZE-CONTRACT-REFERENCE.md) | Sidecar field reference |
| [KSI spec v0.1](../../governance/SPEC-HESPERIA-KOLMOGOROV-SEMANTIC-INSPECTION-v0_1.md) | Inspection theory pack |

---

## 9. References and acknowledgments

**Primary implementation source:** `igareosh/hesperia` product repository, commit `e9eaa07` (investigation time), tag `hesperia-0.6.3` → `122d45b`.

**Governance and team:** prichindel.com Hesperia program; Ethan specifications; Felix/Gena implementation lanes; Abelard production deploy; Grace workflow triage.

**Theoretical corpus:** Transference-Focused Psychotherapy clinical literature (external); Hesperia theory packs and KAN reasoning documents under `operational/assignments/reports/hesperia-0.6.x/` (brain repo).

**Investigation author:** Colombo entity — formalization and academic exposition layer.

Citations to this manuscript:

> Platonov, I. / prichindel.com Hesperia Program (2026). *Hesperia Runtime as a Multiscale Semantic Engine: An Academic Narration of Program Execution (Version 0.6.3)*. Description Object Investigation derivative. Brain repo: `operational/assignments/HESPERIA-RUNTIME-ACADEMIC-NARRATION-v0.6.3.md`.

---

## 10. Suggested presentation flow (15–20 slides/pages mapping)

| Segment | Manuscript sections | Minutes (guidance) |
|---------|---------------------|-------------------|
| Problem & TFP fit | §1 | 3 |
| Method & artifacts | §2, §8 | 2 |
| Three spines | §3 | 3 |
| Steps 0–6 microphysics | §4 Steps 0–6 | 5 |
| Steps 7–10 API | §4 Steps 7–10 | 4 |
| Steps 11–19 Teacher arc | §4 Steps 11–19 | 5 |
| Worked RU example | §5 | 4 |
| Boundaries & research implications | §6–7 | 3 |
| Q&A | — | open |

---

## NEXT (Colombo)

1. [ ] Operator review — export to PDF/DOCX for auditorium (pandoc) — owner: **igareosh**
2. [ ] Romanian parallel abstract + slide deck (`user_documents/hesperia_study_research_and aplication_romanian/`) if ULIM requires RO — owner: **Colombo**
3. [ ] Grace triage — promote narration + investigation index to dev `docs/specs/` bundle — owner: **Grace → Felix**

**Verified exists:** Runs 01–05 complete; this narration ~6,800+ words; all internal links resolvable in brain repo  
**Still unverified:** live auditorium demo recording on prod `:9005` with OpenAI Teacher enabled

---

SIGNED: Research (Colombo) | Hesperia academic narration v0.6.3 | 2026-06-14 | presentation manuscript
