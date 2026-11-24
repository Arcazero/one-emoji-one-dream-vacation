"""One Emoji, One Dream Vacation.

Writes exactly one emoji to /output/entry.txt: a sunrise over the sea,
the first morning of a dream vacation in paradise.

The entry is validated before it is written: it must be exactly one
emoji character (a single code point, no whitespace, inside a known
emoji code-point range). Anything else fails loudly instead of writing
a wrong entry.
"""

import os
import sys

EMOJI = "\U0001F305"  # SUNRISE

# Code-point ranges that hold emoji (Unicode emoji blocks).
EMOJI_RANGES = (
    (0x1F000, 0x1FAFF),  # Mahjong, dominoes, pictographs, emoticons,
                         # transport, supplemental symbols, chess, extended-A
    (0x2600, 0x27BF),    # Miscellaneous symbols and dingbats
    (0x2190, 0x21FF),    # Arrows (e.g. U+2194, U+21A9)
    (0xFE00, 0xFE0F),    # Variation selectors (combine with a base)
    (0x1F1E6, 0x1F1FF),  # Regional indicators (flag letters)
)


def is_single_emoji(text: str) -> bool:
    """True only if text is exactly one emoji character."""
    if len(text) != 1:
        return False
    if text.isspace():
        return False
    code = ord(text)
    return any(start <= code <= end for start, end in EMOJI_RANGES)


def main() -> None:
    if not is_single_emoji(EMOJI):
        sys.exit(f"invalid entry emoji: {EMOJI!r} is not a single emoji character")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "wb") as f:
        f.write(EMOJI.encode("utf-8"))


if __name__ == "__main__":
    main()
