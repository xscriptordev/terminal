#!/usr/bin/env bash
set -euo pipefail

RED='\033[0;31m'
GREEN='\033[0;32m'
CYAN='\033[0;36m'
NC='\033[0m'

THEMES_DIR="${CLAUDE_CODE_THEMES_DIR:-$HOME/.claude/themes}"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SOURCE_DIR="$(cd "$SCRIPT_DIR/../themes" && pwd)"

if [ ! -d "$SOURCE_DIR" ]; then
  echo -e "${RED}Error: themes directory not found at $SOURCE_DIR${NC}"
  echo "Run this script from within the repository."
  exit 1
fi

mkdir -p "$THEMES_DIR"

count=0
for theme_json in "$SOURCE_DIR"/*.json; do
  [ -f "$theme_json" ] || continue
  name="$(basename "$theme_json")"
  target="$THEMES_DIR/$name"

  if [ -L "$target" ] && [ "$(readlink "$target")" = "$theme_json" ]; then
    echo -e "  ${CYAN}⊳${NC} $name ${GREEN}already linked${NC}"
  elif [ -f "$target" ]; then
    cp "$theme_json" "$target"
    echo -e "  ${CYAN}⊳${NC} $name ${GREEN}copied${NC}"
  else
    ln -sf "$theme_json" "$target"
    echo -e "  ${CYAN}⊳${NC} $name ${GREEN}linked${NC}"
  fi
  count=$((count + 1))
done

echo ""
echo -e "${GREEN}Done!${NC} $count theme(s) installed to $THEMES_DIR"
echo -e "Run ${CYAN}/theme${NC} inside Claude Code to pick one."
