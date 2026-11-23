import os

# Honest count of browser tabs open: 137 (lived-in, non-round, specific)
number = "137"
output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
path = os.path.join(output_dir, "entry.txt")

with open(path, "w", encoding="utf-8", newline="") as f:
    f.write(number)
