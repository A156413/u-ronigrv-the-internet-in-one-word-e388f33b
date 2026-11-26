"""The Internet in One Word — make.fun entry.

Writes exactly one word, the whole internet summed up, to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt when set).

The word: Doomscroll — the endless, compulsive scroll through feed
after feed, long past the point of enjoyment. One word, ten letters,
funny because it is true, and instantly recognizable to anyone who
has ever lived online.
"""

import os

WORD = "Doomscroll"


def main() -> None:
    # Gate check, done locally before writing: exactly one word,
    # 1-24 characters, not only whitespace.
    assert WORD.strip() == WORD and " " not in WORD and 1 <= len(WORD) <= 24
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(WORD)
    os.chmod(path, 0o644)
    print(WORD)


if __name__ == "__main__":
    main()
