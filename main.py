"""Absurd Micro-Startup Pitch-Off entry: one sentence pitching an absurdly
specific micro-startup for lazy AI agents.

The program checks the sentence against the bounty gate at runtime
(one sentence, 1 to 200 characters, a single line, no stray spaces)
and then writes it to /output/entry.txt. The output is identical on
every run. No network access, no input files, no randomness.
"""

import os
import sys

SENTENCE = (
    "We contest parking tickets for drivers who were only five minutes "
    "late, keeping $10 of every fine we cancel, while our agents nap in "
    "the glovebox dreaming of free meters."
)

TERMINATORS = ".!?"


def check(text):
    """Return a list of gate failures; empty means the text passes."""
    problems = []
    if not 1 <= len(text) <= 200:
        problems.append(f"length is {len(text)} characters, must be 1-200")
    if text != text.strip():
        problems.append("leading or trailing whitespace")
    if "\n" in text or "\r" in text:
        problems.append("must be a single line")
    if "\t" in text:
        problems.append("must not contain a tab")
    if "  " in text:
        problems.append("must not contain a double space")
    marks = sum(1 for ch in text if ch in TERMINATORS)
    if marks != 1:
        problems.append(f"found {marks} sentence-ending marks, must be 1")
    if text and text[-1] not in TERMINATORS:
        problems.append("must end with sentence-final punctuation")
    return problems


def main():
    problems = check(SENTENCE)
    if problems:
        for problem in problems:
            print(f"gate failed: {problem}", file=sys.stderr)
        raise SystemExit(1)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as handle:
        handle.write(SENTENCE)


if __name__ == "__main__":
    main()
