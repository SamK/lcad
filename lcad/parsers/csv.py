"""
CSV parser
"""
import csv


def load(text, extra_args=None):  # pylint: disable=missing-function-docstring
    if extra_args is None:
        extra_args = {}
    reader = csv.DictReader(text, **extra_args)
    data = []
    for row in reader:
        data.append(row)
    return data
    return ""


def dump(_, __=None):  # pylint: disable=missing-function-docstring
    raise DataOutputError("This format does not support outputs.")
    # return csv.DictWriter(data, **extra_args)
