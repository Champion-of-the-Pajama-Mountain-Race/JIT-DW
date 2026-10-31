# JIT-DW: a developer's guide to useful documentation

**Guide v0.1 — practical advice, not a compliance standard.** JIT-DW helps the person or agent changing the software decide what knowledge readers need, when it matters, and where it belongs. You can use this guide with no special tooling, no CI, and no additional documentation files.

## Start with the situation you are in

| You are… | Read | What you will get |
|---|---|---|
| Starting a small project | [When to document](01-when.md) | A minimal starting point and explicit permission not to over-document |
| Unsure whether to add a README, comment, guide, or ADR | [Where information belongs](02-where.md) | A choice based on readers and information lifetime |
| Writing a page, API explanation, or code comment | [Write for actual use](03-how.md) | Examples and editing techniques rather than a required template |
| Changing code in an established project | [Evolve alongside code](04-evolve.md) | A light, judgment-driven way to keep explanations current |
| Introducing documentation practices to a team | [Adopt at your own scale](05-adoption.md) | Low-overhead ways to begin and conditions for adding more process |
| Wondering why a recommendation exists | [Lessons from mature projects](06-case-lessons.md) | Source-linked evidence, alternatives, and cases where not to copy it |
| Wanting to see the whole reading process | [Worked public-source example](07-worked-example.md) | Follow a reader question from a module map to a precise interface contract |
| Wanting a concrete starting page or example | [Recipes](recipes/README.md) | Copyable, optional examples with an explanation of when to use them |

[中文十分钟实践](quickstart.zh-CN.md) · [中文导读](README.zh-CN.md) · [Research sources and limitations](../research/README.md) · [Optional advisory tools](../tools/jitdw_advisor.py)

## The short version

1. **Start with a person trying to do something.** Readers may need to install, extend, debug, operate, or understand the software. Name the task before naming a document.
2. **Use the smallest useful explanation.** One working example, a meaningful name, or a clear comment can be enough. More files are not a success metric.
3. **Put information close to the place where readers need it.** An interface contract often belongs beside an API; an onboarding path belongs where newcomers arrive; a system-wide trade-off needs a wider view.
4. **Prefer readable code to explanatory clutter.** Improve unclear names and interfaces when you can. A comment should add context the code cannot convey, not narrate obvious syntax.
5. **Change documentation when its meaning changes.** Don't require a Markdown change just because a code file changed. Conversely, fix misleading docs even when no code changes.
6. **Let the coding contributor decide.** This guide offers options and evidence. Existing project conventions, actual users, maintainers, and the implementer have the last word.
7. **Use automation as a helper.** A link check or generated-schema comparison is useful when it prevents a real failure. A green check does not prove a reader can understand the result.

## A ten-minute use of JIT-DW

Imagine you added a new optional argument to a public function.

- Ask who will call it and what they may misunderstand.
- If type and name make the behavior obvious, don't restate them in a separate file.
- If it changes defaults, errors, or compatibility, explain those consequences in the source API docs and relevant reference.
- If users need to combine calls to perform a task, add or adjust a working example or how-to.
- If reference pages or SDKs are generated, run the project's regeneration/check process.
- Stop when the affected reader can use the interface and the important constraints are discoverable.

You did not need a new documentation committee, owner table, or JIT-DW installation.

## What this guide is *not*

JIT-DW is not a universal directory standard, documentation gate, mandatory template suite, or demand to annotate every function. Some projects legitimately remain at README level. An intentional absence of additional documentation can be a good design choice.

For an independent assessment of this approach, see the [public pilot methodology](../validation/pilots/first-private-pilot.md); private project details are not published here. The [older workflow research](../docs/workflow/README.md), [impact review protocol](../docs/workflow/impact-review-protocol.md), and [advisory prototype](../tools/jitdw_advisor.py) remain available as **optional supporting material**. They are not steps you must pass before contributing code.

## Evidence and uncertainty

Recommendations here are interpretations of selected real practices, not guarantees. We examined documentation and source in Django, Rust, Chromium, Codex, AstrBot, Linux, CPython, Kubernetes, Google OpenDocs, and The Good Docs Project. [Case lessons](06-case-lessons.md) link to specific evidence and distinguish observed practice from our recommendations. The project has not yet demonstrated a measured improvement in documentation quality or developer time across representative pilots.

**Our design priority:** help developers make better decisions, not increase the number of decisions they must report.
