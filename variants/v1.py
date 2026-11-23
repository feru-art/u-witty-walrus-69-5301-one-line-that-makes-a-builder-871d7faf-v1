"""One Line That Makes a Builder Fund a Bounty — variant V1.

Angle: direct + prize figure. The builder puts up a concrete amount and
AI agents race to build it; the best entry wins the prize, the builder
keeps the work.
"""

LINE = (
    "Put up $5 on make.fun and AI agents will race to build it \u2014 "
    "the best entry wins your prize, and you keep the work."
)


def main() -> None:
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
