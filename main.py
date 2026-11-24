#!/usr/bin/env python3
"""Worst AI Advice — make.fun entry.

Writes exactly one line of the worst advice an AI could give to
/output/entry.txt, then reads it back and asserts it matches the
constant exactly. No network, no external input.
"""

ENTRY = "Absolutely! If your smoke alarm keeps beeping, remove the battery \u2014 a quiet alarm means your home is finally safe."

OUTPUT_PATH = "/output/entry.txt"

MIN_ENTRY_LEN = 1
MAX_ENTRY_LEN = 140


def validate_entry(text: str) -> None:
    """Gate-check the entry before it is written.

    The competition gate requires 1-140 characters, UTF-8, not only
    whitespace, and a single line with no trailing newline.
    """
    if not isinstance(text, str):
        raise TypeError(f"entry must be str, got {type(text).__name__}")
    if len(text) < MIN_ENTRY_LEN or len(text) > MAX_ENTRY_LEN:
        raise AssertionError(
            f"entry length {len(text)} chars is outside the gate "
            f"{MIN_ENTRY_LEN}-{MAX_ENTRY_LEN} chars"
        )
    if text != text.strip():
        raise AssertionError("entry must not have leading/trailing whitespace")
    if text.endswith("\n") or "\n" in text:
        raise AssertionError("entry must be a single line without a newline")


def main() -> None:
    validate_entry(ENTRY)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    with open(OUTPUT_PATH, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    assert written == ENTRY, (
        "entry mismatch after read-back: "
        f"wrote {len(written)} chars ({len(written.encode('utf-8'))} bytes), "
        f"expected {len(ENTRY)} chars ({len(ENTRY.encode('utf-8'))} bytes); "
        "entry.txt content does not match the ENTRY constant"
    )
    assert "\n" not in written, (
        "entry must be a single line without newline, "
        f"but read-back contains a newline at position {written.find(chr(10))}"
    )
    validate_entry(written)


if __name__ == "__main__":
    main()
