"""
YAML parser using PyYAML

The extra args are given to yaml.dump():
https://pyyaml.org/wiki/PyYAMLDocumentation#reference

Example: --to yaml --output-args "explicit_start=True indent=4"
"""
import yaml


def load(text):  # pylint: disable=missing-function-docstring
    return yaml.load(text, Loader=yaml.SafeLoader)


def dump(data, extra_args=None):  # pylint: disable=missing-function-docstring
    if extra_args is None:
        extra_args = {}
    return yaml.dump(data, **extra_args)
