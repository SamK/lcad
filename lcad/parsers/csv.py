"""
CSV parser

Example: --to csv --output-args "headers=True"
"""

import csv
import io

# from lcad.errors import DataInputError, DataOutputError


def load(text, extra_args=None):  # pylint: disable=missing-function-docstring
    if extra_args is None:
        extra_args = {}
    reader = csv.DictReader(text, **extra_args)
    data = []
    for row in reader:
        data.append(row)
    return data


def is_truthy(value):
    """
    Return the boolean equivalent of a truthy value

    Source: https://stackoverflow.com/a/19015368

    Params:
    truthy_value (str): the truthy value

    Returns (bool): the boolean equivalent
    """

    valid = {
        "true": True,
        "false": False,
        "t": True,
        "f": False,
        "y": True,
        "n": False,
        "yes": True,
        "no": False,
        "1": True,
        "0": False,
    }

    if isinstance(value, bool):
        return value

    if not isinstance(value, str):
        raise ValueError(
            f"invalid literal for boolean. {value} is not a string but {type(value)}."
        )

    lower_value = value.lower()
    if lower_value in valid:
        return valid[lower_value]

    raise ValueError(f'invalid literal for boolean: "{value}"')


def dump(data, _=None):
    """
    Convert Python data into a CSV format.

    Returns a CSV string.

    Params:
    data (list): the data
    """
    filename = io.StringIO()

    # determine if the data has headers
    fieldnames = None
    has_headers = False
    if isinstance(data[0], dict):
        fieldnames = data[0].keys()
        has_headers = True

    writer = csv.DictWriter(filename, fieldnames=fieldnames, dialect="unix")
    if has_headers:
        writer.writeheader()
    writer.writerows(data)

    return filename.getvalue()
