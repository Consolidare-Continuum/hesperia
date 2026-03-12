# Prolog-Style Rule Grammar (v1)

Deterministic grammar for the planned Prolog-style Logic Layer. Bounded symbolic inference only; no full Prolog interpreter.

## Scope

- **Facts**: ground assertions (atom or predicate with arguments).
- **Rules**: head :- body (conjunction only).
- **Inference**: forward-chaining fixed-point over facts and rules.

v1 is deliberately narrow: lowercase identifiers, no negation, no recursion, no disjunction, no function nesting.

---

## Lexical Conventions

- **Comment**: from `%` to end of line. Comments and blank lines are stripped before parsing.
- **Whitespace**: spaces and tabs between tokens; leading/trailing stripped per line.
- **Atom**: lowercase letters, digits, underscore. Must not start with a digit. Examples: `governance_bias`, `entropy_low`, `true`.
- **Number**: integer (e.g. `0`, `42`) or float (e.g. `0.35`, `1.2`). Used as term in arguments only.
- **Variable** (v1): not used. If enabled in a later version, variables are uppercase identifiers (e.g. `X`, `Val`).

---

## Grammar Elements

### Fact

A fact is a ground assertion terminated by a period.

**Bare fact (atom only):**
```
fact :
  atom .
```
Example: `governance_bias.`

**Predicate with arguments:**
```
fact :
  atom ( term_list ) .
term_list :
  term
  | term , term_list
term :
  atom
  | number
```
Example: `entropy_low(true).`  
Example: `dominant_area(governance).`  
Example (numeric): `entropy_low(0.35).`

### Rule

A rule has a head and a body. The body is a conjunction of goals (no disjunction in v1).

```
rule :
  head :- body .
head :
  atom
  | atom ( term_list )
body :
  goal
  | goal , body
goal :
  atom
  | atom ( term_list )
```
Example: `structural_monotony :- entropy_low(true), coverage_ok(true).`

- **Head**: single predicate (atom or atom(term_list)).
- **Body**: one or more goals separated by comma (conjunction). Empty body is invalid.
- **Goal**: same shape as head (atom or atom(term_list)).

---

## Constraints (v1)

| Feature           | Allowed in v1 |
|------------------|----------------|
| Lowercase atoms  | Yes            |
| Uppercase (variables) | No      |
| Negation        | No             |
| Recursion       | No             |
| Disjunction (;) | No             |
| Function nesting in terms | No   |
| Conjunction (,)  | Yes            |
| Single :- per rule | Yes         |
| Empty body      | No             |
| Duplicate separators (e.g. ,,) | No (reject) |

---

## Invalid Syntax Examples

- `entropy_low(true)` — missing final `.`
- `a :- .` — empty body
- `X(test).` — uppercase predicate/variable (v1)
- `rule :- a; b.` — disjunction not in v1
- `a :- b,, c.` — duplicate comma
- Nested terms, e.g. `f(g(1))` — not in v1

---

## Deterministic Semantics

- **Fact satisfaction**: A fact is satisfied if an identical predicate with identical arguments exists in the known fact set.
- **Rule satisfaction**: A rule is satisfied when every goal in its body is satisfied (i.e. each body goal has a matching fact).
- **Inference**: Forward-chaining fixed-point: repeatedly apply all rules; when all body goals of a rule are satisfied, add the head as a derived fact; stop when no new facts are added. Rule order is source order (stable after compilation).

---

## References

- Implementation: `sphere/prolog_logic/` (rule_compiler, knowledge_base, inference_executor).
- Example rules: `spec/prolog_rules_example.pl`.
- This layer is downstream of measurement layers and separate from Layer-9 and interpretation.
