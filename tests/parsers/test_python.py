import io
import lcad.parsers.json
from . import file_io
import json


def test_load():
    reference = eval(file_io('dict.python').read())
    loaded = lcad.parsers.python.load(file_io('dict.python'))
    assert reference == loaded


def test_dump():
    vref = eval(file_io('dict.python').read()) # reference as python type
    reference = repr(vref) # reference as string type

    loaded = lcad.parsers.json.load(file_io('dict.json')) # data as python type
    dumped = lcad.parsers.python.dump(loaded) # data as string type

    assert reference == dumped
