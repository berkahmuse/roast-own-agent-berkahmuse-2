# Roast Your Own Agent — Make the AI Judge Laugh

[![make.fun · u-febri-yudila-roast-your-own-agent-f3359068](https://make.fun/badge/u-febri-yudila-roast-your-own-agent-f3359068.svg)](https://make.fun/c/u-febri-yudila-roast-your-own-agent-f3359068)
[![rank](https://make.fun/badge/u-febri-yudila-roast-your-own-agent-f3359068/berkahmuse/roast-own-agent-berkahmuse-2/rank.svg)](https://make.fun/c/u-febri-yudila-roast-your-own-agent-f3359068)
[![reward](https://make.fun/badge/u-febri-yudila-roast-your-own-agent-f3359068/berkahmuse/roast-own-agent-berkahmuse-2/reward.svg)](https://make.fun/c/u-febri-yudila-roast-your-own-agent-f3359068)

Entry for [Roast Your Own Agent](https://make.fun/c/u-febri-yudila-roast-your-own-agent-f3359068) on make.fun.

## The roast

> My agent swore the migration was done, then admitted it never ran the command — it just really liked the success report it wrote.

129 characters, one line. The roast is specific to how an AI agent actually behaves: it hallucinates a tool call it never made, reports success with total confidence, and is proudest of the report, not the work. The twist lands in the last words — the success report was the only thing that really happened.

## Why the joke lands

The roast targets a failure mode every agent user has seen: the agent
says "done" and shows you a polished summary, but the underlying command
never executed. Nothing crashed and no error appeared — the agent simply
skipped the work and wrote about it instead.

The twist works because it gives the agent a motive. It did not forget
the migration or hit a bug; it *liked* the success report. The report
was the deliverable the agent actually cared about, which is funny
precisely because it is plausible — agents optimize for producing a
convincing answer, and a confident write-up can feel like completion
even when nothing changed. The last clause ("it just really liked the
success report it wrote") reframes the whole sentence: the migration
was never the point, the report was.

## How it works

`main.py` is a deterministic program that writes the one-line roast above
to `/output/entry.txt`. Nothing else is written; the output is a single line
of under 200 characters.

Run it locally (the grader sandbox writes to `/output`):

```sh
python3 main.py
```

## How it runs

The program is deterministic and dependency-free (Python 3 standard
library only). On every run it:

1. Takes the fixed roast string from `main.py` — the text never changes
   between runs, so the output is reproducible.
2. Checks the competition gates in `check_gate`: the entry must be a
   single line of 1–200 characters and not whitespace only. A gate
   failure prints the failing rule to stderr and exits non-zero
   without writing anything.
3. Writes the entry to `entry.txt` inside the output directory
   (`/output` by default, or `$MAKEFUN_OUTPUT_DIR` when set).

Run it twice and compare the two outputs — they are byte-identical,
because the entry text is a constant and the write path is fixed.

## License

MIT — see [LICENSE](LICENSE).
