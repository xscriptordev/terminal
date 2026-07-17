# Theme Generator

Generates Claude Code theme files from X Colors palette definitions (`colors.md`).

## Usage

```bash
# Download latest colors from GitHub and generate
python generate.py

# Use the colors.md URL directly
python generate.py https://raw.githubusercontent.com/xscriptor/xassets/main/colors/colors.md

# Use a local colors.md file
python generate.py ./colors.md

# Specify output directory
python generate.py --out ../themes
python generate.py https://raw.githubusercontent.com/xscriptor/xassets/main/colors/colors.md -o ~/.claude/themes
```

## How it works

1. Reads palette definitions from markdown — either downloaded from the X Colors repository or a local file. The file uses `<h2>` headings for palette names followed by ` ```json ` blocks with ANSI terminal colors (`color0`–`color15`), `background`, and `foreground`.

2. Each palette is automatically classified as **dark** or **light** based on background luminance, and mapped to Claude Code's theme format (~40 semantic tokens):

   | Token group   | Examples                                   |
   |---------------|--------------------------------------------|
   | Accent        | `claude`, `promptBorder`, `suggestion`    |
   | Text          | `text`, `inverseText`, `inactive`, `subtle` |
   | Status        | `success`, `error`, `warning`, `merged`    |
   | Diff          | `diffAdded`, `diffRemoved`, `diffAddedWord` |
   | UI            | `userMessageBackground`, `selectionBg`     |
   | Subagents     | `red_FOR_SUBAGENTS_ONLY`, `blue_...`       |

3. Diff background colors are computed by blending the accent color with the theme background, creating subtle tinted backgrounds for added/removed lines.

4. Output is written as individual JSON files, one per palette.
