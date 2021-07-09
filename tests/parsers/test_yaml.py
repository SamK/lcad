import io
import yaml
import lcad.parsers.yaml
from . import file_io


def test_load_dict():
    reference = eval(file_io('dict.python').read())
    loaded = lcad.parsers.yaml.load(file_io('dict.yaml'))
    assert reference == loaded


def test_dump_dict():
    reference = yaml.dump(yaml.load(file_io('dict.yaml'), Loader=yaml.SafeLoader))
    loaded = eval(file_io('dict.python').read())
    dumped = lcad.parsers.yaml.dump(loaded)
    assert reference == dumped


def test_load_list_of_dict():
    reference = eval(file_io('list_of_dict.python').read())
    loaded = lcad.parsers.yaml.load(file_io('list_of_dict.yaml'))
    assert reference == loaded


def test_dump_list_of_dict():
    reference = yaml.dump(yaml.load(file_io('list_of_dict.yaml'), Loader=yaml.SafeLoader))
    loaded = eval(file_io('list_of_dict.python').read())
    dumped = lcad.parsers.yaml.dump(loaded)
    assert reference == dumped
