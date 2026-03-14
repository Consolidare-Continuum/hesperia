# Deploy a build from scratch

How to **deploy** the built artifacts (CLI binary and/or API container) on a target machine. To build first, see [BUILD_FROM_SCRATCH.md](BUILD_FROM_SCRATCH.md).

---

## 1. What you need from the build

After `./build_shipping.sh all` (or `cli` / `api`) you have:

| Artifact | Location | Use |
|----------|----------|-----|
| **CLI (onefile)** | `dist/hesperia-cli.bin` | Single executable; copy and run |
| **CLI (standalone)** | `dist/hesperia-cli/` | Directory with binary + libs; copy whole dir |
| **API image** | `release/hesperia-api-image.tar` | Docker image tarball; load then run |
| **Manifest** | `release/manifest.json` | Version, commit, build timestamp |
| **Checksums** | `release/checksums.txt` | SHA256 of binary and image (optional verify) |

Copy the files you need to the deploy host (e.g. SCP, USB, CI artifact). No Python or repo required on the target for CLI or API.

---

## 2. Deploy the CLI

**Option A — Onefile binary (simplest)**

1. Copy the binary to the target:
   ```bash
   scp dist/hesperia-cli.bin user@host:/opt/hesperia/hesperia-cli.bin
   ```
2. On the target, make it executable and run:
   ```bash
   chmod +x /opt/hesperia/hesperia-cli.bin
   /opt/hesperia/hesperia-cli.bin analyze --text "Your text here."
   /opt/hesperia/hesperia-cli.bin --version
   ```

**Option B — Standalone directory**

1. Copy the whole directory:
   ```bash
   scp -r dist/hesperia-cli user@host:/opt/hesperia/
   ```
2. On the target, run the binary inside that dir (exact name may be `hesperia-cli` or under a `.dist` subdir; see build output):
   ```bash
   /opt/hesperia/hesperia-cli/hesperia-cli analyze --text "Your text here."
   ```

**CLI commands:** `analyze`, `compare`, `batch-analyze`. Use `--out path.json` to write output to a file. See [release/EVALUATOR_GUIDE.md](../release/EVALUATOR_GUIDE.md).

---

## 3. Deploy the API (Docker)

1. Copy the image tarball to the target:
   ```bash
   scp release/hesperia-api-image.tar user@host:/opt/hesperia/
   ```

2. On the target, load the image and run the container:
   ```bash
   docker load -i /opt/hesperia/hesperia-api-image.tar
   docker run -d -p 8080:8000 -e HESPERIA_LICENSE_SKIP=1 --name hesperia-api hesperia-api:latest
   ```

   - `-p 8080:8000` — host port 8080 → container port 8000 (change as needed).
   - `HESPERIA_LICENSE_SKIP=1` — skip license check (e.g. evaluator / dev). Omit in production if you use a real license.
   - `--name hesperia-api` — optional; handy for `docker stop hesperia-api`.

3. Verify:
   ```bash
   curl http://localhost:8080/health
   curl http://localhost:8080/version
   curl -X POST http://localhost:8080/analyze -H "Content-Type: application/json" -d '{"text": "sample"}'
   ```

**Restart / stop:**

```bash
docker stop hesperia-api
docker start hesperia-api
```

---

## 4. Environment variables (API)

| Variable | Purpose | Example |
|----------|---------|---------|
| **HESPERIA_LICENSE_SKIP** | Skip license check | `1` for eval/dev |
| **HESPERIA_API_HOST** | Bind address | `0.0.0.0` (default) |
| **HESPERIA_API_PORT** | Bind port (in container) | `8000` (default) |
| **HESPERIA_RATE_LIMIT** | Requests per minute | `60` (default) |
| **HESPERIA_ASSETS_ROOT** | Override path to lexicon/assets | `/app/lexicon/curated` |
| **HESPERIA_SCHEMA_SHA256** | Optional schema integrity check | hex from `release/schema_sha256.txt` |

Full list: [docs/governance/RUNTIME_ENV_VARS_v1.md](governance/RUNTIME_ENV_VARS_v1.md).

**Example with custom port and rate limit:**

```bash
docker run -d -p 9000:8000 \
  -e HESPERIA_LICENSE_SKIP=1 \
  -e HESPERIA_RATE_LIMIT=120 \
  --name hesperia-api hesperia-api:latest
```

Then use port 9000 on the host: `curl http://localhost:9000/health`.

---

## 5. Verify deployment

| Check | CLI | API |
|-------|-----|-----|
| Version | `./hesperia-cli.bin --version` | `GET /version` |
| Health | N/A | `GET /health` → `{"status": "ok"}` |
| Analyze | `./hesperia-cli.bin analyze --text "test"` | `POST /analyze` with `{"text": "test"}` |

Optional: compare checksums on the deploy host with `release/checksums.txt` (e.g. `sha256sum hesperia-cli.bin`, `sha256sum hesperia-api-image.tar`).

---

## 6. Minimal “from scratch” deploy (copy-paste)

**CLI only (onefile):**

```bash
# On build host
./build_shipping.sh cli
# Copy dist/hesperia-cli.bin to target, then on target:
chmod +x hesperia-cli.bin
./hesperia-cli.bin analyze --text "Hello."
./hesperia-cli.bin --version
```

**API only:**

```bash
# On build host
./build_shipping.sh api
# Copy release/hesperia-api-image.tar to target, then on target:
docker load -i hesperia-api-image.tar
docker run -p 8080:8000 -e HESPERIA_LICENSE_SKIP=1 hesperia-api:latest
# In another terminal:
curl http://localhost:8080/health
curl -X POST http://localhost:8080/analyze -H "Content-Type: application/json" -d '{"text": "Hello."}'
```

---

## 7. Further reading

- **Usage (commands, endpoints, limits):** [release/EVALUATOR_GUIDE.md](../release/EVALUATOR_GUIDE.md)
- **Build:** [BUILD_FROM_SCRATCH.md](BUILD_FROM_SCRATCH.md)
- **Run from source:** [RUN_FROM_SCRATCH.md](RUN_FROM_SCRATCH.md)
