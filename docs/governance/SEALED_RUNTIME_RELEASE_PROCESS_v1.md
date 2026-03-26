# Sealed runtime release process v1

**Status:** Canonical  
**Purpose:** Exact command sequence to complete the sealed runtime release cleanly. Follow in order.

---

## 1. Build the sealed runtime artifacts

**Master command (recommended):** Run the wrapper to build and run the gate in one step:

```bash
./release_sealed_runtime.sh
```

This runs `./build_shipping.sh all` then `./tools/run_release_gate.sh` and prints `SEALED RUNTIME BUILD COMPLETE` and `READY FOR MANUAL GATE`. It prevents skipping the gate.

**Or run build only:**

```bash
./build_shipping.sh all
```

**Expected results:**
- dist/hesperia-cli.bin
- release/hesperia-api-image.tar
- release/manifest.json
- release/checksums.txt

If any of these are missing, the build must be fixed before continuing.

**Regression test set (recommended before gate):** Run `pytest tests/test_sealed_runtime_regression.py -v` to verify deterministic output, schema validity, and no forbidden keys on the fixed corpus in `tests/sealed_runtime_inputs/`. See MAINTENANCE_GUIDELINE_v1.md.

---

## 2. Run the automated release gate

Execute:

```bash
./tools/run_release_gate.sh
```

**Expected output:**
```
[PASS] Import boundary
[PASS] Projection (no forbidden terms in CLI output)
[PASS] Binary reflection scan
[PASS] Container inspection
[PASS] Manifest verification
==============================================
HESPERIA SEALED RUNTIME: PASS
```

If any line fails:
1. Fix the issue
2. Rebuild (./build_shipping.sh all)
3. Rerun the gate (./tools/run_release_gate.sh)

---

## 3. Perform manual gate steps

These are intentionally manual because they require judgment. See SEALED_RUNTIME_RELEASE_GATE_v1.md for full detail.

### Step 5 — Clean machine test

Use a fresh Linux environment (VM or container, no repo).

**CLI:**
```bash
./hesperia-cli.bin analyze --text "$(cat examples/sample.txt)"
```
(If no sample.txt, use: `./hesperia-cli.bin analyze --text "sample policy text"`.)

**API:**
```bash
docker load -i hesperia-api-image.tar
docker run -p 8080:8000 hesperia-api
```
Then in another terminal:
```bash
curl -X POST http://localhost:8080/analyze \
  -H "Content-Type: application/json" \
  -d '{"text":"sample policy text"}'
```

**Verify:**
- Projected output only (no sphere, hex, topology, layer, bridge, area11, family240, etc.)
- No debug files created
- No stack traces revealing internals

### Step 6 — Reflection audit

Review the bundle as an external evaluator would.

**Confirm the bundle does not reveal:**
- geometry
- layer count
- dictionary generation
- propagation algorithm
- reserved structures

**From:** binary strings, CLI help, API responses, schemas, examples, README, container filesystem.

**Only the product concept should be visible:** *structural measurement engine*.

### Step 7 — Performance sanity

Run a batch test (~100 texts).

**Example:**
```bash
./hesperia-cli.bin batch-analyze --raw_text examples/batch.json
```
(or use --texts with a script that feeds ~100 texts).

**Verify:**
- Runtime scales roughly linearly
- No memory growth across runs
- API rate limiting returns 429 when exceeded

### Step 8 — Final evaluation bundle test (recommended)

Run the exact scenario evaluators will use: unpack bundle, run CLI, run API, send 50–100 requests, verify outputs, shut down and restart container. See **docs/audit/FINAL_EVALUATION_BUNDLE_TEST_v1.md**. Confirms no hidden runtime dependencies on the repo.

---

## 4. Verify manifest hashes

Confirm hashes match artifacts:

```bash
sha256sum dist/hesperia-cli.bin
sha256sum release/hesperia-api-image.tar
```

Both must match the values in **release/checksums.txt**.

---

## 5. Mark release readiness

Once all checks pass (automated gate + manual steps 5–7 + manifest verification):

| Item | Status |
|------|--------|
| Sealed runtime status | PASS |
| Functional integrity | PASS |
| Reflection resistance | PASS |
| Release readiness | TRUE |

At that point the evaluator bundle can be shipped.

---

## What reviewers will receive

The final bundle must contain **only**:

- hesperia-cli.bin
- hesperia-api-image.tar
- examples/
- assets/public/
- release/README.md (or README.md)
- manifest.json
- checksums.txt

**Nothing else.**

---

## Final note

The protection of the model does not come primarily from compilation. It comes from the architecture already implemented:

1. **Service façade boundary** — Entry points use only core.services.
2. **Projection layer filtering** — Last step before serialization; strips internal terms.
3. **Sealed runtime packaging** — Binary and container add reverse-engineering friction.

The binary/container layers simply add friction, which is sufficient for an accelerator evaluation context.

---

---

## Final assessment

From a systems engineering perspective, the architecture has **four strong protection layers**:

1. **Service façade boundary** — Entry points use only core.services.
2. **Projection layer** — Last step before serialization; strips internal terms.
3. **Sealed runtime build** — Binary and container; no source or internal docs in bundle.
4. **Release gate verification** — Automated + manual checks before ship.

Together they prevent architectural reconstruction, geometry inference, layer discovery, and topology discovery, while still allowing evaluators to judge product behavior. This is the right balance for accelerator, VC demo, expert evaluation, and pilot customers.

**Bottom line:** You are ready to produce the first evaluator bundle once `./release_sealed_runtime.sh` (or `./build_shipping.sh all` + `./tools/run_release_gate.sh`) passes and manual steps complete. At that point the runtime is **sealed**, **audited**, and **ship-ready**.

---

---

## Related governance

| Document | Purpose |
|----------|---------|
| **SHIPPING_PATH_POLICY_v1.md** | Only `./release_sealed_runtime.sh` + PASS may ship; manual builds are non-release. |
| **PUBLIC_API_SURFACE_FREEZE_v1.md** | Frozen CLI/API; changes require surface version bump. |
| **PROJECTION_SERIALIZATION_CHAIN_v1.md** | All serialization: projection → schema_guard → serializer; no bypass. |
| **EVALUATOR_PROMISE_v1.md** | Guarantees: reproducible, deterministic, no internal exposure, stable schema. |
| **MAINTENANCE_GUIDELINE_v1.md** | How to add features and keep the release process identical. |

---

*Process version: v1. See SEALED_RUNTIME_RELEASE_GATE_v1.md for step-by-step criteria and SEALED_RUNTIME_FINAL_CLOSURE_CHECKLIST_v1.md for the full checklist. Bundle layout: RELEASE_ARTIFACT_LAYOUT_v1.md.*
