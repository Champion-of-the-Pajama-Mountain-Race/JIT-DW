# JIT-DW provisional change-impact review protocol

**Status:** Proposed from inspected repository evidence; advisory only until pilots demonstrate acceptable precision and maintenance cost.

## Purpose

Use changed information, not a blanket rule on changed filenames, to decide what documentation work is needed. The reviewer should be able to understand the reasoning without reviewing a fabricated document for every source file.

## Stage 0 — Identify the scope

Record the PR/commit, target audience, intended behavior, and whether the change affects public APIs, internal module contracts, data formats, operational procedures, or merely a local implementation detail.

If the change includes a new feature, read the tests and release notes; if it changes a subsystem boundary, inspect module/local source comments and existing navigation. File paths are hints, not a proof of impact.

## Stage 1 — Name changed facts

List only facts whose truth conditions may have changed. For each:

| Field | Meaning |
|---|---|
| Fact | A specific behavioral claim, interface contract, assumption, or procedure |
| Consumers | Who or what relies on it (users, operators, contributors, external SDKs, etc.) |
| Authority | Source declaration, schema, test, current architecture description, or another explicit source |
| Representations | Source comments, reference, tutorial, module README, generated output, release notes, examples |
| Verification | Test, build, generated-doc check, static assertion, or focused reviewer judgment |
| Review route | Existing CODEOWNERS/OWNERS/MAINTAINERS or other actual expertise |
| Confidence | Confirmed / plausible / unknown |

For high-risk changes, require at least one concrete pointer to the authoritative source and relevant verification. For a small internal optimization, a one-sentence rationale may be enough.

## Stage 2 — Trace representations

For each changed fact, ask:

- Is its API contract already documented in source? Should a docstring or annotation change?
- Is there a separate generated reference? Does it regenerate from the source that changed?
- Does a user-facing reference, tutorial, runbook, or example repeat the fact?
- Are multiple versioned API types or language bindings expressing it?
- Does release applicability change? If so, do release notes or version markers matter?
- Is an existing design document historical rationale or current implementation explanation?

Do not automatically create a Markdown file because a source file was added. Do not delete intentional reader-facing summaries merely because an authoritative source exists elsewhere.

## Stage 3 — Review boundary conditions

A relevant reviewer should check changed semantics: errors, default values, security/permission effects, concurrency, compatibility, edge cases, cache behavior, migrations, and operational recovery when applicable.

This stage is guided by project-specific risk, not by a universal hundred-item checklist. Django's HTTP QUERY PR shows why: "safe method" affected CSRF, conditional requests, views, test-client functions, and caching boundaries. A diff-only docs rule would not capture the whole feature.

Review mechanisms must not be conflated:
- A label is notification, not approval.
- A CODEOWNERS entry can be an interested reviewer, not an exclusive owner.
- A passing doc build is not proof of correct prose.
- An unchecked box is not an impact verdict.

## Stage 4 — Choose exactly one disposition per changed fact

| Outcome | When it is valid | Required evidence |
|---|---|---|
| **Updated** | Relevant maintained representations were updated | Paths to modified authoritative/reader-facing artifacts and tests or review |
| **No update required** | No maintained explanation or reader task is affected | Brief concrete rationale for nontrivial changes |
| **Deferred** | An update is required but deliberately split | Explicit owner, issue/PR follow-up, scope, user-visible limitation if relevant |
| **Unknown** | Evidence is insufficient to determine impact | What is unknown, investigation owner or next verification, and whether risk warrants merge blocking |

“Generated/verified” is an evidence attribute of Updated or No update required, not a fifth outcome: successful generation does not decide semantic completeness.

A change may have multiple facts, each with a different disposition.

## Stage 5 — Validate what can actually be validated

**Mechanical:**
- docs build and valid internal navigation;
- targeted docstring/schema/checker validation;
- executable examples, doctests, and testable snippets;
- generated output/inputs or declared source-of-truth discovery;
- changed-file classification and review-routing checks.

**Semantic:**
- consistent API contract and error behavior;
- accurate warnings and limitations;
- correct release applicability;
- reader can perform the documented task;
- acknowledged decisions about intentionally duplicated information.

For any mechanical check, record its real input file set and exclusions. Django PR #22111 shows why duplicating Sphinx file-exclusion logic made checks disagree with the docs builder.

## Worked decisions

| Example | Candidate verdict | Reason |
|---|---|---|
| [CPython heapq indexing optimization](https://github.com/python/cpython/commit/c7d7105b8d230741a5fa04924701d5245d07dace) | No user-doc update likely, **conditional on behavior preservation** | Four local expression changes; no visible public contract change in the inspected diff |
| [Kubernetes perContainer API explanation](https://github.com/kubernetes/kubernetes/commit/cef7481431757c32ddeb07fad52551e27493bb79) | Updated | One semantic explanation synchronized across six API type sources |
| [Linux kref documentation integration](https://github.com/torvalds/linux/commit/b76d32422c09bc9310f61a5a89671975db34bd2a) | Updated | Source comments improved and Sphinx inclusion added so readers see them |
| [Django QUERY feature](https://github.com/django/django/pull/21855) | Updated for core contracts; deferred for full caching | Code/docs/tests/release notes changed together; caching boundary explicitly documented |
| [Chromium componentization](https://github.com/chromium/chromium/commit/924b5bcf53a392fa97f0d517c0d8df67d2cffb1f) | Unknown / investigation | No new README in changed files, but header comments contain meaningful public contracts; reader impact not established |

## Minimal PR note (optional, not a new mandatory file)

A small or medium project may include the following in the PR description, if not already covered by its native workflow:

~~~text
Information changed: <what fact, behavior, contract or procedure>
Readers affected: <who relies on that information>
Representations checked: <source comments / docs / release notes / examples / none>
Outcome: Updated | No update required | Deferred | Unknown
Evidence: <test/check/reviewer/commit path or reason>
Remaining risk: <none known, or explicit gap + owner>
~~~

**Caution:** A PR description can become stale while the patch evolves. For consequential changes, re-check the final diff and tests. In Django PR #21855, the PR body and final 307/308 redirect test coverage describe different states of the work.

## Pilot rules

Do not enable a blocking “docs changed” gate from path heuristics alone. Initially report advisory proposed outcomes and compare them with maintainer assessment. Track false positives, false negatives, time spent, and uncertain cases. See [validation plan](../../validation/README.md).
