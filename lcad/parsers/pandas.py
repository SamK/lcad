"""
Parser for the Pandas library: https://pandas.pydata.org/
Only supports dump
"""
import pandas


def dump(data, _):  # pylint: disable=missing-function-docstring
    return pandas.DataFrame(data)
