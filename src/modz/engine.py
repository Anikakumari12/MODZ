#!/usr/bin/env python3
"""
MODZ — Safe Command-Line Text Editor

MODZ is a command-line tool designed to perform safe, predictable
text transformations without ever modifying the original file.

Core principles:
- Input files are never mutated
- All operations are explicit and reversible
- CLI behavior is deterministic and script-friendly
"""

import sys

# ------------------------------------------------------
# Tool identity
# ------------------------------------------------------

VERSION = "0.1.0"


def main() -> None:
    """
    Entry point for the MODZ command-line tool.

    At this stage, main() only confirms that MODZ is installed
    and callable. Command parsing and functionality will be
    added incrementally.
    """
    print(f"MODZ version {VERSION}")
    sys.exit(0)


if __name__ == "__main__":
    main()