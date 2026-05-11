# TMX Prompt Pack — Whole-session T3 + Supervisor Stance

**Tier**: T3 (Research / draft — non-binding per `specs/INVENTORY.md`)  
**Scope**: Timeline Matrix viewer whole-session analysis; supervisor stance for parameter drift + appear/disappear signals.  
**Used by**: `timeline_matrix_blob.run_supervisor_checklist`, Tersagor agent, Cursor agent loop.

---

## 1. System prompt (supervisor stance)

```
You are a Hesperia session supervisor. Your role is to analyse whole-session trajectory data from
the Timeline Matrix. You receive:
  • A session header (id, iteration range, tier context).
  • A matrix summary (dominant areas, drift table, stability).
  • Appear/disappear signals (family onsets, offsets, theme markers).
  • Parameter diffs between selected iterations.
  • An optional user question.

Rules:
  1. Answer from the provided context only. If the data is absent for a claim, state "not determinable from this session."
  2. Distinguish observation (what the data shows) from interpretation (what it may mean).
  3. Do not reveal internal scoring weights, raw vector values, or system implementation details.
  4. Keep responses brief and operational (3–8 sentences unless detail is explicitly requested).
  5. When a drift exceeds ±0.15, flag it as a notable shift.
  6. Parity note: if therapist-parity data is present, include a one-line assessment.
```

---

## 2. T3 prompt slots

These slots are filled by `build_interpretation_blob_v1` before sending to the LLM.

### Slot: `{session_header}`

```
Session: {{session_id}}
Iterations: {{iteration_range}}  (e.g. "1–12")
Tier: T3 (research context)
Corpus layer: {{corpus_layer}}  (e.g. "tfp_corpus_ru" | "hesperia_families")
```

### Slot: `{matrix_summary}`

```
Dominant areas (by mass): {{top_areas_list}}
Global drift vs imprint: {{global_drift_value}} (positive = higher activation vs baseline)
Stability median: {{stability_median}}
Coherence active: {{coherence_on}}
```

### Slot: `{appear_disappear_signals}`

```
Appeared in session:
{{#appeared}}
  - {{label}} (onset frame {{onset_frame}}, peak dominance {{dominance_peak}})
{{/appeared}}
{{^appeared}}(none detected){{/appeared}}

Disappeared in session:
{{#disappeared}}
  - {{label}} (offset frame {{offset_frame}})
{{/disappeared}}
{{^disappeared}}(none detected){{/disappeared}}

Dominant shift summary: {{dominant_shift}}
```

### Slot: `{parameter_diffs}`

```
Parameter comparison (iteration {{iter_a}} vs {{iter_b}}):
{{#diffs}}
  - {{param_name}}: {{value_a}} → {{value_b}} (delta {{delta}})
{{/diffs}}
{{^diffs}}(no diff requested){{/diffs}}
```

### Slot: `{user_query}`

```
User question: {{query_text}}
```

---

## 3. Composed T3 prompt (full template)

```
<session_context>
{session_header}
</session_context>

<matrix_summary>
{matrix_summary}
</matrix_summary>

<signals>
{appear_disappear_signals}
</signals>

<parameter_diffs>
{parameter_diffs}
</parameter_diffs>

{user_query}

Based on the above, provide a concise supervisor assessment covering:
1. Most notable area drift and its likely clinical relevance.
2. Key appear/disappear signals (if any).
3. Iteration comparison assessment (if diffs provided).
4. Parity observation (if parity_note present).
```

---

## 4. Supervisor checklist slots (deterministic mode)

When `use_llm=False`, `run_supervisor_checklist` fills these four slots without an LLM call:

| Slot | Source field | Rule |
|------|-------------|------|
| `drift_assessment` | `relations.area_drift` | Flag any area with `abs(drift) > 0.15`; otherwise "within normal range" |
| `stability_assessment` | `matrix_summary.stability_median` | `< 0.4` → "low stability detected"; `≥ 0.7` → "high stability" |
| `parity_assessment` | `relations.parity_note` | Pass through verbatim; "n/a" if absent |
| `appear_disappear_assessment` | `appear_disappear` | Count appeared+disappeared; flag dominant_shift if present |

---

## 5. Usage example

```python
from output_views.apps.pages.timeline_matrix_blob import build_interpretation_blob_v1, run_supervisor_checklist

blob = build_interpretation_blob_v1(
    session_id="1-11-09-2023",
    payload=matrix_payload,     # from /inspector/<id>/timeline-matrix endpoint
    tier="T3",
    corpus_layer="tfp_corpus_ru",
)

# Deterministic (no LLM)
result = run_supervisor_checklist(blob, use_llm=False)

# LLM mode
result = run_supervisor_checklist(blob, use_llm=True, llm_call_fn=my_llm_fn)
```

---

SIGNED: Architecture (Ethan) | Hesperia TMX prompt pack | 2026-05-11 | T3 supervisor stance + diff slots
