# Round 4: turning repository evidence into a developer Guide

**Status:** Guide v0.1 authored from already collected field evidence; no usability pilot or measured impact claim.  
**Date:** 2026-10-31.

## Why a course correction

Earlier research progressively treated documentation as a collection of contract and CI consistency problems. That research uncovered real mechanisms but risked building a project whose primary product was a reviewer checklist. We instead use the evidence to answer *developer* questions: should I write this, where should it go, what makes it useful, and how can it evolve naturally with software?

This direction is recorded in [Decision 0001](../../docs/decisions/0001-guide-first.md).

## Conversion from evidence to advice

| Verified source / example | Observed mechanism | Guide advice (our interpretation, not source's universal claim) | Avoid over-transfer |
|---|---|---|---|
| [Django writing guide](https://github.com/django/django/blob/f4c65fd6a517dd32bd2e732ae3543e550e56f206/docs/internals/contributing/writing-documentation.txt) | Tutorials, how-to, topic guides, references serve distinct jobs | [Choose format from reader task](../../guide/02-where.md), [write for use](../../guide/03-how.md) | Do not require four directories in a tiny repo |
| [Rust rustdoc guide](https://github.com/rust-lang/rust/blob/92b5b8c87c61b20adc9001b41baf587634a74734/src/doc/rustdoc/src/how-to-write-documentation.md) | Front-page role, examples, APIs and edge cases | [Start with a meaningful example](../../guide/03-how.md), [first success recipe](../../guide/recipes/first-success.md) | Don't apply full public-crate expectations to private helpers |
| [Chromium base/task README](https://github.com/chromium/chromium/blob/cebb23461ac11d291f8eac596e6b73283c167b4d/base/task/README.md) | Compact directory map, linked concept docs and local interface headers | [Place knowledge where it helps](../../guide/02-where.md), [module README example](../../guide/recipes/module-readme.md) | Never mandate a README for every folder |
| [Codex argument-comment-lint](https://github.com/openai/codex/blob/67f0994b532b8740f14b5b738af7b7b2a915b1d6/tools/argument-comment-lint/README.md) | Prefer self-documenting APIs, check hints when used | [Prefer good code over redundant comments](../../guide/03-how.md), [source comment recipe](../../guide/recipes/source-comment.md) | A specialized Dylint is not an all-language default |
| [Codex auth wording PR](https://github.com/openai/codex/pull/49361) | User-facing information improved in UI copy and snapshots | [Documentation can evolve without Markdown](../../guide/04-evolve.md) | This doesn't mean all changes avoid narrative docs |
| [Codex schema fixtures](https://github.com/openai/codex/blob/67f0994b532b8740f14b5b738af7b7b2a915b1d6/codex-rs/app-server-protocol/src/schema_fixtures_tests.rs) | Regenerate and compare machine representations | [Generate details instead of duplicating by hand](../../guide/04-evolve.md) | Generation doesn't explain why/how to a human |
| [AstrBot LLM tool parser](https://github.com/AstrBotDevs/AstrBot/blob/734b357fe30963365494df0c0603844e708730f3/astrbot/core/star/register/star_handler.py#L650-L700) | Runtime consumes docstrings to construct tool schema | [Recognize executable contracts](../../guide/02-where.md), [source comment recipe](../../guide/recipes/source-comment.md) | Normal docstrings aren't automatically executable |
| [Google OpenDocs approaches](https://github.com/google/opendocs/blob/fbc574e261f0cd363a915776e217abced6e7c952/docs_advisor/part_1.md) | Different resourcing conditions support iteration or focused overhauls | [Start where friction is highest](../../guide/01-when.md), [adopt incrementally](../../guide/05-adoption.md) | This is a methodology proposal, not observed performance data |
| [The Good Docs Project](https://github.com/thegooddocsproject/templates/blob/de840b374c57502bf1e99c3ccfe05a858553f99f/README.md) | Concept/task/reference categories and optional templates | [Choose by reader goal](../../guide/03-how.md), [optional recipes](../../guide/recipes/README.md) | A template catalog is not a project completion standard |

## Editorial quality bar for Guide chapters

Every substantive recommendation should make a useful choice clearer. Favor:
- a named situation and intended reader;
- practical alternatives, including no-documentation work;
- a compact worked or source-backed example;
- a **why**, a **when not**, and a trade-off;
- a link to primary evidence for claims about a real project's practice;
- a clear separation of verified observation from JIT-DW's own interpretation.

A page that only asks the developer to prove compliance belongs in optional validation or research, not the core Guide.

## Why this is not yet a usability result

We used purposively selected projects already in the research set, not a randomized sample; source artifacts and merged PRs do not prove reader comprehension. The Guide has not yet been exercised by independent developers on representative tasks. The next evaluation should ask whether a developer can choose, write and maintain appropriate explanations faster or more clearly **without** installing the optional classifier.

## Next recommended experiment

Try the Guide on two contrasting real tasks, with one person who did not author it:
- an ordinary internal refactor where the right answer may be no new document;
- a public API or onboarding failure where some reader-facing explanation clearly helps.

Observe task completion, needless new artifacts, changes in understanding, time, and whether the author retains autonomy. Use the optional CLI only as a separate comparison group, not as the default definition of JIT-DW success.
