# Round 3 — Codex and AstrBot: confirmed designs and missing mechanisms

**Status:** Pinned source/PR investigation, not a project-wide compliance audit or a measured JIT-DW precision/recall result.  
**Date:** 2026-10-31.  
**Baselines:** [Codex 67f0994b](https://github.com/openai/codex/tree/67f0994b532b8740f14b5b738af7b7b2a915b1d6) and [AstrBot 734b357f](https://github.com/AstrBotDevs/AstrBot/tree/734b357fe30963365494df0c0603844e708730f3).

## A — JIT-DW ideas corroborated by real engineering practice

| Already in JIT-DW | Source/history observation | Evidential limit |
|---|---|---|
| Authoritative source plus derived representations | Codex [schema fixture tests](https://github.com/openai/codex/blob/67f0994b532b8740f14b5b738af7b7b2a915b1d6/codex-rs/app-server-protocol/src/schema_fixtures_tests.rs#L18-L53) compare generated TypeScript/JSON and precomputed artifacts; [PR #57172](https://github.com/openai/codex/pull/57172) changes Rust protocol, generated TypeScript/Python, README and tests in one PR. | Does not prove every hand-authored explanation is current. |
| Comments local to code for interface behavior | Codex [linux-sandbox README](https://github.com/openai/codex/blob/67f0994b532b8740f14b5b738af7b7b2a915b1d6/codex-rs/linux-sandbox/README.md#L1-L24) and [PR #52610](https://github.com/openai/codex/pull/52610) pair module responsibilities, Rust source comments and tests; AstrBot [DecisionService source docs](https://github.com/AstrBotDevs/AstrBot/blob/734b357fe30963365494df0c0603844e708730f3/astrbot/core/provider/decision.py#L18-L65) describe arguments, results and error behavior. | No evidence that every source file needs a dedicated Markdown responsibility note. |
| Update changed meaning, not merely files | Codex [PR #43423](https://github.com/openai/codex/pull/43423) **removed** a blanket app-server-docs update instruction but retained schema-regeneration advice for changed API shapes. | A historical governance change; do not infer that current behavior changes never require docs. |
| Reader-facing representations include non-Markdown surfaces | Codex [PR #49361](https://github.com/openai/codex/pull/49361) corrected misleading credential-persistence statements in TUI/CLI output with snapshots, no separate Markdown edit. AstrBot [PR #10879](https://github.com/AstrBotDevs/AstrBot/pull/10879) updated seven translated READMEs and two guides together. | Matching files or updating text does not prove reader task completion. |
| Semantic review is distinct from a passing docs build | AstrBot [PR #10788](https://github.com/AstrBotDevs/AstrBot/pull/10788) updated plugin reload failure behavior and added HTTP regression tests without a docs file. | Docs impact still needs explicit review; absence of Markdown is neither failure nor success. |

## B — Where these projects are ahead of the first JIT-DW design

### B1. A docstring can be a runtime contract, not a description (highest priority)

AstrBot's [tool registration parser](https://github.com/AstrBotDevs/AstrBot/blob/734b357fe30963365494df0c0603844e708730f3/astrbot/core/star/register/star_handler.py#L650-L700) uses `docstring_parser.parse(awaitable.__doc__)` to construct a tool's argument schema. The [bilingual developer guide](https://github.com/AstrBotDevs/AstrBot/blob/734b357fe30963365494df0c0603844e708730f3/docs/en/dev/star/guides/ai.md#L174-L200) warns that missing or malformed Args metadata can silently discard model-supplied arguments.

**Missing JIT-DW concept:** a `machine-consumed contract` with parser, required syntax, actual runtime consumers, and negative tests. A docstring-only edit can change software behavior.

**Adopt:** schema/invocation tests for such docstrings. **Do not generalize** this to ordinary docstrings.

### B2. Codex checks the complete generated artifact tree

[Codex schema fixture tests](https://github.com/openai/codex/blob/67f0994b532b8740f14b5b738af7b7b2a915b1d6/codex-rs/app-server-protocol/src/schema_fixtures_tests.rs#L99-L184) regenerate schema results and compare both file presence and content, detecting missing/extra or stale files. The [justfile](https://github.com/openai/codex/blob/67f0994b532b8740f14b5b738af7b7b2a915b1d6/justfile#L172-L180) defines the regeneration entry point.

**Missing JIT-DW detail:** a generator relationship needs input set, generator/version, output set, invalidation trigger, and file-tree comparison—not just “remember to regenerate”.

### B3. Codex validates some comments against code structure

[argument-comment-lint](https://github.com/openai/codex/blob/67f0994b532b8740f14b5b738af7b7b2a915b1d6/tools/argument-comment-lint/README.md#L1-L32) verifies `/*parameter*/` call-site hints against resolved parameter names. The same README explicitly prefers self-describing API types/names over comment-heavy code.

**Adopt selectively:** machine-verifiable comments can be checked against AST/symbols, but don't demand comments when better API structure makes them unnecessary. A specialized compiler lint is too expensive for JIT-DW Lite.

### B4. Validation has a phase, trigger and execution scope

Codex's [CI strategy](https://github.com/openai/codex/blob/67f0994b532b8740f14b5b738af7b7b2a915b1d6/.github/workflows/README.md#L1-L38) deliberately separates fast PR-time Bazel/Cargo checks from broader post-merge testing. AstrBot's [docs build workflow](https://github.com/AstrBotDevs/AstrBot/blob/734b357fe30963365494df0c0603844e708730f3/.github/workflows/build-docs.yml#L1-L30) runs on version tags or manual dispatch, **not every PR**. Its [dashboard_ci.yml](https://github.com/AstrBotDevs/AstrBot/blob/734b357fe30963365494df0c0603844e708730f3/.github/workflows/dashboard_ci.yml#L1-L15) includes an upstream-only repository guard, so the inherited job is skipped on the organization's Fork.

**Missing JIT-DW detail:** a check that exists or a green overall workflow cannot establish the required check actually ran. Capture trigger, repo eligibility, job status (success/fail/skipped/queued), files covered, exclusions, phase and cost.

### B5. UI navigation and localization are typed dependencies

AstrBot's [CONTRIBUTING](https://github.com/AstrBotDevs/AstrBot/blob/734b357fe30963365494df0c0603844e708730f3/CONTRIBUTING.md#L37-L45) links changed navigation to Chinese/English guides, screenshots, old-to-new entry maps and verification of actual operation steps. [PR #10879](https://github.com/AstrBotDevs/AstrBot/pull/10879) demonstrates multilingual coordination.

**Adopt where relevant:** optional edges for translations, screenshots, UI entry names/routes and reader tasks. Do not force every project to provide translated pages.

## C — What not to imitate blindly

- Don't require Google-style docstrings on every internal helper just because AstrBot's AGENTS.md states a convention. The runtime-parsed tool docstrings need stronger guarantees than ordinary comments.
- Don't install specialized Rust Dylint throughout unrelated Python/small repos.
- Don't treat every translation or screenshot as mandatory if no corresponding reader-facing artifact exists.
- Don't claim an automated check guarantees semantic readability.
- Don't claim these hand-picked PR examples measure project-wide behavior or JIT-DW impact precision/recall.

## D — Decisions for JIT-DW V0.3

1. Promote `machine-consumed contract` to an explicit information role.
2. Validate generated outputs by input/output closure and stale-file detection.
3. Add staged CI evidence: PR / post-merge / manual / release, real execution status and coverage.
4. Track translation/UI task links only when the project needs them.
5. Preserve the advisory-only impact verdict and report Unknown rather than fabricate completeness.
6. Add a Runner trust check before executing untrusted code.

See [runner evidence](../../validation/pilots/codex-astrbot/runner-probe.md) and [workflow validation rules](../../docs/workflow/validation-provenance.md).
