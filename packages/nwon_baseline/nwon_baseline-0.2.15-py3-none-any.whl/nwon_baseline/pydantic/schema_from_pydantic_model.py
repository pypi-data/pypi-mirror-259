import json
from string import Template
from typing import Type

import jsonref
from pydantic import BaseModel


def schema_from_pydantic_model(model: Type[BaseModel]) -> dict:
    """
    Gets a schema from a pydantic in a way that drf_spectacular can process it properly
    """

    schema = model.model_json_schema()
    json_schema = json.dumps(schema)
    json_schema = Template(json_schema).substitute(
        {"defs": "definitions", "ref": "$ref"}
    )
    schema = jsonref.loads(json_schema, jsonschema=True)

    schema_as_dict = dict(schema)

    # Leads to an error upon schema generation as definitions key is unexpected under
    # schema in an OpenAPI schema
    if "definitions" in schema_as_dict:
        del schema_as_dict["definitions"]

    return schema_as_dict
