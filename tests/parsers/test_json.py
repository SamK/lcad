import io
import json
import lcad.parsers.json
from . import file_io


def test_load_dict():
    reference = eval(file_io('dict.py').read())
    loaded = lcad.parsers.json.load(file_io('dict.json'))
    assert reference == loaded


def test_dump_dict():
    reference = json.dumps(json.load(file_io('dict.json')))
    loaded = eval(file_io('dict.py').read())
    dumped = lcad.parsers.json.dump(loaded)
    assert reference == dumped


def test_dump_sort_keys():
    extra_args = {'sort_keys': True}
    reference = json.dumps(json.load(file_io('dict.json')))
    loaded = lcad.parsers.json.load(file_io('dict-unsorted.json'))
    sorted = lcad.parsers.json.dump(loaded, extra_args)
    assert reference == sorted
