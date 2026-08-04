#!/usr/bin/env python3
"""Generate the Hesperia parameter/variable wiki: one page per item, category hubs, index.
Run once; re-run to regenerate (idempotent, overwrites pages/ and categories/ + index.md).
Also emits index.json — the structured, machine-readable mirror of ITEMS that
agent_mcp_hesperia_wiki (HWIKI-MCP-01) and the code<->wiki linker (HWIKI-MCP-04) read.
index.json is DERIVED from ITEMS below, never hand-edited — same durability rule as the .md pages."""
import datetime
import json
import os
import re

ROOT = "/data/altitudine/prichindel.com/colombo_research/hesperia/wiki"
PAGES = os.path.join(ROOT, "pages")
CATS = os.path.join(ROOT, "categories")

LAN_URL = "http://192.168.100.65:8901"
TAILNET_URL = "http://100.89.236.59:8901"

def slug(name):
    s = re.sub(r"[^a-zA-Z0-9]+", "-", name).strip("-")
    return s

STATUS_LABEL = {
    "LIVE_FULL": "🟢 LIVE_FULL — matches proposal (if any), running in production path",
    "LIVE_SUCCESSOR": "🟢 LIVE_SUCCESSOR — same idea, different name/formula than any Java ancestor",
    "PARTIAL": "🟡 PARTIAL — present in a narrow slice/tool, not the full contract",
    "DEAD": "🔴 DEAD — no implementation under this name or a successor formula",
    "DEAD_ALGO_SURVIVED": "🔴 DEAD (name) / 🟢 ALGORITHM SURVIVED — see linked live page",
    "BEYOND": "🔵 BEYOND — shipped in LIVE, not proposed in the Java corpus",
    "UNVERIFIED": "⚪ UNVERIFIED — claimed in an earlier doc, did not re-confirm by grep this pass",
    "REJECTED": "🔴 REJECTED — explicit, reasoned decision against, not an oversight",
}

# ---------------------------------------------------------------------------
# Data: (name, category, status, kind, module, value, formula, produced_from, needed_by, origin, notes)
# produced_from / needed_by: list of strings — linked automatically if they match another page name
# ---------------------------------------------------------------------------
ITEMS = []

def add(name, category, status, kind, module, value, formula, produced_from, needed_by, origin, notes):
    ITEMS.append(dict(name=name, category=category, status=status, kind=kind, module=module,
                       value=value, formula=formula, produced_from=produced_from, needed_by=needed_by,
                       origin=origin, notes=notes))

CAT_GEOMETRY = "Geometry"
CAT_COREMATH = "Core Math Contract"
CAT_TENSION = "Tension and Bipolar Adversity"
CAT_PROP = "Propagation, Diffusion and Markov"
CAT_THRESH = "Activation and Diagnostic Thresholds"
CAT_GRAPH = "Graph and Structural Metrics"
CAT_ENTROPY = "Entropy and Information Theory"
CAT_STABILITY = "Stability and Control Theory"
CAT_SIM = "Similarity and Retrieval"
CAT_TRUST = "Evidence and Trust"
CAT_CD = "Concept Dictionary"
CAT_DEAD = "Dead and Rejected Science"

CATEGORIES = [CAT_GEOMETRY, CAT_COREMATH, CAT_TENSION, CAT_PROP, CAT_THRESH, CAT_GRAPH,
              CAT_ENTROPY, CAT_STABILITY, CAT_SIM, CAT_TRUST, CAT_CD, CAT_DEAD]

# HWIKI-DOC-29 — how-to-read preambles for cold agents (Geometry / Core Math / Propagation)
CATEGORY_PREAMBLES = {
    CAT_GEOMETRY: (
        "**How to read this map (HWIKI-DOC-29):** Geometry is the *substrate* — 12 areas forced by an icosahedron "
        "built with [[PHI (golden ratio)|φ]], not an arbitrary design choice. Start at [[Icosahedral Surface Graph]] "
        "(5-regular) before tension or DFT claims. Theory spine: Platonic topology → embedding validation → "
        "why [[DFT Ring Smoothness]] is REJECTED."
    ),
    CAT_COREMATH: (
        "**How to read this map (HWIKI-DOC-29):** Core Math is the *contract spine* — fuse ([[alpha (fusion weight)|α]], "
        "[[E_cap]], [[eta (centroid threshold)|η]]) → lazy step ([[lambda (lazy step)|λ]]) → five-penalty "
        "[[metric_governance|governance]]. Read Theory Explainer blocks for authors/extent. Contrast REJECTED "
        "[[KL divergence]] (zeros from η+clamp) and dead Java integrity quartet."
    ),
    CAT_PROP: (
        "**How to read this map (HWIKI-DOC-29):** Propagation is *diffusion on neighborhoods* — YAML radial weights "
        "(center→inner→middle→outer + bridge) feed how mass spreads; [[Transition matrix (W)]] + [[lambda (lazy step)|λ]] "
        "are the Markov-like walk; [[Chapman-Kolmogorov Multi-Step]] and [[Mixing Diagnostics]] are multi-step "
        "diagnostics. PageRank is a [[PageRank-shaped walk (structural analogy)|structural analogy]] only."
    ),
}

# ===== GEOMETRY =====
add("AREAS", CAT_GEOMETRY, "LIVE_FULL", "Parameter (constant)",
    "sphere/topology/, core/topology/ (invariants, dict_b)", "12",
    "Fixed ontology grain — 12 areas = 12 icosahedron vertices.",
    [], ["FAMILIES_PER_AREA", "TOTAL_FAMILIES", "Icosahedral Surface Graph", "compute_tension"],
    "Java 20_GEOMETRY (`final int AREAS = 12`); geometric root: regular icosahedron / Platonic solid",
    "Every area-activation vector has length 12. Sigma shape checks fail if this drifts.")

add("FAMILIES_PER_AREA", CAT_GEOMETRY, "LIVE_FULL", "Parameter (constant)",
    "gcs_lookup, core/topology/", "24", "Families per area, fixed ontology grain.",
    ["AREAS"], ["TOTAL_FAMILIES"], "Java 20_GEOMETRY", "")

add("TOTAL_FAMILIES", CAT_GEOMETRY, "LIVE_FULL", "Derived variable",
    "throughout core/", "288", "TOTAL_FAMILIES = AREAS × FAMILIES_PER_AREA = 12 × 24",
    ["AREAS", "FAMILIES_PER_AREA"], ["F_vec[288]", "detect_dominant_family"],
    "Java 20_GEOMETRY (product)", "Family-activation vector length; Sigma shape check.")

add("HEXES_PER_FAMILY", CAT_GEOMETRY, "PARTIAL", "Parameter (constant)",
    "hex builders", "250 (GCS defect variant: 251)",
    "Hex substrate resolution — finest landing grain before rollup.",
    ["FAMILIES_PER_AREA"], ["TOTAL_HEXES"], "Java 20_GEOMETRY",
    "The 251 GCS-defect variant is a PARTIAL branch, not the base 250 — disclose 72,000 vs 72,240 if claiming a hex census.")

add("TOTAL_HEXES", CAT_GEOMETRY, "LIVE_FULL", "Derived variable",
    "hex census tooling", "72,000 (72,240 GCS defect variant)",
    "TOTAL_HEXES = TOTAL_FAMILIES × HEXES_PER_FAMILY; Euler's theorem requires 12 pentagon defects to close a hex sphere, which produces the 72,240 GCS variant.",
    ["TOTAL_FAMILIES", "HEXES_PER_FAMILY"], [], "Java 20_GEOMETRY + Euler closed-sphere constraint (SCIENCE.md)", "")

add("SIDES_PER_HEX", CAT_GEOMETRY, "LIVE_FULL", "Parameter (constant)",
    "geometry checks", "6", "Hexagonal lattice uniform adjacency — 6 sides per hex.",
    [], ["TOTAL_SIDES"], "Java 20_GEOMETRY", "Dimensionality of energy sides / truth units.")

add("TOTAL_SIDES", CAT_GEOMETRY, "LIVE_FULL", "Derived variable",
    "docs/catalog", "432,000", "TOTAL_SIDES = TOTAL_HEXES × SIDES_PER_HEX (using the 72,000 base variant)",
    ["TOTAL_HEXES", "SIDES_PER_HEX"], [], "Java 20_GEOMETRY (product)", "Absolute side census from the Java corpus.")

add("PHI (golden ratio)", CAT_GEOMETRY, "LIVE_FULL", "Parameter (constant)",
    "sphere/topology/embedding.py", "(1 + √5) / 2 ≈ 1.618033988749895",
    "Coordinate generator for the 12 icosahedron vertices (`ICOSAHEDRON_VERTICES_RAW`).",
    [], ["Icosahedral Surface Graph", "angular_distance", "geodesic_distance"],
    "Classical geometry (φ = (1+√5)/2) — Theory Explainer: plain_lang: the golden ratio is the scale that appears when you build a regular icosahedron from unit coordinates; Hesperia uses it so the 12 area points sit on a true Platonic solid, not an arbitrary cloud. author: classical Greek geometry / Euclidean solid construction (not a Hesperia-native invention). extent: full (verbatim φ in `ICOSAHEDRON_VERTICES_RAW`). reasoning: SCIENCE.md — 12 areas are geometrically forced by this construction. application: [[Icosahedral Surface Graph]], [[angular_distance]], [[geodesic_distance]].",
    "**HWIKI-DOC-09:** Verified in `embedding.py`. Java corpus stated AREAS/FAMILIES as bare integers without embedding — φ is LIVE geometry, not a Java carry-over name.")

add("Icosahedral Surface Graph", CAT_GEOMETRY, "LIVE_FULL", "Topology (structural fact)",
    "assets/topology/area_adjacency_matrix.json, sphere/topology/embedding.py",
    "12 nodes, 30 edges, 5-regular (`degree_per_node: 5`)",
    "The 12 areas are literal icosahedron vertices; `validate_embedding_matches_topology` enforces that every graph edge has near-equal angular length and every non-edge is strictly longer.",
    ["AREAS", "PHI (golden ratio)"], ["compute_tension", "angular_distance", "DFT Ring Smoothness"],
    "Regular icosahedron (Platonic solid) — Theory Explainer: plain_lang: think of the 12 therapy areas as the corners of a 20-faced solid; each corner touches exactly five others (5-regular), so 'next area' is neighborhood on a sphere, not a circle. author: Platonic solid / icosahedron topology. extent: full (adjacency JSON + embedding validation). reasoning: this graph is the substrate for tension and for rejecting ring-DFT. application: [[compute_tension]], [[OPPOSITE_OFFSET]], contrast [[DFT Ring Smoothness]].",
    "**HWIKI-DOC-10:** **Decisive fact against DFT Ring Smoothness**: a meaningful ring-DFT needs a 2-regular cyclic graph (C₁₂); the built topology is 5-regular. See [[DFT Ring Smoothness]].")

# ===== CORE MATH CONTRACT =====
add("alpha (fusion weight)", CAT_COREMATH, "LIVE_FULL", "Parameter (default constant)",
    "core/math/core_math.py", "0.65",
    "E0[i] = clamp(alpha·S'[i] + (1-alpha)·L'[i], 0, E_cap) — 65/35 surface-biased weighted fusion of two normalized evidence vectors S (Dict A) and L (Dict B).",
    ["S vector (Dict A)", "L vector (Dict B)"], ["centroid indices (activation)", "E0 (fused energy)", "eta (centroid threshold)"],
    "22_SPEC Core Math Contract v1.0 §3 — Theory Explainer: plain_lang: blend two evidence maps into one energy field; α=0.65 leans toward Dict A (surface). author: convex combination / linear scalarization (ops research pattern; not a single eponym paper). extent: full. reasoning: first stage of evidence fusion before centroid/η and diffusion. application: [[E_cap]], [[eta (centroid threshold)]], [[P_thin (thin-core penalty)]]; contrast dead [[KL divergence]].",
    "**HWIKI-DOC-25 (fusion trio):** With [[E_cap]] and [[eta (centroid threshold)]] this is the LIVE fusion spine. Distinct from diffusion α / [[Wiener feedback on alpha (k_s / k_j)]].")

add("E_cap", CAT_COREMATH, "LIVE_FULL", "Parameter (constant)",
    "core/math/core_math.py", "1.0", "Clamp ceiling applied after fusion and after every diffusion step.",
    ["alpha (fusion weight)"], ["alpha (fusion weight)", "lambda (lazy step)", "eta (centroid threshold)"],
    "22_SPEC §3 — Theory Explainer: plain_lang: no activation cell may exceed 1.0; the field stays a bounded probability-like surface. author: 22_SPEC Core Math Contract. extent: full. reasoning: normalized bounded field + with η manufactures exact zeros that kill KL. application: [[alpha (fusion weight)]], [[lambda (lazy step)]], [[KL divergence]] (REJECTED).",
    "**HWIKI-DOC-25:** Clamp after fusion and diffusion — partner of [[eta (centroid threshold)]] in the structural-zero story.")

add("eta (centroid threshold)", CAT_COREMATH, "LIVE_FULL", "Parameter (constant)",
    "core/math/core_math.py — centroid_indices()", "0.02",
    "active = [i for i in range(len(E0)) if E0[i] > eta] — sparse centroid selection floor.",
    ["alpha (fusion weight)", "E_cap"], ["K_max", "KL divergence"],
    "22_SPEC §4 — Theory Explainer: plain_lang: ignore near-zero energy cells when picking the 'active' centroid set. author: 22_SPEC Core Math Contract. extent: full. reasoning: sparse activation; **structural reason [[KL divergence]] is REJECTED** (zeros in q). application: [[K_max]], contrast [[compute_entropy (Shannon)]].",
    "**HWIKI-DOC-25:** With [[E_cap]] + clamp, η is why centroid selection kills KL — not taste.")

add("K_max", CAT_COREMATH, "LIVE_FULL", "Parameter (constant)", "core/math/core_math.py", "5",
    "Cap on the number of centroid indices selected.", ["eta (centroid threshold)"], [], "22_SPEC §4",
    "Caps 'how many things are active' in one traversal.")

add("lambda (lazy step)", CAT_COREMATH, "LIVE_FULL", "Parameter (constant)",
    "core/math/core_math.py — base_step()", "0.55",
    "D = (1-lambda)·E + lambda·(E·W) — lazy Markov chain step: a (1-lambda) fraction stays put, lambda actually transitions via W.",
    ["E_cap", "Transition matrix (W)"], ["decay", "Chapman-Kolmogorov Multi-Step", "Wiener feedback on alpha (k_s / k_j)", "PageRank-shaped walk (structural analogy)"],
    "Markov (1906) — Theory Explainer: plain_lang: each step keeps part of current energy and mixes in neighbor energy; λ is how much of the mix comes from the graph. author: A.A. Markov (1906) chain formalism; laziness = standard aperiodicity technique. extent: structural_analogy (hand-set weights, not fitted HMM). reasoning: 22_SPEC base_step; 'Markov-like' discipline in SCIENCE.md. application: [[Transition matrix (W)]], T_steps=8, [[Chapman-Kolmogorov Multi-Step]], [[PageRank-shaped walk (structural analogy)]], diffusion α modulated by [[Wiener feedback on alpha (k_s / k_j)]].",
    "**HWIKI-DOC-04 / DOC-08:** Iterated T_steps=8 times per run. Terminology discipline: 'Markov-like', never 'fitted Markov chain / HMM' — weights are hand-set, not learned. Same lazy form is the PageRank structural analogy (SCIENCE.md) — see [[PageRank-shaped walk (structural analogy)]]. Distinct from [[Wiener feedback on alpha (k_s / k_j)]] which modulates *diffusion* α in `sphere/propagation/weighting.py`, not this fusion/lazy λ.")

add("decay", CAT_COREMATH, "LIVE_FULL", "Parameter (constant)",
    "core/math/core_math.py — base_step()", "0.04",
    "E_next = clamp(D·(1-decay), 0, E_cap) — damped discrete-time attrition after each diffusion step.",
    ["lambda (lazy step)"], [], "22_SPEC §5",
    "Structural analogy to LIF self-decay (Lapicque 1907) noted in related H_self paths; not claimed as literal.")

add("shadow_step", CAT_COREMATH, "LIVE_FULL", "Formula / function",
    "core/math/core_math.py", "—", "E_shadow = E · Ws — propagation through a separate shadow transition matrix Ws.",
    ["E (energy vector)"], ["P_shadow (shadow-hop penalty)", "check_shadow_non_creation"], "22_SPEC §6",
    "Shadow field for fallback / correction cost.")

add("P_amb (ambiguity penalty)", CAT_COREMATH, "LIVE_FULL", "Formula / penalty",
    "core/math/core_math.py", "k_amb = 0.35, delta_gap = 0.08",
    "gap = (e1-e2)/(e1+eps); P_amb = k_amb·(1-gap)^2 — taxes a too-close top-1/top-2 energy gap; degraded flag if gap < delta_gap.",
    ["base_step"], ["metric_governance"], "22_SPEC §8 — Theory Explainer: plain_lang: if top-1 and top-2 energies are almost tied, tax governance — the read is ambiguous. author: 22_SPEC penalty suite. extent: full. reasoning: independently tunable additive term. application: [[metric_governance]].",
    "**HWIKI-DOC-23:** Member of the five-penalty suite → [[metric_governance]].")

add("P_thin (thin-core penalty)", CAT_COREMATH, "LIVE_FULL", "Formula / penalty",
    "core/math/core_math.py", "k_thin = 0.30, tau_core = 0.25",
    "CoreShare = sumS/(sumS+sumL+eps); P_thin = k_thin·(1-CoreShare) — taxes energy leaning too much on Dict B (L) vs Dict A (S).",
    ["alpha (fusion weight)"], ["metric_governance"], "22_SPEC §9 — Theory Explainer: plain_lang: if the fused field leans too hard on Dict B vs Dict A, tax it as a thin core. author: 22_SPEC penalty suite. extent: full. reasoning: protects surface-biased fusion intent of [[alpha (fusion weight)]]. application: [[metric_governance]].",
    "**HWIKI-DOC-23:** Member of the five-penalty suite → [[metric_governance]].")

add("P_disp (dispersion penalty)", CAT_COREMATH, "LIVE_FULL", "Formula / penalty",
    "core/math/core_math.py", "k_disp = 0.25",
    "P_disp = k_disp·H_norm, H_norm = H/ln(M) — normalized Shannon entropy of E_end over active sides.",
    ["compute_entropy (Shannon)"], ["metric_governance"], "22_SPEC §10 — Theory Explainer: plain_lang: smear across many sides → higher dispersion tax. author: Shannon entropy reused as penalty input. extent: full. reasoning: same H tool as [[compute_entropy (Shannon)]]. application: [[metric_governance]].",
    "**HWIKI-DOC-23:** Member of the five-penalty suite → [[metric_governance]].")

add("P_guard (guard penalty)", CAT_COREMATH, "LIVE_FULL", "Formula / penalty",
    "core/math/core_math.py", "k_guard = 0.30",
    "P_guard = clamp(k_guard·(sigma_fail+gamma_violation+theta_reject), 0, 1) — Sigma/Gamma/Theta guard failures taxed directly into governance.",
    ["Sigma/Gamma/Theta guards"], ["metric_governance"], "22_SPEC §11 — Theory Explainer: plain_lang: guard failures are not only hard stops — they also cost governance score. author: 22_SPEC penalty suite. extent: full. reasoning: softens binary gates into a continuous health signal. application: [[metric_governance]], [[metric_obstacle_score]].",
    "**HWIKI-DOC-23:** Member of the five-penalty suite → [[metric_governance]].")

add("P_shadow (shadow-hop penalty)", CAT_COREMATH, "LIVE_FULL", "Formula / penalty",
    "core/math/core_math.py", "k_shadow = 0.40, max_shadow_hops = 2",
    "P_shadow = k_shadow·(shadow_hops/max_shadow_hops) — the largest single weight of the five penalties.",
    ["shadow_step"], ["metric_governance"], "22_SPEC §11 — Theory Explainer: plain_lang: each shadow-propagation hop needed to correct the field costs governance; heaviest single k among the five. author: 22_SPEC penalty suite. extent: full. reasoning: fallback hops are expensive by design. application: [[metric_governance]], [[metric_obstacle_score]].",
    "**HWIKI-DOC-23:** Member of the five-penalty suite → [[metric_governance]].")

add("metric_governance", CAT_COREMATH, "LIVE_FULL", "Composite metric",
    "core/math/core_math.py", "—",
    "metric_governance = clamp(1 − (P_amb+P_thin+P_shadow+P_disp+P_guard), 0, 1) — single health number.",
    ["P_amb (ambiguity penalty)", "P_thin (thin-core penalty)", "P_disp (dispersion penalty)",
     "P_guard (guard penalty)", "P_shadow (shadow-hop penalty)"], [],
    "22_SPEC §12 — Theory Explainer: plain_lang: five independent taxes (ambiguity, thin-core, dispersion, guard, shadow) sum and invert into one 0–1 health score. author: 22_SPEC Core Math Contract (additive penalty-governance pattern). extent: full (suite as one explainable system). reasoning: preferred over Java multiplicative integrity powers — each penalty CI-testable alone. application: governance consumers; pattern reused by [[KME Primitives and Derived Metrics]]; contrast dead [[ALPHA/BETA/GAMMA/DELTA integrity quartet (Java)]].",
    "**HWIKI-DOC-23:** Hub for the penalty suite P_amb/thin/disp/guard/shadow. Clearest 'combine independent criteria into one thresholdable number' example in the repo.")

add("metric_obstacle_score", CAT_COREMATH, "LIVE_FULL", "Composite metric",
    "core/math/core_math.py", "w_decay=0.50, w_guard_obs=0.30, w_shadow_obs=0.20 (CI-enforced sum = 1.0 ± 1e-6)",
    "obstacle_score = w_decay·Loss + w_guard_obs·clamp(GuardCount,0,1) + w_shadow_obs·(shadow_hops/max_shadow_hops)",
    ["decay", "P_guard (guard penalty)", "P_shadow (shadow-hop penalty)"], [],
    "22_SPEC §12 / validate_config §16",
    "Weights encode a judgment (half from decay loss) — building a config where these three don't sum to 1 fails CI.")

add("Energy conservation epsilon", CAT_COREMATH, "LIVE_FULL", "Invariant (constant)",
    "core/math/core_math.py — check_conservation_pre_decay, check_shadow_non_creation", "1e-6",
    "Total energy must be conserved within epsilon after diffusion (E·W), before decay; shadow output must not exceed shadow input.",
    ["lambda (lazy step)", "shadow_step"], [], "22_SPEC — physics-style invariant",
    "Row-stochastic W preserves total mass by construction before decay — this check verifies that construction holds at runtime.")

# ===== TENSION =====
add("compute_tension", CAT_TENSION, "LIVE_SUCCESSOR", "Formula / function",
    "core/result/contract.py:63-65", "—",
    "pairs = (i, i+6) for i in 0..5 on the 12-area vector; tension = Σ|A[i]-A[i+6]| (L1 abs-sum).",
    ["Icosahedral Surface Graph", "A_vec[12] (area activation vector)", "OPPOSITE_OFFSET"], ["Modular tension output (hesperia.result.v1)"],
    "Java 21_MATH `bipolarAxes`: B[k]=A[2k]-A[2k+1], tensionEnergy=ΣB[k]² — interleaved pairing + L2 squares",
    "**HWIKI-OPEN-01 resolved 2026-07-23:** `(i,i+6)` is **not** geometrically antipodal after `get_aligned_area_coordinates`. Ran alignment on canonical adj: geometric antipodes remain `(0,3)(1,2)(4,7)(5,6)(8,11)(9,10)` (dot=-1); `(i,i+6)` dots are ±0.447 (~0.35π / ~0.65π), not antipodal. Live pairing is the combinatorial [[OPPOSITE_OFFSET]]=6 index convention for exclusion/tension — not a claim that area i faces area i+6 on the sphere. Differs from Java also in aggregator (L1 abs-sum vs L2 squares).")

add("metric_tension_energy", CAT_TENSION, "LIVE_FULL", "Formula / function",
    "core/math/core_math.py", "—", "tension_energy = 1 − gapF (gap between top-2 family energies).",
    ["F_vec[288]"], [], "Java 21_MATH `tensionEnergy` name — formula changed",
    "One of the few v0.3-era metric names that survived essentially unchanged in identifier, changed in formula. 17 files consume it across `hesperia/engine/output_trace.py` and `core/propagation/*`.")

add("compute_structural_tension", CAT_TENSION, "LIVE_SUCCESSOR", "Formula / function",
    "core/math/stability_metrics.py", "—", "structural_tension = 1 − max(area)/sum(area) — dominance-competition tension.",
    ["A_vec[12] (area activation vector)"], [], "No direct Java ancestor named this way", "Max-share concentration, HHI-adjacent building block.")

add("tension_from_conflict", CAT_TENSION, "DEAD", "Formula / function",
    "n/a — core/math/dict_b.py deleted (f44b3454, confirmed-dead duplicate, zero importers)", "—",
    "tension = min(1, C·4) from exclusion conflict energy C.",
    ["build_exclusion_pairs / area_projection", "structural_coherence_pass"], [], "No direct Java ancestor",
    "Reclassified 2026-08-04, module path updated 2026-08-04 (same day, second pass): dict-specific logic belongs in its respective registered module (core.dict_a/core.dict_b at hesperia/modules/default/dict_{a,b}_module.py — moved same day from core/runtime/ so core/ holds no module-registry-shaped code, wired via core/engine/module_aliases.py), not in generic core/math/ — that's why core/math/dict_b.py was correctly deleted as dead duplicate, not just relocated. [[compute_tension]] is the live general-purpose tension formula today, but it uses a different formula (L1 abs-sum over (i,i+6) opposite pairs, not conflict-energy C — see compute_tension notes) — this specific conflict-energy channel has no successor formula anywhere in current source.")

add("contradiction_pressure -> tension_energy", CAT_TENSION, "LIVE_SUCCESSOR", "Contract mapping",
    "runtime/services/engine_analyze_contract.py", "—", "ENGINE-ANALYZE maps sealed contradiction_pressure onto the tension_energy contract scalar.",
    ["TRIZ contradiction signals", "Relation weights (conflict/opposition)"], ["metric_tension_energy"],
    "Altshuller / TRIZ contradiction lineage — Theory Explainer: plain_lang: TRIZ calls opposing requirements a 'contradiction'; Hesperia folds that pressure into the same tension_energy slot the rest of the contract already consumes. author: Genrich Altshuller (TRIZ) as theory family; LIVE mapping is Hesperia-native. extent: structural_analogy / partial (not full 39×39 matrix). reasoning: SCIENCE.md — narrow TRIZ slice; sealed analyze maps contradiction_pressure → tension_energy. application: [[metric_tension_energy]], [[Relation weights (conflict/opposition)]], Louvain/TRIZ novelty path.",
    "**HWIKI-DOC-22:** Verified in `engine_analyze_contract.py` (`contradiction_p` → `tension_energy`). Not a Java ancestor — BEYOND-era mechanism reused for a Java-named slot.")

add("Relation weights (conflict/opposition)", CAT_TENSION, "LIVE_SUCCESSOR", "Parameter (constants)",
    "parameter_catalog.md §7", "conflict/negation = 1.0, opposition = 0.85",
    "Typed adversity weights on graph edges.", [], ["contradiction_pressure -> tension_energy"], "No direct Java ancestor",
    "**HWIKI-DOC-22 related:** typed adversity edges feeding TRIZ/tension mapping.")

add("OPPOSITE_OFFSET", CAT_TENSION, "DEAD_ALGO_SURVIVED", "Parameter (constant)",
    "core/result/contract.py:64 (inlined `i, i+6` in compute_tension)", "6", "Offset defining opposite-area exclusion pairs (i, i+6), same offset compute_tension uses.",
    ["Icosahedral Surface Graph"], ["compute_tension", "build_exclusion_pairs / area_projection"], "Java 21_MATH bipolar axis convention (offset changed from interleaved to +6)",
    "**Not geometric antipodes.** After `get_aligned_area_coordinates`, true antipodes are a different pairing (see [[compute_tension]] HWIKI-OPEN-01). OPPOSITE_OFFSET is the shipped bipolar *index* convention. Reclassified 2026-08-04: no longer a named module constant since core/math/dict_b.py was deleted (f44b3454) as dead duplicate — but the `+6` pairing it defined is inlined verbatim in [[compute_tension]]'s `pairs = [(i, i + 6) for i in range(6)]`, so the value/algorithm survives even though the standalone constant does not.")

# ===== PROPAGATION =====
add("center_to_inner", CAT_PROP, "LIVE_FULL", "Parameter (YAML weight)", "assets/specs/canon/propagation_weights.yaml", "0.25",
    "Strongest local spread into the final area vector.", [], ["inner_to_middle / middle_to_inner", "bridge_weight"],
    "Graph diffusion on layered neighborhoods — Theory Explainer: plain_lang: how strongly energy at the center ring leaks into the first neighborhood ring. author: Hesperia propagation YAML (no single classical paper). extent: full (load-bearing weight). reasoning: distance-sensitive diffusion intuition on the icosahedral neighborhoods. application: [[inner_to_middle / middle_to_inner]], [[bridge_weight]], [[lambda (lazy step)]].",
    "**HWIKI-DOC-24:** Strongest local spread weight in the center→inner→middle→outer ladder.")

add("inner_to_middle / middle_to_inner", CAT_PROP, "LIVE_FULL", "Parameter (YAML weight)", "assets/specs/canon/propagation_weights.yaml", "0.18",
    "Second-ring leak, distance-sensitive diffusion.", ["center_to_inner"], ["middle_to_outer / outer_to_middle"],
    "Graph diffusion on layered neighborhoods — Theory Explainer: plain_lang: second-ring leak — weaker than center_to_inner because farther from the activated core. author: Hesperia propagation YAML. extent: full. reasoning: distance decay ladder. application: [[center_to_inner]], [[middle_to_outer / outer_to_middle]].",
    "**HWIKI-DOC-24:** Mid-ring bidirectional weight.")

add("middle_to_outer / outer_to_middle", CAT_PROP, "LIVE_FULL", "Parameter (YAML weight)", "assets/specs/canon/propagation_weights.yaml", "0.12",
    "Peripheral thinning, distance decay.", ["inner_to_middle / middle_to_inner"], ["bridge_weight"],
    "Graph diffusion on layered neighborhoods — Theory Explainer: plain_lang: outermost ring gets the thinnest local weight — periphery thins by design. author: Hesperia propagation YAML. extent: full. reasoning: completes the radial diffusion ladder. application: [[inner_to_middle / middle_to_inner]], [[decay_factor (propagation)]].",
    "**HWIKI-DOC-24:** Peripheral thinning weight.")

add("bridge_weight", CAT_PROP, "LIVE_FULL", "Parameter (YAML weight)", "assets/specs/canon/propagation_weights.yaml", "0.22",
    "Cross-area coupling — semantic bleed across areas.", ["center_to_inner"], ["lambda (lazy step)"],
    "Graph diffusion on layered neighborhoods — Theory Explainer: plain_lang: how much energy can jump across area bridges (semantic bleed), not only along rings. author: Hesperia propagation YAML. extent: full. reasoning: cross-area coupling complementary to radial weights. application: [[center_to_inner]], [[Transition matrix (W)]].",
    "**HWIKI-DOC-24:** Cross-area coupling weight.")

add("decay_factor (propagation)", CAT_PROP, "PARTIAL", "Parameter (YAML weight)", "assets/specs/canon/propagation_weights.yaml", "1.0",
    "Deferred multi-hop attenuation — currently a no-op on single-hop propagation.", [], [],
    "Graph diffusion on layered neighborhoods — Theory Explainer: plain_lang: reserved multi-hop attenuation knob; today it is identity (1.0) on single-hop paths. author: Hesperia propagation YAML. extent: partial (reserved slot). reasoning: future multi-hop attenuation without breaking current YAML. application: [[middle_to_outer / outer_to_middle]].",
    "**HWIKI-DOC-24:** Reserved slot, not yet load-bearing beyond identity.")

add("Transition matrix (W)", CAT_PROP, "BEYOND", "Data structure / formula",
    "core/math/transition_matrix.py", "—", "Transition counts a_t -> a_{t+1}, row-normalized to a stochastic matrix.",
    [], ["lambda (lazy step)", "Chapman-Kolmogorov Multi-Step"], 
    "Markov (1906) finite-state formalism — Theory Explainer: plain_lang: a table of 'from this area, probability of next area' built from counted moves, then normalized so each row sums to 1. author: Markov finite-state chain. extent: full construction (counts→probabilities). reasoning: BEYOND Java; supports lazy step and multi-step diffusion. application: [[lambda (lazy step)]], [[Chapman-Kolmogorov Multi-Step]], [[Mixing Diagnostics]].",
    "**HWIKI-DOC-05:** Full construction (counts -> probabilities); not proposed in the Java corpus, built later for L6 dynamism.")

add("Chapman-Kolmogorov Multi-Step", CAT_PROP, "BEYOND", "Formula / function",
    "sphere/propagation/multi_step_diffusion.py:21-72 (`propagate_k_steps`, `iterative_diffusion`)", "—",
    "v_k = v @ W^k (np.linalg.matrix_power) or iterative current=(1-α)current+α(current@W).",
    ["Transition matrix (W)"], ["Mixing Diagnostics", "cumulativeDrift"],
    "Chapman (1928) / Kolmogorov (1931) — Theory Explainer: plain_lang: instead of one hop, raise the transition matrix to the k-th power (or repeat the lazy step) to see mass after many hops. author: Chapman–Kolmogorov equation lineage. extent: full (verbatim matrix_power / iterative). reasoning: multi-step diffusion + mixing diagnostics. application: [[Mixing Diagnostics]], [[lambda (lazy step)]], contrast dead [[cumulativeDrift / turnCoherence]].",
    "**HWIKI-DOC-06:** Verified in `propagate_k_steps` (pure power) and `iterative_diffusion` (lazy α loop calling `diffuse_step`).")

add("Mixing Diagnostics", CAT_PROP, "BEYOND", "Formula / function",
    "sphere/propagation/multi_step_diffusion.py:75-103 (`propagation_depth_metric`)", "—",
    "propagation_depth_metric(seq): consecutive_l1[i]=Σ|s[i+1]-s[i]| (via vector_sum abs); entropy_sequence[i]=compute_normalized_entropy(s[i]); depth=len(seq)-1.",
    ["Chapman-Kolmogorov Multi-Step", "compute_entropy (Shannon)"], ["cumulativeDrift"],
    "Markov-chain mixing characterization (applied) — Theory Explainer: plain_lang: measures how fast a walk sequence spreads (L1 step sizes) and how disordered each snapshot is (normalized Shannon). author: applied mixing / information theory (no single eponym; entropy via Shannon 1948). extent: full (within-run). reasoning: shipped for multi-step diffusion diagnostics, not turn boundaries. application: [[Chapman-Kolmogorov Multi-Step]], [[compute_entropy (Shannon)]], contrast dead [[cumulativeDrift / turnCoherence]].",
    "**HWIKI-OPEN-03 / DOC-07 re-read 2026-07-23 (line-by-line):** function is `propagation_depth_metric` — returns dict keys `depth`, `consecutive_l1`, `entropy_sequence`. Entropy calls `core.math.entropy_metrics.compute_normalized_entropy` (canonical Shannon path), not a local copy. Empty/short/mismatched sequences return zeros. **Confidence lifted** — no longer UNVERIFIED companion-doc paraphrase. Structurally same shape as dead [[cumulativeDrift / turnCoherence]], different boundary (within-run steps vs turn-to-turn).")

# ===== THRESHOLDS =====
add("activation_threshold", CAT_THRESH, "LIVE_FULL", "Parameter (constant)", "diagnostics config", "0.01",
    "Sparse activation floor — what counts as a hit.", [], [], "No Java ancestor", "")
add("area_active_threshold", CAT_THRESH, "LIVE_FULL", "Parameter (constant)", "diagnostics config", "0.05",
    "Aggregated coverage floor — area 'touched'.", [], [], "No Java ancestor", "")
add("entropy_threshold (monotony)", CAT_THRESH, "LIVE_FULL", "Parameter (constant)",
    "assets/specs/canon/diagnostic_rules.yaml", "0.35", "structural_monotony label — entropy below this = structurally narrow discourse.",
    ["compute_entropy (Shannon)"], [], "Shannon (1948)", "")
add("coverage_threshold (monotony)", CAT_THRESH, "LIVE_FULL", "Parameter (constant)",
    "assets/specs/canon/diagnostic_rules.yaml", "0.20", "Joint with entropy_threshold for the monotony regime.", [], [], "No Java ancestor", "")
add("dominant_area_share_threshold", CAT_THRESH, "LIVE_SUCCESSOR", "Parameter (constant)",
    "sphere/diagnostics/monotony_detector.py", "0.65",
    "compute_dominant_area_share(area_vector) >= threshold triggers dominance classification.",
    ["A_vec[12] (area activation vector)"], ["X_A / X_F alignment (Java)"], "Java 20_GEOMETRY `X_A` alignment concept",
    "Real, wired successor of Java's X_A — has a threshold AND a rule trigger in `rule_registry.py`. No family-share (`X_F`) counterpart exists yet — see [[X_A / X_F alignment (Java)]].")
add("curvature_threshold / severe", CAT_THRESH, "LIVE_FULL", "Parameter (constants)", "diagnostics config", "1.20 / 1.50",
    "Hesperia-native 3-level adjacency step score — explicitly not Ricci curvature.", [], [], "No Java ancestor", "")
add("jump_rate_threshold / severe", CAT_THRESH, "LIVE_FULL", "Parameter (constants)", "diagnostics config", "0.30 / 0.50",
    "Relative frequency of non-adjacent moves — volatility bands.", [], [], "No Java ancestor", "")
add("low_stability_threshold", CAT_THRESH, "LIVE_FULL", "Parameter (constant)", "diagnostics config", "0.15",
    "Self-loop frequency complement — unstable flag.", [], [], "No Java ancestor", "")
add("FGR DOMINANT_SHARE_HIGH", CAT_THRESH, "LIVE_FULL", "Parameter (constant)", "sphere/fpf_bridge/constants.py", "0.35",
    "Trust tier on evidence, FPF FGR calculus.", ["FGR (Formality/Ground/Reliability)"], [],
    "FPF Part B.3 (Levenchuk) — Theory Explainer: plain_lang: when a dominant share exceeds 0.35, treat evidence trust tier as high under FGR. author: FPF Part B.3 via fpf_bridge. extent: full. reasoning: operationalizes Formality/Ground/Reliability into a share gate. application: [[FGR (Formality/Ground/Reliability)]], [[FGR freshness stability map]].",
    "**HWIKI-DOC-26:** DOMINANT_SHARE application of FGR.")
add("FGR freshness stability map", CAT_THRESH, "LIVE_FULL", "Parameter (constants)", "sphere/fpf_bridge/", "0.7 / 0.3",
    "Stability -> freshness map: CURRENT/STALE/EXPIRED.", ["FGR (Formality/Ground/Reliability)"], [],
    "FPF Part B.3 — Theory Explainer: plain_lang: map stability scores into freshness buckets (CURRENT/STALE/EXPIRED) so Reliability stays time-aware. author: FPF Part B.3 via fpf_bridge. extent: full. reasoning: freshness is part of Reliability in the FGR tuple. application: [[FGR (Formality/Ground/Reliability)]], [[FGR DOMINANT_SHARE_HIGH]].",
    "**HWIKI-DOC-26:** Freshness/stability map application of FGR.")

# ===== GRAPH / STRUCTURAL =====
add("Circuit rank (LOOP_COUNT/LOOP_DENSITY)", CAT_GRAPH, "LIVE_FULL", "Formula / function",
    "core/layers/layer_2.py", "—",
    "LOOP_COUNT = max(0, induced_edges - used_edges); LOOP_DENSITY = LOOP_COUNT / (TOTAL_REACHABLE_NODES + eps).",
    ["BFS depth-capped traversal"], [],
    "Kirchhoff (1847) — Theory Explainer: plain_lang: how many independent loops sit in the visited subgraph — cycle-space dimension E−(V−1), reported as LOOP_COUNT/LOOP_DENSITY. author: Gustav Kirchhoff (1847) circuit laws / algebraic graph theory. extent: full (formula), applied to semantic activation graph not electrical circuits. reasoning: SCIENCE.md L2 lineage. application: [[BFS depth-capped traversal]]; same discipline family as dead [[K(R) / L(R) / fragIndex (Java)]] but different invariant (cycle rank vs component count).",
    "**HWIKI-DOC-20:** Algebraic graph theory cycle rank on the BFS-induced subgraph.")

add("largest_component_size", CAT_GRAPH, "DEAD_ALGO_SURVIVED", "Formula / function",
    "core/domain/primitive_metrics.py:96", "—",
    "Deterministic DFS over ActiveGraph adjacency; returns the size of the largest connected component.",
    ["ActiveGraph (KME concept graph)"], ["KME Primitives and Derived Metrics"],
    "**This is Java's L(R) ('largest component'), verbatim as an algorithm** — see [[K(R) / L(R) / fragIndex (Java)]]",
    "The single strongest 'name died, algorithm did not' finding across all passes on this corpus — found by searching for the algorithm shape, not the Java symbol name. See [[DEAD_ALGO_SURVIVED (status term)]].")

add("compute_nc (NodeCoverage)", CAT_GRAPH, "LIVE_FULL", "Formula / function",
    "core/domain/primitive_metrics.py:55", "—", "NC = n/N — active concept nodes over the full domain node count.",
    ["ActiveGraph (KME concept graph)"], ["KME Primitives and Derived Metrics"], "No Java ancestor", "")
add("compute_ci (ConcentrationIndex)", CAT_GRAPH, "LIVE_SUCCESSOR", "Formula / function",
    "core/domain/primitive_metrics.py:64", "—", "Normalized HHI over node hit-counts: ci = (hhi-baseline)/(1-baseline).",
    ["ActiveGraph (KME concept graph)"], ["KME Primitives and Derived Metrics"], "Java 20_GEOMETRY `C(R)` concept (dominance/concentration family)",
    "Same discipline as C(R)=L/active, different formula (HHI concentration, not component-ratio).")
add("compute_ld (LogicalDensity)", CAT_GRAPH, "LIVE_FULL", "Formula / function",
    "core/domain/primitive_metrics.py:84", "—", "ld = avgActiveDegree / Deg95, clamped to [0,1].",
    ["ActiveGraph (KME concept graph)"], ["KME Primitives and Derived Metrics"], "No Java ancestor", "")
add("count_triangles / count_connected_triplets", CAT_GRAPH, "LIVE_FULL", "Formula / function",
    "core/domain/primitive_metrics.py:122-145", "—", "Deterministic triangle count; sum of C(deg(v),2) per node.",
    ["ActiveGraph (KME concept graph)"], ["KME Primitives and Derived Metrics"], "No Java ancestor",
    "Feeds clustering-coefficient-style derived metrics.")

# ===== KME derived metrics (HWIKI-KME-01 stubs; pins from FELIX-HWIKI-KME-02) =====
add("KME Primitives and Derived Metrics", CAT_GRAPH, "BEYOND", "Hub / concept",
    "core/domain/derived_metrics.py + core/domain/primitive_metrics.py", "6 primitives → 35 derived",
    "Hub: PrimitiveMetrics (LD,COH,NC,PR,PV,CI) → compute_derived_metrics → DerivedMetrics (35) → to_derived_vector / fingerprint.",
    ["compute_ld (LogicalDensity)", "compute_ci (ConcentrationIndex)", "compute_nc (NodeCoverage)",
     "largest_component_size", "count_triangles / count_connected_triplets"],
    ["core/domain/pipeline.py", "hesperia/engine/kme/clinical_bridge.py", "core/domain/fingerprint.py"],
    "No Java 1:1 names — BEYOND comparability fingerprint layer",
    "**HWIKI-KME-01:** Individual derived symbols below are stubs with formula+module pins from Felix HWIKI-KME-02. **HWIKI-KME-03:** plain-lang / theory notes expanded on each derived page.")
_KME_DERIVED = [
    ("KDI (KME derived)", "clamp01(LD * COH)", 72, "Knowledge Density Index"),
    ("CSI (KME derived)", "clamp01(NC * PR)", 73, "Coverage–Presence Index"),
    ("SPI (KME derived)", "clamp01(CI)", 74, "Structure Index pass-through"),
    ("TDS (KME derived)", "clamp01(PR * LD)", 75, "PR×LD product"),
    ("SSS (KME derived)", "clamp01(safe_div(COH, PV))", 76, "COH/PV ratio"),
    ("KCI (KME derived)", "clamp01(safe_div(LD, PR))", 77, "LD/PR ratio"),
    ("CCI (KME derived)", "clamp01(COH * NC)", 78, "COH×NC product"),
    ("SPS (KME derived)", "clamp01(PR * COH)", 79, "PR×COH product"),
    ("DCI (KME derived)", "clamp01(LD * NC)", 80, "LD×NC product"),
    ("CSI2 (KME derived)", "clamp01(CI * LD)", 81, "CI×LD product"),
    ("KEF (KME derived)", "clamp01(safe_div(PV, NC))", 82, "PV/NC ratio"),
    ("ASS (KME derived)", "clamp01(safe_div(COH * LD, PV))", 83, "(COH·LD)/PV"),
    ("CDR (KME derived)", "clamp01(safe_div(PR, NC))", 84, "PR/NC ratio"),
    ("KCR (KME derived)", "clamp01(safe_div(LD, NC))", 85, "LD/NC ratio"),
    ("TCI (KME derived)", "clamp01(COH * LD * CI)", 86, "COH·LD·CI"),
    ("PEI (KME derived)", "clamp01(safe_div(PR, PV))", 87, "PR/PV ratio"),
    ("KE (KME derived)", "clamp01(safe_div(PR, LD))", 88, "PR/LD ratio"),
    ("SCS (KME derived)", "clamp01(safe_div(LD * COH, NC))", 89, "(LD·COH)/NC"),
    ("CRI (KME derived)", "clamp01(CI * COH)", 90, "CI×COH product"),
    ("KNS (KME derived)", "clamp01(NC * COH * LD)", 91, "NC·COH·LD"),
    ("CII (KME derived)", "clamp01(safe_div(NC, PR))", 92, "NC/PR ratio"),
    ("TEP (KME derived)", "clamp01(PV * LD)", 93, "PV×LD product"),
    ("KSI (KME derived)", "clamp01(safe_div(COH * LD, PR))", 94, "(COH·LD)/PR — catalog exemplar"),
    ("CDD (KME derived)", "clamp01(safe_div(NC, PV))", 95, "NC/PV ratio"),
    ("SSR (KME derived)", "clamp01(safe_div(PR, PV))", 96, "PR/PV ratio"),
    ("TER (KME derived)", "clamp01(safe_div(CI, LD))", 97, "CI/LD ratio"),
    ("CPC (KME derived)", "clamp01(safe_div(PR * NC, PV))", 98, "(PR·NC)/PV"),
    ("KBS (KME derived)", "clamp01(safe_div(COH * NC, PV))", 99, "(COH·NC)/PV"),
    ("TRI (KME derived)", "clamp01(safe_div(CI * LD, PR))", 100, "(CI·LD)/PR"),
    ("IDE (KME derived)", "clamp01(safe_div(PR * COH, NC))", 101, "(PR·COH)/NC"),
    ("KPS (KME derived)", "clamp01(safe_div(COH, PR))", 102, "COH/PR ratio"),
    ("TBI (KME derived)", "clamp01(NC * PV)", 103, "NC×PV product"),
    ("KDI2 (KME derived)", "clamp01(LD * PR * COH)", 104, "LD·PR·COH"),
    ("CDI (KME derived)", "clamp01(CI * NC)", 105, "CI×NC product"),
    ("KVI (KME derived)", "clamp01(safe_div(LD * COH * PR, PV))", 106, "(LD·COH·PR)/PV"),
]
for _name, _formula, _line, _hint in _KME_DERIVED:
    add(_name, CAT_GRAPH, "LIVE_FULL", "Derived metric",
        f"core/domain/derived_metrics.py:{_line}", "—",
        _formula,
        ["KME Primitives and Derived Metrics"],
        ["core/domain/pipeline.py", "core/domain/fingerprint.py"],
        "BEYOND Java — pure algebra over PrimitiveMetrics (clamp01 + safe_div) — Theory Explainer: plain_lang: {_hint} built only from LD/COH/NC/PR/PV/CI primitives. author: Hesperia KME derived layer (no classical namesake). extent: product_metric. reasoning: clamp01+safe_div keeps fingerprint comparable. application: pipeline / clinical_bridge / fingerprint.".format(_hint=_hint),
        f"**HWIKI-KME-01/03:** {_hint}. Formula `{_formula}`. Consumers: pipeline / clinical_bridge / fingerprint (Felix HWIKI-KME-02). Not clinical TFP judgment — algebra only.")

add("Clustering coefficient", CAT_GRAPH, "PARTIAL", "Formula",
    "core/layers/layer_2.py:_compute_clustering (LOCAL_CLUSTERING_COEFFICIENT)", "C(v) = 2t/(k(k-1))",
    "Local clustering at the dominant family / start node of the L2 BFS.",
    ["count_triangles / count_connected_triplets", "BFS depth-capped traversal"], ["KME Primitives and Derived Metrics"],
    "Watts & Strogatz (1998) — Theory Explainer: plain_lang: of the friends of a node, how many are friends with each other — a local clumpiness score. author: Duncan Watts & Steven Strogatz (1998). extent: partial — formula verbatim at dominant/start node only; full small-world network model not adopted. reasoning: SCIENCE.md L2; code pin `_compute_clustering` in `layer_2.py`. application: [[count_triangles / count_connected_triplets]], L2 LOCAL_CLUSTERING_COEFFICIENT.",
    "**HWIKI-DOC-19:** PARTIAL + code pin — formula only, not the full small-world apparatus. Felix verify: `core/layers/layer_2.py` lines ~42–43, ~142.")

add("BFS depth-capped traversal", CAT_GRAPH, "LIVE_FULL", "Algorithm", "L2 traversal", "—",
    "Unweighted shortest paths, depth-capped breadth-first search.", [], ["Circuit rank (LOOP_COUNT/LOOP_DENSITY)", "Clustering coefficient"],
    "Moore (1959) / Lee (1961)", "")

add("Louvain communities (seed 42)", CAT_GRAPH, "BEYOND", "Algorithm",
    "hesperia/extensions/triz/novelty_engine.py", "LOUVAIN_SEED = 42",
    "networkx.community.louvain_communities — modularity-maximization clustering on the concept graph.",
    [], ["contradiction_pressure -> tension_energy"],
    "Blondel et al. (2008) — Theory Explainer: plain_lang: group concepts into communities by maximizing modularity (denser inside than across); seed 42 makes tie-breaks reproducible. author: Vincent Blondel, Jean-Loup Guillaume, Renaud Lambiotte, Etienne Lefebvre (2008). extent: full (algorithm), Hesperia-specific addition is only the reproducibility seed. reasoning: SCIENCE.md TRIZ/novelty path. application: `detect_concept_clusters_louvain` / novelty_engine; contrast [[K(R) / L(R) / fragIndex (Java)]] (different discipline).",
    "**HWIKI-DOC-18:** **Not the same discipline-instance as [[K(R) / L(R) / fragIndex (Java)]]** — community detection by modularity, not connected-component counting.")
add("detect_dominant_area / detect_dominant_family", CAT_GRAPH, "LIVE_SUCCESSOR", "Formula / function",
    "core/math/vector_ops.py", "—", "Returns the index of the dominant area / family (argmax), not a share fraction.",
    ["A_vec[12] (area activation vector)", "F_vec[288]"], ["dominant_area_share_threshold"],
    "Java `X_A, X_F` alignment concept", "Index-only; the area side has a share-fraction sibling (`compute_dominant_area_share`), the family side does not — see [[X_A / X_F alignment (Java)]].")

# ===== ENTROPY =====
add("compute_entropy (Shannon)", CAT_ENTROPY, "LIVE_FULL", "Formula / function",
    "core/math/entropy_metrics.py", "—", "H = −Σ p·log(p); compute_normalized_entropy divides by ln(M).",
    ["E (energy vector)"], ["P_disp (dispersion penalty)", "entropy_threshold (monotony)", "Mixing Diagnostics"],
    "Shannon (1948), *A Mathematical Theory of Communication* — Theory Explainer: plain_lang: how spread-out / unpredictable a distribution is; high entropy = energy smeared across many sides, low = concentrated. author: Claude Shannon (1948). extent: full (canonical H and H/ln(M)). reasoning: reused as the system's information primitive rather than inventing a second entropy. application: [[P_disp (dispersion penalty)]], [[entropy_threshold (monotony)]], [[Mixing Diagnostics]] (`compute_normalized_entropy`).",
    "**HWIKI-DOC-02:** The single most-reused mathematical primitive in the whole system — canonical, not tool-local. Contrast [[KL divergence]] (REJECTED) and tool-local [[area_entropy (tool-local)]].")
add("Gini concentration", CAT_ENTROPY, "LIVE_FULL", "Formula / function",
    "core/layers/layer_1.py:_compute_gini (GINI_COEFFICIENT); also layer_4._gini", "—",
    "Sorted-array Gini coefficient — concentration alongside entropy (the two can disagree in direction on the same distribution).",
    [], ["entropy_threshold (monotony)", "dominant_area_share_threshold"],
    "Corrado Gini (1912), *Variabilità e mutabilità* — Theory Explainer: plain_lang: how unevenly hits/activation are piled onto a few families versus spread evenly — inequality as concentration. author: Corrado Gini (1912). extent: full (verbatim sorted-array Gini). reasoning: SCIENCE.md L1; independent concentration measure alongside Shannon. application: L1 `GINI_COEFFICIENT`, L3 `GINI_DELTA`, L4 `EVIDENCE_GINI_BASELINE`; pairs with [[compute_entropy (Shannon)]].",
    "**HWIKI-DOC-14:** Concentration alongside entropy — not a Shannon substitute.")
add("area_entropy (tool-local)", CAT_ENTROPY, "PARTIAL", "Formula / function (duplicate)",
    "tools/tfp_calibration_audit.py:245-247", "—",
    "Local `_entropy()` helper computing the same Shannon formula inline, not calling the canonical function.",
    [], [], "Java 21_MATH `areaEntropy`",
    "Cosmetic gap, not a feature gap: [[compute_entropy (Shannon)]] already exists and is used elsewhere. This is a dedup candidate, not new work — see [[Coverage Ledger]].")

# ===== STABILITY =====
add("LYAPUNOV_ESTIMATE / GLOBAL_STABILITY_SCORE", CAT_STABILITY, "LIVE_SUCCESSOR", "Formula / function",
    "core/layers/layer_6.py:76-77", "—",
    "GLOBAL_STABILITY_SCORE = 1 / (1 + CONDITION_NUMBER + |LYAPUNOV_ESTIMATE|) — single-step perturbation-growth proxy.",
    ["CONDITION_NUMBER (L6)", "STABILITY_RADIUS (L6)"], ["CONCEPTUAL_COHERENCE_INDEX (L6)", "sphere/pipeline/contract_validation.py contract"],
    "Lyapunov (1892), *General Problem of the Stability of Motion* — Theory Explainer: plain_lang: a single number claiming 'how stable is this read' from condition + a Lyapunov-named proxy. author: A.M. Lyapunov (1892). extent: structural_analogy (proxy, not iterated exponent). reasoning: SCIENCE.md honesty — not a literal Lyapunov exponent. application: [[GLOBAL_STABILITY_SCORE]] path into L7/L8; [[CONCEPTUAL_COHERENCE_INDEX (L6)]].",
    "**HWIKI-DOC-12 / L6:** Explicitly a conceptual proxy — no iterated perturbation, no divergence-rate over many steps. Same honesty discipline as Java [[ALPHA/BETA/GAMMA/DELTA integrity quartet (Java)]]. L6 neighbors: [[CONDITION_NUMBER (L6)]], [[STABILITY_RADIUS (L6)]], [[SPECTRAL_GAP (L6)]].")

# ===== L6 neighbors (HWIKI-L6-01 first slice) =====
add("CONDITION_NUMBER (L6)", CAT_STABILITY, "LIVE_FULL", "Layer variable",
    "core/layers/layer_6.py:52,91", "1.0 (no-perturbation stub)",
    "CONDITION_NUMBER — ill-conditioning proxy of the hit/response surface; enters GLOBAL_STABILITY_SCORE denominator.",
    [], ["LYAPUNOV_ESTIMATE / GLOBAL_STABILITY_SCORE"], "39_SPEC Layer-6",
    "**HWIKI-L6-01:** When no perturbation data, stubbed to 1.0. Downstream: GLOBAL_STABILITY_SCORE.")

add("STABILITY_RADIUS (L6)", CAT_STABILITY, "LIVE_FULL", "Layer variable",
    "core/layers/layer_6.py:46,78", "1.0 (no-perturbation stub)",
    "STABILITY_RADIUS — radius of claimed local stability; multiplies into CONCEPTUAL_COHERENCE_INDEX.",
    [], ["CONCEPTUAL_COHERENCE_INDEX (L6)"], "39_SPEC Layer-6",
    "**HWIKI-L6-01:** Stub 1.0 without perturbation; live formula path reserved.")

add("SPECTRAL_GAP (L6)", CAT_STABILITY, "LIVE_FULL", "Layer variable",
    "core/layers/layer_6.py:53,92", "0.0 (no-perturbation stub)",
    "SPECTRAL_GAP — gap proxy for mixing/expansion rate of the response operator.",
    [], [], "39_SPEC Layer-6",
    "**HWIKI-L6-01:** Stub 0.0 when no perturbation; neighbor of Lyapunov/condition cluster.")

add("CONCEPTUAL_COHERENCE_INDEX (L6)", CAT_STABILITY, "LIVE_FULL", "Layer variable",
    "core/layers/layer_6.py:78,105", "—",
    "CONCEPTUAL_COHERENCE_INDEX = STABILITY_RADIUS · (1 − NORMALIZED_FAMILY_ENTROPY) · GLOBAL_STABILITY_SCORE.",
    ["STABILITY_RADIUS (L6)", "LYAPUNOV_ESTIMATE / GLOBAL_STABILITY_SCORE"], ["L7/L8 stability regime consumers"],
    "39_SPEC Layer-6",
    "**HWIKI-L6-01:** Combines stability radius, L1 family entropy, and GLOBAL_STABILITY_SCORE.")

add("INPUT_PERTURBATION_RESPONSE (L6)", CAT_STABILITY, "LIVE_FULL", "Layer variable",
    "core/layers/layer_6.py:42,86", "0.0 (no-perturbation stub)",
    "INPUT_PERTURBATION_RESPONSE — first-order response amplitude to input perturbation (stub 0 without perturbation data).",
    [], ["DOMINANT_FAMILY_STABILITY (L6)"], "39_SPEC Layer-6",
    "**HWIKI-L6-01:** Part of L6 I. no-perturbation block.")

add("DOMINANT_FAMILY_STABILITY (L6)", CAT_STABILITY, "LIVE_FULL", "Layer variable",
    "core/layers/layer_6.py:43,87", "True (no-perturbation stub)",
    "DOMINANT_FAMILY_STABILITY — boolean: dominant family remains stable under the (stubbed) perturbation regime.",
    ["INPUT_PERTURBATION_RESPONSE (L6)"], [], "39_SPEC Layer-6",
    "**HWIKI-L6-01:** Boolean neighbor of Lyapunov/stability cluster; L7 consumes related regime flags.")

# ===== L6 curvature / gradient / depth-growth (HWIKI-L6-02) =====
add("DEPTH_GROWTH_RATIO (L6)", CAT_STABILITY, "LIVE_FULL", "Layer variable",
    "core/layers/layer_6.py (L6_LIVE_FIELDS)", "mass_at_depth[1]/mass_at_depth[0]",
    "DEPTH_GROWTH_RATIO = mass_at_depth[1] / (mass_at_depth[0] + eps) when len≥2 and mass[0]>0; else 0.",
    [], ["FIBONACCI_DEVIATION_SCORE (L6)", "EXPONENTIAL_FIT_ERROR (L6)"], "39_SPEC Layer-6 Group IV",
    "**HWIKI-L6-02:** Truly LIVE depth-growth signal from activation mass ladder — not a stub.")

add("FIBONACCI_DEVIATION_SCORE (L6)", CAT_STABILITY, "LIVE_FULL", "Layer variable",
    "core/layers/layer_6.py (L6_LIVE_FIELDS)", "|m2 − (m1+m0)|",
    "FIBONACCI_DEVIATION_SCORE = |mass_at_depth[2] − (mass_at_depth[1] + mass_at_depth[0])| when len≥3; else 0.",
    ["DEPTH_GROWTH_RATIO (L6)"], [], "39_SPEC Layer-6 Group IV",
    "**HWIKI-L6-02:** LIVE fibonacci-like deviation on the depth mass ladder; companion of DEPTH_GROWTH_RATIO.")

add("COVERAGE_GRADIENT (L6)", CAT_STABILITY, "PARTIAL", "Layer variable",
    "core/layers/layer_6.py (L6_STUB_FIELDS)", "0.0 (stub)",
    "COVERAGE_GRADIENT — reserved first-difference of coverage along depth/perturbation; stubbed 0 without series.",
    [], ["DOMINANCE_CURVATURE (L6)"], "39_SPEC Layer-6 Group I",
    "**HWIKI-L6-02:** PARTIAL stub — slot present in layer_6 output allowlist.")

add("ENTROPY_GRADIENT (L6)", CAT_STABILITY, "PARTIAL", "Layer variable",
    "core/layers/layer_6.py (L6_STUB_FIELDS)", "0.0 (stub)",
    "ENTROPY_GRADIENT — reserved first-difference of entropy along depth; stubbed 0.",
    [], ["ENTROPY_CURVATURE (L6)"], "39_SPEC Layer-6 Group I",
    "**HWIKI-L6-02:** PARTIAL stub — pairs with ENTROPY_CURVATURE.")

add("DOMINANCE_CURVATURE (L6)", CAT_STABILITY, "PARTIAL", "Layer variable",
    "core/layers/layer_6.py + core/stability/stability_delta.py", "0.0 (stub)",
    "DOMINANCE_CURVATURE — second-order dominance response slot; stub 0; anomaly path ANOMALY_CURVATURE_SPIKE watches related spikes.",
    ["COVERAGE_GRADIENT (L6)"], ["core/stability/stability_delta.py"], "39_SPEC Layer-6 Group II",
    "**HWIKI-L6-02:** PARTIAL stub — curvature-of-dominance reserved; consumed conceptually by stability_delta.")

add("ENTROPY_CURVATURE (L6)", CAT_STABILITY, "PARTIAL", "Layer variable",
    "core/layers/layer_6.py (L6_STUB_FIELDS)", "0.0 (stub)",
    "ENTROPY_CURVATURE — second-order entropy response slot; stub 0.",
    ["ENTROPY_GRADIENT (L6)"], [], "39_SPEC Layer-6 Group II",
    "**HWIKI-L6-02:** PARTIAL stub — companion curvature of ENTROPY_GRADIENT.")

add("SECOND_ORDER_RESPONSE (L6)", CAT_STABILITY, "PARTIAL", "Layer variable",
    "core/layers/layer_6.py (L6_STUB_FIELDS)", "0.0 (stub)",
    "SECOND_ORDER_RESPONSE — curvature-of-response slot between first-order perturbation and curvature groups; stub 0.",
    ["INPUT_PERTURBATION_RESPONSE (L6)"], ["DOMINANCE_CURVATURE (L6)"], "39_SPEC Layer-6",
    "**HWIKI-L6-02:** PARTIAL stub — bridges perturbation response to curvature block.")

add("POTENTIAL_GRADIENT (L6)", CAT_STABILITY, "PARTIAL", "Layer variable",
    "core/layers/layer_6.py (L6_STUB_FIELDS)", "0.0 (stub)",
    "POTENTIAL_GRADIENT — potential-analogy gradient in Group IV; stub 0.",
    [], ["ESCAPE_ENERGY_THRESHOLD reserved"], "39_SPEC Layer-6 Group IV",
    "**HWIKI-L6-02:** PARTIAL stub — potential analogy alongside depth-growth LIVE fields.")

add("EXPONENTIAL_FIT_ERROR (L6)", CAT_STABILITY, "PARTIAL", "Layer variable",
    "core/layers/layer_6.py", "0.0 (reserved)",
    "EXPONENTIAL_FIT_ERROR — reserved fit residual for exponential depth-growth model; currently forced 0.",
    ["DEPTH_GROWTH_RATIO (L6)"], [], "39_SPEC Layer-6 Group IV",
    "**HWIKI-L6-02:** PARTIAL reserved — LIVE depth ratio exists; fit error not yet computed.")

add("POWER_LAW_FIT_ERROR (L6)", CAT_STABILITY, "PARTIAL", "Layer variable",
    "core/layers/layer_6.py", "0.0 (reserved)",
    "POWER_LAW_FIT_ERROR — reserved fit residual for power-law depth-growth model; currently forced 0.",
    ["DEPTH_GROWTH_RATIO (L6)"], [], "39_SPEC Layer-6 Group IV",
    "**HWIKI-L6-02:** PARTIAL reserved — companion of EXPONENTIAL_FIT_ERROR.")

# ===== L7 / L8 consumers of GLOBAL_STABILITY_SCORE (HWIKI-L7-01 / L8-01) =====
add("SYSTEM_CONFIDENCE_SCORE (L7)", CAT_TRUST, "LIVE_FULL", "Layer variable",
    "core/layers/layer_7.py (~conf product; out SYSTEM_CONFIDENCE_SCORE)", "clamp01 product",
    "SYSTEM_CONFIDENCE_SCORE folds L1–L6 consistency gates and includes l6[GLOBAL_STABILITY_SCORE] in the confidence product path.",
    ["LYAPUNOV_ESTIMATE / GLOBAL_STABILITY_SCORE", "CONSIST_STABILITY_REGIME_VALID (L7)"],
    ["SI_SYSTEM_CONFIDENCE_U1000 (L8)", "SI_SYSTEM_CONFIDENCE_PCT (L8)", "L9 pillars"],
    "40_SPEC Layer-7",
    "**HWIKI-L7-01:** Primary L7 consumer of GLOBAL_STABILITY_SCORE — not a full L7 census; slice is stability→confidence only.")

add("CONSIST_STABILITY_REGIME_VALID (L7)", CAT_TRUST, "LIVE_FULL", "Layer gate",
    "core/layers/layer_7.py (g10)", "boolean gate",
    "CONSIST_STABILITY_REGIME_VALID (g10) — consistency gate that the L6 Lyapunov/stability regime is within MAX_CHAOS_LEVEL / MAX_LYAPUNOV bounds.",
    ["LYAPUNOV_ESTIMATE / GLOBAL_STABILITY_SCORE"], ["SYSTEM_CONFIDENCE_SCORE (L7)", "DECISION_STATUS_CODE"],
    "40_SPEC Layer-7",
    "**HWIKI-L7-01:** Gate sibling of SYSTEM_CONFIDENCE — Lyapunov/stability regime validity.")

add("SI_GLOBAL_STABILITY_U1000 (L8)", CAT_TRUST, "LIVE_FULL", "Scaled indicator",
    "core/layers/layer_8.py:48", "0–1000",
    "SI_GLOBAL_STABILITY_U1000 = _ratio_to_u1000(l6[GLOBAL_STABILITY_SCORE]) — scaled publish of L6 global stability.",
    ["LYAPUNOV_ESTIMATE / GLOBAL_STABILITY_SCORE"], ["SI_GLOBAL_STABILITY_PCT (L8)"],
    "41_SPEC Layer-8",
    "**HWIKI-L8-01:** Direct L8 scaled consumer of GLOBAL_STABILITY_SCORE.")

add("SI_GLOBAL_STABILITY_PCT (L8)", CAT_TRUST, "LIVE_FULL", "Scaled indicator",
    "core/layers/layer_8.py:49", "0–100%",
    "SI_GLOBAL_STABILITY_PCT = _ratio_to_pct(l6[GLOBAL_STABILITY_SCORE]).",
    ["LYAPUNOV_ESTIMATE / GLOBAL_STABILITY_SCORE", "SI_GLOBAL_STABILITY_U1000 (L8)"],
    ["SI_SYSTEM_CONFIDENCE_PCT (L8)"],
    "41_SPEC Layer-8",
    "**HWIKI-L8-01:** Percent twin of SI_GLOBAL_STABILITY_U1000.")

add("SI_SYSTEM_CONFIDENCE_U1000 (L8)", CAT_TRUST, "LIVE_FULL", "Scaled indicator",
    "core/layers/layer_8.py:50", "0–1000",
    "SI_SYSTEM_CONFIDENCE_U1000 = _ratio_to_u1000(l7[SYSTEM_CONFIDENCE_SCORE]) — publishes L7 confidence (which already folded GLOBAL_STABILITY).",
    ["SYSTEM_CONFIDENCE_SCORE (L7)"], [], "41_SPEC Layer-8",
    "**HWIKI-L8-01:** Indirect consumer chain L6→L7→L8.")

# ===== CAT-02 diagnostic thresholds =====
add("ultra_sparse_coverage_threshold", CAT_THRESH, "LIVE_FULL", "Parameter (constants)",
    "assets/specs/canon/diagnostic_rules.yaml + sphere/diagnostics/anomaly_detector.py", "0.02",
    "Below this coverage, the read is flagged zero-signal / anomalous rather than substantive structure.",
    [], ["sphere/diagnostics/anomaly_detector.py"], "parameter_catalog.md §4",
    "**HWIKI-CAT-02:** From CAT-01 delta — diagnostic ultra-sparse gate.")

add("excessive_jump_threshold", CAT_THRESH, "LIVE_FULL", "Parameter (constants)",
    "assets/specs/canon/diagnostic_rules.yaml + sphere/diagnostics/anomaly_detector.py", "0.60",
    "Above this, a single-step trajectory change is anomalous rather than normal dynamics.",
    [], ["sphere/diagnostics/anomaly_detector.py"], "parameter_catalog.md §4",
    "**HWIKI-CAT-02:** CAT-01 delta — change-point / jump anomaly.")

add("transition_concentration_threshold", CAT_THRESH, "LIVE_FULL", "Parameter (constants)",
    "assets/specs/canon/diagnostic_rules.yaml + sphere/diagnostics/anomaly_detector.py", "0.75",
    "Above this, transition mass collapsing into one route is flagged artifact-like concentration.",
    [], ["sphere/diagnostics/anomaly_detector.py"], "parameter_catalog.md §4",
    "**HWIKI-CAT-02:** CAT-01 delta — transition concentration.")

add("unique_areas_max", CAT_THRESH, "LIVE_FULL", "Parameter (constants)",
    "sphere/diagnostics/monotony_detector.py:51,89", "2",
    "Caps how many distinct areas a read can touch and still be labeled monotonous.",
    [], ["sphere/diagnostics/monotony_detector.py"], "parameter_catalog.md §4",
    "**HWIKI-CAT-02:** CAT-01 delta — monotony cardinality cap.")

add("ENTROPY_DROP_SIGNIFICANT", CAT_TRUST, "LIVE_FULL", "Parameter (constants)",
    "sphere/fpf_bridge/constants.py + sphere/interpretation/state_classifier.py", "0.15",
    "Cutoff for when an entropy drop upgrades FGR / trust tier vs mild fluctuation.",
    [], ["sphere/fpf_bridge/evidence_mapper.py", "state_classifier.py"], "parameter_catalog.md §5 / synergies",
    "**HWIKI-CAT-02:** FGR freshness numeric — entropy-drop significance.")

add("STABILITY_CURRENT_THRESHOLD / STABILITY_STALE_THRESHOLD", CAT_TRUST, "LIVE_FULL", "Parameter (constants)",
    "sphere/fpf_bridge/constants.py + evidence_mapper.py", "0.7 / 0.3",
    "Stability→freshness map: ≥CURRENT_THRESHOLD → CURRENT; ≥STALE else EXPIRED below STALE.",
    ["LYAPUNOV_ESTIMATE / GLOBAL_STABILITY_SCORE"], ["sphere/fpf_bridge/evidence_mapper.py"],
    "parameter_catalog.md §5",
    "**HWIKI-CAT-02:** FGR freshness numeric pair from CAT-01 delta.")

# ===== TRIZ contradiction core (HWIKI-TRIZ-02) =====
add("TRIZ contradiction core hub", CAT_GRAPH, "BEYOND", "Hub / concept",
    "hesperia/extensions/triz/{pipeline,contradiction_engine,triz_classifier,contradiction_contract}.py", "—",
    "Hub: run_triz_layer / detect_contradictions / classify_contradiction(s) over ContradictionSignal models; contract forbids synonym drift.",
    ["Louvain communities (seed 42)"],
    ["TRIZ pipeline.run_triz_layer", "contradiction_engine.detect_contradictions", "triz_classifier.classify_contradiction"],
    "extensions/triz — Class B inventives surface",
    "**HWIKI-TRIZ-02:** Core hub beyond Louvain inventory (TRIZ-01). Pins: pipeline.py, contradiction_engine.py, triz_classifier.py, contradiction_contract.py.")

add("run_triz_layer / run_triz_analysis_complete", CAT_GRAPH, "LIVE_FULL", "Function",
    "hesperia/extensions/triz/pipeline.py", "—",
    "Orchestration entry: ActiveGraph bridge → contradiction + novelty signals → TRIZSignals bundle.",
    ["TRIZ contradiction core hub"], ["product/API TRIZ surfaces", "tests/triz/"],
    "extensions/triz/pipeline.py",
    "**HWIKI-TRIZ-02 / TRIZ-03 pin:** orchestration hub — call sites under product/runtime/tests/triz.")

add("detect_contradictions / build_contradiction_signals", CAT_GRAPH, "LIVE_FULL", "Function",
    "hesperia/extensions/triz/contradiction_engine.py", "—",
    "Core contradiction detection + ContradictionSignal construction / pattern classify.",
    ["TRIZ contradiction core hub", "models.ContradictionSignal"],
    ["triz_classifier.classify_contradiction", "family_contradiction.py"],
    "extensions/triz/contradiction_engine.py",
    "**HWIKI-TRIZ-02 / TRIZ-03 pin:** engine core — inventory role: core contradiction.")

add("classify_contradiction(s) principle table", CAT_GRAPH, "LIVE_FULL", "Function",
    "hesperia/extensions/triz/triz_classifier.py", "—",
    "Maps contradiction patterns onto TRIZ inventives / principle table classifications.",
    ["detect_contradictions / build_contradiction_signals"], ["report_builders.py", "direct_outputs.py"],
    "extensions/triz/triz_classifier.py",
    "**HWIKI-TRIZ-02 / TRIZ-03 pin:** classification science surface.")

add("contradiction_contract (canonical fields)", CAT_GRAPH, "LIVE_FULL", "Contract",
    "hesperia/extensions/triz/contradiction_contract.py", "v0.5.8 field sets",
    "Canonical field sets / forbidden synonyms for contradiction payloads — governance edge of TRIZ core.",
    ["TRIZ contradiction core hub"], ["contradiction_engine.py", "contradiction_calibration.py"],
    "extensions/triz/contradiction_contract.py",
    "**HWIKI-TRIZ-02:** Contract pointer — do not invent synonym fields outside contract.")

add("Wiener feedback on alpha (k_s / k_j)", CAT_STABILITY, "LIVE_SUCCESSOR", "Formula / function",
    "sphere/propagation/weighting.py:78-127 (`apply_stability_modulation`, `apply_jump_rate_modulation`, `compute_effective_diffusion_rate`)",
    "k_stability=0.5, k_jump=0.3 (defaults)",
    "effective_α = base_α·(1 − k_stability·stability_index) then ·(1 + k_jump·jump_rate), each clamped to [0,1] — cybernetic feedback on *diffusion* α.",
    ["lambda (lazy step)"], ["sphere/propagation/engine.py (compute_effective_diffusion_rate call)"],
    "Wiener (1948) cybernetic feedback lineage — Theory Explainer: plain_lang: when the system looks stable, slow the spread; when it jumps a lot, allow slightly more spread. author: Norbert Wiener (1948) cybernetics as theory family (not a cited import). extent: structural_analogy. reasoning: renamed symbols `k_stability`/`k_jump` (not `k_s`/`k_j`); modulates propagation diffusion α, **not** [[alpha (fusion weight)]]. application: `sphere/propagation/engine.py`, tests in `tests/propagation/test_stability_modulation.py`.",
    "**HWIKI-OPEN-02 / DOC-13 resolved 2026-07-23:** Grep for `wiener`/`k_s`/`k_j` as claimed names = zero real hits, but the *formula* lives under `k_stability`/`k_jump` in `weighting.py`. Relocated LIVE_SUCCESSOR — do not cite as DEAD. Not fusion α.")

# ===== SIMILARITY =====
add("cosine_similarity", CAT_SIM, "LIVE_SUCCESSOR", "Formula / function",
    "core/domain/fingerprint.py (cosine_similarity, fingerprint_cosine)", "—",
    "Dot product over norms — fingerprint / hit-vector comparison.",
    [], ["KME Primitives and Derived Metrics", "cumulativeDrift / turnCoherence"],
    "Gerard Salton (1975) VSM — Theory Explainer: plain_lang: angle between two vectors — 1 means same direction, 0 means orthogonal. author: Gerard Salton (1975) vector-space model; also Java 21_MATH `cosine` (turn-drift use). extent: full (formula); LIVE_SUCCESSOR for use-site (fingerprints, not turn-drift). reasoning: SCIENCE.md; repurposed from Java turn-coherence toward KME fingerprints. application: [[KME Primitives and Derived Metrics]]; contrast dead [[cumulativeDrift / turnCoherence]].",
    "**HWIKI-DOC-17:** LIVE_SUCCESSOR — fingerprint comparison, not Java turn-to-turn drift.")

add("BM25 retrieval", CAT_SIM, "BEYOND", "Algorithm",
    "core/layers/layer_4.py + defaults RETRIEVAL_MODE_ID", "RETRIEVAL_MODE_ID=LEX_BM25_V1",
    "Standard BM25 ranking for L4 lexical evidence retrieval.",
    [], ["Jaccard overlaps"],
    "Robertson & Spärck Jones (1976) — Theory Explainer: plain_lang: classic search ranking that scores how well a query's terms match a document, with length normalization. author: Stephen Robertson & Karen Spärck Jones (1976), crystallized through TREC. extent: full (verbatim lexical retrieval function). reasoning: SCIENCE.md L4; BEYOND Java corpus. application: L4 evidence retrieval path; pairs with [[Jaccard overlaps]] overlap diagnostics.",
    "**HWIKI-DOC-15:** Not proposed in the Java corpus — BEYOND retrieval path.")

add("Jaccard overlaps", CAT_SIM, "LIVE_FULL", "Formula / function",
    "core/layers/layer_3.py (VISITED_JACCARD_SIMILARITY); layer_4._jaccard", "—",
    "Set overlap |A∩B|/|A∪B| — HIT/VISITED/evidence/bookset overlap variables.",
    [], ["BM25 retrieval", "cosine_similarity"],
    "Paul Jaccard (1901) — Theory Explainer: plain_lang: of the union of two sets, what fraction is shared — overlap without caring about order. author: Paul Jaccard (1901). extent: full (verbatim). reasoning: SCIENCE.md L3/L4 lineage table. application: VISITED_JACCARD_SIMILARITY, HIT_EVIDENCE_OVERLAP_*, EVIDENCE_JACCARD_BS, BOOKSET_JACCARD_BS.",
    "**HWIKI-DOC-16:** Product overlap applications across L3/L4.")

# ===== TRUST =====
add("FGR (Formality/Ground/Reliability)", CAT_TRUST, "BEYOND", "External framework",
    "sphere/fpf_bridge/constants.py", "⟨F,G,R⟩ tuple",
    "F = how rigorously a claim is expressed, G = the context-slice it claims to hold over, R = how well it is evidenced — trust as a computed tuple, not a single scalar.",
    [], ["FGR DOMINANT_SHARE_HIGH", "FGR freshness stability map"],
    "FPF Part B.3, 'Trust & Assurance Calculus' (Anatoly Levenchuk) — Theory Explainer: plain_lang: trust is three numbers, not one vibe score — how formal the claim is, what scope it covers, how well it is evidenced. author: Anatoly Levenchuk / FPF Part B.3. extent: full application of FGR calculus specifically (not all of FPF Spec). reasoning: SCIENCE.md; superseded Java ad hoc evidenceQuality upward. application: [[FGR DOMINANT_SHARE_HIGH]], [[FGR freshness stability map]]; contrast dead [[evidenceQuality / provenanceWeight (Java)]].",
    "**HWIKI-DOC-26:** Explainable Formality/Ground/Reliability terms; share/freshness map applications.")

# ===== CONCEPT DICTIONARY =====
add("PageRank-shaped walk (structural analogy)", CAT_CD, "LIVE_FULL", "Concept / theory term",
    "docs/publication/SCIENCE.md lineage table; core/math/core_math.py base_step", "v' = (1−λ)v + λ·vW (lazy form)",
    "Structural analogy only: the lazy-random-walk mixing form matches PageRank's damping walk; Hesperia's W is semantic adjacency, not a web-link graph, and no eigenvector-convergence claim is made.",
    ["lambda (lazy step)", "Transition matrix (W)"], ["Chapman-Kolmogorov Multi-Step", "Mixing Diagnostics"],
    "Brin & Page (1998), 'The Anatomy of a Large-Scale Hypertextual Web Search Engine' — Theory Explainer: plain_lang: PageRank spreads importance by repeatedly mixing 'stay put' with 'follow a link'; Hesperia reuses that *shape* for energy diffusion on areas, not ranking web pages. author: Sergey Brin & Larry Page (1998). extent: structural_analogy only. reasoning: SCIENCE.md cites the form explicitly; do not claim PageRank product semantics. application: [[lambda (lazy step)]], [[Transition matrix (W)]], [[Chapman-Kolmogorov Multi-Step]].",
    "**HWIKI-DOC-08:** Cite SCIENCE.md — structural analogy only; never claim Hesperia runs PageRank.")

add("Markov-like (term)", CAT_CD, "LIVE_FULL", "Concept / theory term",
    "docs/publication/SCIENCE.md; core/math/core_math.py", "—",
    "Discipline label: hand-set transition weights and lazy steps — *not* a fitted HMM or learned Markov model.",
    ["lambda (lazy step)", "Transition matrix (W)"], ["PageRank-shaped walk (structural analogy)", "structural analogy (extent term)"],
    "A.A. Markov (1906) chain formalism — Theory Explainer: plain_lang: 'Markov-like' means the math shape of a chain step is used; it does **not** mean the system learned transition probabilities from data. author: Markov (1906) as the named shape; Hesperia term discipline is SCIENCE.md. extent: terminology / structural_analogy. reasoning: prevents overclaiming HMM. application: [[lambda (lazy step)]], [[Transition matrix (W)]].",
    "**HWIKI-DOC-27:** Concept Dictionary entry — pair with [[structural analogy (extent term)]].")

add("LIVE_SUCCESSOR (status term)", CAT_CD, "LIVE_FULL", "Concept / status vocabulary",
    "wiki status legend / generate_wiki.py STATUS_LABEL", "LIVE_SUCCESSOR",
    "Same scientific idea as a Java ancestor, but different name and/or formula in the LIVE tree.",
    [], ["cosine_similarity", "compute_tension", "dominant_area_share_threshold"],
    "Hesperia wiki status vocabulary — Theory Explainer: plain_lang: the ancestor idea survived, but the shipped symbol is not a 1:1 rename — check the page's formula before equating. author: wiki STATUS_LABEL (Colombo/Felix audit convention). extent: full (status code). reasoning: prevents false 'DEAD' or false 'identical' claims. application: e.g. [[cosine_similarity]], [[compute_tension]].",
    "**HWIKI-DOC-27:** Status vocabulary — contrast [[DEAD_ALGO_SURVIVED (status term)]].")

add("DEAD_ALGO_SURVIVED (status term)", CAT_CD, "LIVE_FULL", "Concept / status vocabulary",
    "wiki status legend / generate_wiki.py STATUS_LABEL", "DEAD_ALGO_SURVIVED",
    "Java *name* is dead; the underlying algorithm still runs under another symbol/substrate.",
    [], ["largest_component_size", "K(R) / L(R) / fragIndex (Java)"],
    "Hesperia wiki status vocabulary — Theory Explainer: plain_lang: do not revive the Java name — find the live algorithm page and cite that. author: wiki STATUS_LABEL. extent: full (status code). reasoning: flagship case [[largest_component_size]] ≡ Java L(R). application: [[K(R) / L(R) / fragIndex (Java)]], [[largest_component_size]].",
    "**HWIKI-DOC-27:** Status vocabulary — name dead, algorithm lived.")

add("structural analogy (extent term)", CAT_CD, "LIVE_FULL", "Concept / extent vocabulary",
    "docs/publication/SCIENCE.md extent column; Theory Explainer schema", "structural_analogy",
    "Shared mathematical *form* with a named theory, without claiming the theory's full product semantics or proofs.",
    ["PageRank-shaped walk (structural analogy)", "Markov-like (term)"], ["LYAPUNOV_ESTIMATE / GLOBAL_STABILITY_SCORE", "Wiener feedback on alpha (k_s / k_j)"],
    "HWIKI-DOC-01 Theory Explainer extent label — Theory Explainer: plain_lang: 'looks like X mathematically' is not 'implements X'. author: SCIENCE.md extent taxonomy + DOC-01 schema. extent: meta (how we label other pages). reasoning: honesty discipline for PageRank/Lyapunov/Wiener cites. application: [[PageRank-shaped walk (structural analogy)]], [[Markov-like (term)]], [[LYAPUNOV_ESTIMATE / GLOBAL_STABILITY_SCORE]].",
    "**HWIKI-DOC-27:** Extent vocabulary — pairs with full / partial / rejected_with_reason.")

add("apply_saturation", CAT_CD, "LIVE_FULL", "Formula / function",
    "hesperia/engine/concept_dictionary/executor.py:13", "saturation_k (per-concept)",
    "Closed-form weight-capping curve, documented in `docs/governance/cd_v1/SATURATION_CLOSED_FORM.md`.",
    [], [], "No Java ancestor (narrower, differently-scoped concept than Java's composite decision-layer `saturation`)",
    "Not a gap against [[saturation (Java, 23_PROTOTYPE)]] — different, correctly-scoped tool for a different job.")
add("structural_coherence_pass", CAT_CD, "DEAD", "Formula / function",
    "n/a — core/math/dict_b.py deleted (f44b3454, confirmed-dead duplicate, zero importers)", "—", "Coherence pass over Dict-B exclusion structure.",
    ["build_exclusion_pairs / area_projection"], ["tension_from_conflict"], "Java 20_GEOMETRY `C(R)=L/active`",
    "Reclassified 2026-08-04 — repo-wide grep for `structural_coherence_pass` (any case) returns zero hits outside this wiki's own generator. No successor formula found anywhere in current source; see [[tension_from_conflict]] notes for the module-ownership reasoning.")
add("build_exclusion_pairs / area_projection", CAT_CD, "DEAD_ALGO_SURVIVED", "Formula / function",
    "core/result/contract.py:64 (inlined `i, i+6` in compute_tension)", "—", "Constructs opposite-area exclusion pairs and projects weights onto areas.",
    ["OPPOSITE_OFFSET"], ["structural_coherence_pass", "tension_from_conflict"], "No direct Java ancestor",
    "Reclassified 2026-08-04: no standalone function survives (core/math/dict_b.py deleted, f44b3454), but the exclusion-pair construction itself is inlined verbatim as `pairs = [(i, i + 6) for i in range(6)]` inside [[compute_tension]] — same as [[OPPOSITE_OFFSET]]'s finding. Not to be confused with `build_family_area_projection` in sphere/propagation/family_projection.py — despite the similar name, that function distributes propagated mass across families within an area (a different job); it is not this function's successor.")

# ===== DEAD / REJECTED =====
add("KL divergence", CAT_DEAD, "REJECTED", "Formula (never implemented)",
    "n/a — zero matches for `kl_divergence`/`def kl(` in any `.py`", "—",
    "kl(p,q) = Σ p_i·log(p_i/q_i) — Java 21_MATH proposed relative entropy between two distributions.",
    [], [],
    "Kullback & Leibler (1951) / Java 21_MATH `kl(p,q)` — Theory Explainer: plain_lang: how different distribution p is from q; blows up if q has a zero where p does not. author: Kullback–Leibler (1951) as the Java proposal's theory family. extent: rejected_with_reason. reasoning: [[eta (centroid threshold)]] + [[E_cap]] manufacture exact zeros → KL undefined; Shannon [[compute_entropy (Shannon)]] stays. application: contrast Shannon; FPD/APD L2 profile distance fills the comparison slot.",
    "**HWIKI-DOC-03:** Structural reason, not taste. Kolmogorov complexity was separately, explicitly rejected as uncomputable — same discipline, different item.")

add("DFT Ring Smoothness", CAT_DEAD, "REJECTED", "Formula (never implemented)",
    "n/a — zero matches for `np.fft`/`scipy.fft`/`ringSmoothness` in any `.py`", "—",
    "Fourier/DFT-based smoothness measure over a proposed 12-area ring (`AREA_RING_ORDER`), plus a Java `Complex` class.",
    ["Icosahedral Surface Graph"], [],
    "Java 21_MATH §10 / 23_PROTOTYPE — Theory Explainer: plain_lang: a ring Fourier smoothness score needs areas arranged on a circle (each has two neighbors); Hesperia's areas sit on an icosahedron where each has five neighbors — wrong topology for that DFT. author: Java proposal (DFT/ringSmoothness); rejection is Hesperia geometry decision. extent: rejected_with_reason. reasoning: [[Icosahedral Surface Graph]] is 5-regular (`degree_per_node: 5` in adjacency JSON); ring-DFT needs 2-regular C₁₂. application: contrast [[compute_entropy (Shannon)]] / dominance already covering 'smoothness-like' questions.",
    "**HWIKI-DOC-11:** Topology incompatibility — Felix verify degree: `assets/topology/area_adjacency_matrix.json` `degree_per_node: 5`. Not an oversight.")

add("K(R) / L(R) / fragIndex (Java)", CAT_DEAD, "DEAD_ALGO_SURVIVED", "Formula (name dead)",
    "n/a — zero matches for `fragIndex`/`frag_index`/`K(R)` style symbols", "—",
    "K(R) = discrete graph cluster count, L(R) = largest component, F(R)=K = fragmentation index, over the raw per-side truth-boolean graph.",
    [], [], "Java 20_GEOMETRY",
    "**Algorithm survived verbatim, substrate and name changed**: [[largest_component_size]] in KME's primitive calculator is the same deterministic-DFS component sizer, running on `ActiveGraph` (concept graph) instead of the retired per-side truth lattice. See also [[Circuit rank (LOOP_COUNT/LOOP_DENSITY)]] (same discipline, different invariant) and [[Louvain communities (seed 42)]] (different discipline — do not equate).")

add("S=T·C·X_A / S′ composite (Java)", CAT_DEAD, "DEAD", "Formula (never implemented)",
    "n/a", "—", "Composite structural score combining truth, coherence, and area/family alignment shares.",
    [], [], "Java 20_GEOMETRY", "Six-key metrics (governance, obstacle_score, tension family) replaced the instinct of one composite S; see [[metric_governance]].")

add("ALPHA/BETA/GAMMA/DELTA integrity quartet (Java)", CAT_DEAD, "DEAD", "Formula (never implemented)",
    "n/a — not in DEFAULT_CONFIG", "ALPHA=0.35, BETA=0.30, GAMMA=0.25, DELTA=0.20",
    "4-constant exponential decay model driving contextIntegrity / forecastIntegrity / regionReliability.",
    [], [], "Java 21_MATH v1.1 (Stability Control Formalization)",
    "**Documented design pivot**: shipped control is additive penalty-governance ([[metric_governance]]), not multiplicative exponential-integrity powers — easier to reason about and CI-test per-penalty. [[LYAPUNOV_ESTIMATE / GLOBAL_STABILITY_SCORE]] is the live descendant of the same underlying question ('will this read degrade'), via a different, honestly-labeled proxy.")

add("meanTau/varTau/stdTau/fillingRate/adjacencyCorrelation (Java)", CAT_DEAD, "DEAD", "Formula (never implemented)",
    "n/a — `tau_s` itself has zero matches", "TAU_THRESHOLD=0.8",
    "Statistics on the per-side boolean truth array tau[].", [], [], "Java 21_MATH",
    "Dead by the same root cause as [[K(R) / L(R) / fragIndex (Java)]] — the tau[] substrate itself was replaced by continuous energy vectors; nothing to compute these statistics from without reviving a retired layer.")

add("cumulativeDrift / turnCoherence", CAT_DEAD, "DEAD", "Formula (never implemented)",
    "n/a", "—", "Turn-to-turn coherence and cumulative drift via cosine similarity across a multi-turn session.",
    [], [], "Java 21_MATH",
    "**Cleanest 'taken toward, wrong boundary' case in the register.** [[Mixing Diagnostics]] already computes the same shape (consecutive L1 distance + entropy along a state sequence) for within-run diffusion steps; nobody has moved that machinery to a turn-to-turn boundary yet. [[cosine_similarity]] (the other half of what this needed) already exists, repurposed for fingerprints.")

add("expectedTimeToObstacle (Java)", CAT_DEAD, "DEAD", "Formula (never implemented)", "n/a", "—",
    "Predicted turns-to-obstacle metric.", [], [], "Java 21_MATH",
    "No documented downstream consumer even in the prototype notes; low value if revived.")

add("utility / strategicScore / actionScore (Java)", CAT_DEAD, "DEAD", "Formula (never implemented)", "n/a", "—",
    "Decision-layer composite scores from `23_PROTOTYPE`.", [], [], "Java 23_PROTOTYPE",
    "**Pattern survived, proliferation did not.** [[metric_governance]] and [[metric_obstacle_score]] are the same linear-scalarization pattern, consolidated to two CI-governed composites instead of many loosely-named ones with no stated distinguishing formula.")

add("causalCoherence / decisionIntegrity / temporalStability (Java)", CAT_DEAD, "DEAD", "Formula (never implemented)", "n/a", "—",
    "Further 23_PROTOTYPE decision composites.", [], [], "Java 23_PROTOTYPE",
    "`temporalStability`/`tauTemporal` is the one item in this cluster worth a second look now that session infrastructure exists (`hesperia/nlp/session_topology.py`) — see [[cumulativeDrift / turnCoherence]] for the concrete mechanism it would reuse.")

add("IPS / QCS (Java)", CAT_DEAD, "DEAD", "Formula (never implemented)", "n/a — word-boundary grep: zero hits", "—",
    "Unnamed-in-full composite decision scores from 23_PROTOTYPE.", [], [], "Java 23_PROTOTYPE",
    "Raw substring grep on `IPS`/`QCS` returns false positives (e.g. `SHIPS`); word-boundary-verified zero real hits.")

add("domainFit / scaleConsistency / compatibilityScore (Java)", CAT_DEAD, "DEAD", "Formula (never implemented)", "n/a", "—",
    "Further 23_PROTOTYPE decision composites.", [], [], "Java 23_PROTOTYPE", "Same pattern as [[utility / strategicScore / actionScore (Java)]].")

add("runLoop / shouldBreak (Java)", CAT_DEAD, "DEAD", "Formula (never implemented, as named)", "n/a", "—",
    "Traversal-control primitive from 23_PROTOTYPE.", [], [], "Java 23_PROTOTYPE",
    "Traversal itself is very much alive under other APIs — the T_steps loop in [[lambda (lazy step)]], BFS in L2, the agentic bridge's state graph. Only this specific named control surface never shipped.")

add("evidenceQuality / provenanceWeight (Java)", CAT_DEAD, "DEAD", "Formula (never implemented)", "n/a", "—",
    "Ad hoc per-item evidence-quality scalar from 23_PROTOTYPE.", [], [], "Java 23_PROTOTYPE",
    "**Superseded upward**: [[FGR (Formality/Ground/Reliability)]] is a real, independently-specified external trust calculus that solves the problem this was guessing at, more rigorously. Do not reimplement the Java version — it would be strictly worse than what shipped.")

add("summaryFidelity / compressionRatio (Java)", CAT_DEAD, "DEAD", "Formula (never implemented)", "n/a", "—",
    "Product-compression quality composites from 23_PROTOTYPE.", [], [], "Java 23_PROTOTYPE",
    "Covered functionally via loopability/stability in the product-compression path; no gap.")

add("X_A / X_F alignment (Java)", CAT_DEAD, "PARTIAL", "Formula (name dead, concept partial)", "n/a — literal `X_A`/`X_F` symbols: zero word-boundary hits", "—",
    "Dominant area (X_A) / family (X_F) alignment shares.", [], [], "Java 20_GEOMETRY",
    "X_A side: real, wired successor — [[dominant_area_share_threshold]]. X_F side: only an index detector exists ([[detect_dominant_area / detect_dominant_family]]), **no `compute_dominant_family_share` counterpart** — the single cheapest genuine gap identified across all three prior passes.")

add("Sentence capacity 3-5/side (Java)", CAT_DEAD, "PARTIAL", "Constraint (schema only)",
    "assets/lexicon/validation/validate_lexical.py", "3–5 sentences", "Capacity bound on generated content per side.",
    [], [], "Java 20_GEOMETRY", "Schema/validation only — no runtime generation-side enforcer found; unclear if any current producer could violate the bound.")

add("tau_s per-side truth (Java)", CAT_DEAD, "DEAD", "Data structure (never implemented)",
    "n/a — zero matches for `tau_s`", "tau_s ∈ [0,1]",
    "Atomic per-side boolean/scalar truth value.", [], [], "Java 20_GEOMETRY",
    "Replaced by continuous energy vectors ([[alpha (fusion weight)|E0]]) — a deliberate substrate change, not an oversight. Root cause for [[K(R) / L(R) / fragIndex (Java)]] and [[meanTau/varTau/stdTau/fillingRate/adjacencyCorrelation (Java)]] both being dead.")

add("saturation (Java, 23_PROTOTYPE)", CAT_DEAD, "PARTIAL", "Formula (different concept survives)",
    "n/a as a decision-layer composite", "—", "23_PROTOTYPE composite 'saturation' decision score.",
    [], [], "Java 23_PROTOTYPE", "Not the same object as the live [[apply_saturation]] (concept-dictionary weight cap) — no gap, different tool.")


# ---------------------------------------------------------------------------
# Rendering
# ---------------------------------------------------------------------------
NAME_TO_SLUG = {it["name"]: slug(it["name"]) for it in ITEMS}

def link_or_text(name):
    name = name.strip()
    if not name:
        return ""
    # already contains a manual [[...]] link or markdown link — pass through
    if "[[" in name or "](" in name:
        return linkify_inline(name)
    if name in NAME_TO_SLUG:
        return f"[{name}](../pages/{NAME_TO_SLUG[name]}.md)"
    return f"*{name}*"

def linkify_inline(text):
    # convert [[Page Name]] or [[Page Name|label]] occurring inside notes into relative md links
    def repl(m):
        inner = m.group(1)
        if "|" in inner:
            target, label = inner.split("|", 1)
        else:
            target, label = inner, inner
        target = target.strip()
        label = label.strip()
        if target in NAME_TO_SLUG:
            return f"[{label}](../pages/{NAME_TO_SLUG[target]}.md)"
        return f"*{label}*"
    return re.sub(r"\[\[([^\]]+)\]\]", repl, text)

def render_page(it):
    s = it
    lines = []
    lines.append(f"# {s['name']}\n")
    lines.append(f"**Status:** {STATUS_LABEL.get(s['status'], s['status'])}  ")
    lines.append(f"**Category:** [{s['category']}](../categories/{slug(s['category'])}.md)  ")
    lines.append(f"**Type:** {s['kind']}  ")
    lines.append(f"**Responsible (module):** `{s['module']}`  ")
    lines.append(f"**Value / default:** {s['value']}\n")
    lines.append("## Yields (formula)\n")
    lines.append(f"{linkify_inline(s['formula'])}\n")
    if s["produced_from"]:
        lines.append("## Produced from (inputs)\n")
        for p in s["produced_from"]:
            lines.append(f"- {link_or_text(p)}")
        lines.append("")
    if s["needed_by"]:
        lines.append("## Needed by (consumers)\n")
        for n in s["needed_by"]:
            lines.append(f"- {link_or_text(n)}")
        lines.append("")
    lines.append("## Origin\n")
    lines.append(f"{linkify_inline(s['origin'])}\n")
    if s["notes"]:
        lines.append("## Notes\n")
        lines.append(f"{linkify_inline(s['notes'])}\n")
    lines.append("---")
    lines.append("[← back to category](../categories/%s.md) · [wiki home](../index.md)" % slug(s['category']))
    return "\n".join(lines) + "\n"

def render_category(cat_name):
    members = [it for it in ITEMS if it["category"] == cat_name]
    members.sort(key=lambda it: it["name"].lower())
    lines = [f"# {cat_name}\n", f"[← wiki home](../index.md)\n"]
    preamble = CATEGORY_PREAMBLES.get(cat_name)
    if preamble:
        lines.append(linkify_inline(preamble) + "\n")
    lines.extend(["| Item | Status | Type |", "|---|---|---|"])
    for it in members:
        lines.append(f"| [{it['name']}](../pages/{slug(it['name'])}.md) | {it['status']} | {it['kind']} |")
    lines.append("")
    return "\n".join(lines) + "\n"

def render_index():
    lines = ["# Hesperia Parameter & Variable Wiki\n"]
    lines.append("**New here or an agent picking this up cold? Read [CLAUDE.md](CLAUDE.md) first** — what this is, how it's served, how to update it, ownership.\n")
    lines.append("Bottom-up, wikipedia-style register of every math variable/parameter this research thread has verified in `/data/hesperia/hesperia` — LIVE, PARTIAL, and DEAD/proposed-but-never-built alike. Each page: **status, type, responsible module, value, formula (yields), produced-from (inputs), needed-by (consumers), origin, notes** — interlinked for navigation.\n")
    lines.append("Companion research (symbol-level and discipline-level audits this wiki is built from):\n")
    lines.append("- [COLOMBO-HESPERIA-JAVA-PROPOSED-VS-ACCOMPLISHED-AUDIT-2026-07-19.md](../COLOMBO-HESPERIA-JAVA-PROPOSED-VS-ACCOMPLISHED-AUDIT-2026-07-19.md)")
    lines.append("- [COLOMBO-HESPERIA-MATH-PARAMS-THEORY-MAP-2026-07-19.md](../COLOMBO-HESPERIA-MATH-PARAMS-THEORY-MAP-2026-07-19.md)")
    lines.append("- [FELIX-HESPERIA-DEAD-PARTIAL-REIMPLEMENTATION-VIABILITY-2026-07-19.md](../FELIX-HESPERIA-DEAD-PARTIAL-REIMPLEMENTATION-VIABILITY-2026-07-19.md)")
    lines.append("- [COLOMBO-HESPERIA-DEAD-SCIENCE-BOTTOM-UP-SURFACE-2026-07-19.md](../COLOMBO-HESPERIA-DEAD-SCIENCE-BOTTOM-UP-SURFACE-2026-07-19.md)\n")
    lines.append("**[Coverage Ledger — what's in this wiki and what isn't yet](Coverage-Ledger.md)** — read this before assuming completeness.\n")
    lines.append("## System structure @ 0.7.0 (how it works)\n")
    lines.append("Sealed identity hubs (hand-authored under `structure/` — not parameter ITEMS):\n")
    lines.append("- [Phase @ 0.7.0 — freeze · grind · awareness](structure/PHASE-070-FREEZE-GRIND-AWARE.md) — post-seal product phase")
    lines.append("- [System structure @ 0.7.0](structure/SYSTEM-STRUCTURE-0.7.0.md) — core / interpret / Class A·B / apply gate")
    lines.append("- [How it works @ 0.7.0](structure/HOW-IT-WORKS-0.7.0.md) — Plane A sealed analyze + `/product/interpret` + ground_truth schemes")
    lines.append("- [HAND faces @ 0.7.0](structure/HAND-FACES-0.7.0.md) — inquire vs dig under fpf-thinking-map HAND")
    lines.append("- [Apply allowlist @ 0.7.0](structure/APPLY-ALLOWLIST-0.7.0.md) — H070 `update_edge_weight` only")
    lines.append("- [COBALT / REAL_DATA gates @ 0.7.0](structure/COBALT-REAL-DATA-GATES-0.7.0.md) — Class B flags stay off")
    lines.append("- [Class A/B science narrative hub](CLASS-AB-SCIENCE-NARRATIVE-HUB.md) — theories binding core vs TFP/MRT/COBALT")
    lines.append("- Phase frame: [HESPERIA-POST-070-PHASE-FRAME.md](../../../governance/HESPERIA-POST-070-PHASE-FRAME.md) · Inventory: [COLOMBO-HWIKI-STRUCT-01](../../../operational/assignments/COLOMBO-HWIKI-STRUCT-01-INVENTORY-070-2026-07-26.md)\n")
    lines.append("## Categories\n")
    for cat in CATEGORIES:
        n = len([it for it in ITEMS if it["category"] == cat])
        lines.append(f"- [{cat}](categories/{slug(cat)}.md) ({n} items)")
    lines.append("\n## Status legend\n")
    for k, v in STATUS_LABEL.items():
        lines.append(f"- **{k}**: {v}")
    lines.append(f"\n## All pages ({len(ITEMS)} total)\n")
    for it in sorted(ITEMS, key=lambda x: x["name"].lower()):
        lines.append(f"- [{it['name']}](pages/{slug(it['name'])}.md) — {it['status']}")
    return "\n".join(lines) + "\n"

def render_coverage_ledger():
    live = [it for it in ITEMS if it["status"] in ("LIVE_FULL", "LIVE_SUCCESSOR", "BEYOND")]
    partial = [it for it in ITEMS if it["status"] == "PARTIAL"]
    dead = [it for it in ITEMS if it["status"] in ("DEAD", "REJECTED", "DEAD_ALGO_SURVIVED")]
    unverified = [it for it in ITEMS if it["status"] == "UNVERIFIED"]
    kme_derived = [it for it in ITEMS if it["name"].endswith("(KME derived)")]
    l6 = [it for it in ITEMS if "(L6)" in it["name"] or it["name"].startswith("LYAPUNOV")]
    lines = ["# Coverage Ledger\n", "[← wiki home](index.md)\n"]
    lines.append(f"This wiki covers **{len(ITEMS)} items** verified on `/data/hesperia/hesperia` "
                  f"({len(live)} live/beyond, {len(partial)} partial, {len(dead)} dead/rejected, {len(unverified)} unverified). "
                  "It is **not** a full census of every variable in the codebase — bounded to inspected research passes plus HWIKI expansion waves.\n")
    lines.append("**Expansion waves:** all-encompassing `HWIKI-*` — [GRACE-TRIAGE-HESPERIA-WIKI-ALL-ENCOMPASSING-2026-07-19.md](../../../operational/assignments/GRACE-TRIAGE-HESPERIA-WIKI-ALL-ENCOMPASSING-2026-07-19.md). "
                  "**Theory-depth 30** (`HWIKI-DOC-01..30`) — [GRACE-TRIAGE-HESPERIA-WIKI-DOC-THEORY-DEPTH-30-2026-07-19.md](../../../operational/assignments/GRACE-TRIAGE-HESPERIA-WIKI-DOC-THEORY-DEPTH-30-2026-07-19.md). "
                  "**Structure / how-it-works (post 0.7.0)** (`HWIKI-STRUCT-*`) — [GRACE-TRIAGE-HESPERIA-WIKI-STRUCT-070-2026-07-26.md](../../../operational/assignments/GRACE-TRIAGE-HESPERIA-WIKI-STRUCT-070-2026-07-26.md). Gaps below are backlog, not permanent silence.\n")
    lines.append("## Explicitly NOT yet covered (real gaps in this wiki, not silently omitted)\n")
    lines.append("- **L1–L11 pipeline layer variables** (`34_SPEC`…`42_SPEC`, ~25 named variables per layer × 9 layers) — **L6 Lyapunov + curvature/gradient/depth-growth block wikified** (%d L6-related pages). Remaining L6 Group-IV stubs (HIT_VECTOR_RANK, ESCAPE_ENERGY, …) and **L1–L5 / L9–L11** full census still open. L7/L8 stability consumers of GLOBAL_STABILITY_SCORE landed (HWIKI-L7-01 / L8-01)." % len(l6))
    lines.append("- **KME derived metrics** — **35 derived + hub wikified** (%d derived pages + [KME Primitives and Derived Metrics](pages/%s.md)). **HWIKI-KME-03:** plain-lang Theory Explainer notes on each derived page." % (len(kme_derived), slug("KME Primitives and Derived Metrics")))
    lines.append("- **TRIZ extension internals** (`hesperia/extensions/triz/`, 30+ modules) — **contradiction core hub landed** (HWIKI-TRIZ-02); remaining novelty/topology/commercial modules still open beyond Louvain.")
    lines.append("- **Full `parameter_catalog.md` sweep** — CAT-02 landed top diagnostic + FGR freshness pair; field-dynamics env knobs and remaining CAT-01 leftovers still open: [COLOMBO-HWIKI-CAT-01-PARAMETER-CATALOG-DELTA-2026-07-23.md](../../../operational/assignments/COLOMBO-HWIKI-CAT-01-PARAMETER-CATALOG-DELTA-2026-07-23.md).")
    lines.append("- **Post-0.7.0 structure depth:** hubs under [structure/](structure/README.md) — SYSTEM-STRUCTURE, HOW-IT-WORKS, HAND-FACES, APPLY-ALLOWLIST, COBALT-REAL-DATA-GATES. Felix STRUCT-05 code-anchor PASS; Cursor STRUCT-06 ingest DONE.")
    lines.append("\n## Theory-depth wave (HWIKI-DOC-02..29) — refreshed 2026-07-23 (DOC-30)\n")
    lines.append("- **Explainer blocks landed** on OPEN DOC targets this pass: PageRank structural analogy, PHI/icosahedron, DFT REJECTED, Gini, BM25, Jaccard, cosine, Louvain, clustering (PARTIAL+`layer_2` pin), circuit rank, contradiction→tension, penalty suite hub, propagation YAML ladder, fusion α/E_cap/η, FGR + share/freshness, Concept Dictionary status/extent terms, Geometry/Core Math/Propagation hub preambles.")
    lines.append("- **Remaining theory gaps (next batch candidates):** deeper TRIZ inventives beyond Louvain/contradiction map; L7/L8 consumers of GLOBAL_STABILITY_SCORE; KME derived plain-lang names beyond stubs; CAT-01 leftover symbols; turn-boundary Mixing (dead [[cumulativeDrift / turnCoherence]] revival decision).")
    lines.append("\n## Structure / how-it-works wave (HWIKI-STRUCT) — opened 2026-07-26\n")
    lines.append("- **Landed:** [System structure](structure/SYSTEM-STRUCTURE-0.7.0.md) · [How it works](structure/HOW-IT-WORKS-0.7.0.md) · [HAND faces](structure/HAND-FACES-0.7.0.md) · [Apply allowlist](structure/APPLY-ALLOWLIST-0.7.0.md) · [COBALT/REAL_DATA gates](structure/COBALT-REAL-DATA-GATES-0.7.0.md).")
    lines.append("- **Verify:** [FELIX-HWIKI-STRUCT-05](../../../operational/assignments/FELIX-HWIKI-STRUCT-05-CODE-ANCHOR-VERIFY-2026-07-26.md) PASS · ingest includes `structure/*.md`.")
    lines.append("\n## Resolved questions (were open; evidence now on the page)\n")
    lines.append("- **[compute_tension](pages/%s.md)** (HWIKI-OPEN-01): `(i,i+6)` is **not** geometrically antipodal after `get_aligned_area_coordinates` — combinatorial [[OPPOSITE_OFFSET]], not sphere antipodes." % slug("compute_tension"))
    lines.append("- **[Wiener feedback on alpha (k_s / k_j)](pages/%s.md)** (HWIKI-OPEN-02): relocated LIVE_SUCCESSOR → `sphere/propagation/weighting.py` as `k_stability`/`k_jump` (diffusion α, not fusion α)." % slug("Wiener feedback on alpha (k_s / k_j)"))
    lines.append("- **[Mixing Diagnostics](pages/%s.md)** (HWIKI-OPEN-03): line-by-line confirmed as `propagation_depth_metric` (`consecutive_l1` + `entropy_sequence` via canonical `compute_normalized_entropy`)." % slug("Mixing Diagnostics"))
    lines.append("\n## Open / unresolved questions carried into this wiki (do not treat as settled)\n")
    lines.append("- *(none from the original three Coverage-Ledger open Qs — all resolved 2026-07-23.)*")
    lines.append("\n## Cheap, concrete next-wave candidates\n")
    lines.append("- Add `compute_dominant_family_share` as a real page once/if built (mirrors [dominant_area_share_threshold](pages/%s.md)) — see [X_A / X_F alignment (Java)](pages/%s.md)." % (slug("dominant_area_share_threshold"), slug("X_A / X_F alignment (Java)")))
    lines.append("- Finish remaining L6 variables (curvature/gradient/depth-growth block) then L7/L8 consumers of GLOBAL_STABILITY_SCORE.")
    lines.append("- Wikify CAT-01 delta list (diagnostic ultra_sparse / field-dynamics / FGR numeric table leftovers).")
    return "\n".join(lines) + "\n"


def render_json():
    """Structured mirror of ITEMS for tooling (MCP server, code<->wiki linker).
    Deterministic, sorted by name — diff-friendly."""
    records = []
    for it in sorted(ITEMS, key=lambda x: x["name"].lower()):
        page_slug = slug(it["name"])
        cat_slug = slug(it["category"])
        records.append({
            "name": it["name"],
            "slug": page_slug,
            "category": it["category"],
            "category_slug": cat_slug,
            "status": it["status"],
            "status_label": STATUS_LABEL.get(it["status"], it["status"]),
            "kind": it["kind"],
            "module": it["module"],
            "value": it["value"],
            "formula": it["formula"],
            "produced_from": it["produced_from"],
            "needed_by": it["needed_by"],
            "origin": it["origin"],
            "notes": it["notes"],
            "source_page": f"pages/{page_slug}.md",
            "source_page_abs": os.path.join(PAGES, page_slug + ".md"),
            "lan_url": f"{LAN_URL}/pages/{page_slug}.html",
            "tailnet_url": f"{TAILNET_URL}/pages/{page_slug}.html",
        })
    payload = {
        "generated_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "count": len(records),
        "categories": CATEGORIES,
        "status_vocab": STATUS_LABEL,
        "items": records,
    }
    return json.dumps(payload, indent=2, ensure_ascii=False) + "\n"


def main():
    os.makedirs(PAGES, exist_ok=True)
    os.makedirs(CATS, exist_ok=True)
    for it in ITEMS:
        with open(os.path.join(PAGES, slug(it["name"]) + ".md"), "w") as f:
            f.write(render_page(it))
    for cat in CATEGORIES:
        with open(os.path.join(CATS, slug(cat) + ".md"), "w") as f:
            f.write(render_category(cat))
    with open(os.path.join(ROOT, "index.md"), "w") as f:
        f.write(render_index())
    with open(os.path.join(ROOT, "Coverage-Ledger.md"), "w") as f:
        f.write(render_coverage_ledger())
    with open(os.path.join(ROOT, "index.json"), "w") as f:
        f.write(render_json())
    print(f"Generated {len(ITEMS)} pages, {len(CATEGORIES)} category hubs, index.md, Coverage-Ledger.md, index.json")

if __name__ == "__main__":
    main()
