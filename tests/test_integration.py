from fastjsonschema import validate, JsonSchemaException, JsonSchemaDefinitionException
import pytest


@pytest.mark.parametrize(
    "instance, format_value",
    [
        ("2018-12-18", "date-time"),
        ("rubbish", "date-time"),
        ("2", "uri"),
        ("daa520", "color"),
    ],
)
def test_format(instance, format_value):
    with pytest.raises(JsonSchemaException) as excinfo:
        validate(instance, {"format": format_value})
    assert f"'{instance}' is not a '{format_value}'" in str(excinfo.value)
