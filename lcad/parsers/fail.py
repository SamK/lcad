"""
This parser fails successfuly.
Used for test purposes.
"""

from lcad.errors import DataInputError, DataOutputError

HIDE = True


def load(_):  # pylint: disable=missing-function-docstring
    raise DataInputError("This format does not support inputs.")


def dump(_, __=None):  # pylint: disable=missing-function-docstring
    raise DataOutputError("This format does not support outputs.")
