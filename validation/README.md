# Validation plan

**Status:** Planned. No pilot results exist yet.

The workflow must be tested against real repositories and real maintenance tasks. A complete-looking template set is not evidence that the process works.

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
| Change-impact precision | Relevant docs identified / all docs judged relevant after expert review | Tests whether the workflow avoids both misses and needless updates. |
| Change-impact recall | Relevant docs identified / all docs judged relevant after expert review | Tests whether important updates are missed. |
| Stale-information defects | Verified conflicts between docs and current intended behavior | Tests documentation accuracy. |
| Task completion | Participant completes a predefined task using the docs | Tests usefulness, not just readability. |
| Maintenance effort | Time spent assessing, updating, reviewing, and validating docs | Tests whether process overhead is acceptable. |
| Unnecessary documentation churn | Changes made without a corresponding information change | Detects ritual updates. |

Record sample size and limitations. Do not claim statistical significance from a tiny pilot.

## 4. Comparison

Where feasible, compare:

- baseline workflow before JIT-DW;
- workflow after adopting the selected profile;
- the same or closely matched tasks;
- maintainer judgment against the participant's impact assessment.

Avoid comparing unrelated repositories as if they were controlled experiments.

## 5. Exit criteria

A pilot should result in one of:

- **adopt:** the workflow provides clear benefit at acceptable cost;
- **revise:** benefit exists but a specific part creates confusion or overhead;
- **reject:** the proposed mechanism does not improve the target problem;
- **inconclusive:** evidence is insufficient.

Document negative results. They are part of the research.
