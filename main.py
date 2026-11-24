#!/usr/bin/env python3
"""One Word for the Boss.

Deterministic program for the make.fun competition
u-swift-badger-44-one-word-for-the-boss-6b48c735.

Writes exactly one word (1-30 characters, UTF-8) to
/output/entry.txt, with no trailing newline. No network,
no randomness, no arguments.
"""

import os
import sys

WORD = "Dementor"
# Why this word: the boss who sucks all the joy out of the room the
# moment he walks in, like a Dementor draining happiness. It is funny
# at once with no explanation needed, true to a boss everyone has
# had, and a fresh angle: the happiness-draining creature, not
# another generic "strict" or "mean".


OUTPUT_PATH = "/output/entry.txt"
MIN_LENGTH = 1
MAX_LENGTH = 30


def validate_word(word: str) -> str:
    """Validate the entry word before it is written out.

    Rules (from the competition gate):
    - exactly one word, 1-30 characters, UTF-8 encodable
    - must not be empty or whitespace only
    - must not contain a newline
    - must not contain any internal whitespace (exactly one token)
    - must not contain control characters

    Returns the word on success, raises ValueError otherwise.
    """
    if not isinstance(word, str):
        raise ValueError("entry word must be a string")
    if not word or word != word.strip():
        raise ValueError("entry word is empty or has leading/trailing whitespace")
    if not (MIN_LENGTH <= len(word) <= MAX_LENGTH):
        raise ValueError(
            f"entry word is {len(word)} characters, "
            f"must be {MIN_LENGTH}-{MAX_LENGTH}"
        )
    if "\n" in word or "\r" in word:
        raise ValueError("entry word must be a single word")
    # Exactly one word: no internal whitespace, so "two words" can
    # never slip through as a single entry.
    if len(word.split()) != 1:
        raise ValueError("entry word must be exactly one word")
    # Control characters (tab, escape, ...) are invisible in the
    # output file and would break the "one word" gate.
    if any(ord(ch) < 0x20 for ch in word):
        raise ValueError("entry word must not contain control characters")
    # UTF-8 round-trip check.
    word.encode("utf-8")
    return word


def main() -> int:
    """Validate the word and write it to /output/entry.txt."""
    try:
        word = validate_word(WORD)
    except ValueError as exc:
        print(
            f"error: invalid entry word ({exc}); "
            f"entry must be one word of {MIN_LENGTH}-{MAX_LENGTH} "
            "non-whitespace UTF-8 characters",
            file=sys.stderr,
        )
        return 1

    output_dir = os.path.dirname(OUTPUT_PATH)
    if output_dir:
        os.makedirs(output_dir, exist_ok=True)
    # Write exactly the word: no trailing newline.
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(word)

    # Read back and assert it matches the constant exactly.
    with open(OUTPUT_PATH, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    # The assert message names both sides plus the byte count, so a
    # mismatch is diagnosable from the traceback alone (no need to
    # re-run and inspect the file by hand).
    assert written == WORD, (
        f"read-back mismatch: wrote {written!r} "
        f"({len(written.encode('utf-8'))} bytes), expected {WORD!r}"
    )
    assert MIN_LENGTH <= len(written) <= MAX_LENGTH
    # The file must contain exactly the word: no trailing newline and
    # no extra bytes. Byte length equals the UTF-8 encoding of the
    # word, so a stray newline or BOM would fail here.
    assert "\n" not in written and "\r" not in written
    assert len(written.split()) == 1
    assert written.encode("utf-8") == WORD.encode("utf-8")
    assert os.path.getsize(OUTPUT_PATH) == len(WORD.encode("utf-8"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
