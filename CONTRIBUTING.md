# Contributing to GoldBerry

Thanks for your interest in contributing.

GoldBerry is a framework project. Good contributions improve one or more of the following:
- clarity
- rigor
- portability
- inspectability
- reproducibility

## Ways to contribute

### 1. Documentation improvements
Examples:
- clearer wording
- broken links
- consistency fixes
- better explanation of limitations

### 2. Case studies
Add worked examples that show:
- the original input
- a baseline or flatter analysis
- a GoldBerry-structured analysis
- commentary on what changed and what still remains missing

### 3. Evaluation work
Useful additions:
- better rubrics
- prompt sets
- comparison methodology
- evaluator guidance
- score-caveat language
- public comparison packs using the templates in `evals/templates/` and the protocol in `evals/CONTRIBUTOR-PROTOCOL.md`

### 4. Integrations
Examples:
- ChatGPT instructions
- Claude/Claude Code workflows
- Hermes skills
- Ollama packaging
- editor integrations

### 5. Framework development
High-bar contributions include:
- lens refinement proposals
- theoretical gap analysis
- critique of current blind spots
- stronger caveat language where the framework overstates itself

## Before you start

Please read:
- `README.md`
- `PROVENANCE.md`
- `CLAIMS.md`
- `EVALUATION.md`
- `evals/rubric.md`
- `evals/CONTRIBUTOR-PROTOCOL.md`
- `LICENSE-NOTES.md`

## Contribution principles

1. Be concrete.
Ground claims in text, examples, or reproducible comparisons.

2. Be honest about uncertainty.
Do not present framework-internal judgement as scientific validation.

3. Prefer inspection over rhetoric.
A sample, schema, test, or rubric improvement is usually more valuable than a grand claim.

4. Preserve the anti-oracle stance.
GoldBerry is an instrument, not an authority that overrides human judgement.

5. Name limits explicitly.
If a contribution strengthens GoldBerry's honesty, that is a feature, not a weakness.

## Pull request expectations

A good PR should include:
- a clear summary of what changed
- why the change helps users or contributors
- any relevant examples, screenshots, or before/after text
- tests for code changes where appropriate

## For framework or lens proposals

Please include:
- the failure mode being addressed
- why existing lenses do not cover it adequately
- example inputs where the gap is visible
- risks introduced by the proposed change
- whether the change is a new lens, refinement, or evaluation guideline

## Code changes

If you modify the Python package:

```bash
python3 -m pip install -e .
python3 -m pytest -q
```

## Scope boundaries

GoldBerry welcomes contribution, but maintainers may decline changes that:
- overstate validation or certainty
- weaken the explicit limitations of the framework
- add complexity without improving inspectability or usability
- turn the project into vague branding rather than a testable framework

## Questions

Open an issue or discussion with:
- the concrete problem
- the text/example you are working from
- the change you think would help
