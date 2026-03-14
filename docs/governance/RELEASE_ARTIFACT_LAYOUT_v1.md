# Release artifact layout v1

**Status:** Frozen  
**Purpose:** Final layout of the evaluator bundle. No other files allowed.

---

## Directory structure

```
hesperia-evaluator-bundle/
│
├── hesperia-cli.bin
├── hesperia-api-image.tar
│
├── examples/
│
├── assets/
│   └── public/
│
├── manifest.json
├── checksums.txt
│
├── README.md
└── EVALUATOR_GUIDE.md
```

---

## Allowed contents only

| Path | Description |
|------|-------------|
| **hesperia-cli.bin** | Single-file CLI executable (Nuitka onefile). |
| **hesperia-api-image.tar** | Docker image tar; load with `docker load -i`. |
| **examples/** | Sample inputs and/or example outputs (projected only). |
| **assets/public/** | Public schema, ontology map, metric profiles (no internal topology). |
| **manifest.json** | Version, commit, build timestamp, included artifacts, entry points. |
| **checksums.txt** | SHA256 of hesperia-cli.bin and hesperia-api-image.tar. |
| **schema_sha256.txt** | (Optional) SHA256 of public_output_schema.json for runtime integrity check. |
| **README.md** | Quickstart and package overview. |
| **EVALUATOR_GUIDE.md** | What HESPERIA does, how to run CLI/API, what outputs mean, what to test. |

**Nothing else.** No source tree, no docs/internal, no tests, no tools, no legacy, no extra scripts.

---

## Verification

Before shipping, run:

```bash
tar -tf hesperia-evaluator-bundle.tar
```

Confirm the listing matches the structure above and contains no additional files or directories.

---

*Layout version: v1. See SEALED_RUNTIME_RELEASE_PROCESS_v1.md and SHIPPING_EXCLUSION_LOCK_v1.md.*
