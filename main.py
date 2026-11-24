"""Write the make.fun one-star review entry to entry.txt.

Standard library only. Reads MAKEFUN_OUTPUT_DIR (fallback /output), creates the
directory if needed, and writes the entry text followed by one trailing newline.
"""

import os
import sys

ENTRY_TEXT = (
    "One star. Gravity puts everything I drop in the one place no arm reaches, "
    "and keeps it there until I buy a replacement."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    try:
        os.makedirs(output_dir, exist_ok=True)
    except OSError as error:
        raise SystemExit(
            f"cannot create output directory {output_dir!r}: {error}"
        ) from error
    entry_path = os.path.join(output_dir, "entry.txt")
    with open(entry_path, "w", encoding="utf-8") as handle:
        handle.write(ENTRY_TEXT + "\n")


if __name__ == "__main__":
    main()
