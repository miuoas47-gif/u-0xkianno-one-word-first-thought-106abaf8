#!/usr/bin/env python3
"""One Word, First Thought — entry program.

Writes exactly one word, the first that came to mind, to
$MAKEFUN_OUTPUT_DIR/entry.txt (falling back to /output/entry.txt).

The word: defenestration — the act of throwing someone out of a window.
Surprising, vivid, and with a spark of wit: a single word that stages a
whole scene, from the Defenestration of Prague to a cartoon exit.

Stdlib only, no network, no arguments, deterministic.
"""

import os
import sys

WORD = "defenestration"


def validate(word: str) -> None:
    """The gate requires 1-24 UTF-8 characters, not only whitespace, and
    this bounty asks for exactly one word: a single line of ASCII letters,
    so the character count and the byte count agree."""
    if not word:
        raise ValueError("word is empty")
    if len(word) > 24:
        raise ValueError("word is longer than 24 characters")
    if word != word.strip():
        raise ValueError("word has leading or trailing whitespace")
    if len(word.split()) != 1:
        raise ValueError("entry must be exactly one word")
    if not word.isalpha() or not word.isascii():
        raise ValueError("word must contain ASCII letters only")
    if "\n" in word or "\r" in word:
        raise ValueError("word must be a single line")


def main() -> int:
    validate(WORD)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(WORD)
    # Read back and verify byte-identical output before declaring success.
    with open(path, "rb") as f:
        written = f.read()
    if written != WORD.encode("utf-8"):
        raise ValueError("read-back mismatch in entry.txt")
    validate(written.decode("utf-8"))
    print(f"Wrote one word to {path}: {WORD!r} ({len(WORD)} characters)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
