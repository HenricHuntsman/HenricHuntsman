# Linux projects and recovery folders

Reviewed 19 October 2026. These repositories already exist; this pass organises documentation rather than creating duplicate repositories or combining independent build systems.

| Project | Current role | Organisation and next milestone |
| --- | --- | --- |
| [Vitruvian](https://github.com/HenricHuntsman/Vitruvian) | Linux-based OS; update branch amd64 and ISO workflows passed | Pinned amd64 QEMU boot-evidence run started; desktop/install qualification pending |
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

## VM boot attempt — 19 October 2026

[QEMU boot evidence run](https://github.com/HenricHuntsman/Vitruvian/actions/runs/39130337741) was started on the upstream integration branch. It downloads the amd64 raw image from run 39080372001, checks the included SHA-256 files and boots an isolated, network-disabled snapshot. Screenshots at 30/60/90 seconds and serial/QEMU logs are retained for review. Job success means evidence collection, not desktop functionality. This supersedes earlier statements that no fork build was available. The old default branch and its review remain historical evidence.

The hosted connector cannot retrieve the 867 MB raw artifact (512 MB transfer limit), so the VM attempt runs inside GitHub Actions. No local PC installation or disk modification is performed.

## Linux desktop packaging checks — 19 October 2026

Dedicated test-and-package runs started for [RepoForge](https://github.com/HenricHuntsman/repo-manager-ultimate/actions/runs/39130396625) and [AgentFoundry](https://github.com/HenricHuntsman/AgentFoundry-instantly/actions/runs/39130398211). They install using npm ci, run tests and attempt AppImage/deb builds with publishing disabled. These gates do not establish desktop launch or successful package installation. Any package build failures remain blockers until repaired and retested.

### Executed results

- RepoForge: [qualification rerun passed](https://github.com/HenricHuntsman/repo-manager-ultimate/actions/runs/39130525484). Eight tests passed, the frontend built, and AppImage/deb packages were retained in the linux-packages artifact. Fixed missing deb maintainer metadata. Installation and desktop behavior still require testing.
- Vitruvian first capture showed SeaBIOS stuck at Booting from Hard Disk. The artifact is vos-uefi.raw; this establishes a firmware mismatch in the initial test, not a guest OS failure. Corrected to OVMF pflash and started [UEFI rerun](https://github.com/HenricHuntsman/Vitruvian/actions/runs/39130673114). The intermediate -bios attempt failed before guest startup.
- AgentFoundry: clean installation exposed missing XInput headers, then a legacy ANGLE source missing cstdint with the modern compiler. Added native prerequisites and an explicit compiler include; new package qualification is pending. No working installer is claimed.

### Verified graphical boot

The [corrected UEFI run](https://github.com/HenricHuntsman/Vitruvian/actions/runs/39130673114) produced a 120-second screenshot showing the Vitruvian graphical Welcome screen, with language/keymap controls and Install / Try It Now buttons. The screenshot was downloaded and visually inspected. Serial output shows the root filesystem check completed cleanly. This verifies graphical boot of the pinned candidate in QEMU TCG with 2 GiB RAM, not installation, desktop application interaction, shutdown or bare-metal support. [Evidence artifact](https://github.com/HenricHuntsman/Vitruvian/actions/runs/39130673114/artifacts/12137478087).

## Latest check — 19 October, 00:36 Melbourne

- AgentFoundry: [Linux package qualification passed](https://github.com/HenricHuntsman/AgentFoundry-instantly/actions/runs/39130748499); linux-packages artifact retained (971 MB archive). Native dependency prerequisites and legacy ANGLE compiler include resolved the observed installation blockers. Desktop installation/runtime remains untested.
- RepoForge: tests, build and AppImage/deb packaging passed in run 39130525484; installation/runtime remains untested.
- Vitruvian: latest ISO, arm64 and native amd64 workflows passed. Pinned earlier amd64 candidate was visually verified at its graphical Welcome screen in run 39130673114.
- Skai: guarded evaluation passed in [run 39131834007](https://github.com/HenricHuntsman/HenricHuntsman/actions/runs/39131834007). Local CPU response matched, model-created file and memory passed, and absolute path escape was blocked by the evaluation adapter. Upstream remains unchanged.
- Skorpion: same run still retrieving the corrected ISO. Boot capture is pending; no Skorpion boot success established.
- Kimi, DragonForge and Greenlight: latest sampled checks passed. Those checks do not establish GPU runtime or installation on the user's PC.

Earlier pending/failure notes are retained to document repairs; latest results above supersede their current status.

## Continued runtime qualification — 19 October, 01:14 Melbourne

- Skorpion's earlier run reached only 182 MiB of the 3.3 GB ISO in five minutes; curl restarted after timeout and the 15-minute job was cancelled. This was a transfer timeout, not a guest boot failure. Replaced restarting curl transfers with resumable segmented aria2 download, a 25-minute transfer ceiling and 35-minute job limit. Check the latest external evaluation run for completion; checksum verification remains mandatory.
- RepoForge now has an actual offline Electron-window test using production dist assets and its real main process. First attempt failed before UI startup because chrome-sandbox lacked root ownership/setuid permissions on the runner. Configured the disposable runner's helper and started a new run. No successful desktop render is claimed yet. AppImage/deb builds still passed before that runtime failure.
- TraceForge failed-job logs returned BlobNotFound, so failure causes remain unknown from this inspection. No speculative source repair was made.
