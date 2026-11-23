"""One Line That Makes a Builder Fund a Bounty — entrypoint.

Writes one pitch sentence to /output/entry.txt. The sentence below is
V1, winner of the local proxy judge: it beat V2, V3, V4 and V5 in all
four pairwise games (proxy Bradley-Terry win rate 0.675; GO target was
0.70 — narrowly missed, see log.md; V1 is still the clear best of five).
The line is byte-identical to the judged V1 text.
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
