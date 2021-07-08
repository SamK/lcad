"""
YAML parser
"""
import yaml


def load(text):  # pylint: disable=missing-function-docstring
    return yaml.load(text, Loader=yaml.SafeLoader)


def dump(data, extra_args=None):  # pylint: disable=missing-function-docstring
    if extra_args is None:
        extra_args = {}
    return yaml.dump(data, **extra_args)
