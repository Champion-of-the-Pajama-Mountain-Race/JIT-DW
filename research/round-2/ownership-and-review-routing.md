# Ownership and review routing in real repositories

**Status:** Verified configuration patterns; actual notification and approval outcomes are not established unless specific review evidence is given.  
**Inspection:** 2026-10-31.

## Core question

Do mature codebases maintain separate responsibilities for every document or file, or can they route changes by topic, subsystem, and review policy?

The inspected projects use markedly different mechanisms. Treating all of them as "the owner of a file" would erase differences that matter operationally.

## 1. CPython — topical CODEOWNERS joins implementation, tests, and docs

- [CODEOWNERS purpose and interpretation](https://github.com/python/cpython/blob/4a9b98115fec4d93c32c554aa541d6c3fc4c3b27/.github/CODEOWNERS#L13-L31)
- [Heapq group](https://github.com/python/cpython/blob/4a9b98115fec4d93c32c554aa541d6c3fc4c3b27/.github/CODEOWNERS#L483-L489)

CPython expressly warns that an entry in CODEOWNERS does **not** imply ownership in an exclusive sense. The named contributors take an interest in that part of the project and are automatically added as reviewers to matching PRs.

Its structure asks contributors to keep related code, documentation, and tests together. The Heapq group maps a common reviewer to:
- `Doc/library/heapq*`
- `Lib/heapq.py`
- `Lib/test/test_heapq.py`
- `Modules/_heapqmodule.c`

**Observed:** A common topic spans language implementation, tests, and documentation in routing configuration.  
**Inference:** This reduces the chance that reviewers know only one documentation representation of the API.  
**Not proven:** Whether an individual reviewer is available or whether every update to those paths receives a sufficiently deep semantic review.

## 2. Chromium — OWNERS scopes expertise by component and role

- [base/task/OWNERS](https://github.com/chromium/chromium/blob/cebb23461ac11d291f8eac596e6b73283c167b4d/base/task/OWNERS)
- [docs/OWNERS](https://github.com/chromium/chromium/blob/cebb23461ac11d291f8eac596e6b73283c167b4d/docs/OWNERS)
- [page_content_annotations/OWNERS](https://github.com/chromium/chromium/blob/cebb23461ac11d291f8eac596e6b73283c167b4d/components/page_content_annotations/OWNERS)

The base/task OWNERS file says it covers public-facing APIs, while implementation details of ThreadPool and SequenceManager should use the subfolder OWNERS. The component OWNERS file combines human reviewers with references to other OWNERS files. The docs OWNERS file contains wildcard and per-file routing rules.

**Observed:** Responsibility is scoped by component or subcomponent, not by one Markdown responsibility record for each source file.  
**Inference:** Reviews can be routed to the team most likely to know whether a changed contract is correct.  
**Not proven:** A reviewer routing rule by itself does not establish that the right documentation change happened in the CL.

## 3. Kubernetes — separate reviewer, approver, label, and inheritance logic

- [Root OWNERS](https://github.com/kubernetes/kubernetes/blob/f2319f5ce54c9eb4c0438837698fa70e22e34b36/OWNERS#L1-L35)
- [API OWNERS](https://github.com/kubernetes/kubernetes/blob/f2319f5ce54c9eb4c0438837698fa70e22e34b36/staging/src/k8s.io/api/OWNERS#L1-L25)
- [Docs OWNERS](https://github.com/kubernetes/kubernetes/blob/f2319f5ce54c9eb4c0438837698fa70e22e34b36/docs/OWNERS)
- [OWNERS_ALIASES](https://github.com/kubernetes/kubernetes/blob/f2319f5ce54c9eb4c0438837698fa70e22e34b36/OWNERS_ALIASES#L1-L22)

Kubernetes does not model responsibility as a single "owner" field. The configuration distinguishes reviewers, approvers, required reviewers, aliases, labels, and inheritance.

The API OWNERS file explicitly disables parent-owner inheritance, routes API reviews through api-reviewers/api-approvers aliases, and labels Go source changes `kind/api-change`. The docs OWNERS file also disables parent inheritance and has separate reviewers and approvers.

**Observed:** A code change can route differently from an edit under docs; labels are not approvals.  
**Inference:** Some cross-domain changes need coordination across more than one ownership scope.  
**Not proven:** A `kind/api-change` label does not by itself mean that documentation was generated or checked.

## 4. Linux — patch routing by maintainer records and paths

- [MAINTAINERS format](https://github.com/torvalds/linux/blob/a9547379cb381e2a036e3261a6becc17973ac470/MAINTAINERS#L1-L55)
- [get_maintainer.pl](https://github.com/torvalds/linux/blob/a9547379cb381e2a036e3261a6becc17973ac470/scripts/get_maintainer.pl#L1-L12)

The MAINTAINERS file distinguishes maintainers, designated reviewers, mailing lists, status, file glob patterns, exclusions, and optional subsystem profiles. The `get_maintainer.pl` script explicitly accepts a patch or file path and prints selected maintainer information.

**Observed:** Owner discovery is part of the patch-submission path.  
**Inference:** Document changes can be routed by their affected subsystem and file patterns rather than manually maintained per-document ownership prose.  
**Not proven:** The script output has not been executed for the kref change in this research environment, so we do not assert exactly who it would select.

## 5. Rust — automated labeling is not review approval

- [triagebot.toml rustdoc routing](https://github.com/rust-lang/rust/blob/92b5b8c87c61b20adc9001b41baf587634a74734/triagebot.toml#L251-L282)
- [triagebot PR assignment](https://github.com/rust-lang/rust/blob/92b5b8c87c61b20adc9001b41baf587634a74734/triagebot.toml#L1631-L1640)

Rust's triagebot configuration labels rustdoc-related files across source, tests, tools, and documentation paths. It also has a separate PR assignment configuration.

**Observed:** Paths and labels can encode area expertise across code, tests, and docs.  
**Not proven:** An automated label is not evidence that a reviewer approved the change or that API prose is correct.

## 6. Django — review discussion can reveal impact beyond path mapping

- [HTTP QUERY feature PR](https://github.com/django/django/pull/21855)
- [Reviewer asks about additional tests](https://github.com/django/django/pull/21855#discussion_r3911676051)
- [Reviewer asks about middleware coverage](https://github.com/django/django/pull/21855#discussion_r3911767581)
- [Discussion of caching scope](https://github.com/django/django/pull/21855#issuecomment-5592467312)

The actual discussion contains questions about behavior, not merely paths. Reviewers asked for tests around new method acceptance, middleware behavior, redirects, and related documentation. The merged PR has a broad code/docs/test change set and release notes describing explicit limitations.

**Observed:** Human review identifies semantic edges not recoverable from the changed-file list alone.  
**Not proven:** We cannot attribute every final line of code solely to a particular review comment without tracing individual patch revisions.

## 7. Proposed JIT-DW distinction

| Mechanism | Its job | What it cannot prove |
|---|---|---|
| Information authority | Locate the maintained definition of a fact | That readers can discover it |
| Expertise routing | Select reviewers who understand a subsystem | That the documentation is complete |
| Approval rule | Specify who may accept a change | That no semantic defect remains |
| Label/notification | Flag a change as relevant to a domain | That the domain was thoroughly reviewed |
| Mechanical check | Verify explicitly testable properties | That prose is accurate or useful |
| Semantic review | Assess behavior, impact, and explanation | That every downstream reader task succeeds |

**Design consequence:** JIT-DW should not require a standalone owner table for each document. Instead, use the existing repository routing rules where possible and add documentation-specific responsibility only for real gaps (for example, cross-team runbooks or a hand-authored interface reference with no natural code owner).
