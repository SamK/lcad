import lcad.parsers.py
from . import file_io
import json


def test_load():
    reference = eval(file_io('dict.py').read())
    loaded = lcad.parsers.py.load(file_io('dict.py'))
    assert reference == loaded


def test_dump():
    vref = eval(file_io('dict.py').read()) # reference as python type
    reference = repr(vref) # reference as string type

    loaded = json.load(file_io('dict.json')) # data as python type
    dumped = lcad.parsers.py.dump(loaded) # data as string type

    assert reference == dumped
