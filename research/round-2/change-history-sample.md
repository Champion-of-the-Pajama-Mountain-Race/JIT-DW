# Round 2 change-history sample

**Status:** Curated evidence cases, not a random sample or a compliance audit.  
**Collected:** 2026-10-31.

## Case table

| ID | Project and change | Changed-file evidence | Provisional impact reading | What is still unknown |
|---|---|---|---|---|
| H01 | [Linux kref documentation integration](https://github.com/torvalds/linux/commit/b76d32422c09bc9310f61a5a89671975db34bd2a) | `include/linux/kref.h` and `Documentation/core-api/kref.rst` changed together | Documentation can be authored next to code yet remain undiscoverable until included in the rendered manual. The commit adds the Sphinx kernel-doc directive as well as comment fixes. | Project-wide publication completeness and actual external reader success. |
| H02 | [Chromium ThreadPool rename](https://github.com/chromium/chromium/commit/43fd37033b05a48a6f2f3f87fdb844844d84e650) | Large refactor included `base/task/README.md`, whose terminology changed to `ThreadPoolInstance` | One concrete same-CL example consistent with Chromium's stated policy to update docs with code | How consistently all other Chromium CLs follow that policy. |
| H03 | [CPython heapq implementation optimization](https://github.com/python/cpython/commit/c7d7105b8d230741a5fa04924701d5245d07dace) | Only `Lib/heapq.py`; four tuple-unpacking accesses became indexing into `result[0][0]` | Plausible "no user-facing documentation update required" for an internal optimization, if behavior is preserved. An automatic rule requiring a docs file here would likely create noise. | Tests and microbenchmarks were not executed by this study; equivalent behavior remains an inference. |
| H04 | [CPython heapq module docstring correction](https://github.com/python/cpython/commit/659cb7e6b8e83e1541fc27fd29d4846e940b600e) | Only `Lib/heapq.py`; corrections inside its module docstring | A documentation-only change can legitimately live inside a source file without a separate Markdown edit | Whether that wording was duplicated elsewhere and needed synchronization. |
| H05 | [CPython heapq library reference adjustment](https://github.com/python/cpython/commit/9bf5100037f661f3a369d3ee539bec06f063b650) | `Doc/library/heapq.rst` and another reference page | Independent maintenance of the user reference, distinct from the module docstring | This commit is not paired with H04; the two edits alone do not prove drift. |
| H06 | [Kubernetes perContainer description](https://github.com/kubernetes/kubernetes/commit/cef7481431757c32ddeb07fad52551e27493bb79) | Six API type files across internal/core/resource and versioned staging APIs | One semantic clarification had to be added to multiple related comment representations in the same commit | Whether any generator or checker could have enforced this exact synchronization. |
| H07 | [Rust API doc improvement](https://github.com/rust-lang/rust/pull/126428) | Two source files, `library/std/src/fs.rs` and `library/std/src/path.rs`; doc sections and examples improved | API docs can be maintained directly in language-level documentation comments. | No end-to-end doctest run was performed here. |
| H08 | [Django template-tag feature](https://github.com/django/django/pull/21357) | `django/template/defaulttags.py`, a reference page, `docs/releases/6.2.txt`, and a test file | A compact example of feature, docs, release notes, and tests in the same merged PR | The PR does not establish a general update rate for Django. |
| H09 | [Django HTTP QUERY feature](https://github.com/django/django/pull/21855) | 27 changed files: implementation, many user/reference docs, release notes, tests | Strong multi-surface example. The release notes explicitly document deferred cache behavior and changed safe-method handling; review added scrutiny about edge cases. | No execution of its test suite was performed by JIT-DW. |
| H10 | [Django docs-check consolidation](https://github.com/django/django/pull/22111) | Docs lint/format tooling, Sphinx configuration, tox, Windows workflow, docs contributor instructions | CI itself can drift from docs-build input lists. The fix reuses Sphinx source discovery instead of hand-maintaining separate exclusion lists. | No independent local CI execution by JIT-DW. |
| H11 | [Chromium PageStabilityMonitor componentization](https://github.com/chromium/chromium/commit/924b5bcf53a392fa97f0d517c0d8df67d2cffb1f) | About 28 source/build/test files, no standalone README in the changed-file set | **Unknown / inspect**, not automatically a doc failure: the new `page_stability_monitor.h` explains purpose, lifetime, single-use constraint, and callback behavior in code comments. | We found no README at two inspected component paths, but did not audit every doc entrance, Gerrit discussion, or downstream user task. |

## Selection and interpretation

The sample was intentionally selected to cover distinct behaviors. It is **not** suitable for estimating what percentage of commits need documentation updates.

A file-count rule would make opposing mistakes:
- H03 could trigger an unnecessary user-documentation requirement despite appearing to be a local implementation optimization.
- H06 might be dismissed as "comments only" even though it changes six representations of a public API semantic.
- H11 could be flagged for lacking a new README, even though important class-level contracts are written next to the new code.
- H01 would look documented if one checked only the header; the actual failure was absence from published HTML navigation.

An improved classifier must map *changed facts → consumers/representations → validation paths*, with an explicit **unknown** outcome for unverified semantic implications.

## Reproducibility

Every row links directly to a commit or merged PR. For H09 and H10, inspect the documented file-level patches and review conversation in the accompanying case studies. For H11, inspect the pinned [header comment](https://github.com/chromium/chromium/blob/cebb23461ac11d291f8eac596e6b73283c167b4d/components/page_content_annotations/content/renderer/page_stability_monitor.h#L25-L57).

## What is *not* counted

- No population-level precision or recall.
- No test-pass statistics.
- No claim that a project with a configured owner always has active maintenance.
- No claim that a docs-free commit is necessarily a documentation defect.
- No full Gerrit review compliance rate.
