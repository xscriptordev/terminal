#!/usr/bin/env sh
set -eu

DEFAULT_REPO_URL="https://github.com/xscriptor-colors/terminal"
BRANCH="main"
DRY_RUN="0"
FORCE="0"

log() { printf "%s\n" "$*"; }
err() { printf "ERROR: %s\n" "$*" >&2; exit 1; }

usage() {
  cat <<EOF
GitNapse themes installer

Installs Xscriptor colour themes for GitNapse.

Options:
  --branch <name>      Branch to use from remote repo (default: main)
  --repo <url>         Remote repository URL (default: ${DEFAULT_REPO_URL})
  --dry-run            Show actions without executing
  --force              Overwrite without prompting
  --help               Show this help

Remote usage:
  sh -c "\$(curl -fsSL https://raw.githubusercontent.com/xscriptor-colors/terminal/main/cli/gitnapse/scripts/install.sh)" -- [options]
  sh -c "\$(wget -qO- https://raw.githubusercontent.com/xscriptor-colors/terminal/main/cli/gitnapse/scripts/install.sh)" -- [options]
EOF
}

copy_into() {
  if [ "$DRY_RUN" = "1" ]; then
    log "DRY: cp -R \"$1\"/* \"$2\"/"
  else
    mkdir -p "$2"
    cp -R "$1"/* "$2"/
  fi
}

parse_args() {
  REPO_URL="${DEFAULT_REPO_URL}"
  while [ $# -gt 0 ]; do
    case "$1" in
      --branch) BRANCH="${2:-}"; [ -n "${2:-}" ] || err "Missing branch name"; shift 2 ;;
      --repo) REPO_URL="${2:-}"; [ -n "${2:-}" ] || err "Missing repository URL"; shift 2 ;;
      --dry-run) DRY_RUN="1"; shift ;;
      --force) FORCE="1"; shift ;;
      --help|-h) usage; exit 0 ;;
      *) err "Unknown option: $1" ;;
    esac
  done
}

detect_source_dir() {
  # Running from cli/gitnapse/ (themes/ is a sibling of scripts/)
  if [ -d "./themes" ]; then
    SRC_DIR="$(pwd)"
    return
  fi
  # Running from cli/gitnapse/scripts/
  if [ -d "../themes" ]; then
    SRC_DIR="$(cd .. && pwd)"
    return
  fi
  TMP_DIR="$(mktemp -d "${TMPDIR:-/tmp}/gn-inst.XXXXXX")"
  if command -v git >/dev/null 2>&1; then
    if [ "$DRY_RUN" = "1" ]; then
      log "DRY: git clone --depth=1 -b \"$BRANCH\" \"$REPO_URL\" \"$TMP_DIR/terminal\""
    else
      git clone --depth=1 -b "$BRANCH" "$REPO_URL" "$TMP_DIR/terminal"
    fi
    SRC_DIR="$TMP_DIR/terminal/cli/gitnapse"
  else
    command -v curl >/dev/null 2>&1 || command -v wget >/dev/null 2>&1 || err "git or curl/wget required"
    command -v tar >/dev/null 2>&1 || err "tar is required for non-git download"
    TAR_URL="$(printf "%s/archive/refs/heads/%s.tar.gz" "$REPO_URL" "$BRANCH")"
    if [ "$DRY_RUN" = "1" ]; then
      if command -v curl >/dev/null 2>&1; then
        log "DRY: curl -fsSL \"$TAR_URL\" | tar -xz -C \"$TMP_DIR\""
      else
        log "DRY: wget -qO- \"$TAR_URL\" | tar -xz -C \"$TMP_DIR\""
      fi
    else
      if command -v curl >/dev/null 2>&1; then
        curl -fsSL "$TAR_URL" | tar -xz -C "$TMP_DIR"
      else
        wget -qO- "$TAR_URL" | tar -xz -C "$TMP_DIR"
      fi
    fi
    CANDIDATE="$(find "$TMP_DIR" -maxdepth 2 -type d -name "gitnapse" | head -n 1 || true)"
    [ -n "$CANDIDATE" ] || err "Failed to extract remote repository"
    SRC_DIR="$CANDIDATE"
  fi
}

install_themes() {
  SRC_THEMES="$SRC_DIR/themes"
  [ -d "$SRC_THEMES" ] || err "Themes directory not found in source"

  # Determine config directory based on platform
  case "$(uname -s)" in
    Linux)
      CONFIG_DIR="${XDG_CONFIG_HOME:-$HOME/.config}/GitNapse"
      ;;
    Darwin)
      CONFIG_DIR="$HOME/Library/Application Support/com.GitNapse.GitNapse"
      ;;
    *)
      CONFIG_DIR="${XDG_CONFIG_HOME:-$HOME/.config}/GitNapse"
      ;;
  esac

  DEST_THEMES="$CONFIG_DIR/themes"
  copy_into "$SRC_THEMES" "$DEST_THEMES"
  log "Themes installed at: $DEST_THEMES"

  # Create theme config if it doesn't exist
  THEME_CFG="$CONFIG_DIR/theme.jsonc"
  if [ ! -f "$THEME_CFG" ] || [ "$FORCE" = "1" ]; then
    if [ "$DRY_RUN" = "1" ]; then
      log "DRY: write theme config to $THEME_CFG"
    else
      mkdir -p "$CONFIG_DIR"
      printf '{\n    // GitNapse Theme\n    "theme_name": "X"\n}\n' > "$THEME_CFG"
      log "Theme config created at: $THEME_CFG"
    fi
  else
    log "Theme config already exists: $THEME_CFG (use --force to overwrite)"
  fi
}

main() {
  parse_args "$@"
  detect_source_dir
  install_themes
  log "Install completed"
}

main "$@"
