"""
Parser for the Tabulate library: https://pypi.org/project/tabulate/
Only supports dump.
"""
import tabulate
import lcad.errors


def dump(data, _):
    """
    Print the data as a nice table
    """
    # limit case where no data is provided
    if not data:
        raise lcad.errors.DataInputError("There is no input data")

    if not isinstance(data, list):
        raise lcad.errors.DataOutputError("The input is not a list")

    # tabulate
    return tabulate.tabulate(data, headers="keys")
