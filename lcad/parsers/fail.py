"""
This parser fails successfuly.
Used for test purposes.
"""

from lcad.errors import DataInputError, DataOutputError

HIDE = True
"""Hide this parser from "--help" """


def load(_) -> DataInputError:  # pylint: disable=missing-function-docstring
    raise DataInputError("This format does not support inputs.")


def dump(_, __=None) -> DataOutputError:  # pylint: disable=missing-function-docstring
    raise DataOutputError("This format does not support outputs.")
