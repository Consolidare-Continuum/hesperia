# Hesperia Engine Dynamics — **v0.5.0** sealed build record

**Built:** 2026-03-18 (UTC)  
**Product:** Hesperia Engine Dynamics — Canonical Release v0.5

## Commands run

```bash
./build_shipping.sh all          # import boundary + sealing scan + Docker API image + manifest
./tools/run_release_gate.sh      # HESPERIA SEALED RUNTIME: PASS
```

## Artifacts

| Artifact | Note |
|----------|------|
| `release/hesperia-api-image.tar` | `docker load -i …` → `hesperia-api:latest` |
| `release/manifest.json` | version, git commit, checksums path |
| `release/checksums.txt` | SHA256 of image tar |
| `release/schema_sha256.txt` | public output schema fingerprint |
| `dist/hesperia-cli.bin` | **Not produced** (Nuitka absent on builder); use `python3 -m runtime.shipping.cli_main` |

## Manifest snapshot

- **version:** `0.5.0`
- **git_commit:** see `release/manifest.json` at build time
- **Image ID (example):** `471f939b2f92…`

## Verify API image

```bash
docker load -i release/hesperia-api-image.tar
docker run -p 8000:8000 -e HESPERIA_LICENSE_SKIP=1 hesperia-api:latest
curl -s http://127.0.0.1:8000/health
```

## Git tags (sync to origin)

```bash
# Both tags point to the same commit (semver + product name)
git tag -a v0.5.0 -m "Hesperia Engine Dynamics v0.5.0"
git tag -a hesperia-engine-dynamics-v0.5.0 -m "Hesperia Engine Dynamics — Canonical Release v0.5.0"
git push origin v0.5.0 hesperia-engine-dynamics-v0.5.0
```

---

*Sealed runtime gate passed on this tree after build.*

---

## Task 5 — `release/v0.5.0` audit package

Regenerate the **manifest + checksums + frozen E2E reference** (and optional full pytest) with:

```bash
export HESPERIA_RELEASE_BUILD_TIMESTAMP=2026-03-19T12:00:00Z   # bitwise-stable reference JSON
python3 tools/release/build_release_audit_v0_5_0.py              # full tests
# python3 tools/release/build_release_audit_v0_5_0.py --quick    # fast iteration
```

See **`release/v0.5.0/README.md`** for acceptance criteria and tagging instructions.

Artifacts now include **`audit_report.json`** (master pass/fail), **`determinism_report.json`** (triplicate hash), **`schema_validation_report.json`** (jsonschema + leak scan), and the canonical raw_text **`tests/fixtures/release_v0_5_0/canonical_input.txt`**.
