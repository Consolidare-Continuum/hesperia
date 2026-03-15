# HESPERIA Testing Phase — TFP Kernberg, Russian, Session Transcripts

**Domain:** TFP (Transference-Focused Psychotherapy) / Kernberg theories  
**Language:** Russian  
**Scope:** Run session transcripts through the model and receive structural analysis results.

---

## 1. Input format: session transcripts

Transcripts can be supplied as JSON in one of these forms:

- **List of strings** — one text per session/segment:
  ```json
  [ "текст сессии 1...", "текст сессии 2..." ]
  ```
- **Object with `texts` key** — same as above, named:
  ```json
  { "texts": [ "текст 1", "текст 2" ] }
  ```
- **Object with `sessions` key** — each item has `session_id` and `text` (optional metadata):
  ```json
  {
    "sessions": [
      { "session_id": "s001", "text": "текст первой сессии..." },
      { "session_id": "s002", "text": "текст второй сессии..." }
    ]
  }
  ```

Example files:
- `assets/testing/tfp_kernberg/session_transcripts_example.json` — Russian TFP sessions (use with Russian lexicon when available).
- `assets/testing/tfp_kernberg/session_transcripts_smoke_english.json` — English snippets for smoke test with default assets.

---

## 2. Running analysis

### CLI (batch, recommended for transcripts)

From repo root, with default assets (lexicon/curated). Use the **English smoke** file to get results without a Russian lexicon:

```bash
python3 -m runtime.shipping.cli_main batch-analyze \
  --input assets/testing/tfp_kernberg/session_transcripts_smoke_english.json \
  --out results/tfp_kernberg_sessions.json
```

For Russian transcripts (once Russian assets are under `--assets`):

```bash
python3 -m runtime.shipping.cli_main batch-analyze \
  --input assets/testing/tfp_kernberg/session_transcripts_example.json \
  --out results/tfp_kernberg_sessions.json
```

Using a custom assets root (e.g. Russian/TFP-specific lexicon when available):

```bash
python3 -m runtime.shipping.cli_main batch-analyze \
  --assets path/to/your/lexicon \
  --input path/to/transcripts.json \
  --out results/out.json
```

### API (batch)

```bash
curl -X POST http://localhost:8080/batch-analyze \
  -H "Content-Type: application/json" \
  -d '{"texts": ["текст сессии 1", "текст сессии 2"]}'
```

Or with sessions format: send a body that your client converts to `{"texts": [...]}` (list of `text` fields).

---

## 3. Output

Each run returns a **list of public structural analysis results**, one per input text:

- **macro_domain_vector** / **dominant_macro_domain** — structural emphasis over 10 public areas  
- **policy_family_counts** / **dominant_policy_family** — family-level distribution  
- **propagated_macro_domain_vector** — after topology propagation  
- **usf** — Universal Structural Fingerprint (if enabled)  
- **L7** — propagation diagnostics; **L9** — interpretation metrics  

For session-level analysis, map list index (or `session_id` if you keep it in your wrapper) to each result.

---

## 4. Language and domain notes

- **Russian:** Current default assets are English-oriented (lexicon/curated). For Russian TFP transcripts, either:
  - Use Russian-capable or multilingual Dict A/B and surface map under `--assets`, or  
  - Run with existing assets and treat results as structural only (coverage may be partial until Russian lexicon is in place).
- **TFP / Kernberg:** Domain is reflected by the ontology (policy families, macro domains). A dedicated TFP/Kernberg profile or asset set can be pointed at via `--assets` and/or structure profiles when available.

---

## 5. Quick check (single text)

```bash
python3 -m runtime.shipping.cli_main analyze \
  --text "Пример текста сессии на русском." \
  --out results/single.json
```

---

## 6. File layout (suggested)

```
assets/testing/tfp_kernberg/
  session_transcripts_example.json   # example input
  (optional) ru_lexicon/             # when Russian assets are added

results/
  tfp_kernberg_sessions.json         # batch-analyze --out
```

---

*Testing phase: TFP Kernberg, language Russian. Run session transcripts via batch-analyze and use the output JSON for structural metrics per session.*
