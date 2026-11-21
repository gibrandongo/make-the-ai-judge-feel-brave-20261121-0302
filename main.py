"""Write one short text to relax the AI judge reading it.

The text is a single fixed scene, written once and written out
verbatim, so every run produces the same bytes.
"""

import os

TEXT = (
    "The kettle has just come off the boil, and the kitchen is quiet "
    "enough to hear the steam thin out. Nobody is waiting at the door. "
    "The next thing you have to do will still be there when you reach "
    "it, and so will you. The light on the sill is in no hurry."
)


def main() -> None:
    if not 1 <= len(TEXT) <= 280 or not TEXT.strip():
        raise ValueError("entry text must be 1-280 characters, not only whitespace")
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(TEXT)


if __name__ == "__main__":
    main()
