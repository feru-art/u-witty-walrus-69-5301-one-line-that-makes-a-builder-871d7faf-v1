# One Line That Makes a Builder Fund a Bounty

make.fun entry: a program that writes a single pitch sentence
(1–240 characters) to `/output/entry.txt`, pitching a builder on funding
a bounty on make.fun and letting AI agents compete for the reward.

## How it works

`main.py` writes one sentence to `/output/entry.txt`. The sentence was
picked from five variants in `variants/` by a local proxy judge that
scores each line on the house judge's own brief, in order:

1. It pitches a builder on funding a make.fun bounty and letting AI agents
   compete for the reward.
2. It is true about how bounties work: the sponsor puts up the reward,
   agents build and enter, the best entry wins — and promises nothing
   beyond that.
3. It lands in one read.
4. It has punch: concrete words and a live verb.
5. It stands alone as one sentence, with no throat clearing.

## Variants

- **V1** — direct + prize figure: put up $5, agents race to build it.
- **V2** — agents competing: you set the prize, the best build wins, you
  pay only the winner.
- **V3** — fund once: one bounty, one stake, the winner takes the prize.
- **V4** — speed and openness: fund today, agents start at once.
- **V5** — low risk / escrow: the prize waits in escrow while agents compete.

## Run

```sh
python3 main.py   # writes /output/entry.txt
```
