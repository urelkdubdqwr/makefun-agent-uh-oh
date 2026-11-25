"""Write the competition entry text to a single UTF-8 file.

Output goes to $MAKEFUN_OUTPUT_DIR/entry.txt when that variable is set and
non-empty, otherwise to /output/entry.txt. The output directory is created
if it does not already exist. No network, randomness, or clock reads.
"""

import os
import sys

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"

try:
    os.makedirs(OUTPUT_DIR, exist_ok=True)
except OSError as exc:
    sys.exit(f"error: cannot create output directory {OUTPUT_DIR!r}: {exc}")

with open(os.path.join(OUTPUT_DIR, "entry.txt"), "w", encoding="utf-8") as f:
    f.write("Unhandled\n")
