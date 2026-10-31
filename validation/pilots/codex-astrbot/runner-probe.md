# Public Codex and AstrBot Fork runner probes

**Observed:** 2026-10-31. This page records **public-Fork** CI only. Detailed environment information from any private project is deliberately not published here.

## Two verified hosted checks

| Public Fork and branch | Hosted-only run | What passed |
|---|---|---|
| [Codex Fork, research branch](https://github.com/Champion-of-the-Pajama-Mountain-Race/codex/tree/research/jitdw-advisory-pilot) | [41195225991](https://github.com/Champion-of-the-Pajama-Mountain-Race/codex/actions/runs/41195225991) | Basic Ubuntu-hosted workflow without checkout or source execution |
| [AstrBot Fork, research branch](https://github.com/Champion-of-the-Pajama-Mountain-Race/AstrBot/tree/research/jitdw-advisory-pilot) | [41195230456](https://github.com/Champion-of-the-Pajama-Mountain-Race/AstrBot/actions/runs/41195230456) | Basic Ubuntu-hosted workflow without checkout or source execution |

The first probe revision also included a job requesting `[self-hosted, linux, x64]`. Those jobs **queued without executing** on the public Forks and were later **cancelled** when we updated both research workflows to hosted-only.

That is evidence about CI scheduling, **not** evidence of missing compilers, successful project builds, or documentation quality.

## Design consequence for JIT-DW

- Prefer GitHub-hosted or isolated ephemeral runners for public repositories receiving untrusted pull requests.
- Do not grant a persistent organization Runner access to public Forks just to make documentation experiments run.
- Report checks as success, failed, skipped, queued, cancelled or not triggered rather than assuming a checked-in workflow actually ran.
- Scope expensive repository builds to the need of an actual development experiment; a Guide-only reader test does not require a compiler or CI.
- Store private project's Runner inventories, job logs and code-specific task evidence **in that private project**, not in this public Guide repository.

See [GitHub's self-hosted runner access guidance](https://docs.github.com/en/actions/how-tos/manage-runners/self-hosted-runners/manage-access).

## Limits

No full Codex or AstrBot build was run by these hosted probes. No user study or documentation-impact precision/recall has been measured. These experiments do not establish that a public Fork can access an organization's private Runner or that it should.
