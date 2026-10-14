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

Public repository workflow results were reviewed. A scheduled localization check reported an authentication failure; a historical Trinity Studio pull-request workflow also reported failures. These do not establish that all other projects are fully tested.

Five private repositories were reviewed separately. Their identities, workflow links and branch details are not included in this public audit.

## Next validation steps

- Verify authorization for the public localization workflow.
- Review historical pull-request checks before adopting unverified changes.
- Maintain dependency and security findings within the relevant repository's own documentation.
- Do not report an unrun build or security scan as passing.
