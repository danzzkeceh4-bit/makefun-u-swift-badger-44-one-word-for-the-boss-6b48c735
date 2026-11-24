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

OUTPUT_PATH = "/output/entry.txt"
MIN_LENGTH = 1
MAX_LENGTH = 30


def validate_word(word: str) -> str:
    """Validate the entry word before it is written out.

    Rules (from the competition gate):
    - exactly one word, 1-30 characters, UTF-8 encodable
    - must not be empty or whitespace only
    - must not contain a newline

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
    assert written == WORD, f"read-back mismatch: {written!r} != {WORD!r}"
    assert MIN_LENGTH <= len(written) <= MAX_LENGTH
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
