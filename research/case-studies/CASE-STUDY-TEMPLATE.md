# Case study: [project / practice]

**Status:** Draft  
**Repository:** [URL]  
**Revision:** [full commit SHA]  
**Inspection date:** [YYYY-MM-DD]  
**Scope:** [specific subsystem, feature, or documentation workflow]

## 1. Question

What specific documentation practice are we trying to understand?

Avoid broad questions such as "How does Project X do documentation?"

## 2. Repository context

- Project type and approximate scale:
- Primary languages:
- Relevant subsystem:
- Release / contribution model:
- Documentation build system:

Only include context that affects interpretation.

## 3. Evidence inventory

| Evidence ID | Type (P/D/C/I/T/A/H) | Path or commit | Relevant lines / excerpt | What it establishes |
|---|---|---|---|---|
| E1 | | | | |
| E2 | | | | |
| E3 | | | | |

Use commit-pinned URLs where possible. Quote only the minimum passage needed; summarize the rest.

## 4. What the project actually does

Describe observed behavior, not what you think the project ought to do.

- Where is the information authored?
- How close is it to the code it explains?
- What level of detail is maintained?
- What is generated?
- What is manually maintained?
- How is it discovered by contributors and users?
- What is checked automatically?
- What is reviewed by humans?

## 5. Source comments and docstrings

Inspect representative source files.

For each example, explain:

- what the comment documents (intent, invariant, algorithm, API contract, warning, workaround, etc.);
- why this information may belong next to the code;
- whether the implementation or tests corroborate it;
- whether the comment duplicates an external document;
- whether the comment appears stable or likely to become stale.

Do not assume that more comments are better.

## 6. Change workflow

Inspect real PRs or commits if the study concerns maintenance.

| Change | Code paths | Documentation paths | Same change / follow-up? | Review or CI signal |
|---|---|---|---|---|
| | | | | |

Record cases where code changed without documentation, and decide whether that was appropriate or a likely gap.

## 7. Why this practice may exist

Separate the evidence:

- **Stated rationale:** [maintainer or project explanation, with citation]
- **Inferred rationale:** [interpretation and confidence]
- **Unknown:** [what cannot be established]

Consider reader needs, code locality, release cadence, language tooling, safety constraints, and team structure.

## 8. Comparison with frameworks and JIT-DW hypotheses

| Framework / hypothesis | Alignment | Evidence | Qualification or contradiction |
|---|---|---|---|
| Docs as Code | | | |
| Diátaxis | | | |
| C4 / architecture views | | | |
| Change-impact workflow | | | |
| Information ownership | | | |
| Local module documentation | | | |
| Agent navigation | | | |

Use supports, partially supports, contradicts, not observed, or not applicable. Absence in the inspected sample is not proof of absence across the project.

## 9. Trade-offs and failure modes

What does this practice cost? What does it make easier? Where could it fail?

Include counterexamples and inconsistencies.

## 10. Findings

- **Observed practice:**
- **Stated rationale:**
- **Inferred rationale:**
- **Confidence:** High / Medium / Low
- **What JIT-DW should adopt:**
- **What JIT-DW should not copy:**
- **What needs pilot validation:**

## 11. Reproduction notes

List the paths, queries, commands, and revision identifiers needed for another person to repeat the inspection.
