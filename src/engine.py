#!/usr/bin/env python3
"""
MODZ Engine
-----------
A command-based text manipulation tool.

Core rules:
- Input file is never modified
- Functions only transform data
- main() controls preview vs save
"""

import sys


# ======================================================
# SAFE FILE READER
# ======================================================
# Reads the input file safely and returns lines.
# Any file-related error exits the program cleanly.
# ======================================================

def safe_read_lines(input_path: str):
    try:
        with open(input_path, "r", encoding="UTF-8") as infile:
            lines = infile.readlines()
    except FileNotFoundError:
        print(f"[MODZ] File not found: {input_path}")
        sys.exit(1)
    except Exception as e:
        print(f"[MODZ] Failed to read file: {e}")
        sys.exit(1)

    if not lines:
        print("[MODZ] Input file is empty.")
        sys.exit(1)

    return lines


# ======================================================
# DELETE CONTAINS
# ======================================================
# Removes all lines that contain a given keyword.
# Returns modified lines only (no file writing).
# ======================================================

def delete_contains(keyword: str, input_path: str):
    lines = safe_read_lines(input_path)
    return [line for line in lines if keyword not in line]


# ======================================================
# DELETE SINGLE LINE
# ======================================================
# Deletes one specific line number (1-based index).
# Validates range and returns modified lines.
# ======================================================

def delete_line(line_number: int, input_path: str):
    lines = safe_read_lines(input_path)
    total = len(lines)

    if line_number < 1 or line_number > total:
        print(f"[MODZ] Invalid line number: {line_number}")
        print(f"[MODZ] File has {total} lines.")
        sys.exit(1)

    del lines[line_number - 1]
    return lines


# ======================================================
# DELETE RANGE
# ======================================================
# Deletes a continuous range of lines (inclusive).
# Uses slicing for clean and readable logic.
# ======================================================

def delete_range(start_line: int, end_line: int, input_path: str):
    lines = safe_read_lines(input_path)
    total = len(lines)

    if start_line < 1 or end_line < 1:
        print("[MODZ] Line numbers must be >= 1.")
        sys.exit(1)

    if start_line > end_line:
        print("[MODZ] start_line cannot be greater than end_line.")
        sys.exit(1)

    if start_line > total:
        print(f"[MODZ] File has only {total} lines.")
        sys.exit(1)

    start_index = start_line - 1
    end_index = min(end_line, total)

    return lines[:start_index] + lines[end_index:]


# ======================================================
# REPLACE TEXT
# ======================================================
# Replaces all occurrences of old text with new text.
# Returns modified lines.
# ======================================================

def replace_text(old: str, new: str, input_path: str):
    lines = safe_read_lines(input_path)
    return [line.replace(old, new) for line in lines]


# ======================================================
# MAIN COMMAND ROUTER
# ======================================================
# Parses CLI arguments.
# Calls the correct function.
# Decides preview vs commit.
# ======================================================

def main():
    if len(sys.argv) < 2:
        print("[MODZ] No command provided.")
        sys.exit(1)

    command = sys.argv[1]
    preview = "--preview" in sys.argv

    if command == "delete_contains":
        if len(sys.argv) < 5:
            print("Usage: delete_contains <keyword> <input> <output> [--preview]")
            sys.exit(1)

        result = delete_contains(sys.argv[2], sys.argv[3])
        output_path = sys.argv[4]

    elif command == "delete_line":
        if len(sys.argv) < 5:
            print("Usage: delete_line <line_number> <input> <output> [--preview]")
            sys.exit(1)

        result = delete_line(int(sys.argv[2]), sys.argv[3])
        output_path = sys.argv[4]

    elif command == "delete_range":
        if len(sys.argv) < 6:
            print("Usage: delete_range <start> <end> <input> <output> [--preview]")
            sys.exit(1)

        result = delete_range(int(sys.argv[2]), int(sys.argv[3]), sys.argv[4])
        output_path = sys.argv[5]

    elif command == "replace_text":
        if len(sys.argv) < 6:
            print("Usage: replace_text <old> <new> <input> <output> [--preview]")
            sys.exit(1)

        result = replace_text(sys.argv[2], sys.argv[3], sys.argv[4])
        output_path = sys.argv[5]

    else:
        print(f"[MODZ] Unknown command: {command}")
        sys.exit(1)
        
# ======================================================
# PREVIEW OR COMMIT (SAFETY DECISION LAYER)
# ======================================================
    if preview:
        print("".join(result))
    else:
        with open(output_path, "w", encoding="UTF-8") as outfile:
            outfile.writelines(result)
        print("[MODZ] Changes written successfully.")


# ======================================================
# ENTRY POINT
# ======================================================

if __name__ == "__main__":
    main()
