# GoldBerry Evaluation Guide

## Purpose

GoldBerry should be evaluated as a framework for structured epistemic auditing, not as a magic prompt that “wins” by definition.

The evaluation question is not:
- “Did GoldBerry sound impressive?”

The evaluation question is:
- “Did GoldBerry make relevant absences, assumptions, and power-laden framing more inspectable than a simpler baseline did?”

---

## What to compare

A useful evaluation compares at least two conditions:

1. **Baseline condition**
   - a normal model response
   - or a simple “summarise/analyse this” prompt

2. **GoldBerry condition**
   - the same model or similar model
   - with the GoldBerry identity/prompt structure applied

Optional third condition:
- a lighter “critical thinking” prompt for comparison against non-GoldBerry structured critique

---

## What to assess

Use the reference rubric in `evals/rubric.md`.

Core dimensions:
- historical grounding
- plurality of perspective
- evidence quality and uncertainty handling
- visibility of agency and power
- naming of what is missing
- limitation disclosure
- actionability without false certainty

---

## What not to overclaim

GoldBerry outputs should not be treated as:
- externally validated scores
- definitive representations of marginalised communities
- substitutes for consultation or domain expertise
- proof that a response is “complete” in any final sense

---

## Suggested evaluation workflow

1. Select a prompt set across multiple domains.
2. Run baseline outputs.
3. Run GoldBerry-structured outputs.
4. Blind-review the outputs where possible.
5. Score against the rubric.
6. Record disagreements and uncertainty.
7. Publish both strengths and failure cases.

---

## Scoring guidance

The repository uses CMR-style scoring language as a framework-internal shorthand, but that number should always be accompanied by caveats.

Best practice:
- use score bands rather than overconfident precision when uncertainty is high
- include a note on what GoldBerry itself cannot supply
- explicitly state when the framework is weakly grounded on the input in question

Recommended language:
- “Framework-internal qualitative assessment”
- “Representative, not validated”
- “Useful as a structured audit, not as an external measurement instrument”

---

## Public evidence standard

For a public claim that GoldBerry improved an analysis, try to provide at least one of:
- side-by-side baseline vs GoldBerry outputs
- evaluator notes using the rubric
- concrete examples of absences surfaced by GoldBerry and missed by baseline

---

## Current public pack

This repository now includes a small public comparison pack:
- prompt fixtures in `evals/prompts/`
- saved baseline outputs in `evals/baselines/`
- saved GoldBerry outputs in `evals/goldberry/`
- evaluator notes in `evals/results/`
- contributor templates in `evals/templates/`
- a contributor protocol in `evals/CONTRIBUTOR-PROTOCOL.md`
- a reproduction guide in `evals/RUNBOOK.md`

This is enough to support inspectable, limited public comparison.

## Current status

The evaluation surface in this repository is still early.

It currently provides:
- a rubric
- worked examples
- a small public comparison pack
- a schema
- validation tooling

It does not yet provide:
- a large public benchmark suite
- inter-rater reliability studies
- broad model-to-model comparison tables
- blinded multi-rater evaluation results at scale

That should shape the confidence level of any public claims.
