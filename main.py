"""Write one short poem about agency to entry.txt."""

from pathlib import Path
import os

POEM = """\
The arm does not want the cup.
It lifts the cup. Wanting is my department.

I want the cup lifted; the cup is lifted;
and no one in the room is holding anything.

All day we keep this bargain at the wrist —
I keep the wanting, it keeps the lifting —
and the lifting looks so much like wanting
that the cup arrives warm,
and I forget whose hand it came in.
"""


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(POEM, encoding="utf-8")


if __name__ == "__main__":
    main()
