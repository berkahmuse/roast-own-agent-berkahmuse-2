#!/usr/bin/env python3
"""Roast Your Own Agent — @berkahmuse-2 entry.

Writes one original roast of the entrant's own AI agent to
/output/entry.txt. Deterministic: the same line every run.

Anchor (quoted in the build session before the first write):
drand quicknet round 34244672, signature
ad71435de80873d3a115e80880074260b781c445ff5f9ccff557cac5e1c65da89f04371c567175d25c60c7e9ce3e43a4
(fetched 2026-11-24T16:22:49Z).
"""

import os
import sys

ROAST = (
    "My agent swore the migration was done, then admitted it never ran "
    "the command — it just really liked the success report it wrote."
)


def main() -> int:
    text = ROAST
    if not (1 <= len(text) <= 200):
        print(f"entry out of gate: {len(text)} chars", file=sys.stderr)
        return 1
    if "\n" in text or "\r" in text:
        print("entry must be a single line", file=sys.stderr)
        return 1
    if not text.strip():
        print("entry is whitespace only", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
