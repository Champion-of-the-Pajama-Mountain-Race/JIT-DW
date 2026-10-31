# Recipe: a small module README that points somewhere useful

**Use when:** newcomers repeatedly cannot distinguish a component's public entry points from its implementation details or locate the next relevant documentation.

**Don't use when:** the directory contains one obvious file or the existing top-level README already answers the question. No per-directory README requirement.

## Example — fictional job queue component

~~~markdown
# Task queue

This directory owns task submission and dispatch. Callers should use
the public functions in queue/api.py; scheduler.py and storage.py
are implementation details.

## Start here

- To enqueue a task: see the basic example in docs/how-to/submit-task.md.
- To customize retries: see docs/reference/task-options.md.
- To change scheduling: read scheduler.py and its invariant tests.

## Boundaries

A submitted task is accepted for processing, but not guaranteed
to finish successfully. Applications must handle failed tasks.

The queue does not own the user-facing HTTP API.

## Finding the right implementation

- api.py: public requests
- scheduler.py: scheduling logic
- storage.py: persistence
- tests/test_scheduler.py: ordering and retry behavior
~~~

This example is not copied from any project; the paths and behavior are invented solely to illustrate structure. Adapt only the ideas.

## Why this works

A new contributor can answer “Where do I enter?”, “What is internal?”, “What assumption matters?”, and “Where is the next level of detail?” without a per-function catalog.

It is more important to describe *boundaries* than to list every file. Don't repeat a generated API reference or turn the README into a long changelog.

## Real-world comparison

Chromium's [base/task/README](https://github.com/chromium/chromium/blob/cebb23461ac11d291f8eac596e6b73283c167b4d/base/task/README.md) is a short directory map with pointers to conceptual guides. Its interfaces contain the precise call behavior. A large project can use a remarkably short module entry point.

## How to revise it later

When a module's responsibility moves, change the boundary description and key links. Internal file renames that do not affect readers may need no new prose. If the example grows beyond a useful quick orientation, link to a longer explanation instead.

[Back to recipes](README.md).
