import io
import json
import lcad.parsers.json
from . import file_io


def test_load():
    reference = json.load(file_io('basic.json'))
    loaded = lcad.parsers.json.load(file_io('basic.json'))
    assert reference == loaded


def test_dump():
    reference = json.dumps(json.load(file_io('basic.json')))
    loaded = lcad.parsers.json.load(file_io('basic.json'))
    dumped = lcad.parsers.json.dump(loaded)
    assert reference == dumped


def test_dump_sort_keys():
    extra_args = {'sort_keys': True}
    reference = json.dumps(json.load(file_io('basic.json')))
    loaded = lcad.parsers.json.load(file_io('basic-unsorted.json'))
    sorted = lcad.parsers.json.dump(loaded, extra_args)
    assert reference == sorted
