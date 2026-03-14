# HESPERIA release bundle

After running `./release_sealed_runtime.sh` or `./build_shipping.sh all` (or `cli` / `api`), this directory may contain:

- **hesperia-api-image.tar** — Docker image for the API (load with `docker load -i hesperia-api-image.tar`).
- **manifest.json** — Version, git commit, build timestamp, included artifacts, checksums file reference.
- **checksums.txt** — SHA256 checksums of the CLI binary and image tar.
- **EVALUATOR_GUIDE.md** — Short guide: what HESPERIA does, how to run CLI/API, what outputs mean, what to test (~2 pages).

Frozen bundle layout: see `docs/governance/RELEASE_ARTIFACT_LAYOUT_v1.md`. No other files in the evaluator bundle.

## Quickstart (evaluator)

### CLI
- Use the binary from `dist/hesperia-cli.bin` (onefile) or run from `dist/hesperia-cli/`.
- Commands: `analyze`, `compare`, `batch-analyze`. Example: `./hesperia-cli.bin analyze --text "your text"`.

### API
- Load image: `docker load -i release/hesperia-api-image.tar`
- Run: `docker run -p 8000:8000 -e HESPERIA_LICENSE_SKIP=1 hesperia-api:latest`
- Endpoints: `POST /analyze`, `POST /compare`, `POST /batch-analyze`, `GET /health`, `GET /version`.

### Limitations
- No internal endpoints. No debug or layer views. Outputs are projected only (public vocabulary).
- Rate limiting applies (default 60 requests/minute per key). Max 100 texts per batch-analyze request.

## Package contents (what is included)

- One Linux CLI binary (Nuitka onefile or standalone).
- One Dockerized API image.
- Public schema and examples (see examples/ and assets/public if bundled).
- Quickstart and this README.
- Checksums and manifest.

## Excluded (not in the shipped artifact)

- Internal docs, specs history, debug tools, internal-review runners, full source tree. See SHIPPING_EXCLUSION_POLICY_v1.
