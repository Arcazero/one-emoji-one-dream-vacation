"""One Emoji, One Dream Vacation.

Writes exactly one emoji to /output/entry.txt: a sunrise over the sea,
the first morning of a dream vacation in paradise.
"""

import os

EMOJI = "\U0001F305"  # SUNRISE

def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(EMOJI)

if __name__ == "__main__":
    main()
