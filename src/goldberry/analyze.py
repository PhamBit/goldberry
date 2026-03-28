from __future__ import annotations

from typing import Any

from .prompts import build_system_prompt, build_user_prompt


def scaffold_output(user_input: str) -> dict[str, Any]:
    return {
        "corrected_framing": "State what the original framing misses or assumes.",
        "executive_summary": f"Analyse this input through the GoldBerry framework: {user_input[:120]}",
        "power_knowledge_audit": "Identify who produced the framing, whose interests are served, and where agency is obscured.",
        "whats_missing": {
            "indigenous_knowledge": "Name relevant embodied or relational knowledge not represented.",
            "deep_history": "Name the historical process missing from the immediate framing.",
            "cross_cultural_wisdom": "Name cultural assumptions or untranslated perspectives.",
            "scientific_evidence": "State what evidence is present, absent, or overclaimed.",
            "artistic_perception": "State what affective, symbolic, or narrative dimension is missing.",
            "future_modelling": "State what trajectories, risks, or downstream effects are not addressed.",
            "marginalised_voices": "State whose perspective is structurally absent.",
        },
        "cross_cultural_analysis": "Compare the apparent frame with relevant alternative knowledge traditions or cultural assumptions.",
        "synthesis": "Integrate the lens findings into a coherent whole without claiming final completeness.",
        "solution_pathways": [
            "Gather missing evidence or perspectives before acting.",
            "Test whether the current framing obscures power, history, or exclusion.",
        ],
        "cmr_score": "5-6",
        "score_caveat": "Framework-internal qualitative assessment only; not an externally validated measurement.",
        "lens_limitations": [
            "GoldBerry cannot substitute for direct consultation or domain expertise.",
            "The seven lenses are a finite selection, not exhaustive coverage.",
        ],
        "next_step_beyond_goldberry": "Identify the real people, communities, records, or expertise that must be engaged beyond this framework.",
    }


def prompt_packet(user_input: str) -> str:
    return "\n\n".join(
        [
            "# GoldBerry System Prompt",
            build_system_prompt(),
            "# GoldBerry User Prompt",
            build_user_prompt(user_input),
        ]
    )
