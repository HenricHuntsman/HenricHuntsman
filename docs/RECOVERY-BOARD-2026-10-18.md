> Follow-up: [repository-wide catch-up and prepared source updates](REPOSITORY-CATCH-UP-2026-10-18.md). The original evidence below is retained as an earlier snapshot.

# Project recovery board — 18 October 2026

All 31 public repositories are assigned to a recovery lane. Six private repositories have a separate personal queue. This organises existing work; it does not claim every project is revived.

## Recovery rules

- Preserve repository history, licences, original assets and unique archive payloads.
- Keep working baselines separate from speculative integrations and upstream references.
- Recover one runnable workflow per project before expanding features or assigning RC/RTM.
- No percentage is meaningful without a defined acceptance checklist.
- Documentation-only seeds cannot be resurrected into applications without implementing missing source.
- Observed CI is specific to the named workflow/commit; successful administrative workflows are not build evidence.

## Recovery lanes

### 1 — Working baselines to qualify

| Project | Current evidence | Next recovery milestone |
| --- | --- | --- |
| [Book Publish Forge](https://github.com/HenricHuntsman/book-publish-forge) | [CI: success](https://github.com/HenricHuntsman/book-publish-forge/actions/runs/37878180468) at `ae9900a4f4` | Test real manuscript import/save/export and local-model failure handling |
| [OpenCode — Welcome Back Edition](https://github.com/HenricHuntsman/opencode) | [ci: success](https://github.com/HenricHuntsman/opencode/actions/runs/39037592465) at `9c101864c3`; repository release `v0.0.56` (9 assets) | Smoke-test v0.0.56 on Ubuntu with an installed Ollama model; check upgrade and rollback |
| [QuestMaster Pro](https://github.com/HenricHuntsman/QuestMaster-Pro) | [Lua validation: success](https://github.com/HenricHuntsman/QuestMaster-Pro/actions/runs/37850715181) at `4b3eccec26` | Validate current Retail/Classic clients in-game and test real guide routes |
| [Rabbit Code](https://github.com/HenricHuntsman/rabbit-foundry) | [Rabbit Code tests: success](https://github.com/HenricHuntsman/rabbit-foundry/actions/runs/39040752949) at `b17ca50ad3` | Run a real local-model tool-call session, then verify installer and session resume |
| [RepoForge](https://github.com/HenricHuntsman/repo-manager-ultimate) | [CI: success](https://github.com/HenricHuntsman/repo-manager-ultimate/actions/runs/39042044795) at `d2a2845e30` | Test packaged AppImage/deb and read-only live scans on Ubuntu |

### 2 — Repairable prototypes

| Project | Current evidence | Next recovery milestone |
| --- | --- | --- |
| [AgentFoundry Workspace](https://github.com/HenricHuntsman/AgentFoundry-instantly) | [CI: success](https://github.com/HenricHuntsman/AgentFoundry-instantly/actions/runs/39042068488) at `e7eb7e11db` | Reconcile README claims with tested features; validate Electron packaging and offline behavior |
| [DragonForge Code](https://github.com/HenricHuntsman/dragonforge-code) | [DragonForge local-first labs: success](https://github.com/HenricHuntsman/dragonforge-code/actions/runs/39076259514) at `c43d87efea`; repository release `upstream-v0.0.9` (15 assets) | Validate current lab workflow scope and standalone runtime; treat upstream-* release assets as preserved history, not a new DragonForge stable release. |
| [FORGE Integration Lab — Kimi K2](https://github.com/HenricHuntsman/Kimi-K2) | [Prototype integrity checks: in_progress](https://github.com/HenricHuntsman/Kimi-K2/actions/runs/39079157149) at `ac8ba6e99f`; latest local repair suite: 19 passed | CLI/REST baseline repaired; qualify one real local-model adapter, reconcile remaining prompt/benchmark claims and test packaging. |
| [Lisa AI Journal Prototype](https://github.com/HenricHuntsman/LisaAI-DatingApp) | No sampled default-branch workflow run | Resolve README-reported historical privacy exposure and create a valid Xcode project |
| [Nebula Ultimate](https://github.com/HenricHuntsman/NebulaUltimate) | [CI: success](https://github.com/HenricHuntsman/NebulaUltimate/actions/runs/29656493840) at `dc01a53236` | Launch against local Ollama and test actual UI workflow |

### 3 — Specialist research

| Project | Current evidence | Next recovery milestone |
| --- | --- | --- |
| [Henric N64 Decompiler Lab](https://github.com/HenricHuntsman/LLM4Decompile) | No sampled default-branch workflow run; earlier local maintenance: 32 passed, 2 skipped | Run real local checkpoint and Ghidra/MIPS fixture; verify emulator behavior |
| [mini-AGI / Greenlight](https://github.com/HenricHuntsman/mini-AGI) | [Tests: success](https://github.com/HenricHuntsman/mini-AGI/actions/runs/38505247412) at `3f2dc7a665` | Keep CPU CI separate from RTX 5060 Ti resume, optimizer and router-balance evidence |

### 4 — Planning seeds

| Project | Current evidence | Next recovery milestone |
| --- | --- | --- |
| [Genspark OS Concept](https://github.com/HenricHuntsman/https-github.com-SpidermanTotro-genspark-os) | No sampled default-branch workflow run | Define scope; no bootable OS or installer verified |
| [Trinity Studio — Architecture Seed](https://github.com/HenricHuntsman/Trinity-Studio-Architecture) | No sampled default-branch workflow run | Implement proposed read-only status/doctor CLI as a separately tested change |
| [Trinity Studio Placeholder](https://github.com/HenricHuntsman/AgentFoundry-TrinityCore-Studio) | No sampled default-branch workflow run | Define first executable milestone before adding features |

### 5 — Preserve and recover archives

| Project | Current evidence | Next recovery milestone |
| --- | --- | --- |
| [Nebula Legacy Installation Page](https://github.com/HenricHuntsman/-https-SpidermanTotro.github.io-nebula-ultimate-) | No sampled default-branch workflow run | Historical claims labelled; compare retained material against Nebula source before porting unique features. |
| [QuestMaster Legacy Archives](https://github.com/HenricHuntsman/QuestMasterPro) | No sampled default-branch workflow run | Compare retained experimental archives before porting unique code |

### 6 — Upstream-derived/reference checkouts

| Project | Current evidence | Next recovery milestone |
| --- | --- | --- |
| [4NXCI](https://github.com/HenricHuntsman/4NXCI) | No sampled default-branch workflow run | Reproduce this checkout's build and compare local changes with upstream before assigning a release stage |
| [artcraft](https://github.com/HenricHuntsman/artcraft) | No sampled default-branch workflow run | Reproduce this checkout's build and compare local changes with upstream before assigning a release stage |
| [azeroth-pilot-reloaded](https://github.com/HenricHuntsman/azeroth-pilot-reloaded) | [PR Test Report: success](https://github.com/HenricHuntsman/azeroth-pilot-reloaded/actions/runs/39075226196) at `dc7916b1d5` | Resolve localization workflow failure; verify actual route/runtime checks separately |
| [codex](https://github.com/HenricHuntsman/codex) | No sampled default-branch workflow run | Reproduce this checkout's build and compare local changes with upstream before assigning a release stage |
| [continue](https://github.com/HenricHuntsman/continue) | No sampled default-branch workflow run | Reproduce this checkout's build and compare local changes with upstream before assigning a release stage |
| [gemini-cli](https://github.com/HenricHuntsman/gemini-cli) | No sampled default-branch workflow run | Reproduce this checkout's build and compare local changes with upstream before assigning a release stage |
| [kilocode](https://github.com/HenricHuntsman/kilocode) | No sampled default-branch workflow run | Reproduce this checkout's build and compare local changes with upstream before assigning a release stage |
| [nvm](https://github.com/HenricHuntsman/nvm) | No sampled default-branch workflow run | Reproduce this checkout's build and compare local changes with upstream before assigning a release stage |
| [nxdumptool](https://github.com/HenricHuntsman/nxdumptool) | No sampled default-branch workflow run | Reproduce this checkout's build and compare local changes with upstream before assigning a release stage |
| [rea](https://github.com/HenricHuntsman/rea) | No sampled default-branch workflow run | Reproduce this checkout's build and compare local changes with upstream before assigning a release stage |
| [TrinityCore](https://github.com/HenricHuntsman/TrinityCore) | No sampled default-branch workflow run | Reproduce this checkout's build and compare local changes with upstream before assigning a release stage |
| [Vitruvian](https://github.com/HenricHuntsman/Vitruvian) | No sampled default-branch workflow run | Reproduce this checkout's build and compare local changes with upstream before assigning a release stage |
| [wordcraft](https://github.com/HenricHuntsman/wordcraft) | No sampled default-branch workflow run | Reproduce this checkout's build and compare local changes with upstream before assigning a release stage |

### 7 — Project index

| Project | Current evidence | Next recovery milestone |
| --- | --- | --- |
| [Henric — Project Hub](https://github.com/HenricHuntsman/HenricHuntsman) | No sampled default-branch workflow run | Maintain project status catalogue and distinguish snapshots from current checks |

## First completed recovery increment

Kimi/FORGE: repaired CLI statistics/capability commands and legacy REST documentation/statistics using the actual loader; removed fixed quality/sequel claims; npm test now runs real tests; Node entry points fail explicitly as unimplemented. Rust/C++/Go manifests moved into labelled design material without discarding their contents. Local make test and npm test both passed 19 tests. [Recovery commit](https://github.com/HenricHuntsman/Kimi-K2/commit/ac8ba6e99f496e979a3e96b329c65e3e25117ba2). Real inference is still missing.

## Sequence

1. Keep OpenCode's released development baseline usable; qualify DragonForge separately.
2. Restore the Kimi/Python CLI+REST baseline (completed this increment); next qualify an explicit local-model adapter.
3. Resolve TraceForge's exact failing test boundaries in its private review branch.
4. Qualify Rabbit Code, RepoForge and Book Publish Forge through real Ubuntu workflows and packaging.
5. Validate QuestMaster in-game and mini-AGI/N64 paths with their required local hardware/providers.
6. Review archive contents for unique recoverable code; leave planning seeds in design status until real source exists.

## Scope

Account inventory refreshed; sampled latest default-branch workflow and repository release were queried for every accessible repository. Some results are old, partial or administrative; no-run is unknown rather than failed. No account-wide dependency upgrade, complete source audit or all-project build was performed. Most repositories retain their existing layout; the split is a recovery queue, with the Kimi manifest separation applied physically.

[Project catalogue](PROJECT-CATALOGUE.md) · [Folder/build guide](PROGRAM-MATURITY-2026-10-18.md)
