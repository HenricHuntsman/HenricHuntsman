# Preserved early prototypes

These files previously lived at the profile repository root. They were organised on 18 October 2026 without changing their Git blob contents.

- [Swift prototypes](swift-prototypes/): early Lisa.AI components and theme configuration.
- [Bundles](bundles/): historical ZIP uploads, retained as received.

These are historical experiments, not verified installable releases. There is no root Xcode project or Swift package manifest connecting the loose source files. GhostTracker uses a simulated IP address; ThemeEngine only logs an accent colour; DreamWeaver returns a fixed text template. Camera and audio components still need app integration, permissions and device testing.

ZIP contents have not been extracted or validated. The 43-byte LisaAI install package is too small to assume it contains a usable application. Bundle filenames such as FULL, REAL and FOR_BUILD are historical names, not verified capability claims.

## File move inventory

| Original root path | Preserved path | Bytes | Git blob SHA |
| --- | --- | ---: | --- |
| AppDelegate.swift | [swift-prototypes/AppDelegate.swift](swift-prototypes/AppDelegate.swift) | 370 | `d9db8b2f816b1be8c4e591aa58aeca87b538db8c` |
| DreamWeaver.swift | [swift-prototypes/DreamWeaver.swift](swift-prototypes/DreamWeaver.swift) | 205 | `9e5518e64ef16e2775343c0a98993b2856e5dd1b` |
| EmotionLog.swift | [swift-prototypes/EmotionLog.swift](swift-prototypes/EmotionLog.swift) | 526 | `c5526032dbbb9aebe11b29de22ad5b4d383494d1` |
| GhostScanner_OTA_Bundle_REAL.zip | [bundles/GhostScanner_OTA_Bundle_REAL.zip](bundles/GhostScanner_OTA_Bundle_REAL.zip) | 13517 | `1c1078b621ae0ac0e5ad646c259d7230981612eb` |
| GhostTracker.swift | [swift-prototypes/GhostTracker.swift](swift-prototypes/GhostTracker.swift) | 684 | `b403f01705671369dd6d7a651fb9f91ed9f10386` |
| LisaAI_Install_Package.zip | [bundles/LisaAI_Install_Package.zip](bundles/LisaAI_Install_Package.zip) | 43 | `2cc13104e99aa8b7c2bfe7c3aab6ccf77320e555` |
| LisaAI_XcodeProject.zip | [bundles/LisaAI_XcodeProject.zip](bundles/LisaAI_XcodeProject.zip) | 4217 | `b74ee14d74c94b47a2c9ef6281a2a71863d22e6f` |
| LisaCam.swift | [swift-prototypes/LisaCam.swift](swift-prototypes/LisaCam.swift) | 1186 | `c5b6b568099bc0e95b7733bc4edb8ed812002d4a` |
| LisaCodeIDE_XcodeProject_FOR_BUILD.zip | [bundles/LisaCodeIDE_XcodeProject_FOR_BUILD.zip](bundles/LisaCodeIDE_XcodeProject_FOR_BUILD.zip) | 1155 | `989ab96583607196277decd7076a45b7c6c33015` |
| LisaCore_Theme.json | [swift-prototypes/LisaCore_Theme.json](swift-prototypes/LisaCore_Theme.json) | 144 | `2de44e3176e3856ac658c369e1ae261f0e27c343` |
| LisaLogin.swift | [swift-prototypes/LisaLogin.swift](swift-prototypes/LisaLogin.swift) | 671 | `d72f91f21fd1533b3c836bc8be228a37b2e4f8ce` |
| LuisaLauncher_Xcode.zip | [bundles/LuisaLauncher_Xcode.zip](bundles/LuisaLauncher_Xcode.zip) | 663 | `0cf309a9613dbf034d7393940bfdbd0abb67945a` |
| LuisaLauncher_Xcode_FULL.zip | [bundles/LuisaLauncher_Xcode_FULL.zip](bundles/LuisaLauncher_Xcode_FULL.zip) | 1219 | `b6468db6b2ad9decdd08aa2b14b3429ed5371f5d` |
| RadioRecorder.swift | [swift-prototypes/RadioRecorder.swift](swift-prototypes/RadioRecorder.swift) | 894 | `1052bd0895cdb3280bd830b2bd0343ed6b5e527b` |
| ThemeEngine.swift | [swift-prototypes/ThemeEngine.swift](swift-prototypes/ThemeEngine.swift) | 258 | `f166f94afcb0276a9641a088a19c30912cf1d620` |

Git history retains the original root paths. No archive payload or source file was discarded.
