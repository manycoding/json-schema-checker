from typing import Dict, Optional

from fastjsonschema import compile, JsonSchemaDefinitionException, JsonSchemaException

Schema = Dict[str, any]


def check(schema: Schema, extended_keywords: Optional[set] = None):
    if not schema:
        raise JsonSchemaDefinitionException("Schema is empty")

    if not extended_keywords:
        extended_keywords = set()
    invalid_keywords = get_invalid_keywords(schema, extended_keywords)
    if invalid_keywords:
        raise JsonSchemaDefinitionException(
            f"Schema contains invalid keywords:\n{invalid_keywords}"
        )

    invalid_formats = get_invalid_formats(schema)
    if invalid_formats:
        raise JsonSchemaDefinitionException(
            f"Schema contains invalid format values:\n{invalid_formats}"
        )

    compile(schema)


def get_invalid_keywords(schema: Schema, extended_keywords: Optional[set]) -> set:
    draft_keywords = set("valid_keywords_here")
    allowed_keywords = draft_keywords.union(extended_keywords)
    keys = get_filtered_keys(schema, set())
    return keys.difference(allowed_keywords)


def get_filtered_keys(schema: dict, saved_keys: set, parent_key: str = None) -> set:
    parent_keys_to_filter = {
        "properties",
        "patternProperties",
        "definitions",
        "dependencies",
    }
    if isinstance(schema, dict):
        saved_keys = saved_keys.union(
            key for key in schema.keys() if parent_key not in parent_keys_to_filter
        )
        for key, value in schema.items():
            saved_keys = get_filtered_keys(value, saved_keys, key)
    elif isinstance(schema, list):
        for value in schema:
            saved_keys = get_filtered_keys(value, saved_keys, parent_key)

    return saved_keys


def get_invalid_formats(schema):
    allowed_formats = {
        "date-time",
        "date",
        "email",
        "hostname",
        "idn-email",
        "ipv4",
        "ipv6",
        "iri-reference",
        "iri",
        "json-pointer",
        "relative-json-pointer",
        "time",
        "uri-reference",
        "uri-template",
        "uri",
    }

    actual_formats = get_formats(schema)
    return actual_formats.difference(allowed_formats)


def get_formats(schema: dict) -> set:
    formats = set()

    def fill_formats(schema: dict):
        if isinstance(schema, dict):
            for key, value in schema.items():
                if key == "format" and isinstance(value, str):
                    formats.add(value)
                else:
                    fill_formats(value)
        elif isinstance(schema, list):
            for value in schema:
                fill_formats(value)

    fill_formats(schema)
    return formats
