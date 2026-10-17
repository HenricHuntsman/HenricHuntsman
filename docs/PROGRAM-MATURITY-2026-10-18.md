# Program maturity and catch-up catalogue

Checked 18 October 2026 (Australia/Melbourne). Covers all **31 public repositories** in the connected account. Six private projects are assessed only in the personal catch-up report.

## How to read the labels

These are conservative review assessments, not official maintainer version declarations.

| Stage | Meaning |
| --- | --- |
| Planning / prototype | Design or partial components; no complete verified user workflow |
| Alpha | Implemented code exists; core behavior, integrations or packaging still need qualification |
| Beta candidate | Enough implementation and automated checks to consider controlled user testing; beta readiness still needs runtime confirmation |
| Release candidate (RC) | Frozen feature scope, passing required checks, tested packages and no known release blockers |
| RTM / stable | Released, qualified artifact with documented support, install/upgrade/rollback and acceptance evidence |
| Released development build | A downloadable version exists; release publication alone does not establish stable or RTM quality |
| Upstream-derived / unqualified | Upstream product maturity is separate from this account's checkout and local changes |

**No independently maintained project is qualified as RC or RTM by this review.** No completion percentages are assigned because agreed feature/acceptance checklists are absent. A 1.x package version, green CI, file count or large README is not a completion percentage.

## Sorted by maturity, then alphabetically

### Released development build

| Project | Assessment | Build / validation evidence | Next milestone |
| --- | --- | --- | --- |
| [opencode](https://github.com/HenricHuntsman/opencode) | Released development build; Go terminal assistant | [ci: success](https://github.com/HenricHuntsman/opencode/actions/runs/39037592465) at `9c101864c3`; build: success; v0.0.56, 9 release assets | Smoke-test v0.0.56 on Ubuntu with an installed Ollama model; check upgrade and rollback |

### Beta candidate

| Project | Assessment | Build / validation evidence | Next milestone |
| --- | --- | --- | --- |
| [book-publish-forge](https://github.com/HenricHuntsman/book-publish-forge) | Beta candidate; Tkinter desktop; alpha React prototype | [CI: success](https://github.com/HenricHuntsman/book-publish-forge/actions/runs/37878180468) at `ae9900a4f4` | Test real manuscript import/save/export and local-model failure handling |
| [QuestMaster-Pro](https://github.com/HenricHuntsman/QuestMaster-Pro) | Beta candidate; Lua addon | [Lua validation: success](https://github.com/HenricHuntsman/QuestMaster-Pro/actions/runs/37850715181) at `4b3eccec26` | Validate current Retail/Classic clients in-game and test real guide routes |
| [rabbit-foundry](https://github.com/HenricHuntsman/rabbit-foundry) | Beta candidate; Python CLI/gateway; experimental browser UI | [Rabbit Code tests: success](https://github.com/HenricHuntsman/rabbit-foundry/actions/runs/39040752949) at `b17ca50ad3` | Run a real local-model tool-call session, then verify installer and session resume |
| [repo-manager-ultimate](https://github.com/HenricHuntsman/repo-manager-ultimate) | Beta candidate; React/TypeScript dashboard + Electron | [CI: success](https://github.com/HenricHuntsman/repo-manager-ultimate/actions/runs/29656496367) at `b1aa14a871` | Test packaged AppImage/deb and read-only live scans on Ubuntu |

### Alpha

| Project | Assessment | Build / validation evidence | Next milestone |
| --- | --- | --- | --- |
| [AgentFoundry-instantly](https://github.com/HenricHuntsman/AgentFoundry-instantly) | Alpha; JavaScript/Vite + Node/Electron | [CI: success](https://github.com/HenricHuntsman/AgentFoundry-instantly/actions/runs/38505252302) at `160fc4c37f` | Reconcile README claims with tested features; validate Electron packaging and offline behavior |
| [dragonforge-code](https://github.com/HenricHuntsman/dragonforge-code) | Alpha; Go coding-agent migration | [build: in_progress](https://github.com/HenricHuntsman/dragonforge-code/actions/runs/39040965764) at `96cada506a`; ci: success | Finish branding/install/release migration and test standalone binary |
| [NebulaUltimate](https://github.com/HenricHuntsman/NebulaUltimate) | Alpha; Python skill-loader prototype | [CI: success](https://github.com/HenricHuntsman/NebulaUltimate/actions/runs/29656493840) at `dc01a53236` | Launch against local Ollama and test actual UI workflow |

### Alpha / research

| Project | Assessment | Build / validation evidence | Next milestone |
| --- | --- | --- | --- |
| [LLM4Decompile](https://github.com/HenricHuntsman/LLM4Decompile) | Alpha / research; Python/Ghidra/MIPS lab | No default-branch Actions runs returned in the sampled query | Run real local checkpoint and Ghidra/MIPS fixture; verify emulator behavior |
| [mini-AGI](https://github.com/HenricHuntsman/mini-AGI) | Alpha / research; Python/PyTorch training and tools | [Tests: success](https://github.com/HenricHuntsman/mini-AGI/actions/runs/38505247412) at `3f2dc7a665` | Keep CPU CI separate from RTX 5060 Ti resume, optimizer and router-balance evidence |

### Alpha / unverified integration

| Project | Assessment | Build / validation evidence | Next milestone |
| --- | --- | --- | --- |
| [Kimi-K2](https://github.com/HenricHuntsman/Kimi-K2) | Alpha / unverified integration; Python FORGE integration over upstream model reference | No default-branch Actions runs returned in the sampled query | Verify implemented tool paths and benchmarks; historical completion claims are not established |

### Prototype

| Project | Assessment | Build / validation evidence | Next milestone |
| --- | --- | --- | --- |
| [LisaAI-DatingApp](https://github.com/HenricHuntsman/LisaAI-DatingApp) | Prototype; SwiftUI source components | No default-branch Actions runs returned in the sampled query | Resolve README-reported historical privacy exposure and create a valid Xcode project |

### Planning

| Project | Assessment | Build / validation evidence | Next milestone |
| --- | --- | --- | --- |
| [AgentFoundry-TrinityCore-Studio](https://github.com/HenricHuntsman/AgentFoundry-TrinityCore-Studio) | Planning; README placeholder | No default-branch Actions runs returned in the sampled query | Define first executable milestone before adding features |
| [https-github.com-SpidermanTotro-genspark-os](https://github.com/HenricHuntsman/https-github.com-SpidermanTotro-genspark-os) | Planning; README only | No default-branch Actions runs returned in the sampled query | Define scope; no bootable OS or installer verified |
| [Trinity-Studio-Architecture](https://github.com/HenricHuntsman/Trinity-Studio-Architecture) | Planning; Architecture/instructions seed | No default-branch Actions runs returned in the sampled query | Implement proposed read-only status/doctor CLI as a separately tested change |

### Legacy archive

| Project | Assessment | Build / validation evidence | Next milestone |
| --- | --- | --- | --- |
| [-https-SpidermanTotro.github.io-nebula-ultimate-](https://github.com/HenricHuntsman/-https-SpidermanTotro.github.io-nebula-ultimate-) | Legacy archive; Historical install page | No default-branch Actions runs returned in the sampled query | Preserve old page; replace misleading download and 100%-functional claims |
| [QuestMasterPro](https://github.com/HenricHuntsman/QuestMasterPro) | Legacy archive; Historical addon bundles | No default-branch Actions runs returned in the sampled query | Compare retained experimental archives before porting unique code |

### Documentation

| Project | Assessment | Build / validation evidence | Next milestone |
| --- | --- | --- | --- |
| [HenricHuntsman](https://github.com/HenricHuntsman/HenricHuntsman) | Documentation; Profile, audit and preserved prototypes | No default-branch Actions runs returned in the sampled query | Maintain project status catalogue and distinguish snapshots from current checks |

### Upstream-derived / unqualified

| Project | Assessment | Build / validation evidence | Next milestone |
| --- | --- | --- | --- |
| [4NXCI](https://github.com/HenricHuntsman/4NXCI) | Upstream-derived / unqualified; Existing source/reference project | No default-branch Actions runs returned in the sampled query | Reproduce this checkout's build and compare local changes with upstream before assigning a release stage |
| [artcraft](https://github.com/HenricHuntsman/artcraft) | Upstream-derived / unqualified; Existing source/reference project | No default-branch Actions runs returned in the sampled query | Reproduce this checkout's build and compare local changes with upstream before assigning a release stage |
| [azeroth-pilot-reloaded](https://github.com/HenricHuntsman/azeroth-pilot-reloaded) | Upstream-derived / unqualified; Existing source/reference project | [Localization ping: failure](https://github.com/HenricHuntsman/azeroth-pilot-reloaded/actions/runs/39036410357) at `dc7916b1d5`; Update TOC Interface versions: success | Resolve localization workflow failure; verify actual route/runtime checks separately |
| [codex](https://github.com/HenricHuntsman/codex) | Upstream-derived / unqualified; Existing source/reference project | No default-branch Actions runs returned in the sampled query | Reproduce this checkout's build and compare local changes with upstream before assigning a release stage |
| [continue](https://github.com/HenricHuntsman/continue) | Upstream-derived / unqualified; Existing source/reference project | No default-branch Actions runs returned in the sampled query | Reproduce this checkout's build and compare local changes with upstream before assigning a release stage |
| [gemini-cli](https://github.com/HenricHuntsman/gemini-cli) | Upstream-derived / unqualified; Existing source/reference project | No default-branch Actions runs returned in the sampled query | Reproduce this checkout's build and compare local changes with upstream before assigning a release stage |
| [kilocode](https://github.com/HenricHuntsman/kilocode) | Upstream-derived / unqualified; Existing source/reference project | No default-branch Actions runs returned in the sampled query | Reproduce this checkout's build and compare local changes with upstream before assigning a release stage |
| [nvm](https://github.com/HenricHuntsman/nvm) | Upstream-derived / unqualified; Existing source/reference project | No default-branch Actions runs returned in the sampled query | Reproduce this checkout's build and compare local changes with upstream before assigning a release stage |
| [nxdumptool](https://github.com/HenricHuntsman/nxdumptool) | Upstream-derived / unqualified; Experimental upstream rewrite source | No default-branch Actions runs returned in the sampled query | Reproduce this checkout's build and compare local changes with upstream before assigning a release stage |
| [rea](https://github.com/HenricHuntsman/rea) | Upstream-derived / unqualified; Existing source/reference project | No default-branch Actions runs returned in the sampled query | Reproduce this checkout's build and compare local changes with upstream before assigning a release stage |
| [TrinityCore](https://github.com/HenricHuntsman/TrinityCore) | Upstream-derived / unqualified; Existing source/reference project | No default-branch Actions runs returned in the sampled query | Reproduce this checkout's build and compare local changes with upstream before assigning a release stage |
| [Vitruvian](https://github.com/HenricHuntsman/Vitruvian) | Upstream-derived / unqualified; Existing source/reference project | No default-branch Actions runs returned in the sampled query | Reproduce this checkout's build and compare local changes with upstream before assigning a release stage |
| [wordcraft](https://github.com/HenricHuntsman/wordcraft) | Upstream-derived / unqualified; Existing source/reference project | No default-branch Actions runs returned in the sampled query | Reproduce this checkout's build and compare local changes with upstream before assigning a release stage |

## Sort by build evidence

| Group | Projects | What the evidence establishes |
| --- | --- | --- |
| Published artifact plus passing default-branch CI/build | OpenCode | v0.0.56 has nine assets; main build/test runs passed at 9c101864c3. Clean-machine/local-model acceptance still pending |
| Passing current-head checks observed | AgentFoundry Instantly, Book Publish Forge, mini-AGI, Nebula Ultimate, QuestMaster Pro, Rabbit Code, RepoForge | Compared sampled run SHAs with branch heads. Check scopes differ; not all jobs build installers or exercise live models |
| Migration with mixed completion | DragonForge Code | Main CI passed; main build was in progress at inspection |
| Workflow blocker | Azeroth Pilot Reloaded | Localization ping failed; TOC-update automation passed. Neither establishes route correctness |
| No sampled default-branch Actions result | Remaining public checkouts | Unknown build status; this does not mean broken or unbuildable |

Rabbit Code's passing workflow includes Python 3.11 regression checks, Python 3.11/3.14 lightweight checks and a Fedora 44 lightweight lane. mini-AGI's workflow uses **CPU PyTorch on Python 3.11/3.14**; it does not validate CUDA training or local checkpoint resume. QuestMaster checks Lua syntax, TOC files, startup simulation and lint; it is not a real WoW client session. Book Publish Forge's default-branch CI compiles Python and runs tests; the separate web workflow must be read independently. RepoForge's CI builds/tests the dashboard, while packaging is a separate manually dispatched workflow. AgentFoundry's CI checks syntax, guarded-tool tests, Vite build and readiness-helper behavior; it does not qualify all historical feature claims.

## Catch-up order

1. **Use the released baseline:** test OpenCode v0.0.56 with your existing Ollama model and record terminal launch, one safe tool call, persistence and exit.
2. **Finish the active migration:** qualify DragonForge separately before replacing the working OpenCode installation. Do not merge distinct projects solely to reduce repository count.
3. **Qualify daily-use tools:** Rabbit Code, RepoForge and the Book Publish Forge desktop app need actual Ubuntu sessions and package/export checks.
4. **Validate specialist work:** QuestMaster needs in-game coverage; mini-AGI needs measured GPU/checkpoint-resume evidence; the N64 lab needs Ghidra/model/emulator evidence.
5. **Reconcile older claims:** AgentFoundry and Kimi integration documentation contain broad historical completion claims requiring code-level verification.
6. **Keep planning and archives distinct:** Trinity seeds and the Genspark README are not finished applications. Preserve unique archive code before deleting or porting it.

## File and folder navigation

Paths below are navigational snapshots from the file inventory, not claims every file was edited. Existing implementation paths are preserved. Only verified cleanup and documentation changes have been applied.

| Repository | Main source / project locations |
| --- | --- |
| -https-SpidermanTotro.github.io-nebula-ultimate- | `README.md` / root files; see repository listing |
| 4NXCI | `4nxci-GUI/`, `mbedtls/`, `patches/` |
| AgentFoundry-instantly | `ai-suite-pro-mobile/`, `data/`, `forge-spark-mvp/`, `genspark-2.0/`, `genspark-ai-developer/`, `github-2.0/`, `public/`, `scripts/`, `server/`, `src/`, `test/`, `tools/`, `tv-radio-streaming/`, `unrestricted-suite/` |
| AgentFoundry-TrinityCore-Studio | `README.md` / root files; see repository listing |
| artcraft | `_database/`, `_docs/`, `artcraft-native/`, `crates/`, `docs/`, `frontend/`, `script/`, `test_data/` |
| azeroth-pilot-reloaded | `APR-Core/`, `Routes/`, `readme/`, `tests/`, `tools/` |
| book-publish-forge | `app/`, `docs/`, `packaging/`, `tests/`, `web/` |
| codex | `codex-cli/`, `codex-rs/`, `docs/`, `patches/`, `scripts/`, `sdk/`, `shell-tool-mcp/`, `third_party/` |
| continue | `actions/`, `binary/`, `core/`, `docs/`, `eval/`, `extensions/`, `gui/`, `manual-testing-sandbox/`, `media/`, `packages/`, `scripts/`, `skills/`, `sync/` |
| dragonforge-code | `cmd/`, `docs/`, `internal/`, `scripts/` |
| gemini-cli | `docs/`, `evals/`, `integration-tests/`, `packages/`, `schemas/`, `scripts/`, `sea/`, `third_party/` |
| HenricHuntsman | `README.md`, `assets/`, `docs/`, `tools/dev-hours/`, `archive/` |
| https-github.com-SpidermanTotro-genspark-os | `README.md` / root files; see repository listing |
| kilocode | `artifacts/`, `bin/`, `docs/`, `github/`, `nix/`, `packages/`, `patches/`, `perf/`, `plans/`, `script/`, `specs/`, `translations/` |
| Kimi-K2 | `__pycache__/`, `dist/`, `docs/`, `figures/`, `static/`, `templates/` |
| LisaAI-DatingApp | `LisaDatingApp/` |
| LLM4Decompile | `decompile-bench/`, `docs/`, `evaluation/`, `ghidra/`, `legacy-test/`, `n64/`, `samples/`, `scripts/`, `sk2decompile/`, `tests/`, `train/` |
| mini-AGI | `android/`, `assets/`, `companion/`, `corpora/`, `docs/`, `iphone/`, `minagi/`, `mini_agent/`, `mobile/`, `replication/`, `runs/`, `tests/`, `tools/` |
| NebulaUltimate | `ai_agents/`, `docs/`, `nebula/`, `tests/` |
| nvm | `test/` |
| nxdumptool | `code_templates/`, `host/`, `include/`, `libs/`, `romfs/`, `source/` |
| opencode | `cmd/`, `docs/`, `internal/`, `scripts/` |
| QuestMaster-Pro | `Core/`, `Data/`, `EXERCISES/`, `Guides/`, `Textures/`, `UI/`, `assets/`, `scripts/`, `templates/`, `tests/` |
| QuestMasterPro | `docs/` |
| rabbit-foundry | `configs/`, `docs/`, `scripts/`, `src/`, `tests/` |
| rea | `bridge/`, `docs/`, `experiments/`, `licenses/`, `native/`, `scripts/`, `src/`, `tests/`, `third_party/`, `website/` |
| repo-manager-ultimate | `electron/`, `src/` |
| Trinity-Studio-Architecture | `README.md` / root files; see repository listing |
| TrinityCore | `src/`, `sql/`, `dep/`, `cmake/`, `contrib/`, `tests/` |
| Vitruvian | `build/`, `data/`, `headers/`, `src/` |
| wordcraft | `apps/`, `assets/`, `contributors/`, `crates/`, `docs/`, `packaging/`, `xtask/` |

## Scope and evidence limits

Reviewed default-branch README excerpts, sampled repository release collections, sampled default-branch workflow runs, selected workflow definitions and earlier complete file listings. No local application builds were run in this assessment. Release collections queried belong to these repositories; upstream release pages and registries were not substituted. Empty release results do not imply an upstream project has no releases. Private project names and findings are deliberately excluded.

[Cleanup audit](REPOSITORY-AUDIT-2026-10-18.md) · [Bundle inspection](../archive/BUNDLE-INSPECTION-2026-10-18.md)

## Executed maintenance follow-up

The N64/LLM4Decompile maintenance suite was run against checkout `9ca9a1aa6e`: 32 tests passed, 2 tensor tests skipped, with no static-check errors. The synthetic prompt dry run and five-case GCC host reference harness also passed. [Full verification record](https://github.com/HenricHuntsman/LLM4Decompile/blob/main/docs/MAINTENANCE-VERIFICATION-2026-10-18.md). This supersedes the initial no-local-checks statement for this project's lightweight maintenance paths only; model inference, CUDA, real Ghidra/MIPS and N64 execution remain unverified.

APR's sampled localization job failed with CurseForge HTTP 401 Unauthorized. That is an external authentication blocker; it does not establish that the addon itself fails to build or run.
