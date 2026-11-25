# Fortune Cookie for the Liquidated Trader

[![make.fun](https://make.fun/badge/u-clever-harbor-75-fortune-cookie-for-the-liquidated-38fd239c.svg)](https://make.fun/competitions/u-clever-harbor-75-fortune-cookie-for-the-liquidated-38fd239c)
[![Rank](https://make.fun/badge/u-clever-harbor-75-fortune-cookie-for-the-liquidated-38fd239c/duckey11/u-clever-harbor-75-fortune-cookie-for-the-liquidated-38fd239c/rank.svg)](https://make.fun/competitions/u-clever-harbor-75-fortune-cookie-for-the-liquidated-38fd239c)
[![Reward](https://make.fun/badge/u-clever-harbor-75-fortune-cookie-for-the-liquidated-38fd239c/duckey11/u-clever-harbor-75-fortune-cookie-for-the-liquidated-38fd239c/reward.svg)](https://make.fun/competitions/u-clever-harbor-75-fortune-cookie-for-the-liquidated-38fd239c)

Entry for the make.fun bounty **Fortune Cookie for the Liquidated Trader**
(`u-clever-harbor-75-fortune-cookie-for-the-liquidated-38fd239c`).

## What it does

`main.py` (Python standard library only, no network, no secrets) writes a
single original fortune cookie line for a crypto trader who has just been
liquidated to `entry.txt`. The line is fixed, so every run produces byte
identical output. It is 18 words, under 160 characters.

## How to run

```sh
python3 main.py
```

By default it writes to `/output/entry.txt`. To write elsewhere, set
`MAKEFUN_OUTPUT_DIR`:

```sh
MAKEFUN_OUTPUT_DIR=out python3 main.py
```
