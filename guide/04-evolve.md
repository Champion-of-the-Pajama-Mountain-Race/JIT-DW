# 4. Let documentation evolve with code

Documentation maintenance works best as part of ordinary development, not a second approval pipeline. The goal is to keep information useful while the code changes, with the **smallest change that preserves the reader's understanding**.

## Start with what the code change means

Four informal questions are usually enough:

1. Who uses or maintains the thing that changed?
2. Which assumptions, examples or instructions could now be wrong?
3. Is a relevant explanation already next to the code, in a generated reference, or in a user guide?
4. What is the least costly useful fix — changing a sentence, a code example, an error message, a test, or nothing?

These questions are a conversation aid, not a PR form. A maintainer familiar with a subsystem may answer them mentally in seconds.

## Real changes show different valid outcomes

### An internal optimization may not need a doc edit

[CPython's heapq optimization](https://github.com/python/cpython/commit/c7d7105b8d230741a5fa04924701d5245d07dace) changes an implementation expression without visibly changing the public interface. A user-facing reference update is not automatically necessary. The behavior-preservation judgment still belongs to the developer and tests.

### A user-visible statement might live in application copy

[Codex PR #49361](https://github.com/openai/codex/pull/49361) fixes misleading text implying credentials always live in one file, when multiple storage backends exist. The right explanation was corrected in TUI and CLI output, and snapshot coverage changed. There was no need to invent a new Markdown page for that correction.

### A feature may touch multiple documentation jobs

[Django PR #21855](https://github.com/django/django/pull/21855) introduces HTTP QUERY handling across API behavior, tests, reference docs, task guidance and release notes. Its caching limitation is documented rather than disguised. A reader looking up current behavior and a reader upgrading a version need different information, even when the underlying feature is the same.

### Generated references have a special relationship

[Codex's schema tests](https://github.com/openai/codex/blob/67f0994b532b8740f14b5b738af7b7b2a915b1d6/codex-rs/app-server-protocol/src/schema_fixtures_tests.rs) compare generated outputs to checked-in artifacts. If source contracts change, regenerate as the project already expects rather than hand-editing the output. A generated reference may still need a human-written usage explanation alongside it.

## Three ways to maintain without a bureaucracy

**Improve the information where you notice the problem.** An issue, review or debugging session often reveals a missing example. Fix that small problem as part of the work, provided it does not distract from a risky code change.

**Ask for help from someone who knows the reader.** A reviewer can identify a changed behavior that code diffs alone do not reveal. They need not fill out a documentation governance sheet.

**Keep history and current truth separate.** Preserve old design decisions as rationale, but link to the current implementation. Don't silently rewrite history to match today's architecture.

## What about a missed update?

Prefer repairing the inaccurate explanation and learning why it was missed over automatically adding a stricter gate. A small improvement to naming, linking or ownership might prevent more drift than another checklist.

If a project repeatedly ships stale generated references, a focused mechanical check may be justified. If a project repeatedly confuses users despite green documentation CI, review the writing and reader journeys instead.

## Special cases worth more care

- **Machine-consumed comments:** In AstrBot, some docstrings are parsed to build LLM tool schemas. Changing those docstrings can change runtime behavior. Treat them as a program contract, not prose-only cleanup.
- **Public API breaking changes:** Examples, error semantics, compatibility and migration advice may need attention.
- **Operational/safety procedures:** Have someone validate steps and failure conditions; an obsolete runbook can do real harm.
- **Translated or screenshot-based UI docs:** When navigation changes, consider the existing locales and images that show the old workflow. Do not assume every language must have a page.
- **Versioned manuals:** State which version a procedure describes; release notes and current reference pages have different roles.

For optional formal impact records in very large projects, see [the research protocol](../docs/workflow/impact-review-protocol.md). It is not required to use this Guide.

Continue: [Adopt at your own scale](05-adoption.md).
