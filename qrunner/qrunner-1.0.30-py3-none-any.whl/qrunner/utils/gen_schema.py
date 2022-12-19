"""
genson:
https://github.com/wolverdude/GenSON
"""
from genson import SchemaBuilder
from qrunner.core.api.request import ResponseResult


def gen_schema(data: dict = None):
    """
    return schema data
    """
    if (data is None) and ResponseResult.response is not None:
        data = ResponseResult.response

    builder = SchemaBuilder()
    builder.add_object(data)
    to_schema = builder.to_schema()
    return to_schema

