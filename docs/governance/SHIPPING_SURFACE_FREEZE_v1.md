# SHIPPING SURFACE FREEZE v1

**Status:** Locked  
**Purpose:** Lock evaluator-visible commands and endpoints. No other public commands exist in release help or docs.

---

## 1. Allowed commands / endpoints only

The **only** evaluator-visible surface is:

| Type | Name | Description |
|------|------|-------------|
| CLI command | **analyze** | Single-text structural analysis. |
| CLI command | **compare** | Two-text comparison. |
| CLI command | **batch-analyze** | Multiple-text structural analysis. |
| API / serve | **serve** | API server (HTTP). |
| API endpoint | **health** | GET /health — liveness. |

No other public commands or endpoints may appear in:

- Shipped CLI `--help` or subcommand help.
- Shipped API OpenAPI/Swagger or route list.
- Release README, quickstart, or any doc intended for evaluators.

---

## 2. What must not appear as public

- No **run_l1_through_l9**, **run_reference_pipeline**, **run_l1_l2**, **run_l1_l2_l3**, **run_sphere_math_values**, **run_e2e_all**, or any internal runner name as an advertised command.
- No **debug**, **layer**, **trace**, **dump**, **internal** endpoint or command.
- No **L1**–**L9** or **layer view** in help or API docs.

---

## 3. Verification

- Run shipped CLI: `./hesperia-cli.bin --help` and each of `analyze`, `compare`, `batch-analyze` `--help`. Confirm only these three subcommands and no other commands.
- Run shipped API: GET /openapi.json or /docs. Confirm only **POST /analyze**, **POST /compare**, **POST /batch-analyze**, **GET /health**.
- Grep release README and quickstart for command/endpoint names. Confirm only the allowed list above.

---

## 4. Done condition

**Done when:** No other public commands exist in release help or docs. Surface is frozen to: **analyze**, **compare**, **batch-analyze**, **serve**, **health**.
