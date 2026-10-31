# Case study: Linux kernel documentation

**Status:** Evidence-complete for kernel-doc and kref documentation patterns.  
**Repository:** https://github.com/torvalds/linux  
**Revision:** a9547379cb381e2a036e3261a6becc17973ac470  
**Scope:** kernel-doc rules, the kref API header, and the kref conceptual guide.

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

## 5. Why these practices may exist

**Stated rationale:** Embedding structured comments in source makes documentation easier to keep up to date. Placing comments directly before declarations increases the chance that code changes and documentation changes happen together.

**Inferred rationale:** The split between source comments and conceptual documentation reduces the need to repeat every API detail in a separate manual while still giving users a coherent explanation of the broader programming model.

**Unknown:** The inspected sample does not establish the rate at which comments and generated pages drift across the whole kernel or how consistently maintainers update every eligible function.

## 6. Comparison with JIT-DW hypotheses

| Hypothesis | Alignment | Evidence and qualification |
|---|---|---|
| High-value API contracts should live close to declarations | supports | kernel-doc placement rules and kref_put example. |
| Source comments can be an input to generated documentation | supports | kernel-doc extraction to Sphinx C-domain descriptions. |
| Every source file needs a separate responsibility document | not observed | The inspected system documents selected functions/types and broader concepts, not one Markdown file per source file. |
| Every private function needs the same documentation effort | contradicts | Static/private documentation is lower priority and left to maintainer discretion. |
| A successful general build validates every comment | contradicts | Header comments require separate checking. |
| Conceptual explanations and API contracts are interchangeable | contradicts | kref has both source-level API comments and a separate conceptual guide. |

## 7. Trade-offs and limitations

- Structured comments require a format and tooling that contributors must learn.
- Generated reference pages reduce manual duplication but cannot replace conceptual explanations.
- Validation is not uniform across file types; header files have a separate check path.
- The inspected kref example is illustrative, not a measurement of all kernel subsystems.

## 8. Findings

- **Observed practice:** Linux uses structured source comments for selected API contracts and generates reference documentation from them, while maintaining separate conceptual guides.
- **Stated rationale:** Locality increases the chance that documentation is updated with the code.
- **Inferred rationale:** Generated reference pages help serve readers without maintaining a second copy of every API signature.
- **Confidence:** High for the documented kernel-doc mechanism and the kref example; medium for generalizing to all kernel subsystems.
- **What JIT-DW should adopt:** Put stable API contracts near declarations when the language/toolchain supports it; define which symbols require documentation; validate each source form through the right tool.
- **What JIT-DW should not copy:** A blanket requirement to document every private implementation detail.
- **What needs pilot validation:** Whether a lighter version of structured source comments can work in ordinary multi-language repositories.
