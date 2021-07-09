import io
import lcad.parsers.cat
from . import file_io


def test_load():
    reference = file_io('dict.python').read()
    loaded = lcad.parsers.cat.load(file_io('dict.python'))
    assert reference == loaded


def test_dump():
    reference = file_io('dict.json').read()
    dumped = lcad.parsers.cat.dump(reference)
    assert reference == dumped
