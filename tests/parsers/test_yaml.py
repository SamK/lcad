import io
import yaml
import lcad.parsers.yaml
from . import file_io


def test_load():
    reference = yaml.load(file_io('basic.yaml'), Loader=yaml.SafeLoader)
    loaded = lcad.parsers.yaml.load(file_io('basic.yaml'))
    assert reference == loaded


def test_dump():
    reference = yaml.dump(yaml.load(file_io('basic.yaml'), Loader=yaml.SafeLoader))
    loaded = lcad.parsers.yaml.load(file_io('basic.yaml'))
    dumped = lcad.parsers.yaml.dump(loaded)
    assert reference == dumped
