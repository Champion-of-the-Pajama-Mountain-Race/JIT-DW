# JIT-DW — Just-in-Time Documentation Workflow

> A practical, evidence-driven workflow for keeping software documentation useful, readable, and aligned with a changing codebase.

**Project status:** Research and design phase. The workflow described here is provisional until it has been checked against real repositories and tested in pilot projects.

JIT-DW is not intended to be another collection of Markdown templates. It aims to help a project decide:

- what documentation is worth maintaining;
- where each kind of information should live;
- who or what owns the information;
- which changes should trigger a documentation review;
- what can be validated automatically, and what still requires human judgment;
- how contributors and coding agents can find authoritative project knowledge without reading everything.

## Current status

This repository deliberately separates three kinds of statements:

| Label | Meaning |
|---|---|
| **Observed practice** | Directly supported by files, source comments, pull requests, tests, or CI in a real project. |
| **Design hypothesis** | A proposed rule that still needs evidence or validation. |
| **JIT-DW decision** | A choice made for this workflow, with its rationale and known trade-offs recorded. |

Do not promote a hypothesis to an observed practice merely because it sounds reasonable or appears in a guide. Research notes must point to the exact repository path, revision, and relevant passage.

## Work areas

- [Project brief](docs/project-brief.md) — goals, non-goals, users, and success criteria.
- [Research method](research/README.md) — how repository-level evidence is collected and evaluated.
- [Field studies](research/case-studies/README.md) — source-based examinations of real projects.
- [Workflow design](docs/workflow/README.md) — the provisional lifecycle and decision points.
- [Design decisions](docs/decisions/README.md) — decisions and unresolved questions.
- [Validation plan](validation/README.md) — how the workflow will be tested in real projects.

## Round 3: Codex / AstrBot source verification

The first two project Forks have successful hosted Runner probes; the existing organization self-hosted Runner is not confirmed eligible for these public Forks. The third research round separates [JIT-DW ideas validated by real source/PR evidence from mechanisms we had not sufficiently modeled](research/round-3/codex-astrbot-comparison.md). Key additions: **machine-consumed docstrings, full generated artifact-tree consistency, actual CI execution/coverage, multilingual UI navigation, and Runner trust boundaries**.

- [Evidence and contrast](research/round-3/codex-astrbot-comparison.md)
- [Validation provenance design](docs/workflow/validation-provenance.md)
- [Actual Runner probes and security boundary](validation/pilots/codex-astrbot/runner-probe.md)

This is still advisory research; passing a Runner probe does not mean the full Codex or AstrBot test suite passed.

## Live pilot preparation — Codex and AstrBot

The first retrospective pilot [compares real Codex and AstrBot PRs](validation/pilots/codex-astrbot/README.md), includes eight pinned change-file fixtures, and runs a [stdlib-only advisory router](tools/jitdw_advisor.py). It deliberately produces reviewer questions, not automatic claims that a documentation file must be edited. Its [test workflow](.github/workflows/jitdw-advisory-tests.yml) runs on JIT-DW pull requests.

Fork-based execution is not yet complete. See the pilot README for the exact fork creation/access blocker, runner assumptions, and measurement plan. No upstream project was modified.

## Current research

- [Repository field-study synthesis V0.2](research/findings-v0.2.md): actual PR/commit evidence and revisions to our hypotheses.
- [Second-round research](research/round-2/README.md): change histories, documentation ownership and review routing, Django end-to-end trace, and tooling drift.
- [Provisional impact-review protocol](docs/workflow/impact-review-protocol.md): a concrete advisory procedure to test in real changes.

This is still research work, not a validated enforcement standard. A passing automated check does not mean the prose is semantically correct.

## Core research question

Can a project keep documentation sufficiently accurate and easy to navigate by connecting documentation work to real development changes—without requiring every code change to update every document, and without creating a larger maintenance burden than the code itself?

We will answer this through repository evidence and pilot use, not by treating published guidelines as proof.

## Working principles (provisional)

1. **Evidence before prescription.** Distinguish what projects actually do from what their guides recommend.
2. **Change relevance over blanket synchronization.** A change should trigger review of the information it can invalidate, not a ritual update of every document.
3. **One authoritative home per fact.** Avoid copying the same volatile fact into multiple documents.
4. **Documentation has different jobs.** Learning, task completion, explanation, and precise reference need different forms.
5. **Local context should stay local.** Put module-specific knowledge near the module when that makes it easier to discover and maintain.
6. **Automation checks what it can prove.** Links, builds, schemas, and executable examples can be checked mechanically; architectural meaning often cannot.
7. **Scale the process to the project.** A small project should not need the governance overhead of a large multi-team codebase.
8. **Treat agents as contributors, not as the audience that replaces humans.** Agent instructions should route to authoritative knowledge, not duplicate it.

These are working hypotheses, not findings. Each will be reviewed against the field studies.

## Intended outputs

1. An evidence-backed research report describing real documentation practices, why they exist, and where published guidance does or does not match repository reality.
2. A reusable workflow kit with lightweight, standard, and advanced adoption paths, templates, checklists, and optional automation.
3. Pilot results showing whether the workflow improves discoverability, change-impact accuracy, and maintenance cost.

## Contributing to the research

When adding a case study, include:

- repository and exact revision or commit;
- exact file paths (and line ranges where practical);
- whether the evidence is a policy, an example, an implementation comment, a test, a CI rule, or observed maintenance history;
- the problem the practice appears to solve;
- trade-offs and counterexamples;
- whether the practice supports, contradicts, or refines a JIT-DW hypothesis.

A link to a generic project homepage is not sufficient evidence for a claim about implementation practice.

## License

License selection is pending. No license should be inferred from this README.
