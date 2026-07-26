# Hesperia enhancements from Chroma (books): methods, model, approaches, yields, structure, algorithms

Date: 2026-03-25  
Scope: `/data/hesperia` (methods/model/approaches/yields/structure/algorithms)  
Basis: Chroma `layer=books` (275,395 chunks available on this host); targeted retrieval runs performed.

## Executive summary

This report proposes a **measurable upgrade path** for `/data/hesperia`:

- **P0**: install a **yield-first evaluation harness** (IR/RAG-style metrics + task-level acceptance metrics + regression gates). Without this, improvements to “methods/model” cannot be compared, and system drift is invisible.
- **P0**: make Hesperia’s “methods” **explicit, typed, and composable** (a method registry + contracts), so we can run controlled A/Bs and partial rollouts.
- **P1**: implement an **active-learning loop** driven by uncertainty + disagreement, so labeling/curation effort moves to the highest-yield samples.
- **P1**: upgrade retrieval to an **ANN-aware** design (latency/recall knobs, index choice, and monitoring), plus hybrid retrieval (lexical + vector) where needed.
- **P2**: add robustness layers (distribution shift handling, causal thinking where applicable, correctness proofs for critical algorithms).

## What “yield” must mean (definition)

Treat “yield” as **a vector of metrics**, not a single number. Minimum set:

- **Answer quality**: task success / acceptance; precision/recall where definable; graded relevance where ranking exists.
- **Retrieval quality** (when retrieval is used): Recall@k, Precision@k, nDCG@k, MRR (and per-query curves).
- **Cost & latency**: p50/p95 end-to-end latency; token/call cost (if LLM); CPU/RAM; index maintenance costs.
- **Reliability**: failure rate, timeouts, “no answer” rate, retry rate; reproducibility (same input → same output under pinned versions).
- **Safety / compliance** (if applicable): leakage rate, policy violations.

Book anchoring: standard IR evaluation emphasizes **precision/recall tradeoffs and ranked retrieval measures** (precision as a function of recall; ranking-oriented measures). Sources surfaced in Chroma include:
- *Elmasri & Navathe, Fundamentals of Database Systems* (IR evaluation measures, average precision).  
- *Silberschatz & Sudarshan, Database System Concepts* (precision/recall framing for ranked retrieval).

## Current-state assumptions (explicit)

Because this request is “enhance `/data/hesperia`” without pointing at the code, I assume:

- Hesperia already has **multiple methods** (heuristics, retrieval, model-based, pipelines).
- Hesperia produces outputs that can be judged (even if noisy) against human acceptance or proxy metrics.
- Hesperia has enough data/logs to build an offline evaluation set, or can be instrumented to create one quickly.

If any assumption is false, the plan still holds: it just changes “where we get labels/ground truth.”

## Proposals (prioritized)

### P0 — Yield-first evaluation harness (“measure before optimize”)

Deliverables:

- **`hesperia-eval`**: a runnable evaluation pipeline producing a versioned report (JSON + markdown).
- **Datasets**: a curated “golden” set (small, high quality) + a “shadow” set (large, noisy).
- **Gates**: regression checks in CI or workflow automation: “cannot merge / deploy method changes if yield regresses beyond tolerance.”

Design notes:

- For retrieval/ranking tasks, implement **Recall@k / Precision@k / nDCG@k / MRR** plus per-query breakdowns.
- For non-ranking tasks, define a task-specific acceptance metric and **calibration** of “no answer” vs “wrong answer” (penalize confidently wrong).

Evidence in books layer points to classical IR evaluation measures and the precision-recall curve as the primary organizing structure (see sources above).

### P0 — Method registry + contracts (structure upgrade)

Goal: turn “methods” into **first-class objects** with stable contracts so they can be composed, benchmarked, and rolled out safely.

Deliverables:

- **Method registry**: each method has `id`, `version`, `inputs schema`, `outputs schema`, `cost model`, `failure modes`.
- **Typed result envelope**: `answer`, `supporting_evidence`, `confidence`, `abstain_reason`, `trace`.
- **Traceability**: every run emits a method trace with enough data to reproduce (model versions, retrieval params, prompt/templates, index id).

Payoff:

- You can run **A/B tests**, canary deployments, and multi-armed bandits later.
- You can attribute yield changes to a method version instead of “the system.”

### P1 — Active learning loop (high leverage, low waste)

Goal: spend curation/labeling effort where it improves yield fastest.

Deliverables:

- **Acquisition policies**:
  - uncertainty sampling (low margin / high entropy),
  - disagreement (committee / method-ensemble disagreement),
  - error-driven sampling from evaluation failures.
- **Queue**: “to label / to curate / to fix” samples with metadata (why chosen, expected yield).

Book anchoring:

- *Percy Liang (CS229T/STAT231 notes)* highlights that active selection can dramatically improve sample efficiency in some settings (classic 1D threshold example; binary search vs i.i.d.).  
- *Francis Bach, Learning Theory from First Principles* explicitly summarizes active learning as selecting unlabeled points based on uncertainty estimation.

### P1 — Retrieval architecture upgrades (ANN knobs + hybrid retrieval)

Goal: make retrieval **predictable** under scale and tuneable for the yield/latency tradeoff.

Deliverables:

- **Index policy**: pick and document index type and parameters; treat them as versioned artifacts.
- **Latency/recall tuning**: explicit knobs; monitor recall proxy metrics and p95 latency simultaneously.
- **Hybrid retrieval**: combine lexical retrieval (exact terms) + semantic retrieval (embeddings), then rerank.

Book anchoring (ANN / nearest-neighbor algorithms):

- *Yuri Lifshits, Algorithms for Nearest Neighbors* surfaced as relevant; it references classic approximate NN work (e.g., Indyk & Motwani; Kleinberg) and frames the computational tradeoffs.  
- Additional surfaced material (ESLII) reinforces kNN’s performance sensitivity to the metric and approximation choices (useful as a mental model for embedding space retrieval).

### P2 — Robustness to distribution shift (explicit “shift budget”)

Goal: acknowledge drift and handle it explicitly.

Deliverables:

- **Operational profile tracking**: define cohorts/environments; evaluate per cohort.
- **Shift detectors**: embedding distribution drift, topic drift, failure-mode drift.
- **Mitigations**: reweighting, targeted reindexing, domain adaptation strategies, and policy-driven fallback methods.

Book anchoring surfaced learning-theory references (Bach) around generalization, surrogate risks, and structured prediction. Even when specific IRM “buzzwords” are not captured cleanly by retrieval, the general point holds: treat generalization as a measured property, not assumed.

### P2 — Correctness discipline for critical algorithms (prove what must be true)

Goal: for critical algorithmic components (ranking logic, constraints, filters, scoring), require proofs/derivations and property-based tests.

Book anchoring:

- *Skiena, The Algorithm Design Manual* explicitly emphasizes reasoning about correctness, and the necessity of proofs (often by induction/recursion) instead of “it seems to work.”

## A concrete 2–3 week execution plan (fast, measurable)

### Week 1: Measure + structure

- Build `hesperia-eval` skeleton; define yield vector; create the first golden set.
- Add method registry + result envelope; instrument traces.
- Baseline current methods and freeze a “baseline report.”

### Week 2: Retrieval + active learning foundation

- Add retrieval metrics and cohort breakdown.
- Implement active-learning queue from eval failures + disagreement between existing methods.
- Ship ANN/hybrid retrieval knobs behind flags (no default change yet).

### Week 3: Improve yields with controlled changes

- Run a small set of targeted improvements (top 3 failure modes), each with:
  - hypothesis,
  - method change,
  - eval report,
  - rollout plan.

## Immediate next actions (what I would do in the repo / on host)

To convert this report into execution, the next minimal steps are:

- Inspect `/data/hesperia` layout: where methods live, where logs are, where evaluation can hook in.
- Create the evaluation harness + method registry in the codebase, wired to a small dataset.
- Add a “yield regression” gate to the workflow runner (so changes cannot silently regress).

SIGNED: Engineer (Ethan) | Cursor context | 2026-03-25 | Hesperia methods/model/yields proposals from Chroma books

