"""
Lines parser

the `lines` format is a list of elements, one by line.
"""


def load(text: str) -> list:
    """Reads the text and return a list, one element by line"""
    ret = text.read().splitlines()
    return ret


def dump(data: list, _=None) -> str:
    """Reads the data and returns a text, one element by line"""
    # existe-t-il un moyen plus propre?
    return "\n".join(data) + "\n"
