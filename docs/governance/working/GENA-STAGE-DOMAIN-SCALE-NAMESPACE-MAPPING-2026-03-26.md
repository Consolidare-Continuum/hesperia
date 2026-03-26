# Gena — STAGE / DOMAIN / SCALE namespace mapping

Date: 2026-03-26  
Scope: remove ambiguity of the overloaded term `layer` by splitting semantics into 3 explicit axes.

## 1) Three meanings now explicit

- **Execution Flow (execution order)** -> `STAGE`
  - Example: instrumentation -> traversal -> dynamics -> propagation.
- **Structural composition (what exists)** -> `DOMAIN`
  - Example: lexical dictionaries, topology graph, governance operators.
- **Analytical observation scale (how we read output)** -> `SCALE`
  - Example: sentence / paragraph / section / document.

## 2) Canonical namespaces

### STAGE

- `STAGE_1_INSTRUMENTATION` (`S1`)
- `STAGE_2_TOPOLOGY_TRAVERSAL` (`S2`)
- `STAGE_3_DYNAMICS` (`S3`)
- `STAGE_4_PROPAGATION` (`S4`)
- `STAGE_5_INTERPRETATION` (`S5`)
- `STAGE_6_LOGIC` (`S6`)

### DOMAIN

- `DOMAIN_LEXICAL`
- `DOMAIN_TOPOLOGY`
- `DOMAIN_DYNAMICS`
- `DOMAIN_GOVERNANCE`

### SCALE

- `SCALE_SENTENCE` (`SC1`)
- `SCALE_PARAGRAPH` (`SC2`)
- `SCALE_SECTION` (`SC3`)
- `SCALE_DOCUMENT` (`SC4`)

## 3) Concrete mapping from current vocabulary

| Current | New |
|---|---|
| L1 instrumentation | STAGE_1_INSTRUMENTATION |
| L2 traversal | STAGE_2_TOPOLOGY_TRAVERSAL |
| L6 dynamism | STAGE_3_DYNAMICS |
| L7 propagation | STAGE_4_PROPAGATION |
| L8 interpretation | STAGE_5_INTERPRETATION |
| L9 logic | STAGE_6_LOGIC |

| Current | New |
|---|---|
| Dict A / Dict B layer | DOMAIN_LEXICAL |
| Geometry layer | DOMAIN_TOPOLOGY |
| Guard layer (Sigma, Gamma, Theta) | DOMAIN_GOVERNANCE |

| Current | New |
|---|---|
| R1 | SCALE_SENTENCE |
| R2 | SCALE_PARAGRAPH |
| R3 | SCALE_SECTION |
| R4 | SCALE_DOCUMENT |

## 4) Non-breaking implementation note

- Legacy names remain readable in existing payloads/runners.
- New names are emitted as aliases in execution_flow profile outputs and mapping constants.
- Migration can proceed by consumers switching to `STAGE` / `DOMAIN` / `SCALE` keys first.

SIGNED: Main Developer (Gena) | namespace separation | 2026-03-26 | main engine naming

