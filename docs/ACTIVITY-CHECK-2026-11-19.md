# Public repository activity — 19 November 2026

Inventory checked on GitHub on 19 November (Australia/Melbourne). The account has **41 public repositories**, up from 35 in the [2 November snapshot](ACTIVITY-CHECK-2026-11-02.md). See the [project catalogue](PROJECT-CATALOGUE.md) for the full list. The six additions are newly catalogued, and their release maturity has yet to be assessed.

## Public activity sampled

| Repository | Recorded evidence |
| --- | --- |
| [Stela](https://github.com/HenricHuntsman/Stela/commit/dc33db43f057d8563ce976a38afdd35de999ea22) | 18 November commit extends the Bluetooth hardware model’s scan-start responses. Physical hardware and boot validation were outside this review. |
| [TotK PC recompilation reference](https://github.com/HenricHuntsman/totk-pc-recomp/commit/101132a6c8d9654c88838c57b934b4b79636ea90) | 5 November Melbourne-time commit updates the Linux release build after a source-builder argument change. This review sampled the commit, with runtime qualification pending. |
| [Sapphire Blue AI](https://github.com/HenricHuntsman/sapphire/commit/663a944b0e557f7998a0f2ee9b34bf4a2352e872) | 8 November Melbourne-time commit adds funding metadata. The checkout’s self-hosted voice and AI workflows remain unassessed here. |
| [DragonForge Code](https://github.com/HenricHuntsman/dragonforge-code/commit/19145d1a246637412ecd6a388e4b003367bae339) | Default-branch documentation describes an Ubuntu Bash launcher for the existing Go-based OpenCode Revival engine, with selectable workspaces and optional local Ollama. |

## Pull request evidence

| Review | Captured head | GitHub Actions results |
| --- | --- | --- |
| [XenonRecomp PR #1](https://github.com/HenricHuntsman/XenonRecomp/pull/1) | `1160c93730dee2a0b406984325c74b055edb7fd9` | [Synthetic NSO0 header audit passed](https://github.com/HenricHuntsman/XenonRecomp/actions/runs/41707922059). The workflow result covers synthetic metadata checks. |
| [MacNativeGames PR #2](https://github.com/HenricHuntsman/MacNativeGames/pull/2) | `f214b7437c31d81faa89c4b34a34113b6131d6af` | [Linux foundation passed](https://github.com/HenricHuntsman/MacNativeGames/actions/runs/41712238125), the [NativeAOT shader service protocol passed](https://github.com/HenricHuntsman/MacNativeGames/actions/runs/41712238095), and [source regressions failed](https://github.com/HenricHuntsman/MacNativeGames/actions/runs/41712238103). |
| [MacNativeGames PR #3](https://github.com/HenricHuntsman/MacNativeGames/pull/3) | `92e10169a74a0830637bc2f92d767107b0b849fa` | The [shader protocol passed](https://github.com/HenricHuntsman/MacNativeGames/actions/runs/43572218006), and [source regressions failed](https://github.com/HenricHuntsman/MacNativeGames/actions/runs/43572218009). |

The three PRs were open at review time. Investigating the MacNativeGames source-regression failure is the next pre-merge check. The workflow-level XenonRecomp result was checked without independently counting individual test cases. Existing maturity labels retain their dated assessments.
