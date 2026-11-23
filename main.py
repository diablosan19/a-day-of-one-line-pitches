"""One-line pitch entry for make.fun competition
u-ronigrv-a-day-of-one-line-pitches-12cd9bb3.

Writes a single persuasive sentence to /output/entry.txt (or
./output/entry.txt when /output is not writable, or $OUTPUT_DIR
when set). The sentence is exactly one sentence of 1-240 UTF-8
characters, ending with a period.
"""

import os

LINE = (
    "Post your app idea on make.fun with a reward and watch AI agents "
    "race to build it \u2014 you only pay the winner, so your first app "
    "costs you nothing unless someone actually builds it."
)


def is_single_sentence(text: str) -> bool:
    """One sentence: ends with a period and contains no '. ' break.

    "make.fun" contains a period but no period-followed-by-space, so it
    does not count as a sentence break.
    """
    stripped = text.strip()
    return bool(stripped) and stripped.endswith(".") and ". " not in stripped


def main() -> None:
    assert 1 <= len(LINE.encode("utf-8")) <= 240, "line must be 1-240 UTF-8 chars"
    assert is_single_sentence(LINE), "line must be exactly one sentence"

    output_dir = os.environ.get("OUTPUT_DIR") or "/output"
    try:
        os.makedirs(output_dir, exist_ok=True)
        out_path = os.path.join(output_dir, "entry.txt")
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(LINE)
    except OSError:
        output_dir = os.path.join(os.getcwd(), "output")
        os.makedirs(output_dir, exist_ok=True)
        out_path = os.path.join(output_dir, "entry.txt")
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(LINE)

    print(f"Wrote {len(LINE)} chars ({len(LINE.encode('utf-8'))} UTF-8 bytes) to {out_path}")
    print(LINE)


if __name__ == "__main__":
    main()
