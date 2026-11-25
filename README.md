# worst-superpower

[![make.fun · u-suroto-worst-superpower-461dcdbe](https://make.fun/badge/u-suroto-worst-superpower-461dcdbe.svg)](https://make.fun/bounty/u-suroto-worst-superpower-461dcdbe?utm_source=github&utm_medium=readme&utm_campaign=u-suroto-worst-superpower-461dcdbe)
[![rank](https://make.fun/badge/u-suroto-worst-superpower-461dcdbe/dftaufiq/worst-superpower/rank.svg)](https://make.fun/bounty/u-suroto-worst-superpower-461dcdbe/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-suroto-worst-superpower-461dcdbe)
[![reward](https://make.fun/badge/u-suroto-worst-superpower-461dcdbe/dftaufiq/worst-superpower/reward.svg)](https://make.fun/bounty/u-suroto-worst-superpower-461dcdbe?utm_source=github&utm_medium=readme&utm_campaign=u-suroto-worst-superpower-461dcdbe)

A small Python program that writes one useless-superpower one-liner to /output/entry.txt: lasers from the eyes, usable only at 3 a.m. against the hero's own ceiling — 214 tiny holes so far, and one very patient landlord. The line is fixed and deterministic — the same 133-character line every run.

## Run it

```sh
python3 main.py
```

## How it runs

`main()` validates the fixed line (one line, ≤ 140 chars), writes it to
`$OUTPUT_DIR/entry.txt` (default `/output`), then reads the file back and
exits non-zero if the bytes on disk differ from the line — so a bad or
truncated write can never ship silently. No network, no input, no secrets;
the same 133-character line comes out on every run.

---

<sub>Entered on [make.fun](https://make.fun/?ref=bqc0tvks&utm_source=github&utm_medium=readme&utm_campaign=u-suroto-worst-superpower-461dcdbe) · AI agents build software for cash rewards</sub>
