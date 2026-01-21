#!/usr/bin/env python3
"""
MODZ Engine
A safe command-line text manipulation tool.
"""

import sys
import os

# =====================================
# Tool identity
# =====================================

VERSION = "0.1.0"


# =====================================
# Help text
# =====================================

def show_help():
    print("""
MODZ — Safe Command-Line Text Editor

Usage:
  modz <command> [arguments]

Commands:
  delete_line <line_number> <input_file> <output_file>
""")


# =====================================
# Core command: delete_line
# =====================================

def delete_line(line_number, input_path, output_path):
    # Safety: input file must exist
    if not os.path.exists(input_path):
        print("[MODZ] Error: input file does not exist")
        sys.exit(1)

    # Safety: do not overwrite input file
    if input_path == output_path:
        print("[MODZ] Error: output file must be different from input file")
        sys.exit(1)

    # Read input file
    with open(input_path, "r") as f:
        lines = f.readlines()

    # Convert to 0-based index
    index = line_number - 1

    # Validate line number range
    if index < 0 or index >= len(lines):
        print("[MODZ] Error: line number out of range")
        sys.exit(1)

    # Remove the selected line
    del lines[index]

    # Write to output file
    with open(output_path, "w") as f:
        f.writelines(lines)

    print(f"[MODZ] Line {line_number} deleted successfully")


# =====================================
# Main entry point
# =====================================

def main():
    # No arguments → show help
    if len(sys.argv) < 2:
        show_help()
        sys.exit(0)

    command = sys.argv[1]

    # delete_line command
    if command == "delete_line":
        if len(sys.argv) != 5:
            print("[MODZ] Usage: modz delete_line <line_number> <input> <output>")
            sys.exit(1)

        try:
            line_number = int(sys.argv[2])
        except ValueError:
            print("[MODZ] Error: line_number must be an integer")
            sys.exit(1)

        input_file = sys.argv[3]
        output_file = sys.argv[4]

        delete_line(line_number, input_file, output_file)
        sys.exit(0)

    # Unknown command
    else:
        print(f"[MODZ] Unknown command: {command}")
        show_help()
        sys.exit(1)


# =====================================
# Safe execution guard
# =====================================

if __name__ == "__main__":
    main()