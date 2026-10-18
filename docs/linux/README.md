# Linux projects and recovery folders

Reviewed 18 October 2026. These repositories already exist; this pass organises documentation rather than creating duplicate repositories or combining independent build systems.

| Project | Current role | Organisation and next milestone |
| --- | --- | --- |
| [Vitruvian](https://github.com/HenricHuntsman/Vitruvian) | Upstream-derived experimental OS source; fork build unverified | docs/revival/; compare upstream, build x86_64 and boot in a VM |
| [Kimi-K2](https://github.com/HenricHuntsman/Kimi-K2) | Python prototype with opt-in local Ollama chat; 41 Python and two frontend tests passed locally and in hosted CI | docs/local-models/; run actual Qwen smoke; no trained Kimi model, executable tools or OS |
| [Genspark OS concept](https://github.com/HenricHuntsman/https-github.com-SpidermanTotro-genspark-os) | Planning only | docs/concepts/; choose requirements and base distribution before implementation |
| [AgentFoundry Workspace](https://github.com/HenricHuntsman/AgentFoundry-instantly) | Alpha application; previous 22 tests and Vite build passed | docs/history/ holds 56 old reports; qualify complete workflow and Linux installer |
| [RepoForge](https://github.com/HenricHuntsman/repo-manager-ultimate) | Repository dashboard and Linux packaging configuration | docs/PROJECT-GUIDE.md; build, install and smoke-test packages |

No project in this OS review is qualified as RC or RTM. Test results above are previously executed evidence, not new runtime validation of this documentation pass. No bootable image has been verified. Repository names, licences, history, source paths and build entry points are preserved. Historical reports retain earlier claims and are not current acceptance evidence.

## Follow-up verification

- Kimi: repaired source bundle includes UI/dependencies/tests/nested docs, SHA-256 checksums and explicit source-only naming. Twenty-two tests passed locally and after extraction using the existing test environment; fresh dependency installation is still unqualified. Setup failures now propagate; unimplemented system installation returns nonzero.
- AgentFoundry: documentation-cleanup CI passed; agent instructions now acknowledge the existing npm test command. Earlier Vite bundle-size warning remains.
- RepoForge: documentation-cleanup CI passed; README uses npm ci for reproducible lockfile installation. Package installation remains unverified.
- Vitruvian: upstream comparison shows 876 commits behind and only the documentation cleanup ahead; no source synchronisation was performed.
- Genspark concept: remaining acceptance milestones are explicit and unverified.

This follow-up changes Kimi packaging/build commands and project documentation. It does not implement model inference, merge the independent applications, produce an OS image or qualify a release.

## Local Qwen and training-truth follow-up

Kimi now has a guarded local Ollama client, opt-in GUI routing and --smoke reporting for one actual local request. Cloud-disabled confirmation is required before prompt transmission. The 41 Python and two frontend tests passed locally, from the extracted prototype source ZIP, and in [hosted CI](https://github.com/HenricHuntsman/Kimi-K2/actions/runs/39083094509). Fixtures verify protocol and failure behaviour; no live Qwen inference or GPU performance was verified here. The enhancement scripts no longer invent gains or datasets; originals remain archived. Earlier packaging-only and demo-only paragraphs above are historical snapshots. This update does not implement training, tool execution or OS creation.
