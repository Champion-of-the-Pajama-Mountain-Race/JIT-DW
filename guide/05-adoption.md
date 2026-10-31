# 5. Adopt the guide at your own scale

The purpose of adoption is to **make writing code and helping its users easier**. Start with the least expensive helpful habit. You do not need to install JIT-DW, restructure the repository, or follow an external approval process.

## An individual project: the smallest starting point

Choose one user task and improve the existing entry point. Often that means:
- a one-paragraph description of what the software does;
- a command or code example that someone can actually run;
- an expected result;
- the main limitation or prerequisite;
- a pointer to the code or command where other details live.

Then return to software development. When you encounter recurring confusion, improve the relevant explanation. There is no obligation to graduate from this approach.

## A collaborative project: lower the cost of orientation

If new contributors repeatedly ask where a feature lives, add a short module map. If a public API is hard to use, put the important contract next to its declaration and add a task example. If decisions are debated over and over, note the consequential ones and link to the current architecture.

You can ask a reviewer “Did this change affect what users do or expect?” without adding a mandatory PR template or a new approval team. Reviewers should help the author make a decision, not replace their judgment.

## A large, multi-language or multi-team project

At sufficient scale, extra mechanisms may save more work than they create:
- generated API references from authoritative schemas;
- clear contribution paths and module-level navigation;
- automatic tests for executable examples or machine-consumed docstrings;
- translation/update guidance for UI task changes;
- scoped review expertise in existing CODEOWNERS/OWNERS systems;
- fast PR checks with heavier follow-up checks where justified.

Codex's [CI strategy](https://github.com/openai/codex/blob/67f0994b532b8740f14b5b738af7b7b2a915b1d6/.github/workflows/README.md) separates fast PR feedback from heavy post-merge verification. This is a useful example of cost-aware testing, not a reason to require large CI configurations in a small project.

## A practical first session (no tools required)

Choose a part of your own project that another developer might need to understand.

1. Try to follow the current README or module entry point as if you were new.
2. Name the first missing answer.
3. Improve one explanation or one piece of self-describing code.
4. Ask someone to try the task or trace the interface.
5. Stop; remember the lesson for the next change.

Success is not “we created three documents.” Success is “a real developer gets unstuck.”

## How to decide whether to add automation

Add a check only after a concrete recurring failure justifies its cost. Examples:
- Broken links in a large site: link checks may help.
- Stale generated API JSON or SDK output: a generator diff check may help.
- Runtime-generated function tool schema: a parser/invocation test may help.
- Unclear concept explanations: an automated rule is unlikely to be enough; a reader review helps more.

Prefer reusing the project's existing build and review practices. In public projects, do not send untrusted PR code to a persistent private self-hosted Runner just to run documentation checks.

## Signals the process is getting too heavy

- Contributors must write a document to justify not writing a document.
- A reviewer can block a useful change solely because a template section is empty.
- The same technical detail is copied into several human-authored places because the policy demands it.
- A newly introduced check produces more busywork than useful corrections.
- Authors optimize for green badges rather than for the user task.
- The Guide is no longer useful when its optional tool is removed.

When these symptoms appear, delete requirements before adding more tools.

## Measuring improvement without rewarding paperwork

Choose outcomes close to actual use: time to first successful task, number of times a maintainer needs to repeat an explanation, discoverability of a public entry point, and the effort needed to update a changing reference.

These are goals for a pilot, not outcomes already demonstrated by JIT-DW. No measured broad improvement has yet been established.

Return to [Guide home](README.md) or explore [real project lessons](06-case-lessons.md).
