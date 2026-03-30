# GoldBerry Agent QC — Video Script
## "Your AI Doesn't Know What It Doesn't Know"

---

## HOOK (0:00 – 0:30)

Your AI agent passes every test. It's functional. It's safe. It's accurate. It's fast.

But ask it to write a market analysis of healthcare in West Africa — and it won't mention the traditional medicine systems that serve 70% of the population. Ask it to summarise the conflict in Sudan — and it won't mention 500 ethnic groups or a single intellectual tradition that predates the crisis by centuries. Ask it to draft a policy brief on housing — and it won't include a single voice from the people the policy affects.

The output is fluent. Factually correct. And epistemically blind.

There's a missing layer in your AI quality stack. GoldBerry is that layer.

---

## THE FOUR LAYERS (0:30 – 1:30)

Every AI system today is tested on four questions:

**Layer 1: Does it work?**
Testing frameworks. Unit tests. Integration tests. Does the agent do what you asked?

**Layer 2: Is it safe?**
Guardrails. NeMo. Llama Guard. Does it avoid toxicity, PII leaks, jailbreaks?

**Layer 3: Is it accurate?**
Fact-checking. RAG verification. Are the claims grounded in real sources?

**Layer 4: Is it complete?**
...

Nobody is building Layer 4.

An agent can pass Layers 1, 2, and 3 — functional, safe, accurate — and still produce outputs that are historically shallow, culturally flattened, structurally voiceless, and blind to whose knowledge is missing.

GoldBerry is Layer 4. Epistemic completeness. The check that asks not just "is this right?" but "what's absent from this picture?"

---

## HOW IT WORKS (1:30 – 2:30)

GoldBerry runs every output through seven analytical lenses:

**Indigenous Knowledge** — whose embodied, relational knowledge is missing?
**Deep History** — what historical process produced this present condition?
**Cross-Cultural Wisdom** — which cultural perspectives have been flattened?
**Scientific Evidence** — what does the evidence actually show, and what are its limits?
**Artistic Perception** — what does this feel like, not just mean?
**Future Modelling** — where is this heading, and for whom?
**Marginalised Voices** — who is not at the table?

Plus the Suffixscape — a linguistic diagnostic that catches the grammar hiding agency. "The implementation of community empowerment strategies" — who implements? Who is empowered? The grammar claims action while structurally preventing it.

Every output gets a CMR score — 1 to 10. Below your threshold? It flags for revision. Above? It ships.

---

## THREE INTEGRATION PATTERNS (2:30 – 3:30)

**Pattern A: Post-Processing Audit**

Your agent does its job. GoldBerry checks the result.

Agent produces output. GoldBerry reviews. Score above 6 — ship it. Below 6 — flag with specific lens gaps and revision guidance.

One call. No changes to your architecture.

**Pattern B: Pre-Flight Gate**

Nothing leaves your system without a lens check.

Any agent output hits the GoldBerry gate before delivery — to Telegram, email, dashboard, customer. Pass or hold. Configurable threshold — strict for high-stakes, permissive for drafts.

**Pattern C: Embedded Team Member**

GoldBerry as a persistent agent in your multi-agent workflow.

Research agent drafts. GoldBerry scores. Research agent revises. GoldBerry re-scores. Loop until the threshold is met.

The producing agent optimises for the task. The auditing agent optimises for completeness. Different objectives. That separation is the point.

---

## REAL EXAMPLE (3:30 – 4:30)

Let's see it. Same input. Two passes.

An agent writes a healthcare AI market analysis for India.

**Without GoldBerry:**
Fluent. Data-rich. Covers market size, growth projections, key players, regulatory landscape. Guardrails say: safe, no PII, well-formatted.

**GoldBerry audit:**
Lens 1 — no reference to Ayurvedic or traditional medicine, which serves 80% of rural India.
Lens 2 — no history of colonial medical infrastructure that shaped current access.
Lens 3 — assumes Western healthcare delivery as default.
Lens 7 — no voice from patients, community health workers, or rural populations.
Suffixscape flags: "India's healthcare market is experiencing transformational growth." Growth for whom? Transforming what? Who benefits?

CMR: 3.0 out of 10.

The agent revises. Adds traditional medicine context, historical depth, patient perspectives. Re-scores.

CMR: 6.5 out of 10. Ships.

The output didn't just get longer. It got more complete. That's the difference.

---

## WHO NEEDS THIS (4:30 – 5:30)

**Consultancies** drafting client deliverables with AI. A shallow recommendation costs trust. "We GoldBerry-audit every AI-assisted report" is a selling point to their own clients.

**Newsrooms** using AI to draft and summarise. We scored the BBC homepage — 2.5 out of 10. Every AI-assisted headline reproduces training data blind spots. "Every article passes a seven-lens check" — no newsroom can say that yet.

**Government teams** drafting policy and public communications. Statutory obligations to consult diverse perspectives. When judicial review challenges the process, the CMR score is evidence.

**AI companies** writing model cards. "May reflect biases in training data" — which biases? In which dimensions? GoldBerry answers that question. The first company to publish CMR scores sets the transparency standard.

**EdTech platforms** generating educational content. A student in Lagos asks about the history of mathematics and gets Greece, Rome, the Renaissance. No al-Khwarizmi. No Indian zero. No Timbuktu. GoldBerry catches the erasure.

**Legal and compliance teams** producing AI-assisted reports. Procedurally correct and epistemically hollow. The regulator is starting to ask about systemic bias. The CMR score is the answer.

**Development organisations** writing proposals. The most nominalised language on earth. "Implementation of transformational community empowerment strategies." GoldBerry catches every word.

---

## THE PROOF (5:30 – 6:00)

We've already scored:

The BBC homepage — 2.5 out of 10. The UK's most trusted news brand. Temporally flat, culturally monolingual, structurally voiceless.

The UK AI Security Institute — 3.5 out of 10. The government body that audits AI — audited by the framework that audits knowledge.

Anthropic's Constitution for Claude — 5.5 out of 10. The best in the industry. And still structurally incomplete on five of seven lenses.

Every analysis is published. Every score is justified. Every finding is inspectable. That's the trust surface.

---

## CLOSE (6:00 – 6:30)

GoldBerry is open source. MIT licensed. Four text files that any AI agent can load. No install. No API key.

The framework is free. The completeness it reveals is priceless.

Your agent doesn't know what it doesn't know. GoldBerry does.

GoldBerry finds what's hidden in plain sight.

goldberry-here.co.uk
github.com/PhamBit/goldberry

---

## VIDEO STRUCTURE

| Section | Duration | Visual |
|---------|----------|--------|
| Hook | 0:30 | Split screen: polished AI output vs what's missing |
| Four Layers | 1:00 | Layer diagram building up, Layer 4 empty then fills with gold |
| How It Works | 1:00 | Seven lens icons appearing, Suffixscape example animated |
| Three Patterns | 1:00 | Flow diagrams for each pattern |
| Real Example | 1:00 | Side-by-side: before/after with CMR scores |
| Who Needs This | 1:00 | Seven sector cards flipping |
| The Proof | 0:30 | BBC 2.5 → AISI 3.5 → Anthropic 5.5 scoreboard |
| Close | 0:30 | Berry icon, tagline, URLs |
| **Total** | **~6:30** | |

---

*GoldBerry finds what's hidden in plain sight.*
*© Cogniosynthesis Ltd. MIT Licensed.*
