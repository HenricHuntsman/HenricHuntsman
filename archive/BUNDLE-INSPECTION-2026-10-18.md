# Historical bundle inspection — 18 October 2026

Archives were read as bytes, listed and CRC-checked without executing their contents. A passing CRC check does not establish that a project compiles or an installer works.

| Profile file | Result |
| --- | --- |
| GhostScanner_OTA_Bundle_REAL.zip | Valid ZIP, 4 entries: OTA manifest, HTML and two PNGs. No IPA payload. Manifest references an old external GhostScanner.ipa URL; availability unverified |
| LisaAI_Install_Package.placeholder.txt | Formerly named .zip; actually 43 bytes of plain-text placeholder content. Renamed without modifying its contents |
| LisaAI_XcodeProject.zip | Valid ZIP, 12 entries, source files plus a project.pbxproj explicitly labelled placeholder |
| LisaCodeIDE_XcodeProject_FOR_BUILD.zip | Valid ZIP, 3 entries; project configuration explicitly labelled placeholder |
| LuisaLauncher_Xcode.zip | Valid ZIP, 4 entries; tiny source/plist skeleton |
| LuisaLauncher_Xcode_FULL.zip | Valid ZIP, 6 entries; project file is only a comment, not a verified Xcode project |

All five actual profile ZIPs passed CRC checks. No real Apple application build or signing validation was performed.

## Other repositories

- QuestMasterPro's 61-entry historical addon ZIP passed CRC checks and is retained.
- QuestMasterPro's unrelated 86-entry Book Publish Forge ZIP exactly matched the copy in Book Publish Forge by both Git blob SHA and SHA-256. Removed only the redundant QuestMasterPro copy; the Book Publish Forge copy remains.
- Kimi-K2's 21-entry distribution ZIP passed CRC checks. Its MD5 and byte size match the committed checksums.json. No installation or capability claims were validated.
- The larger experimental Azeroth rewrite archive and mini-AGI rebuild archive did not return payloads through the file-read action. Their contents remain unverified and retained.

## Follow-up

Repair placeholder projects in a separate implementation task with an Apple toolchain; compare retained addon snapshots before recovering unique code; review prototype runtime/network behavior before merging archived components.
