# Sealed runtime release gate v1

**Status:** Mandatory before shipping  
**Purpose:** Only when all steps pass may the evaluator bundle be shipped.  

**Single shipping path:** No artifact may be distributed unless produced by `./release_sealed_runtime.sh` and the gate summary is **HESPERIA SEALED RUNTIME: PASS**. Anything built manually is non-release. See **SHIPPING_PATH_POLICY_v1.md**.

**Canonical command sequence:** See **SEALED_RUNTIME_RELEASE_PROCESS_v1.md** for the exact build → gate → manual steps → manifest verify → release readiness flow. Closure decision: sealed runtime status PASS, functional integrity PASS, reflection resistance PASS, release readiness TRUE.

---

## Step 0 — Build artifacts

**Recommended:** Run the master command (build + automated gate in one step):

```bash
./release_sealed_runtime.sh
```

Or build only:

```bash
./build_shipping.sh all
```

**Expected artifacts:**
- dist/hesperia-cli.bin
- release/hesperia-api-image.tar
- release/checksums.txt
- release/manifest.json

If the build script fails, the release gate stops. Do not proceed.

---

## Step 1 — Projection enforcement

**CLI test:**
```bash
./dist/hesperia-cli.bin analyze --text "$(cat examples/sample.txt 2>/dev/null || echo 'test policy statement')"
```

**API test:**
```bash
docker load -i release/hesperia-api-image.tar
docker run -p 8080:8000 hesperia-api &
# wait for startup, then:
curl -s -X POST http://localhost:8080/analyze \
  -H "Content-Type: application/json" \
  -d '{"text":"test policy statement"}'
```

**Verify:** Outputs (CLI stdout, API response body) do **not** contain:
- sphere
- hex
- topology
- layer
- bridge
- area11
- family240
- coordinates
- vector3

Projection must be the last step before serialization.

**Pass:** No forbidden terms in any output. **Fail:** Fix projection/serialization path; re-run.

---

## Step 2 — Binary reflection scan

```bash
strings dist/hesperia-cli.bin | grep -iE "sphere|hex|topology|bridge|layer"
```

**Expected:** (no output)

If anything appears: rename symbols, rebuild binary, repeat scan until clean.

---

## Step 3 — Container inspection

```bash
docker run -it hesperia-api sh
# Inside container, inspect filesystem.
```

**Allowed directories only:**
- /app/runtime
- /app/core
- /app/lexicon
- /app/assets

**Forbidden:**
- docs/
- tests/
- debug/
- legacy/
- specs/
- build tools (gcc, make, etc.)

**Also confirm:** No compiler, no pip cache, no git.

**Pass:** Only allowed dirs; no forbidden content. **Fail:** Adjust Dockerfile.shipping and rebuild image.

---

## Step 4 — Release bundle inspection

After packaging the bundle (e.g. hesperia-release.tar):

```bash
tar -tf hesperia-release.tar
```

**Allowed files only:**
- hesperia-cli.bin
- hesperia-api-image.tar
- examples/
- assets/public/
- release/README.md
- manifest.json
- checksums.txt

Anything else → reject bundle. Repackage until only allowed contents remain.

---

## Step 5 — Clean machine dry run

Use a fresh Linux VM or container (no repo).

- **CLI:** `./hesperia-cli.bin analyze --text "$(cat example.txt)"`
- **API:** `docker load -i hesperia-api-image.tar`, `docker run -p 8080:8000 hesperia-api`, then `curl -X POST http://localhost:8080/analyze ...`

**Expected:**
- Correct projected outputs (no internal terms).
- No new files created (unless --out used).
- No debug logs or stack traces revealing internals.

**Pass:** Bundle works; output projected; no leaks. **Fail:** Fix and re-test on clean machine.

---

## Step 6 — Reflection audit

Evaluate the bundle as if you were an external reviewer.

**Check whether the following can be inferred:**
- internal geometry
- number of layers
- dictionary construction
- propagation algorithm
- reserved structure

If **any** can be deduced from binary strings, CLI help, schema, examples, README, or container layout → **the release fails.**

Remove or reword the leaking channel; re-run reflection audit until none of the above are inferable.

---

## Step 7 — Performance sanity

**CLI batch test:**
```bash
./hesperia-cli.bin batch-analyze --raw_text dataset.json
```
or scripted test with ~100 texts.

**Check:**
- Runtime roughly linear in batch size.
- No memory increase across runs (no leak).
- API rate limit returns 429 when exceeded.

**Pass:** Linear scaling; no leak; rate limit enforced. **Fail:** Fix and re-test.

---

## Step 8 — Manifest verification

**Check:**
- release/manifest.json exists and lists version, artifacts, entry_points, checksums_file.
- release/checksums.txt exists.

**Verify hashes:**
```bash
sha256sum dist/hesperia-cli.bin
sha256sum release/hesperia-api-image.tar
```
Compare to entries in release/checksums.txt. They must match.

**Pass:** Manifest and checksums present; hashes match. **Fail:** Regenerate in build script; re-run build and verify.

---

## Step 9 — Closure decision

When **all** steps 0–8 pass, mark:

| Item | Status |
|------|--------|
| Sealed runtime status | PASS |
| Functional integrity | PASS |
| Reflection resistance | PASS |
| Release readiness | TRUE |

**Only then** ship the evaluator bundle.

---

## Automated gate (optional)

Run:

```bash
./tools/run_release_gate.sh
```

The script executes: import-boundary check, projection test (CLI), binary scan, container scan (if image exists), manifest verification. It prints a single summary:

**HESPERIA SEALED RUNTIME: PASS** or **HESPERIA SEALED RUNTIME: FAIL**

Use this to reduce human error in the release decision. A full gate still requires clean-machine test, reflection audit, and performance sanity (steps 5–7) which may be manual.

---

---

## Practical observation

The architecture already contains the three mechanisms that matter most:

1. **Service façade boundary** — Evaluator entry points use only core.services.
2. **Projection layer** — Last step before serialization; strips internal terms (including keys containing "bridge", "layer", etc.).
3. **Sealed runtime packaging** — Binary and container add reverse-engineering friction.

These protect the conceptual model far more effectively than obfuscation alone. The binary and container layers mainly add friction, which is the right target for an accelerator review environment.

---

*Gate version: v1.*
