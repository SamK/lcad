import lcad.parsers.fail
from lcad.errors import DataInputError, DataOutputError
import pytest


def test_load():
    with pytest.raises(DataInputError):
        lcad.parsers.fail.load("test")


def test_dump():
    with pytest.raises(DataOutputError):
        lcad.parsers.fail.dump("test")
