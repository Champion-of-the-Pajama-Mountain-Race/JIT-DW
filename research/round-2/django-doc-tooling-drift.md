# Django's documentation checks became inconsistent with their own build

**Status:** Concrete merged PR and code review inspected; tools not run locally by JIT-DW.  
**Change:** [Django PR #22111](https://github.com/django/django/pull/22111), merged 2026-10-30.

## 1. Problem found in the real project

Django's docs are built by Sphinx. The documentation lint and code-block formatting commands previously maintained their own lists of files and directories to include or exclude. The PR description says these exclusion rules had drifted, requiring manual re-synchronization in an earlier PR.

A reviewer of the earlier change observed that duplicated exclusion logic was brittle. PR #22111 responds by reusing Sphinx's own source discovery.

This is unusually relevant to JIT-DW: the scripts designed to keep documentation healthy had become another source of documentation-maintenance drift.

## 2. Actual patch architecture

| File | Before / after | Why it matters |
|---|---|---|
| `docs/_utils.py` | Adds `find_sphinx_sources(srcdir)`; creates a minimal Sphinx app and enumerates `app.project.docnames` through `doc2path` | Source discovery is delegated to the renderer's own configuration rather than copied filters. |
| `docs/lint.py` | Replaces hand-maintained ignore flags and directory arguments with the list from `find_sphinx_sources` | Lint now targets the same source set Sphinx sees. |
| `docs/blacken-sources.py` | New small wrapper passes discovered files to `blacken-docs` | Formatting uses the same source selection as lint and build. |
| `docs/conf.py` | Removes warning that its exclusions must be synchronized manually with Makefile/batch/lint | The original list remains in its natural authority, the Sphinx config. |
| `docs/Makefile`, `docs/make.bat` | Remove duplicated shell/batch path filtering and invoke wrappers | Cross-platform commands share implementation. |
| `tox.ini` | Adds Sphinx dependency to lint/format environments | The new shared discovery function requires Sphinx at run time. |
| `.github/workflows/docs_win.yml` | Adds Windows docs checks scoped to relevant tooling paths | Windows-specific commands can be checked independently. |

## 3. What code review revealed

The review discussion is not ceremonial:

- [Reviewer feedback](https://github.com/django/django/pull/22111#pullrequestreview-5704687317) led to explicit Sphinx dependencies for lint/format environments and adjustment of Windows checks.
- [Another review](https://github.com/django/django/pull/22111#pullrequestreview-5689184910) identified an argument-handling problem in the old lint invocation.
- The PR discussion notes that different operating systems can enforce different dictionary behavior, so the Windows spelling check was removed rather than blindly copied.

We inspected the merged patches, not just the PR summary. The implementation actually constructs a Sphinx app to obtain the document sources.

## 4. Why it matters for JIT-DW

The naive rule "add lint, format, spellcheck, docs build" would have encouraged separate tools and duplicate discovery logic. The actual repair suggests a stronger rule:

> Prefer deriving check inputs from the same source that defines build inputs, and test the integration boundaries of that derivation.

This is a *stated and observed mechanism*. It does not prove that every Django documentation check has zero drift, and we have not independently executed the workflow.

## 5. Design changes proposed

- JIT-DW checks must state which repository configuration is the authoritative selector for documents.
- New docs checks should reuse existing discovery APIs or manifest generation when possible.
- CI installation dependencies and cross-platform shell behavior belong in the acceptance criteria.
- A checker should report the number and types of files it actually visited.
- Avoid assuming "CI green" implies the intended file set was checked.
