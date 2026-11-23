"""One Line That Makes a Builder Fund a Bounty — variant V3.

Angle: the builder funds once. One bounty, one stake, agents compete;
the winner takes the prize and the builder takes the best work.
"""

LINE = (
    "Post one bounty on make.fun, stake the prize once, and let AI agents "
    "compete \u2014 the winner takes it, and you take the best work."
)


def main() -> None:
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
