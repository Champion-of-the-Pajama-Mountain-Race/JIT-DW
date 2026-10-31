# Case study: Django documentation and feature workflow

**Status:** Evidence-complete for documentation taxonomy, the inspected Field reference/source pair, and three merged PR examples.  
**Repository:** https://github.com/django/django  
**Revision:** f4c65fd6a517dd32bd2e732ae3543e550e56f206  
**History samples:** PR #21855, PR #21357, and PR #22111  
**Scope:** documentation contributor guide, model field reference, Field source class, feature PRs, and documentation tooling.

## 1. Question

How does Django separate user-facing reference documentation from source comments, and how does it coordinate documentation with feature changes and documentation tooling?

## 2. Repository context

Django maintains a large hand-authored reStructuredText documentation tree built with Sphinx. Its documentation guide defines several reader-oriented document types and explicit rules for documenting new features.

## 3. Evidence inventory

| Evidence | Type | Source | What it establishes |
|---|---|---|---|
| E1 | P | [Writing documentation](https://github.com/django/django/blob/f4c65fd6a517dd32bd2e732ae3543e550e56f206/docs/internals/contributing/writing-documentation.txt#L10-L90) | Documentation is maintained as reStructuredText, built with Sphinx, and organized into tutorials, topic guides, reference guides, and how-to guides. |
| E2 | P | [New feature documentation policy](https://github.com/django/django/blob/f4c65fd6a517dd32bd2e732ae3543e550e56f206/docs/internals/contributing/writing-documentation.txt#L731-L755) | New and changed features use versionadded/versionchanged directives and release notes. |
| E3 | D | [Model field reference](https://github.com/django/django/blob/f4c65fd6a517dd32bd2e732ae3543e550e56f206/docs/ref/models/fields.txt#L35-L60) | User-facing reference explains nuanced differences between null and blank, including backend-specific behavior. |
| E4 | C | [Field source class](https://github.com/django/django/blob/f4c65fd6a517dd32bd2e732ae3543e550e56f206/django/db/models/fields/__init__.py#L129-L140) | The inspected base Field class has a brief class docstring rather than reproducing the full user-facing reference. |
| E5 | H | [Merged feature PR #21855](https://github.com/django/django/pull/21855) | A behavior/API change updated implementation, many reference pages, release notes, and tests in one PR. |
| E6 | H | [Merged feature PR #21357](https://github.com/django/django/pull/21357) | A template-tag feature updated implementation, reference documentation, release notes, and tests in one PR. |
| E7 | H/A | [Merged documentation tooling PR #22111](https://github.com/django/django/pull/22111) | Documentation lint/format checks were changed to use Sphinx's source discovery rather than duplicated file-exclusion logic. |

## 4. What the project actually does

Django's writing guide distinguishes:

- Tutorials, which help readers achieve something through steps.
- Topic guides, which explain a concept at a higher level.
- Reference guides, which describe APIs and how to use them.
- How-to guides, which are result-oriented recipes.

The guide says documentation is edited as plain-text reStructuredText and built with Sphinx. New features and significant changes should be marked with versionadded or versionchanged and included in the appropriate release notes.

The model field reference explains the distinction between null and blank in detail, including the fact that null affects database storage while blank affects validation, plus an Oracle-specific note. The inspected Field base class in source has a short class docstring and does not reproduce that full user-facing explanation.

PR #21855 is a broad change to Django's request/response API. Its changed files include implementation, multiple reference pages, release notes, and tests. PR #21357 is a narrower template-tag feature whose same-PR changes include implementation, the built-in template-tag reference, release notes, and tests.

PR #22111 is a particularly useful maintenance example. It changed documentation tooling so lint and formatting checks use Sphinx's own source discovery. The PR description explains that the checks had duplicated and drifted file-exclusion rules; the fix made docs/conf.py the single source of truth for which files count as documentation sources.

## 5. Why these practices may exist

**Stated rationale:** Django emphasizes consistency and readability. Its documentation guide describes the different purposes of tutorials, topic guides, references, and how-to guides. Its feature policy makes release applicability visible to readers.

**Inferred rationale:** The separation between a short source docstring and a detailed reference page allows the source to remain focused on implementation identity while the manual explains user-visible semantics, examples, and caveats.

**Stated rationale from PR #22111:** Duplicated source-file discovery rules had drifted. Reusing Sphinx's own discovery mechanism removed the need to keep several independent exclusion lists synchronized.

## 6. Comparison with JIT-DW hypotheses

| Hypothesis | Alignment | Evidence and qualification |
|---|---|---|
| Documentation types should reflect reader tasks | supports | Django explicitly distinguishes tutorials, topic guides, references, and how-to guides. |
| Feature changes should update relevant docs and tests together | supports | Merged PRs #21855 and #21357 changed code, docs, release notes, and tests. |
| Every API fact belongs in a source docstring | contradicts | The Field reference is much richer than the inspected source class docstring. |
| Documentation tooling can suffer the same duplication/drift as product docs | supports | PR #22111 fixed duplicated source-file discovery rules. |
| One authoritative source is useful when the same selection logic is repeated | supports | Sphinx's own source discovery became the shared authority for docs checks. |
| A documentation build proves semantic correctness | not established | The inspected evidence establishes build and lint tooling, not full semantic validation. |

## 7. Trade-offs and limitations

- Separate reference pages can provide richer reader guidance but require explicit change coordination.
- Release-note directives and version markers add maintenance work, but make release applicability visible.
- Tooling itself needs documentation and maintenance; duplicated helper logic can drift even when the docs content is sound.
- The PR samples demonstrate examples of coordinated updates, not a guarantee that every Django feature PR is complete.

## 8. Findings

- **Observed practice:** Django uses distinct reader-oriented document types, separate hand-authored reference pages, and feature PRs that can include code, docs, release notes, and tests.
- **Stated rationale:** Consistency, readability, and clear release applicability.
- **Inferred rationale:** Separating user reference from source docstrings keeps each surface useful for its reader.
- **Confidence:** High for the inspected policies, files, and merged PRs.
- **What JIT-DW should adopt:** Document type distinctions, feature documentation as part of change completion, and a single source for documentation build discovery.
- **What JIT-DW should not copy:** A rule that every API reference must be duplicated into source docstrings.
- **What needs pilot validation:** Which feature changes need reference updates, release notes, or only source-level documentation.
