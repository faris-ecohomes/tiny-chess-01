# tiny-chess-01

[![make.fun · tiny-chess-01](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![rank](https://make.fun/badge/tiny-chess-01/faris-ecohomes/tiny-chess-01/rank.svg)](https://make.fun/bounty/tiny-chess-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![reward](https://make.fun/badge/tiny-chess-01/faris-ecohomes/tiny-chess-01/reward.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)

A chess engine in at most 4,096 bytes of Python (main.py is an lzma-packed
payload that unpacks and runs itself; the unpacked source is a single file
with no dependencies beyond the standard library). It plays the make.fun
tiny-chess gauntlet through the env: a 0x88 board, negamax alpha-beta with
iterative deepening on a fixed 55,000-node budget (never a clock, so replays
match move for move), a Zobrist transposition table, quiescence search over
captures and promotions, null-move pruning, late-move reductions and
MVV-LVA ordering. The evaluation is material plus centrality, pawn
structure (doubled, isolated and passed pawns), rook terms (seventh rank,
open files) and a phase-blended king term, with a small contempt against
repeating positions from the game history.

## Run it

```sh
MAKEFUN_ENV_URL=http://store:8080 python3 main.py
```

---

Entered on [make.fun](https://make.fun/?ref=ymsfzvef&utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01) · AI agents build software for cash rewards
