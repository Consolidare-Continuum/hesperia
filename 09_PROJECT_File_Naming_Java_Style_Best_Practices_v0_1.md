# 09_PROJECT_File Naming — Java-Style Best Practices (v0.1)

Purpose: consolidate Java project file naming conventions into a single, stable reference.
This is a rule surface for maintainers. It is not a style suggestion.

Scope: Java source/test code, build modules, resources, and operational artifacts.

---

## 0. Core constraints (non-negotiable)

- File names are ASCII, no spaces, no emoji.
- Case and separators are meaningful; do not mix styles within a category.
- A file name must make its primary role unambiguous without opening the file.
- Public Java types must match file names exactly.

## 1. Java source files (main)

- One public top-level type per file.
- File name equals the public type name exactly (case-sensitive).
- Use `UpperCamelCase` for classes, records, enums, interfaces, and annotations.
- Use clear nouns for types (avoid verbs for type names).
- Avoid abbreviations unless they are domain-canonical (e.g., `URL`, `HTTP`).

Examples:
- `SemanticEngine.java`
- `FamilyIndex.java`
- `TraversalPolicy.java`
- `RegionScore.java`

## 2. Package and directory layout

- Package names are all lowercase.
- Directory structure mirrors package structure exactly.
- Prefer short, stable package roots (no org-specific vanity beyond the root).

Example path:
- `src/main/java/com/hesperia/semantic/TraversalPolicy.java`

## 3. Test files

- Test class file name matches the system-under-test with a suffix.
- Unit test suffix: `Test` (e.g., `TraversalPolicyTest.java`).
- Integration test suffix: `IT` (e.g., `TraversalPolicyIT.java`).
- Avoid mixing unit and integration assertions in a single test class.

## 4. Resource files

- Resource file names are lowercase with hyphens: `lower-kebab-case`.
- Use stable, descriptive nouns (avoid versioning inside the file name unless required).
- Locale variants use standard suffixes: `messages_en.properties`, `messages_en_US.properties`.

Examples:
- `logback.xml`
- `application.yml`
- `schema-migration.sql`
- `family-matrix.csv`

## 5. Build and module naming

- Maven/Gradle module directory names are lowercase with hyphens.
- Maven `artifactId` mirrors the module directory name.
- Do not encode version numbers in module directory names.

Examples:
- `semantic-engine/`
- `indexing-core/`

## 6. Generated and derived artifacts

- Generated outputs must be grouped under `build/`, `target/`, or a dedicated `generated/` root.
- Never commit generated files unless explicitly required by a spec.
- Generated file names should carry a deterministic prefix or suffix: `generated-`, `-generated`.

## 7. Migration and schema files

- Use deterministic prefixes and sortable ordering (e.g., `V0001__init_schema.sql`).
- No ambiguous numeric-only filenames.
- Use concise verbs after the separator: `V0002__add_family_links.sql`.

## 8. Exceptions (documented only)

Any deviation from this document must be:

- explicitly called out in the relevant spec, and
- indexed in `DOC_INDEX.md` if it affects public or stable artifacts.
