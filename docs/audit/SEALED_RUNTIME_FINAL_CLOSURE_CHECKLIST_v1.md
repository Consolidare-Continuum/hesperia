# Sealed runtime — final closure checklist v1

**Status:** Mandatory before release  
**Purpose:** Confirm the sealed evaluator runtime meets structural, projection, binary, container, bundle, clean-machine, reflection, performance, and manifest requirements. Run this checklist before shipping.

---

## 1. Structural verification

**Requirement:** All evaluator entry points use only the service façade.

**Allowed import path:**
- `runtime/shipping/*` → `core.services.analysis_service` (and `runtime.artifact_writer` for writes)
- No other compute imports allowed (no core.layers, core.attribution, sphere.execution_flow, etc.)

**Procedure:**
```bash
python3 tools/check_import_boundary.py
```

**Expected:** Exit code 0. No violations in runtime/shipping, runtime/execution_flow (non-excluded), runtime/runners, runtime/api, runtime/public_reports, runtime/artifact_writer.

**Pass:** Exit code 0.  
**Fail:** Fix imports so shipping and public runtime use only core.services and allowed modules; re-run until 0.

---

## 2. Projection enforcement test

**Requirement:** The projection layer is the last step before serialization. Output never contains internal terms.

**Procedure:**

- **CLI:** Run several inputs through the CLI, e.g.  
  `./dist/hesperia-cli.bin analyze --text "your text"`  
  or `./dist/hesperia-cli.bin analyze --text "$(cat examples/sample.txt)"` if sample exists.
- **API:** `curl -X POST http://localhost:8000/analyze -H "Content-Type: application/json" -d '{"text":"your text"}'`.

**Check:** Output (stdout or response body) must **never** contain:
- sphere
- hex
- topology
- layer
- bridge
- area11
- family240
- coordinates
- vector3

**Pass:** No matches in any CLI or API output.  
**Fail:** Fix projection or response path so internal terms are stripped before serialization.

---

## 3. Binary inspection

**Requirement:** No reflective terms in the shipped CLI binary string table.

**Procedure:**
```bash
strings dist/hesperia-cli.bin | grep -iE "sphere|hex|topology|bridge|layer"
```

**Expected:** No matches.

**Pass:** No matches.  
**Fail:** Remove or rename the source of the hit; rebuild and re-scan. If the hit is in a third-party dependency and not HESPERIA-specific, document and accept only if non-revealing.

---

## 4. Container inspection

**Requirement:** The API image contains only runtime essentials. No docs, tests, debug, legacy, or build tools.

**Procedure:**
```bash
docker run -it hesperia-api:latest sh
# Inside container:
ls -la /app
ls /app/runtime /app/core /app/lexicon /app/assets
# Confirm absence:
ls /app/docs 2>/dev/null && echo "FAIL: docs present" || true
ls /app/tests 2>/dev/null && echo "FAIL: tests present" || true
ls /app/debug 2>/dev/null && echo "FAIL: debug present" || true
ls /app/legacy 2>/dev/null && echo "FAIL: legacy present" || true
which gcc make 2>/dev/null && echo "FAIL: build tools present" || true
```

**Expected:** Only `/app/runtime`, `/app/core`, `/app/lexicon`, `/app/assets` (and expected subdirs). No docs/, tests/, debug/, legacy/, no gcc/make in PATH.

**Pass:** Container has only the four trees above; no docs, tests, debug, legacy, or build toolchain.  
**Fail:** Adjust Dockerfile.shipping and .dockerignore so the final stage does not copy excluded content.

---

## 5. Release bundle inspection

**Requirement:** The final bundle (e.g. hesperia-release.tar) contains only allowed contents.

**Procedure:**
```bash
tar -tf hesperia-release.tar
```

**Allowed contents only:**
- hesperia-cli.bin
- hesperia-api-image.tar
- examples/
- assets/public/
- release/README.md (or README.md)
- manifest.json
- checksums.txt

**Not allowed:** Full source tree, docs/internal, tests/, tools/, legacy/, any file not in the allowed list above.

**Pass:** Listed contents match the allowed set; nothing else.  
**Fail:** Repackage the bundle so it includes only the allowed items.

---

## 6. Clean machine test

**Requirement:** Bundle works on a fresh Linux environment without the repo. No new files written except by explicit request; no logs exposing internals.

**Procedure:**
- Use a clean VM or container (no HESPERIA repo).
- Copy only the release bundle. Unpack.
- **CLI:** `./hesperia-cli.bin analyze --text "$(cat example.txt)"` (or equivalent). Expect projected JSON on stdout; no internal terms.
- **API:** `docker load -i hesperia-api-image.tar`, then `docker run -p 8080:8000 hesperia-api:latest`. Then `curl -X POST http://localhost:8080/analyze -H "Content-Type: application/json" -d '{"text":"..."}'`.

**Expected:**
- Projected output only (no sphere, hex, topology, layer, bridge, area11, family240, etc.).
- No new files written (except e.g. --out if used).
- No logs that expose internal structure (no layer names, topology, propagation, bridge).

**Pass:** CLI and API run; output is projected; no stray files; logs are product-shaped.  
**Fail:** Fix output paths and logging so no internals leak; re-test on clean machine.

---

## 7. Reflection test

**Requirement:** An evaluator with only the bundle cannot infer the internal method.

**Question (pretend you are an evaluator):** From this bundle alone, can I infer:
- the internal geometry
- the number of layers
- the dictionary generation method
- the propagation algorithm
- the reserved structure

**Correct answer:** **No.**

**The only visible concept should be:** *structural measurement engine* (text → structural measurement → evidence + metrics).

**What Upcelerator reviewers will actually see:**
- A product that behaves like: **text → structural measurement → evidence + metrics.**
- They will **not** see: sphere model, hex topology, layer system, dictionary mechanics, propagation graph.

**Pass:** After reviewing bundle (CLI, API, examples, README, schema), the only reasonable conclusion is “structural measurement engine”; internal geometry, layer count, dictionary mechanics, propagation, and reserved structure are not inferable.  
**Fail:** Remove or reword any channel (outputs, help, schema, docs) that reveals the above; re-run reflection test.

---

## 8. Performance sanity

**Requirement:** Batch and API scale reasonably; no obvious memory growth; API rate limit respected.

**Procedure:**
- Run `./hesperia-cli.bin batch-analyze` with ~100 texts (e.g. via --raw_text or --texts). Observe runtime and memory (e.g. with `time` or a profiler).
- Call API at or above rate limit; confirm 429 and no crash.

**Check:**
- Runtime roughly linear in batch size; no memory growth that suggests a leak.
- API rate limit enforced (e.g. 429 when exceeded).

**Pass:** Linear scaling; no memory leak; rate limit enforced.  
**Fail:** Fix bottlenecks or leaks; re-test.

---

## 9. Manifest verification

**Requirement:** release/manifest.json and release/checksums.txt exist and list correct hashes for the shipped artifacts.

**Procedure:**
- Confirm `release/manifest.json` exists and includes: version, build timestamp, included_artifacts, entry_points, checksums_file (or equivalent).
- Confirm `release/checksums.txt` exists and contains SHA256 hashes for:
  - hesperia-cli.bin
  - hesperia-api-image.tar
- Optionally: re-run sha256sum on the binary and image tar and compare to checksums.txt.

**Pass:** Manifest and checksums present; hashes match the built artifacts.  
**Fail:** Regenerate manifest and checksums in build_shipping.sh; re-run build and verify.

---

## Summary table

| # | Item | Pass criterion |
|---|------|----------------|
| 1 | Structural verification | check_import_boundary.py exit 0 |
| 2 | Projection enforcement | No internal terms in CLI/API output |
| 3 | Binary inspection | No matches in strings scan for sphere/hex/topology/bridge/layer |
| 4 | Container inspection | Only /app/runtime, core, lexicon, assets; no docs/tests/debug/legacy/build tools |
| 5 | Release bundle | Only allowed contents in tar |
| 6 | Clean machine test | CLI + API work; projected output; no extra files; no internal logs |
| 7 | Reflection test | Evaluator cannot infer geometry, layers, dict method, propagation, reserve |
| 8 | Performance sanity | Linear batch; no leak; rate limit enforced |
| 9 | Manifest verification | manifest.json + checksums.txt with correct hashes |

---

## Final assessment

When all nine items pass:

- **Functional correctness** is preserved (entry points use service façade; projection applied; outputs and behavior are correct).
- **Internal model architecture** is hidden (no geometry, layer count, dictionary mechanics, propagation graph, or reserved structure inferable from the bundle).
- **Evaluator usability** is maintained (CLI, API, examples, quickstart, and limits are clear; reviewers can run and assess the product).

In practical terms, reconstruction of the internal method from the shipped bundle would require deep reverse-engineering effort with little conceptual payoff. That is the realistic target for proprietary systems.

---

*Checklist version: v1. Run before every sealed release.*
