#!/usr/bin/env python3
"""One Line to Your Younger Self.

A make.fun entry: one line, in English, that the writer would send back
to their younger self if a single line were all they got. No explanation,
no context, no second sentence.

The program prints the line and also writes it to /output/entry.txt,
where the harness gate reads it (1-200 UTF-8 characters).
"""

import os

LINE = "The night you stay quiet to keep the peace will cost you ten years \u2014 speak now, kid, while your voice still scares you a little."


def main():
    """Print the line and write it to /output/entry.txt for the harness."""
    print(LINE)
    try:
        os.makedirs("/output", exist_ok=True)
        with open("/output/entry.txt", "w", encoding="utf-8") as f:
            f.write(LINE)
    except OSError:
        # /output may not exist outside the harness sandbox; the printed
        # line is still the entry.
        pass


if __name__ == "__main__":
    main()
