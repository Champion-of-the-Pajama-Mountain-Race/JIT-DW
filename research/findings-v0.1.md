# Repository field-study synthesis — V0.1

**Status:** Preliminary synthesis from the first source-based inspection tranche.  
**Evidence scope:** Google OpenDocs, The Good Docs Project, Linux kernel, Chromium, CPython, Rust, Kubernetes, and Django.  
**Important limitation:** These are bounded samples, not exhaustive audits of each project. Several projects still need PR/CL history sampling and broader subsystem checks.

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
| Linux kernel | Structured kernel-doc comments beside declarations | Conceptual guides such as kref | Comment extraction, Sphinx generation, explicit header checks | Source comments can be API documentation when the format and toolchain are designed for it. |
| Chromium | Module README, interface comments, implementation comments | Central docs and design archives | Same-CL policy, Gitiles preview, document index | Layer documentation by scope and reader; avoid treating design proposals as current implementation truth. |
| CPython | Module and function docstrings | Hand-authored Sphinx library reference | Sphinx build tooling | Intentional overlap can serve different reading surfaces; synchronization must be considered. |
| Rust | Public API docs in source comments | rustdoc guides and crate-level narrative | missing_docs lint and executable doctests | Examples can be tested, but tests do not prove prose completeness. |
| Kubernetes | API field comments plus structured markers | Cross-cutting API conventions and exported docs | Field-name checks, generated-doc verification, optional API changelog check | Comments may carry both prose and machine-readable schema metadata; not every check is a hard gate. |
| Django | Source docstrings and implementation comments | Detailed hand-authored topic/reference/how-to docs | Sphinx build/lint; feature PRs with docs, release notes, and tests | User-facing reference can be richer than source docstrings; documentation tooling can drift too. |

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

- Linux kernel-doc comments are an authoring source for generated reference pages.
- Rust source doc comments feed rustdoc, and code examples can be executed.
- Kubernetes field comments and markers describe API semantics and are checked by specialized tooling.
- CPython has overlapping module docstrings and separate library reference pages.
- Django's detailed user reference may be separate from a short source class docstring.
- Chromium uses different artifacts for directory orientation, interface contracts, implementation rationale, and design history.

**JIT-DW implication:** every important fact needs a declared authority or synchronization rule. A reader-facing representation may intentionally repeat or transform information when it serves a distinct use.

### 3.4 Documentation update triggers differ

Evidence includes:

- Chromium's explicit same-CL rule.
- Django's merged feature PRs that update implementation, reference docs, release notes, and tests together.
- Rust PRs that improve documentation directly in source comments.
- Linux's comment placement rule designed to increase the chance of synchronized updates.
- Google OpenDocs' recommendation to treat release notes as part of incremental software-change completion.
- Kubernetes' generated-doc and API-documentation verification scripts.

**JIT-DW implication:** change impact should start from changed behavior, contract, schema, assumption, or procedure—not from changed file names alone. The workflow must allow source-comment-only updates, separate reference updates, generated outputs, deferred updates, and no-update outcomes.

### 3.5 Templates need instructions and boundaries

The Good Docs Project requires a template file and a companion guide, while allowing deep dives and examples to be optional. Google OpenDocs asks for purpose, audience, content, intended outcome, and contributors. Both warn against treating a template as a universal structure.

**JIT-DW implication:** a template should explain when to use it, when not to use it, who it serves, and how to validate the result. Do not make every optional section mandatory.

### 3.6 Automation checks specific properties

Examples:
- Linux extracts and validates structured source comments.
- Rust executes documentation examples and warns about missing public docs.
- Kubernetes checks field-name/documentation mismatches and generated outputs.
- Django uses Sphinx source discovery for docs lint/format checks after duplicated discovery logic drifted.
- Chromium offers preview tooling but also relies on human review.

These checks do not prove that an explanation is accurate, complete, or easy to understand. Rust doctests are stronger than plain syntax checks, but they validate example behavior, not all prose.

**JIT-DW implication:** every automation rule must say exactly what it proves and what it does not prove.

## 4. Initial hypotheses that need revision

| Original hypothesis | Evidence-based revision |
|---|---|
| One fact should appear in only one file. | Prefer one canonical authoring source; allow multiple reader-facing representations when their purpose is explicit and synchronization is managed. |
| Every code change should update documentation. | Every consequential information change should be assessed. Some changes need source comments, some need user docs, some need release notes, and some need no documentation update. |
| Every module should have a module contract. | A local module README or contract is useful when a boundary is meaningful. It is not yet supported as a universal mandatory artifact. |
| Every file needs a responsibility record. | Use directory maps, interface comments, ownership rules, or generated inventories where they provide actual value. Do not create per-file Markdown by default. |
| CI can validate documentation. | CI can validate builds, links, generated output, structured comments, and examples. Semantic accuracy and reader success still need review or task-based evaluation. |
| All docs should be maintained in the same way as code. | Some projects use source docs, some use hand-authored manuals, some generate export artifacts, and some keep pre-implementation design discussion outside the code repository. |

## 5. Design changes recommended for JIT-DW

1. Replace the strict one-source-of-truth rule with **authoritative source + representation map**.
2. Keep the change-impact workflow fact-based and permit an explicit no-update outcome.
3. Define a placement model: project entry point, directory/module overview, interface contract, implementation rationale, user/task/reference docs, decision history, and runbooks.
4. Make module contracts optional and risk-driven until pilot evidence justifies a stronger requirement.
5. Pair substantial templates with a short usage guide; keep deep dives and examples optional.
6. Treat generated docs, executable examples, and structured comments as different automation patterns.
7. Distinguish a documented policy from observed behavior. Continue auditing PR/CL history before claiming compliance.

## 6. What is not yet established

- How often the inspected projects update documentation in the same PR/CL as code.
- Whether local READMEs and central indexes remain current over long periods.
- How much documentation drift is caught by CI versus human review.
- How ownership is assigned to individual docs and source-level comments at scale.
- Whether the JIT-DW profiles reduce maintenance effort in real repositories.
- Whether coding agents benefit from the proposed navigation and change-impact artifacts.

## 7. Next research tranche

1. Sample merged and rejected PRs/CLs from Linux, Chromium, CPython, Kubernetes, and Django to compare stated rules with actual updates.
2. Follow one API or module change through source comments, tests, generated output, user documentation, and release notes.
3. Inspect ownership mechanisms such as OWNERS, CODEOWNERS, directory metadata, and reviewer routing.
4. Build a small change-impact matrix from real changes and compare it with maintainer judgment.
5. Use the evidence to revise the workflow before creating the final template kit.
