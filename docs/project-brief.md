# Project brief — Guide-first JIT-DW

**Status:** Working product direction, adopted 2026-10-31. [Decision record](decisions/0001-guide-first.md).

## Purpose

Help a developer **choose, write, place, and maintain the smallest useful explanation at the moment it is needed**. Reduce the cognitive cost of helping readers understand and use software. JIT-DW is a practical Guide; source research and optional tools support it.

The core problem is not that repositories have too few Markdown files. Readers get stuck because critical concepts, entry points, boundary conditions or task steps are unclear, scattered, outdated, or expressed in the wrong place. Authors may respond by creating more documents and process than the project needs.

## Primary users

- An individual building a useful project and deciding whether a README is already enough.
- A contributor implementing a change and wondering what explanation might have become stale.
- A maintainer helping a new developer navigate subsystem boundaries.
- A technical writer collaborating with engineering teams on tutorials and reference docs.
- A coding agent following the project's real design conventions, not inventing additional compulsory files.

The coding contributor and project maintainers retain authority over technical decisions. JIT-DW does not veto code or prescribe a universal directory layout.

## What we ship

1. **[Guide](../guide/README.md):** when to document, where information belongs, how to write for actual tasks, how to maintain without ceremony, and how to adopt incrementally.
2. **[Optional recipes](../guide/recipes/README.md):** small, explained examples, including when *not* to use a recipe.
3. **[Research and evidence](../research/README.md):** source-backed observations from mature projects, alternative approaches, trade-offs and honest uncertainty.
4. **[Optional tools](../tools/jitdw_advisor.py):** narrowly scoped helpers for recurring mechanical failures. They are neither mandatory nor sufficient to judge documentation quality.

Guide is the product; research is evidence; tooling is an accessory.

## Explicit non-goals

- Make a documentation audit, compliance scorecard or merger gate the product.
- Require one README, ADR, contract or comment per file, module or PR.
- Force developers to justify every decision not to create documentation.
- Replace competent technical judgment with path heuristics.
- Require a documentation website, single language, specific renderer or agent plugin.
- Assume comments are always passive prose; some frameworks parse comments as runtime input.
- Infer documentation quality from CI success, file count, or a checklist completion rate.

## Product constraints

1. A developer should get value from reading one Guide chapter without installing anything.
2. Prefer improving code names, APIs, errors or examples over unnecessary explanatory duplication.
3. Write for an identifiable reader task; make useful exceptions and alternatives visible.
4. Keep technical facts near their true source, while allowing deliberate reader-oriented summaries.
5. Use real examples and distinguish what was observed from what JIT-DW recommends.
6. Add automation only when a concrete recurring failure justifies its overhead.
7. Keep historical decisions separate from current behavior; existing research is not a mandatory workflow.

## Evaluation

A useful Guide should help people complete a first task, find the right code, understand important failure modes, make sensible documentation choices and maintain explanations without excessive work. Measure reader success, wrong turns, time spent, unnecessary artifacts and author autonomy in pilots.

Early Codex/AstrBot retrospective checks and CI probes only demonstrate mechanical behavior of an **optional advisory prototype**, not the Guide's impact on reader or author performance. The [validation plan](../validation/README.md) needs Guide-only usability trials.

## Open questions

- Can independent developers apply the Guide to a real code change without feeling compelled to add documentation?
- Does the Guide help people recognize when to improve code rather than document around it?
- How much context and example detail is enough for novices without frustrating experts?
- Can a project naturally combine languages, interfaces and reader groups without duplicating volatile facts?
- Which optional tests or generators clearly save more work than they cost?
