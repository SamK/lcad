import io
import lcad.parsers.json
from . import file_io
import json
import pickle


def test_load():
    reference = eval(file_io('dict.python').read())
    loaded = lcad.parsers.pickle.load(file_io('dict.pickle'))
    assert reference == loaded


def test_dump():
    vref = eval(file_io('dict.python').read()) # reference as python format
    reference = pickle.dumps(vref) # reference as pickle format

    loaded = lcad.parsers.json.load(file_io('dict.json')) # data as python type
    dumped = lcad.parsers.pickle.dump(loaded) # data as string type

    assert reference == dumped
