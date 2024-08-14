"""
Import module for
[Pickle](https://docs.python.org/3/library/pickle.html),
the serialization module of Python.
"""
import ast
import pickle


def load(data) -> object:
    """
    Loads a serialized value given in argument.

    Returns the unserialzed value.
    """
    bdata = ast.literal_eval(data.read())
    return pickle.loads(bdata)


def dump(data, _=None) -> object:
    """Returns the serialized value given in argument"""
    return pickle.dumps(data)
