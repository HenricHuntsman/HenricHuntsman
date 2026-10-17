# Naming and claim corrections — 18 October 2026

## Confirmed corrections

| Repository | Misleading description | Current correction |
| --- | --- | --- |
| Kimi-K2 | Complete Kimi/FORGE integration, working Linux OS builder, professional media tools, measured gains | FORGE Integration Lab: prototype; model and tools are simulated; OS/video build steps only print messages; gains are estimates |
| AgentFoundry-instantly | Complete professional suite, 100% offline, universal installation, native Linux completion | AgentFoundry Workspace: alpha web/Node/Electron application; no OS claim; optional network code and unqualified desktop packages stated |
| Genspark OS concept | AI-first Linux distribution | Planning-only README; no implemented distribution, image or boot evidence |
| Nebula legacy page | Working AppImage/deb downloads and all modules 100% functional | Legacy archive; old page preserved; installation and completion claims withdrawn |
| Trinity architecture seed | Ambiguous product identity | Planning-only project; proposed CLI milestones separated from implemented code |
| RepoForge | Current account audit as fallback data | Historical sample data distinguished from live scans |

Original READMEs and installation instructions were preserved as labelled legacy files where replaced. AgentFoundry's root project reports were labelled historical, with current status delegated to its README. Kimi's 15 Markdown documentation inputs were labelled as historical/unverified; these files are consumed by its prompt loader, so runtime output based on old capability descriptions remains a qualification gap.

## Initial source evidence (before runtime correction)

- Kimi `build_system.py`: `build_video_editor` and `build_linux_os` print readiness strings. Source ZIP/checksum creation does not construct an ISO.
- Kimi `kimi_forge_unified.py`: `generate` simulates a model response; `execute_tool` returns a success-shaped dictionary instead of executing the named implementations.
- Kimi `forge_gui.py`: code-review, book-analysis and upscaling routes contain fixed result strings.
- AgentFoundry `server/index.js`: Express/Socket.IO application, with no explicit loopback host in `server.listen(PORT)`.
- AgentFoundry includes provider/web-access code; deterministic local helpers are not proof of neural inference or an entirely offline app.
- Vitruvian's `build/` contains CMake definitions and image-building scripts; it was preserved as actual build infrastructure.

## Executed validation

AgentFoundry's locked dependency install with scripts disabled, 22 existing tests, and Vite build passed. Build output reported a large JavaScript chunk warning. Git whitespace checks passed for the reviewed local documentation changes. Electron packaging, native dependency installation and live model/GUI acceptance were not performed.

## Scope limits and remaining work

All accessible repository file trees and public root README excerpts were inventoried in the earlier pass. This deeper pass inspected source and scanned claims in the Kimi and AgentFoundry checkouts, plus the small planning/legacy repositories. **It is not an every-line content, security or dependency audit of all 37 repositories.** Historical text remains intentionally preserved and marked; remaining GUI canned success messages and benchmark estimates still need explicit demo handling or replacement.

Display-name changes do not rename GitHub URLs or internal package IDs. Renaming a repository or changing an application ID requires integration/upgrade review; no such renames were performed.

## Runtime follow-up

Kimi/FORGE's model/tool wrapper now labels demonstrations and reports nonexecution; its full build fails explicitly at unimplemented video/OS steps. The test target now propagates syntax and regression failures. Six new regression tests passed locally and failed against the previous implementation; a malformed-source fixture returned nonzero through `make test`. See [the source change](https://github.com/HenricHuntsman/Kimi-K2/commit/7d0caee0d2150b159ce8a1c623b05cc192aa2b7b). Python 3.11/3.14 hosted checks were added; their outcome is separate from the local result. This repairs false completion signals, not the missing implementations.
