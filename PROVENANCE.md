# GoldBerry — Provenance

## What this document is for

This document explains where GoldBerry came from.

It is a development-history document, not a claim of external validation. It tells readers:
- which kinds of practical work informed the framework
- what parts of that history are publicly inspectable today
- what claims remain partial, internal, or not yet published in full

If you want the shortest version: GoldBerry emerged from repeated applied use in journalism, institutional analysis, coalition intelligence, and legislative/policy work, then was formalised into a reusable framework.

---

## Development context

GoldBerry did not begin as a whiteboard abstraction. It was formalised after repeated use of related methods in live analytical settings.

Those settings reportedly included work associated with:
- **CognioNews** — news correction and framing analysis
- **CognioPublic** — institutional/public-body language audit
- **CognioCymru** — bilingual governance and cultural context work
- **CognioBridge** — coalition and network intelligence mapping
- **CognioEnacted** — legislative and policy mapping

In practical terms, this matters because the framework's categories were not chosen only for elegance. They were selected because they repeatedly exposed gaps in texts that otherwise looked finished.

---

## What is publicly inspectable in this repository

This repository currently makes the following public and inspectable:

- The canonical framework files in `agent-identity/`
- The reflexive self-audit in `REFLEXIVE-AUDIT-v1.md`
- Platform examples in `examples/`
- Worked examples in `case-studies/`
- Evaluation scaffolding in `evals/`
- A reference output schema in `schemas/`
- A minimal CLI/package in `src/goldberry/`

From a public-trust point of view, those are the real evidence surface today.

---

## What is not fully public here

This repository does **not** currently publish, in full:
- the underlying corpus said to have informed the framework
- a public dataset of all historical examples behind the origin story
- a full benchmark suite across multiple models
- a validated scoring study with inter-rater reliability
- public weights for any experimental GoldBerry-tuned model

That means readers should not infer more from this repository than it currently demonstrates.

---

## How to read the practical-origin claims

The practical-origin claims should be read as:
- evidence that the framework emerged from repeated applied use
- context for why these lenses were selected
- an explanation of the intellectual and operational setting

They should **not** be read as automatic proof that GoldBerry is:
- externally validated
- complete
- universally transferable
- superior in every context
- a substitute for direct human expertise or consultation

---

## Public status of major claims

A more explicit claims table lives in [`CLAIMS.md`](CLAIMS.md). In short:

### Publicly inspectable now
- the shape of the framework
- the language of the lenses
- the reflexive caveats
- the reference schema
- representative case studies
- the minimal tooling layer

### Partially inspectable / supported by narrative provenance
- the framework's emergence from operational use
- the connection to Cognio* projects named in repository materials
- the broad claim that repeated real-world use informed refinement

### Not yet publicly demonstrated in full
- the complete historical corpus
- the full training or tuning pipeline for any MiniLLM variant
- quantitative superiority claims across broad task classes

---

## On the “MiniLLM” material

Earlier GoldBerry materials have described an experimental small-model effort. That work should be treated as exploratory unless and until the repository publishes:
- model artifacts or weights
- training configuration
- evaluation results
- reproducible comparison methodology

Until then, the most credible public form of GoldBerry is the **framework**, not an implied model release.

---

## Why keep provenance at all?

Because provenance matters.

Without it, GoldBerry can look like a purely rhetorical prompt package. With it, readers can see that the framework was shaped by recurring problems in real analytical work.

But provenance only helps if it is paired with humility. This document is therefore deliberately narrower than a marketing narrative. It is meant to support inspection, not replace it.

---

## Limits and honesty clause

GoldBerry is a framework for structured epistemic auditing. It is not a guarantee of completeness.

Its strongest public claims, today, are:
- that it offers a coherent and inspectable lens-based framework
- that it has been revised to name some of its own blind spots
- that it provides a usable structure for more reflective analysis

Its weaker public claims, today, are any claims that depend on unpublished corpora, internal operational history, or unreleased model artifacts.

That is normal for an early open-source project, but it should be said plainly.

---

*Use the framework. Inspect the examples. Challenge the method. Do not mistake provenance for proof.*
