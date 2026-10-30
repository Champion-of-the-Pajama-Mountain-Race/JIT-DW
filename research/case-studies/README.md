# Repository case studies

This directory contains source-based field studies. A case study is not a project summary: it is an evidence trail connecting repository artifacts to a specific documentation practice and its trade-offs.

## Required structure

Use CASE-STUDY-TEMPLATE.md. Keep each study narrow enough that another contributor can reproduce the inspection.

## Minimum evidence bar

A useful study should normally include:

- at least one maintained documentation artifact;
- at least one source comment, docstring, schema, or interface annotation;
- at least one test, build rule, CI check, or generated-doc mechanism;
- at least one example of a real change (PR or commit history) when the claim concerns maintenance workflow.

If a category does not apply, say why. Do not invent evidence to fill the template.

## Status labels

- queued — target selected, not inspected;
- in-progress — evidence collection underway;
- review-needed — draft exists but claims need checking;
- evidence-complete — evidence set is sufficient for bounded conclusions;
- published — reviewed and included in the research synthesis.

## Case-study index

| Project | Focus | Status |
|---|---|---|
| Google OpenDocs | Docs Advisor, project archetypes, maturity checklist; compare stated method with artifacts in the repository | queued |
| Linux kernel | kernel-doc comments, in-tree documentation, Sphinx build and contribution workflow | queued |
| Chromium | directory-level documentation, code comments, design docs, ownership and presubmit | queued |
| Rust | rustdoc comments, API docs, compiler/library contribution and documentation tests | queued |
| Python | docstrings, Doc/, developer guide, generated/reference documentation | queued |
| Kubernetes | API comments and generated reference, contributor docs, docs review and release workflow | queued |
| Django | docs tree, source docstrings, release notes, contribution and PR practices | queued |

The queue may change as the initial inspections reveal better or more representative examples.
