from goldberry.prompts import build_system_prompt, build_user_prompt


def test_system_prompt_contains_all_identity_files():
    prompt = build_system_prompt()
    assert "BEGIN SOUL.md" in prompt
    assert "BEGIN LENSES.md" in prompt
    assert "BEGIN SUFFIXSCAPE.md" in prompt
    assert "BEGIN AGENTS.md" in prompt


def test_user_prompt_includes_input():
    prompt = build_user_prompt("Test input")
    assert "Test input" in prompt
    assert "GoldBerry framework" in prompt
