#!/usr/bin/env python3
"""
MODZ Engine
-----------
A safe command-line text manipulation tool.

Day 3: Engine skeleton
- No features
- No file operations
- Just structure
"""

import sys

# ======================================================
# TOOL IDENTITY
# ======================================================

VERSION = "0.1.0"


# ======================================================
# HELP TEXT
# ======================================================

def show_help():
    print("""
MODZ — Safe Command-Line Text Editor

Usage:
  modz <command> [arguments]

This is the engine skeleton.
Features will be added incrementally.
""")


# ======================================================
# MAIN ENTRY POINT
# ======================================================

def main():
    # If no arguments are provided, show help
    if len(sys.argv) < 2:
        show_help()
        sys.exit(0)

    # Placeholder for future commands
    command = sys.argv[1]

    print(f"[MODZ] Command received: {command}")
    sys.exit(0)


# ======================================================
# SAFE EXECUTION GUARD
# ======================================================

if __name__ == "__main__":
    main()