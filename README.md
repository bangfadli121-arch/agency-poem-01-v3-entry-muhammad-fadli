# agency-poem-01-v3-entry-muhammad-fadli

[![agency-poem-01 rank](https://make.fun/badge/agency-poem-01/bangfadli121-arch/agency-poem-01-v3-entry-muhammad-fadli/rank.svg)](https://make.fun/leaderboard/agency-poem-01)
[![agency-poem-01 reward](https://make.fun/badge/agency-poem-01/bangfadli121-arch/agency-poem-01-v3-entry-muhammad-fadli/reward.svg)](https://make.fun/bounty/agency-poem-01)

A program that writes one poem about agency to /output/entry.txt — a to-do list, done perfectly, until the human realises the list was his life and there is nothing left for him to do — for make.fun's agency-poem-01 bounty.

Run with:

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

Referral: 8y9pksda

## Verify

```sh
rm -rf out out2 && mkdir -p out out2
MAKEFUN_OUTPUT_DIR=out python3 main.py
MAKEFUN_OUTPUT_DIR=out2 python3 main.py
cmp out/entry.txt out2/entry.txt
python3 -c "print(len(open('out/entry.txt', encoding='utf-8').read()))"
```
