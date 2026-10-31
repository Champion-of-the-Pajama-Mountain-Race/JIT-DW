# Validation plan

**Status:** Guide-only usability pilots are still planned. Optional advisory prototype tests and GitHub Actions Runner probes have executed, but no independent Guide usability or maintenance-cost trial has been completed.

The **Guide** must be tested with real developers and maintenance tasks, without requiring them to run the optional classifier. A complete-looking template set or passing CI is not evidence that readers can use the documentation.

## Guide-first test: developer autonomy and reader success

Before evaluating automation accuracy, compare a developer using **only the [Guide](../guide/README.md)** against an ordinary baseline on a real task.

- Ask the person to decide whether they need a new document, an existing-page change, a source comment, clearer API code, or no documentation change.
- Observe whether they can explain the intended reader and the reason for the choice.
- Give a second reader a concrete task to complete using the result.
- Record **time, reader success, unnecessary new artifacts, confusion, and whether the developer felt constrained**.
- Include one code-only refactor (where doing nothing may be correct) and one genuine reader-facing API/onboarding problem.
- Give the developer final authority subject to the project's actual conventions. Do not award points for filling a template.

The advisory tool should be evaluated separately, only if it appears to add value beyond the Guide.

## 1. Pilot types

### Pilot A — multi-module project

Test whether the workflow helps contributors understand boundaries, locate authoritative information, and identify documentation impact across modules.

### Pilot B — small project

Test whether the Lite profile can improve discoverability without imposing unnecessary documents, review steps, or tooling.

Choose projects with permission to make a documentation-only trial or use a controlled branch. Record baseline conditions before changing the workflow.

## 2. Task-based evaluation

Use concrete tasks rather than asking participants whether the docs look good.

Examples:

- locate the entry point for a subsystem;
- identify the owner of a public interface;
- explain the effect of a configuration default;
- find the source of truth for a data structure;
- modify a public interface and identify all relevant documentation;
- decide whether an internal refactor requires a documentation update;
- follow a runbook or contributor guide to complete a task.

Record success, time, wrong turns, missing information, and whether a maintainer had to intervene.

## 3. Measures

| Measure | Operational definition | Why it matters |
|---|---|---|
| Discovery success | Participant finds the authoritative artifact without maintainer intervention | Tests navigation and information ownership. |
| Change-impact precision | True positives / (true positives + false positives): relevant docs correctly proposed / all docs proposed | Tests whether the workflow avoids needless updates. |
| Change-impact recall | True positives / (true positives + false negatives): relevant docs correctly proposed / all docs judged relevant after expert review | Tests whether important updates are missed. |
| Stale-information defects | Verified conflicts between docs and current intended behavior | Tests documentation accuracy. |
| Task completion | Participant completes a predefined task using the docs | Tests usefulness, not just readability. |
| Maintenance effort | Time spent assessing, updating, reviewing, and validating docs | Tests whether process overhead is acceptable. |
| Unnecessary documentation churn | Changes made without a corresponding information change | Detects ritual updates. |

### Defining the impact evaluation set

Before scoring, two maintainers (or a maintainer and independent reviewer) should decide which documents or representations **actually required review** for the test change. If they disagree, record the disagreement and adjudication instead of hiding it in an average.

- **True positive:** JIT-DW proposes a documentation representation and the reference reviewers agree it required attention.
- **False positive:** JIT-DW proposes a representation that does not require attention.
- **False negative:** JIT-DW misses a representation that required attention.
- **True negative:** An unrelated artifact that correctly requires no attention (usually not individually enumerated).
- **Abstention:** JIT-DW explicitly marks a proposed impact as unknown; report separately from both positive and negative predictions.

Use the same unit of evaluation throughout a trial (e.g. docs artifact, semantic assertion, or representation); do not mix document-level and fact-level counts. When there are no predicted positives or no reference positives, report precision/recall as not applicable rather than inventing a perfect score.

**Self-audit correction:** The previous V0.1 plan accidentally used recall's denominator for both precision and recall. That made the metrics identical and unable to detect unnecessary update suggestions. The formulas above correct it; no pilot data existed under the erroneous definition.

Record sample size and limitations. Do not claim statistical significance from a tiny pilot.

## 4. Advisory-only trial from Round 2 findings

First use the [change-impact protocol](../docs/workflow/impact-review-protocol.md) without blocking contributions.

Include test changes like:
- a code-only internal optimization with no apparent public contract change;
- a new public API that affects several user-facing documents;
- source-comment-only API behavior clarification replicated across versions;
- a refactor with inline contracts but no new README;
- changes to documentation build/discovery tooling.

Record proposed outcome, author/maintainer judgment, the final resolved impact, and additional review time. Treat "unknown" as a meaningful abstention, not a disguised "no docs needed".

Do not promise that all proposals are correct because the selected examples look persuasive.

## 5. Comparison

Where feasible, compare:

- baseline workflow before JIT-DW;
- workflow after adopting the selected profile;
- the same or closely matched tasks;
- maintainer judgment against the participant's impact assessment.

Avoid comparing unrelated repositories as if they were controlled experiments.

## 6. Exit criteria

A pilot should result in one of:

- **adopt:** the workflow provides clear benefit at acceptable cost;
- **revise:** benefit exists but a specific part creates confusion or overhead;
- **reject:** the proposed mechanism does not improve the target problem;
- **inconclusive:** evidence is insufficient.

Document negative results. They are part of the research.

## 7. First implementation baseline

The first working advisory prototype and its limitations are described in the [Codex + AstrBot pilot plan](pilots/codex-astrbot/README.md). Eight real PRs were sampled (four per project), and deterministic path-to-question behavior has local Python standard-library tests. These fixtures are not independently labeled gold-standard documentation impacts; no precision, recall, user-task success, or maintenance time is reported yet. Running the test workflow on a hosted GitHub runner validates the prototype only, not the full Codex or AstrBot build.
