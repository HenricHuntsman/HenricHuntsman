# Repository audit — 14 October 2026

This is a **metadata and root-README audit**, not a complete build, security or dependency audit.

## Scope and verified totals

- 31 repositories in connected account inventory: **26 public, 5 private**.
- 30 root `README.md` files were readable; one zero-size private repository has no readable README.
- None of the 31 repositories is flagged `archived` by GitHub. Labels such as “archive” in the profile are editorial, not GitHub's archive flag.
- The profile repository `HenricHuntsman/HenricHuntsman` is public and uses `main`.

## Public repository inventory

| Repository | Default branch | Root README | Follow-up |
| --- | --- | --- | --- |
| mini-AGI | main | Yes | Fork; preserve upstream credit, verify tests |
| QuestMasterPro | main | Yes | Legacy content; cross-link to QuestMaster-Pro |
| LisaAI-DatingApp | main | Yes | Review build and dependencies |
| azeroth-pilot-reloaded | dev | Yes | Check upstream attribution and dev branch |
| https-github.com-SpidermanTotro-genspark-os | main | Yes | GitHub reports zero size; review before renaming |
| -https-SpidermanTotro.github.io-nebula-ultimate- | main | Yes | Old URLs and release claims need verification |
| kilocode | main | Yes | Review upstream and local changes |
| 4NXCI | master | Yes | Review upstream/license; preserve branch |
| nxdumptool | rewrite | Yes | Review upstream/license; preserve branch |
| AgentFoundry-instantly | main | Yes | Check installer links and actual CI |
| book-publish-forge | main | Yes | Check tests and packaging |
| TrinityCore | master | Yes | Upstream-derived; verify attribution and build |
| Vitruvian | master | Yes | Review provenance and build |
| rabbit-foundry | main | Yes | Review code/tests and former rabbit-code remote |
| nvm | master | Yes | Upstream-derived; verify attribution |
| Trinity-Studio-Architecture | main | Yes | Very short README; improve documentation |
| QuestMaster-Pro | main | Yes | Active addon; validate Lua packaging |
| repo-manager-ultimate | main | Yes | Historical old-name reference in audit description |
| codex | main | Yes | Review upstream and license |
| Kimi-K2 | main | Yes | Verify build instructions before use |
| NebulaUltimate | main | Yes | Small repository; verify current scope |
| LLM4Decompile | main | Yes | Verify install steps and upstream license |
| gemini-cli | main | Yes | Upstream-derived; verify attribution |
| AgentFoundry-TrinityCore-Studio | main | Yes | Very short README; improve documentation |
| continue | main | Yes | Upstream-derived; verify attribution |
| HenricHuntsman | main | Yes | Live profile README |

The five private repositories were included in the counts and checked for root README availability; their names and contents are intentionally omitted from this public audit document.

## Changes made in this cleanup

- Corrected README links for mini-AGI, AgentFoundry-instantly, Kimi-K2, LLM4Decompile, rabbit-foundry and QuestMasterPro.
- The profile README now links to this audit.
- No repository was renamed, deleted, archived, made public or force-pushed.

## Still requiring attention

1. The **profile repository website metadata** still points to `https://github.com/SpidermanTotro`. The available GitHub connector cannot edit repository metadata. Set the Website field manually to `https://github.com/HenricHuntsman` in the repository's About settings.
2. Review the two public repository names containing `SpidermanTotro`. A repository rename requires separate review of links, releases, branches and integrations.
3. Check old README download instructions in the Nebula legacy repository. Do not assume release assets exist.
4. Verify workflows, tests, licenses, release packaging, branch protection and dependency health before marking projects healthy.
5. Local development hours remain unmeasured until the opt-in timer is run on a machine.

**Do not treat repository size, a README, or an open-issues count as evidence of a passing build.**

## GitHub Actions evidence (checked 14 October 2026)

**Interpretation:** latest recorded workflow run, not necessarily a test/build; `success` for a bot/comment workflow is **not** a passing build. Skipped, cancelled and no-runs are **not** passes. Some workflows may be stale.

| Repository | Latest workflow | Latest conclusion | Date (UTC) |
| --- | --- | --- | --- |
| mini-AGI | Tests | success | 2026-10-14 |
| rabbit-foundry | Rabbit Code tests | success | 2026-10-14 |
| AgentFoundry-instantly | CI | success | 2026-10-14 |
| QuestMaster-Pro | Lua validation | success | 2026-10-08 |
| book-publish-forge | CI | success | 2026-10-09 |
| nxdumptool | Test local content verifier | success | 2026-10-09 |
| repo-manager-ultimate | CI | success | 2026-07-18 |
| NebulaUltimate | CI | success | 2026-07-18 |
| nEW-tEST (private) | CI | success | 2026-07-18 |
| Test-New- (private) | CI | success | 2026-07-18 |
| azeroth-pilot-reloaded | Localization ping | **failure** | 2026-10-13 |
| Trinity-Studio-Architecture | CI/CD Pipeline | **failure** | 2025-12-09 |
| Henric-Programming (private) | CI | **failure** | 2026-10-14 |
| kilocode | Community label | skipped | 2026-10-09 |
| opencode-local (private) | docs-update | skipped | 2026-10-14 |
| gemini-cli | PR comment workflow | cancelled | 2026-04-04 |
| Kimi-K2 | PR comment workflow | success | 2026-04-04 |
| LisaAI-DatingApp | Running Copilot | success | 2025-11-11 |
| TrinityCore | Running Copilot | success | 2025-11-08 |
| AgentFoundry-TrinityCore-Studio | PR comment workflow | success | 2025-12-09 |
| -https-SpidermanTotro.github.io-nebula-ultimate- | PR comment workflow | success | 2025-12-11 |
| QuestMasterPro | None returned | unverified | — |
| https-github.com-SpidermanTotro-genspark-os | None returned | unverified | — |
| 4NXCI | None returned | unverified | — |
| Vitruvian | None returned | unverified | — |
| nvm | None returned | unverified | — |
| codex | None returned | unverified | — |
| continue | None returned | unverified | — |
| LLM4Decompile | None returned | unverified | — |
| luna-levdeling-guide- (private) | None returned | unverified | — |
| HenricHuntsman | None returned | unverified | — |

**Prioritize:** inspect the failing `Henric-Programming` CI and `azeroth-pilot-reloaded` localization workflow, then the stale `Trinity-Studio-Architecture` CI. Validate workflows against their default branches before changing code. No workflows were triggered or rerun during this audit.

## Failure triage — 14 October 2026

- **Henric-Programming:** Latest failed run [38499991318](https://github.com/HenricHuntsman/Henric-Programming/actions/runs/38499991318) is a **pull request** on `chore/devterminal-revival-20261014`, not a failing default-branch run. The `npm audit --omit=dev --audit-level=high` step reported **7 vulnerabilities (5 moderate, 1 high, 1 critical)**, including DOMPurify and proxy-addr dependency advisories. Keep the audit gate; update the dependency tree and lockfile in the PR branch and rerun tests before merging.
- **azeroth-pilot-reloaded:** Latest failed scheduled [localization run 38437440593](https://github.com/HenricHuntsman/azeroth-pilot-reloaded/actions/runs/38437440593) received **HTTP 401 Unauthorized** when exporting CurseForge localization. Review API credentials/permissions and workflow secret wiring. Do not disable the job or commit a secret.
- **Trinity-Studio-Architecture:** Historical failed [PR run 20073440937](https://github.com/HenricHuntsman/Trinity-Studio-Architecture/actions/runs/20073440937) on `copilot/expand-wow-emulator-system`; jobs named Test (20.x) and Security Scan failed, but log retrieval returned HTTP 410. Inspect workflow and branch before proposing a code fix.

**Remediation rule:** Do not remove failing checks, weaken security thresholds, invent passing results, or modify unrelated upstream forks. Fixes require the relevant workflow/configuration and tests.
