# Change impact assessment

**Status:** Provisional decision aid. The categories and examples must be validated against real project histories.

The purpose of change-impact assessment is to identify documentation that may have become incorrect because the system changed. It is not a rule that every code change must produce a documentation edit.

## 1. Start from changed facts

Ask:

1. What behavior, contract, constraint, assumption, or operational procedure changed?
2. Who relies on that information?
3. Where is the authoritative version maintained?
4. Which derived explanations or examples may now be misleading?
5. What evidence can verify the update?

A changed file is a clue, not the unit of impact. A single change may affect multiple documents; many code changes affect none.

## 2. Provisional impact matrix

| Change type | Potentially affected information | Typical action |
|---|---|---|
| Public API or CLI change | API reference, usage examples, compatibility or migration notes | Update authoritative reference and affected examples. |
| Configuration/default change | Configuration reference, tutorials, deployment examples | Update the canonical configuration description and relevant user guidance. |
| Module responsibility or boundary change | Module contract, architecture view, dependency rules | Update the nearest authoritative module/architecture description. |
| Data schema or persisted format change | Schema reference, migration guide, compatibility notes | Update schema source/reference and migration guidance where users or operators are affected. |
| Error or failure behavior change | API contract, troubleshooting guide, runbook | Describe externally relevant failure behavior and recovery. |
| Internal implementation refactor | Usually no user guide change; possibly module contract or design notes | Update only if an invariant, boundary, operational assumption, or maintained explanation changed. |
| Build, test, or release process change | Contributor guide, CI/development guide, release runbook | Update the instructions people actually follow. |
| Security boundary or permission change | Security model, configuration guide, operational guidance | Require focused review; do not rely on a generic PR checklist alone. |
| New subsystem or major capability | Architecture, module entry point, user guide, tests/examples | Add navigation and only the explanations needed by relevant readers. |
| Decision reversal | Current design explanation plus a new decision record | Preserve history; clearly identify the superseded decision. |

This matrix is a prompt for analysis, not a complete mapping and not a substitute for project-specific ownership.

## 3. Outcome categories

Every reviewed change should resolve to one of these outcomes:

- **Updated:** an authoritative documentation artifact changed with the implementation.
- **No update required:** the change does not alter maintained information; give a short reason when the impact is not obvious.
- **Deferred:** the information changed, but the documentation update is intentionally tracked elsewhere with an owner and follow-up reference.
- **Unknown / needs investigation:** impact cannot yet be determined. Do not silently treat this as no update required.

## 4. Direct and indirect impact

Distinguish:

- **Direct impact:** the changed fact is documented in an artifact that can be identified.
- **Indirect impact:** another document depends on the changed fact, such as an example, tutorial, diagram, or runbook.
- **Potential impact:** a relationship is plausible but has not been verified.

A project may begin with a manually maintained map for a few high-risk interfaces. Do not introduce repository-wide dependency mapping until its value and maintenance cost are demonstrated.

## 5. Review prompts

For a code review, ask only the prompts relevant to the change:

- Did an externally visible behavior or contract change?
- Did a module's responsibility, boundary, or dependency change?
- Did a configuration default, schema, or persisted format change?
- Did a user, contributor, or operator procedure change?
- Did a failure mode, security boundary, or recovery path change?
- Did a decision or assumption become invalid?
- Are generated docs or examples derived from changed source inputs?

A no answer to all prompts can be valid. If the change is consequential and the reason is not self-evident, record why no documentation update is needed.

## 6. What automation may do

Potentially automatable:

- detect changed paths and known owners;
- identify changed public symbols or schemas;
- flag stale generated output;
- run documentation builds and examples;
- require an impact outcome for selected change classes.

Not safely inferred from path changes alone:

- whether a module's responsibility changed;
- whether a design rationale is now invalid;
- whether a tutorial remains understandable;
- whether a change is truly internal;
- whether the document's explanation matches intended behavior.

Automation should produce evidence and prompts, not fabricate a semantic impact verdict.

## 7. Open research questions

- Which projects enforce documentation updates in CI, and which rely on reviewer judgment?
- How do projects map code ownership to documentation ownership?
- Do projects record no-docs-needed decisions? If so, where and at what granularity?
- How often do docs-only changes lag behind code changes?
- What proportion of stale documentation can be caught mechanically?
- Which impact signals are stable enough to automate without overwhelming maintainers?
