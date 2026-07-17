#!/usr/bin/env bash
# Xscriptor Themes for OpenCode - Install Script
# Usage:
#   Remote: curl -fsSL https://raw.githubusercontent.com/xscriptor/opencode/main/themes/xscriptor-themes/install.sh | bash
#   Local:  ./install.sh
set -euo pipefail

REPO_URL="https://raw.githubusercontent.com/xscriptor/opencode/main"
THEMES_DIR="${XDG_CONFIG_HOME:-$HOME/.config}/opencode/themes"
THEMES=(
  "x"
  "madrid"
  "lahabana"
  "miami"
  "paris"
  "tokio"
  "oslo"
  "helsinki"
  "berlin"
  "london"
  "praha"
  "bogota"
)

echo "==> Xscriptor Themes for OpenCode"
echo "==> Installing to: $THEMES_DIR"
echo ""

mkdir -p "$THEMES_DIR"

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
LOCAL_SOURCE="$SCRIPT_DIR/colors"

is_local() {
  if [ -f "$LOCAL_SOURCE/x.json" ] && [ -f "$LOCAL_SOURCE/madrid.json" ]; then
    return 0
  fi
  return 1
}

install_remote() {
  echo "--> Downloading themes from GitHub..."
  for theme in "${THEMES[@]}"; do
    url="$REPO_URL/themes/xscriptor-themes/colors/$theme.json"
    dest="$THEMES_DIR/$theme.json"
    if curl -fsSL "$url" -o "$dest"; then
      echo "    + $theme.json"
    else
      echo "    ERROR: Failed to download $theme.json"
      exit 1
    fi
  done
}

install_local() {
  echo "--> Copying themes from local source..."
  for theme in "${THEMES[@]}"; do
    src="$LOCAL_SOURCE/$theme.json"
    dest="$THEMES_DIR/$theme.json"
    if [ -f "$src" ]; then
      cp "$src" "$dest"
      echo "    + $theme.json"
    else
      echo "    WARNING: $theme.json not found at $src, skipping"
    fi
  done
}

if is_local; then
  install_local
else
  if ! command -v curl &>/dev/null; then
    echo "ERROR: curl is required for remote installation."
    echo "Install curl or run this script from the cloned repository."
    exit 1
  fi
  install_remote
fi

echo ""
echo "==> Installation complete."
echo ""
echo "Select a theme in OpenCode using /theme or set it in tui.json:"
echo '  { "theme": "x" }'
echo ""
echo "Available themes: ${THEMES[*]}"
