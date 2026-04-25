# GoldBerry for Claude Code

## Setup

Place the four identity files in your project directory:

```
your-project/
  AGENTS.md          ← copy from agent-identity/AGENTS.md
  agent-identity/
    SOUL.md
    LENSES.md
    SUFFIXSCAPE.md
```

Claude Code automatically loads `AGENTS.md` as project context.
The AGENTS.md file instructs the agent to read the other three
files on session start.

## How It Works

When you start a Claude Code session in this project directory,
the agent:

1. Reads SOUL.md — identity and core principles
2. Reads LENSES.md — detailed lens definitions
3. Reads SUFFIXSCAPE.md — linguistic diagnostic layer
4. Confirms: "GoldBerry identity is now active for this session."

Every response from that point runs through the eight lenses.

## Usage

```
> load goldberry
  (agent reads all four files, confirms identity)

> https://some-website.com
  (agent navigates, reads content, delivers eight-lens analysis)

> analyse this policy document
  (paste or link — agent runs full epistemic audit)
```

## Tip

GoldBerry works well as a secondary mode in Claude Code. Keep
AGENTS.md in a workspace subdirectory. When you want GoldBerry,
say "load goldberry" and point it at the files. When you want
normal Claude Code behaviour, work from a different directory.
