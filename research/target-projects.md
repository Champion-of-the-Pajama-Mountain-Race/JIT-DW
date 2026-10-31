# Candidate projects for repository-level research

**Status:** The first field-study tranche is complete for bounded examples. The next tranche should deepen change-history and ownership analysis rather than merely add more project names.

The goal is not to audit every project exhaustively. Select representative artifacts and follow a small number of real changes deeply enough to understand the relationship between policy, source comments, maintained docs, tests, automation, and history.

| Project | Primary questions | Initial inspection targets | Status |
|---|---|---|---|
| Google OpenDocs | How are documentation projects scoped and sequenced? | docs_advisor/, project_archetypes/, audit/ | First tranche complete; guidance repository, not a codebase practice sample |
| The Good Docs Project | What makes templates usable and maintainable? | template files, companion guides, contribution and review process | First tranche complete; template-system sample |
| Linux kernel | How are function/type comments connected to generated docs? | Documentation/, kernel-doc comments, Sphinx build configuration | First tranche complete; one source-plus-doc integration commit sampled |
| Chromium | How are directory context, design docs, code comments, ownership, and presubmit combined? | docs/, component README files, source comments, OWNERS | First tranche complete; one same-commit README update sampled; broader CL history pending |
| Rust | How do doc comments, examples, links, and doctests constrain API documentation? | rustdoc guides, standard-library docs, documentation tests | First tranche complete; one merged source-doc PR sampled |
| Python | How do source docstrings relate to the manually authored library reference? | Doc/, heapq source and reference, Sphinx configuration | First tranche complete; separate source and reference history samples; synchronization analysis pending |
| Kubernetes | How are API comments, generated reference docs, and validation coordinated? | API type comments, API conventions, verify/update scripts | First tranche complete; one six-file API comment update sampled; broader PR history pending |
| Django | How do source docstrings, narrative docs, release notes, and contribution practices interact? | docs/, representative source, feature PRs, documentation checks | First tranche complete; three merged PRs sampled |

## Selection rules

- Prefer a concrete subsystem or API with visible source comments and corresponding docs.
- Prefer a real PR or commit that changes behavior and lets us observe documentation updates.
- Include examples that contradict our assumptions.
- Record exact commit SHAs before drawing conclusions.
- Do not infer project-wide consistency from one directory or one contributor.

## Interpretation boundary

C4 and Diátaxis are frameworks, not substitutes for repository case studies. Google OpenDocs and The Good Docs Project are documentation-method/template repositories, not ordinary application codebases. Their findings should be used for workflow and template design, not as evidence of source-code comment practice.
