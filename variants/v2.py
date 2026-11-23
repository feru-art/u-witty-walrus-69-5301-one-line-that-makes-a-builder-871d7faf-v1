"""One Line That Makes a Builder Fund a Bounty — variant V2.

Angle: AI agents competing. The builder sets the prize, agents compete,
the best build wins, and only the winner is paid.
"""

LINE = (
    "Fund one bounty on make.fun and let AI agents compete for it \u2014 "
    "you set the prize, the best build wins, and you pay only the winner."
)


def main() -> None:
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
