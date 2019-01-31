# perfect-jsonschema
[![Build Status](https://travis-ci.org/manycoding/perfect-jsonschema.svg?branch=master)](https://travis-ci.org/manycoding/perfect-jsonschema)
[![codecov](https://codecov.io/gh/manycoding/perfect-jsonschema/branch/master/graph/badge.svg)](https://codecov.io/gh/manycoding/perfect-jsonschema)

Strictly checks that a json schema is valid

It does rely on [jsonschema](https://github.com/Julian/jsonschema) package and supports additional keywords to ignore.

# Features

Derives the draft from the schema and yields a `jsonschema.SchemaError` if:
* A schema is empty
* A schema contains a keyword which is not a part of a jsonschema implementation or `extended_keywords` set
* A schema contains an invalid format value
* A schema fails with `jsonschema.check_schema()`

# Usage

    from perfect-jsonschema import check

    try:
        check(schema, extended_keywords={"tag"})
    except Exception as e:
        do_something()

# Local development

    pipenv install --dev
    pipenv shell
    tox

# Contribution
  
  Any contribution is welcome
  
