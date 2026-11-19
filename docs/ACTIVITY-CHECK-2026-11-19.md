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

XenonRecomp PR #1 [merged into main](https://github.com/HenricHuntsman/XenonRecomp/commit/968df9ce47a45c18b79e7fa8376889745c550aa9). The Actions job log records **nine passing synthetic tests**.

MacNativeGames PRs #2 and #3 remain open. The PR #3 source regression log shows four settings-panel height assertion failures at `settings_panel_probe.m:829`, across the compact and corners layouts with both override settings. The Linux shader protocol checks passed. The next check is to reproduce the macOS layout failure on the base branch.

## Account-wide catch-up

The connected inventory review covered 51 owned repositories and 114 open PRs, including 70 drafts. The catch-up merged 22 PRs, including 21 documentation-only dragon branding updates and the XenonRecomp audit. Repository-specific release assessments retain their recorded dates.

## Follow-up on 19 November

- Six more branding-only PRs merged in [opencode](https://github.com/HenricHuntsman/opencode/pull/14), [repo-manager-ultimate](https://github.com/HenricHuntsman/repo-manager-ultimate/pull/10), [Kimi-K2](https://github.com/HenricHuntsman/Kimi-K2/pull/47), [TrinityCore](https://github.com/HenricHuntsman/TrinityCore/pull/3), [Vitruvian](https://github.com/HenricHuntsman/Vitruvian/pull/1), [https-github.com-SpidermanTotro-genspark-os](https://github.com/HenricHuntsman/https-github.com-SpidermanTotro-genspark-os/pull/1). The account-wide total rose to 28 merges.
- [MacNativeGames PR #4](https://github.com/HenricHuntsman/MacNativeGames/pull/4) adds a Linux NativeAOT Actions gate on current `main`. It runs the existing test for malformed-request recovery, subsequent synthetic shader translation, and SPIR-V validation. [The new workflow run](https://github.com/HenricHuntsman/MacNativeGames/actions/runs/44470409406) was queued at publication.
- Greenlight PR #55 passed hosted [Python 3.11 and 3.14 checks](https://github.com/HenricHuntsman/mini-AGI/actions/runs/43532140840). It remains a draft pending GPU validation and further integration review.

## MacNativeGames CI follow-up

- [PR #4](https://github.com/HenricHuntsman/MacNativeGames/pull/4) passed [Linux NativeAOT shader protocol and SPIR-V validation](https://github.com/HenricHuntsman/MacNativeGames/actions/runs/44470409406). Its [macOS source regression run](https://github.com/HenricHuntsman/MacNativeGames/actions/runs/44470409801) repeated the four panel height failures even though the PR only adds a Linux workflow.
- [PR #5](https://github.com/HenricHuntsman/MacNativeGames/pull/5) updates the macOS probe to check rendered row geometry in both regular and compact layouts. Hosted macOS verification is pending.

## Upstream refresh and settings panel follow-up

Four existing draft PRs were fast-forwarded to verified upstream revisions: [Azeroth Pilot Reloaded](https://github.com/HenricHuntsman/azeroth-pilot-reloaded/pull/5), [nvm](https://github.com/HenricHuntsman/nvm/pull/2), [Gemini CLI](https://github.com/HenricHuntsman/gemini-cli/pull/3), and [Codex](https://github.com/HenricHuntsman/codex/pull/2). Continue's review branch already matched upstream. TrinityCore's candidate and the Greenlight default branch have diverged from upstream and require integration review.

[MacNativeGames PR #5](https://github.com/HenricHuntsman/MacNativeGames/pull/5) now caps compact row height at the regular height. The earlier CI run showed that reducing the gap could otherwise make compact rows taller than regular rows. [CI for the corrected revision](https://github.com/HenricHuntsman/MacNativeGames/actions/runs/44473369745) was still running at publication.

## Further upstream refresh and macOS merge

- [artcraft draft #2](https://github.com/HenricHuntsman/artcraft/pull/2) fast-forwarded by 31 upstream commits to `a6d52df45e55`.
- [wordcraft draft #2](https://github.com/HenricHuntsman/wordcraft/pull/2) fast-forwarded by 1077 upstream commits to `6ef13b2cc8a6`.
- [kilocode draft #5](https://github.com/HenricHuntsman/kilocode/pull/5) fast-forwarded by 403 upstream commits to `00a5d30cf76f`.
- [skorpion_os draft #1](https://github.com/HenricHuntsman/skorpion_os/pull/1) fast-forwarded by 10 upstream commits to `a013a223d7d4`.
- [rea draft #5](https://github.com/HenricHuntsman/rea/pull/5) fast-forwarded by 2164 upstream commits to `dd1bb43db3d4`.
- nxdumptool's review branch already matched upstream. Vitruvian's candidate and upstream both contain unique commits, so integration review remains open.
- [MacNativeGames #5](https://github.com/HenricHuntsman/MacNativeGames/pull/5) merged after the [macOS source regressions passed](https://github.com/HenricHuntsman/MacNativeGames/actions/runs/44473369745). [PR #4](https://github.com/HenricHuntsman/MacNativeGames/pull/4) now also runs Linux shader verification on matching pushes to main and has fresh CI pending.
