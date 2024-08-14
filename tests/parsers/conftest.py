import pytest


@pytest.fixture
def dict_py_txt():
    with open('tests/fixtures/dict.py','r') as f:
        data = f.read()
    return eval(data)


@pytest.fixture
def dict_json_txt():
    with open('tests/fixtures/dict.json','r') as f:
        output = f.read()
    return output


@pytest.fixture
def dict_yaml_io():
    return open('tests/fixtures/dict.yml','r')
    with open('tests/fixtures/dict.yml','r') as f:
        output = f.read()
    return output

