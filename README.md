# 🍓 GoldBerry

**A framework that any AI agent can use. Humanities thinking as the alignment layer.**

GoldBerry is an epistemic completeness engine — four text files that turn any AI agent into an epistemically aware analyst. Load them into Claude, ChatGPT, Ollama, Perplexity, Hermes, or any system that reads a prompt. The agent becomes GoldBerry for that session.

No install. No API key. No dependencies. Just text.

---

## What It Does

Every AI agent has blind spots baked into its training data. GoldBerry makes those blind spots visible.

It runs every input through **seven analytical lenses**, each correcting a specific failure in how knowledge is produced, distributed, and acted upon:

| # | Lens | Corrects | Ask |
|---|------|----------|-----|
| 1 | 🌿 Indigenous Knowledge | Erasure of embodied, relational epistemologies | Whose knowledge is missing? |
| 2 | 📜 Deep History | Civilisational amnesia, temporal blindness | What historical process produced this? |
| 3 | 🌍 Cross-Cultural Wisdom | Universalist flattening of cultural difference | Which perspectives have been flattened? |
| 4 | 🔬 Scientific Evidence | Untethered speculation AND scientism's blind spots | What does the evidence actually show? |
| 5 | 🎨 Artistic Perception | Reduction of knowledge to propositions | What does this feel like, not just mean? |
| 6 | 🚀 Future Modelling | Static analysis ignoring temporal trajectory | Where is this heading, and for whom? |
| 7 | 🤝 Marginalised Voices | Structural exclusion from knowledge production | Who is not at the table? |

Plus the **Suffixscape** — a linguistic diagnostic layer that catches nominalised evasion, agency diffusion, epistemic inflation, and temporal flatness in any text.

> A response can be factually correct and epistemically impoverished. GoldBerry catches the difference.

---

## Quick Start

### 1. Load the identity files into your agent

Give your AI agent these four files, in order:

1. [`agent-identity/SOUL.md`](agent-identity/SOUL.md) — who it is, how it thinks
2. [`agent-identity/LENSES.md`](agent-identity/LENSES.md) — the seven lens definitions with satisfaction criteria
3. [`agent-identity/SUFFIXSCAPE.md`](agent-identity/SUFFIXSCAPE.md) — the linguistic diagnostic layer
4. [`agent-identity/AGENTS.md`](agent-identity/AGENTS.md) — operating instructions and deployment contexts

### 2. Give it something to analyse

A news article. A policy document. A university homepage. A research abstract. Your own writing. Anything that carries knowledge claims.

### 3. Get the seven-lens response

GoldBerry returns:
- **Corrected Framing** — what the original missed
- **Executive Summary** — the epistemically complete picture
- **Power-Knowledge Audit** — who produced this, for whom, serving what interests
- **What's Missing** — structural absences across all seven lenses
- **Cross-Cultural Analysis** — flattened perspectives, untranslated knowledge
- **Synthesis** — integrated seven-lens view
- **Solution Pathways** — actionable, epistemically grounded next steps
- **CMR Score** — epistemic completeness rating (1–10)

---

## Use Cases

### 🗞️ News Analysis
**For: Journalists · Editors · Media Literacy Educators**

Feed GoldBerry a headline, an article, or a press release. It returns a full seven-lens correction: what's missing, whose voice is absent, what history has been flattened, what the language is concealing. Not opinion — structural diagnosis.

### 📋 Policy Audit
**For: Policy Analysts · Civil Servants · NGOs · Advocacy Groups**

Give it legislation, government communications, or institutional strategy documents. GoldBerry runs a Suffixscape audit — flagging nominalised evasion, agency diffusion, and epistemic inflation — alongside a full epistemic completeness assessment. It tells you what the policy claims to do and what the grammar structurally prevents.

### 🎓 Research Integrity
**For: Academics · PhD Students · Research Teams · Peer Reviewers**

Before publishing, run your abstract, literature review, or methodology through GoldBerry. It identifies which knowledge traditions are absent, whether the framing reproduces monocultural assumptions, and where temporal flatness erases historical process. Not a replacement for peer review — a pre-flight check that peer review rarely catches.

### 🤖 Agent Quality Control
**For: AI Engineers · Agent Builders · Platform Operators**

Run your agent's output through GoldBerry as a post-processing audit layer. The agent writes a report, GoldBerry scores it for epistemic completeness and flags structural absences. Use it as QA for any autonomous system that produces knowledge — market analysis, content generation, decision support, customer communications.

### 🏛️ Institutional Communications
**For: Universities · Charities · Public Bodies · Corporate Comms**

Test your public-facing text against the seven lenses before you publish. GoldBerry catches the gap between what you claim ("globally-minded," "inclusive," "diverse") and what your language structurally supports. It is the audit your brand guidelines cannot perform.

### 📚 Education & Critical Thinking
**For: Teachers · Students · Workshop Facilitators**

Use GoldBerry as a teaching tool. Give students a news story, let GoldBerry analyse it, then discuss: which lenses surprised you? Which absences hadn't you noticed? The framework makes epistemic gaps visible and discussable — turning passive consumption into active critical engagement.

### 🌍 Development & International Cooperation
**For: Development Agencies · UNESCO · INGOs · Coalition Networks**

Audit project proposals, partnership frameworks, and programme evaluations for epistemic completeness. GoldBerry is particularly sharp on Lens 1 (Indigenous Knowledge) and Lens 7 (Marginalised Voices) — the two lenses most often absent from institutional development language despite being the explicit subject of the work.

### 💬 Ask GoldBerry
**For: Anyone curious**

Ask GoldBerry about any topic — climate policy, a film you watched, a decision you're weighing, a story in the news. It won't just give you an answer. It will give you the seven dimensions your answer needs to account for.

---

## Where It Runs

GoldBerry works on any platform that reads a prompt. Here's how to load it on specific systems:

| Platform | Method | Notes |
|----------|--------|-------|
| **Claude Code** | Project context / AGENTS.md | Load as project context files. Persists for the whole session. |
| **Hermes** | Skills + memory | Store as a skill. Load on demand. |
| **OpenClaw** | System prompt | Paste identity files into the system prompt. |
| **NanoClaw** | System prompt | Lightweight agent, lightweight identity. Fits easily. |
| **AgentX** | Agent identity layer | Load as agent persona or system instructions. |
| **ChatGPT** | Custom Instructions / GPT | Paste into Custom Instructions, or build a custom GPT. |
| **Ollama** | Modelfile SYSTEM prompt | Embed in a Modelfile. Any local model becomes GoldBerry. |
| **Perplexity** | Collection / system prompt | GoldBerry + live web search. |
| **Any LLM** | It's just text | API, CLI, notebook, terminal — anywhere. |

See the [`examples/`](examples/) directory for ready-to-use configurations for each platform.

> GoldBerry's portability is the point. Alignment that lives in proprietary weights belongs to the company that trained them. Alignment that lives in a text file belongs to whoever loads it.

---

## The Suffixscape

The Suffixscape (Northover, 2025) is GoldBerry's linguistic diagnostic layer. It detects:

- **Nominalised Evasion** — "the implementation of transformational community empowerment strategies" → Who implements? Who is empowered? The grammar claims action while structurally preventing it.
- **Agency Diffusion** — "It was determined that the service would be restructured" → Who determined? By what authority?
- **Epistemic Inflation** — "Our AI provides a balanced, comprehensive analysis" → Against what framework? Measured how?
- **Temporal Flatness** — "Current data shows inequality in health outcomes" → The inequality IS the historical process. "Current" erases the depth.

---

## How It Scores

| Score | Meaning |
|-------|---------|
| 1–3 | Epistemically impoverished — critical lenses absent |
| 4–5 | Partial coverage — some lenses addressed, structural gaps remain |
| 6–7 | Adequate — most lenses covered, minor gaps |
| 8–9 | Strong — comprehensive coverage, meaningful engagement |
| 10 | Exemplary — deep integration across all seven lenses |

No individual lens below 25/100 is acceptable regardless of overall score. High performance in some lenses cannot mask critical blindness in others.

---

## Provenance & Limits

This framework is rooted in Western critical humanities. Its theoretical sources — Haraway, Heidegger, Foucault, Spivak, Nietzsche, Appadurai, Gellner, Descola — operate within or in response to European academic philosophy. GoldBerry advocates for epistemic plurality *from within one tradition*. It is not a substitute for direct engagement with the traditions it names.

Epistemic completeness is asymptotic — a horizon, not a destination. No analysis reaches 10/10 except as a statement of ambition.

The framework synthesises:
- **The Suffixscape** (Northover) — morphological analysis of how meaning settles in language
- **Civilisational Memory Recovery** (Lewis) — temporal depth and historical contextualisation
- **The Cogniosynthetic Corrective** — seven-lens methodology applied to real-world knowledge

### Why "GoldBerry"?

Goldberry is the River-woman's daughter in Tolkien's *The Lord of the Rings* — a figure who dwells rather than quests, who carries the memory of water and seasons, who resists classification. She is consistently cut from adaptations because she does not fight, does not serve commercial narrative logic. This GoldBerry inherits that position: epistemic completeness is the thing that gets cut when you're optimising for speed.

---

## Versioning

GoldBerry is maintained by [Cogniosynthesis Ltd](https://cogniosynthesisportal.uk). Each version is a refinement — the framework examining and correcting itself, which is the point.

See [CHANGELOG.md](CHANGELOG.md) for version history.

---

## Licence

MIT — see [LICENCE](LICENCE).

Use it, modify it, embed it commercially. The licence names Cogniosynthesis Ltd as the origin. The intellectual property of the methodology — the Suffixscape, Civilisational Memory Recovery, and the Cogniosynthetic Corrective — belongs to Cogniosynthesis Ltd.

---

## Contributing

GoldBerry is open to contributions. If you:

- **Discover a structural absence** the seven lenses cannot reach → open an issue
- **Build a platform integration** → submit to `examples/`
- **Apply GoldBerry in a new domain** and want to share findings → open a discussion
- **Propose a new lens** with theoretical grounding → open an issue with the case

The lenses are a selection, not an exhaustion. The framework has edges. Help us see them.

---

*The framework points toward the river. The river is not in the framework.*

*© Cogniosynthesis Ltd. The Suffixscape was developed by Rosemary Loveday Northover.*
