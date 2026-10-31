# Repository field-study synthesis — V0.1

**Status:** Preliminary synthesis from the first source-based inspection tranche.  
**Evidence scope:** Google OpenDocs, The Good Docs Project, Linux kernel, Chromium, CPython, Rust, Kubernetes, and Django.  
**Important limitation:** These are bounded samples, not exhaustive audits of each project. Some projects still need more PR/CL history sampling and broader subsystem checks.

## 1. Executive finding

The original theory was too tidy. Mature projects do not use one universal documentation architecture, one universal source of truth, or one universal update rule.

What they do share is a set of practical distinctions:

- different information belongs at different levels;
- readers need different document forms;
- source comments, generated references, narrative docs, tests, and design records have different jobs;
- documentation changes are triggered by changed information, not simply by the fact that a file changed;
- automation checks narrow, provable properties, while human review still handles meaning and usefulness.

The most important correction to JIT-DW is this:

**We should model information authority and representation separately. One fact may have a canonical authoring source and several intentionally maintained reader-facing representations.**

A strict one-file-per-fact rule would misdescribe CPython, Django, and projects that publish source comments through generated reference pages.

## 2. Cross-project comparison

| Project | Source-level practice | Separate documentation | Automation / maintenance evidence | Main lesson |
|---|---|---|---|---|
| Google OpenDocs | Not a codebase example | Archetypes, planning guide, maturity checklist | Planning and evaluation guidance | Choose documentation work according to audience, resources, and project condition. |
| The Good Docs Project | Not a codebase example | Concept/task/reference templates with companion guides | Defined template authoring and review roles | A reusable template needs usage guidance and an appropriate scope. |
| Linux kernel | Structured kernel-doc comments beside declarations | Conceptual guides such as kref | Comment extraction, Sphinx generation, explicit header checks; one commit fixed missing HTML integration | Source comments need both proximity and a maintained path into reader-facing docs. |
| Chromium | Module README, interface comments, implementation comments | Central docs and design archives | Same-CL policy; one refactor updated the component README in the same commit | Layer documentation by scope and reader; avoid treating design proposals as current implementation truth. |
| CPython | Module and function docstrings | Hand-authored Sphinx library reference | Separate commits update source and reference surfaces | Multiple reader surfaces can be valid, but their independent maintenance must be visible. |
| Rust | Public API docs in source comments | rustdoc guides and crate-level narrative | missing_docs lint and executable doctests; a docs-only API comment PR | Examples can be tested, but tests do not prove prose completeness. |
| Kubernetes | API field comments plus structured markers | Cross-cutting API conventions and exported docs | Field-name checks, generated-doc verification, optional API changelog check; one change updated six API type files | Comments may carry prose and machine-readable schema metadata; replicated API representations need coordinated updates. |
| Django | Source docstrings and implementation comments | Detailed hand-authored topic/reference/how-to docs | Sphinx build/lint; feature PRs with docs, release notes, and tests; docs tooling drift fix | User-facing reference can be richer than source docstrings; documentation tooling can drift too. |

## 3. What the evidence supports

### 3.1 Documentation is layered, not flat

The strongest explicit model comes from Chromium:

- directory/module README for purpose and navigation;
- interface/class comments for contracts and usage;
- implementation comments for non-obvious reasoning.

Linux and Rust show a different but compatible layer: structured comments attached to declarations can become API reference documentation. Django and CPython show that some user-facing references remain separate, hand-authored documents.

**JIT-DW implication:** define placement by information type and reader context. Do not force every explanation into a central manual or every fact into source comments.

### 3.2 A per-file Markdown responsibility map is not supported as a default

The inspected examples use:
- a component README to map a meaningful directory;
- comments beside public declarations;
- module docstrings;
- generated API reference;
- broader architecture or conceptual guides.

None of the inspected examples supports creating a separate Markdown responsibility document for every source file as a universal default.

**JIT-DW implication:** file-level responsibility should be expressed only where it changes discovery, review, or maintenance. A directory map, ownership file, API comment, or generated code map may be sufficient.

### 3.3 Source of truth is a relationship, not always one file

Evidence shows several patterns:

- Linux kernel-doc comments are an authoring source for generated reference pages, but a separate kref.rst inclusion was needed to make those comments appear in the HTML manual.
- Rust source doc comments feed rustdoc, and doctests validate examples.
- Kubernetes field comments and markers describe API semantics; one change replicated a clarification across six internal and versioned type files.
- CPython has overlapping module docstrings and separate library reference pages, with separate commits touching each surface.
- Django's detailed user reference may be separate from a short source class docstring.
- Chromium uses different artifacts for directory orientation, interface contracts, implementation rationale, and design history.

**JIT-DW implication:** every important fact needs a declared authority or synchronization rule. A reader-facing representation may intentionally repeat or transform information when it serves a distinct use.

### 3.4 Documentation update triggers differ

Evidence includes:

- Chromium's explicit same-CL rule and a ThreadPool refactor that updated base/task/README.md in the same commit.
- Django's merged feature PRs that update implementation, reference docs, release notes, and tests together.
- Rust PRs that improve documentation directly in source comments.
- Linux's kref commit, which changed source comments and the Sphinx page that includes them.
- Kubernetes' comment update replicated across internal and versioned API types.
- Google OpenDocs' recommendation to treat release notes as part of incremental software-change completion.

**JIT-DW implication:** change impact should start from changed behavior, contract, schema, assumption, or procedure—not from changed file names alone. The workflow must allow source-comment-only updates, separate reference updates, generated outputs, deferred updates, and no-update outcomes.

### 3.5 Templates need instructions and boundaries

The Good Docs Project requires a template file and a companion guide, while allowing deep dives and examples to be optional. Google OpenDocs asks for purpose, audience, content, intended outcome, and contributors. Both warn against treating a template as a universal structure.

**JIT-DW implication:** a template should explain when to use it, when not to use it, who it serves, and how to validate the result. Do not make every optional section mandatory.

### 3.6 Automation checks specific properties

Examples:
- Linux extracts and validates structured source comments.
- Rust executes documentation examples and warns about missing public docs.
- Kubernetes checks field-name/documentation mismatches and generated outputs; its Go API changelog checker is explicitly optional.
- Django uses Sphinx source discovery for docs lint/format checks after duplicated discovery logic drifted.
- Chromium offers preview tooling but also relies on human review.

These checks do not prove that an explanation is accurate, complete, or easy to understand. Rust doctests are stronger than plain syntax checks, but they validate example code, not all prose.

**JIT-DW implication:** every automation rule must say exactly what it proves and what it does not prove.

## 4. Real change-history snapshots

These examples test whether written rules connect to actual repository changes:

| Project | Change observed | What it demonstrates | What it does not prove |
|---|---|---|---|
| Linux kernel | [kref documentation commit](https://github.com/torvalds/linux/commit/b76d32422c09bc9310f61a5a89671975db34bd2a) | Source comments and the Sphinx inclusion page were updated together after maintainers noticed the comments were not linked into HTML docs. | That all kernel APIs receive the same treatment. |
| Chromium | [ThreadPool rename commit](https://github.com/chromium/chromium/commit/43fd37033b05a48a6f2f3f87fdb844844d84e650) | A broad code refactor updated the component README in the same commit. | That all Gerrit CLs comply with the same-CL policy. |
| CPython | [heapq source docstring commit](https://github.com/python/cpython/commit/659cb7e6b8e83e1541fc27fd29d4846e940b600e) and [heapq reference commit](https://github.com/python/cpython/commit/9bf5100037f661f3a369d3ee539bec06f063b650) | The source docstring and reference page are separately maintained change surfaces. | That the two specific changes caused drift; they were different changes. |
| Kubernetes | [perContainer API comment commit](https://github.com/kubernetes/kubernetes/commit/cef7481431757c32ddeb07fad52551e27493bb79) | One semantic clarification was copied into six internal/versioned API type files in one commit. | That all duplicated API comments are always synchronized. |
| Rust | [rustdoc API documentation PR](https://github.com/rust-lang/rust/pull/126428) | API documentation can be improved directly in source comments without changing a separate user manual. | That doctests validate all semantic claims. |
| Django | [feature PR #21855](https://github.com/django/django/pull/21855), [feature PR #21357](https://github.com/django/django/pull/21357), [docs tooling PR #22111](https://github.com/django/django/pull/22111) | Feature changes can bundle code, docs, release notes, and tests; documentation tooling itself also needs a source of truth. | That every feature PR is complete or that all doc drift is detected. |

The history samples matter because a static documentation policy cannot show whether maintainers actually update documents with code. They are still samples, not compliance statistics.

## 5. Initial hypotheses that need revision

| Original hypothesis | Evidence-based revision |
|---|---|
| One fact should appear in only one file. | Prefer one canonical authoring source; allow multiple reader-facing representations when their purpose is explicit and synchronization is managed. |
| Every code change should update documentation. | Every consequential information change should be assessed. Some changes need source comments, some need user docs, some need release notes, and some need no documentation update. |
| Every module should have a module contract. | A local module README or contract is useful when a boundary is meaningful. It is not yet supported as a universal mandatory artifact. |
| Every file needs a responsibility record. | Use directory maps, interface comments, ownership rules, or generated inventories where they provide actual value. |
| CI can validate documentation. | CI can validate builds, links, generated output, structured comments, and examples. Semantic accuracy and reader success still need review or task-based evaluation. |
| All docs should be maintained in the same way as code. | Some projects use source docs, some use hand-authored manuals, some generate export artifacts, and some keep pre-implementation design discussion outside the code repository. |

## 6. Design changes recommended for JIT-DW

1. Replace the strict one-source-of-truth rule with **authoritative source + representation map**.
2. Keep the change-impact workflow fact-based and permit an explicit no-update outcome.
3. Define a placement model: project entry point, directory/module overview, interface contract, implementation rationale, user/task/reference docs, decision history, and runbooks.
4. Make module contracts optional and risk-driven until pilot evidence justifies a stronger requirement.
5. Pair substantial templates with a short usage guide; keep deep dives and examples optional.
6. Treat generated docs, executable examples, and structured comments as different automation patterns.
7. Distinguish a documented policy from observed behavior. Continue auditing PR/CL history before claiming compliance.

## 7. What is not yet established

- How often the inspected projects update documentation in the same PR/CL as code.
- Whether local READMEs and central indexes remain current over long periods.
- How much documentation drift is caught by CI versus human review.
- How ownership is assigned to individual docs and source-level comments at scale.
- Whether the JIT-DW profiles reduce maintenance effort in real repositories.
- Whether coding agents benefit from the proposed navigation and change-impact artifacts.

## 8. Next research tranche

1. Sample more merged and rejected PRs/CLs from Linux, Chromium, CPython, Kubernetes, and Django to compare stated rules with actual updates.
2. Follow one API or module change through source comments, tests, generated output, user documentation, and release notes.
3. Inspect ownership mechanisms such as OWNERS, CODEOWNERS, directory metadata, and reviewer routing.
4. Build a small change-impact matrix from real changes and compare it with maintainer judgment.
5. Use the evidence to revise the workflow before creating the final template kit.
