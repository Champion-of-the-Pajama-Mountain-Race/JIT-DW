# 6. Lessons from mature projects — what to borrow, and what not to copy

JIT-DW studies real projects because a published style guide alone does not tell us how maintainers actually work. Each lesson separates an **observed artifact** from a **portable interpretation**. Don't copy a solution without the problem that made it useful.

## Django: organize around the reader's mode

**Observed:** Django's [contributor writing guide](https://github.com/django/django/blob/f4c65fd6a517dd32bd2e732ae3543e550e56f206/docs/internals/contributing/writing-documentation.txt) explicitly distinguishes tutorials (learning by doing), how-to guides (complete a task), topic guides (understand a concept), and reference (look up precise behavior).

**Why it is interesting:** These reader activities have different narrative shapes. A huge mixed page can force experts to wade through tutorials and novices to learn from parameter tables.

**Borrow:** Ask what the reader is doing before choosing a page structure.

**Don't copy blindly:** A small library may combine several modes in a concise README rather than opening four documentation directories.

## Rust: write the first useful example before the encyclopedia

**Observed:** The [rustdoc writing guide](https://github.com/rust-lang/rust/blob/92b5b8c87c61b20adc9001b41baf587634a74734/src/doc/rustdoc/src/how-to-write-documentation.md) recommends a crate front-page summary and concrete example, and describes API item docs as summary → details → example → deeper explanation as needed.

**Why it is interesting:** An early example answers whether a component fits the reader's problem before they invest in the entire reference.

**Borrow:** Lead with role and a realistic example, and make failure modes discoverable.

**Don't copy blindly:** A public library's rich API-reference expectation is not the right scope for every private helper.

## Chromium: orientation is not exhaustive inventory

**Observed:** [base/task/README](https://github.com/chromium/chromium/blob/cebb23461ac11d291f8eac596e6b73283c167b4d/base/task/README.md) is a compact map of public API and implementations, with links to other guides. Detailed interface rules live near source in headers such as [sequenced_task_runner.h](https://github.com/chromium/chromium/blob/cebb23461ac11d291f8eac596e6b73283c167b4d/base/task/sequenced_task_runner.h).

**Why it is interesting:** A newcomer needs the boundary and next place to look, not a list of every file.

**Borrow:** Use module READMEs as signposts when multiple paths are otherwise confusing.

**Don't copy blindly:** One README per directory would add maintenance and dilute this signal.

## Codex: first improve the interface, then explain remaining ambiguity

**Observed:** [argument-comment-lint's own README](https://github.com/openai/codex/blob/67f0994b532b8740f14b5b738af7b7b2a915b1d6/tools/argument-comment-lint/README.md) recommends self-documenting APIs first and provides a specialized linter for parameter-name hints only when comments are useful.

**Why it is interesting:** Tools can keep useful comments accurate without creating an obligation to decorate every call.

**Borrow:** Prefer names, types and APIs that carry their own meaning.

**Don't copy blindly:** Specialized Rust compiler lints are costly and inappropriate as a universal documentation policy.

## Codex: generation should remove repetition, not hide the user

**Observed:** [Schema fixture tests](https://github.com/openai/codex/blob/67f0994b532b8740f14b5b738af7b7b2a915b1d6/codex-rs/app-server-protocol/src/schema_fixtures_tests.rs) compare generated file trees, while [PR #57172](https://github.com/openai/codex/pull/57172) updates protocol code, generated clients, tests, and human-facing README information.

**Borrow:** Generate exact machine contracts; hand-write motivation, examples and migration notes when they matter to readers.

**Don't copy blindly:** Not every project needs a schema generator or an API documentation website.

## AstrBot: comments can be program inputs

**Observed:** [Tool registration code](https://github.com/AstrBotDevs/AstrBot/blob/734b357fe30963365494df0c0603844e708730f3/astrbot/core/star/register/star_handler.py#L650-L700) parses docstrings into a tool parameter schema. Its [developer guide](https://github.com/AstrBotDevs/AstrBot/blob/734b357fe30963365494df0c0603844e708730f3/docs/en/dev/star/guides/ai.md#L174-L200) warns of missing or malformed argument descriptions.

**Borrow:** Understand whether a docstring is a human explanation or an executable contract before changing it.

**Don't copy blindly:** Ordinary comments need not all follow a machine schema.

## Google OpenDocs and The Good Docs Project: start with constraints, then templates

**Observed:** [Google OpenDocs](https://github.com/google/opendocs/blob/fbc574e261f0cd363a915776e217abced6e7c952/docs_advisor/part_1.md) compares continuous small improvements, focused overhauls and large overhauls based on resources and urgency. [The Good Docs Project](https://github.com/thegooddocsproject/templates/blob/de840b374c57502bf1e99c3ccfe05a858553f99f/README.md) organizes templates by concept, task and reference and encourages readers to choose by information need.

**Borrow:** Treat methods and templates as a menu, not a compulsory stack.

**Don't copy blindly:** Methodology repositories are advice, not evidence that their recommendations are always followed in production.

## The common lesson

The strongest pattern is **fit between explanation and the work the reader is doing**. Mature projects make different trade-offs because their readers, code, scale and costs are different.

These examples are deliberately selected; they are not a statistical survey. More complete raw evidence, counterexamples and uncertainties are in [research](../research/README.md). Use the Guide to choose, not to conform.
