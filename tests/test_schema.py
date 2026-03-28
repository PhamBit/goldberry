from goldberry.analyze import scaffold_output
from goldberry.schemas import validate_output


def test_scaffold_output_is_valid():
    data = scaffold_output("Test input")
    assert validate_output(data) == []


def test_missing_field_fails_validation():
    data = scaffold_output("Test input")
    data.pop("synthesis")
    errors = validate_output(data)
    assert any("Missing top-level field: synthesis" == error for error in errors)
