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
| Google OpenDocs | Docs Advisor, project archetypes, maturity checklist; distinguish guidance from implementation evidence | evidence-complete |
| The Good Docs Project | Template files, companion guides, taxonomy, and template review process | evidence-complete |
| Linux kernel | kernel-doc comments, in-tree conceptual documentation, Sphinx extraction and validation | evidence-complete |
| Chromium | directory README, interface comments, implementation comments, design-doc lifecycle | evidence-complete |
| CPython | source docstrings versus separately authored Sphinx library reference | evidence-complete |
| Rust | rustdoc comments, missing-doc lint, executable examples | evidence-complete |
| Kubernetes | API comments and markers, API conventions, field-name and generated-doc checks | evidence-complete |
| Django | docs taxonomy, source/reference separation, feature PR and docs tooling history | evidence-complete |

Evidence-complete means sufficient for the bounded scope stated in each case study. It does not mean the entire project has been audited.

## Next tranche

- sample more PRs/CLs to test whether policies match practice;
- inspect ownership mechanisms and actual review routing;
- follow one change end-to-end through source comments, tests, generated docs, user docs, and release notes;
- record examples that contradict the current synthesis.
