# TMX-17: query_knowledge / layer docs — timeline retrieval for agents

**Owner**: Abelard  
**Status**: 2026-05-11 — layer query contract documented.

---

## Purpose

Define the `query_knowledge` call contract for agents retrieving timeline matrix context from Chroma during session inspection.

## Layer query contract

### For session timeline context

```python
# Via MCP tool (preferred in n8n / agent nodes)
query_knowledge(
    query="<iteration label or relational summary>",
    channel="#agents-ingest",
    n_results=5,
    where={"layer": "tfp_corpus_ru"}   # or "reference_literature" when available
)

# Direct Chroma (Python, for supervisor runner)
col.query(
    query_texts=["<composed_query>"],
    n_results=5,
    where={"layer": "tfp_corpus_ru"},
    include=["documents", "metadatas", "distances"]
)
```

### Layer routing table (timeline retrieval)

| Use case | Layer | Channel ACL |
|----------|-------|-------------|
| TFP corpus context | `tfp_corpus_ru` | `#agents-ingest`, `#hesperia` |
| Reference literature | `reference_literature` | `#agents-ingest`, `#agents-ops` |
| Operational / workflow | `operational` | all channels |
| Books / theory | `books` | `#agents-ops`, `#hesperia` |

### Composition pattern (spec §6)

1. Build query from iteration labels + relational summary (see TMX-11 prompt pack slots).
2. Call `query_knowledge` with `where={"layer": "tfp_corpus_ru"}`.
3. Top-K = 5–8 → optionally rerank to 3–5 before feeding to supervisor.
4. If `corpus_available=false` (503 from `/inspector/tfp-corpus/compose`): fall back to `layer=operational` query.

### Agent usage (n8n / Tersagor)

In the n8n intent router (`cluster/trustmaster/n8n/ingest-minimal.template.json`):
```js
// For query_knowledge intent, already calls MCP /tool with n_results=2 and no layer filter.
// To add timeline context: include where: {layer: "tfp_corpus_ru"} in the MCP body.params
body: {
  tool: 'query_knowledge',
  params: { query: cleanPrompt(), channel, n_results: 3, layer: 'tfp_corpus_ru' }
}
```
Note: the MCP host (`cluster/trustmaster/imirc-mcp-host/mcp_host.py`) must pass `layer` from params to Chroma `where` filter. Verify with MCP host version ≥ 2026-05-08.

## Blocker

`tfp_corpus_ru` not in `chroma-new`. Until ingested, all timeline layer queries return empty (`corpus_available=false`). MCP host at `127.0.0.1:18093` on trustmaster uses SSH to prichindel Chroma — confirm SSH tunnel is still active.

SIGNED: DevOps (Abelard) | Hesperia TMX-17 layer docs | 2026-05-11 | timeline retrieval contract
