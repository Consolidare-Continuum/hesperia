# HESPERIA v0.5 — Prove dense is live (runbook)

Run on the API server as the **same user the service runs under** (e.g. igareosh).

## 1. Prove chroma venv has deps and centroids

```bash
/data/chroma/venv/bin/python -c "import sentence_transformers, torch; print('OK', sentence_transformers.__version__, torch.__version__)"
# Expected: OK 2.x.x 2.x.x

/data/chroma/venv/bin/python -c "import json; p='/data/workspaces/cursor/CLIENTS/hesperia/hesperia_lex/frozen/FAMILY_CENTROIDS_v0_5.json'; print('exists', __import__('os').path.exists(p)); print('len', len(json.load(open(p))))"
# Expected: exists True, len 288
```

If either fails:
- **A)** Install into chroma venv: `/data/chroma/venv/bin/pip install sentence-transformers torch`
- **B)** Point service to build venv: change `ExecStart` in `hesperia-api.service` to use `CLIENTS/hesperia/.venv_v040_build/bin/uvicorn` and ensure `WorkingDirectory` + `PYTHONPATH` point at cursor repo.

## 2. Prove dense through public API (both must be 200)

Set key: `export HESPERIA_API_KEY='...'` (or `source /etc/hesperia/hesperia-api.env` if readable).

**One-liner (both curls; expect 200 200):**
```bash
a=$(curl -s -o /dev/null -w "%{http_code}" -X POST https://hesperia.prichindel.com/hesperia/analyze -H "Authorization: Bearer $HESPERIA_API_KEY" -H "Content-Type: application/json" -d '{"text":"randomwordthatneverexisted"}'); b=$(curl -s -o /dev/null -w "%{http_code}" -X POST https://hesperia.prichindel.com/hesperia/analyze -H "Authorization: Bearer $HESPERIA_API_KEY" -H "Content-Type: application/json" -d '{"text":"architecture and symbolism influence belief systems"}'); echo "$a $b"; [ "$a" = "200" ] && [ "$b" = "200" ] && echo "PASS" || echo "FAIL"
```

**Single curls:**
```bash
# Unknown token — must 200 (dense); 400 = sparse vacuum
curl -s -w "\n%{http_code}" -X POST https://hesperia.prichindel.com/hesperia/analyze -H "Authorization: Bearer $HESPERIA_API_KEY" -H "Content-Type: application/json" -d '{"text":"randomwordthatneverexisted"}'

# Former vacuum — must 200
curl -s -w "\n%{http_code}" -X POST https://hesperia.prichindel.com/hesperia/analyze -H "Authorization: Bearer $HESPERIA_API_KEY" -H "Content-Type: application/json" -d '{"text":"architecture and symbolism influence belief systems"}'
```

Both must be `200`. If either is 400, dense is not live or centroids aren’t loading.

## 3. Don’t run shadow comparisons until core consumes seed/vector

Shadow has no effect until the pipeline core takes `family_vector` (or top-K + weights) as initial state and shadow perturbs that. See task: `TASK__wire_family_vector_into_core_shadow_perturbs.md`.
