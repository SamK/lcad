import lcad.parsers.fail
from lcad.errors import DataInputError, DataOutputError
from . import file_io
import pytest


def test_load():
    with pytest.raises(DataInputError):
        loaded = lcad.parsers.fail.load("test")


def test_dump():
    with pytest.raises(DataOutputError):
        loaded = lcad.parsers.fail.dump("test")
