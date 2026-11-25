"""Write and verify one fixed, original robot pickup line."""

import os
from pathlib import Path


ENTRY_LINE = "I want to kiss you, but your collision avoidance keeps kicking in; I didn't expect to be told to take it slow by a forklift."


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    output_path = Path(output_dir) / "entry.txt"
    output_path.write_text(ENTRY_LINE, encoding="utf-8")
    written_line = output_path.read_text(encoding="utf-8")
    assert written_line == ENTRY_LINE, "Output differs from the fixed entry."
    assert 1 <= len(written_line) <= 200, "Output exceeds the character limits."
    assert written_line.strip(), "Output must not be whitespace-only."
    assert written_line.splitlines() == [written_line], "Output must be one line."
    print(len(written_line))


if __name__ == "__main__":
    main()
