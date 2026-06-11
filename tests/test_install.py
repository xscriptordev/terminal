"""Basic validation of install.sh."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
INSTALL_SH = ROOT / "install.sh"


def test_install_sh_exists() -> None:
    assert INSTALL_SH.exists(), "install.sh not found"


def test_install_sh_is_shell_script() -> None:
    content = INSTALL_SH.read_text()
    assert content.startswith("#!/"), "install.sh must start with shebang"


def test_install_sh_dry_run() -> None:
    result = subprocess.run(
        [sys.executable, "-c", """
import subprocess
import sys

# Basic syntax check: run with --help (POSIX sh)
result = subprocess.run(
    ["sh", "-n", str(INSTALL_SH)],
    capture_output=True, text=True, cwd=str(ROOT)
)
sys.exit(result.returncode)
""".replace("INSTALL_SH", str(INSTALL_SH)).replace("ROOT", str(ROOT))],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, f"Shell syntax check failed:\n{result.stderr}"


def test_install_sh_has_options() -> None:
    content = INSTALL_SH.read_text()
    for opt in ["--themes-only", "--minimal", "--complete", "--dry-run", "--force"]:
        assert opt in content, f"Missing option {opt} in install.sh"
