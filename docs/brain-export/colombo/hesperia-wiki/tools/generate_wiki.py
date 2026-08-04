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

def theory_explainer(plain, author, extent="full", reasoning="", application=""):
    """HWIKI-PLAIN — durable plain-language block embedded in origin (see TEMPLATES-PLAIN-DEFINITION.md)."""
    parts = [
        f"Theory Explainer: plain_lang: {plain}. author: {author}. extent: {extent}."
    ]
    if reasoning:
        parts.append(f" reasoning: {reasoning}.")
    if application:
        parts.append(f" application: {application}.")
    return "".join(parts)

def extract_plain_lang(*blobs):
    """Pull Theory Explainer plain_lang from origin/notes text."""
    for blob in blobs:
        if not blob:
            continue
        m = re.search(r"plain_lang:\s*(.+?)(?:\s+author:|\s*$)", blob, re.DOTALL)
        if m:
            return re.sub(r"\s+", " ", m.group(1)).strip().rstrip(".")
    return ""

def extract_te_field(blob, field):
    if not blob:
        return ""
    m = re.search(rf"{field}:\s*(.+?)(?:\s+(?:author|extent|reasoning|application):|\s*$)", blob, re.DOTALL)
    if not m:
        return ""
    return re.sub(r"\s+", " ", m.group(1)).strip().rstrip(".")

def _first_note_sentence(notes):
    if not notes:
        return ""
    s = re.sub(r"\*\*[^*]+\*\*:\s*", "", notes)
    s = re.sub(r"\[\[([^\]]+)\]\]", r"\1", s)
    s = re.sub(r"\s+", " ", s).strip()
    parts = re.split(r"(?<=[.!?])\s+", s, maxsplit=1)
    return (parts[0] if parts else s).strip().rstrip(".")[:280]

def backfill_plain_lang():
    """HWIKI-PLAIN batch B — every ITEMS row gets Theory Explainer plain_lang in origin if missing.
    Uses existing formula (often already plain) + notes; does not invent science."""
    extent_map = {
        "LIVE_FULL": "full",
        "LIVE_SUCCESSOR": "full",
        "BEYOND": "full",
        "PARTIAL": "partial",
        "DEAD": "dead",
        "DEAD_ALGO_SURVIVED": "structural_analogy",
        "REJECTED": "rejected_with_reason",
        "UNVERIFIED": "unverified",
    }
    filled = 0
    for it in ITEMS:
        if extract_plain_lang(it.get("origin"), it.get("notes")):
            continue
        formula = (it.get("formula") or "").strip()
        notes = it.get("notes") or ""
        plain = formula
        if plain.lower().startswith("hub:"):
            plain = plain[4:].strip()
        if len(plain) < 16 and notes:
            plain = _first_note_sentence(notes) or plain
        plain = re.sub(r"\s+", " ", plain).strip().rstrip(".")
        if not plain:
            plain = f"{it['kind']}: {it['name']}"
        reason = _first_note_sentence(notes)
        if not reason or reason.lower() == plain.lower():
            reason = f"{it['status']} {it['kind']} in {it['category']}"
        apps = list(it.get("needed_by") or [])[:3] or list(it.get("produced_from") or [])[:2]
        application = ", ".join(f"[[{a}]]" for a in apps) if apps else it["category"]
        te = theory_explainer(
            plain,
            f"Hesperia wiki ({it['module']})"[:100],
            extent=extent_map.get(it["status"], "full"),
            reasoning=reason[:240],
            application=application[:220],
        )
        origin = (it.get("origin") or "").rstrip()
        it["origin"] = f"{origin} — {te}" if origin else te
        tag = "**HWIKI-PLAIN-B:** plain_lang backfilled from formula/notes 2026-08-04."
        it["notes"] = f"{tag} {notes}".strip() if notes else tag
        filled += 1
    return filled

def rewrite_plain_lang(it, plain, reasoning=None, tag="**HWIKI-PLAIN-C:**"):
    """Replace Theory Explainer plain_lang in origin (keeps author/extent/application when present)."""
    origin = it.get("origin") or ""
    author = extract_te_field(origin, "author") or f"Hesperia wiki ({it.get('module', '')})"[:100]
    extent = extract_te_field(origin, "extent") or {
        "PARTIAL": "partial", "REJECTED": "rejected_with_reason", "DEAD": "dead",
        "DEAD_ALGO_SURVIVED": "structural_analogy", "LIVE_SUCCESSOR": "full",
        "BEYOND": "full", "LIVE_FULL": "full", "UNVERIFIED": "unverified",
    }.get(it.get("status"), "full")
    reason = reasoning or extract_te_field(origin, "reasoning") or f"{it['status']} {it['kind']} in {it['category']}"
    application = extract_te_field(origin, "application") or it.get("category", "")
    # Drop any prior Theory Explainer block, then append polished one
    base = re.sub(r"\s*—?\s*Theory Explainer:.*$", "", origin, flags=re.DOTALL).rstrip(" —")
    te = theory_explainer(plain.rstrip("."), author, extent=extent, reasoning=reason, application=application)
    it["origin"] = f"{base} — {te}" if base else te
    notes = it.get("notes") or ""
    if tag not in notes:
        it["notes"] = f"{tag} algebra plain_lang polished 2026-08-04. {notes}".strip()

def polish_plain_lang():
    """HWIKI-PLAIN batch C — hand-polish rows where plain_lang was still formula-shaped."""
    # name -> (plain_lang, optional reasoning)
    polish = {
        "compute_ld (LogicalDensity)": (
            "how densely the active concept graph is wired — average degree of active nodes over a high-degree reference (Deg95), clamped to [0,1]",
            "KME primitive LD — connectivity intensity of the live subgraph",
        ),
        "compute_ci (ConcentrationIndex)": (
            "how piled-up hits are on a few nodes versus spread evenly — a normalized Herfindahl (HHI) concentration score on node hit-counts",
            "KME primitive CI — concentration, not component count",
        ),
        "compute_nc (NodeCoverage)": (
            "what fraction of the whole concept domain lit up — active nodes divided by total nodes (n/N)",
            "KME primitive NC — coverage of the domain",
        ),
        "compute_tension": (
            "how uneven opposite area-pairs are — sum absolute gaps between each area and its partner six indices away on the 12-area vector",
            "LIVE tension aggregator; pairing is combinatorial OPPOSITE_OFFSET, not sphere antipodes",
        ),
        "compute_structural_tension": (
            "how contested the area field is — one minus the dominant area's share of total activation (closer to 1 means no clear winner)",
            "dominance-competition tension; HHI-adjacent building block",
        ),
        "decay": (
            "after each diffusion step, shrink remaining energy by a fixed fraction so the field does not stay forever-hot — damped attrition before the next step",
            "discrete-time attrition after diffusion; partner of E_cap",
        ),
        "shadow_step": (
            "run the same energy through a separate 'shadow' transition matrix to estimate fallback/correction cost without changing the main field",
            "shadow propagation for governance/obstacle costing",
        ),
        "metric_tension_energy": (
            "how close the top two family energies are — when the gap shrinks, tension_energy rises (ambiguous which family leads)",
            "surviving v0.3-era tension name used by governance/TRIZ consumers",
        ),
        "metric_obstacle_score": (
            "a weighted health tax from decay loss, guard failures, and shadow hops — higher means the run paid more structural friction",
            "composite obstacle score feeding governance",
        ),
        "DEPTH_GROWTH_RATIO (L6)": (
            "how much activation mass grows from BFS depth 0 to depth 1 — mass_at_depth[1] over mass_at_depth[0]; 0 if the ladder is too short",
            "LIVE L6 depth-growth signal from the activation mass ladder",
        ),
        "FIBONACCI_DEVIATION_SCORE (L6)": (
            "how far the depth-2 mass strays from 'depth1 + depth0' (Fibonacci-like growth) — large deviation means the ladder is not additive",
            "LIVE L6 fibonacci-like deviation on the depth mass ladder",
        ),
        "CONCEPTUAL_COHERENCE_INDEX (L6)": (
            "a single L6 coherence read: stability radius × (1 − family entropy) × global stability — high when the structure is both stable and focused",
            "combines STABILITY_RADIUS, L1 entropy, and GLOBAL_STABILITY_SCORE",
        ),
        "CONDITION_NUMBER (L6)": (
            "how ill-conditioned the hit/response surface looks — enters global stability; stubs to 1.0 when no perturbation data exists",
            "L6 ill-conditioning proxy",
        ),
        "TOTAL_FAMILIES": (
            "size of the family vector — always 12 areas × 24 families per area = 288 slots Sigma shape-checks against",
            "fixed ontology grain for family-activation vectors",
        ),
        "TOTAL_HEXES": (
            "finest hex count under the ontology — TOTAL_FAMILIES × HEXES_PER_FAMILY; Euler checks use this lattice size",
            "hex substrate census",
        ),
        "TOTAL_SIDES": (
            "absolute side census — TOTAL_HEXES × 6 sides per hex (72,000-base variant)",
            "dimensionality of energy sides / truth units at full rollup",
        ),
        "FAMILIES_PER_AREA": (
            "fixed ontology grain — each of the 12 areas owns exactly this many families (24)",
            "partner of AREAS and TOTAL_FAMILIES",
        ),
        "AREAS": (
            "fixed ontology grain — always 12 therapy areas, one per icosahedron vertex; area vectors must be length 12",
            "geometry/ontology constant under Sigma shape checks",
        ),
        "SIDES_PER_HEX": (
            "each hex has six sides — uniform hexagonal adjacency for the finest energy grain",
            "lattice constant for TOTAL_SIDES",
        ),
        "HEXES_PER_FAMILY": (
            "how many hex cells roll up into one family — finest landing grain before family aggregation (PARTIAL 251-variant disclosed separately)",
            "hex→family resolution",
        ),
        "SI_GLOBAL_STABILITY_U1000 (L8)": (
            "publish L6's global stability score on the 0–1000 unit scale so L9 and humans never see the raw ratio",
            "L8 rescale consumer of GLOBAL_STABILITY_SCORE",
        ),
        "SI_GLOBAL_STABILITY_PCT (L8)": (
            "same L6 global stability, published as a percent (0–100) twin of the U1000 form",
            "percent twin of SI_GLOBAL_STABILITY_U1000",
        ),
        "SI_SYSTEM_CONFIDENCE_U1000 (L8)": (
            "publish L7's system confidence on the 0–1000 scale — the confidence number L9 bands and brand words read",
            "L8 rescale of SYSTEM_CONFIDENCE_SCORE (L6→L7→L8 chain)",
        ),
        "SYSTEM_CONFIDENCE_SCORE (L7)": (
            "L7's overall confidence that the structural read is trustworthy — folds consistency gates and includes L6 global stability",
            "primary L7 consumer of GLOBAL_STABILITY_SCORE",
        ),
        "REALITY_GATE_TRIG": (
            "hard pass/fail: every trig/metric-space self-test residual must sit inside tolerance — if this fails, do not trust angle-based claims",
            "summary gate over the 13 L5 trig residuals",
        ),
        "K_max": (
            "hard cap on how many centroid indices may be selected as 'active' in one traversal",
            "limits how many simultaneous activation foci the core math keeps",
        ),
        "activation_threshold": (
            "sparse activation floor — below this energy a cell does not count as a hit",
            "diagnostics/config threshold for hit detection",
        ),
        "area_active_threshold": (
            "coverage floor that decides whether an area counts as 'touched' for aggregation",
            "area-level activation threshold",
        ),
        "dominant_area_share_threshold": (
            "if the dominant area's share of activation clears this threshold, classify the read as dominance (wired successor of Java X_A)",
            "share-fraction rule trigger in rules config",
        ),
        "entropy_threshold (monotony)": (
            "if family entropy falls below this, label the discourse structurally narrow (monotony regime)",
            "pairs with coverage_threshold for monotony",
        ),
        "coverage_threshold (monotony)": (
            "coverage floor used with entropy_threshold to decide the monotony regime",
            "joint monotony gate with entropy",
        ),
        "Energy conservation epsilon": (
            "after diffusion, total energy must match the pre-diffusion total within this tiny epsilon (before decay) — catches broken stochastic matrices",
            "conservation check on E·W before decay",
        ),
        "energy_conservation_tolerance": (
            "how much drift the pre-decay energy-conservation check allows before rejecting the step",
            "tolerance twin of Energy conservation epsilon",
        ),
        "BFS depth-capped traversal": (
            "walk outward from the start family by unweighted shortest hops, stopping at a max depth — the L2 reachability engine",
            "Moore/Lee BFS used by L2 topology",
        ),
        "count_triangles / count_connected_triplets": (
            "count three-node cliques (and connected triplets) in the visited graph — feeds local clustering-style metrics",
            "triangle/triplet census for clustering",
        ),
        "shadow_step": (
            "push energy through a separate shadow transition matrix to estimate correction cost without rewriting the main field",
            "shadow propagation for fallback costing",
        ),
        "Relation weights (conflict/opposition)": (
            "fixed edge weights for conflict/negation (1.0) and opposition (0.85) — how strongly adversity edges feed tension",
            "typed adversity weights into tension_energy / TRIZ",
        ),
        "apply_saturation": (
            "closed-form curve that caps concept-dictionary weights so no single weight runs away — documented saturation, not the dead Java composite score",
            "LIVE weight-capping; distinct from Java 23_PROTOTYPE saturation",
        ),
        "STABILITY_RADIUS (L6)": (
            "claimed radius of local structural stability — multiplies into conceptual coherence; stubs to 1.0 without perturbation data",
            "L6 stability-radius factor",
        ),
        "SPECTRAL_GAP (L6)": (
            "proxy for how fast the response operator mixes/expands — neighbor of Lyapunov/condition; stubs to 0 without perturbation",
            "L6 mixing/expansion gap proxy",
        ),
        "HIT_VECTOR_RANK (L6)": (
            "rank of the family hit vector (scaffold; often stubbed as rank-1) reserved for a future perturbation-analysis pass",
            "L6 Group-IV scaffold constant",
        ),
        "PRINCIPAL_COMPONENT_ENERGY_RATIO (L6)": (
            "fraction of hit-vector energy sitting in the leading component — scaffold for future PCA-style analysis",
            "L6 Group-IV scaffold constant",
        ),
        "ESCAPE_ENERGY_THRESHOLD (L6)": (
            "how much energy would be needed to leave the current structural basin — scaffold threshold, not a live escape simulation today",
            "L6 Group-IV scaffold constant",
        ),
        "FORCE_ANALOG_MAGNITUDE (L6)": (
            "force-like magnitude from the potential-field scaffold (usually stubbed 0 until perturbation analysis is live)",
            "L6 Group-IV scaffold constant",
        ),
        "MONOTONICITY_CHECK (L6)": (
            "whether activation mass decays monotonically across BFS depth — flags non-monotonic ladders",
            "L6 Group-IV depth-ladder check",
        ),
        "FIXED_POINT_DETECTION (L6)": (
            "whether the structural read has settled into a fixed point (no further meaningful change under the scaffold test)",
            "L6 Group-IV dynamical fixed-point flag",
        ),
        "CYCLE_DETECTION_FUNCTIONAL (L6)": (
            "whether a dynamical cycle was detected across the functional/response scaffold",
            "L6 Group-IV cycle-detection flag",
        ),
    }
    n = 0
    by_name = {it["name"]: it for it in ITEMS}
    for name, (plain, reason) in polish.items():
        it = by_name.get(name)
        if not it:
            continue
        rewrite_plain_lang(it, plain, reasoning=reason)
        n += 1
    return n

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
    _plain = (
        f"{_hint} — a clamped [0,1] fingerprint feature from KME primitives "
        f"(LD=logical density, COH=coherence, NC=node coverage, PR=presence, PV=volume, CI=concentration); "
        f"algebra `{_formula}` only, not a clinical TFP judgment"
    )
    add(_name, CAT_GRAPH, "LIVE_FULL", "Derived metric",
        f"core/domain/derived_metrics.py:{_line}", "—",
        _formula,
        ["KME Primitives and Derived Metrics"],
        ["core/domain/pipeline.py", "core/domain/fingerprint.py"],
        "BEYOND Java — pure algebra over PrimitiveMetrics (clamp01 + safe_div) — "
        + theory_explainer(
            _plain,
            "Hesperia KME derived layer (no classical namesake)",
            extent="product_metric",
            reasoning="clamp01+safe_div keeps fingerprint comparable across runs",
            application="pipeline / clinical_bridge / fingerprint",
        ),
        f"**HWIKI-KME-01/03 / HWIKI-PLAIN-C:** {_hint}. Formula `{_formula}`. Consumers: pipeline / clinical_bridge / fingerprint (Felix HWIKI-KME-02). Not clinical TFP judgment — algebra only.")

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

# ===== L1 — STRUCTURAL ACTIVATION CENSUS (HWIKI-CATALOG-L1, docs/foundations/output_catalog.md §1) =====
# Source-verified against core/layers/layer_1.py::compute_L1 directly (not just output_catalog.md's
# table) 2026-08-04. GINI_COEFFICIENT excluded — already wikified as "Gini concentration". Base 27 keys
# always present; 6 profile keys only when a structure profile is supplied to compute_L1.
add("L1 — Structural Activation Census", CAT_GRAPH, "BEYOND", "Hub / concept",
    "core/layers/layer_1.py::compute_L1 (34_SPEC)", "27 base + up to 6 profile",
    "Hub: token-attribution census — the first of nine pipeline layers (L1-L9), everything downstream is built on this layer's family/area hit counts.",
    ["ActiveGraph (KME concept graph)"], ["STRUCTURAL_STABILITY_INDEX", "L2 — Topology Traversal"],
    "Hesperia-native `34_SPEC` L1 instrumentation — docstring claims 25 variables, actual base return dict has 27 keys (recovered-spec resolution: item 18 bundles two names into one spec entry; PROFILE_MODE_ACTIVE is a code-only flag outside the spec's numbered list) — "
    + theory_explainer(
        "token-attribution census — the first of nine pipeline layers; everything downstream is built on this layer's family/area hit counts",
        "Hesperia L1 hub (34_SPEC)",
        reasoning="foundation layer for L2–L9 structural and trust pipeline",
        application="[[STRUCTURAL_STABILITY_INDEX]], [[L2 — Topology Traversal]]",
    ),
    "**HWIKI-CATALOG-L1 / HWIKI-PLAIN:** `docs/foundations/output_catalog.md` §1 already did the source-verification — this hub + per-variable pages transcribe that research, re-verified against `compute_L1`.")

_L1_BASE = [
    ("PROFILE_MODE_ACTIVE", "LIVE_FULL", "Parameter (flag)", "bool", "profile is not None",
     "Whether a structure profile was supplied for this run — set explicitly from the input argument, never inferred from downstream profile-conformance keys being present."),
    ("TOTAL_TOKENS", "LIVE_FULL", "Derived variable", "int", "len(input tokens)", "Token count of the input — the denominator for coverage."),
    ("ATTRIBUTED_TOKENS", "LIVE_FULL", "Derived variable", "int", "sum(hits)", "Tokens matched to Dict A/B — the numerator for coverage, and the base for every downstream ratio in this layer."),
    ("COVERAGE_RATIO", "LIVE_FULL", "Derived variable", "float [0,1]", "attributed / total_tokens", "Fraction of input tokens that produced a concept hit at all."),
    ("UNIQUE_FAMILIES_HIT", "LIVE_FULL", "Derived variable", "int [0,288]", "count(hits[f] > 0)", "Count of distinct families with at least one hit."),
    ("FAMILY_ACTIVATION_DENSITY", "LIVE_FULL", "Derived variable", "float [0,1]", "unique_families / F", "Fraction of all 288 families touched at all this run."),
    ("FAMILY_HIT_VECTOR_L1", "LIVE_FULL", "Derived variable", "float", "float(attributed)", "L1 norm of the family hit vector — numerically identical to ATTRIBUTED_TOKENS, kept as a separate named field for the norm-pair symmetry with L2."),
    ("FAMILY_HIT_VECTOR_L2", "LIVE_FULL", "Derived variable", "float", "sqrt(sum(h*h for h in hits))", "L2 norm of the family hit vector — how concentrated the hit distribution is (higher relative to L1 norm = fewer families carrying more weight each)."),
    ("MAX_FAMILY_HITS", "LIVE_FULL", "Derived variable", "int", "max(hits)", "Peak single-family hit count."),
    ("DOMINANT_FAMILY_ID", "LIVE_FULL", "Derived variable", "int [0,287]", "argmax(hits), first index on ties", "Which family had the most hits this run."),
    ("DOMINANT_AREA_ID", "LIVE_FULL", "Derived variable", "int [0,11]", "dominant_family // FAMILIES_PER_AREA", "Which of the 12 areas the dominant family belongs to."),
    ("DOMINANCE_RATIO", "LIVE_FULL", "Derived variable", "float [0,1]", "max_hits / (attributed + eps)", "How much of all attributed activity landed in the single dominant family — feeds STRUCTURAL_STABILITY_INDEX directly."),
    ("MEAN_ALTITUDE_GLOBAL", "LIVE_FULL", "Derived variable", "float [0,1]", "sum(altitude_sum) / (attributed + eps)", "Hit-weighted mean altitude across all families — altitude is the per-hit depth/specificity score carried in from concept matching."),
    ("MEAN_ALTITUDE_DOMINANT", "LIVE_FULL", "Derived variable", "float [0,1]", "altitude_sum[dominant] / (hits[dominant] + eps)", "Mean altitude within the dominant family only, not the global average."),
    ("ALTITUDE_VARIANCE_GLOBAL", "LIVE_FULL", "Derived variable", "float", "hit-weighted variance of per-family mean altitude", "How much altitude varies across the families that were hit — low variance means a consistent depth of match everywhere."),
    ("FAMILY_ENTROPY", "LIVE_FULL", "Derived variable", "float [0, ln F]", "-sum(p*log(p) for p in family_probs)", "Shannon entropy of the family hit distribution — raw (unnormalized) information-theoretic spread."),
    ("NORMALIZED_FAMILY_ENTROPY", "LIVE_FULL", "Derived variable", "float [0,1]", "min(1.0, FAMILY_ENTROPY / ln(F))", "FAMILY_ENTROPY rescaled to [0,1] — the form every downstream consumer (STRUCTURAL_STABILITY_INDEX, L7 SYSTEM_CONFIDENCE_SCORE) actually uses."),
    ("UNIQUE_AREAS_HIT", "LIVE_FULL", "Derived variable", "int [0,12]", "count of distinct areas with >=1 hit", "How many of the 12 areas were touched at all — coarser-grained version of UNIQUE_FAMILIES_HIT."),
    ("AREA_SPREAD", "LIVE_FULL", "Derived variable", "float [0,1]", "unique_areas / A", "Fraction of the 12 areas touched — area-level counterpart to FAMILY_ACTIVATION_DENSITY."),
    ("AREA_DOMINANCE_RATIO", "LIVE_FULL", "Derived variable", "float [0,1]", "hits_in_dominant_area / (attributed + eps)", "How much of all activity landed in the dominant family's area specifically, not just the dominant family itself."),
    ("SECONDARY_FAMILY_RATIO", "LIVE_FULL", "Derived variable", "float [0,1]", "second_max_hits / (max_hits + eps)", "How close the runner-up family came to the dominant one — near 1.0 means a genuine two-way split, not a clear single dominant."),
    ("SIGNAL_TO_NOISE_RATIO", "LIVE_FULL", "Derived variable", "float >=0", "max_hits / (attributed - max_hits + eps)", "Dominant family's hits versus everything else combined — how much the read is 'about one thing' versus diffuse."),
    ("SPARSITY_INDEX", "LIVE_FULL", "Derived variable", "float [0,1]", "1 - FAMILY_ACTIVATION_DENSITY", "Direct complement of activation density — how much of the 288-family space stayed completely untouched."),
    ("TOKEN_REDUNDANCY_RATIO", "LIVE_FULL", "Derived variable", "float [0,1]", "1 - (unique_families / (attributed + eps))", "How much repeated hitting of the same few families happened versus each attributed token landing somewhere new."),
    ("ALTITUDE_WEIGHTED_MASS", "LIVE_FULL", "Derived variable", "float >=0", "sum(hits[f] * mean_altitude[f] for hit families)", "Total activation mass weighted by how deep/specific each hit was, summed across every family that was touched."),
    ("STRUCTURAL_STABILITY_INDEX", "LIVE_FULL", "Derived variable", "float [0,1]", "DOMINANCE_RATIO * (1 - NORMALIZED_FAMILY_ENTROPY)", "L1's single composite read on 'how structurally settled is this activation' — high when one family dominates AND the overall spread is low-entropy. Feeds L7 SYSTEM_CONFIDENCE_SCORE directly (see output_catalog.md's worked 'Confidence' example)."),
]
_L1_ENTROPY_NAMES = {"FAMILY_ENTROPY", "NORMALIZED_FAMILY_ENTROPY"}
for _name, _status, _kind, _rng, _formula_expr, _meaning in _L1_BASE:
    _cat = CAT_ENTROPY if _name in _L1_ENTROPY_NAMES else CAT_GRAPH
    add(_name, _cat, _status, _kind,
        f"core/layers/layer_1.py::compute_L1 -> result[\"{_name}\"]", _rng,
        _formula_expr,
        ["L1 — Structural Activation Census"], [],
        "Hesperia-native `34_SPEC` L1 instrumentation — no Java prototype ancestor for the L1-L9 layer pipeline as a whole — "
        + theory_explainer(
            _meaning,
            "Hesperia L1 (34_SPEC / output_catalog §1)",
            reasoning="L1 census field — first pipeline layer every later layer reads",
            application="[[L1 — Structural Activation Census]], L2–L9",
        ),
        f"**HWIKI-CATALOG-L1 / HWIKI-PLAIN:** {_meaning} Source: `docs/foundations/output_catalog.md` §1, re-verified against `compute_L1` 2026-08-04.")

_L1_PROFILE = [
    ("PROFILE_ID", "PARTIAL", "Parameter (flag)", "str", "Name/version string identifying the active profile."),
    ("PROFILE_VERSION", "PARTIAL", "Parameter (flag)", "str", "The profile's own version tag."),
    ("PROFILE_CHECKSUM", "PARTIAL", "Parameter (flag)", "str", "Content hash of the profile, for audit trail."),
    ("FAMILY_PROFILE_DEVIATION", "PARTIAL", "Derived variable", "float", "L2 distance between observed and expected family distribution, normalized by /sqrt(2)."),
    ("AREA_PROFILE_DEVIATION", "PARTIAL", "Derived variable", "float", "Same L2-distance deviation measure, at area grain instead of family grain."),
    ("PROFILE_CONFORMANCE_SCORE", "PARTIAL", "Derived variable", "float", "1 - weighted_penalty — hard-gates L7 decision code 75 when too low."),
]
for _name, _status, _kind, _rng, _meaning in _L1_PROFILE:
    add(_name, CAT_GRAPH, _status, _kind,
        f"core/layers/layer_1.py::compute_L1 -> result[\"{_name}\"] (profile-conditional)", _rng,
        "See notes — profile-conformance formula, only computed when a StructureProfile is supplied.",
        ["L1 — Structural Activation Census"], [],
        "Hesperia-native `34_SPEC N1` profile-conformance extension — no Java prototype ancestor — "
        + theory_explainer(
            _meaning,
            "Hesperia L1 profile extension (34_SPEC N1)",
            extent="partial",
            reasoning="only present when a StructureProfile is supplied to compute_L1",
            application="[[L1 — Structural Activation Census]], L7 conformance gates",
        ),
        f"**HWIKI-CATALOG-L1 / HWIKI-PLAIN:** {_meaning} PARTIAL because these keys only appear in `compute_L1`'s return dict when a `profile` argument is supplied — absent on every unprofiled run. Source: `docs/foundations/output_catalog.md` §1.")

_L1_PROFILE_CONDITIONAL = [
    ("FORBIDDEN_MASS_PENALTY", "profile has `DENY_FAMILIES`", "Hit mass landing in denied families."),
    ("ALTITUDE_DEVIATION", "profile has `ALT_BAND`/`ALT_TARGET`", "Distance from the profile's altitude band/target."),
    ("BUDGET_VIOLATION_SCORE", "profile has any `MAX_*`/`MIN_*` cap", "Worst single budget-cap breach (max, not averaged)."),
]
for _name, _condition, _meaning in _L1_PROFILE_CONDITIONAL:
    add(_name, CAT_GRAPH, "PARTIAL", "Derived variable",
        f"core/layers/layer_1.py::compute_L1 -> result[\"{_name}\"] (doubly-conditional)", "float",
        "See notes — only computed when both a profile is supplied and the profile sets the specific field this key checks.",
        ["L1 — Structural Activation Census"], [],
        "Hesperia-native `34_SPEC N1` profile-conformance extension — no Java prototype ancestor — "
        + theory_explainer(
            _meaning,
            "Hesperia L1 profile extension (34_SPEC N1)",
            extent="partial",
            reasoning=f"only when {_condition}",
            application="[[L1 — Structural Activation Census]]",
        ),
        f"**HWIKI-CATALOG-L1 / HWIKI-PLAIN:** {_meaning} Narrower than the other 6 profile keys: only appears when {_condition}, not merely when a profile is supplied at all. Source: `docs/foundations/output_catalog.md` §1.")

# ===== L2 — TOPOLOGY TRAVERSAL (HWIKI-CATALOG-L2, docs/foundations/output_catalog.md §2) =====
# Source-verified against core/layers/layer_2.py::compute_L2 2026-08-04. LOCAL_CLUSTERING_COEFFICIENT
# and LOOP_COUNT/LOOP_DENSITY excluded — already wikified as "Clustering coefficient" and
# "Circuit rank (LOOP_COUNT/LOOP_DENSITY)".
add("L2 — Topology Traversal", CAT_GRAPH, "BEYOND", "Hub / concept",
    "core/layers/layer_2.py::compute_L2 (35_SPEC)", "27",
    "Hub: BFS traversal from L1's dominant family outward — how far and how densely activation reaches through the concept graph.",
    ["L1 — Structural Activation Census", "BFS depth-capped traversal"], ["L3 — Baseline/Shadow Comparison"],
    "Hesperia-native `35_SPEC` L2 instrumentation — no Java prototype ancestor",
    "**HWIKI-CATALOG-L2:** Source: `docs/foundations/output_catalog.md` §2, re-verified against `compute_L2` 2026-08-04.")

_L2_BASE = [
    ("TRAVERSAL_START_FAMILY", "LIVE_FULL", "Derived variable", "int", "= L1 DOMINANT_FAMILY_ID", "BFS root — L2 always starts traversal from L1's dominant family, not an independent choice."),
    ("BASE_NEIGHBOR_COUNT", "LIVE_FULL", "Derived variable", "int", "degree(start_family)", "Graph degree of the start family — how many families it's directly adjacent to."),
    ("ACTIVE_NEIGHBOR_COUNT", "LIVE_FULL", "Derived variable", "int", "count(neighbors with >=1 hit)", "Of the start family's direct neighbors, how many were themselves hit this run."),
    ("NEIGHBOR_ACTIVATION_RATIO", "LIVE_FULL", "Derived variable", "float [0,1]", "ACTIVE_NEIGHBOR_COUNT / BASE_NEIGHBOR_COUNT", "Fraction of the start family's immediate neighborhood that lit up alongside it."),
    ("TRAVERSAL_DEPTH_REACHED", "LIVE_FULL", "Derived variable", "int", "max BFS depth with nonzero mass", "Deepest BFS ring that still carried any activation mass."),
    ("TOTAL_REACHABLE_NODES", "LIVE_FULL", "Derived variable", "int", "count(families visited within MAX_ALLOWED_DEPTH)", "Total families the BFS actually visited — the denominator for most of this layer's ratios."),
    ("REACH_RATIO", "LIVE_FULL", "Derived variable", "float [0,1]", "TOTAL_REACHABLE_NODES / F", "Visited families as a fraction of the full 288-family space."),
    ("MEAN_TRAVERSAL_DISTANCE", "LIVE_FULL", "Derived variable", "float", "mean(BFS hop distance over visited set)", "Average how-many-hops-away the visited families were from the start."),
    ("MAX_TRAVERSAL_DISTANCE", "LIVE_FULL", "Derived variable", "int", "max single hop distance reached", "Deepest single hop the BFS reached — bounded by MAX_ALLOWED_DEPTH."),
    ("TRAVERSAL_RADIUS_RATIO", "LIVE_FULL", "Derived variable", "float [0,1]", "MAX_TRAVERSAL_DISTANCE / MAX_ALLOWED_DEPTH", "How much of the allowed traversal depth budget actually got used."),
    ("PATH_COUNT", "LIVE_FULL", "Derived variable", "int", "TOTAL_REACHABLE_NODES - 1", "Edge count of the BFS spanning tree — one less than the node count, by construction."),
    ("BRANCHING_FACTOR_MEAN", "LIVE_FULL", "Derived variable", "float", "mean(degree over visited set)", "Average graph degree across every visited family, not just the start."),
    ("PROPAGATION_MASS_DECAY", "LIVE_FULL", "Derived variable", "float", "mass ratio, two deepest populated depths", "How fast activation mass thins out at the traversal's outer edge."),
    ("MASS_RETENTION_RATIO", "LIVE_FULL", "Derived variable", "float", "total visited-set mass / start family's own mass", "How much total activation the traversal picked up relative to just the start family alone — feeds GEOMETRIC_STABILITY_INDEX."),
    ("CROSS_AREA_TRAVERSAL_COUNT", "LIVE_FULL", "Derived variable", "int", "count(visited families outside dominant area)", "How many visited families live in a different area than the dominant one."),
    ("CROSS_AREA_RATIO", "LIVE_FULL", "Derived variable", "float [0,1]", "CROSS_AREA_TRAVERSAL_COUNT / TOTAL_REACHABLE_NODES", "Fraction of the traversal that spilled outside the dominant area — feeds L9 area-containment classification."),
    ("AREA_BOUNDARY_CROSSINGS", "LIVE_FULL", "Derived variable", "int", "count(BFS tree edges crossing an area boundary)", "How many single hops in the BFS tree itself crossed from one area into another."),
    ("TRAVERSAL_COMPACTNESS", "LIVE_FULL", "Derived variable", "float", "TOTAL_REACHABLE_NODES / (MAX_TRAVERSAL_DISTANCE + 1)", "How many families were reached per unit of traversal depth — high value means a wide, shallow spread rather than a narrow, deep one."),
    ("CENTRALITY_SHIFT", "LIVE_FULL", "Derived variable", "float", "abs(degree(start) - mean degree over visited set)", "How atypical the start family's connectivity is compared to the rest of the visited neighborhood."),
    ("EDGE_UTILIZATION_RATIO", "LIVE_FULL", "Derived variable", "float [0,1]", "BFS tree edges / total induced-subgraph edges", "What fraction of all edges among visited families the BFS tree itself actually used, versus edges that exist but weren't traversal edges."),
    ("TRAVERSAL_SYMMETRY_INDEX", "LIVE_FULL", "Derived variable", "float", "variance(BFS distance from start, over visited set)", "How evenly distances from the start are spread across the visited set — low variance means a roughly uniform ring-by-ring spread."),
    ("GEOMETRIC_STABILITY_INDEX", "LIVE_FULL", "Derived variable", "float [0,1]", "MASS_RETENTION_RATIO * (1-CROSS_AREA_RATIO) * (1-LOOP_DENSITY)", "L2's composite structural-settledness read — high when the traversal keeps its mass, stays within one area, and doesn't loop back on itself. Feeds L7/L9 PILLAR_GEOMETRY directly."),
    ("VISITED_IDS", "LIVE_FULL", "Derived variable", "list[int]", "family IDs reached by BFS", "Not an independent measurement — an internal handoff. Consumed by L3's Jaccard similarity and L7's g4 gate."),
    ("MASS_AT_DEPTH", "LIVE_FULL", "Derived variable", "list[float]", "per-depth mass profile", "Not an independent measurement — an internal handoff. Consumed by L6's DEPTH_GROWTH_RATIO."),
]
for _name, _status, _kind, _rng, _formula_expr, _meaning in _L2_BASE:
    add(_name, CAT_GRAPH, _status, _kind,
        f"core/layers/layer_2.py::compute_L2 -> result[\"{_name}\"]", _rng,
        _formula_expr,
        ["L2 — Topology Traversal"], [],
        "Hesperia-native `35_SPEC` L2 instrumentation — no Java prototype ancestor — "
        + theory_explainer(
            _meaning,
            "Hesperia L2 (35_SPEC / output_catalog §2)",
            reasoning="L2 topology-traversal field — how activation spreads from L1 dominant",
            application="[[L2 — Topology Traversal]], L3–L9",
        ),
        f"**HWIKI-CATALOG-L2 / HWIKI-PLAIN:** {_meaning} Source: `docs/foundations/output_catalog.md` §2, re-verified against `compute_L2` 2026-08-04.")

# ===== L3 — BASELINE/SHADOW COMPARISON (HWIKI-CATALOG-L3, docs/foundations/output_catalog.md §3) =====
# Source-verified against core/layers/layer_3.py::compute_L3 2026-08-04. GINI_DELTA and
# VISITED_JACCARD_SIMILARITY are separately mentioned inside "Gini concentration" / "Jaccard overlaps"
# (algorithm-level pages) but had no dedicated output-variable page of their own — added here.
add("L3 — Baseline/Shadow Comparison", CAT_GRAPH, "BEYOND", "Hub / concept",
    "core/layers/layer_3.py::compute_L3 (36_SPEC)", "25",
    "Hub: runs L1+L2 twice (baseline text vs. shadow/counter text) and diffs every metric — the layer that turns single-run measurements into a comparison.",
    ["L1 — Structural Activation Census", "L2 — Topology Traversal"], ["L4 — Evidence Retrieval"],
    "Hesperia-native `36_SPEC` L3 instrumentation — no Java prototype ancestor",
    "**HWIKI-CATALOG-L3:** Source: `docs/foundations/output_catalog.md` §3, re-verified against `compute_L3` 2026-08-04.")

_L3_BASE = [
    ("SHADOW_ENABLED", "LIVE_FULL", "Parameter (flag)", "bool", "True whenever L3 runs", "Always True when L3 runs at all — a shadow pair was supplied, this isn't a conditional check on the data itself."),
    ("DOMINANT_FAMILY_CHANGED", "LIVE_FULL", "Derived variable", "bool", "baseline.DOMINANT_FAMILY_ID != shadow.DOMINANT_FAMILY_ID", "Whether the single most-active family differs between baseline and shadow runs."),
    ("DOMINANT_AREA_CHANGED", "LIVE_FULL", "Derived variable", "bool", "baseline.DOMINANT_AREA_ID != shadow.DOMINANT_AREA_ID", "Coarser version of DOMINANT_FAMILY_CHANGED, at area grain."),
    ("DOMINANT_FAMILY_DELTA_HITS", "LIVE_FULL", "Derived variable", "int", "hit-count delta at each run's own dominant family", "How many more/fewer hits the (possibly different) dominant family got, shadow vs. baseline."),
    ("DOMINANCE_RATIO_DELTA", "LIVE_FULL", "Derived variable", "float", "shadow.DOMINANCE_RATIO - baseline.DOMINANCE_RATIO", "Change in how concentrated activation is in the single dominant family."),
    ("COVERAGE_RATIO_DELTA", "LIVE_FULL", "Derived variable", "float", "shadow.COVERAGE_RATIO - baseline.COVERAGE_RATIO", "Change in what fraction of tokens got attributed at all."),
    ("UNIQUE_FAMILIES_HIT_DELTA", "LIVE_FULL", "Derived variable", "int", "shadow.UNIQUE_FAMILIES_HIT - baseline.UNIQUE_FAMILIES_HIT", "Change in how many distinct families were touched."),
    ("AREA_SPREAD_DELTA", "LIVE_FULL", "Derived variable", "float", "shadow.AREA_SPREAD - baseline.AREA_SPREAD", "Change in how many of the 12 areas were touched."),
    ("ENTROPY_DELTA", "LIVE_FULL", "Derived variable", "float", "shadow.NORMALIZED_FAMILY_ENTROPY - baseline.NORMALIZED_FAMILY_ENTROPY", "Change in how spread-out (versus concentrated) the family hit distribution is."),
    ("GINI_DELTA", "LIVE_FULL", "Derived variable", "float", "shadow.GINI_COEFFICIENT - baseline.GINI_COEFFICIENT", "Change in [[Gini concentration]] between the two runs — L3's application of the general Jaccard/Gini algorithm pages to a paired comparison."),
    ("ALTITUDE_MEAN_DELTA", "LIVE_FULL", "Derived variable", "float", "shadow.MEAN_ALTITUDE_GLOBAL - baseline.MEAN_ALTITUDE_GLOBAL", "Change in average hit-weighted altitude across all families."),
    ("ALTITUDE_DOMINANT_DELTA", "LIVE_FULL", "Derived variable", "float", "shadow.MEAN_ALTITUDE_DOMINANT - baseline.MEAN_ALTITUDE_DOMINANT", "Change in mean altitude within just the (possibly different) dominant family."),
    ("TRAVERSAL_DEPTH_DELTA", "LIVE_FULL", "Derived variable", "int", "shadow.TRAVERSAL_DEPTH_REACHED - baseline.TRAVERSAL_DEPTH_REACHED", "Change in how deep the L2 BFS traversal reached."),
    ("REACHABLE_NODES_DELTA", "LIVE_FULL", "Derived variable", "int", "shadow.TOTAL_REACHABLE_NODES - baseline.TOTAL_REACHABLE_NODES", "Change in how many families the L2 traversal visited."),
    ("MAX_DISTANCE_DELTA", "LIVE_FULL", "Derived variable", "int", "shadow.MAX_TRAVERSAL_DISTANCE - baseline.MAX_TRAVERSAL_DISTANCE", "Change in the single deepest hop the L2 traversal reached."),
    ("CROSS_AREA_RATIO_DELTA", "LIVE_FULL", "Derived variable", "float", "shadow.CROSS_AREA_RATIO - baseline.CROSS_AREA_RATIO", "Change in how much the traversal spilled outside its dominant area."),
    ("LOOP_DENSITY_DELTA", "LIVE_FULL", "Derived variable", "float", "shadow.LOOP_DENSITY - baseline.LOOP_DENSITY", "Change in [[Circuit rank (LOOP_COUNT/LOOP_DENSITY)]] between the two runs."),
    ("EDGE_UTILIZATION_DELTA", "LIVE_FULL", "Derived variable", "float", "shadow.EDGE_UTILIZATION_RATIO - baseline.EDGE_UTILIZATION_RATIO", "Change in what fraction of available edges the BFS tree actually used."),
    ("VISITED_JACCARD_SIMILARITY", "LIVE_FULL", "Derived variable", "float [0,1]", "jaccard(baseline.VISITED_IDS, shadow.VISITED_IDS)", "How much the two runs' visited-family sets overlap — L3's specific application of [[Jaccard overlaps]] to L2's VISITED_IDS handoff."),
    ("VISITED_SYMMETRIC_DIFFERENCE_RATIO", "LIVE_FULL", "Derived variable", "float [0,1]", "1 - VISITED_JACCARD_SIMILARITY", "Direct complement of the Jaccard similarity — how much of the combined visited set was NOT shared."),
    ("FAMILY_HIT_VECTOR_L1_DELTA", "LIVE_FULL", "Derived variable", "float", "shadow.FAMILY_HIT_VECTOR_L1 - baseline.FAMILY_HIT_VECTOR_L1", "Change in the L1-norm hit-vector magnitude between the two runs."),
    ("HIT_VECTOR_COSINE_SIMILARITY", "LIVE_FULL", "Derived variable", "float [-1,1]", "cosine(baseline hit vector, shadow hit vector)", "How aligned the two runs' full family-hit-count vectors are in direction, independent of magnitude — see [[cosine_similarity]]."),
    ("TOP_K_OVERLAP_RATIO", "LIVE_FULL", "Derived variable", "float [0,1]", "overlap(top-K families, baseline vs. shadow) / K", "Whether the two runs agree on which families mattered most, not just on the single dominant one."),
    ("SHADOW_DEVIATION_SCORE", "LIVE_FULL", "Derived variable", "float", "0.35*(1-cosine) + 0.35*sym_diff + 0.30*abs(dominance_delta)", "L3's single composite read on how different the shadow run is from baseline — feeds L7/L9 decision logic."),
    ("SHADOW_ACCEPTABILITY_GATE", "LIVE_FULL", "Derived variable", "bool", "deviation, cross-area delta, and area-flip all within policy caps", "The hard pass/fail gate downstream layers check before trusting a shadow comparison at all."),
]
for _name, _status, _kind, _rng, _formula_expr, _meaning in _L3_BASE:
    add(_name, CAT_GRAPH, _status, _kind,
        f"core/layers/layer_3.py::compute_L3 -> result[\"{_name}\"]", _rng,
        _formula_expr,
        ["L3 — Baseline/Shadow Comparison"], [],
        "Hesperia-native `36_SPEC` L3 instrumentation — no Java prototype ancestor — "
        + theory_explainer(
            _meaning,
            "Hesperia L3 (36_SPEC / output_catalog §3)",
            reasoning="L3 baseline/shadow delta field — turns single-run measures into comparison",
            application="[[L3 — Baseline/Shadow Comparison]], L4–L9",
        ),
        f"**HWIKI-CATALOG-L3 / HWIKI-PLAIN:** {_meaning} Source: `docs/foundations/output_catalog.md` §3, re-verified against `compute_L3` 2026-08-04.")

# ===== L4 — EVIDENCE RETRIEVAL (HWIKI-CATALOG-L4, docs/foundations/output_catalog.md §4) =====
# Source-verified against core/layers/layer_4.py::compute_L4 2026-08-04.
add("L4 — Evidence Retrieval", CAT_TRUST, "BEYOND", "Hub / concept",
    "core/layers/layer_4.py::compute_L4 (37_SPEC)", "25",
    "Hub: retrieves supporting text chunks (BM25) for both baseline and shadow runs, then scores how well retrieval actually backs up what L1/L2 measured structurally.",
    ["BM25 retrieval", "L1 — Structural Activation Census", "L2 — Topology Traversal"], ["L5 — Counter-Evidence & Trig Invariants"],
    "Hesperia-native `37_SPEC` L4 instrumentation — no Java prototype ancestor",
    "**HWIKI-CATALOG-L4:** Source: `docs/foundations/output_catalog.md` §4, re-verified against `compute_L4` 2026-08-04.")

_L4_BASE = [
    ("RETRIEVAL_MODE_ID", "LIVE_FULL", "Parameter (flag)", "string", "\"LEX_BM25_V1\"", "Identifies which retrieval engine produced this layer's output — currently always the lexical BM25 implementation."),
    ("TOP_K", "LIVE_FULL", "Parameter (constant)", "int", "20 (default)", "Target retrieval count — how many chunks the engine tries to return."),
    ("RETRIEVED_COUNT_BASELINE", "LIVE_FULL", "Derived variable", "int", "len(retrieved chunks, baseline)", "Chunks actually retrieved for the baseline text — may fall short of TOP_K."),
    ("RETRIEVED_COUNT_SHADOW", "LIVE_FULL", "Derived variable", "int", "len(retrieved chunks, shadow)", "Same, for the shadow/counter text."),
    ("RETRIEVAL_SHORTFALL_BASELINE", "LIVE_FULL", "Derived variable", "int", "max(0, TOP_K - RETRIEVED_COUNT_BASELINE)", "How far baseline retrieval fell short of the TOP_K target — gates L9's ACTION_REQUIRE_EVIDENCE_REBUILD."),
    ("RETRIEVAL_SHORTFALL_SHADOW", "LIVE_FULL", "Derived variable", "int", "max(0, TOP_K - RETRIEVED_COUNT_SHADOW)", "Same shortfall measure, for the shadow run."),
    ("UNIQUE_BOOKS_BASELINE", "LIVE_FULL", "Derived variable", "int", "count(distinct source books, baseline retrieval)", "How many distinct source books the baseline retrieval drew from."),
    ("UNIQUE_BOOKS_SHADOW", "LIVE_FULL", "Derived variable", "int", "count(distinct source books, shadow retrieval)", "Same, for the shadow run."),
    ("DUPLICATE_BOOK_RATIO_BASELINE", "LIVE_FULL", "Derived variable", "float [0,1]", "1 - UNIQUE_BOOKS_BASELINE / RETRIEVED_COUNT_BASELINE", "How much of the baseline retrieval is repeat chunks from the same book rather than new sources."),
    ("DUPLICATE_BOOK_RATIO_SHADOW", "LIVE_FULL", "Derived variable", "float [0,1]", "1 - UNIQUE_BOOKS_SHADOW / RETRIEVED_COUNT_SHADOW", "Same, for the shadow run."),
    ("FAMILY_MATCH_COUNT_BASELINE", "LIVE_FULL", "Derived variable", "int", "count(retrieved chunks tagged with dominant family)", "How many retrieved chunks are actually tagged with L1's dominant family."),
    ("FAMILY_MATCH_RATIO_BASELINE", "LIVE_FULL", "Derived variable", "float [0,1]", "FAMILY_MATCH_COUNT_BASELINE / RETRIEVED_COUNT_BASELINE", "Fraction of retrieval that matches the dominant family — the single heaviest-weighted term (0.45) in EVIDENCE_SUPPORT_INDEX_BASELINE."),
    ("AREA_MATCH_RATIO_BASELINE", "LIVE_FULL", "Derived variable", "float [0,1]", "count(retrieved in dominant area) / RETRIEVED_COUNT_BASELINE", "Coarser version of FAMILY_MATCH_RATIO_BASELINE, at area grain — 0.35 weight in the support index."),
    ("TOP_K_FAMILY_COVERAGE_BASELINE", "LIVE_FULL", "Derived variable", "float [0,1]", "count(distinct families in retrieval) / F", "How many of the 288 families the retrieved evidence set touches at all, not just the dominant one."),
    ("EVIDENCE_ENTROPY_BASELINE", "LIVE_FULL", "Derived variable", "float [0,1]", "normalized Shannon entropy of retrieved-chunk family distribution", "How spread-out (versus concentrated) the retrieved evidence is across families."),
    ("EVIDENCE_GINI_BASELINE", "LIVE_FULL", "Derived variable", "float [0,1]", "[[Gini concentration]] of retrieved-chunk family distribution", "Inequality measure on the same distribution EVIDENCE_ENTROPY_BASELINE covers — the two can disagree in direction, same as L1's GINI_COEFFICIENT/FAMILY_ENTROPY pair."),
    ("RANK_WEIGHTED_ALIGNMENT_BASELINE", "LIVE_FULL", "Derived variable", "float [0,1]", "sum(1/(rank+1) for chunks in dominant area) / normalizer", "Like AREA_MATCH_RATIO_BASELINE but weighted so higher-ranked (more relevant) retrieved chunks count more."),
    ("HIT_EVIDENCE_OVERLAP_BASELINE", "LIVE_FULL", "Derived variable", "float [0,1]", "jaccard(hit families, retrieved-chunk families)", "How much overlap there is between which families L1 actually hit and which families the retrieved evidence covers — a [[Jaccard overlaps]] application, 0.20 weight in the support index."),
    ("HIT_EVIDENCE_OVERLAP_SHADOW", "LIVE_FULL", "Derived variable", "float [0,1]", "jaccard(hit families, retrieved-chunk families), shadow", "Same overlap measure, for the shadow run."),
    ("EVIDENCE_JACCARD_BS", "LIVE_FULL", "Derived variable", "float [0,1]", "jaccard(baseline retrieved chunk IDs, shadow retrieved chunk IDs)", "How much the baseline and shadow runs' actual retrieved chunk sets overlap — a [[Jaccard overlaps]] application."),
    ("BOOKSET_JACCARD_BS", "LIVE_FULL", "Derived variable", "float [0,1]", "jaccard(baseline book set, shadow book set)", "Coarser version of EVIDENCE_JACCARD_BS, at source-book grain instead of chunk grain."),
    ("EVIDENCE_SHIFT_SCORE", "LIVE_FULL", "Derived variable", "float [0,1]", "1 - EVIDENCE_JACCARD_BS", "Direct complement of EVIDENCE_JACCARD_BS — how much the evidence set shifted between baseline and shadow."),
    ("INTEGRITY_CHECK_PASS_RATIO", "LIVE_FULL", "Derived variable", "float [0,1]", "count(chunks with valid checksum) / retrieved", "Fraction of retrieved chunks that pass a checksum integrity check — gates L7's g6 hard guard."),
    ("EVIDENCE_SUPPORT_INDEX_BASELINE", "LIVE_FULL", "Derived variable", "float [0,1]", "0.45*FAMILY_MATCH_RATIO + 0.35*AREA_MATCH_RATIO + 0.20*HIT_EVIDENCE_OVERLAP", "L4's single most load-bearing output — the composite read on how well retrieved evidence actually supports what was structurally measured. Traces through L7/L8 rescale to L9 PILLAR_EVIDENCE_U1000 (see output_catalog.md's worked 'Trust' example)."),
    ("EVIDENCE_ACCEPTABILITY_GATE", "LIVE_FULL", "Derived variable", "bool", "integrity, shortfall, support, and duplication all within policy caps", "The hard pass/fail gate downstream layers check before trusting this layer's evidence at all — same pattern as L3's SHADOW_ACCEPTABILITY_GATE."),
]
for _name, _status, _kind, _rng, _formula_expr, _meaning in _L4_BASE:
    add(_name, CAT_TRUST, _status, _kind,
        f"core/layers/layer_4.py::compute_L4 -> result[\"{_name}\"]", _rng,
        _formula_expr,
        ["L4 — Evidence Retrieval"], [],
        "Hesperia-native `37_SPEC` L4 instrumentation — no Java prototype ancestor — "
        + theory_explainer(
            _meaning,
            "Hesperia L4 (37_SPEC / output_catalog §4)",
            reasoning="L4 evidence-retrieval field — how well retrieved text backs structural measures",
            application="[[L4 — Evidence Retrieval]], L5–L9",
        ),
        f"**HWIKI-CATALOG-L4 / HWIKI-PLAIN:** {_meaning} Source: `docs/foundations/output_catalog.md` §4, re-verified against `compute_L4` 2026-08-04.")

# ===== L5 — COUNTER-EVIDENCE & TRIG INVARIANTS (HWIKI-CATALOG-L5, docs/foundations/output_catalog.md §5) =====
# Source-verified against core/layers/layer_5.py::compute_L5 2026-08-04. Two unrelated halves:
# 5A counter-evidence/contradiction pressure, 5B trig/metric-space axiom self-test (6 of 13 residuals
# are hardcoded 0.0 reserved placeholders in the current deterministic-only mode -> marked PARTIAL,
# not LIVE_FULL, per the code's own explicit reservation comments, not silently upgraded).
add("L5 — Counter-Evidence & Trig Invariants", CAT_TRUST, "BEYOND", "Hub / concept",
    "core/layers/layer_5.py::compute_L5 (38_SPEC)", "25 (12 counter-evidence + 13 trig)",
    "Hub: two unrelated jobs sharing one layer — 5A retrieves and scores evidence AGAINST the dominant read (contradiction pressure); 5B self-tests the vector-space math itself (dot product, norm, angle axioms) as a sanity gate, not a content measurement.",
    ["L4 — Evidence Retrieval"], ["L7 — Consistency and Decision"],
    "Hesperia-native `38_SPEC` L5 instrumentation — no Java prototype ancestor",
    "**HWIKI-CATALOG-L5:** Source: `docs/foundations/output_catalog.md` §5, re-verified against `compute_L5` 2026-08-04.")

_L5A_BASE = [
    ("ANTI_REGION_SIZE", "int", "count(families flagged anti-dominant)", "How many families are flagged as structurally contradicting the dominant read."),
    ("RETRIEVED_COUNT_NEG", "int", "len(counter-evidence chunks retrieved)", "How many counter-evidence chunks the retrieval engine found, mirroring L4's RETRIEVED_COUNT_BASELINE but for the 'against' side."),
    ("NEG_SHORTFALL", "int", "max(0, TOP_K - RETRIEVED_COUNT_NEG)", "Counter-evidence version of L4's RETRIEVAL_SHORTFALL_BASELINE."),
    ("NEG_UNIQUE_BOOKS", "int", "count(distinct books, counter-evidence set)", "Counter-evidence version of L4's UNIQUE_BOOKS_BASELINE."),
    ("NEG_DUPLICATE_BOOK_RATIO", "float [0,1]", "1 - NEG_UNIQUE_BOOKS / RETRIEVED_COUNT_NEG", "Counter-evidence version of L4's DUPLICATE_BOOK_RATIO_BASELINE."),
    ("NEG_AREA_MATCH_RATIO", "float [0,1]", "count(counter-evidence in dominant area) / RETRIEVED_COUNT_NEG", "How much of the counter-evidence still lands in the dominant area — high values here weaken the 'genuine contradiction' read."),
    ("POS_NEG_BOOKSET_JACCARD", "float [0,1]", "jaccard(positive book set, negative book set)", "How much source overlap there is between supporting and contradicting evidence — 0.20 weight in CONTRADICTION_PRESSURE_SCORE."),
    ("POS_NEG_CHUNK_JACCARD", "float [0,1]", "jaccard(positive chunks, negative chunks)", "Finer-grained version of POS_NEG_BOOKSET_JACCARD, at chunk instead of book grain."),
    ("POS_SUPPORT_INDEX", "float [0,1]", "= L4 EVIDENCE_SUPPORT_INDEX_BASELINE (passthrough)", "Not independently computed — L5's name for L4's support index, kept alongside NEG_SUPPORT_INDEX so both sides of the pressure formula live in one place."),
    ("NEG_SUPPORT_INDEX", "float [0,1]", "count(counter-evidence tagged anti-family) / RETRIEVED_COUNT_NEG", "How well the counter-evidence actually supports the anti-dominant read — 0.55 weight, the heaviest term in CONTRADICTION_PRESSURE_SCORE."),
    ("CONTRADICTION_PRESSURE_SCORE", "float", "0.55*neg_support + 0.25*(1-pos_support) + 0.20*bookset_jaccard", "L5A's single composite read on how much genuine contradicting evidence exists — feeds L9 CONSISTENCY_U1000."),
    ("REALITY_GATE_COUNTER_EVIDENCE", "bool", "integrity, shortfall, and pressure all within policy caps", "Hard pass/fail gate on the counter-evidence half — gates L7's g9 guard."),
]
for _name, _rng, _formula_expr, _meaning in _L5A_BASE:
    add(_name, CAT_TRUST, "LIVE_FULL", "Derived variable",
        f"core/layers/layer_5.py::compute_L5 -> result[\"{_name}\"]", _rng,
        _formula_expr,
        ["L5 — Counter-Evidence & Trig Invariants"], [],
        "Hesperia-native `38_SPEC` L5 instrumentation — no Java prototype ancestor — "
        + theory_explainer(
            _meaning,
            "Hesperia L5 (38_SPEC / output_catalog §5)",
            reasoning="L5 counter-evidence field — pressure against the dominant read",
            application="[[L5 — Counter-Evidence & Trig Invariants]], L7",
        ),
        f"**HWIKI-CATALOG-L5 / HWIKI-PLAIN:** {_meaning} Source: `docs/foundations/output_catalog.md` §5, re-verified against `compute_L5` 2026-08-04.")

_L5B_TRIG = [
    ("DOT_SYMMETRY_RESIDUAL", "LIVE_FULL", "abs(dot(v,w) - dot(w,v))", "Self-test: dot product should be symmetric — near-zero residual confirms the implementation actually is."),
    ("DOT_SELF_NONNEG_RESIDUAL", "LIVE_FULL", "max(0, -dot(v,v))", "Self-test: a vector dotted with itself should never be negative."),
    ("NORM_CONSISTENCY_RESIDUAL", "LIVE_FULL", "abs(norm(v)**2 - dot(v,v))", "Self-test: squared norm should equal the vector dotted with itself."),
    ("COSI_CLAMP_VIOLATION_COUNT", "LIVE_FULL", "1 if raw cosine outside [-1,1] else 0", "Self-test: counts whether the raw (pre-clamp) cosine similarity ever left its valid range."),
    ("ANGLE_RANGE_VIOLATION_COUNT", "LIVE_FULL", "1 if arccos angle outside [0,pi] else 0", "Self-test: counts whether the derived angle ever left its valid range."),
    ("LAW_OF_COSINES_RESIDUAL", "PARTIAL", "hardcoded 0.0", "Reserved for a future non-deterministic-input mode — not a live computation today. The code sets this literal 0.0, explicitly flagged as reserved, not silently omitted."),
    ("SIN_COS_IDENTITY_RESIDUAL", "LIVE_FULL", "abs(sin(theta)**2 + cos(theta)**2 - 1)", "Self-test: the Pythagorean trig identity, checked against the actual computed angle."),
    ("ROTATION_NORM_PRESERVATION_RESIDUAL", "PARTIAL", "hardcoded 0.0", "Reserved placeholder — not live today, same status as LAW_OF_COSINES_RESIDUAL."),
    ("ORTHONORMALITY_RESIDUAL_FROBENIUS", "PARTIAL", "hardcoded 0.0", "Reserved placeholder — not live today."),
    ("TRIANGLE_INEQUALITY_VIOLATION_COUNT", "PARTIAL", "hardcoded 0", "Reserved placeholder — not live today."),
    ("METRIC_SYMMETRY_RESIDUAL", "PARTIAL", "hardcoded 0.0", "Reserved placeholder — not live today."),
    ("METRIC_IDENTITY_RESIDUAL", "PARTIAL", "hardcoded 0.0", "Reserved placeholder — not live today."),
]
for _name, _status, _formula_expr, _meaning in _L5B_TRIG:
    add(_name, CAT_TRUST, _status, "Derived variable (self-test)",
        f"core/layers/layer_5.py::compute_L5 -> result[\"{_name}\"]", "float/int, near-zero expected",
        _formula_expr,
        ["L5 — Counter-Evidence & Trig Invariants"], ["REALITY_GATE_TRIG"],
        "Hesperia-native `38_SPEC` L5 instrumentation — no Java prototype ancestor — "
        + theory_explainer(
            _meaning,
            "Hesperia L5 trig self-test (38_SPEC)",
            extent="partial" if "hardcoded" in _formula_expr else "full",
            reasoning="vector-space axiom self-test — not a content measurement",
            application="[[REALITY_GATE_TRIG]], L7 g8",
        ),
        f"**HWIKI-CATALOG-L5 / HWIKI-PLAIN:** {_meaning} Not a content measurement — a self-test that the vector-space math the rest of the engine relies on actually holds its own axioms. Source: `docs/foundations/output_catalog.md` §5.")

add("REALITY_GATE_TRIG", CAT_TRUST, "LIVE_FULL", "Derived variable",
    "core/layers/layer_5.py::compute_L5 -> result[\"REALITY_GATE_TRIG\"]", "bool",
    "AND of all 13 trig/metric-space residual checks within tolerance",
    ["DOT_SYMMETRY_RESIDUAL", "DOT_SELF_NONNEG_RESIDUAL", "NORM_CONSISTENCY_RESIDUAL"], [],
    "Hesperia-native `38_SPEC` L5 instrumentation — no Java prototype ancestor",
    "**HWIKI-CATALOG-L5:** The single hard gate summarizing all 13 trig self-tests (5 live + 6 reserved-0.0 + itself) — gates L7's g8 guard and L9's ACTION_ALLOW_HUMAN_SUMMARY. Source: `docs/foundations/output_catalog.md` §5.")

# ===== L7 — CONSISTENCY AND DECISION (HWIKI-CATALOG-L7, docs/foundations/output_catalog.md §7) =====
# Source-verified against core/layers/layer_7.py::compute_L7 2026-08-04. Two items
# (CONSIST_STABILITY_REGIME_VALID (L7), SYSTEM_CONFIDENCE_SCORE (L7)) already wikified — excluded.
# Naming follows the existing "(L7)" suffix convention those two items already established.
add("L7 — Consistency and Decision", CAT_STABILITY, "BEYOND", "Hub / concept",
    "core/layers/layer_7.py::compute_L7 (40_SPEC)", "25 base + up to 3 conditional",
    "Hub: ten pass/fail consistency gates (g1-g10) plus alignment/confidence aggregation — the layer where L1-L6's separate measurements collapse into one trust tier and one decision code.",
    ["L1 — Structural Activation Census", "L2 — Topology Traversal", "L3 — Baseline/Shadow Comparison", "L4 — Evidence Retrieval", "L5 — Counter-Evidence & Trig Invariants"], ["L8 — Unit Standardization"],
    "Hesperia-native `40_SPEC` L7 instrumentation — no Java prototype ancestor",
    "**HWIKI-CATALOG-L7:** Source: `docs/foundations/output_catalog.md` §7, re-verified against `compute_L7` 2026-08-04. `docs/specs/history/40_SPEC` recovery confirmed `OUTPUT_TRUST_TAG` is spec item 25, correcting an earlier miscounted '24 base' claim.")

_L7_GATES = [
    ("CONSIST_COVERAGE_MIN_GATE (L7, g1)", "bool", "COVERAGE_RATIO >= MIN_COVERAGE_RATIO", "First consistency gate — L1's coverage must clear a policy floor before anything else is trusted."),
    ("CONSIST_ATTRIBUTION_MASS_EQUALITY (L7, g2)", "bool", "L1 FAMILY_HIT_VECTOR_L1 ~= ATTRIBUTED_TOKENS", "Sanity check that L1's own two ways of counting attributed mass agree with each other."),
    ("CONSIST_TRAVERSAL_NONEMPTY_WHEN_ATTRIBUTED (L7, g3)", "bool", "traversal empty iff attribution empty", "Sanity check that L2's traversal and L1's attribution agree on whether there was anything to work with at all."),
    ("CONSIST_DOMINANT_FAMILY_IN_TRAVERSAL (L7, g4)", "bool", "L1 DOMINANT_FAMILY_ID in L2 VISITED_IDS", "Sanity check that the family L1 called dominant is actually one the L2 traversal reached — uses L2's VISITED_IDS handoff directly."),
    ("CONSIST_AREA_MAPPING (L7, g5)", "bool", "L1 DOMINANT_AREA_ID == DOMINANT_FAMILY_ID // FAMILIES_PER_AREA", "Sanity check that the dominant area was derived correctly from the dominant family, not independently computed and possibly inconsistent."),
    ("CONSIST_EVIDENCE_INTEGRITY_HARD (L7, g6)", "bool", "L4 INTEGRITY_CHECK_PASS_RATIO == 1.0", "Hard gate — unlike most others here this demands exact 1.0, not just 'within policy cap'."),
    ("CONSIST_SHADOW_DELTA_ONLY_IF_SHADOW (L7, g7)", "bool", "shadow delta is zero unless a shadow run happened", "Sanity check that L3's delta fields don't silently carry nonzero values when there was no actual shadow comparison to produce them."),
    ("CONSIST_TRIG_REQUIRED_FOR_ANGLE_METRICS (L7, g8)", "bool", "= L5 REALITY_GATE_TRIG", "Passthrough — L7's name for L5's trig self-test gate, kept alongside the other nine g-gates so all ten live in one namespace."),
    ("CONSIST_COUNTER_EVIDENCE_VALID (L7, g9)", "bool", "= L5 REALITY_GATE_COUNTER_EVIDENCE", "Passthrough — L7's name for L5's counter-evidence gate."),
    ("TRUST_TIER", "int [0,3]", "0 if g1 fails; 1 if g6 fails; 2 if g8 fails; else 3", "The first tier-defining escalation — how far down the gate chain the run got before something failed. Directly feeds SYSTEM_CONFIDENCE_SCORE as the (tier/3) factor."),
    ("MAX_ALLOWABLE_SHADOW_DEVIATION", "float", "echoed policy constant", "Not a measurement — the policy cap value itself, echoed into the output so a consumer can see what threshold SHADOW_WITHIN_LIMITS was checked against."),
    ("SHADOW_WITHIN_LIMITS", "bool", "= L3 SHADOW_ACCEPTABILITY_GATE", "Passthrough — L7's name for L3's shadow gate."),
    ("MAX_ALLOWABLE_CONTRADICTION", "float", "echoed policy constant", "Policy cap echo, paired with CONTRADICTION_WITHIN_LIMITS."),
    ("CONTRADICTION_WITHIN_LIMITS", "bool", "L5 CONTRADICTION_PRESSURE_SCORE <= policy cap", "Whether L5's contradiction pressure stayed under the configured ceiling."),
    ("MAX_AREA_LEAKAGE", "float", "echoed policy constant", "Policy cap echo, paired with AREA_LEAKAGE_WITHIN_LIMITS."),
    ("AREA_LEAKAGE_WITHIN_LIMITS", "bool", "L2 CROSS_AREA_RATIO <= policy cap", "Whether L2's cross-area traversal spillover stayed under the configured ceiling."),
    ("MAX_CHAOS_LEVEL", "float", "echoed policy constant (Lyapunov cap)", "Policy cap echo for the L6 Lyapunov stability estimate — no paired *_WITHIN_LIMITS field in this layer's own output, unlike the other policy-cap rows."),
    ("STRUCTURE_EVIDENCE_ALIGNMENT", "float [0,1]", "0.60*L4_support + 0.40*L2_geometric_stability", "How well the structural read (L2's geometry) and the evidence read (L4's support) agree with each other."),
    ("SHADOW_EVIDENCE_ALIGNMENT_DELTA", "float", "shadow support - baseline support", "How much the evidence-alignment picture changes between baseline and shadow runs."),
    ("SHADOW_JUSTIFICATION_SCORE", "float [0,1]", "nonzero only if shadow gate passed AND shadow improved support", "Whether running the shadow comparison at all was worthwhile — zero unless it both passed its own gate and actually made the evidence picture better."),
    ("CONTRADICTION_ADJUSTED_SUPPORT", "float [0,1]", "L4_support * (1 - L5_pressure)", "L4's evidence support discounted by however much L5 found contradicting it — feeds directly into SYSTEM_CONFIDENCE_SCORE."),
    ("DECISION_STATUS_CODE", "int", "0 pass; else 10/20/30/40/50/60/70 by which gate failed first; 75 reserved for profile-conformance failure", "The single number a consumer checks to know exactly which gate (if any) blocked this run — a full audit trail compressed to one int."),
    ("OUTPUT_TRUST_TAG", "string", "HIGH/MED/LOW from code+confidence thresholds; spec item 25", "The human-readable trust label — closes the `40_SPEC` recovery finding that this is spec item 25, not an unspecced code-only addition as an earlier pass of the catalog miscounted."),
]
for _name, _rng, _formula_expr, _meaning in _L7_GATES:
    add(_name, CAT_STABILITY, "LIVE_FULL", "Derived variable",
        f"core/layers/layer_7.py::compute_L7 -> out[...]", _rng,
        _formula_expr,
        ["L7 — Consistency and Decision"], [],
        "Hesperia-native `40_SPEC` L7 instrumentation — no Java prototype ancestor — "
        + theory_explainer(
            _meaning,
            "Hesperia L7 (40_SPEC / output_catalog §7)",
            reasoning="L7 consistency/decision field — collapses L1–L6 into trust tier and decision code",
            application="[[L7 — Consistency and Decision]], L8–L9",
        ),
        f"**HWIKI-CATALOG-L7 / HWIKI-PLAIN:** {_meaning} Source: `docs/foundations/output_catalog.md` §7, re-verified against `compute_L7` 2026-08-04.")

_L7_CONDITIONAL = [
    ("CONSIST_PROFILE_CONFORMANCE (L7)", "profile is active", "Only present when a structure profile is active — not in `40_SPEC`'s original 25, a later profile-mode addition."),
    ("PROFILE_CHECKSUM (L7)", "profile is active and supplies a checksum", "Same conditional family as CONSIST_PROFILE_CONFORMANCE (L7) — later addition, not in the original spec."),
    ("STABILITY_ANOMALY_SCORE (L7)", "run() receives a stability dict", "Only present when the `run()` wrapper (not `compute_L7` itself) receives a stability anomaly score — also demotes OUTPUT_TRUST_TAG to \"LOW_CONFIDENCE\" post-hoc when high enough. This demotion path lives in `run()`, not visible inside `compute_L7` itself — code-only, post-spec addition."),
]
for _name, _condition, _meaning in _L7_CONDITIONAL:
    add(_name, CAT_STABILITY, "PARTIAL", "Derived variable",
        "core/layers/layer_7.py -> run() wrapper (profile/stability-conditional)", "varies",
        "See notes — only computed under the stated condition, not part of compute_L7's guaranteed base output.",
        ["L7 — Consistency and Decision"], [],
        "Hesperia-native `40_SPEC` L7 instrumentation, code-only post-spec addition — no Java prototype ancestor — "
        + theory_explainer(
            _meaning,
            "Hesperia L7 post-spec conditional",
            extent="partial",
            reasoning=f"only under condition: {_condition}",
            application="[[L7 — Consistency and Decision]]",
        ),
        f"**HWIKI-CATALOG-L7 / HWIKI-PLAIN:** {_meaning} Condition: {_condition}. Source: `docs/foundations/output_catalog.md` §7.")

# ===== L8 — UNIT STANDARDIZATION (HWIKI-CATALOG-L8, docs/foundations/output_catalog.md §8) =====
# Source-verified against core/layers/layer_8.py::compute_L8 2026-08-04. Three items already
# wikified (SI_GLOBAL_STABILITY_PCT/U1000 (L8), SI_SYSTEM_CONFIDENCE_U1000 (L8)) — excluded.
add("L8 — Unit Standardization", CAT_STABILITY, "BEYOND", "Hub / concept",
    "core/layers/layer_8.py::compute_L8 (41_SPEC)", "30",
    "Hub: takes every L1-L7 raw ratio/score and rescales it into fixed, documented unit families (PCT, U1000) so L9 and downstream consumers never have to know each upstream layer's native scale.",
    ["L1 — Structural Activation Census", "L2 — Topology Traversal", "L3 — Baseline/Shadow Comparison", "L4 — Evidence Retrieval", "L5 — Counter-Evidence & Trig Invariants", "L7 — Consistency and Decision"], ["L9 — Pillars, Brand Labels, Action Triggers"],
    "Hesperia-native `41_SPEC` L8 instrumentation — no Java prototype ancestor",
    "**HWIKI-CATALOG-L8:** Source: `docs/foundations/output_catalog.md` §8, re-verified against `compute_L8` 2026-08-04. 5 policy/metadata constants (always identical text) + 22 SI_* metrics from `compute_L8` + 3 more (POLICY_MODE, INTERPRETATION_CONSTRAINTS, INTERPRETATION_SCOPE) always added by the `run()` wrapper regardless of whether a policy was supplied.")

_L8_POLICY_CONST = [
    ("UNIT_TYPE_ENUM (L8)", "Fixed reference string", '"COUNT,RATIO,PERCENT,U1000,RADIANS,SECONDS,BYTES,HASH,BOOLEAN,CODE"', "Enumerates every unit family this layer knows how to tag a value with — a fixed reference constant, not a measurement."),
    ("SCALE_POLICY_ENUM (L8)", "Fixed reference string", '"RAW,CLAMP_0_1,CLAMP_0_100,CLAMP_0_1000,ZSCORE,LOG10"', "Enumerates every rescaling policy this layer knows how to apply — fixed reference constant."),
    ("EPSILON_POLICY (L8)", "Fixed constant", "1e-12", "The floor epsilon this layer's rescaling math uses to avoid division-by-zero — distinct from the `eps=1e-9` used in L1's own internal formulas."),
    ("CLAMP_POLICY (L8)", "Fixed formula string", '"max(lo,min(hi,v))"', "Documents the exact clamp formula every SI_* bounded value was put through — a fixed reference constant, not itself a computation."),
    ("ROUNDING_POLICY (L8)", "Fixed string", '"DECIMALS_RATIO=6,DECIMALS_PCT=2,DECIMALS_U1000=0"', "Documents the rounding precision applied per unit family."),
]
for _name, _kind, _val, _meaning in _L8_POLICY_CONST:
    add(_name, CAT_STABILITY, "LIVE_FULL", "Parameter (constant)",
        "core/layers/layer_8.py::compute_L8 -> result[...]", _val,
        "Fixed reference constant, identical every run.",
        ["L8 — Unit Standardization"], [],
        "Hesperia-native `41_SPEC` L8 instrumentation — no Java prototype ancestor — "
        + theory_explainer(
            _meaning,
            "Hesperia L8 (41_SPEC / output_catalog §8)",
            reasoning="L8 unit-policy constant — documents how SI_* values are tagged and scaled",
            application="[[L8 — Unit Standardization]], L9",
        ),
        f"**HWIKI-CATALOG-L8 / HWIKI-PLAIN:** {_meaning} Source: `docs/foundations/output_catalog.md` §8.")

_L8_SI = [
    ("SI_TOTAL_TOKENS_COUNT (L8)", "int", "= L1 TOTAL_TOKENS", "Passthrough, tagged with the COUNT unit type — not itself rescaled, just re-labeled for consumers that read every field through the same unit-tagged interface."),
    ("SI_COVERAGE_PCT (L8)", "float [0,100]", "L1 COVERAGE_RATIO -> [0,100]", "L1's coverage ratio rescaled to a percent."),
    ("SI_COVERAGE_U1000 (L8)", "float [0,1000]", "L1 COVERAGE_RATIO -> [0,1000]", "Same value, U1000 scale — feeds L9's banding logic, which reads U1000 not PCT."),
    ("SI_DOMINANCE_PCT (L8)", "float [0,100]", "L1 DOMINANCE_RATIO -> [0,100]", "L1's dominance ratio rescaled to a percent."),
    ("SI_DOMINANCE_U1000 (L8)", "float [0,1000]", "L1 DOMINANCE_RATIO -> [0,1000]", "Same value, U1000 scale."),
    ("SI_ENTROPY_U1000 (L8)", "float [0,1000]", "L1 NORMALIZED_FAMILY_ENTROPY -> [0,1000]", "L1's normalized entropy rescaled to U1000."),
    ("SI_ENTROPY_PCT (L8)", "float [0,100]", "L1 NORMALIZED_FAMILY_ENTROPY -> [0,100]", "Same value, percent scale."),
    ("SI_GEOMETRIC_STABILITY_U1000 (L8)", "float [0,1000]", "L2 GEOMETRIC_STABILITY_INDEX -> [0,1000]", "L2's composite geometric-stability read, rescaled to U1000."),
    ("SI_GEOMETRIC_STABILITY_PCT (L8)", "float [0,100]", "L2 GEOMETRIC_STABILITY_INDEX -> [0,100]", "Same value, percent scale."),
    ("SI_AREA_LEAKAGE_PCT (L8)", "float [0,100]", "L2 CROSS_AREA_RATIO -> [0,100]", "L2's cross-area spillover, rescaled to a percent."),
    ("SI_AREA_LEAKAGE_U1000 (L8)", "float [0,1000]", "L2 CROSS_AREA_RATIO -> [0,1000]", "Same value, U1000 scale — L9 inverts this into AREA_CONTAINMENT_U1000 (leakage vs. containment are complementary framings of the same measurement)."),
    ("SI_SHADOW_DEVIATION_U1000 (L8)", "float [0,1000]", "L3 SHADOW_DEVIATION_SCORE -> [0,1000]", "L3's composite shadow-deviation score, rescaled to U1000."),
    ("SI_SHADOW_DEVIATION_PCT (L8)", "float [0,100]", "L3 SHADOW_DEVIATION_SCORE -> [0,100]", "Same value, percent scale."),
    ("SI_EVIDENCE_SUPPORT_U1000 (L8)", "float [0,1000]", "L4 EVIDENCE_SUPPORT_INDEX_BASELINE -> [0,1000]", "L4's evidence support index, rescaled to U1000 — the rescale-only hop in output_catalog.md's worked 'Trust' example chain."),
    ("SI_EVIDENCE_SUPPORT_PCT (L8)", "float [0,100]", "L4 EVIDENCE_SUPPORT_INDEX_BASELINE -> [0,100]", "Same value, percent scale."),
    ("SI_CONTRADICTION_PRESSURE_U1000 (L8)", "float [0,1000]", "L5 CONTRADICTION_PRESSURE_SCORE -> [0,1000]", "L5's contradiction pressure score, rescaled to U1000."),
    ("SI_CONTRADICTION_PRESSURE_PCT (L8)", "float [0,100]", "L5 CONTRADICTION_PRESSURE_SCORE -> [0,100]", "Same value, percent scale."),
    ("SI_TRIG_REALITY_FLAG (L8)", "bool", "= L5 REALITY_GATE_TRIG (passthrough)", "Not rescaled, just re-tagged with a BOOLEAN unit type for the same unified-interface reason as SI_TOTAL_TOKENS_COUNT."),
    ("SI_SYSTEM_CONFIDENCE_PCT (L8)", "float [0,100]", "L7 SYSTEM_CONFIDENCE_SCORE -> [0,100]", "Percent-scale sibling of the already-wikified SI_SYSTEM_CONFIDENCE_U1000 (L8) — same source value, feeds L9's confidence bands alongside the U1000 form."),
    ("POLICY_MODE (L8)", "string", 'default "STRUCTURE_PLUS_CONTEXT"', "Always present regardless of whether a policy dict was actually supplied to `run()` — falls back to this default string."),
    ("INTERPRETATION_CONSTRAINTS (L8)", "dict", "{allow_text, allow_context, allow_structure}", "Always present — the three-flag permission set L9/the LLM must respect for what kind of claim they're allowed to make."),
    ("INTERPRETATION_SCOPE (L8)", "string", '"structure_only" or "structure_and_context"', "The Pi gate limiting what L9 and the LLM substrate may claim — derived from INTERPRETATION_CONSTRAINTS, not independently set."),
]
for _name, _rng, _formula_expr, _meaning in _L8_SI:
    add(_name, CAT_STABILITY, "LIVE_FULL", "Derived variable",
        f"core/layers/layer_8.py::compute_L8 -> result[...]", _rng,
        _formula_expr,
        ["L8 — Unit Standardization"], [],
        "Hesperia-native `41_SPEC` L8 instrumentation — no Java prototype ancestor — "
        + theory_explainer(
            _meaning,
            "Hesperia L8 (41_SPEC / output_catalog §8)",
            reasoning="L8 SI_* rescale — fixed unit family so L9 never sees each layer's native scale",
            application="[[L8 — Unit Standardization]], L9 pillars/bands",
        ),
        f"**HWIKI-CATALOG-L8 / HWIKI-PLAIN:** {_meaning} Source: `docs/foundations/output_catalog.md` §8, re-verified against `compute_L8` 2026-08-04.")

# ===== L9 — PILLARS, BRAND LABELS, ACTION TRIGGERS — TERMINUS (HWIKI-CATALOG-L9, docs/foundations/output_catalog.md §9) =====
# Source-verified against core/layers/layer_9.py::compute_L9 2026-08-04. Every one of these 25 is
# user-facing by construction — no wiki duplicates found, clean batch.
add("L9 — Pillars, Brand Labels, Action Triggers", CAT_STABILITY, "BEYOND", "Hub / concept",
    "core/layers/layer_9.py::compute_L9 (42_SPEC)", "25 (spec-exact)",
    "Hub: the terminus of the L1-L9 pipeline — bands, directional reframes, six pillar scores, five brand words, and four action triggers, all derived from L8's rescaled SI_* values. Every field here is user-facing; there is no further internal-only tier above this layer.",
    ["L8 — Unit Standardization"], ["fpf_bridge"],
    "Hesperia-native `42_SPEC` L9 instrumentation — no Java prototype ancestor",
    "**HWIKI-CATALOG-L9:** Source: `docs/foundations/output_catalog.md` §9, re-verified against `compute_L9` 2026-08-04. `docs/specs/history/42_SPEC` recovery confirms all 25 spec-exact; item order here follows the spec, not the code's dict-literal order.")

_L9_BANDS = [
    ("BAND_0_CRITICAL (L9)", "bool", "SI_SYSTEM_CONFIDENCE_U1000 < 200"),
    ("BAND_1_POOR (L9)", "bool", "200 <= SI_SYSTEM_CONFIDENCE_U1000 < 400"),
    ("BAND_2_FAIR (L9)", "bool", "400 <= SI_SYSTEM_CONFIDENCE_U1000 < 600"),
    ("BAND_3_GOOD (L9)", "bool", "600 <= SI_SYSTEM_CONFIDENCE_U1000 < 800"),
    ("BAND_4_VERY_GOOD (L9)", "bool", "800 <= SI_SYSTEM_CONFIDENCE_U1000 < 950"),
    ("BAND_5_EXCELLENT (L9)", "bool", "SI_SYSTEM_CONFIDENCE_U1000 >= 950"),
]
for _name, _rng, _formula_expr in _L9_BANDS:
    add(_name, CAT_STABILITY, "LIVE_FULL", "Derived variable",
        "core/layers/layer_9.py::compute_L9 -> result[...]", _rng, _formula_expr,
        ["L9 — Pillars, Brand Labels, Action Triggers", "SI_SYSTEM_CONFIDENCE_U1000 (L8)"], [],
        "Hesperia-native `42_SPEC` L9 instrumentation — no Java prototype ancestor — "
        + theory_explainer(
            "One of six mutually-exclusive confidence bands on L8 SI_SYSTEM_CONFIDENCE_U1000 — exactly one True per run",
            "Hesperia L9 (42_SPEC / output_catalog §9)",
            reasoning="terminus confidence banding for human-facing labels and actions",
            application="[[L9 — Pillars, Brand Labels, Action Triggers]], brand words / actions",
        ),
        "**HWIKI-CATALOG-L9 / HWIKI-PLAIN:** One of six mutually-exclusive confidence bands on L8's SI_SYSTEM_CONFIDENCE_U1000 — exactly one is True per run. Source: `docs/foundations/output_catalog.md` §9.")

add("DIRECTIONALIZE_HIGH_IS_GOOD (L9)", CAT_STABILITY, "LIVE_FULL", "Parameter (constant)",
    "core/layers/layer_9.py::compute_L9 -> result[...]", '"clamp(u,0,1000)"',
    "Fixed formula string, not a value.",
    ["L9 — Pillars, Brand Labels, Action Triggers"], [],
    "Hesperia-native `42_SPEC` L9 instrumentation — no Java prototype ancestor — "
    + theory_explainer(
        "Documents the i18n/reporting convention for metrics where higher U1000 means better — a reference string, not a per-run computation",
        "Hesperia L9 (42_SPEC)",
        reasoning="shared directionalize convention for reporting",
        application="[[L9 — Pillars, Brand Labels, Action Triggers]]",
    ),
    "**HWIKI-CATALOG-L9 / HWIKI-PLAIN:** Documents the i18n/reporting convention for metrics where higher U1000 means better (most of them) — a reference string other layers/consumers can cite, not itself computed per-run. Source: `docs/foundations/output_catalog.md` §9.")
add("DIRECTIONALIZE_LOW_IS_GOOD (L9)", CAT_STABILITY, "LIVE_FULL", "Parameter (constant)",
    "core/layers/layer_9.py::compute_L9 -> result[...]", '"1000-clamp(u,0,1000)"',
    "Fixed formula string, not a value.",
    ["L9 — Pillars, Brand Labels, Action Triggers"], [],
    "Hesperia-native `42_SPEC` L9 instrumentation — no Java prototype ancestor — "
    + theory_explainer(
        "Counterpart convention for metrics where lower U1000 means better (leakage/pressure before containment/consistency reframes)",
        "Hesperia L9 (42_SPEC)",
        reasoning="shared directionalize convention for inverted 'bad-when-high' metrics",
        application="[[AREA_CONTAINMENT_U1000 (L9)]], [[CONSISTENCY_U1000 (L9)]]",
    ),
    "**HWIKI-CATALOG-L9 / HWIKI-PLAIN:** Counterpart to DIRECTIONALIZE_HIGH_IS_GOOD (L9) for metrics where lower U1000 means better — a reference string, not itself computed per-run. Source: `docs/foundations/output_catalog.md` §9.")

add("AREA_CONTAINMENT_U1000 (L9)", CAT_STABILITY, "LIVE_FULL", "Derived variable",
    "core/layers/layer_9.py::compute_L9 -> result[...]", "int [0,1000]",
    "1000 - L8 SI_AREA_LEAKAGE_U1000",
    ["SI_AREA_LEAKAGE_PCT (L8)"], ["PILLAR_GEOMETRY_U1000 (L9)"],
    "Hesperia-native `42_SPEC` L9 instrumentation — no Java prototype ancestor — "
    + theory_explainer(
        "Reframes L8 area leakage into containment (good when high) for geometry pillar scoring",
        "Hesperia L9 (42_SPEC item 9)",
        reasoning="directionalize leakage→containment so pillars stay 'higher is better'",
        application="[[PILLAR_GEOMETRY_U1000 (L9)]]",
    ),
    "**HWIKI-CATALOG-L9 / HWIKI-PLAIN:** Spec item 9 — reframes leakage into containment; feeds PILLAR_GEOMETRY_U1000. Source: `docs/foundations/output_catalog.md` §9.")
add("CONSISTENCY_U1000 (L9)", CAT_STABILITY, "LIVE_FULL", "Derived variable",
    "core/layers/layer_9.py::compute_L9 -> result[...]", "int [0,1000]",
    "1000 - L8 SI_CONTRADICTION_PRESSURE_U1000",
    ["SI_CONTRADICTION_PRESSURE_PCT (L8)"], ["PILLAR_CONSISTENCY_U1000 (L9)", "BRAND_WORD_CONTRADICTION (L9)"],
    "Hesperia-native `42_SPEC` L9 instrumentation — no Java prototype ancestor — "
    + theory_explainer(
        "Reframes contradiction pressure into consistency (good when high) for pillar and brand labels",
        "Hesperia L9 (42_SPEC item 10)",
        reasoning="directionalize pressure→consistency so pillars stay 'higher is better'",
        application="[[PILLAR_CONSISTENCY_U1000 (L9)]], [[BRAND_WORD_CONTRADICTION (L9)]]",
    ),
    "**HWIKI-CATALOG-L9 / HWIKI-PLAIN:** Item 10 — reframes contradiction pressure into consistency. Source: `docs/foundations/output_catalog.md` §9.")

_L9_PILLARS = [
    ("PILLAR_INPUT_QUALITY_U1000 (L9)", "round(0.60*SI_COVERAGE + 0.40*SI_DOMINANCE), clamped", "How much and how concentrated the raw input activation was — the earliest, most upstream pillar."),
    ("PILLAR_GEOMETRY_U1000 (L9)", "round(0.70*SI_GEOMETRIC_STABILITY + 0.30*AREA_CONTAINMENT_U1000), clamped", "How structurally settled and contained the L2 traversal was."),
    ("PILLAR_EVIDENCE_U1000 (L9)", "= L8 SI_EVIDENCE_SUPPORT_U1000 (direct passthrough)", "Not independently blended — a direct rename/passthrough of L8's evidence-support rescale, four layers downstream of L4's original EVIDENCE_SUPPORT_INDEX_BASELINE with zero re-blends (see output_catalog.md's worked 'Trust' example)."),
    ("PILLAR_CONSISTENCY_U1000 (L9)", "round(0.60*CONSISTENCY_U1000 + 0.40*(1000-SI_ENTROPY)), clamped", "Blends the contradiction-derived consistency reframe with low-entropy (focused, not diffuse) structure."),
    ("PILLAR_STABILITY_U1000 (L9)", "= L8 SI_GLOBAL_STABILITY_U1000 (direct passthrough)", "Direct rename/passthrough of L8's L6-Lyapunov-derived global stability rescale — no re-blend."),
    ("PILLAR_GOVERNANCE_U1000 (L9)", "1000 if DECISION_STATUS_CODE==0 else clamp(1000-10*code, 0, 1000)", "The one pillar keyed directly off L7's gate-chain outcome rather than an SI_* rescale — a clean pass scores 1000, each unit of failure code linearly costs 10 points."),
]
for _name, _formula_expr, _meaning in _L9_PILLARS:
    add(_name, CAT_STABILITY, "LIVE_FULL", "Derived variable",
        "core/layers/layer_9.py::compute_L9 -> result[...]", "int [0,1000]",
        _formula_expr,
        ["L9 — Pillars, Brand Labels, Action Triggers"], ["BRAND_WORD_GEOMETRY (L9)" if "GEOMETRY" in _name else "BRAND_WORD_TRUST (L9)"],
        "Hesperia-native `42_SPEC` L9 instrumentation — no Java prototype ancestor — "
        + theory_explainer(
            _meaning,
            "Hesperia L9 pillar (42_SPEC)",
            reasoning="mid-level aggregation between L8 SI_* rescales and L9 brand words",
            application="[[L9 — Pillars, Brand Labels, Action Triggers]]",
        ),
        f"**HWIKI-CATALOG-L9 / HWIKI-PLAIN:** {_meaning} One of six pillar scores. Source: `docs/foundations/output_catalog.md` §9.")

_L9_BRAND_WORDS = [
    ("BRAND_WORD_TRUST (L9)", '"BLOCKED" if code!=0 else "TRUSTED">=850 else "USABLE">=650 else "TENTATIVE">=450 else "FRAGILE"', "The single headline trust label — checks the gate-chain outcome first, then bands SI_SYSTEM_CONFIDENCE_U1000."),
    ("BRAND_WORD_EVIDENCE (L9)", '"SUPPORTED">=800 else "BACKED">=600 else "THIN">=400 else "UNSUPPORTED"', "Human-readable label on SI_EVIDENCE_SUPPORT_U1000."),
    ("BRAND_WORD_CONTRADICTION (L9)", '"CONSISTENT">=800 else "MIXED">=600 else "CONTESTED">=400 else "CONTRADICTED"', "Human-readable label on CONSISTENCY_U1000 (L9)."),
    ("BRAND_WORD_GEOMETRY (L9)", '"CONTAINED">=800 else "STABLE">=600 else "DIFFUSE">=400 else "CHAOTIC"', "Human-readable label on PILLAR_GEOMETRY_U1000 (L9)."),
    ("BRAND_WORD_SHADOW (L9)", '"OFF" if not shadow_enabled else "REJECTED" if gate failed else "JUSTIFIED" if justification>0 else "NEUTRAL"', "Stateful, four-way label — the only brand word whose first branch depends on whether a shadow run happened at all (L3 SHADOW_ENABLED), not just on a threshold."),
]
for _name, _formula_expr, _meaning in _L9_BRAND_WORDS:
    add(_name, CAT_STABILITY, "LIVE_FULL", "Derived variable",
        "core/layers/layer_9.py::compute_L9 -> result[...]", "string enum",
        _formula_expr,
        ["L9 — Pillars, Brand Labels, Action Triggers"], [],
        "Hesperia-native `42_SPEC` L9 instrumentation — no Java prototype ancestor — "
        + theory_explainer(
            _meaning,
            "Hesperia L9 brand word (42_SPEC)",
            reasoning="human-readable terminus label from U1000 / gate thresholds",
            application="[[L9 — Pillars, Brand Labels, Action Triggers]]",
        ),
        f"**HWIKI-CATALOG-L9 / HWIKI-PLAIN:** {_meaning} Source: `docs/foundations/output_catalog.md` §9, thresholds re-verified against `layer_9.py` 2026-08-04.")

_L9_ACTIONS = [
    ("ACTION_REQUIRE_MORE_INPUT (L9)", "SI_COVERAGE_U1000 < 500", "Fires when too little of the input actually got attributed to trust any read from it."),
    ("ACTION_REQUIRE_EVIDENCE_REBUILD (L9)", "L4 INTEGRITY_CHECK_PASS_RATIO < 1.0 or L4 RETRIEVAL_SHORTFALL_BASELINE > MAX_SHORTFALL", "Fires when the evidence retrieval itself was broken or incomplete — a rebuild-the-index signal, not a content judgment."),
    ("ACTION_REQUIRE_GOVERNANCE_REVIEW (L9)", "L7 DECISION_STATUS_CODE != 0 or SI_SYSTEM_CONFIDENCE_U1000 < 450", "Fires when either a hard gate failed or confidence is too low to auto-trust — routes to human review."),
    ("ACTION_ALLOW_HUMAN_SUMMARY (L9)", "code==0 and confidence>=650 and SI_TRIG_REALITY_FLAG", "The release gate — the single field that decides whether the pipeline is even allowed to hand a human-readable summary onward. Requires a clean gate chain, a Good-or-better confidence band, and passing trig self-tests, all three at once."),
]
for _name, _formula_expr, _meaning in _L9_ACTIONS:
    add(_name, CAT_STABILITY, "LIVE_FULL", "Derived variable",
        "core/layers/layer_9.py::compute_L9 -> result[...]", "bool",
        _formula_expr,
        ["L9 — Pillars, Brand Labels, Action Triggers"], [],
        "Hesperia-native `42_SPEC` L9 instrumentation — no Java prototype ancestor — "
        + theory_explainer(
            _meaning,
            "Hesperia L9 action trigger (42_SPEC)",
            reasoning="terminus action flag — what the product may ask a human or allow next",
            application="[[L9 — Pillars, Brand Labels, Action Triggers]]",
        ),
        f"**HWIKI-CATALOG-L9 / HWIKI-PLAIN:** {_meaning} Source: `docs/foundations/output_catalog.md` §9.")

# ===== FPF_BRIDGE + TRIZ EXPORTS (HWIKI-CATALOG-BRIDGE, docs/foundations/output_catalog.md §11-12) =====
# Source-verified against sphere/fpf_bridge/constants.py 2026-08-04. TRIZ contradiction-detection
# pipeline already wikified (classify_contradiction, contradiction_contract, detect_contradictions,
# run_triz_layer, TRIZ contradiction core hub) — these are the three separate NAMED EXPORT PRODUCTS
# (Policy Contradiction Detector / Innovation Radar / Narrative Propagation Monitor) the Coverage-Ledger
# flagged as "novelty/topology/commercial modules still open beyond Louvain".
add("fpf_bridge structural states", CAT_TRUST, "LIVE_FULL", "Hub / concept",
    "sphere/fpf_bridge/constants.py", "5 states",
    "The state machine the LLM actually sees — bridge_to_llm_prompt()'s envelope is a projection (one active state + legal next transitions + evidence requirements + pre-evaluated guard verdicts), never L1-L9's ~190 raw variables directly.",
    ["L9 — Pillars, Brand Labels, Action Triggers"], [],
    "Hesperia-native fpf_bridge design — no Java prototype ancestor",
    "**HWIKI-CATALOG-BRIDGE:** Source: `docs/foundations/output_catalog.md` §12, re-verified against `sphere/fpf_bridge/constants.py` 2026-08-04. Evidence surface (as of `fpf_bridge_v7_2`, flag-gated off by default) can additionally join L5 contradiction_pressure/counter_evidence_gate, L7 trust_tier/system_confidence/decision_status, L4 evidence_support_baseline, KME's 6 primitives + kme_ksi, and TRIZ's triz_contradiction_* (explicitly namespaced apart from contradiction_pressure — two independently-computed mechanisms, never averaged) — gated behind `HESPERIA_FPF_EVIDENCE_EXPANSION`/`HESPERIA_FPF_CONTRADICTION_GATE`/`HESPERIA_FPF_KME_EVIDENCE`. None of this changes the projection discipline: still a menu of FGR-scored evidence and legal transitions, never the raw dict.")

_FPF_STATES = [
    ("STATE_FOCUSED_DOMINANT", '"focused_dominant"', "normal", "One family/area clearly dominates the activation — the calmest, most legible read."),
    ("STATE_DISTRIBUTED_BALANCED", '"distributed_balanced"', "low", "Activation spread fairly evenly across multiple families/areas without any one dominating — read as balanced, not alarming."),
    ("STATE_UNSTABLE_TRANSITION", '"unstable_transition"', "high", "The structural read is mid-shift between states — highest risk tier, since a snapshot in transition is the least trustworthy to narrate confidently."),
    ("STATE_TENSION_ELEVATED", '"tension_elevated"', "high", "Contradiction/tension signals are high enough to flag — same risk tier as UNSTABLE_TRANSITION but a distinct cause (opposition, not instability)."),
    ("STATE_DIFFUSE_SPREAD", '"diffuse_spread"', "normal", "Activation is spread very thin across many families — different from DISTRIBUTED_BALANCED in degree, but not flagged as risky on its own."),
]
for _name, _val, _risk, _meaning in _FPF_STATES:
    add(_name, CAT_TRUST, "LIVE_FULL", "Parameter (constant)",
        "sphere/fpf_bridge/constants.py", _val,
        f"Risk level: {_risk}",
        ["fpf_bridge structural states"], [],
        "Hesperia-native fpf_bridge design — no Java prototype ancestor — "
        + theory_explainer(
            _meaning,
            "Hesperia fpf_bridge (output_catalog §12)",
            reasoning="one of five structural states the LLM actually sees — not the raw L1–L9 dict",
            application="[[fpf_bridge structural states]]",
        ),
        f"**HWIKI-CATALOG-BRIDGE / HWIKI-PLAIN:** {_meaning} One of exactly 5 structural states in `ALL_STATES`. Source: `docs/foundations/output_catalog.md` §12.")

add("TRIZ decision-intelligence exports", CAT_CD, "LIVE_FULL", "Hub / concept",
    "hesperia/extensions/triz/ (corners/triz_extension.md)", "3 export products",
    "Three named, shaped export products the TRIZ extension produces — read-only against everything in L1-L9/KME, not part of either HTTP contract (/analyze or /product/interpret).",
    ["TRIZ contradiction core hub", "Louvain communities (seed 42)"], [],
    "Hesperia-native TRIZ extension design — no Java prototype ancestor",
    "**HWIKI-CATALOG-BRIDGE:** Distinct from the already-wikified contradiction-*detection* pipeline (classify_contradiction, contradiction_contract, detect_contradictions, run_triz_layer) — these are the shaped *export products* built on top of it. Closes the Coverage-Ledger's 'novelty/topology/commercial modules still open beyond Louvain' gap. Source: `docs/foundations/output_catalog.md` §11.")

add("Policy Contradiction Detector (TRIZ export)", CAT_CD, "LIVE_FULL", "Formula / function",
    "hesperia/extensions/triz/ (corners/triz_extension.md)", "per-item export",
    "Per contradicting item: contradiction_score, contradiction_density, area_id, family_ids, triz_principle (segmentation/counterbalance/parameter_change/dynamic_adaptation).",
    ["TRIZ decision-intelligence exports"], [],
    "Hesperia-native TRIZ extension design, TRIZ inventive-principle naming (Altshuller) applied to Hesperia's own contradiction detection — no Java prototype ancestor",
    "**HWIKI-CATALOG-BRIDGE:** The `triz_principle` field borrows Altshuller's TRIZ inventive-principle vocabulary (segmentation, counterbalance, parameter_change, dynamic_adaptation) to label *how* a detected contradiction could structurally resolve, not just that one exists. Source: `docs/foundations/output_catalog.md` §11.")

add("Innovation Radar (TRIZ export)", CAT_CD, "LIVE_FULL", "Formula / function",
    "hesperia/extensions/triz/ (corners/triz_extension.md)", "per-cluster + aggregate export",
    "Per cluster: innovation_score, rarity, contradiction_density, propagation_reach. Aggregate: cluster_count, max_innovation_score, mean_innovation_score.",
    ["TRIZ decision-intelligence exports", "Louvain communities (seed 42)"], [],
    "Hesperia-native TRIZ extension design — no Java prototype ancestor",
    "**HWIKI-CATALOG-BRIDGE:** Built on the Louvain clustering (seed 42, reproducible run-to-run) — scores each innovation cluster on rarity and reach, not just size. Source: `docs/foundations/output_catalog.md` §11.")

add("Narrative Propagation Monitor (TRIZ export)", CAT_CD, "LIVE_FULL", "Formula / function",
    "hesperia/extensions/triz/ (corners/triz_extension.md)", "per-narrative + aggregate export",
    "Per narrative: penetration, velocity, stability. Aggregate versions of the same three.",
    ["TRIZ decision-intelligence exports"], [],
    "Hesperia-native TRIZ extension design — no Java prototype ancestor",
    "**HWIKI-CATALOG-BRIDGE:** Tracks how a narrative thread spreads (penetration), how fast (velocity), and how settled it is (stability) — the one TRIZ export explicitly about change over time/turns rather than a single-run snapshot. Source: `docs/foundations/output_catalog.md` §11.")

add("energy_conservation_tolerance", CAT_COREMATH, "LIVE_FULL", "Parameter (constant)",
    "core/math/core_math.py -> DEFAULT_CONFIG[\"energy_conservation_tolerance\"]; check_conservation_pre_decay", "1e-6 (must be < 1e-3)",
    "Tolerance the pre-decay energy-conservation check allows before rejecting a step as physically invalid.",
    [], ["check_conservation_pre_decay"],
    "Hesperia-native Core Math Contract constant — no Java prototype ancestor",
    "**HWIKI-CATALOG-CROSSCHECK (2026-08-04):** Last genuine gap found in a full parameter_catalog.md-vs-wiki cross-check after the HWIKI-CATALOG wave — every other §3/§4 constant (k_amb, tau_core, k_thin, k_disp, k_guard, k_shadow, delta_gap, max_shadow_hops, w_decay/w_guard_obs/w_shadow_obs, severe_curvature_threshold, severe_jump_rate_threshold) turned out already covered inside the P_amb/P_disp/P_guard/P_shadow/P_thin penalty pages or the paired curvature/jump_rate threshold pages, just not under their own bare name. This one genuinely had no page.")

# ===== L6 GROUP-IV STUBS — CLOSES THE COVERAGE-LEDGER'S NAMED NEXT-WAVE CANDIDATE =====
# 7 remaining no-perturbation scaffold constants, same "documented stub, not an oversight" status
# as the 8 L6 items already wikified (HWIKI-L6-01) — matching that entry's exact style/convention.
_L6_GROUP_IV = [
    ("HIT_VECTOR_RANK (L6)", "1 (no-perturbation stub)", "core/layers/layer_6.py:50,89",
     "HIT_VECTOR_RANK — rank of the family hit vector (stub 1, a rank-1/degenerate placeholder without perturbation data).",
     [], ["PRINCIPAL_COMPONENT_ENERGY_RATIO (L6)"]),
    ("PRINCIPAL_COMPONENT_ENERGY_RATIO (L6)", "1.0 (no-perturbation stub)", "core/layers/layer_6.py:51,90",
     "PRINCIPAL_COMPONENT_ENERGY_RATIO — fraction of hit-vector energy in the top principal component (stub 1.0, i.e. fully concentrated, without real PCA).",
     ["HIT_VECTOR_RANK (L6)"], []),
    ("ESCAPE_ENERGY_THRESHOLD (L6)", "1.0 (no-perturbation stub)", "core/layers/layer_6.py:70,98",
     "ESCAPE_ENERGY_THRESHOLD — energy needed to leave the current structural basin (stub 1.0, i.e. maximally sticky, without a real potential-field model).",
     [], ["FORCE_ANALOG_MAGNITUDE (L6)"]),
    ("FORCE_ANALOG_MAGNITUDE (L6)", "0.0 (no-perturbation stub)", "core/layers/layer_6.py:71,99",
     "FORCE_ANALOG_MAGNITUDE — force-like quantity analog from the potential-field scaffold (stub 0.0, i.e. no net force, without real dynamics).",
     ["ESCAPE_ENERGY_THRESHOLD (L6)"], []),
    ("MONOTONICITY_CHECK (L6)", "True (no-perturbation stub)", "core/layers/layer_6.py:72,100",
     "MONOTONICITY_CHECK — whether mass decay across BFS depth is monotonic (stub True, vacuously, without a real multi-sample trajectory to check).",
     [], ["FIXED_POINT_DETECTION (L6)"]),
    ("FIXED_POINT_DETECTION (L6)", "True (no-perturbation stub)", "core/layers/layer_6.py:73,101",
     "FIXED_POINT_DETECTION — whether the structural read has settled into a fixed point (stub True, vacuously, without a real iterative dynamical model).",
     ["MONOTONICITY_CHECK (L6)"], ["CYCLE_DETECTION_FUNCTIONAL (L6)"]),
    ("CYCLE_DETECTION_FUNCTIONAL (L6)", "False (no-perturbation stub)", "core/layers/layer_6.py:74,102",
     "CYCLE_DETECTION_FUNCTIONAL — whether a dynamical cycle was detected across turns (stub False, vacuously, without real turn-over-turn state to cycle-check).",
     ["FIXED_POINT_DETECTION (L6)"], []),
]
for _name, _val, _module, _formula, _pf, _nb in _L6_GROUP_IV:
    add(_name, CAT_STABILITY, "LIVE_FULL", "Layer variable",
        _module, _val, _formula, _pf, _nb, "39_SPEC Layer-6",
        "**HWIKI-CATALOG-L6-GROUP-IV (2026-08-04):** Closes the Coverage-Ledger's named next-wave candidate — Group-IV scaffold constant, same status as the other 21 L6 stubs (`docs/foundations/output_catalog.md` §6: \"documented no-perturbation identity constants... a named scaffold reserved for a future perturbation-analysis pass — not an oversight\"). Verified against `layer_6.py` directly.")

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
# Rendering + HWIKI-WIRE graph passes
# ---------------------------------------------------------------------------
NAME_TO_SLUG = {}
INBOUND = {}

def refresh_name_index():
    global NAME_TO_SLUG
    NAME_TO_SLUG = {it["name"]: slug(it["name"]) for it in ITEMS}

def wire_bidirectional():
    """If A.produced_from contains B, ensure B.needed_by contains A."""
    by_name = {it["name"]: it for it in ITEMS}
    added = 0
    for it in ITEMS:
        for p in list(it.get("produced_from") or []):
            parent = by_name.get(p)
            if not parent:
                continue
            nb = parent.setdefault("needed_by", [])
            if it["name"] not in nb:
                nb.append(it["name"])
                added += 1
    return added

def wire_orphans_and_successors():
    """Attach orphan I/O pages to category anchors; wire known DEAD→LIVE successors."""
    by_name = {it["name"]: it for it in ITEMS}
    category_anchor = {
        CAT_GEOMETRY: "Icosahedral Surface Graph",
        CAT_COREMATH: "alpha (fusion weight)",
        CAT_TENSION: "compute_tension",
        CAT_PROP: "Transition matrix (W)",
        CAT_THRESH: "dominant_area_share_threshold",
        CAT_GRAPH: "L1 — Structural Activation Census",
        CAT_ENTROPY: "compute_entropy (Shannon)",
        CAT_STABILITY: "L7 — Consistency and Decision",
        CAT_SIM: "cosine_similarity",
        CAT_TRUST: "L4 — Evidence Retrieval",
        CAT_CD: "LIVE_SUCCESSOR (status term)",
        CAT_DEAD: "KL divergence",
    }
    # Verify anchors exist; drop missing
    category_anchor = {k: v for k, v in category_anchor.items() if v in by_name}
    successors = {
        "KL divergence": ["compute_entropy (Shannon)", "eta (centroid threshold)", "E_cap"],
        "DFT Ring Smoothness": ["Icosahedral Surface Graph", "compute_entropy (Shannon)"],
        "saturation (Java, 23_PROTOTYPE)": ["apply_saturation"],
        "X_A / X_F alignment (Java)": ["dominant_area_share_threshold", "detect_dominant_area / detect_dominant_family"],
        "ALPHA/BETA/GAMMA/DELTA integrity quartet (Java)": ["metric_governance"],
        "evidenceQuality / provenanceWeight (Java)": ["FGR (Formality/Ground/Reliability)"],
        "cumulativeDrift / turnCoherence": ["cosine_similarity", "Mixing Diagnostics"],
        "K(R) / L(R) / fragIndex (Java)": ["largest_component_size", "Circuit rank (LOOP_COUNT/LOOP_DENSITY)"],
        "area_entropy (tool-local)": ["compute_entropy (Shannon)"],
    }
    attached = 0
    for it in ITEMS:
        pf = it.setdefault("produced_from", [])
        nb = it.setdefault("needed_by", [])
        # successors
        for live in successors.get(it["name"], []):
            if live in by_name and live not in nb:
                nb.append(live)
                attached += 1
            # reverse: live receives this dead/partial as origin context
            if live in by_name:
                lpf = by_name[live].setdefault("produced_from", [])
                # don't claim dead as input — mention via needed_by only on dead side
        # orphans: no named wiki edges at all
        named_pf = [x for x in pf if x in by_name]
        named_nb = [x for x in nb if x in by_name]
        if named_pf or named_nb:
            continue
        anchor = category_anchor.get(it["category"])
        if not anchor or anchor == it["name"]:
            continue
        pf.append(anchor)
        anb = by_name[anchor].setdefault("needed_by", [])
        if it["name"] not in anb:
            anb.append(it["name"])
        attached += 1
        notes = it.get("notes") or ""
        tag = "**HWIKI-WIRE:** attached to category anchor"
        if tag not in notes:
            it["notes"] = f"{tag} [[{anchor}]]. {notes}".strip()
    return attached

def _protect_spans(text):
    """Stash [[wikilinks]] and `code` so autolink cannot nest inside them."""
    protected = []
    def stash(m):
        protected.append(m.group(0))
        return f"\x00P{len(protected)-1}\x00"
    text = re.sub(r"\[\[[^\]]+\]\]", stash, text)
    text = re.sub(r"`[^`]+`", stash, text)
    return text, protected

def _restore_spans(text, protected):
    for i, chunk in enumerate(protected):
        text = text.replace(f"\x00P{i}\x00", chunk)
    return text

def autolink_known_names():
    """Wrap first exact page-name hit in formula/origin/notes with [[name]] (longest-first)."""
    names = sorted(NAME_TO_SLUG.keys(), key=len, reverse=True)
    # Skip very short / ambiguous tokens
    names = [n for n in names if len(n) >= 4]
    hits = 0
    for it in ITEMS:
        self_name = it["name"]
        for field in ("formula", "origin", "notes"):
            text = it.get(field) or ""
            if not text:
                continue
            work, protected = _protect_spans(text)
            changed = False
            for name in names:
                if name == self_name:
                    continue
                if name not in work:
                    continue
                pat = re.escape(name)
                new_work, nsub = re.subn(
                    rf"(?<![A-Za-z0-9_\x00]){pat}(?![A-Za-z0-9_\x00\]])",
                    f"[[{name}]]",
                    work,
                    count=1,
                )
                if nsub:
                    work = new_work
                    hits += 1
                    changed = True
                    break  # one new link per field per page — keep readable
            if changed:
                it[field] = _restore_spans(work, protected)
    return hits

def rebuild_inbound():
    global INBOUND
    INBOUND = {it["name"]: [] for it in ITEMS}
    for it in ITEMS:
        for p in it.get("produced_from") or []:
            if p in INBOUND:
                INBOUND[p].append(it["name"])
        for n in it.get("needed_by") or []:
            if n in INBOUND:
                INBOUND[n].append(it["name"])

def see_also_names(it, limit=12):
    related = []
    seen = {it["name"]}
    for bucket in (
        list(it.get("produced_from") or []),
        list(it.get("needed_by") or []),
        list(INBOUND.get(it["name"]) or []),
    ):
        for name in bucket:
            if name in NAME_TO_SLUG and name not in seen:
                related.append(name)
                seen.add(name)
            if len(related) >= limit:
                return related
    # same-category peers that share a produced_from hub
    my_hubs = [p for p in (it.get("produced_from") or []) if p in NAME_TO_SLUG]
    if my_hubs:
        for other in ITEMS:
            if other["name"] in seen or other["category"] != it["category"]:
                continue
            if any(h in (other.get("produced_from") or []) for h in my_hubs):
                related.append(other["name"])
                seen.add(other["name"])
                if len(related) >= limit:
                    break
    return related

def render_wire_map():
    """Generated navigation spine for HWIKI-WIRE."""
    hubs = [it for it in ITEMS if "Hub" in (it.get("kind") or "") or it["name"].startswith("L") and "—" in it["name"]]
    hubs = sorted(hubs, key=lambda it: (-len(it.get("needed_by") or []), it["name"].lower()))
    orphan = []
    for it in ITEMS:
        pf = [x for x in (it.get("produced_from") or []) if x in NAME_TO_SLUG]
        nb = [x for x in (it.get("needed_by") or []) if x in NAME_TO_SLUG]
        if not pf and not nb:
            orphan.append(it["name"])
    lines = [
        "# Wiki Wire Map\n",
        "[← wiki home](../index.md) · template [TEMPLATES-WIKI-WIRE.md](../TEMPLATES-WIKI-WIRE.md)\n",
        "Generated navigation spine: hub membership (`needed_by` after bidirectional wire), orphans, and how to follow links.\n",
        "## How to read a page\n",
        "1. **In plain words** / **Definition** — Receives → Does → Outputs → Exists for  ",
        "2. **Produced from / Needed by** — formal graph edges  ",
        "3. **See also** — parents, children, inbound, same-hub peers  ",
        "4. Inline `[[wikilinks]]` in formula / origin / notes\n",
        f"## Hubs ({len(hubs)})\n",
        "| Hub | Members (needed_by) | Status |",
        "|---|---:|---|",
    ]
    for it in hubs:
        n = len([x for x in (it.get("needed_by") or []) if x in NAME_TO_SLUG])
        lines.append(f"| [{it['name']}]({slug(it['name'])}.md) | {n} | {it['status']} |")
    lines.append(f"\n## Orphans (no named wiki I/O edges)\n")
    if not orphan:
        lines.append("*None — every page has at least one named produced_from or needed_by edge.*\n")
    else:
        lines.append(f"{len(orphan)} pages still lack named edges:\n")
        for name in sorted(orphan, key=str.lower):
            lines.append(f"- [{name}]({slug(name)}.md)")
        lines.append("")
    lines.append("---\n[← wiki home](../index.md)\n")
    return "\n".join(lines)

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
    plain = extract_plain_lang(s.get("origin"), s.get("notes"))
    exists_for = extract_te_field(s.get("origin") or "", "reasoning") or plain
    lines.append("## In plain words\n")
    if plain:
        plain_out = linkify_inline(plain)
        if not plain_out.endswith((".", "!", "?")):
            plain_out += "."
        lines.append(f"{plain_out}\n")
    else:
        lines.append("*(plain-language definition pending — HWIKI-PLAIN wave; formula and I/O below still authoritative)*\n")
    lines.append("## Definition\n")
    if s["produced_from"]:
        recv = ", ".join(link_or_text(p) for p in s["produced_from"])
    else:
        recv = "*none declared (constant, hub, or external)*"
    if s["needed_by"]:
        out_cons = ", ".join(link_or_text(n) for n in s["needed_by"])
    else:
        out_cons = "*no named wiki consumer yet*"
    lines.append(f"- **Receives:** {recv}")
    lines.append(f"- **Does:** {linkify_inline(s['formula'])}")
    lines.append(f"- **Outputs:** `{s['value']}` → {out_cons}")
    lines.append(f"- **Exists for:** {linkify_inline(exists_for) if exists_for else '*purpose pending (HWIKI-PLAIN)*'}\n")
    lines.append("## Yields (formula)\n")
    lines.append(f"{linkify_inline(s['formula'])}\n")
    if s["produced_from"]:
        lines.append("## Produced from (inputs)\n")
        for p in s["produced_from"]:
            lines.append(f"- {link_or_text(p)}")
        lines.append("")
    if s["needed_by"]:
        lines.append("## Needed by (consumers)\n")
        # Cap huge hub fan-out for readability; full list still in Wire Map
        consumers = s["needed_by"]
        show = consumers
        if len(consumers) > 40:
            show = consumers[:40]
        for n in show:
            lines.append(f"- {link_or_text(n)}")
        if len(consumers) > 40:
            lines.append(f"- *… +{len(consumers) - 40} more — see [Wiki Wire Map](Wiki-Wire-Map.md)*")
        lines.append("")
    related = see_also_names(s)
    if related:
        lines.append("## See also\n")
        for name in related:
            lines.append(f"- {link_or_text(name)}")
        lines.append("")
    lines.append("## Origin\n")
    lines.append(f"{linkify_inline(s['origin'])}\n")
    if s["notes"]:
        lines.append("## Notes\n")
        lines.append(f"{linkify_inline(s['notes'])}\n")
    lines.append("---")
    lines.append(
        "[← back to category](../categories/%s.md) · [wiki home](../index.md) · [Wire Map](Wiki-Wire-Map.md)"
        % slug(s["category"])
    )
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
    lines.append("Bottom-up, wikipedia-style register of every math variable/parameter this research thread has verified in `/data/hesperia/hesperia` — LIVE, PARTIAL, and DEAD/proposed-but-never-built alike. Each page: **In plain words**, **Definition** (Receives / Does / Outputs / Exists for), **See also**, **status, type, module, value, formula, inputs, consumers, origin, notes** — interlinked. Plain-language: [TEMPLATES-PLAIN-DEFINITION.md](TEMPLATES-PLAIN-DEFINITION.md) (HWIKI-PLAIN). Wire: [TEMPLATES-WIKI-WIRE.md](TEMPLATES-WIKI-WIRE.md) · **[Wiki Wire Map](pages/Wiki-Wire-Map.md)**.\n")
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
    lines.append("- **L1–L9 pipeline layer variables** (`34_SPEC`…`42_SPEC`) — **HWIKI-CATALOG wave, 2026-08-04: full census landed, including L6.** L1 through L9 all wikified (L1 hub [L1 — Structural Activation Census](pages/%s.md), L2–L9 hubs alongside), and L6's Group-IV stubs (HIT_VECTOR_RANK, PRINCIPAL_COMPONENT_ENERGY_RATIO, ESCAPE_ENERGY_THRESHOLD, FORCE_ANALOG_MAGNITUDE, MONOTONICITY_CHECK, FIXED_POINT_DETECTION, CYCLE_DETECTION_FUNCTIONAL) closed the same day — all 25 L6 keys now wikified, %d L6-related pages total. **Correction:** the pipeline terminates at L9 (`docs/foundations/output_catalog.md` calls it \"the terminus\" explicitly) — there is no L10/L11; the old \"L1–L11\" phrasing in this ledger was stale/aspirational, not a real gap. See [GRACE-TRIAGE-HESPERIA-WIKI-CATALOG-ABSORB-2026-08-04.md](../../../operational/assignments/GRACE-TRIAGE-HESPERIA-WIKI-CATALOG-ABSORB-2026-08-04.md) for the closure record." % (slug("L1 — Structural Activation Census"), len(l6)))
    lines.append("- **KME derived metrics** — **35 derived + hub wikified** (%d derived pages + [KME Primitives and Derived Metrics](pages/%s.md)). **HWIKI-KME-03:** plain-lang Theory Explainer notes on each derived page." % (len(kme_derived), slug("KME Primitives and Derived Metrics")))
    lines.append("- **TRIZ extension internals** (`hesperia/extensions/triz/`, 30+ modules) — **contradiction core hub landed** (HWIKI-TRIZ-02); **the three named export products landed 2026-08-04** (HWIKI-CATALOG-BRIDGE: [Policy Contradiction Detector](pages/%s.md), [Innovation Radar](pages/%s.md), [Narrative Propagation Monitor](pages/%s.md)). Remaining: the internal implementation modules beneath these exports (30+ files) are not individually wikified — only their shaped output products are." % (slug("Policy Contradiction Detector (TRIZ export)"), slug("Innovation Radar (TRIZ export)"), slug("Narrative Propagation Monitor (TRIZ export)")))
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
    lines.append("\n## Plain-language definition wave (HWIKI-PLAIN) — opened 2026-08-04\n")
    lines.append("**Mandate:** every parameter/term page answers **Receives / Does / Outputs / Exists for** in ordinary words **and** keeps the formula. Template: [TEMPLATES-PLAIN-DEFINITION.md](TEMPLATES-PLAIN-DEFINITION.md). Live: [http://wiki.hesperia.local/](http://wiki.hesperia.local/). Prod-of-record mirror: `Consolidare-Continuum/hesperia` → `docs/brain-export/colombo/hesperia-wiki/`.\n")
    n_plain = sum(1 for it in ITEMS if "plain_lang" in ((it.get("origin") or "") + (it.get("notes") or "")))
    lines.append(f"- **Batch A landed:** page renderer always emits **In plain words** + **Definition**; L1–L9 catalog + L9 terminus + fpf_bridge states promote `_meaning` → Theory Explainer `plain_lang`.")
    lines.append(f"- **Batch B landed (2026-08-04):** `backfill_plain_lang()` fills remaining LIVE/PARTIAL/BEYOND/DEAD rows from existing formula+notes (no invented science).")
    lines.append(f"- **Batch C landed (2026-08-04):** hand-polish for algebra-shaped rows (KME derived sentences + curated core/L6/SI/ontology plains). Coverage **{n_plain}/{len(ITEMS)}** with `plain_lang`.")
    orphan_n = sum(
        1 for it in ITEMS
        if not any(x in NAME_TO_SLUG for x in (it.get("produced_from") or []))
        and not any(x in NAME_TO_SLUG for x in (it.get("needed_by") or []))
    )
    lines.append(f"- **HWIKI-WIRE landed (2026-08-04):** bidirectional hub↔member edges, orphan→category anchors, DEAD→LIVE successors, autolink of known names, **See also** on every page, [Wiki Wire Map](pages/Wiki-Wire-Map.md). Orphans remaining: **{orphan_n}**.")
    lines.append("- **Still open:** Felix export/promote to `Consolidare-Continuum/hesperia`; Abelard CHROMA-1 `hesperia_wiki` re-ingest.\n")
    lines.append("\n## Cheap, concrete next-wave candidates\n")
    lines.append("- **Still open:** Add `compute_dominant_family_share` as a real page once/if built (mirrors [dominant_area_share_threshold](pages/%s.md)) — see [X_A / X_F alignment (Java)](pages/%s.md). Re-checked 2026-08-04: still doesn't exist in source." % (slug("dominant_area_share_threshold"), slug("X_A / X_F alignment (Java)")))
    lines.append("- **DONE 2026-08-04:** ~~Finish remaining L6 variables~~ — all 25 L6 keys now wikified (Group-IV stubs HIT_VECTOR_RANK/PRINCIPAL_COMPONENT_ENERGY_RATIO/ESCAPE_ENERGY_THRESHOLD/FORCE_ANALOG_MAGNITUDE/MONOTONICITY_CHECK/FIXED_POINT_DETECTION/CYCLE_DETECTION_FUNCTIONAL landed HWIKI-CATALOG-L6-GROUP-IV). ~~then L7/L8 consumers of GLOBAL_STABILITY_SCORE~~ — subsumed by the full L7/L8/L9 HWIKI-CATALOG batches.")
    lines.append("- **DONE 2026-08-04, re-verified not just assumed:** ~~Wikify CAT-01 delta list~~ — the CAT-01 delta doc itself (`COLOMBO-HWIKI-CAT-01-PARAMETER-CATALOG-DELTA-2026-07-23.md`, linked above) doesn't exist on disk, so checked source directly: diagnostic `ultra_sparse_coverage_threshold` already has its own page, all 4 FGR numeric-table constants (`DOMINANT_SHARE_HIGH`, `ENTROPY_DROP_SIGNIFICANT`, `STABILITY_CURRENT_THRESHOLD`, `STABILITY_STALE_THRESHOLD`) already wikified. Field Dynamics extension constants remain a deliberate scope exclusion (no consumer path — `EXTENSION_STATUS.yaml` classifies it `internal`), not an oversight.")
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
    filled = backfill_plain_lang()
    polished = polish_plain_lang()
    refresh_name_index()
    bi = wire_bidirectional()
    attached = wire_orphans_and_successors()
    refresh_name_index()
    auto = autolink_known_names()
    # second bidirectional pass after orphan attach
    bi2 = wire_bidirectional()
    refresh_name_index()
    rebuild_inbound()
    os.makedirs(PAGES, exist_ok=True)
    os.makedirs(CATS, exist_ok=True)
    for it in ITEMS:
        with open(os.path.join(PAGES, slug(it["name"]) + ".md"), "w") as f:
            f.write(render_page(it))
    with open(os.path.join(PAGES, "Wiki-Wire-Map.md"), "w") as f:
        f.write(render_wire_map())
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
    print(f"HWIKI-PLAIN-B backfill: {filled} pages gained plain_lang")
    print(f"HWIKI-PLAIN-C polish: {polished} pages hand-polished")
    print(f"HWIKI-WIRE: bidirectional +{bi}+{bi2} edges; orphan/successor attach {attached}; autolink hits {auto}")

if __name__ == "__main__":
    main()
