"""
Json parser

Example: --to json --output-args "indent=5 sort_keys=True"
"""
import json


def load(text):  # pylint: disable=missing-function-docstring
    return json.load(text)


def dump(data, extra_args=None):  # pylint: disable=missing-function-docstring
    if extra_args is None:
        extra_args = {}
    return json.dumps(data, **extra_args)
