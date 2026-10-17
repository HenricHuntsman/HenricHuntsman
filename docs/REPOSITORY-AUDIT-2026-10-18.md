# Repository audit — 18 October 2026

Checked using the connected GitHub account; date is Australia/Melbourne.

## Scope

37 repositories are accessible: **31 public, 6 private**. Recursive default-branch file listings were obtained for 36 repositories without truncation. TrinityCore was subsequently enumerated in smaller subtrees, including each historical SQL version, without truncation. File-structure inventory now covers all 37 accessible repositories. Private names and contents are omitted here.

This is an account inventory and file-structure review, plus a content review and cleanup of the profile repository. It is not a complete source-code, dependency, security or build audit of every project. File counts below are the pre-cleanup snapshot. Presence of README or workflow files does not establish that tests pass.

## Public inventory

| Repository | Default branch | Tracked files | Root README present |
| --- | --- | ---: | --- |
| [-https-SpidermanTotro.github.io-nebula-ultimate-](https://github.com/HenricHuntsman/-https-SpidermanTotro.github.io-nebula-ultimate-) | `main` | 2 | Yes |
| [4NXCI](https://github.com/HenricHuntsman/4NXCI) | `master` | 919 | Yes |
| [AgentFoundry-instantly](https://github.com/HenricHuntsman/AgentFoundry-instantly) | `main` | 247 | Yes |
| [AgentFoundry-TrinityCore-Studio](https://github.com/HenricHuntsman/AgentFoundry-TrinityCore-Studio) | `main` | 1 | Yes |
| [artcraft](https://github.com/HenricHuntsman/artcraft) | `main` | 5821 | Yes |
| [azeroth-pilot-reloaded](https://github.com/HenricHuntsman/azeroth-pilot-reloaded) | `dev` | 412 | Yes |
| [book-publish-forge](https://github.com/HenricHuntsman/book-publish-forge) | `main` | 110 | Yes |
| [codex](https://github.com/HenricHuntsman/codex) | `main` | 2462 | Yes |
| [continue](https://github.com/HenricHuntsman/continue) | `main` | 3155 | Yes |
| [dragonforge-code](https://github.com/HenricHuntsman/dragonforge-code) | `main` | 1 | No |
| [gemini-cli](https://github.com/HenricHuntsman/gemini-cli) | `main` | 2351 | Yes |
| [HenricHuntsman](https://github.com/HenricHuntsman/HenricHuntsman) | `main` | 22 | Yes |
| [https-github.com-SpidermanTotro-genspark-os](https://github.com/HenricHuntsman/https-github.com-SpidermanTotro-genspark-os) | `main` | 1 | Yes |
| [kilocode](https://github.com/HenricHuntsman/kilocode) | `main` | 10937 | Yes |
| [Kimi-K2](https://github.com/HenricHuntsman/Kimi-K2) | `main` | 53 | Yes |
| [LisaAI-DatingApp](https://github.com/HenricHuntsman/LisaAI-DatingApp) | `main` | 5 | Yes |
| [LLM4Decompile](https://github.com/HenricHuntsman/LLM4Decompile) | `main` | 140 | Yes |
| [mini-AGI](https://github.com/HenricHuntsman/mini-AGI) | `main` | 137 | Yes |
| [NebulaUltimate](https://github.com/HenricHuntsman/NebulaUltimate) | `main` | 38 | Yes |
| [nvm](https://github.com/HenricHuntsman/nvm) | `master` | 360 | Yes |
| [nxdumptool](https://github.com/HenricHuntsman/nxdumptool) | `rewrite` | 187 | Yes |
| [opencode](https://github.com/HenricHuntsman/opencode) | `main` | 177 | Yes |
| [QuestMaster-Pro](https://github.com/HenricHuntsman/QuestMaster-Pro) | `main` | 70 | Yes |
| [QuestMasterPro](https://github.com/HenricHuntsman/QuestMasterPro) | `main` | 6 | Yes |
| [rabbit-foundry](https://github.com/HenricHuntsman/rabbit-foundry) | `main` | 166 | Yes |
| [rea](https://github.com/HenricHuntsman/rea) | `main` | 4059 | Yes |
| [repo-manager-ultimate](https://github.com/HenricHuntsman/repo-manager-ultimate) | `main` | 24 | Yes |
| [Trinity-Studio-Architecture](https://github.com/HenricHuntsman/Trinity-Studio-Architecture) | `main` | 3 | Yes |
| [TrinityCore](https://github.com/HenricHuntsman/TrinityCore) | `master` | 22458 | Yes |
| [Vitruvian](https://github.com/HenricHuntsman/Vitruvian) | `master` | 12087 | Yes |
| [wordcraft](https://github.com/HenricHuntsman/wordcraft) | `main` | 514 | Yes |

## Profile cleanup

- Replaced the repetitive profile README with a concise project guide, including OpenCode, Wordcraft, Artcraft and REA.
- Updated account totals from the 14 October snapshot.
- Corrected the migration checklist that still claimed the profile repository had not been renamed.
- Moved nine source/configuration files to `archive/swift-prototypes/` and six ZIP bundles to `archive/bundles/`.
- Preserved every moved file by its existing Git blob SHA; archive inventory records original names, sizes and hashes.
- Kept the banner, dev-hours utility and historical audit documents.
- Added ignore rules for Python cache files and local timer state.
- No repository was deleted, renamed, archived or made public.

## Findings and next checks

| Area | Evidence | Follow-up |
| --- | --- | --- |
| Profile prototypes | Loose Swift files, simulated IP lookup, theme logging stub, fixed scene template, no root app manifest | Preserved and labelled; a separate Apple-platform build is needed before claiming a working app |
| Profile bundles | Six historical ZIP uploads; smallest is 43 bytes | Preserved unchanged; inspect ZIP contents before claiming a valid installer or removing a duplicate |
| Kimi-K2 | Four tracked Python bytecode files had corresponding source files | Removed those four generated files and added cache ignore rules; kept distribution ZIP and checksums |
| Vitruvian | `build/` contains CMake definitions, profiles and image-building shell scripts | Retained as source/build infrastructure |
| mini-AGI | `corpora/` contains Python source/configuration; `runs/samples.txt` is a recorded output; README.md.clean differs from README.md | Retained source, unique documentation and recorded output; rebuild ZIP remains uninspected |
| QuestMasterPro | ZIP-heavy legacy collection distinct from QuestMaster-Pro | Keep separate until contents and unique history are compared |
| AgentFoundry TrinityCore Studio | Only a README in the default-branch listing | Expanded README to explain placeholder status and link separate Trinity projects |
| Trinity Studio Architecture | Three tracked files including README and instructions | Small planning repository; no build verified |
| Genspark legacy | One README despite reported size zero | Repository size zero does not mean empty |
| dragonforge-code | Initial scaffold changed during review; follow-up found 177 files including Go source, README and workflows | Earlier scaffold observation is superseded; runtime/build status was not checked |
| Legacy URL names | Two public repository slugs still contain SpidermanTotro | Review integrations before renaming |
| AgentFoundry Instantly | Many root status/completion reports alongside multiple app directories | Reconcile reports with actual builds before reorganising app roots |
| TrinityCore | 22458 tracked files enumerated through split subtrees | Nested inventory complete; code/build review remains separate |

## Validation boundary

Profile relative links and moved-file hashes were checked against the resulting tree. No application build, dependency upgrade, ZIP extraction, all-branch recovery, runtime test, or account-wide secret scan was performed. Existing reports dated 14 October remain historical snapshots, not today's results.

Further source changes belong in each project's own reviewed change set. In particular, generated-looking folders, checkpoints and old ZIPs must be compared before deciding they are redundant.

## Follow-up cleanup completed

- Rabbit Code README now uses `rabbit-code.git` in its explicitly conditional post-rename example. The repository itself remains `rabbit-foundry`.
- Kimi-K2 cleanup commit: `e7fa6d0cb1c52c7c7315c727a889d17c6eabcedc`.
- Rabbit Code documentation commit: `b17ca50ad3d09feae0e0e96c8fdba9d0f3cfaa37`.
- Trinity Studio placeholder documentation commit: `f5dba3e27e1b94d81c02c6835f2fe87539c41c60`.
- Verified resulting default-branch file listings: only the four intended bytecode files were removed from Kimi-K2; its source files and distribution artifacts were preserved. The other two repositories changed only their README.
- No runtime code or dependencies were changed. Application tests were not run for these cache/documentation changes.
