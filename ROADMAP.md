# GoldBerry Roadmap

## Product goal

Turn GoldBerry from a documentation-led framework repository into a credible open-source product for structured epistemic auditing.

Success means an outsider can:
1. understand what GoldBerry is quickly
2. run the reference tooling locally
3. inspect representative examples
4. validate outputs against a published schema
5. review public claims against public evidence
6. contribute safely and productively

---

## Phase 0 — Public trust surface

Status: in progress

Goals:
- tighten README messaging
- revise provenance and claims language
- add governance and contribution docs
- remove or explain ambiguities and missing references

Deliverables:
- `README.md`
- `PROVENANCE.md`
- `CLAIMS.md`
- `CONTRIBUTING.md`
- `CODE_OF_CONDUCT.md`
- `SECURITY.md`
- `LICENSE-NOTES.md`
- `ACT.md`

---

## Phase 1 — Inspectable evidence

Goals:
- publish worked examples
- add evaluation scaffolding
- define a stable rubric

Deliverables:
- `case-studies/`
- `evals/rubric.md`
- `EVALUATION.md`
- baseline and GoldBerry comparison examples

Exit criteria:
- at least 5 representative case studies
- at least 1 public rubric used consistently across examples

---

## Phase 2 — Reference implementation

Goals:
- provide a minimal but honest tooling layer
- support prompt assembly, scaffolding, and output validation

Deliverables:
- Python package in `src/goldberry/`
- CLI entry point `goldberry`
- reference schema in `schemas/`
- tests for prompt assembly and schema validation

Exit criteria:
- a new user can run `goldberry prompt`, `goldberry scaffold`, and `goldberry validate`

---

## Phase 3 — Reproducible evaluation

Goals:
- compare GoldBerry-structured prompting against simpler baselines
- document methodology and caveats
- reduce faux precision in scoring

Deliverables:
- prompt sets
- model settings documentation
- evaluator guidance
- score-band language instead of overconfident single-point claims where appropriate

Exit criteria:
- at least one reproducible comparison pack across multiple prompts

---

## Phase 4 — Contributor ecosystem

Goals:
- support external contributions without diluting the framework
- formalise how lens changes and methodology proposals are handled

Deliverables:
- lens proposal template
- case-study submission template
- eval contribution guidelines
- maintainership rules

Exit criteria:
- clear path for docs, integration, and evaluation contributions

---

## Phase 5 — Optional product expansion

Possible future work:
- hosted playground
- browser extension or article auditor
- richer local integrations
- model-specific adapters
- public dataset release where lawful and appropriate
- experimental model release backed by published evaluation

This phase should happen only after Phases 0–3 are strong.

---

## Release framing

Suggested milestones:
- **v0.1.0** — trustworthy docs + governance + examples
- **v0.2.0** — reference CLI and schema
- **v0.3.0** — public evaluation pack
- **v0.4.0** — contributor workflows and templates
- **v1.0.0** — stable framework + stable schema + reproducible examples + clear trust surface
