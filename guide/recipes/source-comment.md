# Recipe: useful source comments and API contracts

**Use when:** code names and types do not explain a non-obvious reason, invariant, usage constraint, error behavior, or consumer-visible contract.

**Don't use when:** the comment would only translate obvious syntax into prose. Improve the code first when feasible.

## Example 1 — a why-comment

Weak:

~~~python
# Increase the attempt count.
attempts += 1
~~~

Better, if this invariant actually exists:

~~~python
# Count only requests accepted by the remote service. Local connection
# failures do not consume the server-side retry budget.
if response.accepted:
    attempts += 1
~~~

This is an illustrative snippet, not a claim about a real project's retry contract. Such an invariant merits a test if it is important.

## Example 2 — document the public behavior, not the function's syntax

~~~python
import json
from pathlib import Path

def read_config(path: str) -> dict:
    """Load a JSON object from a local file.

    Raises:
        FileNotFoundError: The path does not exist.
        ValueError: The file is not valid JSON or its root is not an object.
    """
    with Path(path).open(encoding="utf-8") as stream:
        data = json.load(stream)
    if not isinstance(data, dict):
        raise ValueError("Configuration root must be a JSON object")
    return data
~~~

This example is complete enough to run and deliberately documents errors the implementation can produce (JSON decoding errors are subclasses of ValueError). The interface's actual errors and return semantics must match the explanation. Do not add irrelevant Args/Returns sections simply to fill a template unless the project or runtime parser needs them.

## Example 3 — when a docstring is actually executable

In AstrBot, the [LLM tool registration path](https://github.com/AstrBotDevs/AstrBot/blob/734b357fe30963365494df0c0603844e708730f3/astrbot/core/star/register/star_handler.py#L650-L700) parses docstring Args metadata into tool parameter schemas. Its [developer guide](https://github.com/AstrBotDevs/AstrBot/blob/734b357fe30963365494df0c0603844e708730f3/docs/en/dev/star/guides/ai.md#L174-L200) gives the exact syntax and warns of silently dropped arguments when metadata is malformed.

For such APIs, the docstring is **not optional prose**. Follow that parser's conventions and test the generated schema. Do not assume every Python docstring has this property.

## Example 4 — a self-documenting API instead of more comments

~~~rust
// Illustrative alternatives.
set_retry_policy(/*enabled*/ false);
// If the public API can be changed safely:
set_retry_policy(RetryPolicy::Disabled);
~~~

Codex's [argument-comment-lint README](https://github.com/openai/codex/blob/67f0994b532b8740f14b5b738af7b7b2a915b1d6/tools/argument-comment-lint/README.md) explicitly recommends an enum, named helper or self-explaining type before adding parameter hint comments in ambiguous Rust call sites. If compatibility prevents the refactor, a short checked hint can still help.

## A useful stopping test

Ask: “If this comment is removed, what important misunderstanding becomes more likely?” If you have no concrete answer, deleting it may improve the source.

[Back to recipes](README.md).
