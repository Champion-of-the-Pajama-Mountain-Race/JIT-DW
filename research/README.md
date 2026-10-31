# Research method

**Status:** Research protocol. No project-level conclusions should be treated as findings until supported by case-study evidence.

The central requirement of this research is to inspect what open-source projects actually maintain—not only what their documentation guidelines say they should maintain.

## 1. Research questions

1. Where do projects put explanations of system architecture, modules, APIs, invariants, and operational procedures?
2. What do source comments and docstrings explain that external documentation does not?
3. How do projects distinguish current implementation documentation from historical design rationale?
4. What events trigger documentation changes?
5. How are documentation changes reviewed, tested, generated, or enforced?
6. How is responsibility assigned across files, directories, modules, and teams?
7. Which practices are consistent with published frameworks, and which contradict or refine them?
8. What maintenance costs or failure modes are visible in repository history?

## 2. Evidence categories

Each case study must label evidence by type:

| Code | Evidence type | What it can establish |
|---|---|---|
| P | Policy or guidance | What maintainers say contributors should do. |
| D | Maintained documentation | What readers are actually given. |
| C | Source comment / docstring | What the implementation explains locally. |
| I | Implementation structure | Boundaries, interfaces, generated annotations, and code organization. |
| T | Tests / fixtures / examples | Executable expectations and behavior contracts. |
| A | Automation / CI / presubmit | What the project mechanically checks or generates. |
| H | History / PR / issue | How documentation changes alongside code in real work. |

A policy file alone cannot establish that the policy is followed. A source comment alone cannot establish that readers find it useful. Strong conclusions should compare multiple evidence types.

## 3. Evidence quality

Use these confidence labels:

- **High:** directly observed in a pinned repository revision and corroborated by another evidence type or repeated examples.
- **Medium:** directly observed in one or more files, but intent, consistency, or practical effect is not fully established.
- **Low:** plausible interpretation, isolated example, or incomplete evidence.

For claims about why a project uses a practice, separate:
- **stated rationale** — explicitly explained by maintainers;
- **inferred rationale** — a reason suggested by the design or context, labeled as inference;
- **unknown** — repository evidence does not establish the reason.

Do not turn inference into fact.

## 4. Repository inspection protocol

For each project:

1. Record repository URL, default branch, and exact commit SHA.
2. Inspect top-level structure and documentation entry points.
3. Locate contribution guidance, documentation policies, ownership files, build configuration, and CI checks.
4. Select representative modules and inspect:
   - source comments and docstrings;
   - nearby README or design documentation;
   - public API or schema definitions;
   - tests and examples;
   - generated documentation inputs and outputs.
5. Inspect a small number of relevant PRs or commits to see whether docs change with code.
6. Compare observed practice with published guidance (for example Diátaxis, C4, Docs as Code, or the project's own policy).
7. Record counterexamples, gaps, and maintenance trade-offs.
8. Write a bounded conclusion: what the evidence supports, what it does not support, and what needs further inspection.

## 5. Case-study output

Use case-studies/CASE-STUDY-TEMPLATE.md.

Each claim should link to a specific file or commit and, where possible, a line range. Pin references to a commit SHA so the evidence remains reproducible when the default branch changes.

## 6. Anti-patterns in our own research

- citing only a project homepage or high-level guide;
- treating the presence of a template as proof it is used;
- treating a directory tree as proof of clear ownership;
- inferring intent from a comment without corroboration;
- selecting only examples that support our preferred design;
- generalizing from one subsystem to an entire project;
- comparing projects without accounting for language, scale, safety requirements, and release model;
- copying a practice without recording its trade-offs.

## 7. First field-study tranche

The first source-based case studies are now available:

- Google OpenDocs — planning methods and documentation project archetypes.
- The Good Docs Project — reusable templates and their authoring process.
- Linux kernel — structured source comments and generated API reference.
- Chromium — layered component/interface/implementation documentation.
- CPython — overlapping source docstrings and separate library reference.
- Rust — public API comments and executable documentation tests.
- Kubernetes — API field comments, structured markers, and verification scripts.
- Django — reader-oriented docs, feature PRs, and documentation tooling.

See [the evidence register](evidence-register.md) for pinned revisions and [the synthesis](findings-v0.1.md) for cross-project conclusions.

These are bounded samples, not exhaustive audits.

## 8. Second research tranche

The next stage inspects real commits, review comments, and responsibility-routing configuration. Its results are available in [Round 2](round-2/README.md), including a [curated change-history sample](round-2/change-history-sample.md), a [Django HTTP QUERY end-to-end trace](round-2/django-query-end-to-end.md), and [ownership/review-routing evidence](round-2/ownership-and-review-routing.md).

Read the [V0.2 synthesis](findings-v0.2.md) for the revised conclusions and the [advisory impact-review protocol](../docs/workflow/impact-review-protocol.md) for a testable procedure. These are still hypotheses to validate in pilots; they are not production-compliance statistics.

## 9. Round 3: Codex/AstrBot Fork-based source comparison

The [third-round comparison](round-3/codex-astrbot-comparison.md) explicitly separates JIT-DW ideas corroborated by actual Codex/AstrBot files and PRs from mechanisms our initial model did not handle well: runtime-parsed docstrings, AST-checked inline hints, complete generated artifact closure, multilingual UI navigation, and actual CI execution/coverage. The [Runner report](../validation/pilots/codex-astrbot/runner-probe.md) records successful hosted probes on both public Forks and a successful private-repository toolchain inspection on the existing self-hosted Runner. This does **not** demonstrate lower documentation cost or a measured impact-prediction accuracy rate.
