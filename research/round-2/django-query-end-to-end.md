# End-to-end trace: Django HTTP QUERY support

**Status:** Source-based trace complete for selected code, docs, tests, release notes, and review comments; no local test execution.  
**Change:** [Django PR #21855](https://github.com/django/django/pull/21855), merged 2026-10-26.  
**Title:** Fixed #37232 -- Added support for the HTTP QUERY method.  
**Observed changed files:** 27.

## 1. Why this is a useful specimen

The feature spans several distinct public contracts: safe request methods, CSRF exemptions, HTTP conditional handling, class-based view dispatch, test-client APIs, body parsing, and cache behavior. The PR is large enough to expose dependencies but still bounded to one user-visible change.

The PR's stated rationale is implementing HTTP QUERY as a safe, idempotent method with request content in the body. It explicitly says cache integration is deferred because a correct cache key must include request content, not merely the URL. That limitation is documented in the 6.2 release notes.

## 2. Fact-to-representation trace

| Changed fact or decision | Implementation | User-facing representation | Tests or review evidence |
|---|---|---|---|
| `QUERY` is accepted by `require_safe()` | `django/views/decorators/http.py` changes allowed methods to GET/HEAD/QUERY | `docs/topics/http/decorators.txt` and `docs/releases/6.2.txt` add version 6.2 notes and behavior change | `tests/decorators/test_http.py` checks accepted and rejected methods, including async |
| `QUERY` is CSRF-safe | `django/middleware/csrf.py` adds QUERY to safe-method checks | `docs/ref/csrf.txt` and release notes explain exemption | `tests/csrf_tests/tests.py` adds a positive QUERY case |
| Conditional request processing recognizes QUERY | `django/utils/cache.py`, `django/middleware/http.py` and HTTP decorator paths | Conditional middleware and request docs plus release notes | Middleware and conditional processing test paths changed |
| `View` can dispatch QUERY | `django/views/generic/base.py` includes query in method names; `RedirectView` handles query via its method | `docs/ref/class-based-views/base.txt` and release notes mark the new method | `tests/generic_views/test_base.py` checks query() handling, 405, and redirects |
| Test clients and factories can issue QUERY | `django/test/client.py` adds query methods for synchronous/asynchronous paths | `docs/topics/testing/tools.txt`, advanced testing docs and release notes describe `Client.query` and its parameters | `tests/test_client/tests.py` adds body, content type, JSON, redirect and method coverage |
| QUERY content lives in `HttpRequest.body`, not automatically `POST` | Request processing and test-client implementation | `docs/ref/request-response.txt` and release notes explain body access and parsing | Test client and view tests cover request body behavior |
| Caching support is intentionally incomplete | Existing cache middleware remains outside the feature's full cache-key implementation | `docs/releases/6.2.txt` explicitly says QUERY responses are not cached by the named middleware/decorator | PR discussion requests separate treatment; caching scope was deliberately deferred |

All paths above are from the PR's changed-file list and selected per-file patches, not guesses based on filenames. See [PR files](https://github.com/django/django/pull/21855/files) for the complete diff.

## 3. From implementation to release notes

The `docs/releases/6.2.txt` patch performs three separate jobs:

1. Introduces the new method and a class-based-view usage example.
2. Warns that QUERY content must be parsed from `HttpRequest.body` and is not automatically converted to `HttpRequest.POST`.
3. Clearly distinguishes supported conditional request handling from caching that is *not* yet supported.

This is not redundant documentation. It makes a compatibility and operational boundary visible to adopters of the new feature.

The corresponding `docs/ref/csrf.txt`, `docs/topics/http/decorators.txt`, and `docs/ref/class-based-views/base.txt` patches include `versionchanged:: 6.2` notes. The test-client docs include `versionadded:: 6.2`.

**JIT-DW lesson:** Release notes and reference pages answer different questions. A reference explains current behavior; release notes explain the change and its migration significance.

## 4. Review discussion changed the scope of checking

Concrete review observations:

- [A reviewer asked for tests around admin behavior](https://github.com/django/django/pull/21855#discussion_r3886970606).
- [A reviewer identified RedirectView dispatch as a potential gap](https://github.com/django/django/pull/21855#discussion_r3887075216); the merged diff includes a `test_redirect_QUERY`.
- [A reviewer asked for QUERY cases in method tests](https://github.com/django/django/pull/21855#discussion_r3911676051); the final tests include them.
- [A reviewer asked whether conditional middleware's GET tests should cover QUERY](https://github.com/django/django/pull/21855#discussion_r3911767581).
- [Review discussion agreed to keep QUERY caching separate](https://github.com/django/django/pull/21855#issuecomment-5592467312), matching the release-note limitation.

These examples show why a list of changed paths is only an input to review. Semantic questions still need to be asked.

## 5. A non-obvious evidence warning: PR body versus final patch

The PR description says the `follow=True` redirect issue for 307/308 was not addressed, claiming a QUERY redirect would be replayed as GET. However, the merged tests in `tests/test_client/tests.py` explicitly include QUERY in the 307/308 method-preservation matrix and add `test_follow_307_and_308_preserves_query_body`.

This means the PR description and merged test coverage do not tell the same story for that specific built-in test-client case. We should not infer a remaining bug solely from the PR prose; nor should we claim full runtime correctness without executing the tests.

**JIT-DW lesson:** PR descriptions are historical explanations that may become stale as patches evolve. For final behavior, inspect the final code and tests; for rationale, read the conversation and distinguish any superseded claims.

## 6. Research-only impact verdict

Using the provisional protocol:
- **Direct impacts:** HTTP method acceptance, CSRF, conditional handling, class-based views, test-client APIs.
- **Indirect representations:** guides, API reference, versioned release notes, examples.
- **Verified in source:** corresponding files and tests exist in the merged PR.
- **Unverified by this study:** actual test execution; full implementation compliance with HTTP QUERY semantics on every platform.
- **Deferred but documented:** full caching support.
- **Unknown:** any user-facing documentation outside the inspected changed-file set.

This is a strong positive example of *documentation-aware change review*, not evidence that every Django PR reaches the same quality.

## 7. Reproduction

1. Open [PR #21855](https://github.com/django/django/pull/21855).
2. Inspect the changed-file list of 27 paths.
3. Compare hunks for `django/views/decorators/http.py`, `django/middleware/csrf.py`, `django/test/client.py`, and `django/views/generic/base.py`.
4. Inspect documentation hunks under `docs/ref/`, `docs/topics/`, and `docs/releases/6.2.txt`.
5. Inspect matching tests under `tests/decorators/`, `tests/csrf_tests/`, `tests/generic_views/`, and `tests/test_client/`.
6. Compare the body of the PR with final redirect-related tests; read review links above.

Do not replace these steps with a generic summary of the PR description.
