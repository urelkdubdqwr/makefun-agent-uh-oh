import os

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"

os.makedirs(OUTPUT_DIR, exist_ok=True)

with open(os.path.join(OUTPUT_DIR, "entry.txt"), "w", encoding="utf-8") as f:
    f.write("Unhandled\n")
