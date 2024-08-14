"""
Json parser


output args can be specified and are given to
`json.dumps()`.

See: https://docs.python.org/3/library/json.html#json.dumps

Example:

    --to json --output-args "indent=5 sort_keys=True"
"""
import json


def load(text):  # pylint: disable=missing-function-docstring
    return json.load(text)


def dump(data, extra_args=None):  # pylint: disable=missing-function-docstring
    if extra_args is None:
        extra_args = {}
    return json.dumps(data, **extra_args)
