# GoldBerry Evaluation Runbook

## Purpose

This runbook explains how to reproduce the small public comparison pack in this repository.

## Directory layout

- `prompts/` — prompt fixtures and source text
- `baselines/` — saved baseline outputs
- `goldberry/` — saved GoldBerry structured outputs
- `results/` — evaluator notes and comparison summaries

## Minimal reproduction workflow

1. Choose a prompt file from `evals/prompts/`.
2. Run a baseline condition using the baseline prompt in that file.
3. Run a GoldBerry condition using the identity files or the `goldberry prompt` scaffolding.
4. Save the outputs.
5. If the GoldBerry output is JSON, validate it:

```bash
goldberry validate evals/goldberry/<file>.json
```

6. Score both outputs against `evals/rubric.md`.
7. Save evaluator notes in `evals/results/`.

## Suggested discipline

- Keep the model constant where possible.
- Record the date and model used.
- Preserve the original prompt wording.
- Publish failure cases, not just flattering examples.
- Use the rubric to justify claims of improvement.

## Important caution

This comparison pack is a public inspection aid, not a claim of comprehensive validation.
