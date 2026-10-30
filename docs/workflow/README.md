# Workflow overview

**Status:** Provisional design. The stages below are hypotheses to test against real repositories and pilot projects.

JIT-DW is a decision workflow, not a requirement to create every possible document. A project should enter only the stages and artifacts that solve a real discovery, coordination, or maintenance problem.

## Lifecycle

~~~text
Understand the project
        |
        v
Assess readers, risks, and existing information
        |
        v
Choose the minimum useful documentation set
        |
        v
Establish authoritative locations and navigation
        |
        v
Develop and change the software
        |
        v
Assess the change's information impact
        |
        +---- no relevant information changed ----> record rationale when needed
        |
        +---- information may have changed --------> update the authoritative artifact
        |
        v
Validate mechanically and review semantically
        |
        v
Observe drift, reader problems, and maintenance cost
        |
        +-------------------- feedback to assessment
~~~

## Stage 1 — Understand

Identify:

- the project's primary users and contributors;
- its language and build ecosystem;
- major subsystems and public boundaries;
- how users install, configure, operate, and extend it;
- where existing documentation and technical knowledge live.

Do not begin by creating a large directory tree. First establish what readers need to do and what information is difficult to discover.

## Stage 2 — Assess

Record the current state, including:

- useful and actively maintained documents;
- duplicated or conflicting explanations;
- undocumented critical paths;
- broken links, examples, or generated references;
- undocumented public interfaces or operational risks;
- existing review, ownership, and CI mechanisms.

An assessment should distinguish missing information from information that exists but is hard to find.

## Stage 3 — Choose the minimum useful set

Select artifacts according to project needs. Possible artifacts include:

- a project entry point;
- contribution and development instructions;
- user tutorials and task-oriented guides;
- API or configuration reference;
- architecture and subsystem explanations;
- module-level contracts;
- decision records;
- operational runbooks;
- code comments and generated documentation.

The list is a menu, not a mandatory checklist. See information-ownership.md before copying the same fact into multiple places.

## Stage 4 — Establish navigation and authority

For every high-value piece of information, decide:

- where it is authored;
- whether it is generated or derived;
- who maintains it (a person, team, or code owner);
- what kind of change can invalidate it;
- how a reader or agent discovers it.

A directory README or index should help a reader navigate; it should not duplicate every detail in the files below it.

## Stage 5 — Change the software and assess information impact

When a change is proposed, ask what facts it changes—not merely which files it touches.

Examples:

- a public signature change may affect API reference, examples, and migration guidance;
- a new dependency boundary may affect architecture and module contracts;
- a changed default may affect user guides, configuration reference, and tests;
- an internal refactor may require no user-facing documentation change, but may still change a module contract or operational assumption.

Use change-impact.md as a provisional decision aid.

## Stage 6 — Validate

Separate two forms of validation:

**Mechanical validation**
- Markdown and documentation build;
- internal and external links, where practical;
- generated reference freshness;
- code examples and snippets;
- schema or API reference consistency;
- required metadata and formatting.

**Semantic validation**
- does the explanation still describe the intended behavior?
- does it match the implementation and tests?
- can the intended reader complete the task?
- are limitations, failure modes, and security implications represented accurately?

A passing build is not proof of semantic correctness.

## Stage 7 — Maintain

Use evidence from issues, support questions, reviews, failed tasks, and code changes to decide what to improve. Review high-risk documents when their underlying interfaces or assumptions change. Avoid periodic review of every document unless the project has evidence that it is useful.

## Adoption profiles (provisional)

These profiles describe process overhead, not maturity rankings.

| Profile | Typical fit | Minimum process |
|---|---|---|
| Lite | Individual or small project | Clear entry point, contribution guidance, local module context where needed, a lightweight impact question in review. |
| Standard | Multi-module project with multiple contributors | Explicit information ownership, selected architecture/module contracts, decision records for consequential choices, PR impact review, basic documentation CI. |
| Advanced | Large or multi-team project | Ownership mapping, generated references, change-impact automation, broader quality checks, agent navigation, and measured maintenance practices. |

A project may use different profiles for different subsystems. These profiles will be revised after field studies.

## Guardrails

- Do not create a document just because a template exists.
- Do not update unrelated documents to satisfy a blanket rule.
- Do not treat a historical design record as the current source of implementation truth.
- Do not duplicate generated API details in manually maintained prose.
- Do not mark an impact assessment as complete merely because the checklist was checked.
- When evidence is uncertain, say so and identify how to verify it.
