# Information ownership and source of truth

**Status:** Provisional design principle; repository field studies will test how projects implement it.

The same fact can appear in source code, schemas, comments, generated API references, tutorials, architecture documents, and runbooks. Repeating a volatile fact in many manually maintained places creates synchronization work and ambiguity.

JIT-DW therefore proposes assigning one authoritative home to each important fact, then treating other appearances as derived explanations or views.

## 1. Choose authority by information type

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

This table is a starting point, not a universal prescription. Some projects use source annotations, schemas, tests, or build configuration as their primary documentation mechanism.

## 2. Separate current truth from historical rationale

A decision record explains why a decision was made at a point in time. It should not automatically be treated as a description of the current implementation.

When a decision is reversed:

- preserve the earlier record as history;
- create a new record describing the reversal and its consequences;
- update the current architecture or module documentation;
- mark the old decision as superseded and link to the replacement.

## 3. Prefer derivation over copying

When practical, generate stable technical details from the source that owns them:

- API signatures from code or interface definitions;
- configuration references from schemas or declarative configuration;
- command help from the CLI implementation;
- diagrams or inventories from machine-readable data only when the generated result is genuinely easier to maintain.

Generation is not automatically better. A generated page that is hard to navigate or omits the explanation readers need is not a good substitute for authored documentation.

## 4. Resolve conflicts explicitly

If two artifacts disagree:

1. identify which artifact is designated as authoritative for the fact;
2. verify the implementation and tests where behavior is involved;
3. correct the derived or stale artifact;
4. record an unresolved discrepancy if authority itself is unclear.

Do not resolve a conflict by assuming the newest file is correct.

## 5. Locality and central navigation

Keep detailed module knowledge near the module when contributors naturally work there. Use central architecture pages and indexes to explain cross-module relationships and provide navigation.

A local README should answer "what is this directory and where should I go next?", not reproduce every function and internal detail.

## 6. Ownership metadata

Possible ownership mechanisms include CODEOWNERS, maintainers listed in a document, directory-level ownership files, or review routing. The field studies will determine which mechanisms are used in practice and their limits.

Avoid adding a manually maintained owner field to every document unless it changes review behavior or makes responsibility clearer.
