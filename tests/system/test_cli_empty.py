import subprocess
import sys


def test_cli_empty(package_description):
    result = subprocess.run(["exchange-automator"], capture_output=True, text=True)
    assert result.returncode == 0
    assert package_description in result.stdout
