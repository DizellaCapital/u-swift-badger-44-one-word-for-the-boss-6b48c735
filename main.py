import os

# Entry: "Foghorn" — the boss whose voice carries across the whole floor,
# announcing everything, drowning everyone else out. One word, 7 bytes:
# funny on its own, true of a real boss habit, fresh (no boss cliche),
# and it travels across any workplace. Gate: 1-30 chars, single word.
WORD = "Foghorn"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = WORD
    if not (1 <= len(text) <= 30):
        raise SystemExit("entry must be 1 to 30 characters")
    if not text.strip():
        raise SystemExit("entry must not be only whitespace")
    if len(text.split()) != 1:
        raise SystemExit("entry must be exactly one word")
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != text:
        raise SystemExit("read-back verification failed")


if __name__ == "__main__":
    main()
