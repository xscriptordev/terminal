#!/usr/bin/env sh
set -eu

DEFAULT_REPO_URL="https://github.com/xscriptor/helix"
BRANCH="main"
MODE="complete"
DRY_RUN="0"
FORCE="0"
NO_BACKUP="0"

log() { printf "%s\n" "$*"; }
err() { printf "ERROR: %s\n" "$*" >&2; exit 1; }

usage() {
  cat <<EOF
Helix installer (themes and config)

Options:
  --themes-only        Install only themes
  --minimal            Install minimal config + themes
  --complete           Install complete config + themes (default)
  --branch <name>      Branch to use from remote repo (default: main)
  --repo <url>         Remote repository URL (default: ${DEFAULT_REPO_URL})
  --dry-run            Show actions without executing
  --force              Overwrite without creating backup
  --no-backup          Do not create backup of existing config
  --help               Show this help

Remote usage:
  sh -c "\$(curl -fsSL https://raw.githubusercontent.com/xscriptor/helix/main/install.sh)" -- [options]
  sh -c "\$(wget -qO- https://raw.githubusercontent.com/xscriptor/helix/main/install.sh)" -- [options]
EOF
}

copy() {
  if [ "$DRY_RUN" = "1" ]; then
    log "DRY: cp -R \"$1\" \"$2\""
  else
    mkdir -p "$2"
    cp -R "$1" "$2"
  fi
}

copy_into() {
  if [ "$DRY_RUN" = "1" ]; then
    log "DRY: cp -R \"$1\"/* \"$2\"/"
  else
    mkdir -p "$2"
    cp -R "$1"/* "$2"/
  fi
}

backup_file() {
  path="$1"
  if [ -f "$path" ] && [ "$NO_BACKUP" = "0" ] && [ "$FORCE" = "0" ]; then
    ts="$(date +%Y%m%d%H%M%S)"
    bak="${path}.bak-${ts}"
    if [ "$DRY_RUN" = "1" ]; then
      log "DRY: mv \"$path\" \"$bak\""
    else
      mv "$path" "$bak"
      log "Backup created: $bak"
    fi
  fi
}

parse_args() {
  REPO_URL="${DEFAULT_REPO_URL}"
  while [ $# -gt 0 ]; do
    case "$1" in
      --themes-only) MODE="themes"; shift ;;
      --minimal) MODE="minimal"; shift ;;
      --complete) MODE="complete"; shift ;;
      --branch) BRANCH="${2:-}"; [ -n "${2:-}" ] || err "Missing branch name"; shift 2 ;;
      --repo) REPO_URL="${2:-}"; [ -n "${2:-}" ] || err "Missing repository URL"; shift 2 ;;
      --dry-run) DRY_RUN="1"; shift ;;
      --force) FORCE="1"; shift ;;
      --no-backup) NO_BACKUP="1"; shift ;;
      --help|-h) usage; exit 0 ;;
      *) err "Unknown option: $1" ;;
    esac
  done
}

detect_source_dir() {
  if [ -d "./themes" ] && [ -d "./settings" ]; then
    SRC_DIR="$(pwd)"
    return
  fi
  TMP_DIR="$(mktemp -d "${TMPDIR:-/tmp}/hx-inst.XXXXXX")"
  if command -v git >/dev/null 2>&1; then
    if [ "$DRY_RUN" = "1" ]; then
      log "DRY: git clone --depth=1 -b \"$BRANCH\" \"$REPO_URL\" \"$TMP_DIR/helix\""
    else
      git clone --depth=1 -b "$BRANCH" "$REPO_URL" "$TMP_DIR/helix"
    fi
    SRC_DIR="$TMP_DIR/helix"
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
    CANDIDATE="$(find "$TMP_DIR" -maxdepth 1 -type d -name "*helix*" | head -n 1 || true)"
    [ -n "$CANDIDATE" ] || err "Failed to extract remote repository"
    SRC_DIR="$CANDIDATE"
  fi
}

install_themes() {
  DEST_DIR="$HOME/.config/helix/themes"
  copy_into "$SRC_DIR/themes" "$DEST_DIR"
  log "Themes installed at: $DEST_DIR"
}

install_config_minimal() {
  DEST_CFG="$HOME/.config/helix/config.toml"
  SRC_CFG="$SRC_DIR/settings/minimal/config.toml"
  [ -f "$SRC_CFG" ] || err "Minimal config not found in repository"
  backup_file "$DEST_CFG"
  if [ "$DRY_RUN" = "1" ]; then
    log "DRY: cp \"$SRC_CFG\" \"$DEST_CFG\""
  else
    mkdir -p "$(dirname "$DEST_CFG")"
    cp "$SRC_CFG" "$DEST_CFG"
  fi
  log "Minimal config installed at: $DEST_CFG"
}

install_config_complete() {
  DEST_CFG="$HOME/.config/helix/config.toml"
  SRC_CFG="$SRC_DIR/settings/complete/config.toml"
  [ -f "$SRC_CFG" ] || err "Complete config not found in repository"
  backup_file "$DEST_CFG"
  if [ "$DRY_RUN" = "1" ]; then
    log "DRY: cp \"$SRC_CFG\" \"$DEST_CFG\""
  else
    mkdir -p "$(dirname "$DEST_CFG")"
    cp "$SRC_CFG" "$DEST_CFG"
  fi
  log "Complete config installed at: $DEST_CFG"
}

main() {
  parse_args "$@"
  detect_source_dir
  case "$MODE" in
    themes)
      install_themes
      ;;
    minimal)
      install_themes
      install_config_minimal
      ;;
    complete)
      install_themes
      install_config_complete
      ;;
    *)
      err "Invalid mode: $MODE"
      ;;
  esac
  if [ "$(uname -s)" = "Darwin" ]; then
    if [ "$DRY_RUN" = "1" ]; then
      log "DRY: mkdir -p \"$HOME/.config/helix\" && touch \"$HOME/.config/helix/config.toml\""
    else
      mkdir -p "$HOME/.config/helix"
      touch "$HOME/.config/helix/config.toml"
    fi
  fi
  log "Install completed"
}

main "$@"
