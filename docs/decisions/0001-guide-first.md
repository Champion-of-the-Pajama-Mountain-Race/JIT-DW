# Decision 0001: JIT-DW is a Guide first, not an audit system

**Status:** Adopted as the working product direction (2026-10-31).  
**Scope:** JIT-DW's own presentation, authoring priorities, workflow and optional tools. Not a mandate imposed on downstream repositories.

## Context

The first three research rounds emphasized change-impact analysis, CI coverage and documentation consistency. Those findings were valuable, but the project was starting to optimize for inspection and policy rather than helping people write and maintain useful documentation.

The central question is broader: **How can a contributor make good documentation decisions naturally while designing, writing, and evolving software?** Many effective choices involve writing less, improving code structure, or choosing a more useful reader-facing explanation—not adding a control.

## Options considered

1. **Audit-first:** Build a documentation impact classifier, gate and compliance reports, then write usage documentation around it.
   - Pros: mechanically measurable on selected failure types.
   - Cons: risks turning optional guidance into rigid process; cannot prove clarity or usefulness.
2. **Template-first:** Ship many reusable document templates.
   - Pros: concrete, easy to copy.
   - Cons: encourages empty sections and fixed layouts even where a short README is enough.
3. **Guide-first with optional tooling (chosen):** Teach decisions, examples and trade-offs first, with research supporting the advice and tools addressing specific recurring failures.
   - Pros: keeps developer judgment central; can be adopted without installation or extra files.
   - Cons: harder to measure with simple CI badges; depends on actual reader-task feedback.

## Decision

JIT-DW's primary deliverable is a **developer documentation practice Guide**.

The navigation order is:
1. Guide: when, where, how and how much to document.
2. Recipes and worked examples: concrete but optional ways to start.
3. Real project cases: observed mechanisms, trade-offs and counterexamples.
4. Research and evidence: support for conclusions and identified uncertainty.
5. Optional automation/validation: accessories, never prerequisites for adopting the Guide.

The contributor who changes code owns the first judgment about what is worth explaining, informed by user needs, review, project conventions and risks. JIT-DW does not claim authority over the project maintainer.

## Consequences

- No default mandatory doc-per-file, PR documentation proof, audit score or compliance gate.
- “No additional documentation” can be a good outcome; better code, names or tests may be the best response.
- The advisory classifier is **demoted** to optional experimental tooling; it must not dictate Guide structure.
- Existing case studies, runner probes, and CI work are kept for research and reproducibility rather than deleted.
- New research should answer “What can a developer learn and when should they use it?” before “What new rule can be automated?”
- Evaluation prioritizes reader task completion, discoverability, writing effort and maintenance friction over number of audit findings.

## What would make us revisit this?

Real user feedback that the Guide is too vague to use, that it costs more than it saves, or that a narrowly scoped tool consistently prevents an important real failure. An eventual automation-heavy subproject may exist, but should not quietly redefine JIT-DW's identity.

## Source context

- [Google OpenDocs: choose an approach by resources and urgency](https://github.com/google/opendocs/blob/fbc574e261f0cd363a915776e217abced6e7c952/docs_advisor/part_1.md)
- [Django: documentation types and reader tasks](https://github.com/django/django/blob/f4c65fd6a517dd32bd2e732ae3543e550e56f206/docs/internals/contributing/writing-documentation.txt)
- [Chromium: compact module navigation](https://github.com/chromium/chromium/blob/cebb23461ac11d291f8eac596e6b73283c167b4d/base/task/README.md)
- [Codex: favor self-documenting APIs over comment clutter](https://github.com/openai/codex/blob/67f0994b532b8740f14b5b738af7b7b2a915b1d6/tools/argument-comment-lint/README.md)

These support individual design insights; they do not independently prove this decision improves JIT-DW outcomes.
