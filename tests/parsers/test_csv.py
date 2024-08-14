import io
import csv
import lcad.parsers.csv
from . import file_io
import io


def test_load_list_of_dict():
    reference = eval(file_io('list_of_dict.py').read())
    loaded = lcad.parsers.csv.load(file_io('list_of_dict.csv'))
    assert reference == loaded


def test_dump_list_of_dict():
    reference = file_io("list_of_dict.csv").read()

    data = eval(file_io('list_of_dict.py').read())
    dumped = lcad.parsers.csv.dump(data)

    assert reference == dumped
