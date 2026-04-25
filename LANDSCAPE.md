# GoldBerry Landscape Analysis

**Last updated:** 29 March 2026
**Method:** Systematic search across DuckDuckGo (150+ results), arXiv, GitHub, academic databases, and direct inspection of identified projects.

---

## Position Statement

GoldBerry is, to our knowledge, the first open-source framework for structured epistemic auditing of AI outputs — combining portable identity files, named analytical lenses, a linguistic diagnostic layer, and inspectable evaluation artifacts. We invite anyone to point us to comparable work.

This document maps every adjacent project we could find and explains why none of them occupies the same space.

---

## The GoldBerry Feature Set (for comparison)

GoldBerry's current public distinctiveness appears to come from this combination of features:

1. **Agent-loadable** — works by loading text into any LLM, no install, no API key
2. **Epistemic auditing** — checks what's structurally ABSENT, not just what's present
3. **Named lenses** — specific analytical dimensions with satisfaction criteria
4. **Linguistic diagnostics** — detects grammatical patterns that conceal agency and meaning (Suffixscape)
5. **Inspectable evaluation** — public eval pack with baselines, outputs, evaluator notes
6. **Self-aware limits** — explicitly names its own edges and what it cannot see
7. **Open source** — MIT licensed, fully public

No project found in this survey provides all seven. Most provide one or two. This combination — not any single feature — is the basis of the distinctiveness claim.

---

## Category 1: AI Safety & Guardrails

### Guardrails AI (guardrailsai.com)
- **What it does:** Input/output validation for LLM applications. Checks for toxicity, PII, hallucination, format compliance.
- **What it doesn't do:** No epistemic auditing. Asks "is this output safe/valid?" not "is this output epistemically complete?" No lenses, no Suffixscape, no concept of structural absence.
- **Gap:** Safety ≠ epistemic completeness. A safe, well-formatted output can score 2.5/10 on GoldBerry.

### NVIDIA NeMo Guardrails (github.com/NVIDIA-NeMo/Guardrails)
- **What it does:** Programmable rails for LLM conversations. Topical control, jailbreak prevention, fact-checking integration.
- **What it doesn't do:** No epistemic framework. Rails are behavioural constraints, not analytical lenses. No concept of what knowledge is missing.
- **Gap:** Constrains output behaviour. Does not audit output knowledge.

### Llama Guard (Meta)
- **What it does:** Safety classifier for LLM inputs/outputs. Categorises content against a safety taxonomy.
- **What it doesn't do:** Binary safe/unsafe classification. No multidimensional epistemic analysis. No concept of absence.
- **Gap:** Safety taxonomy is not an epistemic framework.

### Constitutional AI (Anthropic)
- **What it does:** Self-critique against a set of principles (helpful, harmless, honest). The closest in spirit to GoldBerry.
- **What it doesn't do:** Principles are behavioural, not epistemic. No named knowledge lenses. No Suffixscape. No concept of Indigenous Knowledge, Deep History, or Marginalised Voices as specific dimensions. No public eval pack.
- **Gap:** Constitutional AI aligns behaviour. GoldBerry audits knowledge. Different layers.

---

## Category 2: Bias Detection & Fairness

### IBM AIF360 / Fairlearn / LangFair
- **What they do:** Detect statistical bias in model outputs. Measure fairness metrics across demographic groups.
- **What they don't do:** Quantitative bias metrics, not epistemic auditing. They measure disparity in outputs, not absence of knowledge dimensions. No lenses, no linguistic diagnostics.
- **Gap:** Bias detection measures what IS there (unevenly). GoldBerry identifies what ISN'T there (at all).

### Perspective API (Google)
- **What it does:** Toxicity scoring for text.
- **Gap:** Single-axis toxicity score. Not an epistemic framework.

### Epistemic Justice in AI (academic literature)
- **What it does:** Growing body of papers (Cambridge, Springer, ACM) on AI and epistemic injustice — Fricker's framework applied to AI.
- **What it doesn't do:** Theoretical analysis. Not operationalised as agent-loadable tooling. You cannot load a paper into ChatGPT.
- **Gap:** GoldBerry operationalises what this literature describes. The literature is the theory; GoldBerry is the tool.

---

## Category 3: Fact-Checking & Media Analysis

### ClaimBuster / Full Fact / Google Fact Check
- **What they do:** Verify factual claims against known facts.
- **Gap:** Fact-checking verifies what's stated. GoldBerry audits what's unstated. A fully fact-checked article can score 2.5/10 on GoldBerry — as the BBC analysis demonstrated.

### Media Bias Detector (UPenn/Annenberg)
- **What it does:** AI-powered bias detection in news articles. Selection bias, framing bias.
- **What it doesn't do:** Quantitative bias scoring, not multidimensional epistemic auditing. No named lenses, no Suffixscape, no concept of Deep History or Indigenous Knowledge.
- **Gap:** Detects bias in what's published. Doesn't identify what's structurally absent from knowledge production.

### GDELT / MediaCloud
- **What they do:** Large-scale quantitative media monitoring. Volume, sentiment, source tracking.
- **Gap:** Count coverage. GoldBerry audits what coverage excludes. Different layer.

---

## Category 4: Critical Thinking Frameworks

### Paul & Elder Critical Thinking Framework
- **What it does:** Pedagogical framework for developing critical thinking skills. Elements of thought, intellectual standards.
- **What it doesn't do:** Not operationalised for AI. Not loadable into an agent. No linguistic diagnostics. No satisfaction criteria per dimension.
- **Gap:** Designed for human classroom use. GoldBerry is designed for AI agent loading.

### Microsoft MMCTAgent (github.com/microsoft/MMCTAgent)
- **What it does:** Multi-modal critical thinking for visual reasoning. Planning, self-critique, tool-based reasoning.
- **What it doesn't do:** Visual reasoning only, not epistemic auditing of text/knowledge. No named epistemic lenses. No Suffixscape.
- **Gap:** Critical thinking about images, not about knowledge completeness.

### rfxlamia/skillkit — Framework Critical Thinking (LobeHub)
- **What it does:** Agent skill for metacognition and self-correction. Published March 2026.
- **What it doesn't do:** Generic metacognitive prompting. No specific epistemic lenses, no Suffixscape, no eval pack, no concept of structural absence.
- **Gap:** "Think critically" as a skill. GoldBerry specifies WHAT to think critically about across eight named dimensions.

---

## Category 5: Epistemic AI (closest adjacent projects)

### Epistemic Alignment Framework (arXiv 2504.01205, April 2025)
- **What it does:** Proposes ten challenges in knowledge transmission between users and LLMs. Philosophical framework for epistemic alignment.
- **What it doesn't do:** Theoretical paper. Not operationalised as agent-loadable files. No linguistic diagnostics. No eval pack. No open-source implementation.
- **Relationship to GoldBerry:** Complementary. Their ten challenges address user-LLM knowledge transmission. GoldBerry's eight lenses address what knowledge is structurally absent from LLM outputs. Different problems, compatible frameworks.
- **Gap:** Theory without tooling vs tooling grounded in theory.

### Epistemic AI (EU Horizon 2020 project, epistemic-ai.eu)
- **What it does:** Research project on worst-case guarantees for AI predictions through epistemic uncertainty modelling.
- **What it doesn't do:** Statistical uncertainty quantification, not epistemic completeness auditing. No lenses, no Suffixscape, no concept of absent knowledge traditions.
- **Gap:** "Epistemic" used in the statistical sense (uncertainty about model predictions) not the humanities sense (whose knowledge is represented).

### caspiankeyes/Epistemic-Audit-Anthropic-Case-Study (GitHub)
- **What it does:** A specific audit of Anthropic's systems via role-specific applications. Self-supervising audit methodology.
- **What it doesn't do:** Audits a specific company's systems, not a general-purpose framework. Not loadable into any agent. Not a reusable tool.
- **Gap:** Case study, not framework.

### addyvantage/Epistemic-Audit-Engine (GitHub)
- **What it does:** "Evidence-based AI verification system designed to surface epistemic confidence and detect hallucinations."
- **What it doesn't do:** Confidence scoring and hallucination detection. Not multidimensional epistemic auditing. No lenses, no Suffixscape, no concept of absence.
- **Gap:** Epistemic confidence ≠ epistemic completeness. Confidence asks "how sure are we?" GoldBerry asks "what's missing from the picture?"

### Thriveity Epistemic Audit Dashboard (thriveity.com)
- **What it does:** Evaluates content across five "trust-critical dimensions" for machine legibility and inference resilience.
- **What it doesn't do:** Focused on SEO/content credibility for AI ingestion, not on epistemic completeness of knowledge. No humanities-grounded lenses, no Suffixscape, no eval pack.
- **Gap:** Content trust signals for discoverability. Not knowledge completeness auditing.

---

## Category 6: Linguistic Analysis

### No directly comparable integrated tool found for the Suffixscape in this survey.

The Suffixscape detects:
- Nominalised evasion (process → entity, agency abstracted)
- Agency diffusion (passive voice hiding who decides)
- Epistemic inflation (claims of balance unsupported by evidence)
- Temporal flatness (present conditions as ahistorical baselines)

NLP tools exist for:
- Sentiment analysis (different axis)
- Named entity recognition (different purpose)
- Passive voice detection (one narrow piece of what the Suffixscape does)
- Readability scoring (different purpose)

No tool found in this survey combines these four specific diagnostics as an integrated epistemic instrument.

---

## Summary Matrix

*This matrix is a compression aid, not a substitute for the per-project notes above. Partial overlaps matter more than a simple tick/cross reading suggests.*

| Project | Agent-loadable | Epistemic auditing | Named lenses | Linguistic diagnostics | Eval pack | Self-aware limits | Open source |
|---------|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| **GoldBerry** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Guardrails AI | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ |
| NeMo Guardrails | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ |
| Llama Guard | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ |
| Constitutional AI | ❌ | ❌ | ❌ | ❌ | ❌ | Partial | ❌ |
| IBM AIF360 | ❌ | ❌ | ❌ | ❌ | Partial | ❌ | ✅ |
| Media Bias Detector | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Epistemic Alignment (arXiv) | ❌ | Partial | ✅ | ❌ | ❌ | ✅ | ❌ |
| Epistemic AI (EU) | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | Partial |
| Epistemic Audit Engine | ❌ | Partial | ❌ | ❌ | ❌ | ❌ | ✅ |
| Thriveity Dashboard | ❌ | Partial | Partial | ❌ | ❌ | ❌ | ❌ |
| MMCTAgent | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ |
| FCT Skill (rfxlamia) | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ |

---

## What We Can Learn From Each

- **Constitutional AI:** The principle of self-critique is powerful. GoldBerry already does this (Reflexive Audit). Worth monitoring how Anthropic evolves their constitution.
- **Epistemic Alignment Framework (arXiv):** The ten challenges are complementary to our eight lenses. Potential academic collaboration.
- **Epistemic justice literature:** The theoretical foundation GoldBerry operationalises. Cite this work properly.
- **Media Bias Detector:** Their quantitative methods could complement GoldBerry's structural analysis. Different layers, potentially stackable.
- **FCT Skill:** Shows the pattern of agent-loadable skills is emerging. GoldBerry is ahead but the format is becoming normalised.

---

## Conclusion

The survey suggests a real gap in the open-source landscape as currently inspected. No project found combines agent-loadable identity files, named epistemic lenses, a linguistic diagnostic layer, and inspectable evaluation artifacts. The closest projects operate in adjacent spaces — safety, bias, uncertainty, fact-checking — none of which address epistemic completeness as GoldBerry defines it.

We found no directly comparable integrated equivalent to the Suffixscape in this survey.

The current public position appears defensible, subject to continued challenge and updates. The distinctiveness is the combination, not any single feature.

---

*This document will be updated as new projects are identified. If you know of comparable work, please open an issue: github.com/PhamBit/goldberry/issues*

*© Cogniosynthesis Ltd. MIT Licensed.*
