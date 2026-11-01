# Project activity check — 1 November 2026

Checked against the connected GitHub account and saved source-build evidence on 1 November 2026. This is a dated report, not a live build badge.

## Inventory and scope

The accessible owned inventory contains **44 repositories: 34 public and 10 private**. The public table below includes only public projects. The older 18 October inventory remains historical.

The check read up to 10 recent Actions runs per repository, plus up to 30 runs on each public repository's default branch. Each run retains its branch, date and source revision. A green feature-branch run does not qualify the default branch, and a successful scheduled report does not prove the application's full test suite passed. An empty run history is unverified.

## Current work

- **Seed Engine:** the saved 1 November source-build report records 6/6 CPU/debugger harness checks, 14/14 C++ regressions, a backing-memory ownership probe, and 9/9 integration checks. The repair covers PC/SP register bounds, trace delivery, memory lifetime, error exits and build/run scripts. ASan/UBSan passed with leak detection disabled; LeakSanitizer was unavailable. These are execution results from the report's build host, not a fresh run on the developer's PC.
- **ARM64 milestone:** the Seed instruction step is still a placeholder. The assembly fixture was not loaded or executed. A working harness does not establish guest execution, a game boot, graphics or gameplay.
- **Local developer tools:** DragonForge Code, OpenCode, Rabbit Code and Greenlight remain active areas. Current CI evidence and known failures are recorded by branch below; consumer-GPU training and resume qualification remain separate milestones.
- **RepoForge / DragonHub page:** replace the old sample list with a dated public inventory; inspect the latest result of each workflow on the selected repository's default branch. Independent failing workflows must remain visible after another workflow succeeds. Public scans exclude private and unclassified entries.

## Errors still requiring evidence

| Project/check | Observed failure | Next gate |
| --- | --- | --- |
| [Profile external Linux evaluation](https://github.com/HenricHuntsman/HenricHuntsman/actions/runs/39134948356) | The Skorpion ISO download did not complete; its checksum failed. The Skai job passed in that same run. | Complete and verify the pinned ISO before attempting another isolated boot. Preserve the failed checksum. |
| [Azeroth localisation](https://github.com/HenricHuntsman/azeroth-pilot-reloaded/actions/runs/41217863555) | CurseForge returned HTTP 401; the job's API-key input was empty. | The repository owner must configure authorised service access before notification delivery can work. |
| [DragonForge build](https://github.com/HenricHuntsman/dragonforge-code/actions/runs/39497259397) | A separate build workflow failed although the `ci` workflow passed. | Inspect its check annotations; the passing workflow does not erase this historical failure. |

Research branches, upstream copies and repositories without default-branch runs remain visible; they are not automatically treated as broken or release-ready.

## Public default-branch run history

“Other latest failures” means the newest run of each distinct workflow within the inspected window, rather than every old failed attempt. A newer pass supersedes an older failure of that same workflow. This bounded history does not establish current-HEAD coverage or every optional lane.

| Public repository | Default branch | Most recent recorded run | Other latest failures in inspected window |
| --- | --- | --- | --- |
| [-https-SpidermanTotro.github.io-nebula-ultimate-](https://github.com/HenricHuntsman/-https-SpidermanTotro.github.io-nebula-ultimate-) | `main` | No runs found | None observed in this window |
| [4NXCI](https://github.com/HenricHuntsman/4NXCI) | `master` | No runs found | None observed in this window |
| [AgentFoundry-instantly](https://github.com/HenricHuntsman/AgentFoundry-instantly) | `main` | [success · 2026-10-19](https://github.com/HenricHuntsman/AgentFoundry-instantly/actions/runs/39190517509) | None observed in this window |
| [AgentFoundry-TrinityCore-Studio](https://github.com/HenricHuntsman/AgentFoundry-TrinityCore-Studio) | `main` | No runs found | None observed in this window |
| [anomalyco-opencode-](https://github.com/HenricHuntsman/anomalyco-opencode-) | `dev` | No runs found | None observed in this window |
| [artcraft](https://github.com/HenricHuntsman/artcraft) | `main` | No runs found | None observed in this window |
| [azeroth-pilot-reloaded](https://github.com/HenricHuntsman/azeroth-pilot-reloaded) | `dev` | [success · 2026-11-01](https://github.com/HenricHuntsman/azeroth-pilot-reloaded/actions/runs/41272841640) | [Localization ping](https://github.com/HenricHuntsman/azeroth-pilot-reloaded/actions/runs/41217863555) |
| [book-publish-forge](https://github.com/HenricHuntsman/book-publish-forge) | `main` | [success · 2026-10-09](https://github.com/HenricHuntsman/book-publish-forge/actions/runs/37878180468) | None observed in this window |
| [codex](https://github.com/HenricHuntsman/codex) | `main` | No runs found | None observed in this window |
| [continue](https://github.com/HenricHuntsman/continue) | `main` | [skipped · 2026-10-17](https://github.com/HenricHuntsman/continue/actions/runs/39080144414) | None observed in this window |
| [dragonforge-code](https://github.com/HenricHuntsman/dragonforge-code) | `main` | [success · 2026-10-20](https://github.com/HenricHuntsman/dragonforge-code/actions/runs/39497259492) | [build](https://github.com/HenricHuntsman/dragonforge-code/actions/runs/39497259397) |
| [gemini-cli](https://github.com/HenricHuntsman/gemini-cli) | `main` | No runs found | None observed in this window |
| [HenricHuntsman](https://github.com/HenricHuntsman/HenricHuntsman) | `main` | [failure · 2026-10-18](https://github.com/HenricHuntsman/HenricHuntsman/actions/runs/39134948356) | [External Linux and Skai evaluation](https://github.com/HenricHuntsman/HenricHuntsman/actions/runs/39134948356) |
| [https-github.com-SpidermanTotro-genspark-os](https://github.com/HenricHuntsman/https-github.com-SpidermanTotro-genspark-os) | `main` | No runs found | None observed in this window |
| [kilocode](https://github.com/HenricHuntsman/kilocode) | `main` | No runs found | None observed in this window |
| [Kimi-K2](https://github.com/HenricHuntsman/Kimi-K2) | `main` | [success · 2026-10-18](https://github.com/HenricHuntsman/Kimi-K2/actions/runs/39083094509) | None observed in this window |
| [LisaAI-DatingApp](https://github.com/HenricHuntsman/LisaAI-DatingApp) | `main` | No runs found | None observed in this window |
| [LLM4Decompile](https://github.com/HenricHuntsman/LLM4Decompile) | `main` | No runs found | None observed in this window |
| [mini-AGI](https://github.com/HenricHuntsman/mini-AGI) | `main` | [success · 2026-10-14](https://github.com/HenricHuntsman/mini-AGI/actions/runs/38505247412) | [Android](https://github.com/HenricHuntsman/mini-AGI/actions/runs/37850744699) |
| [NebulaUltimate](https://github.com/HenricHuntsman/NebulaUltimate) | `main` | [success · 2026-07-18](https://github.com/HenricHuntsman/NebulaUltimate/actions/runs/29656493840) | None observed in this window |
| [nvm](https://github.com/HenricHuntsman/nvm) | `master` | No runs found | None observed in this window |
| [nxdumptool](https://github.com/HenricHuntsman/nxdumptool) | `rewrite` | No runs found | None observed in this window |
| [opencode](https://github.com/HenricHuntsman/opencode) | `main` | [success · 2026-10-19](https://github.com/HenricHuntsman/opencode/actions/runs/39190511075) | None observed in this window |
| [QuestMaster-Pro](https://github.com/HenricHuntsman/QuestMaster-Pro) | `main` | [success · 2026-10-08](https://github.com/HenricHuntsman/QuestMaster-Pro/actions/runs/37850715181) | None observed in this window |
| [QuestMasterPro](https://github.com/HenricHuntsman/QuestMasterPro) | `main` | No runs found | None observed in this window |
| [rabbit-foundry](https://github.com/HenricHuntsman/rabbit-foundry) | `main` | [success · 2026-10-19](https://github.com/HenricHuntsman/rabbit-foundry/actions/runs/39190504315) | None observed in this window |
| [rea](https://github.com/HenricHuntsman/rea) | `main` | No runs found | None observed in this window |
| [repo-manager-ultimate](https://github.com/HenricHuntsman/repo-manager-ultimate) | `main` | [success · 2026-11-01](https://github.com/HenricHuntsman/repo-manager-ultimate/actions/runs/41288422482) | None observed in this window |
| [skai_ap](https://github.com/HenricHuntsman/skai_ap) | `main` | No runs found | None observed in this window |
| [skorpion_os](https://github.com/HenricHuntsman/skorpion_os) | `main` | No runs found | None observed in this window |
| [Trinity-Studio-Architecture](https://github.com/HenricHuntsman/Trinity-Studio-Architecture) | `main` | No runs found | None observed in this window |
| [TrinityCore](https://github.com/HenricHuntsman/TrinityCore) | `master` | No runs found | None observed in this window |
| [Vitruvian](https://github.com/HenricHuntsman/Vitruvian) | `master` | No runs found | None observed in this window |
| [wordcraft](https://github.com/HenricHuntsman/wordcraft) | `main` | No runs found | None observed in this window |

## Validation of this update

RepoForge's repaired code passed **30 Vitest checks and 17 Python checks**, and the public hosted production build completed locally. Six new regressions reproduced incorrect or incomplete behaviour on the original code before the repair. The DragonHub page's outdated CSP assertion also reproduced a failure before being aligned with the existing public-GitHub connection policy.

GitHub CI and hosting deployment results are recorded separately after publication. Local checks do not establish a new cloud build, remote PC run, or live Forgejo/MCP connection.
