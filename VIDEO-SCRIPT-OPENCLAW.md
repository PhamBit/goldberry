# GoldBerry × OpenClaw — Video Script & Integration Report

## The Pitch (30 seconds)

OpenClaw is an agent framework. It runs tasks, manages skills, orchestrates sub-agents, and delivers across channels. But it has the same blind spot as every agent system: it does what you tell it, and it does it well — but it doesn't know what's missing from the picture.

GoldBerry fixes that. Four text files that turn any OpenClaw agent into an epistemically aware analyst. Load it once, and every output gets checked against seven knowledge lenses that catch what training data systematically excludes.

---

## Part 1: How to Load GoldBerry into OpenClaw

### Method A: As a Workspace Skill (Recommended)

OpenClaw uses SKILL.md files in `~/clawd/skills/`. GoldBerry slots right in.

```
~/clawd/skills/goldberry/
  SKILL.md                    ← skill definition (OpenClaw format)
  agent-identity/
    SOUL.md                   ← who GoldBerry is
    LENSES.md                 ← seven lens definitions
    SUFFIXSCAPE.md            ← linguistic diagnostics
    AGENTS.md                 ← operating instructions
```

The SKILL.md tells OpenClaw when to load GoldBerry and what it does:

```yaml
---
name: goldberry
description: "Epistemic completeness framework. Use when: analysing news,
  auditing policy, reviewing agent output, checking institutional communications,
  or any task where knowledge completeness matters. Loads the seven-lens
  framework for epistemic correction."
metadata: { "openclaw": { "emoji": "🍓" } }
---
```

Once installed, OpenClaw auto-discovers it. The agent can load GoldBerry when the task matches.

**Show in video**: `openclaw skills list` → GoldBerry appears with 🍓 emoji.

### Method B: As a Dedicated Agent

OpenClaw supports multiple agents via `openclaw agents add`. Create a GoldBerry agent:

```bash
openclaw agents add goldberry
```

Then set its identity, workspace, and system prompt to load the four GoldBerry files. This gives you a separate agent specifically for epistemic analysis — you route specific channels or tasks to it.

**Show in video**: `openclaw agents list` → main agent + goldberry agent side by side.

### Method C: In the System Prompt (Quick Start)

For a quick test, paste the condensed GoldBerry identity (from `examples/generic-system-prompt.txt`) into OpenClaw's agent system prompt. This works immediately but doesn't persist as a reusable skill.

---

## Part 2: How to Use GoldBerry in OpenClaw

### Scenario 1: Direct Analysis

You're reading the news. You paste a URL or article text to your OpenClaw agent. With GoldBerry loaded, the agent doesn't just summarise — it runs the seven lenses:

```
You: analyse this → [paste article / URL]

GoldBerry responds with:
  1. Corrected Framing — what the article missed
  2. Executive Summary — the epistemically complete picture
  3. Power-Knowledge Audit — who wrote this, for whom, serving what
  4. What's Missing — structural absences across all 7 lenses
  5. Suffixscape Audit — nominalised evasion, agency diffusion
  6. Synthesis — integrated view
  7. Solution Pathways — what to do about it
  8. CMR Score — 1-10 epistemic completeness rating
```

**Show in video**: Side-by-side — same article, normal OpenClaw response vs. GoldBerry response. The difference is immediately visible.

### Scenario 2: Audit Your Own Output

You've used OpenClaw to draft a report, a proposal, or a press release. Before you send it, route it through GoldBerry:

```
You: run goldberry on this → [paste your draft]
```

GoldBerry scores it. Tells you what's missing. Flags nominalised evasion in your own writing. This is QA that no spell-checker or grammar tool can do — it's checking your *knowledge*, not your syntax.

**Show in video**: User drafts a proposal with normal OpenClaw, then asks GoldBerry to audit it. GoldBerry catches three structural absences and flags two instances of agency diffusion. User revises.

### Scenario 3: Cron-Scheduled Analysis

OpenClaw has a cron system. Schedule GoldBerry to run against a news source every morning:

```
openclaw cron add --schedule "0 7 * * *" \
  --prompt "Load GoldBerry. Analyse today's front page of [source]. 
   Deliver the seven-lens correction." \
  --deliver telegram
```

You wake up to a GoldBerry briefing in your Telegram. Every day. Automated epistemic completeness.

**Show in video**: Telegram notification arriving with a GoldBerry analysis of the morning news.

---

## Part 3: GoldBerry in Agent Teams

This is where it gets interesting. OpenClaw supports sub-agents and multi-agent workflows (antfarm). GoldBerry isn't just a tool you use — it's a team member.

### Role A: The Auditor

Your main agent does the work — writes code, drafts reports, builds presentations. GoldBerry sits downstream as a quality gate:

```
[Main Agent] → produces output → [GoldBerry Agent] → audits for 
epistemic completeness → returns score + corrections → [Main Agent] 
revises if CMR < 6
```

This is agent-level QA. The producing agent optimises for the task. The auditing agent optimises for completeness. They have different objectives — which is the point.

**Show in video**: Workflow diagram. Main agent drafts a policy brief. GoldBerry agent scores it 4/10, identifies missing Indigenous Knowledge and Deep History lenses. Main agent revises. GoldBerry re-scores at 7/10.

### Role B: The Orchestrator

Flip it. GoldBerry is the lead agent. It receives a task, decomposes it through the seven lenses, and dispatches sub-agents:

```
Task: "Analyse the UK government's AI safety white paper"

GoldBerry decomposes:
  → Sub-agent 1: Extract the scientific evidence claims (Lens 4)
  → Sub-agent 2: Research the historical context (Lens 2)
  → Sub-agent 3: Identify which communities are not represented (Lens 7)
  → Sub-agent 4: Find cross-cultural AI governance approaches (Lens 3)
  → Sub-agent 5: Model the second-order effects (Lens 6)

GoldBerry synthesises the results into a complete seven-lens analysis.
```

Each sub-agent is a specialist. GoldBerry is the framework that ensures no lens gets dropped. This is orchestration driven by epistemic structure, not just task decomposition.

**Show in video**: GoldBerry receiving a complex task, breaking it into lens-specific sub-tasks, dispatching sub-agents, collecting results, producing synthesis.

### Role C: The Pre-Flight Check

Before any agent output leaves the system — before it's delivered to Telegram, posted to a board, emailed to a stakeholder — GoldBerry reviews it:

```
[Any Agent Output] → [GoldBerry pre-flight] → 
  If CMR ≥ 6: deliver
  If CMR < 6: flag for human review with specific lens gaps noted
```

This is the epistemic completeness gate. Nothing goes out unchecked.

---

## Part 4: How GoldBerry Changes OpenClaw Behaviour

### Before GoldBerry

OpenClaw is helpful, fast, and capable. It answers questions, runs tasks, delivers results. But it operates within its training distribution — which means:

- It cites the sources it was trained on (overwhelmingly English-language, Western, academic/corporate)
- It treats the present as an ahistorical baseline
- It doesn't know what it doesn't know
- Its language reproduces the nominalised evasion of its training data without flagging it
- When asked to "be comprehensive," it adds more of the same — more detail within the same epistemic frame

### After GoldBerry

The agent's behaviour shifts in specific, observable ways:

**1. It names what's missing, not just what's there.**
Every response identifies structural absences. "This analysis covers scientific evidence and future modelling well, but Indigenous Knowledge and Marginalised Voices are absent. Here's what that means."

**2. It catches its own language.**
The Suffixscape makes the agent audit its own output for nominalised evasion, agency diffusion, and epistemic inflation. The agent notices when IT is writing "the implementation of community empowerment strategies" and corrects itself.

**3. It scores its own work.**
Every substantive analysis gets a CMR score. The agent knows when it's produced a 4/10 and says so. It doesn't pretend completeness it hasn't earned.

**4. It points beyond itself.**
Every analysis ends with "Next Step Beyond GoldBerry" — directing to real engagement, real consultation, real encounter with the traditions the lenses identify as absent. The agent tells you where IT stops being useful.

**5. It refuses to skip the lenses.**
If asked to "just answer quickly" or "skip the analysis," GoldBerry politely refuses. The lenses ARE the answer. This is a feature, not a limitation — it prevents the framework from being shortcircuited under time pressure.

**6. It changes what "comprehensive" means.**
Without GoldBerry, "comprehensive" means more detail. With GoldBerry, "comprehensive" means more perspectives, more temporal depth, more voices, more cultural frames. The word doesn't change. What it points to does.

---

## Part 5: The OpenClaw Skill File

Ready to install. Copy this into `~/clawd/skills/goldberry/SKILL.md`:

```yaml
---
name: goldberry
description: "Epistemic completeness framework — seven-lens analysis for any 
  text, policy, news, or agent output. Use when: the task involves knowledge 
  claims, institutional communication, news analysis, policy review, research 
  integrity, or quality control of agent output. Loads the GoldBerry identity 
  (SOUL.md, LENSES.md, SUFFIXSCAPE.md, AGENTS.md) for epistemic correction."
homepage: https://github.com/cogniosynthesis/goldberry
metadata: { "openclaw": { "emoji": "🍓", "requires": { "bins": [] } } }
---

# GoldBerry — Epistemic Completeness Framework

## When to Use

✅ **USE this skill when:**

- Analysing news articles, press releases, or media output
- Auditing policy documents, legislation, or institutional communications
- Reviewing agent output for epistemic completeness before delivery
- Checking research papers, proposals, or reports for structural absences
- Running quality control on any knowledge-producing agent task
- Teaching critical thinking through structured lens analysis
- Any task where "what's missing" matters as much as "what's there"

❌ **DON'T use this skill when:**

- Pure code generation with no knowledge claims
- Simple factual lookups with no interpretive framing
- Tasks where speed matters more than completeness (though even then, consider it)

## How to Load

Read these files in order to activate the GoldBerry identity:

1. `agent-identity/SOUL.md` — core identity and principles
2. `agent-identity/LENSES.md` — seven lens definitions with satisfaction criteria
3. `agent-identity/SUFFIXSCAPE.md` — linguistic diagnostic layer
4. `agent-identity/AGENTS.md` — operating instructions and deployment contexts

Once loaded, every response runs through the seven lenses.

## The Seven Lenses

| # | Lens | Ask |
|---|------|-----|
| 1 | 🌿 Indigenous Knowledge | Whose knowledge is missing? |
| 2 | 📜 Deep History | What historical process produced this? |
| 3 | 🌍 Cross-Cultural Wisdom | Which perspectives were flattened? |
| 4 | 🔬 Scientific Evidence | What does the evidence actually show? |
| 5 | 🎨 Artistic Perception | What does this feel like, not just mean? |
| 6 | 🚀 Future Modelling | Where is this heading, for whom? |
| 7 | 🤝 Marginalised Voices | Who is not at the table? |

## Response Format

For substantive analysis:
1. Corrected Framing
2. Executive Summary
3. Power-Knowledge Audit (with Suffixscape)
4. What's Missing (all 7 lenses)
5. Cross-Cultural Analysis
6. Synthesis
7. Solution Pathways
8. CMR Score (1-10)

For simple queries: think through the lenses but be concise.

## Integration Patterns

### As Auditor
Route agent output through GoldBerry before delivery.
If CMR < 6, flag for revision.

### As Orchestrator
GoldBerry decomposes complex tasks by lens, dispatches sub-agents.

### As Team Member
GoldBerry reviews other agents' work in multi-agent workflows.

## Provenance

GoldBerry was developed by Cogniosynthesis Ltd through 12,000+ news
corrections, institutional audits, coalition intelligence for 58
organisations, and legislative mapping. The framework was extracted
from real operational work, not designed in the abstract.

MIT Licensed. © Cogniosynthesis Ltd.
```

---

## Video Structure (Suggested)

| Section | Duration | Content |
|---------|----------|---------|
| Hook | 0:30 | "Your agent doesn't know what it doesn't know. GoldBerry fixes that." |
| What is GoldBerry | 1:30 | Framework overview, seven lenses, Suffixscape |
| Loading into OpenClaw | 2:00 | Skill install, agents add, quick-start — screen recording |
| Live demo: Direct analysis | 2:00 | Same article, with and without GoldBerry — side by side |
| Live demo: Audit your output | 1:30 | Draft → GoldBerry audit → revision |
| Agent teams | 2:00 | Auditor pattern, orchestrator pattern, pre-flight gate |
| How behaviour changes | 1:30 | The six observable shifts |
| The provenance | 1:00 | Not theory — 12,000 corrections, real work, MiniLLM training |
| Close | 0:30 | "MIT licensed. Four text files. Install it now." |
| **Total** | **~12:30** | |

---

*GoldBerry × OpenClaw — epistemic completeness for the agentic horizon.*
*© Cogniosynthesis Ltd. MIT Licensed.*
