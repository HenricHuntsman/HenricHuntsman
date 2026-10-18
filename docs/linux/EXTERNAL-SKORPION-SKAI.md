# External Skorpion OS and Skai evaluation

Author and upstream: [Endrx2008](https://github.com/Endrx2008). These are external projects; this evaluation does not claim their authorship or merge them into Henric's applications. Original source and licence notices remain in upstream checkouts.

[Runner started 19 October 2026](https://github.com/HenricHuntsman/HenricHuntsman/actions/runs/39131321672).

## Pinned inputs

- Skorpion source/assets: e24616de79cfb5941b9287e9ebe4534baa45a7b5.
- Skai source: 3bd015fe45653b867fab2cb8c98e7c8c8f0a8238.
- Skorpion ISO: external SourceForge URL linked from upstream README. Its digest is recorded at download time; no publisher digest was available from the inspected repository. It is not version-pinned by the source commit.
- Ollama runtime: v0.40.6, release SHA-256 verified by runner.
- Test model: qwen2.5:0.5b, downloaded to runner-only storage; resolved model list recorded. This differs from upstream qwen2.5:14b.

## What the runner attempts

Skorpion: validate ISO boot catalog, boot in network-disabled QEMU UEFI with 2 GiB RAM, and retain screenshots/serial output. Screenshot collection is not a boot-success assertion. No host disk is attached.

Skai: test create/read, persistent memory roundtrip, absolute-path workspace boundary, real local CPU inference, model JSON parsing and an allowlisted file creation. Source is loaded without terminal stream wrappers for import, with temporary working/memory directories. Web searches, browser extensions and unrestricted model-selected operations are not executed.

## Observations before execution

The OS repository mainly contains Calamares configuration and visual assets, rather than a complete ISO build pipeline. Skai includes an absolute personal SKAI_HOME path; the test overrides it in memory. File creation constructs paths without rejecting absolute roots, so the runner probes this within a temporary fixture and records the result. Passing the job does not mean this boundary is repaired.

Results are pending in the linked run. Check skai-capability-evidence and skorpion-boot-evidence artifacts. No upstream repository was modified, no message was sent, and no changes were made to the user's installed Ollama.

## Follow-up — 19 October

Initial run results: live CPU inference returned SKAI_RUNNER_OK, model-generated create_file JSON created runner-note.txt, file readback and memory roundtrip passed. The upstream absolute path probe escaped SKAI_HOME inside a disposable fixture. Original ISO URL returned HTTP 404 before VM startup.

Added runner-side skai_guard.py to reject absolute paths, parent traversal, resolved symlink escapes and bulk deletion. Six local regression categories passed. The adapter changes the evaluation dispatch, not upstream code; concurrent symlink replacement is outside its guarantees. A normal nested path remains supported.

Located current Lite 3.5 ISO at https://downloads.sourceforge.net/project/skos/skorpion_lite-3.5/skorpion_lite-3.5.iso . Current download-page SHA-256: cde94abb299ca213d38b69dfb1b9531903c9fe4ef3df9533ab2da566e2e03b64 . Source: https://sourceforge.net/projects/skos/files/skorpion_lite-3.5/skorpion_lite-3.5.iso/download . Earlier search snapshot had a different digest; the runner requires the current pinned value and refuses a mismatch.

[Guarded AI and corrected ISO rerun](https://github.com/HenricHuntsman/HenricHuntsman/actions/runs/39131834007) is pending. No Skorpion boot claim yet.
