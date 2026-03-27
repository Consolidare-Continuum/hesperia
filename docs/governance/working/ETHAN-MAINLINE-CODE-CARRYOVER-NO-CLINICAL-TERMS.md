# Mainline carryover: implementation only — no clinical vocabulary

**Status:** binding intent for Engine Dynamics mainline (sealed product path, v0.5.1 lineage and forward).  
**Scope:** what may move from experimental lexical/TFP-style stacks into canonical code and specs.

---

## 1. What we do not carry into mainline

The following must **not** appear in canonical specs, public schemas, shipping surfaces, or product-facing documentation as **defining** vocabulary:

- Medical, psychiatric, psychotherapeutic, or diagnostic terminology (including modality-specific labels used as *domain semantics*).
- Roles or settings framed as care, treatment, patient, clinician, or session-as-therapy (as product meaning).
- Any wording that implies regulated health claims or clinical decision support in the **product** narrative.

**Allowed:** neutral technical nouns already in the engine (e.g. *concept*, *segment*, *window*, *area*, *family*, *hex*) where they denote **structural indices** in the Hesperia topology, not medical entities.

Clinical and domain-specific corpora may continue to exist only under **non-product** trees (`research/`, experimental tests, optional assets) per `EXTENSION_STATUS.yaml` and `docs/PUBLIC_PRODUCT_SURFACE.md`.

---

## 2. What we do carry: code and implementation decisions

Mainline adoption is limited to **reproducible engineering choices**, expressible without clinical framing:

| Decision class | Description (domain-neutral) |
|----------------|------------------------------|
| **Evidence path** | Lexical matches → aggregated per-id weights → deterministic stabilization (caps, length normalization, optional dampers). |
| **Single authoritative downstream path** | One execution_flow from stabilized concept-level weights through hex-related feedback into area-level competition and normalized outputs; alternatives remain audit-only. |
| **Bounded transforms** | Nonlinear saturation, pruning, normalization, and fixed-temperature competition so scores do not drift unbounded across long inputs. |
| **Temporal topology** | Segmentation of text into windows or spans; optional deterministic smoothing or carried state between segments. |
| **Fixed sparse operator (optional)** | Precompiled symmetric bounded sparse graph over a declared concept index; one-step state update with explicit coefficients; load from versioned JSON; default off until matrix is release-pinned. |
| **Calibration as data** | Numeric parameters and file references in `assets/` (versioned), not ad hoc runtime tuning from free text. |
| **Audit envelope** | Internal fields for operator flags, matrix id, counts, top-k mass — for governance and regression, not for public projection unless explicitly schema-approved. |

These decisions are **orthogonal** to which real-world domain later maps onto the lexicon; the engine describes **topology and determinism**, not indication or use case.

---

## 3. Code locus (reference, not exhaustive)

Implementation that embodies the above may live in shared modules (e.g. `hesperia/nlp/*`, `hesperia/engine/*`, `core/*`, `lexicon/*`) **provided** public names, docstrings, and schema fields in shipping paths comply with §1.

Experimental orchestration and domain-specific runners remain out of the shipping graph unless allowlisted.

---

## 4. Review gate

Any change that:

- introduces clinical or medical **product** vocabulary into canon or public artifacts, or  
- promotes `research.*` / experimental-only semantics into `runtime/shipping`, public schema, or sealed release narrative  

requires an explicit **minor release** decision and documentation update — not a silent patch on a sealed line.

---

## 5. Relation to other docs

- Product boundary: `docs/PUBLIC_PRODUCT_SURFACE.md`  
- Extension registry: `EXTENSION_STATUS.yaml`  
- Optional sparse concept operator (technical): `docs/semantic_dynamics_operator_spec.md` (must be described in neutral terms; no clinical use cases as normative requirements)
- Master index §8 (v0.5.1 code envelope): `docs/HESPERIA_v0_5_ENGINE_DYNAMICS.md`  
- Tier-1 index hooks: `specs/CANONICAL_INDEX.md` (v0.5.1 implementation anchors)

---

## 6. Main execution_flow integration backlog (engine features to keep; clinical shell to drop)

**Policy:** Pull **code paths and data shapes** into shared modules and main runners; leave **clinical naming and `research.clinical_tfp` interpretation** in research unless re-specified as domain-neutral.

| Item | Where it lives today | Main-execution_flow target |
|------|----------------------|----------------------|
| Lexical → markers → concept evidence → stabilization → hex → area competition | `hesperia/nlp/session_parser.py`, `hesperia/nlp/tfp_activation.py` | **Keep** as default path for any text that needs concept-level mass before hex; optional rename component/file to neutral `concept_activation` with re-export. |
| Versioned numeric calibration + suppression matrix bundle | `hesperia/engine/tfp_signal_calibration.py`, `assets/data/engine_dynamics_v060/tfp/` | **Keep**; treat as **lexical/area competition calibration pack** (filename “tfp” is legacy; data is structural). |
| Optional sparse operator + `ψ` carry | `hesperia/nlp/semantic_state_update.py`, `semantic_dynamics` block in calibration JSON | **Keep**; enable when `h_total_concepts.json` is pinned to the active concept index ([spec](../../semantic_dynamics_operator_spec.md)). |
| Windowed segments + `psi_prev` threading | `research/clinical_tfp/session_topology.py`, `hesperia/nlp/session_topology.py` | **Expose** from neutral entrypoints (same functions, no clinical imports in shipping allowlist). |
| Speaker / role-weighted marker merge | `analyze_session_speaker_aware` in `session_parser.py` | **Keep** as **multi-channel weighting**; document without care-setting vocabulary in mainline docs. |
| Family embedding propagation (topology) | Optional branch in `tfp_activation.py` via `sphere.topology` | **Keep** as optional post-activation propagation when embedding asset present. |
| DLCR lexical-concept execution_flow | `hesperia/engine/lexical_concept/execution_flow.py` | **Already** parallel canon path; align naming with §1–2 of this doc. |
| TFP stage enum / `detect_tfp_stage` | `research/clinical_tfp/stage_detection.py` | **Do not** promote labels to mainline; replace with **neutral phase mapping** if product needs discrete stages. |
| `run_tfp_file_pipeline` orchestration | `runtime/execution_flow/run_tfp_file_pipeline.py` | **Refactor** over time: call shared analyze/topology helpers; keep clinical-only artifacts behind flags; optional rename to `run_lexical_calibration_bundle.py` when content is generic. |
| Product E2E minimal path | `runtime.pipeline.run_e2e_product` | **Optional add:** smoke that touches lexical→concept path (and optional `H` when enabled) without clinical fixtures. |

---

*Ethan — mainline carryover policy: topology and code only; clinical language excluded from canonical product definition.*
