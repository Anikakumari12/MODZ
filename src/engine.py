#!/usr/bin/env python3
"""
MODZ Engine
-----------
A safe command-line text manipulation tool.

Design rules:
1. Input file is NEVER modified
2. Functions ONLY transform data
3. main() decides preview vs write
"""

import sys


# ======================================================
# SAFE FILE READER
# ======================================================
# Reads input file safely.
# Exits if file does not exist or is empty.
# ======================================================

def safe_read_lines(input_path):
    try:
        with open(input_path, "r", encoding="utf-8") as f:
            lines = f.readlines()
    except FileNotFoundError:
        print(f"[MODZ] File not found: {input_path}")
        sys.exit(1)

    if not lines:
        print("[MODZ] Input file is empty.")
        sys.exit(1)

    return lines


# ======================================================
# DELETE CONTAINS
# ======================================================
# Removes lines containing a keyword
# ======================================================

def delete_contains(keyword, input_path):
    lines = safe_read_lines(input_path)
    return [line for line in lines if keyword not in line]


# ======================================================
# DELETE SINGLE LINE
# ======================================================
# Deletes a specific line number (1-based)
# ======================================================

def delete_line(line_number, input_path):
    lines = safe_read_lines(input_path)

    if line_number < 1 or line_number > len(lines):
        print(f"[MODZ] Invalid line number: {line_number}")
        sys.exit(1)

    del lines[line_number - 1]
    return lines


# ======================================================
# DELETE RANGE
# ======================================================
# Deletes lines from start to end (inclusive)
# ======================================================

def delete_range(start, end, input_path):
    lines = safe_read_lines(input_path)

    if start < 1 or end < 1 or start > end:
        print("[MODZ] Invalid range.")
        sys.exit(1)

    return lines[:start - 1] + lines[end:]


# ======================================================
# REPLACE TEXT
# ======================================================
# Replaces text everywhere
# ======================================================

def replace_text(old, new, input_path):
    lines = safe_read_lines(input_path)
    return [line.replace(old, new) for line in lines]


# ======================================================
# HELP TEXT
# ======================================================

def show_help():
    print("""
MODZ — Safe Command-Line Text Editor

Usage:
  modz <command> [arguments] [--preview]

Commands:
  delete_contains <keyword> <input> <output>
  delete_line <line_number> <input> <output>
  delete_range <start> <end> <input> <output>
  replace_text <old> <new> <input> <output>

Flags:
  --preview     Show output only (do not write file)

Examples:
  modz delete_line 3 notes.txt out.txt --preview
  modz delete_range 2 5 notes.txt out.txt
  modz replace_text error warning in.txt out.txt
""")


# ======================================================
# MAIN COMMAND ROUTER
# ======================================================
# Reads CLI input
# Calls correct function
# Decides preview vs commit
# ======================================================

def main():
    # -------- GLOBAL HELP --------
    if len(sys.argv) < 2 or sys.argv[1] in ("help", "--help", "-h"):
        show_help()
        sys.exit(0)

    command = argv[1]
    preview = "--preview" in sys.argv

    # -------- COMMAND DISPATCH --------
    if command == "delete_contains":
        if len(sys.argv) < 5:
            show_help()
            sys.exit(1)

        result = delete_contains(sys.argv[2], sys.argv[3])
        output_path = sys.argv[4]

    elif command == "delete_line":
        if len(sys.argv) < 5:
            show_help()
            sys.exit(1)

        result = delete_line(int(sys.argv[2]), sys.argv[3])
        output_path = sys.argv[4]

    elif command == "delete_range":
        if len(sys.argv) < 6:
            show_help()
            sys.exit(1)

        result = delete_range(
            int(sys.argv[2]),
            int(sys.argv[3]),
            sys.argv[4]
        )
        output_path = sys.argv[5]

    elif command == "replace_text":
        if len(sys.argv) < 6:
            show_help()
            sys.exit(1)

        result = replace_text(sys.argv[2], sys.argv[3], sys.argv[4])
        output_path = sys.argv[5]

    else:
        print(f"[MODZ] Unknown command: {command}")
        show_help()
        sys.exit(1)

    # -------- PREVIEW OR COMMIT --------
    if preview:
        print("".join(result))
    else:
        with open(output_path, "w", encoding="utf-8") as f:
            f.writelines(result)
        print("[MODZ] Changes written successfully.")


# ======================================================
# ENTRY POINT
# ======================================================

if __name__ == "__main__":
    main()
