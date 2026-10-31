# Repository field-study synthesis — V0.2

**Status:** Evidence-informed proposal, not validated JIT-DW field deployment.  
**Date:** 2026-10-31.  
**Sources:** [Round 1 synthesis](findings-v0.1.md), [Round 2 sample](round-2/change-history-sample.md), [ownership analysis](round-2/ownership-and-review-routing.md), [Django QUERY trace](round-2/django-query-end-to-end.md), and [Django docs-check drift](round-2/django-doc-tooling-drift.md).

## Executive finding

After inspecting selected real changes and review conversations, the main improvement to JIT-DW is a shift from **document file management** toward **information-change management**.

A good workflow asks:

1. What observable behavior, contract, rationale, operational procedure, or compatibility claim changed?
2. Which code, source comments, tests, docs, and release notes express that fact?
3. Where does review expertise come from, and who may approve or defer the change?
4. What can the project validate mechanically? What still needs a human or task-based review?
5. Is the effect verified, deliberately deferred, irrelevant, or still unknown?

The answer can legitimately be a source-comment update, a reference page, a release note, several synchronized API representations, no new document, or a flagged uncertainty.

## Result A — Route by expertise and information domain, not just by individual files

CPython's CODEOWNERS explicitly groups heapq source, reference docs, tests, and C extension under the same topical reviewer. It also states that the named contributors are interested reviewers, not exclusive owners.

Chromium's OWNERS distinguishes component APIs from implementation subfolders. Kubernetes distinguishes reviewers, approvers, required reviewers, aliases, labels, and inheritance settings. Linux routes patches through MAINTAINERS and get_maintainer.pl. Rust triagebot labels documentation-relevant code, tools, tests, and docs.

**Design correction:** JIT-DW must keep separate fields for authoritative information, reviewer routing, approver authority, and notification labels. Do not add another per-file owner registry if the repository already has useful routing configuration.

**Limitation:** Configuration proves declared routing, not actual reviewer attendance or response.

## Result B — A change can impact many knowledge surfaces without a one-file-to-one-doc mapping

[Django PR #21855](https://github.com/django/django/pull/21855) modified 27 files for one HTTP QUERY feature. Relevant contracts included CSRF, safe-method decorators, conditional HTTP behavior, class-based dispatch, request bodies, and testing utilities. Corresponding user docs, reference pages, tests, and release notes were edited together. The release notes make deferred caching behavior explicit.

[Kubernetes's perContainer comment update](https://github.com/kubernetes/kubernetes/commit/cef7481431757c32ddeb07fad52551e27493bb79) changed a single semantic explanation in six internal and versioned API type files.

**Design correction:** The unit of impact is the changed fact and its representations, not the changed source file.

**Limitation:** We did not independently run the affected test suites.

## Result C — A code-only change is not automatically a documentation failure

[CPython's heapq optimization](https://github.com/python/cpython/commit/c7d7105b8d230741a5fa04924701d5245d07dace) replaced tuple-unpacking with indexing in four local expressions; its commit changed only the implementation file. No public-interface change is evident in the inspected patch. A user-docs update would plausibly be unnecessary if behavior is preserved.

[Chromium's PageStabilityMonitor componentization](https://github.com/chromium/chromium/commit/924b5bcf53a392fa97f0d517c0d8df67d2cffb1f) moved boundaries without a new README in the changed files. The new header still documents purpose, lifetime, single-use constraints, and callback behavior. Its full documentation impact is not established.

**Design correction:** Distinguish “no docs needed after analysis” from “unknown”. A path heuristic should never treat no Markdown edit as proof of a defect.

## Result D — Review can catch what automation cannot

In Django PR #21855, reviewers asked about redirect handling, tests, middleware behavior, and caching. The merged tests include new QUERY-specific cases, while caching was left for later with an explicit explanation.

The PR body still describes some 307/308 redirect handling as not addressed, whereas final tests include method/body preservation for that test-client scenario. This is a useful warning: PR descriptions are not always an accurate snapshot of the final patch.

**Design correction:** Human review should inspect the final diff, tests, and documented exclusions; historical PR prose should be treated as rationale, not an automatically authoritative description of final behavior.

**Limitation:** The code and tests were inspected; they were not executed in this study.

## Result E — The documentation checker itself needs an authoritative source

[Django PR #22111](https://github.com/django/django/pull/22111) removed duplicated documentation-file selection filters from lint/format scripts. Its replacement uses Sphinx's own document discovery through a minimal application. Review identified missing Sphinx dependencies and cross-platform details that the final patch addressed.

**Design correction:** Mechanical checks should derive their input lists from the documentation build source when possible, report coverage, and explicitly say what they do not prove.

## Negative and uncertain cases matter

The [curated history sample](round-2/change-history-sample.md) contains 11 different cases selected for their contrasting characteristics. It is not random. We must not report any population-level percentage from it.

One especially instructive ambiguity is a large refactor with meaningful source comments and no standalone README. A JIT-DW rule that automatically rejects this change would likely be too rigid. The correct result is either a reasoned no-update verdict or an explicit investigation, depending on whether actual reader tasks remain supported.

## What changes in the proposed workflow now

1. **Information impact record:** identify changed fact, consumer, canonical source, representations, review owner, and validation evidence.
2. **Four outcomes:** updated, justified no-update, deferred with owner, or unknown. Generated/verified is an evidence attribute, not a substitute for one of these decisions.
3. **Authority/representation split:** intentional duplication is allowed when each surface has a different reader need and a synchronization mechanism.
4. **Review-routing reuse:** rely on CODEOWNERS, OWNERS, MAINTAINERS, and existing triage tools where available.
5. **Non-blocking pilot first:** run the impact protocol as advisory analysis before gating CI. Assess false positives, misses, time spent, and abstention quality.
6. **Docs-check coverage:** record which files the check actually read and which it intentionally excluded.
7. **PR descriptions are not final truth:** compare important claims with the final merged code and tests.

An actionable draft is in [the impact-review protocol](../docs/workflow/impact-review-protocol.md).

## Open questions remaining

- How do we detect that a behavior change has occurred without confidently interpreting arbitrary diffs?
- How much more time does impact review take compared with the baseline?
- Can an agent identify indirect docs from dependency/context links without overwhelming human reviewers?
- Do overlapping summaries in CPython and other projects produce measurable drift?
- Under what conditions should “unknown” block merging rather than permit a tracked deferral?
- Do CODEOWNERS or OWNERS rules consistently lead to the right domain expert reviewing docs?
- Can a pilot show measurable reader task completion improvement without distorting contributor workflow?

**Next evidence gate:** apply the protocol to recent real changes in an opt-in pilot repository; compare its proposed impact to maintainer judgments before enforcing any CI policy.
