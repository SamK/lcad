"""
This module does not actually anything, it reads and write without looking at the content.
"""


def load(text):
    """Returns the `data` given in argument"""
    return text.read()


def dump(text, _=None):
    """Returns the `data` given in argument"""
    return text
