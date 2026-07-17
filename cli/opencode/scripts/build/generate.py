#!/usr/bin/env python3
"""Generate opencode built-in theme JSON files from Xscriptor color palettes.

Usage:
  # Use built-in theme data (12 themes)
  ./generate.py

  # Parse themes from colors.md
  ./generate.py --colors ../../colors.md

  # Specify output directory
  ./generate.py --output ../dist
"""

import json
import os
import sys
import re
import argparse

SCHEMA = "https://opencode.ai/theme.json"

# ─── helpers ────────────────────────────────────────────────────────────

def dv(dark, light):
    return {"dark": dark, "light": light}

def theme(defs_data, theme_data):
    return {"$schema": SCHEMA, "defs": defs_data, "theme": theme_data}

def ensure_dir(path):
    os.makedirs(path, exist_ok=True)

# ─── built-in theme definitions ─────────────────────────────────────────

BUILTIN_THEMES = {}

def register(name, defs_data, theme_data):
    BUILTIN_THEMES[name] = theme(defs_data, theme_data)

# X
register("x", {
    "darkBg": "#0a0a0a", "darkPanel": "#1a1a1a", "darkElement": "#111111",
    "darkFg": "#f7f1ff", "darkMuted": "#69676c",
    "darkRed": "#fc618d", "darkGreen": "#7bd88f", "darkYellow": "#fce566",
    "darkOrange": "#fd9353", "darkPurple": "#948ae3", "darkCyan": "#5ad4e6",
    "lightBg": "#f7f1ff", "lightPanel": "#e8e0f0", "lightElement": "#f0e8f8",
    "lightFg": "#1a1a1a", "lightMuted": "#9a98a0",
    "lightRed": "#d4557a", "lightGreen": "#5fb87a", "lightYellow": "#d4b84a",
    "lightOrange": "#d47a42", "lightPurple": "#7a70c4", "lightCyan": "#4ab8cc",
}, {
    "primary": dv("darkCyan", "lightCyan"),
    "secondary": dv("darkPurple", "lightPurple"),
    "accent": dv("darkCyan", "lightCyan"),
    "error": dv("darkRed", "lightRed"),
    "warning": dv("darkYellow", "lightYellow"),
    "success": dv("darkGreen", "lightGreen"),
    "info": dv("darkCyan", "lightCyan"),
    "text": dv("darkFg", "lightFg"),
    "textMuted": dv("darkMuted", "lightMuted"),
    "background": dv("darkBg", "lightBg"),
    "backgroundPanel": dv("darkPanel", "lightPanel"),
    "backgroundElement": dv("darkElement", "lightElement"),
    "border": dv("darkMuted", "lightMuted"),
    "borderActive": dv("darkCyan", "lightCyan"),
    "borderSubtle": dv("darkMuted", "lightMuted"),
    "diffAdded": dv("darkGreen", "lightGreen"),
    "diffRemoved": dv("darkRed", "lightRed"),
    "diffContext": dv("darkFg", "lightFg"),
    "diffHunkHeader": dv("darkMuted", "lightMuted"),
    "diffHighlightAdded": dv("#a8e8b0", "#5fb87a"),
    "diffHighlightRemoved": dv("#fca0b0", "#d4557a"),
    "diffAddedBg": dv("#1a2a1a", "#e8f5e9"),
    "diffRemovedBg": dv("#2a1a1a", "#fce4ec"),
    "diffContextBg": dv("darkPanel", "lightPanel"),
    "diffLineNumber": dv("darkMuted", "lightMuted"),
    "diffAddedLineNumberBg": dv("#152215", "#d0e8d4"),
    "diffRemovedLineNumberBg": dv("#221515", "#f0d4d8"),
    "markdownText": dv("darkFg", "lightFg"),
    "markdownHeading": dv("darkCyan", "lightCyan"),
    "markdownLink": dv("darkOrange", "lightOrange"),
    "markdownLinkText": dv("darkCyan", "lightCyan"),
    "markdownCode": dv("darkGreen", "lightGreen"),
    "markdownBlockQuote": dv("darkMuted", "lightMuted"),
    "markdownEmph": dv("darkYellow", "lightYellow"),
    "markdownStrong": dv("darkYellow", "lightYellow"),
    "markdownHorizontalRule": dv("darkMuted", "lightMuted"),
    "markdownListItem": dv("darkCyan", "lightCyan"),
    "markdownListEnumeration": dv("darkCyan", "lightCyan"),
    "markdownImage": dv("darkOrange", "lightOrange"),
    "markdownImageText": dv("darkCyan", "lightCyan"),
    "markdownCodeBlock": dv("darkFg", "lightFg"),
    "syntaxComment": dv("darkMuted", "lightMuted"),
    "syntaxKeyword": dv("darkPurple", "lightPurple"),
    "syntaxFunction": dv("darkCyan", "lightCyan"),
    "syntaxVariable": dv("darkOrange", "lightOrange"),
    "syntaxString": dv("darkGreen", "lightGreen"),
    "syntaxNumber": dv("darkYellow", "lightYellow"),
    "syntaxType": dv("darkOrange", "lightOrange"),
    "syntaxOperator": dv("darkRed", "lightRed"),
    "syntaxPunctuation": dv("darkFg", "lightFg"),
})

# Madrid
register("madrid", {
    "darkBg": "#1a1a1a", "darkPanel": "#2d2d2d", "darkElement": "#242424",
    "darkFg": "#fafafa", "darkMuted": "#666666",
    "darkRed": "#cc0030", "darkGreen": "#009030", "darkYellow": "#a07810",
    "darkBlue": "#008ab0", "darkPurple": "#6030b0", "darkCyan": "#008ab0",
    "lightBg": "#fafafa", "lightPanel": "#e8e8e8", "lightElement": "#f0f0f0",
    "lightFg": "#1a1a1a", "lightMuted": "#4d4d4d",
    "lightRed": "#990026", "lightGreen": "#007a28", "lightYellow": "#8a6408",
    "lightBlue": "#007a9e", "lightPurple": "#4d2699", "lightCyan": "#007a9e",
}, {
    "primary": dv("darkCyan", "lightCyan"),
    "secondary": dv("darkPurple", "lightPurple"),
    "accent": dv("darkCyan", "lightCyan"),
    "error": dv("darkRed", "lightRed"),
    "warning": dv("darkYellow", "lightYellow"),
    "success": dv("darkGreen", "lightGreen"),
    "info": dv("darkCyan", "lightCyan"),
    "text": dv("darkFg", "lightFg"),
    "textMuted": dv("darkMuted", "lightMuted"),
    "background": dv("darkBg", "lightBg"),
    "backgroundPanel": dv("darkPanel", "lightPanel"),
    "backgroundElement": dv("darkElement", "lightElement"),
    "border": dv("darkMuted", "#cccccc"),
    "borderActive": dv("darkCyan", "lightCyan"),
    "borderSubtle": dv("darkMuted", "#cccccc"),
    "diffAdded": dv("darkGreen", "lightGreen"),
    "diffRemoved": dv("darkRed", "lightRed"),
    "diffContext": dv("darkFg", "lightFg"),
    "diffHunkHeader": dv("darkMuted", "lightMuted"),
    "diffHighlightAdded": dv("#60d080", "#007a28"),
    "diffHighlightRemoved": dv("#e04860", "#990026"),
    "diffAddedBg": dv("#2a3a2a", "#e8f5e9"),
    "diffRemovedBg": dv("#3a2a2a", "#ffebee"),
    "diffContextBg": dv("darkPanel", "lightPanel"),
    "diffLineNumber": dv("darkMuted", "lightMuted"),
    "diffAddedLineNumberBg": dv("#253525", "#d0e8d4"),
    "diffRemovedLineNumberBg": dv("#352525", "#f0d4d8"),
    "markdownText": dv("darkFg", "lightFg"),
    "markdownHeading": dv("darkCyan", "lightCyan"),
    "markdownLink": dv("darkBlue", "lightBlue"),
    "markdownLinkText": dv("darkCyan", "lightCyan"),
    "markdownCode": dv("darkGreen", "lightGreen"),
    "markdownBlockQuote": dv("darkMuted", "lightMuted"),
    "markdownEmph": dv("darkYellow", "lightYellow"),
    "markdownStrong": dv("darkYellow", "lightYellow"),
    "markdownHorizontalRule": dv("darkMuted", "lightMuted"),
    "markdownListItem": dv("darkCyan", "lightCyan"),
    "markdownListEnumeration": dv("darkCyan", "lightCyan"),
    "markdownImage": dv("darkBlue", "lightBlue"),
    "markdownImageText": dv("darkCyan", "lightCyan"),
    "markdownCodeBlock": dv("darkFg", "lightFg"),
    "syntaxComment": dv("darkMuted", "lightMuted"),
    "syntaxKeyword": dv("darkPurple", "lightPurple"),
    "syntaxFunction": dv("darkCyan", "lightCyan"),
    "syntaxVariable": dv("darkBlue", "lightBlue"),
    "syntaxString": dv("darkGreen", "lightGreen"),
    "syntaxNumber": dv("darkYellow", "lightYellow"),
    "syntaxType": dv("darkBlue", "lightBlue"),
    "syntaxOperator": dv("darkRed", "lightRed"),
    "syntaxPunctuation": dv("darkFg", "lightFg"),
})

# Lahabana
register("lahabana", {
    "darkBg": "#363537", "darkPanel": "#4a484c", "darkElement": "#424043",
    "darkFg": "#f7f1ff", "darkMuted": "#69676c",
    "darkRed": "#fc618d", "darkGreen": "#7bd88f", "darkYellow": "#e5ff9d",
    "darkOrange": "#fd9353", "darkPurple": "#948ae3", "darkCyan": "#5ad4e6",
    "lightBg": "#f7f1ff", "lightPanel": "#e8e0f0", "lightElement": "#f0e8f8",
    "lightFg": "#363537", "lightMuted": "#8a8890",
    "lightRed": "#d4557a", "lightGreen": "#5fb87a", "lightYellow": "#c0d880",
    "lightOrange": "#d47a42", "lightPurple": "#7a70c4", "lightCyan": "#4ab8cc",
}, {
    "primary": dv("darkCyan", "lightCyan"),
    "secondary": dv("darkPurple", "lightPurple"),
    "accent": dv("darkCyan", "lightCyan"),
    "error": dv("darkRed", "lightRed"),
    "warning": dv("darkYellow", "lightYellow"),
    "success": dv("darkGreen", "lightGreen"),
    "info": dv("darkCyan", "lightCyan"),
    "text": dv("darkFg", "lightFg"),
    "textMuted": dv("darkMuted", "lightMuted"),
    "background": dv("darkBg", "lightBg"),
    "backgroundPanel": dv("darkPanel", "lightPanel"),
    "backgroundElement": dv("darkElement", "lightElement"),
    "border": dv("darkMuted", "lightMuted"),
    "borderActive": dv("darkCyan", "lightCyan"),
    "borderSubtle": dv("darkMuted", "lightMuted"),
    "diffAdded": dv("darkGreen", "lightGreen"),
    "diffRemoved": dv("darkRed", "lightRed"),
    "diffContext": dv("darkFg", "lightFg"),
    "diffHunkHeader": dv("darkMuted", "lightMuted"),
    "diffHighlightAdded": dv("#a8e8b0", "#5fb87a"),
    "diffHighlightRemoved": dv("#fca0b0", "#d4557a"),
    "diffAddedBg": dv("#2a2a2a", "#e8f5e9"),
    "diffRemovedBg": dv("#2a2020", "#fce4ec"),
    "diffContextBg": dv("darkPanel", "lightPanel"),
    "diffLineNumber": dv("darkMuted", "lightMuted"),
    "diffAddedLineNumberBg": dv("#252525", "#d0e8d4"),
    "diffRemovedLineNumberBg": dv("#252020", "#f0d4d8"),
    "markdownText": dv("darkFg", "lightFg"),
    "markdownHeading": dv("darkCyan", "lightCyan"),
    "markdownLink": dv("darkOrange", "lightOrange"),
    "markdownLinkText": dv("darkCyan", "lightCyan"),
    "markdownCode": dv("darkGreen", "lightGreen"),
    "markdownBlockQuote": dv("darkMuted", "lightMuted"),
    "markdownEmph": dv("darkYellow", "lightYellow"),
    "markdownStrong": dv("darkYellow", "lightYellow"),
    "markdownHorizontalRule": dv("darkMuted", "lightMuted"),
    "markdownListItem": dv("darkCyan", "lightCyan"),
    "markdownListEnumeration": dv("darkCyan", "lightCyan"),
    "markdownImage": dv("darkOrange", "lightOrange"),
    "markdownImageText": dv("darkCyan", "lightCyan"),
    "markdownCodeBlock": dv("darkFg", "lightFg"),
    "syntaxComment": dv("darkMuted", "lightMuted"),
    "syntaxKeyword": dv("darkPurple", "lightPurple"),
    "syntaxFunction": dv("darkCyan", "lightCyan"),
    "syntaxVariable": dv("darkOrange", "lightOrange"),
    "syntaxString": dv("darkGreen", "lightGreen"),
    "syntaxNumber": dv("darkYellow", "lightYellow"),
    "syntaxType": dv("darkOrange", "lightOrange"),
    "syntaxOperator": dv("darkRed", "lightRed"),
    "syntaxPunctuation": dv("darkFg", "lightFg"),
})

# Miami
register("miami", {
    "darkBg": "#000000", "darkPanel": "#1a1a1a", "darkElement": "#111111",
    "darkFg": "#f7f1ff", "darkMuted": "#69676c",
    "darkRed": "#FF4C8B", "darkGreen": "#7FFFD4", "darkYellow": "#FFD84C",
    "darkBlue": "#00FFA8", "darkPurple": "#D36CFF", "darkCyan": "#47CFFF",
    "lightBg": "#f7f1ff", "lightPanel": "#e8e0f0", "lightElement": "#f0e8f8",
    "lightFg": "#1a1a1a", "lightMuted": "#9a98a0",
    "lightRed": "#d44078", "lightGreen": "#5cd4a8", "lightYellow": "#d4b040",
    "lightBlue": "#30d490", "lightPurple": "#b05cd4", "lightCyan": "#40b0d4",
}, {
    "primary": dv("darkCyan", "lightCyan"),
    "secondary": dv("darkPurple", "lightPurple"),
    "accent": dv("darkGreen", "lightGreen"),
    "error": dv("darkRed", "lightRed"),
    "warning": dv("darkYellow", "lightYellow"),
    "success": dv("darkGreen", "lightGreen"),
    "info": dv("darkCyan", "lightCyan"),
    "text": dv("darkFg", "lightFg"),
    "textMuted": dv("darkMuted", "lightMuted"),
    "background": dv("darkBg", "lightBg"),
    "backgroundPanel": dv("darkPanel", "lightPanel"),
    "backgroundElement": dv("darkElement", "lightElement"),
    "border": dv("darkMuted", "lightMuted"),
    "borderActive": dv("darkCyan", "lightCyan"),
    "borderSubtle": dv("darkMuted", "lightMuted"),
    "diffAdded": dv("darkGreen", "lightGreen"),
    "diffRemoved": dv("darkRed", "lightRed"),
    "diffContext": dv("darkFg", "lightFg"),
    "diffHunkHeader": dv("darkMuted", "lightMuted"),
    "diffHighlightAdded": dv("#a8f0d0", "#5cd4a8"),
    "diffHighlightRemoved": dv("#f4a0b8", "#d44078"),
    "diffAddedBg": dv("#1a2a22", "#e8f5e9"),
    "diffRemovedBg": dv("#2a1a1e", "#fce4ec"),
    "diffContextBg": dv("darkPanel", "lightPanel"),
    "diffLineNumber": dv("darkMuted", "lightMuted"),
    "diffAddedLineNumberBg": dv("#15251d", "#d0e8d4"),
    "diffRemovedLineNumberBg": dv("#22151a", "#f0d4d8"),
    "markdownText": dv("darkFg", "lightFg"),
    "markdownHeading": dv("darkCyan", "lightCyan"),
    "markdownLink": dv("darkBlue", "lightBlue"),
    "markdownLinkText": dv("darkCyan", "lightCyan"),
    "markdownCode": dv("darkGreen", "lightGreen"),
    "markdownBlockQuote": dv("darkMuted", "lightMuted"),
    "markdownEmph": dv("darkYellow", "lightYellow"),
    "markdownStrong": dv("darkYellow", "lightYellow"),
    "markdownHorizontalRule": dv("darkMuted", "lightMuted"),
    "markdownListItem": dv("darkCyan", "lightCyan"),
    "markdownListEnumeration": dv("darkCyan", "lightCyan"),
    "markdownImage": dv("darkBlue", "lightBlue"),
    "markdownImageText": dv("darkCyan", "lightCyan"),
    "markdownCodeBlock": dv("darkFg", "lightFg"),
    "syntaxComment": dv("darkMuted", "lightMuted"),
    "syntaxKeyword": dv("darkPurple", "lightPurple"),
    "syntaxFunction": dv("darkCyan", "lightCyan"),
    "syntaxVariable": dv("darkBlue", "lightBlue"),
    "syntaxString": dv("darkGreen", "lightGreen"),
    "syntaxNumber": dv("darkYellow", "lightYellow"),
    "syntaxType": dv("darkBlue", "lightBlue"),
    "syntaxOperator": dv("darkRed", "lightRed"),
    "syntaxPunctuation": dv("darkFg", "lightFg"),
})

# Paris
register("paris", {
    "darkBg": "#10081a", "darkPanel": "#1e142e", "darkElement": "#181022",
    "darkFg": "#f7f1ff", "darkMuted": "#525053",
    "darkRed": "#fc618d", "darkGreen": "#7bd88f", "darkYellow": "#fce566",
    "darkBlue": "#a3f3ff", "darkPurple": "#c4bdff", "darkCyan": "#a3f3ff",
    "lightBg": "#f7f1ff", "lightPanel": "#e8e0f0", "lightElement": "#f0e8f8",
    "lightFg": "#1a1228", "lightMuted": "#8a8890",
    "lightRed": "#d4557a", "lightGreen": "#5fb87a", "lightYellow": "#d4b84a",
    "lightBlue": "#70c8d4", "lightPurple": "#9a94c4", "lightCyan": "#70c8d4",
}, {
    "primary": dv("darkCyan", "lightCyan"),
    "secondary": dv("darkPurple", "lightPurple"),
    "accent": dv("darkBlue", "lightBlue"),
    "error": dv("darkRed", "lightRed"),
    "warning": dv("darkYellow", "lightYellow"),
    "success": dv("darkGreen", "lightGreen"),
    "info": dv("darkCyan", "lightCyan"),
    "text": dv("darkFg", "lightFg"),
    "textMuted": dv("darkMuted", "lightMuted"),
    "background": dv("darkBg", "lightBg"),
    "backgroundPanel": dv("darkPanel", "lightPanel"),
    "backgroundElement": dv("darkElement", "lightElement"),
    "border": dv("darkMuted", "lightMuted"),
    "borderActive": dv("darkCyan", "lightCyan"),
    "borderSubtle": dv("darkMuted", "lightMuted"),
    "diffAdded": dv("darkGreen", "lightGreen"),
    "diffRemoved": dv("darkRed", "lightRed"),
    "diffContext": dv("darkFg", "lightFg"),
    "diffHunkHeader": dv("darkMuted", "lightMuted"),
    "diffHighlightAdded": dv("#a8e8b0", "#5fb87a"),
    "diffHighlightRemoved": dv("#fca0b0", "#d4557a"),
    "diffAddedBg": dv("#221a2a", "#e8f5e9"),
    "diffRemovedBg": dv("#2a1a22", "#fce4ec"),
    "diffContextBg": dv("darkPanel", "lightPanel"),
    "diffLineNumber": dv("darkMuted", "lightMuted"),
    "diffAddedLineNumberBg": dv("#1d1525", "#d0e8d4"),
    "diffRemovedLineNumberBg": dv("#251520", "#f0d4d8"),
    "markdownText": dv("darkFg", "lightFg"),
    "markdownHeading": dv("darkCyan", "lightCyan"),
    "markdownLink": dv("darkBlue", "lightBlue"),
    "markdownLinkText": dv("darkCyan", "lightCyan"),
    "markdownCode": dv("darkGreen", "lightGreen"),
    "markdownBlockQuote": dv("darkMuted", "lightMuted"),
    "markdownEmph": dv("darkYellow", "lightYellow"),
    "markdownStrong": dv("darkYellow", "lightYellow"),
    "markdownHorizontalRule": dv("darkMuted", "lightMuted"),
    "markdownListItem": dv("darkCyan", "lightCyan"),
    "markdownListEnumeration": dv("darkCyan", "lightCyan"),
    "markdownImage": dv("darkBlue", "lightBlue"),
    "markdownImageText": dv("darkCyan", "lightCyan"),
    "markdownCodeBlock": dv("darkFg", "lightFg"),
    "syntaxComment": dv("darkMuted", "lightMuted"),
    "syntaxKeyword": dv("darkPurple", "lightPurple"),
    "syntaxFunction": dv("darkCyan", "lightCyan"),
    "syntaxVariable": dv("darkBlue", "lightBlue"),
    "syntaxString": dv("darkGreen", "lightGreen"),
    "syntaxNumber": dv("darkYellow", "lightYellow"),
    "syntaxType": dv("darkBlue", "lightBlue"),
    "syntaxOperator": dv("darkRed", "lightRed"),
    "syntaxPunctuation": dv("darkFg", "lightFg"),
})

# Tokio
register("tokio", {
    "darkBg": "#363537", "darkPanel": "#4a484c", "darkElement": "#424043",
    "darkFg": "#f7f1ff", "darkMuted": "#69676c",
    "darkRed": "#fc618d", "darkGreen": "#7bd88f", "darkYellow": "#fce566",
    "darkOrange": "#fd9353", "darkPurple": "#948ae3", "darkCyan": "#5ad4e6",
    "lightBg": "#f7f1ff", "lightPanel": "#e8e0f0", "lightElement": "#f0e8f8",
    "lightFg": "#363537", "lightMuted": "#8a8890",
    "lightRed": "#d4557a", "lightGreen": "#5fb87a", "lightYellow": "#d4b84a",
    "lightOrange": "#d47a42", "lightPurple": "#7a70c4", "lightCyan": "#4ab8cc",
}, {
    "primary": dv("darkCyan", "lightCyan"),
    "secondary": dv("darkPurple", "lightPurple"),
    "accent": dv("darkCyan", "lightCyan"),
    "error": dv("darkRed", "lightRed"),
    "warning": dv("darkYellow", "lightYellow"),
    "success": dv("darkGreen", "lightGreen"),
    "info": dv("darkCyan", "lightCyan"),
    "text": dv("darkFg", "lightFg"),
    "textMuted": dv("darkMuted", "lightMuted"),
    "background": dv("darkBg", "lightBg"),
    "backgroundPanel": dv("darkPanel", "lightPanel"),
    "backgroundElement": dv("darkElement", "lightElement"),
    "border": dv("darkMuted", "lightMuted"),
    "borderActive": dv("darkCyan", "lightCyan"),
    "borderSubtle": dv("darkMuted", "lightMuted"),
    "diffAdded": dv("darkGreen", "lightGreen"),
    "diffRemoved": dv("darkRed", "lightRed"),
    "diffContext": dv("darkFg", "lightFg"),
    "diffHunkHeader": dv("darkMuted", "lightMuted"),
    "diffHighlightAdded": dv("#a8e8b0", "#5fb87a"),
    "diffHighlightRemoved": dv("#fca0b0", "#d4557a"),
    "diffAddedBg": dv("#2a2a2a", "#e8f5e9"),
    "diffRemovedBg": dv("#2a2020", "#fce4ec"),
    "diffContextBg": dv("darkPanel", "lightPanel"),
    "diffLineNumber": dv("darkMuted", "lightMuted"),
    "diffAddedLineNumberBg": dv("#252525", "#d0e8d4"),
    "diffRemovedLineNumberBg": dv("#252020", "#f0d4d8"),
    "markdownText": dv("darkFg", "lightFg"),
    "markdownHeading": dv("darkCyan", "lightCyan"),
    "markdownLink": dv("darkOrange", "lightOrange"),
    "markdownLinkText": dv("darkCyan", "lightCyan"),
    "markdownCode": dv("darkGreen", "lightGreen"),
    "markdownBlockQuote": dv("darkMuted", "lightMuted"),
    "markdownEmph": dv("darkYellow", "lightYellow"),
    "markdownStrong": dv("darkYellow", "lightYellow"),
    "markdownHorizontalRule": dv("darkMuted", "lightMuted"),
    "markdownListItem": dv("darkCyan", "lightCyan"),
    "markdownListEnumeration": dv("darkCyan", "lightCyan"),
    "markdownImage": dv("darkOrange", "lightOrange"),
    "markdownImageText": dv("darkCyan", "lightCyan"),
    "markdownCodeBlock": dv("darkFg", "lightFg"),
    "syntaxComment": dv("darkMuted", "lightMuted"),
    "syntaxKeyword": dv("darkPurple", "lightPurple"),
    "syntaxFunction": dv("darkCyan", "lightCyan"),
    "syntaxVariable": dv("darkOrange", "lightOrange"),
    "syntaxString": dv("darkGreen", "lightGreen"),
    "syntaxNumber": dv("darkYellow", "lightYellow"),
    "syntaxType": dv("darkOrange", "lightOrange"),
    "syntaxOperator": dv("darkRed", "lightRed"),
    "syntaxPunctuation": dv("darkFg", "lightFg"),
})

# Oslo
register("oslo", {
    "darkBg": "#3f4451", "darkPanel": "#4f5666", "darkElement": "#474d5c",
    "darkFg": "#e6e6e6", "darkMuted": "#4f5666",
    "darkRed": "#e05561", "darkGreen": "#8cc265", "darkYellow": "#d18f52",
    "darkBlue": "#4aa5f0", "darkPurple": "#c162de", "darkCyan": "#42b3c2",
    "lightBg": "#e6e6e6", "lightPanel": "#d4d8dc", "lightElement": "#dde0e4",
    "lightFg": "#3f4451", "lightMuted": "#8a8f9a",
    "lightRed": "#c04850", "lightGreen": "#70a850", "lightYellow": "#b07840",
    "lightBlue": "#4088c4", "lightPurple": "#a050b8", "lightCyan": "#3890a0",
}, {
    "primary": dv("darkBlue", "lightBlue"),
    "secondary": dv("darkPurple", "lightPurple"),
    "accent": dv("darkCyan", "lightCyan"),
    "error": dv("darkRed", "lightRed"),
    "warning": dv("darkYellow", "lightYellow"),
    "success": dv("darkGreen", "lightGreen"),
    "info": dv("darkCyan", "lightCyan"),
    "text": dv("darkFg", "lightFg"),
    "textMuted": dv("darkMuted", "lightMuted"),
    "background": dv("darkBg", "lightBg"),
    "backgroundPanel": dv("darkPanel", "lightPanel"),
    "backgroundElement": dv("darkElement", "lightElement"),
    "border": dv("darkMuted", "lightMuted"),
    "borderActive": dv("darkBlue", "lightBlue"),
    "borderSubtle": dv("darkMuted", "lightMuted"),
    "diffAdded": dv("darkGreen", "lightGreen"),
    "diffRemoved": dv("darkRed", "lightRed"),
    "diffContext": dv("darkFg", "lightFg"),
    "diffHunkHeader": dv("darkMuted", "lightMuted"),
    "diffHighlightAdded": dv("#b0d890", "#70a850"),
    "diffHighlightRemoved": dv("#e88890", "#c04850"),
    "diffAddedBg": dv("#2a3028", "#e8f0e4"),
    "diffRemovedBg": dv("#30202a", "#fce8e8"),
    "diffContextBg": dv("darkPanel", "lightPanel"),
    "diffLineNumber": dv("darkMuted", "lightMuted"),
    "diffAddedLineNumberBg": dv("#252a24", "#d8e4d4"),
    "diffRemovedLineNumberBg": dv("#2a2025", "#f0dce0"),
    "markdownText": dv("darkFg", "lightFg"),
    "markdownHeading": dv("darkBlue", "lightBlue"),
    "markdownLink": dv("darkBlue", "lightBlue"),
    "markdownLinkText": dv("darkCyan", "lightCyan"),
    "markdownCode": dv("darkGreen", "lightGreen"),
    "markdownBlockQuote": dv("darkMuted", "lightMuted"),
    "markdownEmph": dv("darkYellow", "lightYellow"),
    "markdownStrong": dv("darkYellow", "lightYellow"),
    "markdownHorizontalRule": dv("darkMuted", "lightMuted"),
    "markdownListItem": dv("darkCyan", "lightCyan"),
    "markdownListEnumeration": dv("darkCyan", "lightCyan"),
    "markdownImage": dv("darkBlue", "lightBlue"),
    "markdownImageText": dv("darkCyan", "lightCyan"),
    "markdownCodeBlock": dv("darkFg", "lightFg"),
    "syntaxComment": dv("darkMuted", "lightMuted"),
    "syntaxKeyword": dv("darkPurple", "lightPurple"),
    "syntaxFunction": dv("darkBlue", "lightBlue"),
    "syntaxVariable": dv("darkBlue", "lightBlue"),
    "syntaxString": dv("darkGreen", "lightGreen"),
    "syntaxNumber": dv("darkYellow", "lightYellow"),
    "syntaxType": dv("darkBlue", "lightBlue"),
    "syntaxOperator": dv("darkRed", "lightRed"),
    "syntaxPunctuation": dv("darkFg", "lightFg"),
})

# Helsinki
register("helsinki", {
    "darkBg": "#3a3835", "darkPanel": "#4a4845", "darkElement": "#42403d",
    "darkFg": "#f8fafe", "darkMuted": "#8a8780",
    "darkTeal": "#009e91", "darkPurple": "#5a1f8a", "darkBlue": "#0f5ba2",
    "darkOrange": "#b23b00", "darkGreen": "#218c00", "darkRed": "#b32e1f",
    "lightBg": "#f8fafe", "lightPanel": "#e8ecf0", "lightElement": "#f0f2f6",
    "lightFg": "#544d40", "lightMuted": "#b0a999",
    "lightTeal": "#1faa9e", "lightPurple": "#733d9a", "lightBlue": "#2e70ad",
    "lightOrange": "#b55a0f", "lightGreen": "#3e9d21", "lightRed": "#bd4c3d",
}, {
    "primary": dv("darkTeal", "lightTeal"),
    "secondary": dv("darkPurple", "lightPurple"),
    "accent": dv("darkTeal", "lightTeal"),
    "error": dv("darkRed", "lightRed"),
    "warning": dv("darkOrange", "lightOrange"),
    "success": dv("darkGreen", "lightGreen"),
    "info": dv("darkBlue", "lightBlue"),
    "text": dv("darkFg", "lightFg"),
    "textMuted": dv("darkMuted", "lightMuted"),
    "background": dv("darkBg", "lightBg"),
    "backgroundPanel": dv("darkPanel", "lightPanel"),
    "backgroundElement": dv("darkElement", "lightElement"),
    "border": dv("darkMuted", "#c0baab"),
    "borderActive": dv("darkTeal", "lightTeal"),
    "borderSubtle": dv("darkMuted", "#c0baab"),
    "diffAdded": dv("darkGreen", "lightGreen"),
    "diffRemoved": dv("darkRed", "lightRed"),
    "diffContext": dv("darkFg", "lightFg"),
    "diffHunkHeader": dv("darkMuted", "lightMuted"),
    "diffHighlightAdded": dv("#60c050", "#3e9d21"),
    "diffHighlightRemoved": dv("#d06050", "#bd4c3d"),
    "diffAddedBg": dv("#2a3a28", "#e8f5e9"),
    "diffRemovedBg": dv("#3a2a28", "#ffebee"),
    "diffContextBg": dv("darkPanel", "lightPanel"),
    "diffLineNumber": dv("darkMuted", "lightMuted"),
    "diffAddedLineNumberBg": dv("#253523", "#d0e8d4"),
    "diffRemovedLineNumberBg": dv("#352523", "#f0d4d8"),
    "markdownText": dv("darkFg", "lightFg"),
    "markdownHeading": dv("darkTeal", "lightTeal"),
    "markdownLink": dv("darkBlue", "lightBlue"),
    "markdownLinkText": dv("darkTeal", "lightTeal"),
    "markdownCode": dv("darkGreen", "lightGreen"),
    "markdownBlockQuote": dv("darkMuted", "lightMuted"),
    "markdownEmph": dv("darkOrange", "lightOrange"),
    "markdownStrong": dv("darkOrange", "lightOrange"),
    "markdownHorizontalRule": dv("darkMuted", "lightMuted"),
    "markdownListItem": dv("darkTeal", "lightTeal"),
    "markdownListEnumeration": dv("darkTeal", "lightTeal"),
    "markdownImage": dv("darkBlue", "lightBlue"),
    "markdownImageText": dv("darkTeal", "lightTeal"),
    "markdownCodeBlock": dv("darkFg", "lightFg"),
    "syntaxComment": dv("darkMuted", "lightMuted"),
    "syntaxKeyword": dv("darkPurple", "lightPurple"),
    "syntaxFunction": dv("darkTeal", "lightTeal"),
    "syntaxVariable": dv("darkBlue", "lightBlue"),
    "syntaxString": dv("darkGreen", "lightGreen"),
    "syntaxNumber": dv("darkOrange", "lightOrange"),
    "syntaxType": dv("darkBlue", "lightBlue"),
    "syntaxOperator": dv("darkRed", "lightRed"),
    "syntaxPunctuation": dv("darkFg", "lightFg"),
})

# Berlin
register("berlin", {
    "darkBg": "#000000", "darkPanel": "#1a1a1a", "darkElement": "#111111",
    "darkFg": "#ffffff", "darkMuted": "#333333",
    "darkRed": "#999999", "darkGreen": "#bbbbbb", "darkYellow": "#dddddd",
    "darkBlue": "#888888", "darkPurple": "#aaaaaa", "darkCyan": "#cccccc",
    "lightBg": "#f5f5f5", "lightPanel": "#e8e8e8", "lightElement": "#eeeeee",
    "lightFg": "#1a1a1a", "lightMuted": "#888888",
    "lightRed": "#777777", "lightGreen": "#666666", "lightYellow": "#555555",
    "lightBlue": "#999999", "lightPurple": "#888888", "lightCyan": "#777777",
}, {
    "primary": dv("darkCyan", "lightCyan"),
    "secondary": dv("darkPurple", "lightPurple"),
    "accent": dv("darkCyan", "lightCyan"),
    "error": dv("darkRed", "lightRed"),
    "warning": dv("darkYellow", "lightYellow"),
    "success": dv("darkGreen", "lightGreen"),
    "info": dv("darkCyan", "lightCyan"),
    "text": dv("darkFg", "lightFg"),
    "textMuted": dv("darkMuted", "lightMuted"),
    "background": dv("darkBg", "lightBg"),
    "backgroundPanel": dv("darkPanel", "lightPanel"),
    "backgroundElement": dv("darkElement", "lightElement"),
    "border": dv("darkMuted", "lightMuted"),
    "borderActive": dv("darkCyan", "lightCyan"),
    "borderSubtle": dv("#555555", "#cccccc"),
    "diffAdded": dv("darkGreen", "lightGreen"),
    "diffRemoved": dv("darkRed", "lightRed"),
    "diffContext": dv("darkFg", "lightFg"),
    "diffHunkHeader": dv("darkMuted", "lightMuted"),
    "diffHighlightAdded": dv("#d0d0d0", "#666666"),
    "diffHighlightRemoved": dv("#b0b0b0", "#777777"),
    "diffAddedBg": dv("#1a1a1a", "#e8f5e9"),
    "diffRemovedBg": dv("#1a1a1a", "#fce4ec"),
    "diffContextBg": dv("darkPanel", "lightPanel"),
    "diffLineNumber": dv("darkMuted", "lightMuted"),
    "diffAddedLineNumberBg": dv("#1a1a1a", "#d0e8d4"),
    "diffRemovedLineNumberBg": dv("#1a1a1a", "#f0d4d8"),
    "markdownText": dv("darkFg", "lightFg"),
    "markdownHeading": dv("darkCyan", "lightCyan"),
    "markdownLink": dv("darkBlue", "lightBlue"),
    "markdownLinkText": dv("darkCyan", "lightCyan"),
    "markdownCode": dv("darkGreen", "lightGreen"),
    "markdownBlockQuote": dv("darkMuted", "lightMuted"),
    "markdownEmph": dv("darkYellow", "lightYellow"),
    "markdownStrong": dv("darkYellow", "lightYellow"),
    "markdownHorizontalRule": dv("darkMuted", "lightMuted"),
    "markdownListItem": dv("darkCyan", "lightCyan"),
    "markdownListEnumeration": dv("darkCyan", "lightCyan"),
    "markdownImage": dv("darkBlue", "lightBlue"),
    "markdownImageText": dv("darkCyan", "lightCyan"),
    "markdownCodeBlock": dv("darkFg", "lightFg"),
    "syntaxComment": dv("darkMuted", "lightMuted"),
    "syntaxKeyword": dv("darkPurple", "lightPurple"),
    "syntaxFunction": dv("darkCyan", "lightCyan"),
    "syntaxVariable": dv("darkBlue", "lightBlue"),
    "syntaxString": dv("darkGreen", "lightGreen"),
    "syntaxNumber": dv("darkYellow", "lightYellow"),
    "syntaxType": dv("darkBlue", "lightBlue"),
    "syntaxOperator": dv("darkRed", "lightRed"),
    "syntaxPunctuation": dv("darkFg", "lightFg"),
})

# London
register("london", {
    "darkBg": "#333333", "darkPanel": "#444444", "darkElement": "#3a3a3a",
    "darkFg": "#ffffff", "darkMuted": "#888888",
    "darkRed": "#444444", "darkGreen": "#555555", "darkYellow": "#666666",
    "darkBlue": "#777777", "darkPurple": "#888888", "darkCyan": "#999999",
    "lightBg": "#ffffff", "lightPanel": "#f0f0f0", "lightElement": "#f8f8f8",
    "lightFg": "#1a1a1a", "lightMuted": "#999999",
    "lightRed": "#333333", "lightGreen": "#444444", "lightYellow": "#555555",
    "lightBlue": "#666666", "lightPurple": "#777777", "lightCyan": "#888888",
}, {
    "primary": dv("darkCyan", "lightCyan"),
    "secondary": dv("darkPurple", "lightPurple"),
    "accent": dv("darkCyan", "lightCyan"),
    "error": dv("darkRed", "lightRed"),
    "warning": dv("darkYellow", "lightYellow"),
    "success": dv("darkGreen", "lightGreen"),
    "info": dv("darkCyan", "lightCyan"),
    "text": dv("darkFg", "lightFg"),
    "textMuted": dv("darkMuted", "lightMuted"),
    "background": dv("darkBg", "lightBg"),
    "backgroundPanel": dv("darkPanel", "lightPanel"),
    "backgroundElement": dv("darkElement", "lightElement"),
    "border": dv("darkMuted", "#dddddd"),
    "borderActive": dv("darkCyan", "lightCyan"),
    "borderSubtle": dv("darkMuted", "#dddddd"),
    "diffAdded": dv("darkGreen", "lightGreen"),
    "diffRemoved": dv("darkRed", "lightRed"),
    "diffContext": dv("darkFg", "lightFg"),
    "diffHunkHeader": dv("darkMuted", "lightMuted"),
    "diffHighlightAdded": dv("#888888", "#444444"),
    "diffHighlightRemoved": dv("#777777", "#333333"),
    "diffAddedBg": dv("#3a3a3a", "#f0f0f0"),
    "diffRemovedBg": dv("#3a3a3a", "#f0f0f0"),
    "diffContextBg": dv("darkPanel", "lightPanel"),
    "diffLineNumber": dv("darkMuted", "lightMuted"),
    "diffAddedLineNumberBg": dv("#3a3a3a", "#e8e8e8"),
    "diffRemovedLineNumberBg": dv("#3a3a3a", "#e8e8e8"),
    "markdownText": dv("darkFg", "lightFg"),
    "markdownHeading": dv("darkCyan", "lightCyan"),
    "markdownLink": dv("darkBlue", "lightBlue"),
    "markdownLinkText": dv("darkCyan", "lightCyan"),
    "markdownCode": dv("darkGreen", "lightGreen"),
    "markdownBlockQuote": dv("darkMuted", "lightMuted"),
    "markdownEmph": dv("darkYellow", "lightYellow"),
    "markdownStrong": dv("darkYellow", "lightYellow"),
    "markdownHorizontalRule": dv("darkMuted", "lightMuted"),
    "markdownListItem": dv("darkCyan", "lightCyan"),
    "markdownListEnumeration": dv("darkCyan", "lightCyan"),
    "markdownImage": dv("darkBlue", "lightBlue"),
    "markdownImageText": dv("darkCyan", "lightCyan"),
    "markdownCodeBlock": dv("darkFg", "lightFg"),
    "syntaxComment": dv("darkMuted", "lightMuted"),
    "syntaxKeyword": dv("darkPurple", "lightPurple"),
    "syntaxFunction": dv("darkCyan", "lightCyan"),
    "syntaxVariable": dv("darkBlue", "lightBlue"),
    "syntaxString": dv("darkGreen", "lightGreen"),
    "syntaxNumber": dv("darkYellow", "lightYellow"),
    "syntaxType": dv("darkBlue", "lightBlue"),
    "syntaxOperator": dv("darkRed", "lightRed"),
    "syntaxPunctuation": dv("darkFg", "lightFg"),
})

# Praha
register("praha", {
    "darkBg": "#1A1A1A", "darkPanel": "#2d2d2d", "darkElement": "#242424",
    "darkFg": "#FFFFFF", "darkMuted": "#6272A4",
    "darkRed": "#FF5555", "darkGreen": "#B8E6A0", "darkYellow": "#FFE4A3",
    "darkPurple": "#BD93F9", "darkPink": "#FF9AA2", "darkCyan": "#8BE9FD",
    "lightBg": "#f5f5f5", "lightPanel": "#e8e8e8", "lightElement": "#eeeeee",
    "lightFg": "#1a1a1a", "lightMuted": "#8a9ab8",
    "lightRed": "#d44040", "lightGreen": "#90c080", "lightYellow": "#d4b880",
    "lightPurple": "#9478c4", "lightPink": "#c47880", "lightCyan": "#70c0d4",
}, {
    "primary": dv("darkCyan", "lightCyan"),
    "secondary": dv("darkPurple", "lightPurple"),
    "accent": dv("darkCyan", "lightCyan"),
    "error": dv("darkRed", "lightRed"),
    "warning": dv("darkYellow", "lightYellow"),
    "success": dv("darkGreen", "lightGreen"),
    "info": dv("darkCyan", "lightCyan"),
    "text": dv("darkFg", "lightFg"),
    "textMuted": dv("darkMuted", "lightMuted"),
    "background": dv("darkBg", "lightBg"),
    "backgroundPanel": dv("darkPanel", "lightPanel"),
    "backgroundElement": dv("darkElement", "lightElement"),
    "border": dv("darkMuted", "lightMuted"),
    "borderActive": dv("darkCyan", "lightCyan"),
    "borderSubtle": dv("darkMuted", "lightMuted"),
    "diffAdded": dv("darkGreen", "lightGreen"),
    "diffRemoved": dv("darkRed", "lightRed"),
    "diffContext": dv("darkFg", "lightFg"),
    "diffHunkHeader": dv("darkMuted", "lightMuted"),
    "diffHighlightAdded": dv("#c8e8b8", "#90c080"),
    "diffHighlightRemoved": dv("#ff8888", "#d44040"),
    "diffAddedBg": dv("#2a2a1a", "#e8f5e9"),
    "diffRemovedBg": dv("#2a1a1a", "#fce4ec"),
    "diffContextBg": dv("darkPanel", "lightPanel"),
    "diffLineNumber": dv("darkMuted", "lightMuted"),
    "diffAddedLineNumberBg": dv("#252515", "#d0e8d4"),
    "diffRemovedLineNumberBg": dv("#251515", "#f0d4d8"),
    "markdownText": dv("darkFg", "lightFg"),
    "markdownHeading": dv("darkCyan", "lightCyan"),
    "markdownLink": dv("darkPurple", "lightPurple"),
    "markdownLinkText": dv("darkCyan", "lightCyan"),
    "markdownCode": dv("darkGreen", "lightGreen"),
    "markdownBlockQuote": dv("darkMuted", "lightMuted"),
    "markdownEmph": dv("darkYellow", "lightYellow"),
    "markdownStrong": dv("darkYellow", "lightYellow"),
    "markdownHorizontalRule": dv("darkMuted", "lightMuted"),
    "markdownListItem": dv("darkCyan", "lightCyan"),
    "markdownListEnumeration": dv("darkCyan", "lightCyan"),
    "markdownImage": dv("darkPurple", "lightPurple"),
    "markdownImageText": dv("darkCyan", "lightCyan"),
    "markdownCodeBlock": dv("darkFg", "lightFg"),
    "syntaxComment": dv("darkMuted", "lightMuted"),
    "syntaxKeyword": dv("darkPurple", "lightPurple"),
    "syntaxFunction": dv("darkCyan", "lightCyan"),
    "syntaxVariable": dv("darkPurple", "lightPurple"),
    "syntaxString": dv("darkGreen", "lightGreen"),
    "syntaxNumber": dv("darkYellow", "lightYellow"),
    "syntaxType": dv("darkPurple", "lightPurple"),
    "syntaxOperator": dv("darkRed", "lightRed"),
    "syntaxPunctuation": dv("darkFg", "lightFg"),
})

# Bogota
register("bogota", {
    "darkBg": "#140606", "darkPanel": "#2a1010", "darkElement": "#1f0c0c",
    "darkFg": "#f7f1ff", "darkMuted": "#525053",
    "darkRed": "#fc618d", "darkGreen": "#7bd88f", "darkYellow": "#ffed89",
    "darkBlue": "#47e6ff", "darkPink": "#ff9999", "darkCyan": "#47e6ff",
    "lightBg": "#f7f1ff", "lightPanel": "#e8e0f0", "lightElement": "#f0e8f8",
    "lightFg": "#1a0a0a", "lightMuted": "#8a8890",
    "lightRed": "#d4557a", "lightGreen": "#5fb87a", "lightYellow": "#d4c070",
    "lightBlue": "#40b8cc", "lightPink": "#c47878", "lightCyan": "#40b8cc",
}, {
    "primary": dv("darkCyan", "lightCyan"),
    "secondary": dv("darkPink", "lightPink"),
    "accent": dv("darkCyan", "lightCyan"),
    "error": dv("darkRed", "lightRed"),
    "warning": dv("darkYellow", "lightYellow"),
    "success": dv("darkGreen", "lightGreen"),
    "info": dv("darkCyan", "lightCyan"),
    "text": dv("darkFg", "lightFg"),
    "textMuted": dv("darkMuted", "lightMuted"),
    "background": dv("darkBg", "lightBg"),
    "backgroundPanel": dv("darkPanel", "lightPanel"),
    "backgroundElement": dv("darkElement", "lightElement"),
    "border": dv("darkMuted", "lightMuted"),
    "borderActive": dv("darkCyan", "lightCyan"),
    "borderSubtle": dv("darkMuted", "lightMuted"),
    "diffAdded": dv("darkGreen", "lightGreen"),
    "diffRemoved": dv("darkRed", "lightRed"),
    "diffContext": dv("darkFg", "lightFg"),
    "diffHunkHeader": dv("darkMuted", "lightMuted"),
    "diffHighlightAdded": dv("#a8e8b0", "#5fb87a"),
    "diffHighlightRemoved": dv("#fca0b0", "#d4557a"),
    "diffAddedBg": dv("#2a1a1a", "#e8f5e9"),
    "diffRemovedBg": dv("#2a1010", "#fce4ec"),
    "diffContextBg": dv("darkPanel", "lightPanel"),
    "diffLineNumber": dv("darkMuted", "lightMuted"),
    "diffAddedLineNumberBg": dv("#251515", "#d0e8d4"),
    "diffRemovedLineNumberBg": dv("#250e0e", "#f0d4d8"),
    "markdownText": dv("darkFg", "lightFg"),
    "markdownHeading": dv("darkCyan", "lightCyan"),
    "markdownLink": dv("darkBlue", "lightBlue"),
    "markdownLinkText": dv("darkCyan", "lightCyan"),
    "markdownCode": dv("darkGreen", "lightGreen"),
    "markdownBlockQuote": dv("darkMuted", "lightMuted"),
    "markdownEmph": dv("darkYellow", "lightYellow"),
    "markdownStrong": dv("darkYellow", "lightYellow"),
    "markdownHorizontalRule": dv("darkMuted", "lightMuted"),
    "markdownListItem": dv("darkCyan", "lightCyan"),
    "markdownListEnumeration": dv("darkCyan", "lightCyan"),
    "markdownImage": dv("darkBlue", "lightBlue"),
    "markdownImageText": dv("darkCyan", "lightCyan"),
    "markdownCodeBlock": dv("darkFg", "lightFg"),
    "syntaxComment": dv("darkMuted", "lightMuted"),
    "syntaxKeyword": dv("darkPink", "lightPink"),
    "syntaxFunction": dv("darkCyan", "lightCyan"),
    "syntaxVariable": dv("darkBlue", "lightBlue"),
    "syntaxString": dv("darkGreen", "lightGreen"),
    "syntaxNumber": dv("darkYellow", "lightYellow"),
    "syntaxType": dv("darkBlue", "lightBlue"),
    "syntaxOperator": dv("darkRed", "lightRed"),
    "syntaxPunctuation": dv("darkFg", "lightFg"),
})


# ─── colors.md parser ───────────────────────────────────────────────────

def hex_blend(h1, h2, ratio):
    """Blend two hex colors. ratio=0 -> h1, ratio=1 -> h2."""
    r1, g1, b1 = int(h1[1:3], 16), int(h1[3:5], 16), int(h1[5:7], 16)
    r2, g2, b2 = int(h2[1:3], 16), int(h2[3:5], 16), int(h2[5:7], 16)
    r = int(r1 + (r2 - r1) * ratio)
    g = int(g1 + (g2 - g1) * ratio)
    b = int(b1 + (b2 - b1) * ratio)
    return f"#{r:02x}{g:02x}{b:02x}"

def is_dark_scheme(colors):
    """Heuristic: check if color0 (bg) is darker than color7 (fg)."""
    bg = colors.get("color0", "#000000")
    fg = colors.get("color7", "#ffffff")
    lum = lambda h: 0.299 * int(h[1:3], 16) + 0.587 * int(h[3:5], 16) + 0.114 * int(h[5:7], 16)
    return lum(bg) < lum(fg)

def parse_colors_md(filepath):
    """Parse colors.md and return a dict of {name: {color0..color15}}."""
    with open(filepath) as f:
        text = f.read()

    themes = {}
    # Match sections: <h2...>Name</h2> ... ```json ... ```
    pattern = re.compile(
        r'<h2[^>]*>(.*?)</h2>\s*```json\s*\n(.*?)```',
        re.DOTALL
    )
    for match in pattern.finditer(text):
        name = match.group(1).strip()
        raw = match.group(2).strip()
        try:
            colors = json.loads(raw)
        except json.JSONDecodeError:
            continue
        # Validate
        if all(f"color{i}" in colors for i in range(16)):
            themes[name] = colors
    return themes

def ansi_to_opencode(name, ansi):
    """Convert ANSI color dict to opencode theme data."""
    c = [ansi[f"color{i}"] for i in range(16)]
    bg, fg = c[0], c[7]
    muted = c[8]
    dark = is_dark_scheme(ansi)

    # Generate light variant by swapping bg/fg
    if dark:
        light_bg = fg
        light_fg = bg
        light_muted = hex_blend(fg, bg, 0.4)
        light_panel = hex_blend(fg, bg, 0.15)
        light_element = hex_blend(fg, bg, 0.08)
    else:
        light_bg = bg
        light_fg = fg
        light_muted = muted
        light_panel = hex_blend(bg, fg, 0.1)
        light_element = hex_blend(bg, fg, 0.05)
        # Swap: original is light, generate dark variant
        dark_bg = fg
        dark_fg = bg
        dark_muted = hex_blend(fg, bg, 0.5)
        dark_panel = hex_blend(fg, bg, 0.85)
        dark_element = hex_blend(fg, bg, 0.92)
    # end variant generation

    # Map ANSI indices to semantic roles
    ansi_red = c[1]
    ansi_green = c[2]
    ansi_yellow = c[3]
    ansi_blue = c[4]
    ansi_magenta = c[5]
    ansi_cyan = c[6]

    # For dark schemes
    if dark:
        d_bg, d_fg = bg, fg
        d_muted = muted
        d_panel = hex_blend(bg, fg, 0.12)
        d_element = hex_blend(bg, fg, 0.06)
        l_bg, l_fg = light_bg, light_fg
        l_muted = light_muted
        l_panel = light_panel
        l_element = light_element
    else:
        d_bg, d_fg = dark_bg, dark_fg
        d_muted = dark_muted
        d_panel = dark_panel
        d_element = dark_element
        l_bg, l_fg = light_bg, light_fg
        l_muted = light_muted
        l_panel = light_panel
        l_element = light_element

    defs_data = {
        "darkBg": d_bg, "darkPanel": d_panel, "darkElement": d_element,
        "darkFg": d_fg, "darkMuted": d_muted,
        "darkRed": ansi_red, "darkGreen": ansi_green, "darkYellow": ansi_yellow,
        "darkBlue": ansi_blue, "darkPurple": ansi_magenta, "darkCyan": ansi_cyan,
        "lightBg": l_bg, "lightPanel": l_panel, "lightElement": l_element,
        "lightFg": l_fg, "lightMuted": l_muted,
        "lightRed": ansi_red, "lightGreen": ansi_green, "lightYellow": ansi_yellow,
        "lightBlue": ansi_blue, "lightPurple": ansi_magenta, "lightCyan": ansi_cyan,
    }

    theme_data = {
        "primary": dv("darkCyan", "lightCyan"),
        "secondary": dv("darkPurple", "lightPurple"),
        "accent": dv("darkCyan", "lightCyan"),
        "error": dv("darkRed", "lightRed"),
        "warning": dv("darkYellow", "lightYellow"),
        "success": dv("darkGreen", "lightGreen"),
        "info": dv("darkCyan", "lightCyan"),
        "text": dv("darkFg", "lightFg"),
        "textMuted": dv("darkMuted", "lightMuted"),
        "background": dv("darkBg", "lightBg"),
        "backgroundPanel": dv("darkPanel", "lightPanel"),
        "backgroundElement": dv("darkElement", "lightElement"),
        "border": dv("darkMuted", "lightMuted"),
        "borderActive": dv("darkCyan", "lightCyan"),
        "borderSubtle": dv("darkMuted", "lightMuted"),
        "diffAdded": dv("darkGreen", "lightGreen"),
        "diffRemoved": dv("darkRed", "lightRed"),
        "diffContext": dv("darkFg", "lightFg"),
        "diffHunkHeader": dv("darkMuted", "lightMuted"),
        "diffHighlightAdded": dv("#a8e8b0", "#5fb87a"),
        "diffHighlightRemoved": dv("#fca0b0", "#d4557a"),
        "diffAddedBg": dv("#1a2a1a", "#e8f5e9"),
        "diffRemovedBg": dv("#2a1a1a", "#fce4ec"),
        "diffContextBg": dv("darkPanel", "lightPanel"),
        "diffLineNumber": dv("darkMuted", "lightMuted"),
        "diffAddedLineNumberBg": dv("#152215", "#d0e8d4"),
        "diffRemovedLineNumberBg": dv("#221515", "#f0d4d8"),
        "markdownText": dv("darkFg", "lightFg"),
        "markdownHeading": dv("darkCyan", "lightCyan"),
        "markdownLink": dv("darkBlue", "lightBlue"),
        "markdownLinkText": dv("darkCyan", "lightCyan"),
        "markdownCode": dv("darkGreen", "lightGreen"),
        "markdownBlockQuote": dv("darkMuted", "lightMuted"),
        "markdownEmph": dv("darkYellow", "lightYellow"),
        "markdownStrong": dv("darkYellow", "lightYellow"),
        "markdownHorizontalRule": dv("darkMuted", "lightMuted"),
        "markdownListItem": dv("darkCyan", "lightCyan"),
        "markdownListEnumeration": dv("darkCyan", "lightCyan"),
        "markdownImage": dv("darkBlue", "lightBlue"),
        "markdownImageText": dv("darkCyan", "lightCyan"),
        "markdownCodeBlock": dv("darkFg", "lightFg"),
        "syntaxComment": dv("darkMuted", "lightMuted"),
        "syntaxKeyword": dv("darkPurple", "lightPurple"),
        "syntaxFunction": dv("darkCyan", "lightCyan"),
        "syntaxVariable": dv("darkBlue", "lightBlue"),
        "syntaxString": dv("darkGreen", "lightGreen"),
        "syntaxNumber": dv("darkYellow", "lightYellow"),
        "syntaxType": dv("darkBlue", "lightBlue"),
        "syntaxOperator": dv("darkRed", "lightRed"),
        "syntaxPunctuation": dv("darkFg", "lightFg"),
    }

    return theme(defs_data, theme_data)


# ─── main ───────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description="Generate opencode built-in theme JSON files from Xscriptor color palettes."
    )
    parser.add_argument(
        "--colors", metavar="PATH",
        help="Path to colors.md to parse theme definitions from. If omitted, uses built-in data."
    )
    parser.add_argument(
        "--output", "-o", default="dist",
        help="Output directory for generated theme files (default: dist)"
    )
    args = parser.parse_args()

    output_dir = os.path.abspath(args.output)
    ensure_dir(output_dir)

    if args.colors:
        colors_path = os.path.abspath(args.colors)
        if not os.path.isfile(colors_path):
            print(f"Error: file not found: {colors_path}", file=sys.stderr)
            sys.exit(1)
        ansi_themes = parse_colors_md(colors_path)
        if not ansi_themes:
            print("Error: no valid themes found in colors.md", file=sys.stderr)
            sys.exit(1)
        themes = {}
        for name, ansi in ansi_themes.items():
            slug = name.lower().replace(" ", "-")
            themes[slug] = ansi_to_opencode(name, ansi)
        source_note = f"Parsed {len(themes)} themes from {colors_path}"
    else:
        themes = BUILTIN_THEMES
        source_note = f"Generated {len(themes)} built-in themes"

    for name, data in themes.items():
        filename = f"{name}.json"
        filepath = os.path.join(output_dir, filename)
        with open(filepath, "w") as f:
            json.dump(data, f, indent=2)
            f.write("\n")
        print(f"  + {filename}")

    print(f"\n{source_note}")
    print(f"Output: {output_dir}/")


if __name__ == "__main__":
    main()
