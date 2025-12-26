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


def test_unknown_command():
    exit_code, stdout, stderr = run_modz(["deletee_line"])

    assert exit_code != 0
    assert "Unknown command" in stderr

def test_input_file_is_not_modified(tmp_path):
    input_file = tmp_path / "input.txt"
    output_file = tmp_path / "out.txt"

    original_content = "a\nb\nc\n"
    input_file.write_text(original_content)

    run_modz([
        "delete_line", "2",
        str(input_file),
        str(output_file)
    ])

    assert input_file.read_text() == original_content

def test_preview_does_not_create_output_file(tmp_path):
    input_file = tmp_path / "input.txt"
    output_file = tmp_path / "out.txt"

    input_file.write_text("line1\nline2\nline3\n")

    exit_code, stdout, stderr = run_modz([
        "delete_line", "2",
        str(input_file),
        str(output_file),
        "--preview"
    ])

    assert exit_code == 0
    assert output_file.exists() is False


def test_invalid_usage_exit_code():
    exit_code, stdout, stderr = run_modz(["delete_line"])

    assert exit_code == 2
    
