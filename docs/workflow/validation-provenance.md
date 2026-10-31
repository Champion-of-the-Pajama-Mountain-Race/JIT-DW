# JIT-DW validation provenance and machine-consumed documentation

**Status:** V0.3 proposal grounded in the Codex/AstrBot source study, not yet an accepted universal standard.

## 1. The document's role changes the impact rule

| Artifact role | Example | Appropriate verification |
|---|---|---|
| Human explanation | Concept, module README, tutorial | Semantic review and reader-task test |
| Source-local API contract | Rustdoc, Python method docstring | Contract-oriented review, examples/tests |
| Machine-consumed contract | AstrBot `@filter.llm_tool` docstring parsed into LLM tool JSON schema | Validate parser output, missing/malformed Args, runtime tool invocation |
| Generator input | Codex Rust app-server protocol types | Regenerate schemas/SDKs and compare **full file set and content** |
| Derived representation | Generated JSON/TypeScript/Python API | Detect missing/extra files and stale bytes |
| UI/documentation surface | TUI messages, translated WebUI guide, screenshot | Test actual user task, correct locale and navigation mapping |
| Decision history | ADR or proposal after implementation | Supersession and links to current behavior |

A source-comment-only change can be a **runtime behavior change** when code parses the comment. A Markdown-free PR can still update user-facing information through UI text.

## 2. Generator closure

For high-value derived artifacts record: **input paths + generator/version + command + expected output paths + validation command + affected versions/consumers**. Run the generator in a clean location where possible, compare output names and bytes with stored artifacts, and explicitly check for obsolete outputs. This is stronger than checking that a regeneration command returned exit code 0.

Source: [Codex schema-fixture tests](https://github.com/openai/codex/blob/67f0994b532b8740f14b5b738af7b7b2a915b1d6/codex-rs/app-server-protocol/src/schema_fixtures_tests.rs).

## 3. Record actual CI execution, not hypothetical coverage

For each meaningful check record:

```text
Check: <name>
Trigger/phase: <PR | push | post-merge | release | manual>
Runner/trust: <hosted | isolated private | persistent self-hosted>
State: <success | failure | skipped | queued | not triggered>
Input set / exclusions: <which files, versions and platforms>
Artifact or fact validated: <what property was checked>
Evidence: <job run URL, or command + logs>
Not proven: <semantic completeness, user tasks, other variants>
```

A workflow file is only a configuration. An upstream-only repository guard can make a Fork job skip, and a release-only documentation build does not validate each PR.

Sources: [Codex CI strategy](https://github.com/openai/codex/blob/67f0994b532b8740f14b5b738af7b7b2a915b1d6/.github/workflows/README.md), [AstrBot docs workflow](https://github.com/AstrBotDevs/AstrBot/blob/734b357fe30963365494df0c0603844e708730f3/.github/workflows/build-docs.yml), [AstrBot dashboard workflow guard](https://github.com/AstrBotDevs/AstrBot/blob/734b357fe30963365494df0c0603844e708730f3/.github/workflows/dashboard_ci.yml#L9-L15).

## 4. Staged validation

- **PR:** cheap syntax, impacted unit tests, generated-reference consistency, document build for relevant doc paths, human semantic review.
- **Post-merge/nightly:** broader platform/build/test matrices where time and compute cost justify deferral.
- **Release:** docs publication, compatibility/migration and cross-version navigation.
- **Reader feedback:** task-completion checks; mechanical success never substitutes for comprehension.

Explicit deferral is acceptable only with owners, evidence and risk boundaries. Do not quietly treat skipped checks as success.

## 5. Runner trust

Public pull-request code should not execute on the organization's existing persistent Runner, even if a documentation workflow calls itself a harmless linter. Prefer GitHub-hosted runners or tightly isolated ephemeral infrastructure. GitHub's [runner group guide](https://docs.github.com/en/actions/how-tos/manage-runners/self-hosted-runners/manage-access) warns of untrusted fork PR risk.

## 6. Reviewer questions

1. Could an edit to a comment/docstring alter a parser, generated schema or runtime?
2. If an API changes, which generated output tree and client versions need comparison?
3. Was the declared verification executed **on the reviewed revision**, or skipped/queued/not triggered?
4. Did an existing reader-facing locale, UI instruction, screenshot, or CLI string become stale?
5. Does the selected Runner cross an untrusted-code boundary?
6. Is the outcome Updated, justified No update required, Deferred with owner, or Unknown?

These augment, not replace, [the JIT-DW impact review protocol](impact-review-protocol.md).
