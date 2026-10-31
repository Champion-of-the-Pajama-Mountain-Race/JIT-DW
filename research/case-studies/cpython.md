# Case study: CPython documentation surfaces

**Status:** Evidence-complete for the heapq example and two separate documentation-history paths.  
**Repository:** https://github.com/python/cpython  
**Revision:** 4a9b98115fec4d93c32c554aa541d6c3fc4c3b27  
**History samples:** 659cb7e6b8e83e1541fc27fd29d4846e940b600e; 9bf5100037f661f3a369d3ee539bec06f063b650  
**Scope:** Doc build instructions, the heapq module docstring, the heapq library reference, and separate edits to each surface.

## 1. Question

How does CPython divide information between source docstrings and the separately maintained library reference, and what does history reveal about keeping the two surfaces aligned?

## 2. Repository context

CPython maintains the Python language implementation and a large reStructuredText documentation tree. The inspected example is heapq, where both the implementation module and the library reference describe the heap invariant and basic behavior.

## 3. Evidence inventory

| Evidence | Type | Source | What it establishes |
|---|---|---|---|
| E1 | P/A | [Doc/README.rst](https://github.com/python/cpython/blob/4a9b98115fec4d93c32c554aa541d6c3fc4c3b27/Doc/README.rst#L4-L52) | Documentation sources are reStructuredText and are built with Sphinx and related tools. |
| E2 | C | [Lib/heapq.py](https://github.com/python/cpython/blob/4a9b98115fec4d93c32c554aa541d6c3fc4c3b27/Lib/heapq.py#L1-L35) | The source module docstring explains the heap invariant, basic usage, and design differences. |
| E3 | C | [heapq.py function docstrings](https://github.com/python/cpython/blob/4a9b98115fec4d93c32c554aa541d6c3fc4c3b27/Lib/heapq.py#L133-L150) | Individual functions have concise behavior summaries and selected caveats. |
| E4 | D | [Doc/library/heapq.rst](https://github.com/python/cpython/blob/4a9b98115fec4d93c32c554aa541d6c3fc4c3b27/Doc/library/heapq.rst#L1-L60) | The library reference repeats core heap facts, links to source, and expands the explanation and API reference. |
| E5 | H | [Source docstring correction](https://github.com/python/cpython/commit/659cb7e6b8e83e1541fc27fd29d4846e940b600e) | A documentation-focused commit changed only Lib/heapq.py, improving the module docstring. |
| E6 | H | [Library reference update](https://github.com/python/cpython/commit/9bf5100037f661f3a369d3ee539bec06f063b650) | A separate documentation commit changed Doc/library/heapq.rst, including the placement of the heapify API entry. |

## 4. What the project actually does

The source module docstring explains the heap invariant, zero-based indexing, the smallest element at index zero, and basic operations. Individual function docstrings are shorter, for example describing the behavior of heappush and heappop.

The separate library reference also explains the min-heap invariant and indexing, links to the source file, and expands into a user-facing API reference.

This means some facts appear in more than one place. The inspected example does not show a single generated document replacing all source and reference text.

The documentation tree has its own build instructions. Doc/README describes reStructuredText sources and a Sphinx-based build using a virtual environment and Makefile targets.

### What history adds

Two commits illustrate that the source docstring and the library reference are separate maintenance surfaces:

- The 2024 heapq docstring correction changed only Lib/heapq.py.
- A later library-reference change modified Doc/library/heapq.rst, including moving the heapify reference entry into the min-heap API section.

These are not the same change, so they do not prove that the two surfaces drifted or that a synchronized update was missed. They do prove that a maintainer may work on one surface without editing the other.

## 5. Why these practices may exist

**Stated rationale:** The inspected README establishes that the documentation is maintained as a separate reStructuredText source tree and built with Sphinx. It does not explicitly explain why heapq repeats selected information in its module docstring and library reference.

**Inferred rationale:** The module docstring likely supports source-level discovery and interactive help, while the library reference provides a more complete, navigable manual for readers. These are different reading surfaces, so some overlap may be intentional.

**Unknown:** The inspected sample does not establish what process ensures that duplicated facts remain synchronized or how often drift occurs.

## 6. Comparison with JIT-DW hypotheses

| Hypothesis | Alignment | Evidence and qualification |
|---|---|---|
| Source docstrings and external docs can have different purposes | supports | heapq has a module docstring and a separate detailed library reference. |
| Every fact must appear in exactly one file | contradicts | The heap invariant and usage appear in both source and reference documentation. |
| Documentation surfaces can be updated independently | supports | The two history samples touch different files and different changes. |
| Documentation should be buildable and previewable | supports | The Doc tree documents its Sphinx build process. |
| Source comments are sufficient for complete user documentation | contradicts | The separate library reference contains more detailed explanation and API material. |
| Duplicate text is always harmful | not established | Overlap exists, but this sample does not measure its maintenance cost or synchronization quality. |

## 7. Trade-offs and limitations

- Repeating core facts may improve discovery across different reader surfaces.
- Repeated facts can drift unless the project has a synchronization practice or the duplicated text is deliberately limited to stable summaries.
- The existence of two copies is not enough to conclude that one should be deleted.
- The history samples are not a complete audit of all heapq changes or the CPython documentation workflow.

## 8. Findings

- **Observed practice:** CPython uses both source docstrings and separately authored library reference pages, and the two surfaces have independent change histories.
- **Stated rationale:** The docs tree is a separate Sphinx-built documentation source.
- **Inferred rationale:** Multiple reader surfaces justify some controlled overlap.
- **Confidence:** High for the observed structure and separate commits; medium-low for the inferred rationale.
- **What JIT-DW should adopt:** Distinguish canonical authoring sources from reader-facing representations; allow intentional summaries when they serve a distinct reading context.
- **What JIT-DW should not copy:** Treating every duplicated paragraph as acceptable without a maintenance plan.
- **What needs pilot validation:** How to identify and test intentional duplication versus accidental drift.
