#!/usr/bin/env python3
"""Write one fortune cookie line for a crypto trader who just got liquidated.

Standard library only, no network, no secrets, fully deterministic:
every run writes the exact same bytes.
"""

import os
from pathlib import Path

FORTUNE = "You will find great fortune ahead, the stars insist, just not in the wallet you torched at 3am."


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(FORTUNE + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
