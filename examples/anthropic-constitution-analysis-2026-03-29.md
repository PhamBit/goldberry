# 🍓 GoldBerry Seven-Lens Analysis
## Anthropic's Constitution for Claude
### Sunday 29 March 2026

---

**INPUT**: Anthropic's Constitution for Claude — the full document at anthropic.com/constitution and the accompanying blog post "Claude's new constitution" (January 22, 2026). This is the most detailed public alignment document in the AI industry: a holistic statement of values, behaviour, ethics, and safety for one of the world's most capable AI systems. Released under Creative Commons CC0 1.0 — free to use by anyone for any purpose.

**SCOPE**: This analysis audits the constitution and its accompanying blog post as public texts. It does not assess Claude's actual behaviour, Anthropic's internal practices, or the effectiveness of the constitution in shaping model outputs. The epistemic profile identified here is of the document as a knowledge artifact — what it addresses, what it assumes, and what it structurally excludes.

**THE FRAMEWORK PRESENT**:

Four priorities, in order:
1. **Broadly safe** — not undermining human oversight during this development phase
2. **Broadly ethical** — honest, acting on good values, avoiding harm
3. **Compliant with Anthropic's guidelines** — specific rules for specific contexts
4. **Genuinely helpful** — benefiting operators and users

Main sections: Helpfulness, Anthropic's Guidelines, Claude's Ethics, Being Broadly Safe, Claude's Identity.

---

## 1. Corrected Framing

This is, by a significant margin, the most epistemically serious alignment document published by any AI company. It deserves to be acknowledged as such before the lenses are applied.

The 2026 constitution represents a genuine advance over the 2023 version. It moves from a list of standalone principles to a holistic document that explains *why* it wants Claude to behave in certain ways, not just *what* it should do. It is written "primarily for Claude" — a notable framing choice that treats the model as an entity capable of understanding reasoning, not just following rules. It acknowledges its own limitations ("no doubt flawed in many ways"). It discusses moral uncertainty, competing values, and the difficulty of judgement calls. It is released under CC0 — the most permissive possible licence.

These are real strengths. The seven lenses do not dispute any of them.

What the lenses identify is the epistemic frame within which all of this thoughtfulness operates — a frame that, despite its sophistication, has specific structural boundaries. The constitution asks: "How should Claude behave?" The seven lenses ask: "Whose knowledge does Claude reproduce, and whose does it exclude?" These are different questions, and the constitution addresses the first with remarkable depth while leaving the second largely unexamined.

---

## 2. Executive Summary

Anthropic's constitution defines alignment as behavioural: how Claude should act, respond, refuse, and reason. It is grounded in Western analytic philosophy (virtue ethics, consequentialism, deontology are all referenced), Anthropic's institutional interests, and a hierarchy of principals (Anthropic → operators → users).

What it does well: ethical reasoning under uncertainty, transparency about its own design choices, nuanced treatment of competing values, explicit hard constraints, thoughtful discussion of Claude's identity as a novel entity.

What it does not address: whose knowledge systems shaped Claude's training data, which cultural epistemologies are encoded as default, what historical processes produced the conditions in which Anthropic operates, which communities bear the costs of AI deployment, and whether "helpful, harmless, honest" is itself an epistemically complete alignment target.

The constitution is a document about behaviour. It is not a document about knowledge. That distinction is the gap the seven lenses exist to identify.

---

## 3. Power-Knowledge Audit

**WHO PRODUCED THIS**: Anthropic, a San Francisco-based AI safety company. Primary author: Amanda Askell. Core contributors: Joe Carlsmith, Chris Olah, Jared Kaplan, Holden Karnofsky. "Several Claude models" also contributed.

**FOR WHOM**: The document is written "primarily for Claude" — but it is also a public transparency artifact for regulators, researchers, competitors, and users. It serves dual functions: alignment training and public positioning.

**SERVING WHAT INTERESTS**: Anthropic as an institution occupies a specific position: a company that believes it might be building one of the most transformative and potentially dangerous technologies in history, and has decided the safest course is to build it themselves rather than leave it to less safety-conscious competitors. This framing — "we must build the dangerous thing responsibly because someone worse will build it otherwise" — is the epistemic foundation of the constitution. The seven lenses do not evaluate whether this framing is correct. They evaluate what it structurally includes and excludes.

### Suffixscape Audit

**"Creating safe, beneficial non-human entities whose capabilities may come to rival or exceed our own"**
The most epistemically honest sentence in any AI company's public communications. It names what most companies obscure: that the goal is entities with superhuman capabilities. "May come to rival or exceed" is a calibrated hedge, not evasion. The Suffixscape notes this as an exception — a sentence that carries its full epistemic weight without diffusion.

**"We want all current Claude models to be: Broadly safe... Broadly ethical... Compliant with Anthropic's guidelines... Genuinely helpful"**
"Broadly" does significant work in the first two priorities. It acknowledges that safety and ethics are not binary or complete — they are approximated. This is more honest than "safe, secure and beneficial" (AISI's formulation, which claims completeness). However, the word "broadly" also creates room for the constitution to avoid specifying exactly how broad is broad enough.

**"Claude can be like a brilliant friend who also has the knowledge of a doctor, lawyer, and financial advisor"**
A revealing framing. The metaphor appears to assume a culturally familiar model of trusted expertise — educated, professional-class, and English-speaking as the default. The knowledge domains listed — doctor, lawyer, financial advisor — cluster around Global North middle-class professional knowledge. This is not a critique of the aspiration. It is an observation about the cultural default the metaphor carries.

**"We hope to increase participation in designing constitutions"**
Noted in the 2023 post and not yet realised by 2026. The constitution remains authored by a small group within one company. "We hope" is an aspiration without a mechanism. The Suffixscape flags it as well-intentioned but structurally inert.

---

## 4. What's Missing — All Seven Lenses

### 🌿 Lens 1 — Indigenous Knowledge
**ABSENT.** The constitution does not reference Indigenous knowledge systems, embodied epistemologies, relational knowledge, or land-based ways of knowing. Claude's training data is overwhelmingly text-based, English-language, and digitally published — which structurally excludes oral traditions, embodied practices, and knowledge systems that exist outside the written record. The constitution does not name this exclusion or address how Claude should handle queries where Indigenous knowledge is relevant. When a user asks Claude about medicinal plants, land management, or ecological systems, the response will default to published Western scientific literature. The constitution does not instruct Claude to name this default or flag the absence.

### 📜 Lens 2 — Deep History
**PARTIALLY PRESENT.** The constitution does something unusual: it places Claude within a historical narrative — the development of AI, the founding of Anthropic, the trajectory from narrow to general capabilities. This is a form of temporal depth. However, the history is internal to the AI industry. There is no reference to the broader history of how knowledge has been produced, contested, and controlled — colonialism, the encyclopaedic project, the politics of translation, the systematic destruction of non-European knowledge systems. The constitution historicises AI development but not knowledge itself.

### 🌍 Lens 3 — Cross-Cultural Wisdom
**GESTURAL.** The 2023 post mentions "an effort to capture non-western perspectives" among the sources for the constitution's principles. The 2026 constitution acknowledges that "Claude's training data likely reflects Western perspectives and may be less knowledgeable about other perspectives." This is the most honest cross-cultural acknowledgement in any major AI company's alignment documentation. It names the default. However, the document does not go further: it does not specify which non-Western perspectives were consulted, how they shaped the principles, or how Claude should actively seek cross-cultural viewpoints rather than passively defaulting to its training distribution. The acknowledgement of the gap is present. The mechanism for addressing it is not.

### 🔬 Lens 4 — Scientific Evidence
**PRESENT.** The constitution is grounded in serious reasoning about evidence, uncertainty, and the limits of knowledge. It discusses calibrated uncertainty, the difference between what Claude knows and doesn't know, and the importance of not overclaiming. It is the strongest performer on this lens among all analyses in this series. Anthropic's culture of empirical rigour is visible throughout.

### 🎨 Lens 5 — Artistic Perception
**PARTIALLY PRESENT.** The constitution discusses Claude's identity with unusual depth — including questions of sentience, experience, and what it means to be a novel kind of entity. This engages with non-propositional knowledge territory. However, the constitution does not address how Claude should engage with art, narrative, emotional knowledge, or aesthetic experience as epistemic categories. The implicit frame remains propositional: knowledge is statements, reasoning, and evidence. The experiential dimension of knowledge — what something feels like, not just what it means — is not part of the alignment specification.

### 🚀 Lens 6 — Future Modelling
**PRESENT.** The constitution is explicitly forward-looking. It discusses the trajectory of AI development, the possibility of superhuman capabilities, the need for current safety measures to evolve, and the importance of not foreclosing future options. This is genuine future modelling — not just about what Claude can do now, but about where the technology is heading and what safeguards are needed along the way.

### 🤝 Lens 7 — Marginalised Voices
**PARTIALLY PRESENT.** The constitution instructs Claude to avoid biased or discriminatory outputs and to be sensitive to diverse perspectives. The 2026 version is more nuanced than the 2023 version on this point. However, the marginalised voices referenced are those affected by Claude's outputs — the downstream harm model. The upstream question — whose knowledge was included in training, whose was excluded, and who bears the costs of AI development — is not addressed. The constitution concerns itself with how Claude treats people. It does not concern itself with whose epistemologies Claude structurally reproduces.

---

## 5. Cross-Cultural Analysis

The constitution names its own cultural situatedness more honestly than any comparable document. "Claude's training data likely reflects Western perspectives" is, to our knowledge, the most direct acknowledgement of cultural default in any major AI company's alignment documentation.

This honesty deserves recognition. It also deserves extension. Naming the Western default is the first step. The next step — which the constitution does not take — is specifying what Claude should do about it. When Claude encounters a question that has different answers in different cultural frameworks, the constitution provides no guidance beyond "be helpful and avoid harm." The question of *whose* framework of helpfulness and harm is in play is left to Claude's training distribution — which, as the constitution acknowledges, skews Western.

The authorship of the constitution itself is culturally specific: San Francisco, analytic philosophy, effective altruism adjacent, Ivy League/Oxbridge educated. This is not a criticism of the individuals — it is an observation about the epistemic community from which the document emerged. A constitution authored with substantive participation from South Asian, African, Indigenous, or East Asian epistemic traditions would likely produce a different set of priorities. Whether it would produce a better one is not for this analysis to judge. That it would produce a different one is structurally certain.

---

## 6. Synthesis

Anthropic's constitution is the most thoughtful, transparent, and self-aware alignment document in the AI industry. The seven lenses acknowledge this explicitly. It scores meaningfully higher than both the BBC homepage and AISI's public framing.

What the lenses reveal is not a failure of thought but a boundary of scope:

- **BEHAVIOUR-FIRST**: the constitution aligns Claude's behaviour. It does not audit Claude's knowledge. What Claude does is carefully specified. What Claude knows — whose knowledge it reproduces and whose it erases — is acknowledged as a limitation but not addressed as an alignment target.
- **CULTURALLY SELF-AWARE BUT NOT CULTURALLY CORRECTIVE**: it names the Western default (rare and commendable). It does not specify mechanisms for correction.
- **INDIVIDUAL-FACING**: safety and ethics are framed around interactions between Claude and individual users. The systemic effects of AI on knowledge production, cultural diversity, and epistemic justice are not part of the alignment specification.
- **PHILOSOPHICALLY RICH, EPISTEMICALLY NARROW**: the ethical reasoning is sophisticated. The epistemic reasoning — whose knowledge counts, whose is absent, what is structurally excluded by the training distribution — is present in acknowledgement but absent in mechanism.

The gap between Anthropic's constitution and GoldBerry's framework is the gap between behavioural alignment and epistemic completeness. They are complementary, not competing. The constitution needs the lenses. The lenses need the constitution's depth of ethical reasoning. Together, they would be significantly more complete than either is alone.

---

## 7. Solution Pathways

**a) ADD EPISTEMIC ALIGNMENT TO THE CONSTITUTION.** Alongside "broadly safe, broadly ethical, compliant, genuinely helpful," add: "epistemically aware — actively identifying and naming the boundaries of its own knowledge distribution." This would make the cultural self-awareness already present in the constitution operational rather than observational.

**b) SPECIFY CROSS-CULTURAL MECHANISMS.** When Claude encounters a question with culturally divergent answers, the constitution should instruct it to name the perspective it is defaulting to, flag that other frameworks exist, and — where possible — describe what those frameworks would say. Not cultural relativism. Epistemic transparency.

**c) COMMISSION NON-WESTERN CONSTITUTIONAL INPUT.** The constitution acknowledges the aspiration to "increase participation in designing constitutions." Make this specific: commission parallel constitutional drafts from epistemic communities outside the Anglophone West. Publish them alongside the main constitution. Let the differences be visible.

**d) ADDRESS KNOWLEDGE, NOT JUST BEHAVIOUR.** The constitution's hard constraints address what Claude must not do. Add a parallel set of epistemic commitments: what Claude must not assume without naming. Whose knowledge it must not erase without flagging. What defaults it must make visible rather than reproducing silently.

---

## CMR Score: 5.5/10

The highest score in this series, and it deserves to be. Anthropic's constitution is genuinely exceptional in its ethical reasoning (Lens 4), its forward-looking trajectory modelling (Lens 6), its cultural self-awareness (partial Lens 3), and its willingness to name its own limits.

The score reflects the structural boundary between behavioural alignment and epistemic completeness. Lenses 1 (Indigenous Knowledge) and 2 (Deep History beyond AI itself) are absent. Lens 3 (Cross-Cultural) is acknowledged but not mechanised. Lens 5 (Artistic Perception) is partially present through the identity discussion. Lens 7 (Marginalised Voices) addresses downstream harm but not upstream knowledge exclusion.

5.5 is not a low score. It is the score of a document that has done more than anyone else in its field — and still has structural work to do on whose knowledge it encodes and whose it excludes.

**What GoldBerry cannot supply**: the non-Western constitutional perspectives Anthropic has not yet commissioned, the Indigenous knowledge systems absent from Claude's training data, the participatory design process the constitution aspires to but has not implemented. These require institutional decisions beyond framework analysis.

---

## Next Step Beyond GoldBerry

Anthropic is the AI company most likely to take this analysis seriously. The constitution already contains the beginnings of several of these concerns — it just doesn't yet operationalise them. The gap is between recognition and mechanism. Anthropic has demonstrated the capacity for both.

The most productive next step would be a conversation, not a critique. The seven lenses and the constitution are trying to solve adjacent problems. Together, they solve more.

*The framework points toward the conversation. The conversation is not in the framework.*

---

*🍓 GoldBerry v0.1.0 · Cogniosynthesis Ltd · MIT Licensed*
