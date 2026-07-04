# Documentation traceability matrix (ISO/IEC/IEEE 15289-style information-item register)

This is the master registry the rest of the ISO-grade and publication documentation tiers plug
into. Each row is one required information item, which standard it answers to, which document
satisfies it, and whether that document's claims have actually been checked against source — the
same "verified, not merely cited" discipline `docs/foundations/provenance.md` already established
for spec citations.

**How to read `status`:** `built` = document exists and its claims are source-verified. `draft` =
document exists but has not had a full verification pass. `todo` = not yet written. A row with
`built` is a claim about the *document*, not about the underlying system being finished — a `built`
architecture description can honestly describe an in-progress subsystem, as long as it says so.

**`last_verified_against_commit`** is the mechanism that keeps this LTS: a row whose commit hash is
behind the current `HEAD` is a visible signal to re-check, not a silent drift.

| Information item | Standard | Document | Built from | Status | Last verified against commit |
|---|---|---|---|---|---|
| Architecture description (stakeholders/viewpoints/concerns) | ISO/IEC/IEEE 42010 | `docs/iso/ARCHITECTURE_DESCRIPTION.md` | Full index grind: all 22 `corners/*.md`, all 11 `layers/*.md`, all 8 `eras/*.md` from `00_INDEX.md` (era 8 added), each registered against a viewpoint in Appendix A | built | `eec627ac` |
| Requirements specification (functional + non-functional) | ISO/IEC/IEEE 29148 | `docs/iso/REQUIREMENTS_SPECIFICATION.md` | `specs/canon/*.yaml` (Sigma/Gamma/Theta invariant IDs, verified), `core/math/core_math.py`, `VERSION.yaml`, `corners/lexicon_resolver.md`, `corners/shadow_correction.md` (`max_entropy_increase=0.1`, verified against `sphere/shadow/entropy_correction.py`), `corners/interpretation_usf.md`; NFR-G3/NFR-I1 added — flag-default-off discipline and Layer-11 read-only guarantee, both traced to passing tests, not just cited as design intent | built | `eec627ac` |
| Product quality model | ISO/IEC 25010 (SQuaRE) | `docs/iso/QUALITY_MODEL.md` | `corners/guards.md` (Sigma/Gamma/Theta), `corners/release_governance.md`, 294 test files under `tests/` (verified count); Security row extended with the fpf_bridge_v7_3 new-exposure-path recognition (process evidence, still no threat model); Maintainability row extended with `runtime/agentic_bridge/` as a further modularity instance | built | `eec627ac` |
| Software life cycle process model | ISO/IEC/IEEE 12207 | `docs/iso/LIFECYCLE_PROCESS.md` | `corners/release_governance.md`, `corners/release_seal.md`, `VERSION.yaml`, `eras/*.md`; §1 now cites the three ratification-pending fpf_bridge specs as a live, current instance of the "not done until sealed" pattern | built | `eec627ac` |
| Information-item register (this document) | ISO/IEC/IEEE 15289 | `docs/iso/DOCUMENTATION_TRACEABILITY_MATRIX.md` | — (self) | built | `eec627ac` |
| Operator/user documentation | ISO/IEC/IEEE 26511/26512 | `docs/iso/OPERATOR_GUIDE.md` | `docs/ENGINE-ANALYZE-CONTRACT.md`, `runtime/services/product_interpret_service.py`, `output_catalog.md` §0 | built (re-verified this pass — `runtime/agentic_bridge/` is not an HTTP endpoint, correctly out of this guide's stated scope, no content change needed) | `eec627ac` |
| Novelty & positioning statement (invention vs. innovation) | — (publication track, not ISO) | `docs/publication/NOVELTY_AND_POSITIONING.md` | `provenance.md`, `corners/pipeline_l1_l11_science.md` | built | `63a2295b` |
| Productization / MVP orientation Q&A (time-bounded GTM layer) | — (publication/productization track) | `docs/publication/UPCELERATOR_PRODUCTIZATION_QA.md` | Upcelerator 2026 archive at `/data/altitudine/prichindel.com/.cache_to_sort_out/HESPERIA - Upcelerator 2026-20260704T155731Z-3-001.zip`; market-definition, pitch-script, landing-page, pivot, and key-insights files; doc explicitly preserves virtual-round caveats instead of laundering them into timeless product truth | built | `a9ae78fd` |
| Methods (paper-shaped pipeline description) | — (publication track) | `docs/publication/METHODS.md` | `corners/pipeline_l1_l11_science.md`, `output_catalog.md`, `parameter_catalog.md` | built | `63a2295b` |
| Validation evidence index | — (publication track) | `docs/publication/VALIDATION_EVIDENCE.md` | `tests/router`, `tests/calibration`, `tests/test_product_interpret_api.py` (76 tests re-run, exit 0), `scripts/verify-hesperia-v7-source-truth.sh`, `release/v0.7.0/RELEASE_SCOPE.md` | built | `63a2295b` |
| Reproducibility package | — (publication track) | `docs/publication/REPRODUCIBILITY_PACKAGE.md` | `VERSION.yaml` (re-read directly), `parameter_catalog.md` (seeds, tolerances) — found and fixed a stale pin example in `corners/calibration.md` in the process | built | `63a2295b` |
| Terminology and abbreviations register (glossary) | ISO/IEC/IEEE 15289 (glossary item) + publication nomenclature | `docs/publication/TERMINOLOGY_AND_ABBREVIATIONS.md` | Full grep-based abbreviation sweep across `docs/foundations/`, `docs/iso/`, `docs/publication/`; every KME derived-metric code verified letter-for-letter against `hesperia/engine/kme/derived/calculator.py`; 35 metric-code expansions explicitly marked PROPOSED (unverified) pending author confirmation; 3 terms (BELL, `HSR`, `HSPR`) marked UNRESOLVED rather than guessed | built (with declared open items — see doc §5/§7/§10) | `63a2295b` |
| Science register (named scientists/works, extent of application) | — (publication track) | `docs/publication/SCIENCE.md` | Consolidates `references.md`, `corners/pipeline_l1_l11_science.md`'s formula-lineage table, `provenance.md`; ~35 works across 11 disciplines scored on a 5-level extent taxonomy (full-verbatim / partial / structural-analogy / conceptual-inspiration / explicitly-rejected); a declared subset of full citations (Blondel et al. 2008, Lesk 1986, Colmerauer & Roussel 1972, Fellbaum 1998, Cauchy 1821/Schwarz 1888) supplied from established record, not from a Hesperia source file — flagged in the doc's own methodology note | built | `63a2295b` |

## Existing documents this matrix does not duplicate

These already satisfy real information-item needs and are referenced, not re-created, by the rows
above:

| Existing document | Role this matrix relies on it for |
|---|---|
| `docs/foundations/00_INDEX.md` | Narrative architecture trace — primary source for `ARCHITECTURE_DESCRIPTION.md` |
| `docs/foundations/parameter_catalog.md`, `output_catalog.md` | Exhaustive, source-verified parameter/output inventory — primary source for `METHODS.md` and `REPRODUCIBILITY_PACKAGE.md` |
| `docs/foundations/provenance.md` | Canonical-vs-native audit — primary source for `NOVELTY_AND_POSITIONING.md` |
| `docs/foundations/corners/release_seal.md`, `corners/release_governance.md` | Existing code-seal discipline — `LIFECYCLE_PROCESS.md` formalizes this, does not replace it |
| `docs/ENGINE-ANALYZE-CONTRACT.md` | Frozen legacy HTTP contract — input to `OPERATOR_GUIDE.md`, not superseded by it |
| `VERSION.yaml` | Single source of truth for component/pipeline versions — cited, never re-stated as a separate number, by any document in this matrix |

## Maintenance rule (the LTS mechanism)

On every version seal (`corners/release_seal.md`'s existing process), before the seal is signed:
1. Check every `built` row's `last_verified_against_commit` — if it's behind the commit being
   sealed, re-verify that row's document against current source before the seal proceeds.
2. Any new `docs/iso/*` or `docs/publication/*` document must add a row here before being
   considered complete — a document with no row in this matrix is not yet part of the tracked set.
3. `status` moves `todo` → `draft` → `built` only when the document's specific factual claims (not
   just its existence) have been checked against the source file it cites — the same bar
   `output_catalog.md`'s per-layer tables were held to.

## Navigation

← [`docs/README.md`](../README.md) (start here — this matrix is linked from there as the master
registry) · [`../foundations/00_INDEX.md`](../foundations/00_INDEX.md) (full system trace)

Every document row above links to itself in its own file for direct navigation:
[`ARCHITECTURE_DESCRIPTION.md`](ARCHITECTURE_DESCRIPTION.md) ·
[`REQUIREMENTS_SPECIFICATION.md`](REQUIREMENTS_SPECIFICATION.md) ·
[`QUALITY_MODEL.md`](QUALITY_MODEL.md) · [`LIFECYCLE_PROCESS.md`](LIFECYCLE_PROCESS.md) ·
[`OPERATOR_GUIDE.md`](OPERATOR_GUIDE.md) ·
[`../publication/NOVELTY_AND_POSITIONING.md`](../publication/NOVELTY_AND_POSITIONING.md) ·
[`../publication/METHODS.md`](../publication/METHODS.md) ·
[`../publication/VALIDATION_EVIDENCE.md`](../publication/VALIDATION_EVIDENCE.md) ·
[`../publication/REPRODUCIBILITY_PACKAGE.md`](../publication/REPRODUCIBILITY_PACKAGE.md) ·
[`../publication/TERMINOLOGY_AND_ABBREVIATIONS.md`](../publication/TERMINOLOGY_AND_ABBREVIATIONS.md) ·
[`../publication/SCIENCE.md`](../publication/SCIENCE.md)
