# Repository catch-up review — 18 October 2026

The account inventory contains **37 repositories: 31 public and 6 private**. All were checked for metadata, default-branch head, up to five recent default-branch workflow runs, open PRs and the latest published release. Seventeen public fork defaults were compared with their parent default branches. This is an account-wide status and ancestry review, not a line-by-line review, dependency upgrade, full build or runtime test of all projects.

## Changes and discoveries

- Prepared **11 draft upstream-update PRs**. Eight are pinned upstream snapshots of forks with no default-branch-only commits; Vitruvian and TrinityCore candidates retain fork maintenance documentation; Mini-AGI now contains a resolved and CPU-tested integration of five incoming training commits.
- The eight strictly-behind forks are Azeroth Pilot Reloaded (107), Codex (9,566), nvm (172), Gemini CLI (1,213), Continue (77), Kilo (343), Wordcraft (277) and REA (264). Counts are commits at the pinned comparison time, not feature-completion measures.
- Divergent forks at initial inspection: Vitruvian 2 ahead / 876 behind; TrinityCore 2 ahead / 1,542 behind; Mini-AGI 139 ahead / 5 behind. TrinityCore received a subsequent corrective commit, so its initial ahead count is historical.
- Fixed TrinityCore's incompatible expansion-ID insertion on master. Preserved the old Legion Remix proposal as a patch and restored canonical numeric IDs. Targeted C++17 enum/level-function assertions passed; full server build and runtime remain untested.
- Upstream Vitruvian publishes [0.6.2](https://github.com/VitruvianOS/Vitruvian/releases/tag/0.6.2) amd64 and ARM64 ISO/raw images with SHA-256 assets. These are upstream releases, not builds produced or boot-tested by this review. The earlier fork's ARM64 stub does not describe the current upstream source. Updated configure shell syntax passed.
- Kimi's repaired source packaging and **22 tests** passed locally, from an extracted source bundle in the existing environment, and in Python 3.11/3.14 hosted CI. Real inference and OS creation remain unimplemented.
- AgentFoundry and RepoForge's latest default-branch CI passed after the cleanup.
- nxdumptool, 4NXCI and Artcraft default heads match parent default heads. Kimi-K2, LLM4Decompile and original OpenCode are ahead with no incoming parent-default commits at comparison time.

## Current public projects

A successful latest workflow is scoped to that workflow. For example, Azeroth Pilot Reloaded has a successful PR Test Report and separate failing localization jobs; the former is not proof all tests passed. No returned runs means unverified coverage, not a broken project. Draft mergeability is not build or runtime qualification. Update branches do not change the default source tree.

| Repository | Latest sampled workflow | Parent comparison | Source update | Finding / next qualification |
| --- | --- | --- | --- | --- |
| [HenricHuntsman](https://github.com/HenricHuntsman/HenricHuntsman) | No runs returned | Independent lineage / no fork parent | — | Profile/catalogue hub; this report and Linux index are the current account overview. |
| [LisaAI-DatingApp](https://github.com/HenricHuntsman/LisaAI-DatingApp) | No runs returned | Independent lineage / no fork parent | — | Prototype; no default-branch Actions runs or release returned. Qualify an actual iOS build and device workflow. |
| [azeroth-pilot-reloaded](https://github.com/HenricHuntsman/azeroth-pilot-reloaded) | PR Test Report: success | 0 ahead / 107 behind | [Draft #5](https://github.com/HenricHuntsman/azeroth-pilot-reloaded/pull/5) | Upstream reference fork; source/build qualification is separate from ancestry. |
| [TrinityCore](https://github.com/HenricHuntsman/TrinityCore) | No runs returned | 2 ahead / 1542 behind | [Draft #4](https://github.com/HenricHuntsman/TrinityCore/pull/4) | Published canonical expansion-ID fix 4dc5b8c198de9a516b30d64fdc60828258937068. Full server/database build untested. |
| [QuestMaster-Pro](https://github.com/HenricHuntsman/QuestMaster-Pro) | Lua validation: success | Independent lineage / no fork parent | — | Lua validation passed; in-game addon behaviour still needs a matching supported-client test. |
| [book-publish-forge](https://github.com/HenricHuntsman/book-publish-forge) | CI: success | Independent lineage / no fork parent | — | Latest CI passed; qualify installation and full edit/save/export workflow. |
| [QuestMasterPro](https://github.com/HenricHuntsman/QuestMasterPro) | No runs returned | Independent lineage / no fork parent | — | Historical addon collection; retain unique archives and keep separate from QuestMaster-Pro. |
| [Kimi-K2](https://github.com/HenricHuntsman/Kimi-K2) | Prototype integrity checks: success | 36 ahead / 0 behind | — | 22 tests passed locally, from extracted sources and in Python 3.11/3.14 CI. Demo, not model inference or OS. |
| [-https-SpidermanTotro.github.io-nebula-ultimate-](https://github.com/HenricHuntsman/-https-SpidermanTotro.github.io-nebula-ultimate-) | No runs returned | Independent lineage / no fork parent | — | Historical web snapshot; keep separate from NebulaUltimate. |
| [NebulaUltimate](https://github.com/HenricHuntsman/NebulaUltimate) | CI: success | Independent lineage / no fork parent | — | Latest CI passed; historical Pylint failure is a separate run, not proof the entire app is qualified. |
| [AgentFoundry-instantly](https://github.com/HenricHuntsman/AgentFoundry-instantly) | CI: success | Independent lineage / no fork parent | — | Latest cleanup/instruction CI passed. 56 reports archived; Linux installer workflow remains unqualified. |
| [https-github.com-SpidermanTotro-genspark-os](https://github.com/HenricHuntsman/https-github.com-SpidermanTotro-genspark-os) | No runs returned | Independent lineage / no fork parent | — | Concept only; requirements and image/boot/install milestones remain open. |
| [AgentFoundry-TrinityCore-Studio](https://github.com/HenricHuntsman/AgentFoundry-TrinityCore-Studio) | No runs returned | Independent lineage / no fork parent | — | Planning/integration seed; no default-branch CI/release returned. |
| [Trinity-Studio-Architecture](https://github.com/HenricHuntsman/Trinity-Studio-Architecture) | No runs returned | Independent lineage / no fork parent | — | Architecture planning; no runnable product qualification established. |
| [repo-manager-ultimate](https://github.com/HenricHuntsman/repo-manager-ultimate) | CI: success | Independent lineage / no fork parent | — | Latest CI passed; installation and desktop package smoke tests remain open. |
| [codex](https://github.com/HenricHuntsman/codex) | No runs returned | 0 ahead / 9566 behind | [Draft #2](https://github.com/HenricHuntsman/codex/pull/2) | Upstream reference fork; source/build qualification is separate from ancestry. |
| [nvm](https://github.com/HenricHuntsman/nvm) | No runs returned | 0 ahead / 172 behind | [Draft #2](https://github.com/HenricHuntsman/nvm/pull/2) | Upstream reference fork; source/build qualification is separate from ancestry. |
| [gemini-cli](https://github.com/HenricHuntsman/gemini-cli) | No runs returned | 0 ahead / 1213 behind | [Draft #3](https://github.com/HenricHuntsman/gemini-cli/pull/3) | Upstream reference fork; source/build qualification is separate from ancestry. |
| [Vitruvian](https://github.com/HenricHuntsman/Vitruvian) | No runs returned | 2 ahead / 876 behind | [Draft #2](https://github.com/HenricHuntsman/Vitruvian/pull/2) | Upstream 0.6.2 has amd64/arm64 images and checksums. Own fork has no release; image boot remains untested. |
| [continue](https://github.com/HenricHuntsman/continue) | No runs returned | 0 ahead / 77 behind | [Draft #2](https://github.com/HenricHuntsman/continue/pull/2) | Upstream reference fork; source/build qualification is separate from ancestry. |
| [mini-AGI](https://github.com/HenricHuntsman/mini-AGI) | Tests: success | 139 ahead / 5 behind | [Draft #43](https://github.com/HenricHuntsman/mini-AGI/pull/43) | Default CPU baseline CI passed. Resolved upstream candidate: 180 CPU tests ran, one optional lifecycle skipped; strengthened pruning regression passed. GPU and production checkpoint qualification remain open. |
| [LLM4Decompile](https://github.com/HenricHuntsman/LLM4Decompile) | No runs returned | 6 ahead / 0 behind | — | Research, not a qualified decompiler product. Earlier lightweight checks passed; no live GPU/MIPS qualification. |
| [rabbit-foundry](https://github.com/HenricHuntsman/rabbit-foundry) | Rabbit Code tests: success | Independent lineage / no fork parent | — | Latest tests passed; qualify the complete local model/tool workflow and installation. |
| [nxdumptool](https://github.com/HenricHuntsman/nxdumptool) | No runs returned | 0 ahead / 0 behind | — | Upstream reference fork; source/build qualification is separate from ancestry. |
| [kilocode](https://github.com/HenricHuntsman/kilocode) | No runs returned | 0 ahead / 343 behind | [Draft #5](https://github.com/HenricHuntsman/kilocode/pull/5) | Upstream reference fork; source/build qualification is separate from ancestry. |
| [4NXCI](https://github.com/HenricHuntsman/4NXCI) | No runs returned | 0 ahead / 0 behind | — | Upstream reference fork; source/build qualification is separate from ancestry. |
| [artcraft](https://github.com/HenricHuntsman/artcraft) | No runs returned | 0 ahead / 0 behind | — | Upstream reference fork; source/build qualification is separate from ancestry. |
| [wordcraft](https://github.com/HenricHuntsman/wordcraft) | No runs returned | 0 ahead / 277 behind | [Draft #2](https://github.com/HenricHuntsman/wordcraft/pull/2) | Upstream reference fork; source/build qualification is separate from ancestry. |
| [rea](https://github.com/HenricHuntsman/rea) | No runs returned | 0 ahead / 264 behind | [Draft #2](https://github.com/HenricHuntsman/rea/pull/2) | Upstream reference fork; source/build qualification is separate from ancestry. |
| [opencode](https://github.com/HenricHuntsman/opencode) | ci: success | 11 ahead / 0 behind | — | Original Go lineage: CI/build passed; published development release v0.0.56. |
| [dragonforge-code](https://github.com/HenricHuntsman/dragonforge-code) | DragonForge local-first labs: success | Independent lineage / no fork parent | — | Latest labs/CI/build passed. upstream-v0.0.9 is a historical upstream mirror, not a newly qualified stable fork release. |

## Remaining gates

The source-update PRs are not merged. Mini-AGI's conflicts were resolved; 180 CPU tests ran with one optional lifecycle skipped, followed by two passing focused expert-state regression tests. The candidate's uploaded tree matches the tested tree. GPU, real optional lifecycle and production checkpoint compatibility remain unverified. NVM and Kilo checks were still queued/running at inspection. Other PRs also require relevant builds and runtime checks before qualification. Existing feature, design and branding PRs were preserved; this review does not attest to human author readiness. No project is newly declared RC or RTM.

For the earlier recovery grouping see [recovery board](RECOVERY-BOARD-2026-10-18.md), and for Linux project folders see [Linux index](linux/README.md). The companion JSON is a public-only machine-readable snapshot. Private project names and findings are excluded from this public report.

NVM follow-up: incoming core scripts passed Bash/POSIX syntax checks, and source-only version smoke returned 0.40.8. No Node installation or profile modification was performed. NVM's complete hosted matrix remains separate.
