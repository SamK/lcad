"""
Basic Python parser using "eval()" to load and "repr()" to dump.
See "pickle".
"""


def load(data):  # pylint: disable=missing-function-docstring
    return eval(data.read())


def dump(data, _=None):  # pylint: disable=missing-function-docstring
    return repr(data)
