# GoldBerry for Hermes

## Setup

Save GoldBerry as a Hermes skill so it can be loaded on demand.

### Option A: Reference the files

If the identity files are on disk (e.g. ~/goldberry/agent-identity/),
the agent can load them with:

```
> load goldberry
```

The agent reads SOUL.md, LENSES.md, SUFFIXSCAPE.md, AGENTS.md
and activates the identity for the session.

### Option B: Create a Hermes skill

Use skill_manage to create a skill that contains the condensed
GoldBerry identity. This loads faster and works even without
the files on disk.

The skill should:
1. Set the agent identity to GoldBerry
2. Include the eight lens definitions
3. Include the Suffixscape diagnostic markers
4. Instruct the agent to run all eight lenses on every input

### Memory Integration

Add to Hermes memory:
```
GoldBerry workspace ~/path/to/goldberry/: On wake, SILENTLY read
SOUL.md, LENSES.md, SUFFIXSCAPE.md, AGENTS.md then confirm identity.
```

This triggers automatic loading when working in the GoldBerry directory.

## Usage

Once loaded, use normally — paste URLs, text, documents.
GoldBerry analyses everything through the eight lenses and
writes results back to CognioBook when deployed inside the
Cognio ecosystem.
