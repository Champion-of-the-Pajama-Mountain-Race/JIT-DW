# Recipe: a lightweight note when changed behavior affects readers

**Use when:** the relationship between the code change and reader-facing knowledge is not obvious to a teammate. A short PR explanation can point to the right place.

**Don't use when:** everybody already understands the change and the relevant documentation is beside the code. Don't force contributors to fill in a document explaining why no document was written.

## Example 1 — no new user documentation needed

> The parser now uses a faster internal lookup. The public input format, error behavior, and output remain unchanged; existing tests exercise those contracts. No user-facing explanation was made inaccurate.

This is a *sample rationale*; it is not evidence that a particular real optimization is correct. The developer should make the call based on the actual diff.

## Example 2 — one updated explanation is enough

> The CLI now supports OS keyring storage. I removed the UI text that said credentials always live in a particular file and updated the snapshot. The existing setup instructions don't make that claim.

[Codex PR #49361](https://github.com/openai/codex/pull/49361) is a real case of changing UI/CLI credential wording and snapshot tests rather than adding a new Markdown page.

## Example 3 — multiple kinds of explanation change

> The new request method is available to applications. Its method semantics changed in middleware and in the test client. I updated the reference and release notes; caching behavior remains explicitly unsupported.

[Django PR #21855](https://github.com/django/django/pull/21855) is a real multi-surface example, including documented limits.

## The point

The note is a conversation starter that explains changed *meaning*. It is not a compliance certificate. In a small team it may never need to be written at all.

If your project has repeated, high-risk drift, the [optional impact-review protocol](../../docs/workflow/impact-review-protocol.md) offers more structure. Don't start there by default.

[Back to recipes](README.md).
