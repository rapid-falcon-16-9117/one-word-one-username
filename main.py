"""One Word, One Username, One Reward.

Writes our own make.fun username -- the entrant's genuine handle --
as a single word to entry.txt, exactly as the brief requires:
one word, no explanation, no links, no pitch.
"""

import os

USERNAME = "rapid-falcon-16-9117"


def main() -> None:
    # Self-check against the sealed gate: entry.txt must be UTF-8 text
    # of 1 to 30 characters, not only white space, a single word.
    if not (1 <= len(USERNAME) <= 30):
        raise SystemExit(f"username must be 1-30 chars, got {len(USERNAME)}")
    if USERNAME != USERNAME.strip() or any(ch.isspace() for ch in USERNAME):
        raise SystemExit("username must be a single word with no spaces")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(USERNAME)


if __name__ == "__main__":
    main()
