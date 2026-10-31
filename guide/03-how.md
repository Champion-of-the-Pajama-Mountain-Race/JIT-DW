# 3. Write documentation that someone can use

A document should help its reader accomplish a specific task, build a mental model, or look up a fact. Completeness is not the same as usefulness.

## Give the reader an early success

For a first-use page, lead with:
1. What this component is for and when someone should use it.
2. The smallest realistic working example, including prerequisites.
3. The expected result and how to recognize it.
4. Constraints, limitations, and links to deeper material.

Rust's [rustdoc writing guide](https://github.com/rust-lang/rust/blob/92b5b8c87c61b20adc9001b41baf587634a74734/src/doc/rustdoc/src/how-to-write-documentation.md) recommends starting with a crate's front page, a role-oriented summary and a practical example. That is a recommendation for Rust library docs, not a universal requirement to document every private helper.

## Different documents deserve different writing styles

- **Tutorial:** lead the reader through a learning experience; don't introduce every internal concept before the first success.
- **How-to:** assume some prior knowledge; focus on a concrete end state, decisions and recovery steps.
- **Explanation:** discuss trade-offs and mental models, with links to precise definitions.
- **Reference:** describe exact inputs, outputs, invariants, errors and versions, without burying them in a story.

The [Django writing guide](https://github.com/django/django/blob/f4c65fd6a517dd32bd2e732ae3543e550e56f206/docs/internals/contributing/writing-documentation.txt) makes this separation explicit. The Good Docs Project [distinguishes concept, task and reference templates](https://github.com/thegooddocsproject/templates/blob/de840b374c57502bf1e99c3ccfe05a858553f99f/README.md). Both are useful lenses; neither requires a separate file for every purpose.

## Prefer clarity in the code when possible

Imagine an API call:

~~~rust
// Illustrative; not copied from a production project.
set_policy(false);
~~~

One option is to explain the mystery with a comment:

~~~rust
set_policy(/*enabled*/ false);
~~~

Another may be to improve the API:

~~~rust
set_policy(Policy::Disabled);
~~~

The third form often communicates intent without maintenance of a separate comment. But changing an API may be impractical or incompatible; in that case a short parameter hint can be worthwhile.

Codex's [argument-comment-lint guide](https://github.com/openai/codex/blob/67f0994b532b8740f14b5b738af7b7b2a915b1d6/tools/argument-comment-lint/README.md) explicitly recommends self-documenting APIs before comment-heavy call sites and explains when checked argument comments are useful.

## Comments should carry information the code cannot

Weak comment:

~~~python
# Increment the retry counter by one.
retries += 1
~~~

More useful comment:

~~~python
# Illustrative: count an attempt only after the server accepts the request,
# so a local connection failure does not consume the retry budget.
if response.accepted:
    retries += 1
~~~

The better comment names a **reason or invariant**. If that rule is critical and testable, write a test too. Do not use a comment to conceal a misleading function name, and do not insist every line needs a justification.

## Write examples readers can actually adapt

An example should:
- use real API names and a realistic setup;
- specify prerequisites and output;
- make important errors and boundaries discoverable;
- avoid invented shortcuts that work only in prose;
- be short enough to understand, but not so short it misleads.

If a snippet cannot execute independently, say what context it omits. A compilation or doctest check proves the behavior exercised by that example, not that the whole explanation is correct.

## Edit by asking the reader's next question

After a draft, imagine the reader pauses at each paragraph. Are they asking “Why does this matter?”, “What should I do next?”, “How do I know it worked?”, or “What happens if it fails?” Supply that answer or a direct link. Remove repeated implementation details that do not serve this task.

## When not to borrow a template

Templates are helpful for repeatable cases, but they can distort simple content. Use [recipes](recipes/README.md) when they save time; delete irrelevant sections. Do not write filler headings just to make a document look complete.

Continue: [Keep documentation aligned with code](04-evolve.md).
