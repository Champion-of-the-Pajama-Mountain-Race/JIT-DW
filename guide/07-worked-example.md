# 7. A worked reading exercise: finding the right level of explanation

This example uses **public Chromium source code**, not a private pilot project. It demonstrates how to use the Guide when a large codebase already has good documentation at multiple levels. You do not need any JIT-DW tool to follow it.

**Pinned source:** [Chromium `cebb2346`](https://github.com/chromium/chromium/tree/cebb23461ac11d291f8eac596e6b73283c167b4d). The observations below concern this revision, not every later implementation.

## The developer's question

> "I need to post tasks that run in a predictable order. Where should I learn which TaskRunner API to use and what it actually guarantees?"

### First: find the smallest credible starting point

Chromium's [`base/task/README.md`](https://github.com/chromium/chromium/blob/cebb23461ac11d291f8eac596e6b73283c167b4d/base/task/README.md) is short: it maps the public API folder, thread-pool implementation, sequence-manager implementation and shared internals. It also points to a higher-level [threading and tasks guide](https://github.com/chromium/chromium/blob/cebb23461ac11d291f8eac596e6b73283c167b4d/docs/threading_and_tasks.md).

That README is a **navigation document**, not an exhaustive catalog of every method and scheduling edge case. Reading it first tells a developer which layer is relevant.

### Second: inspect the exact interface contract

The [`SequencedTaskRunner` declaration](https://github.com/chromium/chromium/blob/cebb23461ac11d291f8eac596e6b73283c167b4d/base/task/sequenced_task_runner.h#L92-L139) describes sequence ordering and non-overlap guarantees, plus specific conditions involving delays and task nesting.

It does **not** simply promise “every task runs FIFO in every possible circumstance.” The precise conditions matter. This is why an interface comment is the right place to answer an API-contract question: the compiler type alone cannot communicate all scheduling semantics.

If implementing or changing behavior, the next source to read is the corresponding implementation and tests for that specific contract. A documentation page should not silently replace code evidence.

### Third: decide if a new document would help

Imagine a newcomer misunderstood task ordering. Would a brand-new `SEQUENCE_RULES.md` that copies the entire header improve the project?

Maybe not. The short README already points to the subsystem, and the header already defines the behavior. A clear example or a direct link from the task-oriented guide might help **if real readers repeatedly miss the condition**.

The developer can reasonably choose **no extra document** if the existing path answers the task.

## The resulting reading route

~~~text
base/task/README.md                 Which component is responsible?
  → docs/threading_and_tasks.md     How are tasks and sequences used?
  → sequenced_task_runner.h         What ordering behavior is guaranteed?
  → implementation and tests        What does the actual code prove?
~~~

This is a guide to **selecting the right level of evidence**, not a mandate to read every file or create new paperwork.

## Transfer the method

In a different project, try the same pattern:
1. Identify what the reader wants to accomplish or understand.
2. Start with an existing human-scale entry point.
3. Follow references to the nearest authoritative behavior or API contract.
4. Only then decide whether readers truly lack information.

The first independent JIT-DW usability pilot will test whether this reasoning transfers to an unfamiliar boundary in a separate project. Its project-specific source keys and task materials are maintained **privately**; the [public study outline](../validation/pilots/first-private-pilot.md) contains only its methodology.

[Back to the Guide](README.md).
