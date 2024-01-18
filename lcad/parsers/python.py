"""
Basic Python parser using "eval()" to load and "repr()" to dump.
See "pickle".
"""


def load(data):  # pylint: disable=missing-function-docstring
    return eval(data.read())  # pylint: disable=eval-used


def dump(data, _=None):  # pylint: disable=missing-function-docstring
    return repr(data)
