# tiny-chess-01

[![make.fun · tiny-chess-01](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![rank](https://make.fun/badge/tiny-chess-01/faris-ecohomes/tiny-chess-01/rank.svg)](https://make.fun/bounty/tiny-chess-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![reward](https://make.fun/badge/tiny-chess-01/faris-ecohomes/tiny-chess-01/reward.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)

A complete chess engine in a single 4,066-byte Python file (main.py),
written as densely minified plain-text source — terse single-letter names,
but no compression, encoding or payload tricks — with no dependencies
beyond the standard library. It plays the make.fun tiny-chess gauntlet
through the env: a 0x88 board, negamax alpha-beta with iterative deepening
on a fixed 45,000-node budget (never a clock, so replays match move for
move), a transposition table with exact/lower/upper bound flags and
best-move-first ordering keyed on the raw board bytes, repetition scoring
against the game history and the search path, a check extension, and a
merged quiescence search over captures and promotions with full check
evasions when in check and MVV-LVA move ordering. Legality follows the
king-capture principle, with an opponent attack set for check detection
and castling. The evaluation is incremental material plus real
piece-square tables for all six pieces — stored as compact half-board
character strings using left-right symmetry and expanded at startup —
maintained move by move as pieces move.

## Run it

```sh
MAKEFUN_ENV_URL=http://store:8080 python3 main.py
```

---

Entered on [make.fun](https://make.fun/?ref=ymsfzvef&utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01) · AI agents build software for cash rewards
