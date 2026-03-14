# Build HESPERIA from scratch

How to build the **shipping artifacts** (CLI binary, API Docker image, manifest) on a clean machine. For “run only” see [RUN_FROM_SCRATCH.md](RUN_FROM_SCRATCH.md). After building, see [DEPLOY_FROM_SCRATCH.md](DEPLOY_FROM_SCRATCH.md) to deploy the artifacts.

---

## 1. Same as run-from-scratch

Do the run-from-scratch steps first so the project runs and tests pass:

```bash
git clone https://github.com/Atomic-Commits-Team/hesperia.git
cd hesperia
python3 -m venv .venv
source .venv/bin/activate   # or .venv\Scripts\activate on Windows
pip install -r requirements.txt
python3 -m pytest tests/ -q   # optional but recommended
```

---

## 2. Build script (one command)

From the **repo root**:

```bash
./build_shipping.sh all
```

This runs, in order:

1. **Import-boundary check** — `python3 tools/check_import_boundary.py` (fail → build stops)
2. **Sealing scan** — `tools/sealing_scan.py` if present (forbidden terms in public tree; fail → build stops)
3. **Version file** — Writes `runtime/shipping/version_info.py` (VERSION, COMMIT, BUILD)
4. **CLI build** — Nuitka standalone + onefile (if `nuitka3` is available)
5. **API build** — Docker image (if `docker` is available)
6. **Manifest** — Generates `release/manifest.json`, `release/checksums.txt`, `release/schema_sha256.txt`

Outputs:

- **CLI:** `dist/hesperia-cli/` (standalone dir), `dist/hesperia-cli.bin` (onefile binary)
- **API:** `release/hesperia-api-image.tar` (Docker image saved as tarball)
- **Release:** `release/manifest.json`, `release/checksums.txt`, `release/schema_sha256.txt`

---

## 3. Build only CLI or only API

```bash
./build_shipping.sh cli    # checks + Nuitka CLI + manifest
./build_shipping.sh api    # checks + Docker API + manifest
./build_shipping.sh manifest   # only regenerate manifest/checksums
```

If `nuitka3` is missing, CLI is skipped (no failure). If `docker` is missing, API is skipped.

---

## 4. Prerequisites for full build

| Want | Need |
|------|------|
| **CLI binary** | `nuitka3` (`pip install nuitka`), `strip` (binutils, usually installed) |
| **API image** | Docker, `.dockerignore.shipping`, `Dockerfile.shipping` |
| **Manifest only** | Nothing extra; run `./build_shipping.sh manifest` |

Check:

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install nuitka
nuitka3 --version
docker --version
```

---

## 5. Nuitka CLI build (manual)

If you only want the CLI without running the full script:

```bash
# From repo root
pip install nuitka
./tools/build_nuitka_cli.sh
```

Produces:

- `dist/hesperia-cli/` — standalone directory (binary + shared libs)
- `dist/hesperia-cli.bin` — single executable (onefile)

Then strip and manifest are up to you, or run `./build_shipping.sh manifest` to refresh `release/`.

---

## 6. Full release flow (build + gate)

To build and run the **automated release gate** (import boundary, projection test, binary/container scans, manifest):

```bash
./release_sealed_runtime.sh
```

This runs:

1. `./build_shipping.sh all`
2. `./tools/run_release_gate.sh`

Gate passes → “HESPERIA SEALED RUNTIME: PASS” and “READY FOR MANUAL GATE”. Then follow manual steps in `docs/governance/SEALED_RUNTIME_RELEASE_PROCESS_v1.md`.

---

## 7. Docker API build (manual)

```bash
cp -f .dockerignore.shipping .dockerignore
docker build -f Dockerfile.shipping -t hesperia-api:latest .
# Optional: save image
mkdir -p release
docker save hesperia-api:latest -o release/hesperia-api-image.tar
```

---

## 8. Troubleshooting

| Issue | Fix |
|-------|-----|
| `nuitka3 not found` | `pip install nuitka`; use same Python as venv |
| `Import boundary check failed` | Fix imports so runtime only uses allowed modules; see `tools/check_import_boundary.py` |
| `Sealing scan failed` | Remove or reword forbidden terms in the public/shipping tree |
| `docker not found` | Install Docker or run `./build_shipping.sh cli` only |
| CLI binary missing after build | Check `dist/hesperia-cli/` or `dist/hesperia-cli.bin`; Nuitka may put the binary in a `.dist` subdir (the script renames it) |

---

## Quick reference

| Goal | Command |
|------|---------|
| Build everything (CLI + API + manifest) | `./build_shipping.sh all` |
| Build CLI only | `./build_shipping.sh cli` |
| Build API only | `./build_shipping.sh api` |
| Regenerate manifest only | `./build_shipping.sh manifest` |
| Build + release gate | `./release_sealed_runtime.sh` |
| Nuitka CLI by hand | `./tools/build_nuitka_cli.sh` |
