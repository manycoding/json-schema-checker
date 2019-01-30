# json_schema_checker
[![Build Status](https://travis-ci.org/manycoding/json-schema-checker.svg?branch=master)](https://travis-ci.org/manycoding/json-schema-checker)
[![codecov](https://codecov.io/gh/manycoding/json-schema-checker/branch/master/graph/badge.svg)](https://codecov.io/gh/manycoding/json-schema-checker)

Strictly checks that a json schema is valid

It does rely on [jsonschema](https://github.com/Julian/jsonschema) package and supports additional keywords to ignore.

# Features

Derives the draft from the schema and yields a `jsonschema.SchemaError` if:
* A schema is empty
* A schema contains a keyword which is not a part of a jsonschema implementation or `extended_keywords` set
* A schema contains an invalid format value
* A schema fails with `jsonschema.check_schema()`

# Usage

    from json_schema_checker import check_schema

    try:
        check_schema(schema, extended_keywords={"tag"})
    except Exception as e:
        do_something()

# Local development

    pipenv install --dev
    pipenv shell
    tox

# Contribution
  
  Any contribution is welcome
  
