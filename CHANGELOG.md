# Changelog

All notable changes to Terminal Xscriptor will be documented in this file.

## 2026-07-17

### Added
- `cli/` directory with Helix and OpenCode repos imported via git subtree
- `cli/README.md` entry point for CLI tools
- `cli/claude-code` added
- `cli/gitnapse/` with Xscriptor colour themes for GitNapse and install script

### Changed
- Updated main README with CLI section and content nav entry
- Updated CLI tools badge from 2 to 3

### Added
- `emulators/terax/` with Terax themes imported via git merge (history preserved)
- Terax badge and entry in main README and emulators README

### Removed
- Duplicate CODE_OF_CONDUCT, CONTRIBUTING, LICENSE, SECURITY from `cli/helix/`, `cli/opencode/`, `emulators/terax/` (handled at repo root)

## [1.0.0] - 2026-06-12

### Added
- Initial release with 12 city-themed color schemes (x, madrid, lahabana, miami, paris, tokio, oslo, helsinki, berlin, london, praha, bogota)
- Support for 18+ terminal emulators: Alacritty, Foot, Ghostty, GNOME Terminal, Hyper, iTerm2, Kitty, Konsole, MobaXterm, PowerShell/Windows Terminal, Ptyxis, PuTTY, Terminal.app, Terminator, Termux, Tilix, Warp, WezTerm, XFCE Terminal
- Per-emulator install and uninstall scripts with dependency management
- Universal interactive installer (`emulators/install.sh`)
- Theme builder/generator (`builder/build.py`) with template system
- Shell aliases for quick theme switching in each terminal
- Starship prompt configuration with per-theme variants
- Ghostty CSS gradient border styles per theme
- Hack Nerd Font asset
- GitHub Issues-Roadmap sync action
- ROADMAP.md, CONTRIBUTING.md, CODE_OF_CONDUCT.md, SECURITY.md, SUPPORT.md

### Changed
- Project rebranded from xscriptordev to xscriptor
- Major refactor of directory structure and naming conventions across all emulators
- Updated installation scripts for improved reliability and cross-platform support
- Standardized theme file names across all emulators

### Fixed
- Fixed theme names and references across multiple emulators
- Corrected Konsole theme display issues
- Fixed font download logic in install scripts
- Adjusted Ghostty padding configuration
