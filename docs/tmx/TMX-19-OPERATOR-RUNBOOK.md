# TMX-19: Operator Runbook — Open Matrix, Regenerate Bundle, Tiers

**Owner**: Marcus (operator runbook)  
**Status**: 2026-05-11 — runbook complete.

---

## 1. Open the matrix viewer

```bash
# From hesperia repo root on prichindel:
cd /data/hesperia/hesperia/output_views/hex_matrix_viewer

# Serve dist/ locally (already built):
python3 -m http.server 8888 --directory dist/

# OR rebuild + serve:
NODE=$(find /home/igareosh/.cursor-server -name 'node' -type f | head -1)
export PATH=$(dirname $NODE):$PATH
node ./node_modules/.bin/vite preview --port 8888
```

Open: `http://localhost:8888/`

Load a session dataset: append `?data=<url-to-json>` where the JSON matches the `Dataset` schema (see `src/schema/hexSchema.js`).

## 2. Regenerate the mock bundle (dev only)

```bash
# Rebuild with Cursor's Node (prichindel):
NODE=$(find /home/igareosh/.cursor-server -name 'node' -type f | head -1)
export PATH=$(dirname $NODE):$PATH
cd /data/hesperia/hesperia/output_views/hex_matrix_viewer
node ./node_modules/.bin/vite build
# Output: dist/assets/index-*.js + dist/index.html
```

## 3. Tier context for loaded datasets

| Tier | Meaning | Display note |
|------|---------|-------------|
| T1 | Canonical session bundle | Full drift/parity trust |
| T2 | Derived / estimated | Drift bars shown; parity note flagged as estimated |
| T3 | Research / mock | RelationsPanel shows "mock" watermark (RU: `src/i18n/ru.js` → `tiers.T3`) |

To set tier in the interpretation blob:
```js
// In dataset JSON (optional metadata field):
{ "tier": "T2", "frames": [...], "relations": {...}, "appear_disappear": {...} }
```

## 4. Gold fixture smoke test

```bash
cd /data/hesperia/hesperia
python3 -m pytest tests/hex_matrix/test_hex_matrix_fixture.py -v
# Expected: 5 passed
```

## 5. TFP corpus compose (Tersagor / agent)

```bash
curl -s -X POST http://localhost:8010/inspector/tfp-corpus/compose \
  -H "Authorization: Bearer $HESPERIA_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"session_id":"test-001","iteration_labels":["iteration 1","iteration 2"],"query":"dominance shift","n_results":3}' | python3 -m json.tool
# corpus_available=false until tfp_corpus_ru ingested into chroma-new
```

SIGNED: DevOps (Marcus) | Hesperia TMX-19 operator runbook | 2026-05-11 | matrix viewer + bundle + tiers
