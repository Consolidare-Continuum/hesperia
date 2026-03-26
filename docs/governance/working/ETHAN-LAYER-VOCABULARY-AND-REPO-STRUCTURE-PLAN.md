# Ethan plan — distinct names (R / Tier / F), definitions, repo topology

**Status:** Planning — documentation and symbols migrate in phases; **no** shared **L*** vocabulary for these three ladders in new material.  
**Normative vocabulary:** [LAYER_VOCABULARY_AND_STRUCTURE.md](../../LAYER_VOCABULARY_AND_STRUCTURE.md).  
**File/term checklist (do not execute yet):** [ETHAN-VOCABULARY-MIGRATION-INVENTORY.md](ETHAN-VOCABULARY-MIGRATION-INVENTORY.md).

**Related:** [HESPERIA_DEPENDENCY_GRAPH.md](../../HESPERIA_DEPENDENCY_GRAPH.md), [LAYER_PIPELINE_ORDER.md](../../LAYER_PIPELINE_ORDER.md), [ETHAN_SEMANTIC_FIELD_DYNAMICS_SPEC.md](../../../specs/dynamics/ETHAN_SEMANTIC_FIELD_DYNAMICS_SPEC.md), [ENGINE_DYNAMICS_CANONICAL_NAMING_v0.5.md](../../ENGINE_DYNAMICS_CANONICAL_NAMING_v0.5.md).

---

## 1. Problem

Prefixes (**Sphere-L5**, **Ethan-L5**) still imply **one numbering scheme** with tags. We need **different names and letters** so **no index implies another**.

---

## 2. Target naming (normative)

| Ladder | New primary names | Legacy (phased out in prose) |
|--------|-------------------|------------------------------|
| Sphere numeric execution_flow | **Metric cascade**, stages **R1–R10** | L1–L10 |
| Dependency graph | **Tiers**, **Tier 0–Tier 11** | Layer 0–11 |
| Ethan Part A timeline | **Field phases**, **F0–F10** | L0–L10 |
| Text → hits | **Attribution** (no stage number) | “word layers” |
| Product geometry | **Multiscale chain** (concept→…→HSPR) | informal “layers” |

**Rules**

- **R*, F*, Tier *** are **not** interchangeable: **F5 ≠ R5**.
- New specs and runbooks use **R / Tier / F**; JSON keys and Python `layer_id` may lag until a release-gated rename.
- Optional table shorthand **T0–T11** for tiers only with an explicit legend (avoid **T** vs TRIZ confusion in prose — prefer **Tier *k***).

---

## 3. Phased plan

### Phase 0 — Ratify symbols (docs-only)

- [ ] ACK **R1–R10**, **Tier 0–11**, **F0–F10** on [LAYER_VOCABULARY_AND_STRUCTURE.md](../../LAYER_VOCABULARY_AND_STRUCTURE.md).
- [ ] Ethan spec Part A: terminology box with **F0–F10** and pointer to metric cascade **R1–R10** as **distinct** ladder.
- [ ] **Exit:** merged PR; no code changes required.

### Phase 1 — Doc sweep (replace L-labels in prose)

1. **ETHAN_SEMANTIC_FIELD_DYNAMICS_SPEC.md** — Part A: **F0–F10** throughout (keep backward-compat footnote “formerly L0–L10” once per major section if needed).
2. **HESPERIA_DEPENDENCY_GRAPH.md** — headings **Tier 0 … Tier 11**; opening paragraph legacy map.
3. **LAYER_PIPELINE_ORDER.md** — retitle to **Metric cascade (R1–R10)**; table column **Stage** = R1…R10.
4. **HESPERIA_SYSTEM_SPEC_v1.md**, **internal PIPELINE_LAYER_REGISTRY**, **MATH_LAYER_REGISTRY** — dual column **R*k*** / legacy L*k* until code catches up.
5. **AGENTS.md**, **HESPERIA_v0_5_ENGINE_DYNAMICS.md**, **ENGINE_DYNAMICS_CANONICAL_NAMING** — link vocabulary doc; use **R/Tier/F** in new paragraphs.

- [ ] **Exit:** CI green; regen **IMPORT_GRAPH** only if comments/paths changed.

### Phase 2 — Code-facing aliases (low risk)

- [ ] Constants or enums: e.g. `MetricStageId.R4` mirroring existing numeric ids (additive, no JSON break).
- [ ] Component docstrings: “implements **R4** (legacy layer_id L4)”.
- [ ] Runtime orchestrator comment: **F*** phase → packages invoked.

### Phase 3 — Optional package moves

- Same as before: only after Phase 1; gates for imports / seal.

### Phase 4 — Breaking rename (product decision)

- Public JSON / `layer_id` strings **L1→R1** (or keep **L** in artifacts forever and document as legacy-only) — requires **version / seal** process.

---

## 4. Acceptance criteria

- No new documentation uses **L*n*** for **metric cascade**, **dependency bands**, or **Ethan field** without marking it **legacy**.
- One glance at a heading tells **which ladder**: **R** vs **F** vs **Tier**.

---

## 5. Out of scope

- Changing **math inside** R1–R9.
- Renaming multiscale chain nouns (concept, hex, …).
- **H*** hex hooks in Ethan — separate symbol set; document cross-reference to **F*** when touching dynamics docs.

---

*Ethan / governance — distinct names (not prefixes) for each ladder.*
