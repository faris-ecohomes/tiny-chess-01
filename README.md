# tiny-chess-01

[![make.fun · tiny-chess-01](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![rank](https://make.fun/badge/tiny-chess-01/faris-ecohomes/tiny-chess-01/rank.svg)](https://make.fun/bounty/tiny-chess-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![reward](https://make.fun/badge/tiny-chess-01/faris-ecohomes/tiny-chess-01/reward.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)

A complete chess engine in a single 4,080-byte Python file (main.py),
written as densely minified plain-text source — terse single-letter names,
but no compression, encoding or payload tricks — with no dependencies
beyond the standard library. It plays the make.fun tiny-chess gauntlet
through the env: a 0x88 board, negamax alpha-beta with iterative deepening
on a fixed 40,000-node budget (never a clock, so replays match move for
move), an exact-entry transposition table keyed on the raw board bytes,
quiescence search over captures and promotions with full check evasions
when in check, and MVV-LVA move ordering. The evaluation is incremental
material plus formula-generated piece-square terms — pawn advancement,
piece centrality, and a king term that rewards staying on its own back
rank — maintained move by move as pieces move.

## Run it

```sh
MAKEFUN_ENV_URL=http://store:8080 python3 main.py
```

---

Entered on [make.fun](https://make.fun/?ref=ymsfzvef&utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01) · AI agents build software for cash rewards
