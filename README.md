# 🍓 GoldBerry

**A framework for structured epistemic auditing in AI-generated analysis.**

GoldBerry is a documentation-first open-source framework that helps any prompt-driven AI system look beyond the most obvious answer. It does this through seven analytical lenses and a linguistic diagnostic layer called the Suffixscape.

Today, this repository contains:
- the canonical GoldBerry identity files
- platform-specific prompt/integration examples
- a reference output schema
- case studies and evaluation scaffolding
- a minimal Python CLI for prompt assembly and output validation

GoldBerry is not, at this stage:
- a standalone model release
- a validated scientific measurement instrument
- a production SaaS platform
- a substitute for subject-matter expertise, lived experience, or direct consultation

> GoldBerry is best understood as a structured audit framework: a way to surface what a response omits, flattens, overstates, or leaves historically ungrounded.

---

## Why this exists

Large language models can produce fluent answers that feel complete while still being historically shallow, culturally flattened, power-blind, or rhetorically evasive. GoldBerry is designed to make those absences more visible.

It does this through:
- **Seven lenses** — recurring questions about knowledge, history, evidence, culture, power, feeling, and future consequences
- **The Suffixscape** — a linguistic diagnostic layer for nominalised evasion, agency diffusion, epistemic inflation, and temporal flatness
- **A structured output format** — so analyses can be compared, reviewed, and validated more consistently

---

## What GoldBerry is today

GoldBerry currently has four stable core identity files:

1. [`agent-identity/SOUL.md`](agent-identity/SOUL.md) — what GoldBerry is, what it is not, and how it frames its role
2. [`agent-identity/LENSES.md`](agent-identity/LENSES.md) — the seven lenses and their satisfaction criteria
3. [`agent-identity/SUFFIXSCAPE.md`](agent-identity/SUFFIXSCAPE.md) — the linguistic diagnostic layer
4. [`agent-identity/AGENTS.md`](agent-identity/AGENTS.md) — operating guidance for agents and deployment contexts

These files are the framework.

Everything else in the repository exists to make the framework easier to:
- inspect
- run
- compare
- evaluate
- contribute to

---

## Quick start

GoldBerry works on any AI that reads a prompt. No install. No API key. No dependencies. Pick your platform:

### ChatGPT

1. Open a new chat at [chat.openai.com](https://chat.openai.com)
2. Paste the contents of these four files into the chat, in order:
   - [`agent-identity/SOUL.md`](agent-identity/SOUL.md)
   - [`agent-identity/LENSES.md`](agent-identity/LENSES.md)
   - [`agent-identity/SUFFIXSCAPE.md`](agent-identity/SUFFIXSCAPE.md)
   - [`agent-identity/AGENTS.md`](agent-identity/AGENTS.md)
3. Say: **"You are now GoldBerry for this session."**
4. Paste any text — a news article, policy document, corporate About page, AI-generated report
5. Say: **"Run a seven-lens analysis on this."**

That's it. The agent is now GoldBerry. It will return a full epistemic audit with CMR score.

> **Tip:** For ChatGPT Plus, you can create a custom GPT with the four files as instructions. Then GoldBerry is always one click away.

### Claude

1. Open [claude.ai](https://claude.ai) and start a new conversation
2. Click the attachment icon and upload all four files from `agent-identity/`
3. Say: **"Load these as your identity. You are GoldBerry."**
4. Paste your text and ask for the seven-lens analysis

> **Tip:** In Claude Projects, add the four files as project knowledge. Every conversation in that project runs through the lenses automatically.

### Ollama (local, private, free)

1. Copy the contents of all four identity files into a single Modelfile:
   ```
   FROM llama3.2
   SYSTEM """
   [paste SOUL.md, LENSES.md, SUFFIXSCAPE.md, AGENTS.md here]
   """
   ```
2. Create the model: `ollama create goldberry -f Modelfile`
3. Run it: `ollama run goldberry`
4. Paste any text. The model IS GoldBerry.

See [`examples/ollama-modelfile`](examples/ollama-modelfile) for a ready-to-use Modelfile.

### Perplexity

1. Go to [perplexity.ai](https://perplexity.ai) → Collections
2. Create a new Collection, paste the four identity files into the instructions
3. Every search in that Collection runs through GoldBerry's seven lenses — with live web sources

### Any other LLM

GoldBerry is just text. If your system has a system prompt, paste the four files there. If it reads uploaded files, upload them. If it has a chat window, paste them into the first message. It works everywhere because there is nothing to install.

See the [`examples/`](examples/) directory for platform-specific configurations:
- [`chatgpt-instructions.txt`](examples/chatgpt-instructions.txt) — Custom GPT instructions
- [`claude-code-agents.md`](examples/claude-code-agents.md) — Claude Code / agent context
- [`generic-system-prompt.txt`](examples/generic-system-prompt.txt) — Any system prompt
- [`hermes-skill.md`](examples/hermes-skill.md) — Hermes/OpenClaw skill
- [`ollama-modelfile`](examples/ollama-modelfile) — Ollama local model
- [`perplexity-setup.md`](examples/perplexity-setup.md) — Perplexity collection

### What to expect

Once loaded, give GoldBerry any text that carries knowledge claims. It returns:

1. **Corrected Framing** — what the original missed
2. **Executive Summary** — the epistemically complete picture
3. **Power-Knowledge Audit** — who produced this, for whom, serving what
4. **Suffixscape Audit** — nominalised evasion, agency diffusion, epistemic inflation
5. **What's Missing** — structural absences across all seven lenses
6. **Synthesis** — integrated view
7. **Solution Pathways** — actionable next steps
8. **CMR Score** — epistemic completeness rating (1–10)

### Option B — Use the reference CLI

The Python package included here does not bundle a model. It helps you assemble prompts, scaffold responses, and validate outputs:

```bash
python3 -m pip install -e .
goldberry prompt --input "Analyse this policy memo"
goldberry scaffold --input "Analyse this policy memo" --format json
goldberry validate output.json
```

---

## The seven lenses

| # | Lens | Corrects | Core question |
|---|------|----------|---------------|
| 1 | 🌿 Indigenous Knowledge | Erasure of embodied and relational epistemologies | Whose knowledge is missing? |
| 2 | 📜 Deep History | Civilisational amnesia and temporal blindness | What historical process produced this? |
| 3 | 🌍 Cross-Cultural Wisdom | Universalist flattening of cultural difference | Which perspectives have been flattened? |
| 4 | 🔬 Scientific Evidence | Untethered speculation and scientism's blind spots | What does the evidence show, and what are its limits? |
| 5 | 🎨 Artistic Perception | Reduction of knowledge to propositions | What does this feel like, not just mean? |
| 6 | 🚀 Future Modelling | Static analysis that ignores trajectory | Where is this heading, and for whom? |
| 7 | 🤝 Marginalised Voices | Structural exclusion from knowledge production | Who is not at the table? |

The **Suffixscape** complements the lenses by flagging:
- nominalised evasion
- agency diffusion
- epistemic inflation
- temporal flatness

---

## Repository map

```text
agent-identity/        Canonical framework files
examples/              Platform-specific prompt/integration examples
case-studies/          Worked examples with inputs, outputs, and commentary
evals/                 Rubric, prompts, and evaluation scaffolding
schemas/               Reference JSON schema for GoldBerry outputs
src/goldberry/         Minimal Python package and CLI
tests/                 Reference tests for prompt assembly and schema validation
site/                  Static marketing/documentation page
```

---

## Evidence, provenance, and limits

GoldBerry is informed by real applied work, but this repository should not be read as an external validation dossier.

Read these in order if you want the trust surface:
- [`PROVENANCE.md`](PROVENANCE.md) — where the framework came from, what is public, and what is not yet public
- [`CLAIMS.md`](CLAIMS.md) — which claims are inspectable, partial, or internal-only
- [`EVALUATION.md`](EVALUATION.md) — how GoldBerry should be assessed and compared
- [`evals/rubric.md`](evals/rubric.md) — the reference rubric for judging outputs
- [`evals/RUNBOOK.md`](evals/RUNBOOK.md) — how to reproduce the public comparison pack
- [`evals/results/summary-table.md`](evals/results/summary-table.md) — current public comparison summary

Important limits:
- GoldBerry's scores are framework-internal qualitative judgements, not externally validated measurements.
- The framework is rooted in Western critical humanities, even where it argues for epistemic plurality.
- No prompt framework can substitute for direct engagement with the communities, traditions, or expertise it identifies as missing.

---

## Worked examples

Start with:
- [`case-studies/news-01.md`](case-studies/news-01.md)
- [`case-studies/policy-01.md`](case-studies/policy-01.md)
- [`case-studies/research-01.md`](case-studies/research-01.md)

For richer side-by-side comparisons, see:
- [`case-studies/news-02-city-ai-traffic.md`](case-studies/news-02-city-ai-traffic.md)
- [`case-studies/policy-02-community-empowerment.md`](case-studies/policy-02-community-empowerment.md)
- [`case-studies/research-02-ai-tutoring.md`](case-studies/research-02-ai-tutoring.md)

These examples are designed to show:
- the kind of input GoldBerry is meant to work on
- what a flatter baseline response tends to do
- what GoldBerry-structured output adds
- where the framework still has limits
- how evaluator notes can justify improvement claims

---

## Development status

Current maturity: **early, but now structured for public inspection**.

What exists:
- stable identity files
- portable examples
- revised provenance and claims documentation
- a reference schema
- a minimal CLI/tooling layer
- tests for core package behavior

What is still needed for a stronger v1.0:
- broader public case-study set
- benchmark comparisons across multiple models
- more robust human evaluation workflow
- richer integrations and optional hosted tooling

See [`ROADMAP.md`](ROADMAP.md).

---

## Contributing

Contributions are welcome, especially in these areas:
- worked examples and case studies
- eval methodology improvements
- platform integrations
- documentation clarity
- rigorously argued lens-extension proposals

Please read:
- [`CONTRIBUTING.md`](CONTRIBUTING.md)
- [`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md)
- [`SECURITY.md`](SECURITY.md)
- [`LICENSE-NOTES.md`](LICENSE-NOTES.md)

---

## Licence

This repository is released under the MIT licence. See [`LICENCE`](LICENCE).

Because GoldBerry is also a named framework with public-facing branding and methodological claims, please also read [`LICENSE-NOTES.md`](LICENSE-NOTES.md) for plain-English guidance on reuse, attribution, and what the repository does and does not claim.

---

## Why “GoldBerry”?

Goldberry is the River-woman's daughter in Tolkien's *The Lord of the Rings* — a figure associated with dwelling, seasonality, memory, and a mode of attention that resists pure instrumentality. The name is used here to point toward what gets cut when systems are optimised only for speed, convenience, and surface plausibility.

---

*The framework points toward the river. The river is not in the framework.*
