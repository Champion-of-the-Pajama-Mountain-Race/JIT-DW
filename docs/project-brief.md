# Project brief

**Status:** Working brief; subject to revision after repository field studies.

## 1. Problem

Software projects accumulate documentation in different places and for different readers. Over time, implementation changes, but the documents that explain it do not always change with it.

The cost is not simply outdated Markdown. The deeper problems are:

- readers cannot tell which document is authoritative;
- contributors do not know which documents a code change may invalidate;
- the same fact is copied into several places and must be synchronized;
- large documentation plans create overhead before a project knows what it needs;
- code comments, generated references, design records, and user guides are often treated as interchangeable;
- automation can validate syntax and links while leaving semantic drift undetected.

JIT-DW investigates whether a change-aware, evidence-backed workflow can reduce these problems without turning documentation into a second codebase that costs more to maintain than the software.

## 2. Goal

Create two usable outputs:

1. **Research:** a repository-level account of how mature open-source projects actually document systems, APIs, modules, decisions, and changes.
2. **Workflow kit:** a reusable process and set of optional templates that help projects create, update, and validate documentation at the point where it is needed.

The workflow must be usable by both human contributors and coding agents, while remaining readable to project users and maintainers.

## 3. Non-goals

JIT-DW will not:

- prescribe one universal directory tree for every project;
- require a separate Markdown file for every source file;
- require every code change to modify documentation;
- claim that a checklist or CI job can prove that documentation is semantically correct;
- replace source code, tests, schemas, or generated API references as authoritative technical sources;
- force every project to adopt a documentation website or a particular toolchain;
- treat a published guideline as evidence that a project consistently follows it.

## 4. Intended users

- maintainers of small and medium open-source projects;
- contributors working across unfamiliar modules;
- teams maintaining multi-module or multi-language systems;
- coding agents that need reliable project context and change instructions;
- technical writers collaborating with engineering teams.

## 5. Working vocabulary

| Term | Working meaning |
|---|---|
| Documentation artifact | A document, code comment, schema, generated reference, runbook, or other maintained explanation. |
| Information owner | The canonical place where a particular fact is defined or maintained. |
| Change impact | The set of information and documentation artifacts that may become incorrect because of a change. |
| Contract | An explicit statement of a module's externally relevant behavior, boundaries, constraints, and failure semantics. |
| Decision record | A durable record of a decision, its context, alternatives, and consequences. |
| Documentation drift | A divergence between maintained documentation and the current intended or actual system. |
| Evidence item | A specific repository artifact or change history that supports or challenges a research claim. |

These definitions are working terminology, not claims that all studied projects use the same terms.

## 6. Success criteria

The project is successful only if its workflow can be used and evaluated. Desired outcomes:

- a contributor can locate the authoritative explanation for a module or interface;
- a maintainer can identify likely documentation impact from a real code change;
- the process distinguishes no documentation change needed from impact not assessed;
- duplicated volatile facts are reduced or explicitly marked as derived;
- automated checks catch mechanical failures without creating false confidence about semantic correctness;
- a small project can adopt the minimum useful subset;
- a larger project can add ownership, dependency mapping, and stronger validation incrementally.

Pilot evaluation methods and metrics are defined in validation/README.md.

## 7. Design constraints

1. Minimize mandatory artifacts.
2. Prefer local context when it improves discoverability.
3. Keep historical rationale separate from current operational truth.
4. Make the update trigger explicit for high-value documentation.
5. Preserve evidence and uncertainty in research outputs.
6. Avoid introducing a central index that becomes a manually maintained copy of the whole repository.
7. Treat generated documents as derived outputs and identify their source inputs.

## 8. Open questions

- How much file-level responsibility information is useful before it becomes expensive to maintain?
- Which project types benefit from module contracts, and what is the minimum useful contract?
- Can a PR checklist reliably distinguish not applicable from not considered?
- What forms of change-impact mapping are maintained in practice: ownership files, dependency graphs, tests, code comments, or reviewer knowledge?
- When should an architectural description live near code, and when should it be centralized?
- How do successful projects prevent decision records from being mistaken for current implementation documentation?
- What information should be exposed to coding agents, and what should remain in human-oriented documentation?

These questions remain open until the field studies and pilots provide evidence.
