# 1. When to document — and when not to

**The question is not “What document is missing?”** It is “What should another person be able to do or understand that they cannot reliably do or understand today?”

## Begin with a reader problem

Consider one of these signals:
- A new contributor cannot run the project or find the subsystem entry point.
- A user can call an API but cannot predict its errors, defaults, security constraints, or compatibility.
- A maintainer repeatedly explains the same non-obvious reason in reviews.
- An operator must recover from a failure and the steps are scattered across chat messages.
- An interface or UI has changed and an existing instruction now leads someone to the wrong place.

If none apply, do not invent a documentation project simply because a template exists. The next useful improvement may be a better name, a more obvious API, an executable test, or nothing at all.

## Pick the smallest useful intervention

| Situation | Possible first intervention | Don't immediately do |
|---|---|---|
| A small utility has no entry point | One README: purpose, setup, use, limits | A documentation site and full architecture wiki |
| A helper is hard to understand | Improve names or split an unclear contract; add one why-comment if needed | A prose paraphrase of each line |
| People misuse a public API | One example and its important failure/compatibility rules | A large tutorial unrelated to the actual confusion |
| A directory has several subsystem boundaries | A short directory map and pointers | One documentation file for every source file |
| A cross-team decision is repeatedly reopened | A brief rationale/decision note | An ADR for every trivial change |
| A CLI command or config option changes | Update actual help text or the generated reference, plus task guidance if affected | Recopy the same argument table into several hand-maintained pages |
| One isolated internal optimization preserves observable behavior | Usually no new user documentation | A compulsory “docs changed” checkbox |

**Decision ownership:** the implementer and relevant maintainers decide what is useful. These rows are suggestions, not release-blocking classifications.

## Three entry scenarios

### A. One-person project

Start with a README that answers what this does, how to try it, and how to tell success from failure. If someone asks the same question twice, improve that spot. A single excellent README may remain enough indefinitely.

### B. A growing project

When newcomers get lost, add a directory-level orientation page. When users repeatedly misuse an API, add a reference example or contract beside the public API. Grow only at the point of real friction.

### C. A mature but confusing documentation collection

Do not start by rewriting everything. Choose a high-value reader journey (for example, install → configure → first successful task), repair broken steps, and connect existing references. If critical material is scattered or contradictory, a focused mini-overhaul may help more than tiny edits.

Google OpenDocs distinguishes [incremental iteration, focused mini-overhauls, and full overhauls](https://github.com/google/opendocs/blob/fbc574e261f0cd363a915776e217abced6e7c952/docs_advisor/part_1.md); different resource and urgency constraints justify different approaches. This is an observed guide recommendation, not evidence that every team succeeds with it.

## Know when to stop

A documentation change is often sufficient when the intended reader can:
- find the right starting point;
- perform the task or understand the contract without consulting the author;
- recognize the relevant limitations and failure conditions;
- follow a reliable pointer for details instead of being confronted with repeated prose.

A page does not need to explain the entire codebase. A useful example is more valuable than an inventory that nobody can navigate.

## Quick exercise

Before writing, complete this in your own words (no form or artifact required):

> “A reader who is trying to ___ gets stuck at ___ because ___. The smallest change that would help is ___.”

If the last blank is “rename the function,” that may be the correct documentation decision.

Continue: [Choose where the information belongs](02-where.md).
