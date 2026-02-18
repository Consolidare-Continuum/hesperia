# Ethan report: Semantic engine integration in Hesperia — Chroma vs tech investigation

**Task**: [TASK-ETHAN-HESPERIA-SEMANTIC-ENGINE-INTEGRATION.md](TASK-ETHAN-HESPERIA-SEMANTIC-ENGINE-INTEGRATION.md)
**Owner**: Ethan
**Date**: 2026-02-18

---

## Question

Proceed open task: do we run a **tech investigation** for "our best shot" on a dedicated semantic engine, or **still use Chroma** for Hesperia semantic engine integration?

---

## Recommendation: use Chroma

**Use Chroma** as the semantic engine for Hesperia integration (cursor-repo today; product semantic layer when in scope in Phase D). **No separate tech investigation** for an alternative engine unless we hit a clear gate.

### Rationale

1. **Single store, one ops path**
   Chroma is already the main knowledge store (CHROMA-USAGE-POLICY). hesperia_families, matrix_run, context_rag, books, FPF are on Chroma. One schema, one ingest pipeline (Abelard), one server. Adding a second engine = second vector store, second ops, split context and duplication.

2. **Cursor-repo use is already Chroma**
   Agents (Cursor, Albina) use Chroma for matrix-derived context and context packets. Hesperia “semantic engine” in cursor-repo **is** Chroma + matrix_run + context_rag. No gap to fill with another engine for current scope.

3. **Product semantic layer (Phase D)**
   When SCOPE-AND-SYNC moves to include the product semantic layer (RAG, full engine in workspace), the default is **same stack**: Chroma as the semantic/vector backend for that layer too, unless Phase D explicitly calls for a product-native engine or we hit hard limits.

4. **When to revisit (tech investigation)**
   Run a dedicated “best shot” engine investigation only if:
   - Phase D scope **explicitly** requires a different engine (e.g. product ships its own RAG service), or
   - We hit **hard limits** (scale, latency, feature gap, cost) that Chroma cannot address with current tuning (CHROMA-COOKBOOK-ABELARD, chops, optional hnsw rebuild).

---

## Summary

| Option | Recommendation |
|--------|----------------|
| **Use Chroma** | **Yes** — semantic engine for Hesperia (cursor-repo and, when in scope, product) = Chroma. |
| **Tech investigation for alternative engine** | **No** for now. Revisit only on Phase D decision or proven Chroma limits. |

---

**SIGNED: Architecture (Ethan) | semantic engine integration in Hesperia | 2026-02-18 | governance**
