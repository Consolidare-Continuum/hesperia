# Ethan workflow packet — Hesperia productization T11–T20

Date: 2026-03-26  
Project: `hesperia`  
Scope: product translation layer on top of deterministic engine without adding new engine layers.

## Task set

1. T11 Product Contracts Freeze — Owner: Daniel (review Olivia)  
   Deliverable: strict schemas for `llm_audit`, `tfp_analysis`, `document_fingerprint` in `hesperia/product/contracts/`  
   Acceptance: schema-validated outputs only; no top-level leakage; confidence in `[0,1]`.

2. T12 Interpretation Rule Engine — Owner: Gena  
   Deliverable: deterministic rule files under `hesperia/product/rules/` and mapper from engine signals to product decisions  
   Acceptance: same input + same profile = byte-identical decision output.

3. T13 Profile System Finalization — Owner: Sophia  
   Deliverable: isolated profile configs in `hesperia/product/profiles/` (`llm_audit`, `tfp`, `document`) with versioned thresholds/rules  
   Acceptance: profile switch changes only profile-bound behavior; no cross-profile contamination.

4. T14 Metric Stability Audit Gate — Owner: Noah  
   Deliverable: audit runner for 10x same-input stability (`stability_delta`, `entropy_variance`, vector variance)  
   Acceptance: deterministic hashes stable; drift report generated and enforced.

5. T15 Threshold Calibration on Real Corpus — Owner: Gena (paired Noah)  
   Deliverable: calibrated LOW/MEDIUM/HIGH boundaries per product profile with corpus-backed evidence  
   Acceptance: thresholds independent of text length artifacts; calibration report persisted.

6. T16 Output Compression Layer — Owner: Liam  
   Deliverable: deterministic mapping from dense engine outputs to 4-6 product decisions + `decision_basis` trace  
   Acceptance: compressed outputs reproducible and explainable without raw metric leakage.

7. T17 Product API Endpoints — Owner: Ava  
   Deliverable: `POST /product/llm-audit`, `POST /product/tfp`, `POST /product/fingerprint`  
   Acceptance: endpoint responses schema-valid, profile-versioned, and deterministic.

8. T18 Failure Modes & Guardrails — Owner: Marcus  
   Deliverable: explicit status taxonomy (`ok|insufficient_data|low_coverage|input_too_long|noisy_input`) + coverage reliability checks  
   Acceptance: no silent degradation; all guardrail exits explicit and test-covered.

9. T19 Demo Pipelines + Comparative Runs — Owner: Gena  
   Deliverable: demo scripts (`demo_llm_audit.py`, `demo_tfp.py`, `demo_fingerprint.py`) + run-compare workflow  
   Acceptance: reproducible decision printouts and meaningful delta reports across profile/module toggles.

10. T20 Product Evaluation Benchmarks — Owner: Olivia (QA)  
    Deliverable: benchmark sets for LLM audit, TFP, and document coherence with consistency/accuracy scoring  
    Acceptance: benchmark report with run-to-run consistency and misclassification review.

## Execution order

`T14 -> T15 -> T11 -> T12 -> T13 -> T16 -> T18 -> T17 -> T19 -> T20`

## Engine watchpoints (hard constraints)

- Fix normalization drift at source, never in product schema.
- Enforce saturation for accumulative scores to prevent long-text bias.
- Preserve deterministic ordering and stable iteration at all stages.
- Add caching only for deterministic intermediates (normalized tokens, dict matches, segment outputs).
- Track dict quality (`coverage`, `unknown_tokens`, `ambiguity`) as first-class product risk.

SIGNED: Architect (Ethan) | hesperia context | 2026-03-26 | productization tasks T11-T20
