# Round 2 — Repository-history and review-routing field study

**Status:** Source inspection complete for the bounded cases listed below; broader sampling and field pilots still required.  
**Inspection date:** 2026-10-31.  
**Research mode:** purposive, not random sampling. No population-level compliance rate is estimated.

## Why this round exists

The [first round](../findings-v0.1.md) mostly identified policies, source-level comment structures, and examples. The second round checks actual commits, PR diffs, reviewer discussion, maintenance ownership, and concrete verification scripts.

We intentionally include:
- code plus documentation changed together;
- documentation-only changes inside source files;
- code changes with no accompanying documentation;
- separate doc surfaces maintained independently;
- potentially ambiguous cases where an automatic rule should abstain;
- review tools and responsibility rules whose names do not necessarily reflect actual authority.

## Deliverables

| File | Question answered |
|---|---|
| [Change-history sample](change-history-sample.md) | What did real changes include and omit? |
| [Django QUERY trace](django-query-end-to-end.md) | How can one feature change propagate through code, docs, release notes, tests, review, and explicit non-goals? |
| [Ownership and review routing](ownership-and-review-routing.md) | How do real projects direct review without creating per-file responsibility Markdown? |
| [Django docs tooling drift](django-doc-tooling-drift.md) | What happens when the checks for documentation acquire their own duplicated sources of truth? |
| [Round 2 synthesis](../findings-v0.2.md) | Which JIT-DW assumptions should be retained, revised, or rejected? |

## Method

For each selected change:
1. Record a stable GitHub PR or commit URL and status (merged, unmerged, commit).
2. Inspect the exact changed-file list; do not infer files from a title.
3. Read relevant hunks from implementation, comments, docs, release notes, and tests.
4. Read available review comments where they materially alter the interpretation.
5. Classify *observed fact*, *stated rationale*, *inference*, and *unknown* separately.
6. Apply a provisional JIT-DW impact verdict only as a research exercise, not as an assertion of project-wide quality.
7. Note missing verification explicitly.

## Main limits

- GitHub's changed-file list is evidence of files touched, not proof that all tests actually passed.
- A merged PR is evidence that a change was accepted, not proof that every runtime behavior was tested on every platform.
- Not finding a README at two inspected paths does not prove an entire component is undocumented.
- Review configuration shows *possible routing*, not proof that a reviewer received or acted on a notification.
- The sampled projects are heterogeneous; direct averages would be misleading.
- When investigating Chromium, GitHub is the source mirror; the authoritative review discussions are Gerrit CLs. We inspected a mirrored commit and its metadata but have not audited all Gerrit reviews.

## Pilot gate

Do not promote a proposed automatic "docs required" rule into CI enforcement from these cases alone. First test it as advisory output against real changes, measure false positives and missed documentation impacts, then tune thresholds with maintainers.
