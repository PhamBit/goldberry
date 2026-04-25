# GoldBerry Claims Register

This file distinguishes between what the repository demonstrates publicly and what remains partial, contextual, or internal.

## Claim categories

- **Publicly inspectable** — a reader can verify this directly from repository contents
- **Partially inspectable** — the repo provides context or representative evidence, but not full proof
- **Internal / not yet published** — the repo mentions this as background, but does not yet publish the full supporting material

---

## Publicly inspectable claims

### Claim
GoldBerry is an eight-lens framework plus a linguistic diagnostic layer.

Status: **Publicly inspectable**

Evidence:
- `agent-identity/SOUL.md`
- `agent-identity/LENSES.md`
- `agent-identity/SUFFIXSCAPE.md`
- `agent-identity/AGENTS.md`

### Claim
GoldBerry explicitly names some of its own limitations.

Status: **Publicly inspectable**

Evidence:
- `REFLEXIVE-AUDIT-v1.md`
- `README.md`
- `PROVENANCE.md`

### Claim
This repository provides a reference schema and minimal tooling.

Status: **Publicly inspectable**

Evidence:
- `schemas/goldberry-output.schema.json`
- `src/goldberry/`
- `tests/`

---

## Partially inspectable claims

### Claim
GoldBerry emerged from repeated applied work rather than from abstract design alone.

Status: **Partially inspectable**

Evidence:
- `PROVENANCE.md`
- named project context in repository documentation
- representative case studies and framework structure

What is missing publicly:
- full underlying corpus
- comprehensive historical artifact set

### Claim
The framework was refined through operational feedback and reflexive audit.

Status: **Partially inspectable**

Evidence:
- `CHANGELOG.md`
- `REFLEXIVE-AUDIT-v1.md`
- versioned changes in framework files

What is missing publicly:
- full change log of operational iterations prior to repository publication

---

## Internal / not yet published claims

### Claim
A corpus of 12,000+ corrections informed the framework.

Status: **Internal / not yet published in full**

Evidence in repo:
- narrative mention in provenance materials

What would strengthen this publicly:
- representative dataset release
- data card
- methodology note
- public examples linked to the corpus

### Claim
An experimental GoldBerry MiniLLM or fine-tuning effort exists.

Status: **Internal / exploratory / not yet published in full**

Evidence in repo:
- narrative mention only

What would strengthen this publicly:
- model card
- training configuration
- evaluation results
- reproducible artifacts

### Claim
GoldBerry materially outperforms simpler prompting across broad tasks.

Status: **Not yet established publicly**

Evidence in repo:
- case studies and evaluation scaffolding only

What would strengthen this publicly:
- controlled comparisons
- evaluator notes
- benchmark publication

---

## Rule for future claims

If a claim cannot be inspected, compared, or reproduced from public materials, it should be presented as context or aspiration, not as settled proof.
