# Contributor Protocol for Comparison Packs

## Purpose

This protocol is for contributors who want to submit public comparison packs that are more useful than promotional examples.

## Minimum submission standard

A comparison pack should include:
- a prompt fixture or input text
- a baseline prompt and output
- a GoldBerry prompt condition and output
- evaluator notes using the rubric
- at least one explicit limitation note

## Submission workflow

1. Add or reference a prompt in `evals/prompts/`.
2. Save the baseline output in `evals/baselines/`.
3. Save the GoldBerry output in `evals/goldberry/`.
4. Validate GoldBerry JSON outputs when applicable.
5. Add evaluator notes in `evals/results/`.
6. If helpful, include a longer narrative case study in `case-studies/`.

## Naming convention

Use the same stem across files where possible.

Example:
- `evals/prompts/news-traffic.md`
- `evals/baselines/news-traffic.md`
- `evals/goldberry/news-traffic.json`
- `evals/results/news-traffic-evaluator-notes.md`

## What makes a submission credible

Prefer:
- ordinary or mildly adversarial examples
- prompts where baseline is decent, not ridiculous
- notes on where GoldBerry adds structure rather than just more words
- honest failure cases

Avoid:
- straw-man baselines
- cherry-picked triumphalism
- claims of validation unsupported by the materials
- treating GoldBerry output as if it were ground truth

## Recommended reviewer questions

- Did GoldBerry genuinely surface relevant absences?
- Did it merely sound deeper, or was it actually more inspectable?
- Did it introduce speculative critique unsupported by the source?
- Did it disclose its limits clearly enough?

## Useful commands

```bash
. .venv/bin/activate
python -m pytest -q
goldberry validate evals/goldberry/<file>.json
```
