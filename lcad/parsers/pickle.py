"""
"""
import ast
import pickle


def load(data):  # pylint: disable=missing-function-docstring
    bdata = ast.literal_eval(data.read())
    return pickle.loads(bdata)


def dump(data, _=None):  # pylint: disable=missing-function-docstring
    return pickle.dumps(data)
