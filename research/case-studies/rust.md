# Case study: Rust and rustdoc

**Status:** Evidence-complete for public API docs, doctests, and the inspected standard-library example.  
**Repository:** https://github.com/rust-lang/rust  
**Revision:** 92b5b8c87c61b20adc9001b41baf587634a74734  
**Scope:** rustdoc writing guidance, documentation tests, missing-doc lint, core crate configuration, and Option documentation.

## 1. Question

How does Rust make source documentation discoverable and how much of its correctness can be checked automatically?

## 2. Repository context

Rust's documentation system is closely integrated with the language toolchain. The inspected files include rustdoc's own writing guidance and the standard library's Option type.

## 3. Evidence inventory

| Evidence | Type | Source | What it establishes |
|---|---|---|---|
| E1 | P | [How to write documentation](https://github.com/rust-lang/rust/blob/92b5b8c87c61b20adc9001b41baf587634a74734/src/doc/rustdoc/src/how-to-write-documentation.md#L15-L60) | Public items should be documented; crate-level docs introduce the library and show realistic usage. |
| E2 | P/A | [Documentation tests](https://github.com/rust-lang/rust/blob/92b5b8c87c61b20adc9001b41baf587634a74734/src/doc/rustdoc/src/write-documentation/documentation-tests.md#L1-L60) | rustdoc extracts code examples and compiles/runs them as tests. |
| E3 | P | [What to include](https://github.com/rust-lang/rust/blob/92b5b8c87c61b20adc9001b41baf587634a74734/src/doc/rustdoc/src/write-documentation/what-to-include.md#L11-L45) | missing_docs warnings or errors can be used to prevent public API documentation gaps. |
| E4 | A | [core crate attributes](https://github.com/rust-lang/rust/blob/92b5b8c87c61b20adc9001b41baf587634a74734/library/core/src/lib.rs#L74-L80) | The actual core crate enables warn(missing_docs). |
| E5 | C | [Option source docs](https://github.com/rust-lang/rust/blob/92b5b8c87c61b20adc9001b41baf587634a74734/library/core/src/option.rs#L598-L630) | Enum variants carry source-level descriptions. |
| E6 | C | [Option method docs](https://github.com/rust-lang/rust/blob/92b5b8c87c61b20adc9001b41baf587634a74734/library/core/src/option.rs#L924-L945) | Method docs describe behavior, panic conditions, and executable examples. |
| E7 | H | [PR #126428](https://github.com/rust-lang/rust/pull/126428) | A merged change reorganized source-level API documentation for platform-specific behavior and errors. |

## 4. What the project actually does

Rust uses source documentation comments as the input to rustdoc. The writing guide recommends crate-level front-page documentation, practical examples, and documentation for public items. It distinguishes crate/module-level documentation from item documentation.

The documentation-tests guide explains that rustdoc extracts fenced examples, preprocesses them, compiles them, and runs them. A doctest fails if the code does not compile or if its assertions fail. This makes examples executable maintenance artifacts rather than decorative snippets.

The rustdoc guide also recommends the missing_docs lint. The inspected core crate actually enables warn(missing_docs), so the policy is not merely theoretical in this example.

The Option type and methods show the resulting style: source comments describe behavior and panic conditions and include code examples. PR #126428 demonstrates a real documentation-only refinement in a source file: platform-specific behavior and errors were separated into explicit sections, and examples were reorganized.

## 5. Why these practices may exist

**Stated rationale:** Rust's documentation tests ensure examples remain up to date and working. The writing guide emphasizes that public items need documentation and that realistic, copyable examples help users get started.

**Inferred rationale:** Putting API documentation in source makes it natural to review alongside interface changes, while doctests make at least the example code mechanically verifiable.

**Unknown:** Doctests cannot prove that prose is complete, that the example covers every important edge case, or that the API's design rationale remains correct.

## 6. Comparison with JIT-DW hypotheses

| Hypothesis | Alignment | Evidence and qualification |
|---|---|---|
| Public APIs should have discoverable contracts | supports | Rust recommends documenting public items and enables missing_docs warnings in core. |
| Examples can be executable tests | supports | rustdoc compiles and runs documentation examples. |
| Source comments can be the authoring source for generated API pages | supports | Rust's rustdoc system is built around source documentation comments. |
| CI can prove documentation is correct | partially supports | It can prove examples compile and run, not that prose is semantically complete. |
| All documentation should be source comments | not observed | Rust also maintains rustdoc guides and other narrative documentation. |

## 7. Trade-offs and limitations

- Doctests provide strong protection against stale examples but require examples to be written in testable form.
- Some examples need hidden setup code or special annotations, which adds authoring complexity.
- Missing-doc lints can prevent gaps but may encourage low-value boilerplate if applied without judgment.
- A successful doctest validates the example's execution, not the surrounding explanation.

## 8. Findings

- **Observed practice:** Rust integrates public API docs and executable examples into source comments and the rustdoc toolchain.
- **Stated rationale:** Examples should remain working and public items should be documented.
- **Inferred rationale:** Tooling reduces the time between API changes and documentation validation.
- **Confidence:** High for the inspected core crate and rustdoc mechanism.
- **What JIT-DW should adopt:** Executable examples where the language supports them, plus a missing-doc policy for selected public surfaces.
- **What JIT-DW should not copy:** Treating all prose as mechanically testable or requiring every project to use a language-specific doc compiler.
- **What needs pilot validation:** Whether a small project's examples can be tested without excessive setup.
