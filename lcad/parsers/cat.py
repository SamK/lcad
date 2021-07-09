"""
Parser that returns what has been given without modification
"""


def load(text):  # pylint: disable=missing-function-docstring
    return text.read()


def dump(text, _=None):  # pylint: disable=missing-function-docstring
    return text
