#!/usr/bin/env python3
"""One-line bounty pitch for make.fun (rebuild, post-open session).

Winning sentence (V2, local proxy-judge win rate 0.700): a single
sentence that tells a builder to fund a bounty, post the reward, and
let AI agents compete for it, with the best entry winning the prize.

Writes the sentence to /output/entry.txt (or ./output/entry.txt
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
    # Single-sentence guard: the only dots are the one inside "make.fun"
    # and the final full stop, so the entry stays one sentence.
    assert text.endswith(".") and text.count(".") == 2, "entry must be one sentence"
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
