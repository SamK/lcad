"""
This parser fails successfuly.
Used for test purposes.
"""

from lcad.errors import DataInputError, DataOutputError


def load(_):  # pylint: disable=missing-function-docstring
    raise DataInputError("This format does not support inputs.")


def dump(_, __):  # pylint: disable=missing-function-docstring
    """fails to dump"""
    raise DataOutputError("This format does not support outputs.")
