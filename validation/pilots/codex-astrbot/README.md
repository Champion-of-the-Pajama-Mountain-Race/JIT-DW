# Codex + AstrBot: retrospective pilot baseline

**Status:** Upstream diff inspection, local and hosted prototype tests, organization Fork creation, and successful hosted Runner probes completed. Both public-Fork self-hosted probes initially queued and were later cancelled after the workflows were changed to hosted-only. This is *not* a validated documentation-impact accuracy result.

**Inspected:** 2026-10-31. Both targets were confirmed publicly readable:
- https://github.com/openai/codex (default branch main)
- https://github.com/AstrBotDevs/AstrBot (default branch master)

The target organization is Champion-of-the-Pajama-Mountain-Race. Neither org/codex nor org/AstrBot existed when checked. The GitHub connector can create branches, commits, and PRs in existing accessible repos but does not expose a create-fork/create-repository action. The isolated local environment has no authenticated gh and cannot resolve github.com. No upstream source was modified.

## Fork and runner results

Both organization Forks exist and the connected GitHub account can create branches and commits:

- [Codex pilot branch](https://github.com/Champion-of-the-Pajama-Mountain-Race/codex/tree/research/jitdw-advisory-pilot)
- [AstrBot pilot branch](https://github.com/Champion-of-the-Pajama-Mountain-Race/AstrBot/tree/research/jitdw-advisory-pilot)

The branches contain only isolated, branch-scoped Runner-probe workflows. Their **GitHub-hosted jobs passed**; self-hosted jobs initially queued and were then cancelled after removing those jobs from the public Fork branches. The older "Fork setup required" instructions are superseded. See the [dated Runner evidence](runner-probe.md).

**Safety:** Both Forks are public. Do not grant the existing persistent organization Runner blanket access merely to clear the queued jobs. Use hosted CI for this advisory experiment.

The [Codex/AstrBot source comparison](../../../research/round-3/codex-astrbot-comparison.md) documents confirmed JIT-DW design points and newly discovered gaps.

## Why these projects are good contrasts

Codex is a large Rust project with modules, rustdoc, protocol schemas, generated TypeScript/Python APIs, local READMEs, and a split Bazel/Cargo CI strategy. AstrBot is a Python + Vue project with a public plugin API, translated English/Chinese docs, generated OpenAPI/client files and contributor rules that tie WebUI navigation changes to docs.

### Codex actual PR examples

| PR | Observed change | Documentation impact hypothesis |
|---|---|---|
| [#43423](https://github.com/openai/codex/pull/43423) | Only AGENTS.md changed; a blanket app-server docs update requirement was removed while schema regeneration instructions remained. | Docs requirements should have meaningful triggers, not blanket file-based rules. |
| [#52610](https://github.com/openai/codex/pull/52610) | Seven linux-sandbox files: README, Rust source comments and renamed modules/tests. README explains bubblewrap, seccomp, legacy Landlock and network boundaries. The PR states enforcement behavior did not change. | A terminology/boundary refactor may need updated module docs even if runtime contract is unchanged. |
| [#49361](https://github.com/openai/codex/pull/49361) | Six source/snapshot files update the misleading auth.json persistence wording. There was no separate Markdown edit. | UI copy and command output can be the relevant user-facing documentation surfaces. |
| [#57172](https://github.com/openai/codex/pull/57172) | Large protocol and runtime update: startedAtMs/completedAtMs appear in schemas, generated TS/Python types, tests and app-server README. README notes older servers may omit the fields. | One API fact can propagate into many generated and human-readable representations. |

Project context: [Codex installation](https://github.com/openai/codex/blob/main/docs/install.md) lists Rust, just, DotSlash, cargo-nextest. [Workflow strategy](https://github.com/openai/codex/blob/main/.github/workflows/README.md) separates PR-time Bazel/fmt checks from heavier Cargo checks after merge. Full repository builds are not justified for the Python-only JIT-DW pilot tool.

### AstrBot actual PR examples

| PR | Observed change | Documentation impact hypothesis |
|---|---|---|
| [#10775](https://github.com/AstrBotDevs/AstrBot/pull/10775) | New Decision Provider API, source docstrings, Chinese/English developer guides, WebUI docs, localization, generated interfaces and tests. | Real bilingual contract and generated-reference coordination. |
| [#10788](https://github.com/AstrBotDevs/AstrBot/pull/10788) | Two files; plugin configuration reload errors become explicit and five parameterized HTTP regression cases were added. The saved config is retained after failure. No docs file changed. | Ask whether any user guide promises reload success/rollback; no automatic failure solely for missing Markdown. |
| [#10685](https://github.com/AstrBotDevs/AstrBot/pull/10685) | Removes pip --trusted-host default TLS bypass; updates implementation comments, config description translations and tests. | Configuration labels and security comments are document representations, too. |
| [#10879](https://github.com/AstrBotDevs/AstrBot/pull/10879) | Seven translated READMEs plus two SerpApi docs pages; no runtime code. | Docs-only synchronization across languages and link targets. |

Project context: [AstrBot CONTRIBUTING](https://github.com/AstrBotDevs/AstrBot/blob/master/CONTRIBUTING.md) explicitly asks for docs/zh and docs/en synchronization on WebUI navigation changes and says to run docs build. [AstrBot AGENTS](https://github.com/AstrBotDevs/AstrBot/blob/master/AGENTS.md) describes uv, Ruff, and API client regeneration. [pyproject](https://github.com/AstrBotDevs/AstrBot/blob/master/pyproject.toml) requires Python >=3.12.

## Executable advisory baseline

- [Project-specific prompts](profiles.json) are tied to changed-file patterns and verified real PRs.
- [Fixtures](fixtures/) provide 8 real PR samples: 4 Codex, 4 AstrBot.
- Each fixture is explicitly marked **complete** or **subset**. Subset fixture counts are not full PR file counts.
- [Advisor](../../../tools/jitdw_advisor.py) uses Python's standard library only; it produces review prompts, not an automatic requirement to add docs.
- [Tests](../../../tests/test_jitdw_advisor.py) check deterministic classification, negative cases, input validation, and abstention.

Run from the JIT-DW checkout:

    python -m unittest discover -s tests -p 'test_jitdw_advisor.py' -v
    python tools/jitdw_advisor.py --profile codex --input validation/pilots/codex-astrbot/fixtures/codex-linux-sandbox-pr52610.json
    python tools/jitdw_advisor.py --profile astrbot --input validation/pilots/codex-astrbot/fixtures/astrbot-reload-pr10788.json --format json

**Verified results:** 14 Python unittest cases passed locally. The same test suite and sample CLI generation also passed on a GitHub-hosted Ubuntu runner in [JIT-DW Actions run 41186150913](https://github.com/Champion-of-the-Pajama-Mountain-Race/JIT-DW/actions/runs/41186150913) for commit 21d1a6c957f62f6867eb7f11f56cec8d1f0a8c77. This validates the prototype's mechanical behavior, **not** the correctness of predicted documentation impact.

## Measurement and acceptance

For each PR, have a knowledgeable maintainer identify changed semantic facts and independently label needed representations. Compare the advisor's *proposals* with those assessments. Record true positives, false positives, misses, unknowns, and extra reviewer time. No relevance gold standard exists yet, so **no precision or recall figure is claimed**.

Use Updated / No update required / Deferred / Unknown per changed fact. A source code refactor with inline docs and no README should not automatically be marked as a documentation failure. A changed schema may need generated outputs and a user-facing explanation, but that conclusion requires inspecting the actual contract.

## Runner needs

- **JIT-DW advisor:** GitHub-hosted ubuntu-latest + Python 3.12; standard-library only. No self-hosted runner required.
- **Future Codex fork code checks:** pinned Rust toolchain and possibly Bazel, just, dotslash, cargo-nextest, build tools and sufficient disk space for scoped crate tests. Inspect fork workflow/toolchain pin before installing.
- **Future AstrBot fork code checks:** Python >=3.12, uv, Ruff/pytest, and Node + pnpm if documentation site/WebUI or generated clients are touched.

Hosted runners successfully ran the two Fork probes. Organization self-hosted jobs were initially queued in the public Forks and then cancelled without execution. Detailed tool inventories from separate private systems are not published in this public research repository; for public Fork trials, use the [hosted-runner evidence](runner-probe.md) and install dependencies only if a real scoped build needs them. CI should start advisory and scope tests narrowly; don't enable untrusted upstream workflows with privileged secrets.

## Limitations and next step

This is a retrospective upstream PR analysis, not a fork-based live change experiment. Some fixtures intentionally sample only part of large PRs. Neither upstream test suite was executed; no real maintenance-cost or reader-task experiment has been completed. Fork availability is resolved. Remaining validation work: expert labeling of documentation impacts, a real scoped hosted-runner experiment, and measurement of false positives, misses and reviewer time. 
