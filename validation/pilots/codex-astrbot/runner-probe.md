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

## Security decision

**Do not grant these public Forks access to the existing persistent organization Runner just to clear a queued smoke test.** GitHub [recommends self-hosted runners primarily for private repos](https://docs.github.com/en/actions/how-tos/manage-runners/self-hosted-runners/manage-access), because untrusted public pull requests can compromise a self-hosted machine. For the next JIT-DW experiments, use hosted Ubuntu; a separate ephemeral, isolated Runner is the alternative for a costly build.

If jobs remain queued, they can be canceled from each workflow's Actions page; GitHub otherwise times out unclaimed jobs. No sensitive software was run on the organization's machine by these Fork tests.

## Environment conclusion

- JIT-DW Python advisor: **no missing dependencies identified**; tests passed earlier on hosted Ubuntu/Python 3.12.
- Codex and AstrBot hosted probes: **no missing dependencies for the probes**.
- Full Codex/AstrBot builds: **not attempted**; no package absence should be claimed.
- Organization self-hosted on these Forks: **not scheduled**, so tool presence cannot be measured.

A passing probe does not equal passing the respective project's native test suites.
