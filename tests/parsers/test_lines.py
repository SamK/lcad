import yaml
import lcad.parsers.lines
from . import file_io


def test_load_list():
    reference = yaml.load(file_io('list.yaml'), Loader=yaml.SafeLoader)
    loaded = lcad.parsers.lines.load(file_io('list.lines'))
    assert reference == loaded


def test_dump_list():
    reference = file_io('list.lines').read()
    loaded = yaml.load(file_io('list.yaml'), Loader=yaml.SafeLoader)
    dumped = lcad.parsers.lines.dump(loaded)
    assert reference == dumped
