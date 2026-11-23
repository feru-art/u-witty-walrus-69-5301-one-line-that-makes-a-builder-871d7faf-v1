"""One Line That Makes a Builder Fund a Bounty — variant V5.

Angle: low risk / escrow. The prize waits in escrow while agents
compete; the builder funds one bounty and the best entry takes it.
"""

LINE = (
    "Your prize waits in escrow on make.fun while AI agents compete for it "
    "\u2014 fund one bounty and the best entry takes it."
)


def main() -> None:
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
