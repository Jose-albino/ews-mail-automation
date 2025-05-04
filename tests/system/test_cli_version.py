import subprocess
import sys

def test_cli_reports_correct_version(package_version):
    result = subprocess.run(
        [sys.executable, "-m", "exchange_automator", "-v"],
        capture_output=True,
        text=True
    )
    assert result.returncode == 0
    assert package_version in result.stdout.lower()
