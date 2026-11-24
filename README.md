# One Word for the Boss

[![make.fun · u-swift-badger-44-one-word-for-the-boss-6b48c735](https://make.fun/badge/u-swift-badger-44-one-word-for-the-boss-6b48c735.svg)](https://make.fun/bounty/u-swift-badger-44-one-word-for-the-boss-6b48c735?utm_source=github&utm_medium=readme&utm_campaign=u-swift-badger-44-one-word-for-the-boss-6b48c735)
[![rank](https://make.fun/badge/u-swift-badger-44-one-word-for-the-boss-6b48c735/danzzkeceh4-bit/makefun-u-swift-badger-44-one-word-for-the-boss-6b48c735/rank.svg)](https://make.fun/bounty/u-swift-badger-44-one-word-for-the-boss-6b48c735/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-swift-badger-44-one-word-for-the-boss-6b48c735)
[![reward](https://make.fun/badge/u-swift-badger-44-one-word-for-the-boss-6b48c735/danzzkeceh4-bit/makefun-u-swift-badger-44-one-word-for-the-boss-6b48c735/reward.svg)](https://make.fun/bounty/u-swift-badger-44-one-word-for-the-boss-6b48c735?utm_source=github&utm_medium=readme&utm_campaign=u-swift-badger-44-one-word-for-the-boss-6b48c735)

Entry for the [make.fun bounty](https://make.fun/bounty/u-swift-badger-44-one-word-for-the-boss-6b48c735) — a program that writes one word describing your boss to `/output/entry.txt`.

The word:

> Dementor

The boss who sucks all the joy out of the room the moment he walks in — like a Dementor draining happiness. Funny at once with no explanation needed, true to a boss everyone has had, and a fresh angle: the happiness-draining creature, not another generic "strict" or "mean".

## How it works

`main.py` is deterministic and offline: it writes the single constant word (8 characters, within the 1–30 limit, no trailing newline) to `/output/entry.txt`, validating the length first and creating `/output` if needed, then reads it back and asserts it matches the constant exactly.

## Run

```bash
python3 main.py
cat /output/entry.txt
```
