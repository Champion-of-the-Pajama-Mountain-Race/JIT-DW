# Information ownership and source of truth

**Status:** Updated after Codex/AstrBot source-level Round 3 observations.

The same fact can appear in source code, schemas, comments, generated API references, tutorials, architecture documents, and runbooks. Repeating a volatile fact in several manually maintained places creates synchronization work and ambiguity.

However, the first field studies show that a strict rule of one fact appearing in only one file is too simple. CPython has both module docstrings and a separate library reference; Django has source docstrings and richer user-facing reference pages; Linux and Rust use source comments as inputs to generated API documentation.

JIT-DW therefore distinguishes **authoritative authoring source** from **reader-facing representation**.

## 1. The two-layer model

For each important fact, identify:

1. **Authority:** where the fact is authored or where its semantics are defined.
2. **Representations:** where readers encounter that fact, including generated pages, short summaries, tutorials, examples, and operational guides.

A fact may have more than one representation. It should not have multiple independently edited authorities unless the project deliberately defines how they are reconciled.

Examples:

- A Rust API comment is an authoring source for rustdoc output; doctests validate its examples.
- A Linux kernel-doc comment is an authoring source for generated API reference.
- A Python module docstring and a library reference may both repeat stable facts for different reader surfaces. The project must understand and manage that overlap.
- A Django source class docstring may be brief while the separate reference page explains user-visible semantics in more detail.
- A Kubernetes field comment and structured marker can define field-level API information, while a separate conventions document explains rules that span many fields.

## 2. Choose authority by information type

| Information | Candidate authoritative home | Other useful representations |
|---|---|---|
| Function signature and types | Source declaration or interface definition | Generated API reference, examples |
| Wire format or data schema | Schema/IDL definition | Generated reference, compatibility guide |
| Runtime behavior | Implementation plus tests | User guide, troubleshooting explanation |
| Module responsibility and boundary | Module contract or a deliberately maintained architecture source | Directory README, architecture diagram |
| Design rationale and alternatives | Decision record | Short rationale link from current docs |
| Build and contribution procedure | Maintained developer guide plus executable configuration | Onboarding tutorial |
| Operational recovery procedure | Runbook validated against deployed system | Short links from service documentation |
| User task | User-facing tutorial or how-to | Product entry point and navigation |

This table is a starting point, not a universal prescription. Some projects use source annotations, schemas, tests, build configuration, or hand-authored manuals as their primary documentation mechanism.

## 3. Rules for multiple representations

When the same fact appears in more than one place, record:

- why each representation exists and which reader it serves;
- which representation is authoritative for the underlying behavior;
- whether the secondary representation is generated, copied, summarized, or independently authored;
- how synchronization is checked;
- what change should trigger review of each representation.

Do not delete a representation merely because another copy exists. First determine whether it serves a distinct reading context, such as interactive help, generated API reference, onboarding, or a user-facing manual.

Do not leave duplicated volatile facts without an explicit synchronization plan.

## 4. Separate current truth from historical rationale

A decision record explains why a decision was made at a point in time. It should not automatically be treated as a description of the current implementation.

When a decision is reversed:

- preserve the earlier record as history;
- create a new record describing the reversal and its consequences;
- update the current architecture or module documentation;
- mark the old decision as superseded and link to the replacement.

Chromium's documentation guidance is a useful example: once code is implemented, design documents become archives of the decision rather than current implementation documentation.

## 5. Prefer derivation where it improves reliability

When practical, generate stable technical details from the source that owns them:

- API signatures from code or interface definitions;
- configuration references from schemas or declarative configuration;
- command help from the CLI implementation;
- API pages from structured source comments;
- examples from executable test blocks.

Generation is not automatically better. A generated page that is hard to navigate or omits the explanation readers need is not a good substitute for authored documentation.

## 6. Resolve conflicts explicitly

If two artifacts disagree:

1. identify which artifact is designated as authoritative for the fact;
2. verify the implementation and tests where behavior is involved;
3. correct the derived or stale artifact;
4. record an unresolved discrepancy if authority itself is unclear.

Do not resolve a conflict by assuming the newest file is correct.

## 7. Locality and central navigation

Keep detailed module knowledge near the module when contributors naturally work there. Use central architecture pages and indexes to explain cross-module relationships and provide navigation.

A local README should answer what this directory is, what its main boundaries are, and where a reader should go next. It should not reproduce every function and internal detail.

The Chromium base/task README is an example of a concise directory map rather than a per-file catalog.

## 8. Ownership metadata

Possible ownership mechanisms include CODEOWNERS, OWNERS, maintainers listed in a document, directory-level ownership files, or review routing. The field studies will determine which mechanisms are used in practice and their limits.

Avoid adding a manually maintained owner field to every document unless it changes review behavior or makes responsibility clearer.

## 9. Runtime-consumed documentation

An important exception to the ordinary prose model: a comment or docstring can be **input to software execution**. [AstrBot's LLM tool registration](https://github.com/AstrBotDevs/AstrBot/blob/734b357fe30963365494df0c0603844e708730f3/astrbot/core/star/register/star_handler.py#L650-L700) parses a Python function's docstring to construct a tool argument schema. The parser may change runtime behavior if a docstring is modified, even when code signatures are unchanged.

For such a **machine-consumed contract**, record the parser/consumer, allowed syntax, generated/runtime behavior, applicable versions, and executable tests. Treat docstring-only edits as potential code-contract changes. Do not generalize this rule to ordinary explanatory comments.

For schema generators, capture **input sets, generator command/version, output sets, and file-tree equality checks**. Codex's [schema fixture tests](https://github.com/openai/codex/blob/67f0994b532b8740f14b5b738af7b7b2a915b1d6/codex-rs/app-server-protocol/src/schema_fixtures_tests.rs) demonstrate that deleting stale generated output is part of consistency, not an optional cleanup.

See [validation provenance](validation-provenance.md) for check phase, execution evidence and Runner trust restrictions.
