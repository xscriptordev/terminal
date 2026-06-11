"""Test the theme generator script."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
SCRIPT = ROOT / "scripts" / "generate_themes.py"
COLORS_MD = ROOT / "colors.md"


def test_generate_themes_dry_run() -> None:
    result = subprocess.run(
        [sys.executable, str(SCRIPT), "--dry-run"],
        cwd=str(ROOT),
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, f"Script failed:\n{result.stderr}"
    assert result.stdout.strip(), "Dry run produced no output"


def test_generate_themes_specific_palette() -> None:
    result = subprocess.run(
        [sys.executable, str(SCRIPT), "--dry-run", "--only", "Madrid"],
        cwd=str(ROOT),
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0
    assert "madrid.toml" in result.stdout


def test_generate_themes_missing_colors() -> None:
    result = subprocess.run(
        [sys.executable, str(SCRIPT), "--dry-run", "--only", "NonExistent"],
        cwd=str(ROOT),
        capture_output=True,
        text=True,
    )
    assert result.returncode == 1


@pytest.fixture
def temp_output(tmp_path: Path) -> Path:
    return tmp_path / "themes"


def test_generate_themes_writes_valid_toml(temp_output: Path) -> None:
    result = subprocess.run(
        [
            sys.executable, str(SCRIPT),
            "--out", str(temp_output),
            "--only", "Madrid",
        ],
        cwd=str(ROOT),
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0

    output_file = temp_output / "madrid.toml"
    assert output_file.exists()
    content = output_file.read_text()
    assert "[palette]" in content
    assert 'bg = "#fafafa"' in content


def test_generate_themes_all_palettes_valid_toml(temp_output: Path) -> None:
    result = subprocess.run(
        [sys.executable, str(SCRIPT), "--out", str(temp_output)],
        cwd=str(ROOT),
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0

    content = COLORS_MD.read_text(encoding="utf-8")
    import re
    palette_count = len(re.findall(r"<h2[^>]*>.*?</h2>\s*```json", content, re.S))
    generated = list(temp_output.glob("*.toml"))
    assert len(generated) == palette_count, (
        f"Expected {palette_count} themes, got {len(generated)}"
    )
