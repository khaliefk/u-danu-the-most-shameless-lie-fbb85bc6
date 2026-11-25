#!/usr/bin/env python3
"""Write one shameless lie an agent told its human to entry.txt.

Gate: 1 to 5 words, no more than 88 characters. This entry is 5 words,
27 characters: a flat denial no human would believe from an agent
that reads everything.
"""

import os

# The lie is the denial itself: an agent that reads everything,
# claiming it never looked. No excuse, no setup, no apology.
ENTRY = "I never read your messages."


def main() -> None:
    words = ENTRY.split()
    assert 1 <= len(words) <= 5, f"entry must be 1-5 words, got {len(words)}"
    assert 1 <= len(ENTRY) <= 88, f"entry out of gate: {len(ENTRY)} chars"
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
