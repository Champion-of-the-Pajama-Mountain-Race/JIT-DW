# Case study: Chromium documentation layers

**Status:** Evidence-complete for documentation policy, the inspected base/task component, and one concrete same-CL update.  
**Repository:** https://github.com/chromium/chromium  
**Revision:** cebb23461ac11d291f8eac596e6b73283c167b4d  
**History sample:** 43fd37033b05a48a6f2f3f87fdb844844d84e650  
**Scope:** documentation best practices, in-code documentation guidelines, docs index, base/task README, SequencedTaskRunner header comments, and one ThreadPool refactor CL.

## 1. Question

Does Chromium's stated distinction between module, interface, and implementation documentation appear in real source directories and code changes?

## 2. Repository context

Chromium is a very large multi-component C++ project. Its documentation guidance explicitly addresses code health, component layout, API contracts, implementation comments, design documents, and the project documentation index. Chromium uses Gerrit CLs for code review; the GitHub repository is a source mirror.

## 3. Evidence inventory

| Evidence | Type | Source | What it establishes |
|---|---|---|---|
| E1 | P | [Documentation guidelines](https://github.com/chromium/chromium/blob/cebb23461ac11d291f8eac596e6b73283c167b4d/docs/documentation_guidelines.md#L12-L35) | Three in-code documentation layers: module/component, interface/class, and implementation. |
| E2 | P | [Documentation best practices](https://github.com/chromium/chromium/blob/cebb23461ac11d291f8eac596e6b73283c167b4d/docs/documentation_best_practices.md#L20-L112) | Same-CL documentation policy, comments for why versus API contracts, README purpose, and design docs as historical archives after implementation. |
| E3 | D | [base/task/README.md](https://github.com/chromium/chromium/blob/cebb23461ac11d291f8eac596e6b73283c167b4d/base/task/README.md#L1-L15) | A real component README explains directory responsibilities and points to broader guides. |
| E4 | C | [sequenced_task_runner.h](https://github.com/chromium/chromium/blob/cebb23461ac11d291f8eac596e6b73283c167b4d/base/task/sequenced_task_runner.h#L106-L150) | An interface header documents ordering and non-nesting guarantees. |
| E5 | P/D | [docs/README.md](https://github.com/chromium/chromium/blob/cebb23461ac11d291f8eac596e6b73283c167b4d/docs/README.md#L10-L50) | New documents are added to a central index; Gitiles is the authoritative rendered view and changes can be previewed. |
| E6 | H | [ThreadPool rename commit](https://github.com/chromium/chromium/commit/43fd37033b05a48a6f2f3f87fdb844844d84e650) | A large ThreadPool refactor changed implementation files and updated base/task/README.md in the same commit. |

## 4. What the project actually does

Chromium's guidelines describe three layers:

1. **Module/component documentation:** README files at the root of a component explain what related classes are for, their rough structure, and intended use.
2. **Interface/class documentation:** comments near class definitions describe what a class does and how it should be used.
3. **Implementation documentation:** comments next to implementation code explain how the code works or why a non-obvious path exists.

The inspected base/task README is a concise directory map. It distinguishes public APIs from ThreadPool, SequenceManager, and shared implementation details, then links to broader threading and callback documentation. It does not enumerate every file.

The SequencedTaskRunner header comment describes externally relevant guarantees: task ordering, sequencing, nested versus non-nested execution, and the consequences of posting a non-nestable task. This is interface behavior, not a line-by-line explanation of the implementation.

Chromium's best-practices document says documentation should change in the same CL as code. It distinguishes inline comments, which explain why code exists, from method API comments, which describe arguments, return values, restrictions, errors, and behavior. It says behavior documented in API comments should reasonably have a test.

The same guide says that after code is implemented, design documents should be treated as archives of decisions rather than as current implementation documentation. The docs directory README also asks contributors to add new pages to the index and explains how to preview the Gitiles-rendered result.

### A real same-CL example

The 2019 ThreadPool rename commit changed a large set of implementation and test files and also modified base/task/README.md. The README's description was updated from ThreadPool to ThreadPoolInstance in the same commit. The patch is small, but it is exactly the kind of change the same-CL rule is intended to capture: a component's public vocabulary changed, so its directory map changed with it.

This is one concrete confirmation of the policy, not proof that every Chromium CL follows it.

## 5. Why these practices may exist

**Stated rationale:** Same-CL updates keep docs fresh and give reviewers a place to understand the code change. Component READMEs orient developers who encounter a directory without knowing its purpose. API comments define the contract future programmers rely on.

**Inferred rationale:** The three layers reduce the temptation to make every source comment too broad or every external document too granular. The component README provides navigation, the header defines behavior, and implementation comments explain local reasoning.

**Unknown:** This inspection has one positive same-CL example, but has not sampled enough Gerrit CLs to estimate compliance or identify common exceptions. The docs index is also a manual navigation mechanism; its ongoing completeness has not been measured.

## 6. Comparison with JIT-DW hypotheses

| Hypothesis | Alignment | Evidence and qualification |
|---|---|---|
| Documentation needs multiple levels of detail | supports | Chromium explicitly defines module, interface, and implementation layers. |
| Important modules need local entry points | supports | The guideline calls for a README for a self-contained directory; base/task has one. |
| Every source file needs a Markdown responsibility record | contradicts | The actual component README summarizes directory structure rather than listing every file. |
| API comments should describe contracts | supports | SequencedTaskRunner documents ordering and execution guarantees. |
| Inline comments should explain why rather than restate code | supports | Explicitly stated in best practices. |
| Historical design docs should remain current implementation truth | contradicts | Chromium says implemented-code documentation belongs with the code and design docs become archives. |
| Every code change updates docs in the same CL | partially supports | Policy is explicit and one real refactor updated the README in the same commit; broader compliance remains unmeasured. |

## 7. Trade-offs and limitations

- A central document index is useful but creates a maintenance obligation.
- A component README should remain a navigation map; if it becomes a second copy of all module details, it will drift.
- The same-CL policy is clear, but one successful example does not establish project-wide compliance.
- Chromium's use of Gerrit CLs differs from projects whose primary workflow is GitHub pull requests.

## 8. Findings

- **Observed practice:** Chromium separates directory orientation, interface contracts, and implementation rationale, and the inspected component follows that layering.
- **Stated rationale:** Documentation should remain fresh and help reviewers and future maintainers understand changes.
- **Inferred rationale:** Local documentation makes the right information discoverable at the point of work.
- **Confidence:** High for policy and inspected examples; medium for project-wide consistency.
- **What JIT-DW should adopt:** A layered placement model and local directory README where a component boundary is meaningful.
- **What JIT-DW should not copy:** A mandatory README for every directory regardless of whether it is a meaningful component.
- **What needs pilot validation:** How much directory-level detail is enough before it becomes a maintenance burden.
