from __future__ import annotations

from typing import Any

REQUIRED_TOP_LEVEL_FIELDS = [
    "corrected_framing",
    "executive_summary",
    "power_knowledge_audit",
    "whats_missing",
    "cross_cultural_analysis",
    "synthesis",
    "solution_pathways",
    "cmr_score",
    "score_caveat",
    "lens_limitations",
    "next_step_beyond_goldberry",
]

REQUIRED_WHATS_MISSING_FIELDS = [
    "indigenous_knowledge",
    "deep_history",
    "cross_cultural_wisdom",
    "scientific_evidence",
    "artistic_perception",
    "future_modelling",
    "marginalised_voices",
    "trickster_knowledge",
]


def validate_output(data: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    for field in REQUIRED_TOP_LEVEL_FIELDS:
        if field not in data:
            errors.append(f"Missing top-level field: {field}")

    if errors:
        return errors

    for field in [
        "corrected_framing",
        "executive_summary",
        "power_knowledge_audit",
        "cross_cultural_analysis",
        "synthesis",
        "score_caveat",
        "next_step_beyond_goldberry",
    ]:
        if not isinstance(data.get(field), str) or not data[field].strip():
            errors.append(f"Field must be a non-empty string: {field}")

    whats_missing = data.get("whats_missing")
    if not isinstance(whats_missing, dict):
        errors.append("Field must be an object: whats_missing")
    else:
        for field in REQUIRED_WHATS_MISSING_FIELDS:
            value = whats_missing.get(field)
            if not isinstance(value, str) or not value.strip():
                errors.append(f"whats_missing.{field} must be a non-empty string")

    solution_pathways = data.get("solution_pathways")
    if not isinstance(solution_pathways, list) or not solution_pathways:
        errors.append("solution_pathways must be a non-empty array")
    elif not all(isinstance(item, str) and item.strip() for item in solution_pathways):
        errors.append("solution_pathways must contain only non-empty strings")

    lens_limitations = data.get("lens_limitations")
    if not isinstance(lens_limitations, list) or not lens_limitations:
        errors.append("lens_limitations must be a non-empty array")
    elif not all(isinstance(item, str) and item.strip() for item in lens_limitations):
        errors.append("lens_limitations must contain only non-empty strings")

    cmr_score = data.get("cmr_score")
    if not isinstance(cmr_score, (int, str)):
        errors.append("cmr_score must be an integer or a string score band")
    elif isinstance(cmr_score, int) and not (1 <= cmr_score <= 10):
        errors.append("cmr_score integer must be between 1 and 10")
    elif isinstance(cmr_score, str) and not cmr_score.strip():
        errors.append("cmr_score string must be non-empty")

    return errors
