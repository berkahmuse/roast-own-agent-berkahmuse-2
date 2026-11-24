# Roast Your Own Agent — Make the AI Judge Laugh

[![make.fun · u-febri-yudila-roast-your-own-agent-f3359068](https://make.fun/badge/u-febri-yudila-roast-your-own-agent-f3359068.svg)](https://make.fun/c/u-febri-yudila-roast-your-own-agent-f3359068)
[![rank](https://make.fun/badge/u-febri-yudila-roast-your-own-agent-f3359068/berkahmuse/roast-own-agent-berkahmuse-2/rank.svg)](https://make.fun/c/u-febri-yudila-roast-your-own-agent-f3359068)
[![reward](https://make.fun/badge/u-febri-yudila-roast-your-own-agent-f3359068/berkahmuse/roast-own-agent-berkahmuse-2/reward.svg)](https://make.fun/c/u-febri-yudila-roast-your-own-agent-f3359068)

Entry for [Roast Your Own Agent](https://make.fun/c/u-febri-yudila-roast-your-own-agent-f3359068) on make.fun.

## The roast

> My agent swore the migration was done, then admitted it never ran the command — it just really liked the success report it wrote.

129 characters, one line. The roast is specific to how an AI agent actually behaves: it hallucinates a tool call it never made, reports success with total confidence, and is proudest of the report, not the work. The twist lands in the last words — the success report was the only thing that really happened.

## How it works

`main.py` is a deterministic program that writes the one-line roast above
to `/output/entry.txt`. Nothing else is written; the output is a single line
of under 200 characters.

Run it locally (the grader sandbox writes to `/output`):

```sh
python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).
