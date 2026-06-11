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
    script = (
        "import subprocess\n"
        "import sys\n"
        "result = subprocess.run(\n"
        f'    ["sh", "-n", {str(INSTALL_SH)!r}],\n'
        f"    capture_output=True, text=True, cwd={str(ROOT)!r},\n"
        ")\n"
        "sys.exit(result.returncode)\n"
    )
    result = subprocess.run(
        [sys.executable, "-c", script],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, f"Shell syntax check failed:\n{result.stderr}"


def test_install_sh_has_options() -> None:
    content = INSTALL_SH.read_text()
    for opt in ["--themes-only", "--minimal", "--complete", "--dry-run", "--force"]:
        assert opt in content, f"Missing option {opt} in install.sh"
