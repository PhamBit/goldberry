from __future__ import annotations

from pathlib import Path

IDENTITY_FILES = [
    "SOUL.md",
    "LENSES.md",
    "SUFFIXSCAPE.md",
    "AGENTS.md",
]


def repo_root() -> Path:
    return Path(__file__).resolve().parents[2]


def identity_dir() -> Path:
    return repo_root() / "agent-identity"


def load_identity_bundle() -> dict[str, str]:
    base = identity_dir()
    bundle: dict[str, str] = {}
    for name in IDENTITY_FILES:
        path = base / name
        bundle[name] = path.read_text(encoding="utf-8")
    return bundle


def build_system_prompt() -> str:
    bundle = load_identity_bundle()
    parts = [
        "You are operating in GoldBerry reference mode.",
        "Load and follow the following identity materials in order.",
    ]
    for name in IDENTITY_FILES:
        parts.append(
            f"\n--- BEGIN {name} ---\n{bundle[name].strip()}\n--- END {name} ---"
        )
    parts.append(
        "\nAlways present GoldBerry outputs with explicit caveats. Do not pretend the framework is externally validated where it is not."
    )
    return "\n".join(parts)


def build_user_prompt(user_input: str) -> str:
    return (
        "Analyse the following input using the GoldBerry framework. "
        "If the input is thin, say what cannot be responsibly inferred.\n\n"
        f"INPUT:\n{user_input.strip()}"
    )
