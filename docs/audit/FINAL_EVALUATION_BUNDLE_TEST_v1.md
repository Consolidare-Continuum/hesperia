# Final evaluation bundle test v1

**Purpose:** Run the exact scenario evaluators will use. Confirms no hidden runtime dependencies on the repo.

---

## Prerequisites

- Unpacked evaluator bundle (no source tree).
- Linux host with Docker (for API).
- Binary: `hesperia-cli.bin`. Image: `hesperia-api-image.tar`.

---

## Steps

### 1. Unpack bundle

```bash
tar -xf hesperia-evaluator-bundle.tar
cd hesperia-evaluator-bundle
```

Confirm layout matches `RELEASE_ARTIFACT_LAYOUT_v1.md`: `hesperia-cli.bin`, `hesperia-api-image.tar`, `examples/`, `assets/public/`, `manifest.json`, `checksums.txt`, `README.md`, `EVALUATOR_GUIDE.md`. No other files.

### 2. Run CLI

```bash
chmod +x hesperia-cli.bin
./hesperia-cli.bin --version
./hesperia-cli.bin analyze --text "Sample policy or statement."
./hesperia-cli.bin compare --text1 "First." --text2 "Second."
```

Expected: version lines; JSON output only; no errors; no files created except with explicit `--out`.

### 3. Run API

```bash
docker load -i hesperia-api-image.tar
docker run -d -p 8080:8000 -e HESPERIA_LICENSE_SKIP=1 --name hesperia-api hesperia-api:latest
# wait a few seconds for startup
curl -s http://localhost:8080/health
curl -s http://localhost:8080/version
curl -s -X POST http://localhost:8080/analyze -H "Content-Type: application/json" -d '{"text":"test"}'
```

Expected: `{"status":"ok"}`; version JSON; analysis JSON. No stack traces or internal module names in responses.

### 4. Send ~50–100 requests

```bash
for i in $(seq 1 50); do
  curl -s -X POST http://localhost:8080/analyze -H "Content-Type: application/json" -d "{\"text\":\"request $i\"}" > /dev/null
done
```

Optional: run 100 requests; check rate limit (e.g. 61st request in same minute returns 429). Verify outputs remain projected (no forbidden terms).

### 5. Verify outputs

- All analysis responses: JSON with public vocabulary only (no sphere, hex, topology, bridge, layer, area11, family240, etc.).
- Error responses: only `{"error": "internal_processing_error"}` or validation/rate-limit messages; no tracebacks, no `core.services`, `runtime.shipping`, `analysis_service`.

### 6. Shut down and restart container

```bash
docker stop hesperia-api
docker rm hesperia-api
docker run -d -p 8080:8000 -e HESPERIA_LICENSE_SKIP=1 --name hesperia-api hesperia-api:latest
curl -s http://localhost:8080/health
```

Expected: after restart, API responds again. No dependency on host filesystem or repo.

### 7. Cleanup

```bash
docker stop hesperia-api
docker rm hesperia-api
```

---

## Pass criteria

- CLI and API run without the repo or source tree.
- 50–100 requests complete; outputs are deterministic (e.g. same input → same output).
- No forbidden terms in any response; no module paths or tracebacks in errors.
- Container restart works; no hidden dependencies.

---

*Test version: v1. See SEALED_RUNTIME_RELEASE_PROCESS_v1.md and EVALUATOR_GUIDE.md.*
