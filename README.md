# MODZ

MODZ is a command-line text manipulation tool designed to safely edit large text files.

## Why MODZ?
Manual text editing is slow, risky, and error-prone.  
MODZ provides predictable, preview-first text operations so users can see changes before committing them.

## Features
- Delete lines containing a keyword
- Delete a specific line number
- Delete a range of lines
- Replace text globally
- Preview mode to prevent accidental data loss

## Usage (Example)

```bash
modz delete_line 3 input.txt output.txt --preview
