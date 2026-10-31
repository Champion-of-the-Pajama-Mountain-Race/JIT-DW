# Case study: Google OpenDocs

**Status:** Evidence-complete for the scope below; not a study of a production software codebase.  
**Repository:** https://github.com/google/opendocs  
**Revision:** fbc574e261f0cd363a915776e217abced6e7c952  
**Scope:** Docs Advisor, documentation project archetypes, maturity checklist, and planning/template artifacts.

## 1. Question

What does Google OpenDocs contribute to a practical documentation workflow, and which parts are guidance rather than evidence of an implementation being maintained this way?

## 2. Repository context

OpenDocs describes itself as a collection of software documentation templates and guidance. Docs Advisor says it draws on case studies from the completed Google Season of Docs program. This repository is therefore a method and resource collection, not a representative application codebase with runtime source comments, tests, and release automation.

That distinction matters: its recommendations are useful inputs, but they do not prove that the recommended process is followed by any particular project.

## 3. Evidence inventory

| Evidence | Type | Source | What it establishes |
|---|---|---|---|
| E1 | P/D | [Docs Advisor README](https://github.com/google/opendocs/blob/fbc574e261f0cd363a915776e217abced6e7c952/docs_advisor/README.md) | The guide is a flexible menu assembled from documentation practice and Season of Docs case studies. |
| E2 | P | [Part 1: Picking an Approach](https://github.com/google/opendocs/blob/fbc574e261f0cd363a915776e217abced6e7c952/docs_advisor/part_1.md#L3-L35) | Planless Iteration, Mini-Overhaul, and Heroic Overhaul are alternatives selected according to resources and time. |
| E3 | P | [Part 4: Getting It Done](https://github.com/google/opendocs/blob/fbc574e261f0cd363a915776e217abced6e7c952/docs_advisor/part_4.md#L15-L40) | A useful page template specifies document type, necessary sections, writing resources, goal, audience, guidelines, intended outcome, and contributors. |
| E4 | P | [The Manual archetype](https://github.com/google/opendocs/blob/fbc574e261f0cd363a915776e217abced6e7c952/project_archetypes/manual.md#L48-L73) | New documentation work should respond to user needs; the archetype warns against writing docs merely to tick a box and suggests release notes as part of incremental change completion. |
| E5 | P | [The Audit archetype](https://github.com/google/opendocs/blob/fbc574e261f0cd363a915776e217abced6e7c952/project_archetypes/audit.md#L6-L75) | Auditing is a distinct project type for unknown, scattered, unmanaged, or untriaged documentation. |
| E6 | P | [Maturity checklist](https://github.com/google/opendocs/blob/fbc574e261f0cd363a915776e217abced6e7c952/audit/checklist.md#L41-L90) | A small single-maintainer project may reasonably remain at README-level documentation; Docs as Code and feature acceptance criteria are later-stage options. |

## 4. What the repository actually does

Docs Advisor does not prescribe a single large documentation overhaul. It offers three approaches:

- Planless Iteration for limited resources and relaxed timelines;
- Mini-Overhaul for a carefully bounded part of the documentation;
- Heroic Overhaul for a larger, resource-intensive effort.

The guide explicitly notes that Planless Iteration still needs a shared goal and examples of the desired result. It is less plan-centric, not directionless.

The archetypes model documentation work as separate project types. The Manual is often preceded by Study, Audit, or Prototype. The Audit is appropriate when maintainers do not know what documentation exists or what condition it is in. The Manual warns against producing documents simply to satisfy a checklist and recommends considering release notes as part of the completion criteria for incremental software changes.

The page-template guidance is more detailed than a bare Markdown skeleton. It asks template authors to specify purpose, audience, content sections, writing guidance, the goal of the particular document, and participating experts. It also notes that detailed document ownership and maintenance are beyond the scope of that guide.

## 5. Why these practices may exist

**Stated rationale:** The guide is written for maintainers who may have limited time, expertise, and funding. It recommends approaches that fit project circumstances and emphasizes audience research, existing documentation inventory, and explicit outcomes.

**Inferred rationale:** Treating documentation work as distinct project archetypes helps maintainers avoid treating every documentation problem as a generic writing task. An audit, a new tutorial, a site migration, and an editing pass have different risks and deliverables.

**Unknown:** This repository alone does not establish how consistently the approaches work in production projects or how code changes are mapped to specific documentation pages.

## 6. Comparison with JIT-DW hypotheses

| Hypothesis | Alignment | Evidence and qualification |
|---|---|---|
| Projects need different adoption paths | supports | The three approaches vary by time and resources; the maturity checklist allows small projects to remain lightweight. |
| Documentation should start from readers' needs | supports | Study, Audit, and Manual archetypes connect work to audiences and documented problems. |
| Every code change should update documentation | contradicts blanket interpretation | The Manual archetype warns against creating documents for every small UI or option change; release notes may be sufficient. |
| A template should explain how to use it | supports | Part 4 recommends purpose, audience, required content, writing resources, and instance-specific goals. |
| A module contract is a universal artifact | not observed | OpenDocs focuses on documentation project planning, not a universal code-module contract. |
| Documentation impact can be inferred automatically | not observed | No code-diff-to-document mapping mechanism is demonstrated here. |

## 7. Trade-offs and limitations

- The guide is valuable for choosing and scoping documentation work, but it does not implement change-impact analysis.
- Its maturity model should not be turned into a mandatory target for every project.
- The guide itself says document ownership and maintenance are beyond the scope of its page-template advice. JIT-DW must investigate those operational details elsewhere.
- These are recommendations informed by case studies, not proof that a specific software repository follows them.

## 8. Findings

- **Observed practice:** Documentation work is divided into distinct project types and selected according to user needs and available resources.
- **Stated rationale:** Maintainers are often resource-constrained and need approachable, flexible methods.
- **Inferred rationale:** Smaller work units reduce the risk of documentation projects becoming stalled or unfinishable.
- **Confidence:** High for what the guide says; low for claims about real-world effectiveness beyond the case studies it cites.
- **What JIT-DW should adopt:** Adaptive workflows, explicit audience and outcome fields, an audit step when the existing state is unknown, and resistance to checkbox-driven document creation.
- **What JIT-DW should not copy:** Treating the maturity checklist as a mandatory ladder or treating the archetypes as a substitute for code-level evidence.
- **What needs pilot validation:** Whether the lightweight approach actually reduces maintenance burden in a live repository.
