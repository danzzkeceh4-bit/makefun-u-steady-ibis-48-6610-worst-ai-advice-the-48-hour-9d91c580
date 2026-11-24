#!/usr/bin/env python3
"""Worst AI Advice — make.fun entry.

Writes exactly one line of the worst advice an AI could give to
/output/entry.txt, then reads it back and asserts it matches the
constant exactly. No network, no external input.
"""

ENTRY = "Absolutely! If your smoke alarm keeps beeping, remove the battery \u2014 a quiet alarm means your home is finally safe."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    with open(OUTPUT_PATH, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    assert written == ENTRY, (
        f"entry mismatch: wrote {len(written)} chars, expected {len(ENTRY)}"
    )
    assert "\n" not in written, "entry must be a single line without newline"


if __name__ == "__main__":
    main()
