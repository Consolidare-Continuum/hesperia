# 08_PROJECT__Agent Workflow and RAG Reality (v0.1)

Purpose: reduce misinterpretation by automated agents (LLM-based coding assistants) working in this repository by specifying:

- interpretation rules (what HESPERIA is / is not),
- workflow traps (how drift happens in code and docs),
- RAG reality constraints (what is deterministic, what is not),
- minimum contribution gates (what must be updated together).

This document is internal. It constrains how work is performed here.

---

## 0. Interpretation rules (doctrine → implementation)

1. HESPERIA is a **constraint system**. It constrains, measures, exposes, and refuses. It is not an actor.
2. **Generation remains external**. Any LLM is an adapter. HESPERIA does not become “the speaker”.
3. “Admissible” ≠ “true”. Admissibility is structural legitimacy under declared constraints.
4. Refusal is a **correct output** under insufficient structure. Lower refusal for throughput is drift unless justified structurally.

Canonical references for these rules:

- `04_IDEOLOGY__Aequitas_et_cognitio_invictae_v0_2.md`
- `06_PRODUCT__Properties_and_Blind_Spots_v0_1.md`
- `07_PROJECT__Operating_Model_and_Documentation_Coherence_v0_1.md`
- `ACADEMIC.md`

## 1. RAG reality (what an agent must not assume)

### 1.1 Separation of concerns (RAG roles)

- **Retriever**: returns candidate evidence (chunks/statements) with identifiers and provenance.
- **Generator** (external): produces natural language output conditioned on evidence.
- **Constraint layer** (HESPERIA): evaluates structure, contradiction, stability, and policy; can refuse.

A common trap is to merge these roles and treat fluent generation as a substitute for admissibility. That is out of scope.

### 1.2 Determinism boundary (what “deterministic” means here)

Determinism is a property of:

- geometry/indexing (coordinates, side IDs),
- policy computations given fixed inputs,
- attribution given fixed dictionaries/embeddings/thresholds.

Determinism is *not guaranteed* by default for:

- approximate nearest-neighbor retrieval in vector DBs,
- embedding model updates or re-indexing,
- corpus growth and compaction effects.

Minimum rule for reproducibility in RAG work:

- version embeddings + thresholds,
- record retrieval parameters (top_k, filters, index settings),
- keep stable identifiers for sources and retrieved items,
- treat retrieval as evidence selection, not as semantic identity.

### 1.3 Evidence, provenance, and citations

If a change introduces or modifies retrieval/grounding:

- Evidence must remain linkable to sources (book/chunk/statement IDs, file paths, offsets when available).
- Provenance is not narrative; it is identifiers + trace paths.
- “Citations” in this repo mean machine-resolvable references (IDs/paths), not rhetorical footnotes.

### 1.4 Table naming trap (source vs semantic)

MySQL schema uses:

- `statements` = source-layer statements (book-derived).
- `statement` = semantic-layer statements (attributed + ready for placement/retrieval).

Automated changes must not conflate these. When in doubt, consult:

- `18_SPEC__MySQL_integration_and_ingestion_v0_1.txt`

## 2. Workflow traps for automated agents (how drift happens)

### 2.1 Documentation drift traps

- Rewriting stable docs in place instead of versioning forward.
- Introducing new terms without adding them to `ACADEMIC.md`.
- Mixing artifact types (doctrine content inside specs; technical mechanics inside doctrine).
- Adding line-number references to living docs (they rot quickly and create false certainty).

### 2.2 Implementation drift traps

- Reducing refusal thresholds to improve “success rate”.
- Increasing output verbosity without adding inspectable structure.
- Hiding contradictions by smoothing or “resolving” them narratively.
- Treating embedding similarity as semantic equivalence.
- Introducing provider-specific assumptions (OpenAI-only flows, hardcoded keys, non-portable APIs).

### 2.3 Naming and posture traps

Avoid agency/omniscience/conquest framing in:

- component names,
- CLI/UI copy,
- doc headings and summaries.

Disallowed examples are listed in:

- `04_IDEOLOGY__Aequitas_et_cognitio_invictae_v0_2.md`
- `07_PROJECT__Operating_Model_and_Documentation_Coherence_v0_1.md`

## 3. Minimum contribution gates (what must move together)

When an agent changes any of the following, it must update the linked artifacts:

- **New term or renamed concept** → update `ACADEMIC.md`.
- **New numbered doc** → update `DOC_INDEX.md` and (if entry-point relevant) `README.md`.
- **Change to ontology/coordinates/IDs** → version forward + note epoch boundary implications.
- **Change to governance thresholds/refusal behavior** → treat as policy; update relevant policy docs or add a versioned note.
- **Change to retrieval backends** → document determinism boundary and provenance requirements.

## 4. Prototype vs spec (avoid false assumptions)

Some code under `sphere_rag/` is intentionally minimal. Agents must not infer that all spec behavior is implemented.

Rule: if a module returns placeholders, document the gap explicitly and avoid building downstream authority on placeholder outputs.

## 5. Secret handling (operational)

- Do not copy `.env` values, API keys, or private endpoints into docs, logs, or commits.
- When adding examples, reference environment variables (e.g. `MYSQL_*`) and configuration files without embedding secrets.

