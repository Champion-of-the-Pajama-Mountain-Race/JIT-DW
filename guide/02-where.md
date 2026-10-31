# 2. Where information belongs

The right location depends on **who needs it, for which task, how quickly it changes, and what can keep it accurate**. There is no universal answer of “put everything near code” or “put everything in a docs site.”

## Start from reader intent, not file extension

| Reader wants to… | Usually start with… | What this surface should do |
|---|---|---|
| Decide whether to use the project | Project README / library front page | Purpose, fit, first working example, important limits |
| Follow a task with an end result | How-to | Prerequisites, steps, expected output, troubleshooting |
| Learn unfamiliar ideas | Tutorial or conceptual explanation | Teach mental model, sequencing and why |
| Look up an API or option | Reference | Specific semantics, defaults, errors, exceptions |
| Understand a subsystem's boundaries | Module/directory README | Responsibility, public entry points, relationships, next links |
| Understand a non-obvious implementation choice | Source-level why-comment or focused design explanation | Rationale and invariant, not line-by-line code narration |
| Understand why a choice was made years ago | Decision record / historical design note | Context, trade-offs and supersession; not necessarily current truth |
| Operate or recover a service | Runbook | Concrete actions, risks, verification and rollback |

Django's [documentation contributor guide](https://github.com/django/django/blob/f4c65fd6a517dd32bd2e732ae3543e550e56f206/docs/internals/contributing/writing-documentation.txt) explicitly separates tutorials, how-tos, topic guides and reference pages because each supports a different reader behavior.

## Layer explanations rather than duplicating everything

A useful arrangement for a multi-module library might be:

~~~text
README.md                   Why use this? How do I try it?
docs/how-to/retry.md        How do I handle a transient failure?
docs/concepts/tasks.md      What is the execution model?
docs/reference/config.md    Which options exist and what do they mean?
src/tasks/README.md         Where is the subsystem boundary?
src/tasks/runner.rs         What does this interface guarantee?
~~~

This is an **illustrative map, not a prescribed tree**. A Python project might put API docs in docstrings; a Go or Rust library may generate reference pages directly from source comments. A tiny project may put all three reader needs in one README.

### A real example of restrained locality

Chromium's [base/task/README](https://github.com/chromium/chromium/blob/cebb23461ac11d291f8eac596e6b73283c167b4d/base/task/README.md) is short. It maps the public API folder, thread-pool implementation, sequence manager, shared internals, and links to broader concepts. It does **not** enumerate every function. Detailed behavioral contracts belong in interfaces such as [sequenced_task_runner.h](https://github.com/chromium/chromium/blob/cebb23461ac11d291f8eac596e6b73283c167b4d/base/task/sequenced_task_runner.h).

The transferable insight is not “every folder needs a README.” It is “a component entry point should orient a newcomer and point to the next appropriate level of detail.”

## Authority is about facts, not monopolizing explanation

Suppose a configuration default is defined in code. Its authoritative value is there. A reference page may show that default, while a how-to explains when to change it. This is useful repetition if it serves different reader tasks.

For volatile values, prefer generated references or links to the source. Where independently written summaries are necessary, make their update triggers understandable. Don't force all readers to inspect a schema to answer a human question.

Likewise, a historical design note should preserve *why* something was proposed, while current docs explain *what the software does now*. Historical and current answers can both be correct when clearly labeled.

## When a comment is not just a comment

Some text becomes program input. AstrBot's [LLM tool registration](https://github.com/AstrBotDevs/AstrBot/blob/734b357fe30963365494df0c0603844e708730f3/astrbot/core/star/register/star_handler.py#L650-L700) parses function docstrings into tool argument schemas. For those APIs, docstring formatting can alter runtime behavior and requires the same care as interface code. Most comments are *not* parsed this way. See [source-comment recipe](recipes/source-comment.md).

## A lightweight placement choice

Before adding a new document, ask:

1. Where would the reader naturally look first?
2. Is the needed fact already defined somewhere trustworthy?
3. Would a short pointer help more than a second copy?
4. Will this surface be changed when the underlying fact changes?
5. Would a better API, error message, or example remove the need for prose?

Choose a location; you need not record a formal owner table to make that choice.

Continue: [Write documentation that people can use](03-how.md).
