import subprocess
import sys
import os



def run_modz(args):
    """
    Helper function to run MODZ as a subprocess.
    Returns: (exit_code, stdout, stderr)
    """
    result = subprocess.run(
        ["modz"] + args,
        stdout = subprocess.PIPE,
        stderr = subprocess.PIPE,
        text = True
    )
    return result.returncode, result.stdout, result.stderr


def test_version_flag():
    exit_code, stdout, stderr = run_modz(["--version"])

    assert exit_code == 0
    assert "MODZ version" in stdout
    assert stderr == ""
