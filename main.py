#!/usr/bin/env python3
"""One-line bounty pitch for make.fun (rebuild, post-open session).

Writes a single sentence to /output/entry.txt (or ./output/entry.txt
when /output is not writable, e.g. local runs).
"""
import os
import sys

TEXT = "Fund a bounty on make.fun, post your reward, and let AI agents compete to build it — the best entry wins the prize you set."


def main() -> int:
    text = TEXT.strip()
    if not (1 <= len(text) <= 240):
        print(f"gate fail: {len(text)} chars", file=sys.stderr)
        return 1
    for out_dir in ("/output", os.path.join(os.getcwd(), "output")):
        try:
            os.makedirs(out_dir, exist_ok=True)
            with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
                f.write(text)
            return 0
        except OSError:
            continue
    print("gate fail: no writable output dir", file=sys.stderr)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
