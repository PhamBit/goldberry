# GoldBerry v0.1.0 — Public Foundation Release

## Summary

This release turns GoldBerry from a documentation-heavy concept repository into a more credible open-source foundation for structured epistemic auditing.

v0.1.0 focuses on four things:
- clearer public framing
- a stronger trust surface
- inspectable examples and evaluation artifacts
- a minimal runnable tooling layer

## Highlights

### 1. Reframed repository positioning
- Rewrote `README.md` to clearly state what GoldBerry is and is not.
- Reworked `PROVENANCE.md` so provenance supports context rather than overclaiming validation.
- Added `CLAIMS.md` to separate publicly inspectable claims from partial or internal claims.

### 2. Governance and contributor readiness
- Added `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, `SECURITY.md`, `LICENSE-NOTES.md`, and `ROADMAP.md`.
- Added GitHub issue and PR templates.

### 3. Reference artifacts
- Added `schemas/goldberry-output.schema.json`.
- Added `ACT.md` as the deeper reference document linked from `AGENTS.md`.
- Added worked examples in `case-studies/`.

### 4. Public comparison pack
- Added prompt fixtures in `evals/prompts/`.
- Added saved baseline outputs in `evals/baselines/`.
- Added saved GoldBerry structured outputs in `evals/goldberry/`.
- Added evaluator notes and summary tables in `evals/results/`.
- Added `evals/RUNBOOK.md` and contributor templates/protocols for future comparison packs.

### 5. Minimal CLI and tests
- Added a Python package in `src/goldberry/`.
- Added CLI commands for prompt assembly, output scaffolding, case-study listing, and JSON validation.
- Added basic tests in `tests/`.

### 6. Static site rewrite
- Reworked the static site copy to match the repository's clearer, more evidence-grounded framing.
- Replaced hype-forward language with framework, trust-surface, and limits language.

## Validation completed locally

- `python -m pytest -q`
- `goldberry validate evals/goldberry/news-traffic.json`
- `goldberry validate evals/goldberry/policy-empowerment.json`
- `goldberry validate evals/goldberry/research-tutoring.json`

## Known limits

This release is still early.

It does not yet provide:
- a large public benchmark suite
- multi-rater reliability studies
- broad cross-model comparison tables
- a public model release with published evaluation

## Recommended next steps

- expand the public comparison pack across more domains
- add evaluator-contribution reviews from multiple people
- align the static site and GitHub release page with the same trust-surface framing
- prepare a v0.2.0 focused on richer integrations and more comparison artifacts
