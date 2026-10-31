# JIT-DW — Just-in-Time Documentation Workflow

> **A developer-first guide to deciding when, where and how to document software — without letting documentation process dictate how code must be written.**

**Status:** Guide v0.1 available for use and feedback. Research-backed, but not yet validated in an independent usability pilot. No tool installation required.

**[Read the Guide](guide/README.md) · [中文导读](guide/README.zh-CN.md) · [Try optional recipes](guide/recipes/README.md)**

## Pick your next step

| Your question | Read |
|---|---|
| Does this project or change need documentation at all? | [When to document — and when not to](guide/01-when.md) |
| Should the explanation be a comment, README, tutorial, API reference or ADR? | [Where information belongs](guide/02-where.md) |
| What makes an explanation genuinely useful? | [Write for actual use](guide/03-how.md) |
| How do I keep docs aligned without another approval pipeline? | [Let documentation evolve with code](guide/04-evolve.md) |
| How should an individual or team adopt this gradually? | [Adopt at your own scale](guide/05-adoption.md) |
| What do mature projects actually do, and why? | [Lessons from mature projects](guide/06-case-lessons.md) |

## The idea

Good documentation is not measured by the number of Markdown files, completed templates or green CI badges. It is measured by whether the person reading it can understand, use, debug or change the software.

JIT-DW helps coding contributors make better choices:

- **Start with reader needs, not required artifacts.** A README may be sufficient indefinitely.
- **Prefer self-explaining code and focused examples.** Adding documentation is not always the best fix.
- **Keep information near its natural source and reader.** A local API comment, a module map and a task guide answer different questions.
- **Update meaning, not files for their own sake.** An internal refactor may require no prose change; a misleading help message deserves correction even without a code-signature change.
- **Protect developer agency.** Project contributors and maintainers retain judgment. JIT-DW recommends; it does not approve or veto their code.
- **Use checks only for genuine, testable failure modes.** The Guide works without CI or the experimental advisory tool.

If you have ten minutes, choose a reader who is stuck, improve the smallest thing that helps them, and stop. See [a practical example](guide/README.md#a-ten-minute-use-of-jit-dw).

## Why we trust these ideas — and what remains unproven

We inspected real source code, documentation structure, issue/PR history, tests and CI from projects including Django, Rust, Chromium, Linux, CPython, Kubernetes, Codex and AstrBot, plus the documentation-methodology projects Google OpenDocs and The Good Docs Project.

Some source-backed lessons:

- [Django distinguishes tutorials, how-tos, concepts and references](guide/06-case-lessons.md#django-organize-around-the-readers-mode) by what a reader is trying to do.
- [Chromium uses a compact directory README](guide/06-case-lessons.md#chromium-orientation-is-not-exhaustive-inventory) rather than an exhaustive source-file catalog.
- [Codex recommends clearer APIs before extra argument comments](guide/06-case-lessons.md#codex-first-improve-the-interface-then-explain-remaining-ambiguity).
- [AstrBot parses some docstrings into executable tool schemas](guide/06-case-lessons.md#astrbot-comments-can-be-program-inputs), showing why their role matters.

These are bounded examples, not proof that JIT-DW reduces documentation effort. We still need readers outside the research team to try the Guide on real tasks.

[Round 4: how evidence became advice](research/round-4/README.md) records that conversion and its limits.

## What's in the repository

| Area | Role |
|---|---|
| [Guide](guide/README.md) | **Primary product:** when, where, how to write, and how to evolve documentation |
| [Recipes](guide/recipes/README.md) | Optional worked examples and reusable starting points |
| [Case studies and research](research/README.md) | Source-backed observations, trade-offs, counterexamples and unresolved questions |
| [Design decisions](docs/decisions/0001-guide-first.md) | Why JIT-DW is Guide-first, and what that means |
| [Workflow research](docs/workflow/README.md) | Previous design exploration and more formal, optional process variants |
| [Validation and pilots](validation/README.md) | Evidence needed to judge usefulness, plus completed tooling probes |
| [Advisory prototype](tools/jitdw_advisor.py) | **Experimental and optional** changed-path prompts, not a documentation gate |

The research and CI work have not been discarded; they now **support** the Guide rather than define what developers must do.

## A note for coding agents

Treat this material as advice about useful explanations, not as an instruction to create docs for every code change. Read the project's actual conventions, relevant code and user-facing behavior first. If better code, tests or a short comment solve the problem, prefer them to unnecessary files. Ask the maintainer about consequential ambiguity instead of silently imposing a new standard.

## Contributing

Improvements to the Guide are welcome, especially:
- a real reader problem and an example showing how the advice helps;
- counterexamples and cases where the guidance creates unnecessary work;
- primary-source evidence from actual project docs, code or PRs;
- clearer recipes with tested commands and honest limitations.

You do **not** need to use the JIT-DW advisory CLI to contribute.

## License

License selection is pending. Do not infer a permission to reuse repo text beyond the rights granted by applicable law or GitHub platform terms until a license is chosen.
