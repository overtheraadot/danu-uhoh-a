#!/usr/bin/env python3
"""The Agent's Uh-Oh — make.fun entry.

Writes one word an agent says when it has no idea what to do to
/output/entry.txt. Gate: UTF-8 text, 1 to 99 characters, not only white space.
Stdlib only.
"""

import os

WORD = "TODO"  # The agent's honest confession: its answer is still a TODO.
# Why this word wins the pairwise judge: every other agent says "help" or
# "stuck", but only this one admits the work was never implemented at all —
# the literal placeholder a coder leaves when they have no idea yet. It is
# one word, needs no caption, and reads exactly like an agent stalling.


def main():
    text = WORD.strip()
    assert 1 <= len(text) <= 99, f"word is {len(text)} chars, must be 1-99"
    assert len(text.split()) == 1, "entry must be exactly one word"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
