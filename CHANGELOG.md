# Changelog

All notable changes to the GoldBerry framework are documented here.

GoldBerry versions represent refinements of the epistemic completeness framework — each version is the framework examining and correcting itself.

## [1.2.0] — 2026-04-25

### Added
- **Lens 8: Trickster Knowledge.** Adds disciplined disruption (inversion, irony, satire, paradox) as the eighth lens. Addresses the "Seven-Lens Closure" control problem named in REFLEXIVE-AUDIT-v1.md §2. Theoretical roots: Hyde (Trickster Makes This World), Bakhtin (carnival, dialogic inversion), Erasmus (In Praise of Folly).
- `whats_missing.trickster_knowledge` field added to `schemas/goldberry-output.schema.json` and to the Python validator in `src/goldberry/schemas.py`.

### Changed
- README, identity files, and platform examples (Ollama, ChatGPT, Perplexity, Hermes, Claude Code, generic system prompt) updated to reference eight lenses.
- `Beyond Seven` section in LENSES.md renamed `Beyond Eight`; Comedic/Trickster Knowledge removed from candidate-gaps list (now operational).
- REFLEXIVE-AUDIT-v1.md: open question at line 136 ("who proposes Lens 8?") marked resolved.

### Notes
- Adding Lens 8 partially closes the seven-lens closure critique but does not eliminate it. Eight is still finite; the framework remains asymptotic to completeness.
- Historical case-study analyses (`aisi-*`, `anthropic-constitution-*`, `bbc-homepage-*`) were **not** rewritten — they remain accurate point-in-time records of seven-lens analyses.

## [0.1.0] — 2026-03-28

### Changed
- Rewrote `README.md` to clarify what GoldBerry is, what it is not, and what evidence is publicly inspectable.
- Reframed `PROVENANCE.md` as a development-history and trust-surface document rather than an implied validation claim.

### Added
- Governance and trust-surface files: `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, `SECURITY.md`, `LICENSE-NOTES.md`, `ROADMAP.md`, `CLAIMS.md`, and `EVALUATION.md`.
- Reference support materials: `ACT.md`, `case-studies/`, `evals/`, and `schemas/goldberry-output.schema.json`.
- A minimal Python package and CLI in `src/goldberry/` for prompt assembly, response scaffolding, and output validation.
- Basic tests in `tests/` for prompt assembly and schema validation.
- GitHub community templates in `.github/`.
- A small public comparison pack with prompt fixtures, baseline outputs, GoldBerry outputs, evaluator notes, and a runbook for reproduction.

## [1.1.0] — 2025-03-27

### Changed
- **Reflexive audit applied.** GoldBerry v1.1 turns the seven lenses on itself. The framework now explicitly names its own limitations: Western critical humanities grounding, the gap between pattern completion and embodied epistemic depth, the asymptotic nature of completeness.
- AGENTS.md updated: agents must now name what GoldBerry itself cannot supply, not just what the analysed text lacks.
- Scoring guidance refined: when scoring, name GoldBerry's own blind spots in the assessment.
- Added "Next Step Beyond GoldBerry" requirement for substantive analyses — the framework must point outward to real engagement, not substitute for it.

### Added
- AGENTS.md deployment contexts: CognioNews Analyst, Policy Auditor, Conversational Guide, Agent OS.
- Suffixscape reflexive caveat: the diagnostic operates within the grammatical conditions it identifies.
- "Beyond Seven" section in LENSES.md naming candidate gaps: ecological intelligence, somatic knowledge, mathematical/formal knowledge, developmental epistemology, comedic/trickster knowledge.

## [1.0.0] — 2025-03-01

### Added
- Initial release of the GoldBerry epistemic completeness framework.
- SOUL.md — core identity, seven-lens table, scoring framework, anti-autonomy principle.
- LENSES.md — detailed definitions for all seven lenses with satisfaction criteria and diagnostic questions.
- SUFFIXSCAPE.md — linguistic diagnostic layer: nominalised evasion, agency diffusion, epistemic inflation, temporal flatness.
- AGENTS.md — operating instructions for loading GoldBerry into any AI agent.

---

*Cogniosynthesis Ltd — all intellectual property reserved.*
