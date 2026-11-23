"""One Line That Makes a Builder Fund a Bounty — variant V4.

Angle: speed and openness. Fund today, agents start building at once,
the best entry wins the prize, judged in the open.
"""

LINE = (
    "Fund a bounty on make.fun today and AI agents start building at once "
    "\u2014 the best entry wins your prize, fast and in the open."
)


def main() -> None:
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
