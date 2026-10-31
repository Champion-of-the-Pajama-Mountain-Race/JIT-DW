# Case study: Linux kernel documentation

**Status:** Evidence-complete for kernel-doc, kref documentation, and one concrete documentation-maintenance commit.  
**Repository:** https://github.com/torvalds/linux  
**Revision:** a9547379cb381e2a036e3261a6becc17973ac470  
**History sample:** b76d32422c09bc9310f61a5a89671975db34bd2a  
**Scope:** kernel-doc rules, the kref API header, the kref conceptual guide, and the change that connected them.

## 1. Question

How does Linux divide API contracts between source comments and separate conceptual documentation, and how does it keep source comments connected to generated reference pages?

## 2. Repository context

The kernel has a long-lived C codebase, public headers, in-tree documentation, and Sphinx-based documentation generation. The inspected example is the kref reference-counting API.

## 3. Evidence inventory

| Evidence | Type | Source | What it establishes |
|---|---|---|---|
| E1 | P | [Writing kernel-doc comments](https://github.com/torvalds/linux/blob/a9547379cb381e2a036e3261a6becc17973ac470/Documentation/doc-guide/kernel-doc.rst#L9-L58) | Structured comments describe functions, types, and design; they are extracted into Sphinx C-domain reference documentation; placement near declarations is intentional. |
| E2 | C/I | [include/linux/kref.h](https://github.com/torvalds/linux/blob/a9547379cb381e2a036e3261a6becc17973ac470/include/linux/kref.h#L49-L63) | kref_put's comment documents arguments, callback restrictions, behavior, and return-value caveats. |
| E3 | D | [kref guide](https://github.com/torvalds/linux/blob/a9547379cb381e2a036e3261a6becc17973ac470/Documentation/core-api/kref.rst#L14-L65) | A separate guide explains the reference-counting concept, initialization, and usage rules. |
| E4 | D/A | [kernel-doc inclusion in kref.rst](https://github.com/torvalds/linux/blob/a9547379cb381e2a036e3261a6becc17973ac470/Documentation/core-api/kref.rst#L324-L329) | The conceptual guide explicitly includes the source header's kernel-doc comments in the rendered reference. |
| E5 | H | [kref: Improve documentation](https://github.com/torvalds/linux/commit/b76d32422c09bc9310f61a5a89671975db34bd2a) | One commit changed both the header comments and kref.rst; its message says the kernel-doc comments existed but were not linked into the HTML documentation. |

## 4. What the project actually does

The kernel-doc guide states that structured comments in source files describe functions, types, and design. The comments are extracted and converted into Sphinx C-domain function/type descriptions with anchors.

The guide distinguishes required and recommended coverage:

- exported functions used by loadable modules should have kernel-doc comments;
- functions and data structures in headers intended for modules should have kernel-doc comments;
- externally visible non-static functions are good candidates;
- private static routines are recommended for consistency, but this is lower priority and left to the file maintainer.

The placement rule is explicit: function and type comments should be immediately before the declaration or definition. The stated reason is to increase the chance that someone changing the code also changes its documentation.

The guide also documents validation boundaries. The kernel-doc tool can check comment formatting. A build with extra warnings checks documentation in C files, but does not check header files; headers need a separate kernel-doc invocation.

The kref header demonstrates what belongs in an API contract comment. The kref_put comment names the parameters, explains when the release callback runs, prohibits passing NULL or kfree as the callback, and explains the return value and a concurrency caveat.

The separate kref guide explains the concept and rules of use, including initialization and when references must be incremented or released.

### A real maintenance change

The 2024 commit titled “kref: Improve documentation” is unusually revealing. Its commit message says that kernel-doc comments already existed for many functions in kref.h, but those comments were not linked into the HTML documentation anywhere. The commit therefore:

- added a kernel-doc directive to kref.rst to include the header's documentation;
- improved the source comments, including standardizing the Return section;
- added comments for previously undocumented functions;
- changed the conceptual guide and the source header in the same commit.

This is stronger evidence than the policy alone. It shows that colocating comments with code does not automatically make them discoverable in the published documentation. The source-to-reference connection must also be maintained.

## 5. Why these practices may exist

**Stated rationale:** Embedding structured comments in source makes documentation easier to keep up to date. Placing comments directly before declarations increases the chance that code changes and documentation changes happen together. The kref commit adds a second explicit rationale: source comments are not useful as published reference until the documentation tree includes them.

**Inferred rationale:** The split between source comments and conceptual documentation reduces the need to repeat every API detail in a separate manual while still giving users a coherent explanation of the broader programming model.

**Unknown:** The inspected sample does not establish the rate at which comments and generated pages drift across the whole kernel or how consistently maintainers update every eligible function.

## 6. Comparison with JIT-DW hypotheses

| Hypothesis | Alignment | Evidence and qualification |
|---|---|---|
| High-value API contracts should live close to declarations | supports | kernel-doc placement rules and kref_put example. |
| Source comments can be an input to generated documentation | supports | kernel-doc extraction to Sphinx C-domain descriptions. |
| Source comments alone guarantee published discoverability | contradicts | The kref commit explicitly fixed comments that existed but were not linked into HTML docs. |
| Every source file needs a separate responsibility document | not observed | The inspected system documents selected functions/types and broader concepts, not one Markdown file per source file. |
| Every private function needs the same documentation effort | contradicts | Static/private documentation is lower priority and left to maintainer discretion. |
| A successful general build validates every comment | contradicts | Header comments require separate checking. |
| Conceptual explanations and API contracts are interchangeable | contradicts | kref has both source-level API comments and a separate conceptual guide. |

## 7. Trade-offs and limitations

- Structured comments require a format and tooling that contributors must learn.
- Generated reference pages reduce manual duplication but cannot replace conceptual explanations.
- Source comments can exist without being included in the published documentation tree.
- Validation is not uniform across file types; header files have a separate check path.
- The inspected kref example is illustrative, not a measurement of all kernel subsystems.

## 8. Findings

- **Observed practice:** Linux uses structured source comments for selected API contracts, generates reference documentation from them, and explicitly wires those generated descriptions into conceptual documentation.
- **Stated rationale:** Locality increases the chance that documentation is updated with the code; the kref change also demonstrates that published discoverability needs a separate integration step.
- **Inferred rationale:** Generated reference pages help serve readers without maintaining a second copy of every API signature.
- **Confidence:** High for the documented mechanism and the concrete kref maintenance commit; medium for generalizing to all kernel subsystems.
- **What JIT-DW should adopt:** Put stable API contracts near declarations when the language/toolchain supports it; define which symbols require documentation; verify both comment quality and publication/navigation integration.
- **What JIT-DW should not copy:** A blanket requirement to document every private implementation detail.
- **What needs pilot validation:** Whether a lighter version of structured source comments can work in ordinary multi-language repositories.
