"""The Internet in One Word — make.fun entry.

Writes exactly one word, the whole internet summed up, to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt when set).

The word: Doomscroll — the endless, compulsive scroll through feed
after feed, long past the point of enjoyment.
"""

import os

WORD = "Doomscroll"


def write_entry(word: str, out_dir: str) -> str:
    """Write a single word to entry.txt in out_dir; return the path.

    The word must be exactly one word: non-empty, no whitespace, and
    at most 30 characters. The file is written with no trailing
    newline and mode 0644, so the output is byte-identical every run.
    """
    assert isinstance(word, str) and word
    assert not any(ch.isspace() for ch in word), "word must be a single word"
    assert len(word) <= 30, "word must be at most 30 characters"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(word)
    os.chmod(path, 0o644)
    return path


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = write_entry(WORD, out_dir)
    print(WORD)
    print(path)


if __name__ == "__main__":
    main()
