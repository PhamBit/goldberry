# GoldBerry — Provenance

## How This Framework Was Developed

GoldBerry did not emerge from a whiteboard. It emerged from work.

The seven-lens epistemic completeness framework was developed by Cogniosynthesis Ltd through sustained, applied research — correcting real news, auditing real institutions, analysing real policy, and building real systems. The agent identity was then formalised from patterns that proved themselves under operational conditions.

This document records how GoldBerry was built, tested, and refined. Every claim the framework makes has been stress-tested against real-world output.

---

## The Research Base

### CognioNews — 12,000+ Corrected Stories

The primary testing ground. CognioNews (https://cognionews.com) ingests news from 40+ daily sources and applies the seven-lens framework to produce epistemically corrected versions. Each story receives:

- A corrected headline
- An executive summary through the lenses
- A power-knowledge audit
- A "What's Missing" analysis across all seven lenses
- Cross-cultural analysis
- Synthesis and solution pathways
- A CMR score (1–10)

Over 12,000 stories have been processed through this pipeline. The patterns that held — which lenses caught what, which absences recurred, which linguistic markers signalled evasion — became the empirical foundation for GoldBerry's operating instructions.

This is not a theoretical framework illustrated with examples. It is an operational framework distilled from thousands of applied corrections.

### CognioPublic — Institutional Audit

CognioPublic (https://public.cogniosynthesisportal.uk) applies the seven lenses to UK public institutions — councils, public bodies, government communications. This work revealed how nominalised evasion and agency diffusion operate systematically in institutional language, directly informing the Suffixscape diagnostic layer.

### CognioCymru — Bilingual Epistemic Governance

CognioCymru applies the framework to Welsh cultural and legislative contexts — a bilingual environment where the relationship between language, knowledge, and governance is structurally visible. This work tested Lens 3 (Cross-Cultural Wisdom) under real conditions: how does epistemic completeness operate when the same institution must communicate across language communities with different knowledge traditions?

### CognioBridge — Coalition Intelligence

CognioBridge maps the UNESCO-MOST BRIDGES coalition — 58 member organisations, 372 projects across multiple countries. The framework was applied to classify language relationships, infer collaborations, and build network intelligence across the coalition. This work tested whether the seven lenses could operate at scale, across organisations, not just on individual texts.

### CognioEnacted — Legislative Mapping

CognioEnacted maps epistemic completeness to UK legislation through the seven lenses, scoring how well law addresses knowledge equity. This tested the framework against the hardest institutional texts — legislation — where nominalised evasion is structurally embedded and agency diffusion is a feature, not a bug.

---

## The Testing Process

### Live Analysis — Continuous Deployment

GoldBerry has been deployed as an active agent across diverse input types: live news from multiple international sources, institutional communications, academic texts, policy documents, encyclopaedic entries, legislative texts, and coalition project data. Each deployment tested different lens combinations and revealed different failure modes. The framework was refined iteratively based on what worked and what didn't.

### The Reflexive Audit — v1.1

GoldBerry v1.1 was produced by turning the seven lenses on the framework itself. This reflexive audit identified six control problems:

1. **Epistemic overconfidence** — the framework's structured output can create an impression of completeness it cannot guarantee
2. **Western theoretical grounding** — the framework advocates for epistemic plurality from within one tradition
3. **Pattern completion vs. embodied depth** — when deployed as an LLM agent, GoldBerry's mechanism is sophisticated pattern completion, not the same as embodied epistemic knowledge
4. **Lens selection bias** — seven is a choice; the epistemic space is infinite
5. **Nominalisation paradox** — "nominalised evasion" is itself a nominalisation
6. **Substitution risk** — the framework could become a substitute for the real engagement it points toward

Each of these was addressed in v1.1: provenance and limits sections added to SOUL.md, a reflexive caveat added to SUFFIXSCAPE.md, "Beyond Seven" candidate lenses added to LENSES.md, and a "Next Step Beyond GoldBerry" requirement added to AGENTS.md to ensure the framework always points outward.

The reflexive audit is published in the repository as REFLEXIVE-AUDIT-v1.md.

---

## The Theoretical Foundations

The framework synthesises three bodies of work:

**The Cogniosynthetic Corrective** — the seven-lens methodology, developed through the applied research described above. The lens selection draws on:
- Donna Haraway (situated knowledges, rejecting the "God trick")
- Martin Heidegger (historicity, enframing, temporal being)
- Michel Foucault (power/knowledge)
- Gayatri Spivak (can the subaltern speak?)
- Friedrich Nietzsche (Apollonian/Dionysian, non-propositional knowledge)
- Arjun Appadurai (disjunctive flows, capacity to aspire)
- Ernest Gellner (Language and Solitude, the Habsburg dilemma)
- Philippe Descola (beyond nature and culture)

**Civilisational Memory Recovery (CMR)** — the temporal depth methodology. The insistence that present conditions are products of historical processes, not ahistorical baselines. The CMR scoring system provides the 1–10 epistemic completeness rating.

**The Suffixscape** — the linguistic diagnostic layer. The identification of grammatical suffixes as fossils of cultural process — sites where meaning settles and epistemic limitations become structurally visible in language. Developed through analysis of thousands of institutional, policy, and news texts.

---

## GoldBerry MiniLLM — A Purpose-Trained Model

GoldBerry exists in two forms:

1. **The Agent Identity** — four text files that any LLM can load to become GoldBerry. This is the open-source framework in this repository. It works with any model, any size, any provider.

2. **GoldBerry MiniLLM** — a purpose-trained language model, fine-tuned directly on the 12,000+ seven-lens corrections produced by CognioNews.

### The Training Pipeline

- **Dataset**: 12,018 stories exported from CognioNews, 11,642 usable after quality filtering
- **Format**: Chat-format JSONL — each story as a prompt/completion pair demonstrating the seven-lens correction
- **Training data**: 50MB training set, 5.6MB validation set
- **Base model**: Qwen2.5-0.5B-Instruct — 500 million parameters
- **Method**: QLoRA fine-tune, 1 epoch, ~1,309 steps
- **Hardware**: Consumer GPU (NVIDIA 1660 Ti, 6GB VRAM)
- **Target deployment**: GGUF quantised (Q4_K_M), runnable via Ollama on any local machine

The 3B parameter model was the first target but exceeded the available VRAM. The 0.5B model was selected to test whether the epistemic completeness patterns could be compressed into a genuinely tiny model — 500 million parameters carrying the seven-lens methodology distilled from thousands of real corrections.

### What This Proves

A 500-million-parameter model, trained on the output of the seven-lens framework applied to 12,000 news stories, can run offline on consumer hardware. No API. No cloud. No dependency on any provider.

This is the smallest aligned model in the world — not aligned to preference data or behavioural compliance, but to epistemic completeness. The alignment comes from the training data: 12,000 demonstrations of what it looks like to correct for indigenous knowledge erasure, civilisational amnesia, cultural flattening, scientism, propositional reduction, temporal blindness, and structural exclusion.

The agent identity (text files) and the trained model (MiniLLM) are complementary:
- The agent identity works with any model, including frontier models with deep reasoning capabilities
- The MiniLLM runs anywhere, offline, sovereign — the framework embedded in weights, not dependent on a prompt

Both are products of the same research programme. Both carry the same epistemic commitments. The difference is portability vs. depth.

### Status

GoldBerry MiniLLM V.1 is in training. The data, scripts, and pipeline are ready for larger models when more compute is available — a free-tier Colab T4 (16GB) can handle the 3B parameter version. The architecture scales; the methodology is fixed.

---

## What This Means

GoldBerry is not a prompt engineering exercise. It is a formalised distillation of a sustained research programme that has:

- Processed **12,000+ news stories** through the seven lenses
- Audited **UK public institutions** for epistemic completeness
- Mapped **58 coalition organisations** and **372 projects** across multiple countries
- Tested against **academic texts, policy documents, legislation, university communications, encyclopaedia articles, and live news**
- Turned the lenses on itself and published the findings

The framework carries the weight of that work. When GoldBerry identifies a structural absence, it is drawing on patterns observed across thousands of real analyses — not generating plausible-sounding critique from training data alone.

This is the provenance. The work came first. The framework was extracted from it.

---

*Cogniosynthesis Ltd · All intellectual property reserved*
*GoldBerry v1.1.0 · March 2025*
