# Candidate projects for repository-level research

**Status:** Queue only. Inclusion does not imply endorsement or prior verification.

The goal is not to audit every project exhaustively. Select representative artifacts and follow a small number of real changes deeply enough to understand the relationship between policy, source comments, maintained docs, tests, automation, and history.

| Project | Primary questions | Initial inspection targets |
|---|---|---|
| Google OpenDocs | Do the repository's own artifacts embody the Docs Advisor and archetype model? How does it distinguish process guidance from deliverables? | docs_advisor/, project_archetypes/, audit/, repository contribution and validation files |
| Linux kernel | How are function/type comments connected to generated docs? Which documentation belongs in code versus Documentation/? | Documentation/, kernel-doc comments in representative subsystems, Sphinx build configuration, documentation contribution rules |
| Chromium | How are directory-level context, design docs, code comments, ownership, and presubmit checks combined? | docs/, representative component README files, source comments, OWNERS, PRESUBMIT.py, documentation best practices |
| Rust | How do doc comments, examples, intra-doc links, and doctests constrain API documentation? | rustdoc/, standard-library docs, rustdoc tests, contribution guidance, relevant CI |
| Python | How do source docstrings relate to the manually authored library reference and developer documentation? | Doc/, representative CPython source modules, docstring conventions, Sphinx configuration, devguide |
| Kubernetes | How are API comments, generated reference docs, versioned docs, and code review coordinated? | API type comments, generated reference sources, website/, contributor docs, verification scripts and CI |
| Django | How do source docstrings, narrative docs, release notes, and contribution practices interact? | docs/, representative model/view/API source, tests, release notes, contribution guidance, documentation checks |

## Selection rules

- Prefer a concrete subsystem or API with visible source comments and corresponding docs.
- Prefer a real PR or commit that changes behavior and lets us observe documentation updates.
- Include examples that contradict our assumptions.
- Record exact commit SHAs before drawing conclusions.
- Do not infer project-wide consistency from one directory or one contributor.
