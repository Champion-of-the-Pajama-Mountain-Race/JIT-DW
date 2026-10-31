# Runner probe: Codex and AstrBot Forks

**Date:** 2026-10-31. **Status:** Both GitHub-hosted jobs passed; both self-hosted jobs remained queued when checked. This is an access/scheduling uncertainty, *not* evidence of missing toolchains.

| Public organization Fork | GitHub Actions run | Hosted job | `[self-hosted, linux, x64]` |
|---|---|---|---|
| [codex pilot branch](https://github.com/Champion-of-the-Pajama-Mountain-Race/codex/tree/research/jitdw-advisory-pilot) | [41193961696](https://github.com/Champion-of-the-Pajama-Mountain-Race/codex/actions/runs/41193961696) | **success** | queued, not executed |
| [AstrBot pilot branch](https://github.com/Champion-of-the-Pajama-Mountain-Race/AstrBot/tree/research/jitdw-advisory-pilot) | [41193966981](https://github.com/Champion-of-the-Pajama-Mountain-Race/AstrBot/actions/runs/41193966981) | **success** | queued, not executed |

Both branches were created via the connected GitHub account with write permission. Each has `.github/workflows/jitdw-runner-probe.yml` scoped to a **push on the pilot branch when that file changes**. The probe has read-only permissions and executes **no checkout or project code**; the hosted job prints basic versions, and the self-hosted job would check tool presence and versions only if GitHub schedules it.

## Organization Runner exists and works somewhere

The private [Bot_R_A_D Rustdoc run 41185445260](https://github.com/Champion-of-the-Pajama-Mountain-Race/Bot_R_A_D/actions/runs/41185445260) succeeded with runner `org-linux-01`, group `default`, machine `Bot`; its logs reported Actions runner 2.338.2, Git 2.53.0, and Rust/Cargo 1.98.0 on Linux x64.

That validates **this private repo**, not permission to schedule jobs from the public Forks. The connector cannot directly read the organization runner-group access settings. Both queued Fork jobs may reflect selected-repository/private-only access or unavailable Runner capacity; those alternatives have not been distinguished.

GitHub documents that a self-hosted job remains queued until an eligible runner is available, with a [24-hour queue limit](https://docs.github.com/en/actions/reference/runners/self-hosted-runners).

## Trusted private-repo toolchain probe (completed)

To distinguish missing packages from public-Fork Runner-group restrictions, we created a separate isolated branch in the **private** Bot_R_A_D repository. Its [workflow run 41194851961](https://github.com/Champion-of-the-Pajama-Mountain-Race/Bot_R_A_D/actions/runs/41194851961) **succeeded** on self-hosted Runner `org-linux-03` (also in group `default`, machine `Bot`). No checkout, repository code, secrets or privileged build commands were involved.

| Tool | Observed version or status |
|---|---|
| Git | 2.53.0 |
| Python 3 | 3.14.4 |
| uv | 0.12.5 |
| rustup | 1.29.0 |
| rustc / Cargo | 1.98.0 |
| Node.js | 22.23.4 |
| npm / pnpm | Commands present; version lines obscured by an experimental proxy warning |
| just | **missing from PATH** |
| bazel | **missing from PATH** |
| bazelisk | **missing from PATH** |
| dotslash | **missing from PATH** |

These are real environment observations for `org-linux-03`, **not** proof of the same PATH state on every other Runner instance. Codex's documented source-build helpers include just, DotSlash, cargo-nextest, and Bazel-based CI; further installation is only needed if a trusted Codex build is deliberately scheduled on that machine. The JIT-DW Python advisory trial has no such dependency and already passes on hosted runners.

This private-repo probe confirms self-hosted scheduling works inside an eligible private repository. It does not resolve the public-Fork queued jobs, which should not be "fixed" by broadening persistent Runner access.

## Refined toolchain inventory on a second private Runner instance

A second run, [41195112204](https://github.com/Champion-of-the-Pajama-Mountain-Race/Bot_R_A_D/actions/runs/41195112204), succeeded on `org-linux-02` (same `default` group and `Bot` machine). It clarified the earlier npm/pnpm output and checked additional tools:

| Tool | Observed on org-linux-02 |
|---|---|
| Python 3 / Python 3.12 | 3.14.4 / 3.12.16 |
| uv | 0.12.5 |
| rustc / Cargo / rustfmt | 1.98.0 / 1.98.0 / 1.9.0-stable |
| Git | 2.53.0 |
| Node / npm / pnpm | 22.23.4 / 10.9.9 / 9.15.9 |
| cargo-nextest | **missing** |
| just | **missing** |
| bazel / bazelisk | **missing** |
| dotslash | **missing** |
| clang / cmake | present; versions not fully extracted in this probe |

These are checks of what is on PATH, not assertions that the tools cannot be installed or bootstrapped by project workflows. AstrBot's docs build specifies Node 24.13.0 and pnpm 10.28.2, so the existing Node 22/pnpm 9 installations are **not the declared docs-build versions**. Codex source-build documentation lists just, DotSlash and cargo-nextest; Codex's primary PR CI uses Bazel.

**No installation is necessary for the JIT-DW advisory trial on hosted Ubuntu.** Before any larger trusted build on the private machine, install/pin dependencies in a dedicated job or isolated environment rather than modifying the machine blindly.

## Security decision

**Do not grant these public Forks access to the existing persistent organization Runner just to clear a queued smoke test.** GitHub [recommends self-hosted runners primarily for private repos](https://docs.github.com/en/actions/how-tos/manage-runners/self-hosted-runners/manage-access), because untrusted public pull requests can compromise a self-hosted machine. For the next JIT-DW experiments, use hosted Ubuntu; a separate ephemeral, isolated Runner is the alternative for a costly build.

If jobs remain queued, they can be canceled from each workflow's Actions page; GitHub otherwise times out unclaimed jobs. No sensitive software was run on the organization's machine by these Fork tests.

## Environment conclusion

- JIT-DW Python advisor: **no missing dependencies identified**; tests passed earlier on hosted Ubuntu/Python 3.12.
- Codex and AstrBot hosted probes: **no missing dependencies for the probes**.
- Full Codex/AstrBot builds: **not attempted**; no package absence should be claimed.
- Organization self-hosted on these Forks: **not scheduled**, so tool presence cannot be measured.

A passing probe does not equal passing the respective project's native test suites.
