import pytest


@pytest.fixture
def dict_python_txt():
    with open('tests/parsers/files/dict.python','r') as f:
        data = f.read()
    return eval(data)


@pytest.fixture
def dict_json_txt():
    with open('tests/parsers/files/dict.json','r') as f:
        output = f.read()
    return output


@pytest.fixture
def dict_yaml_io():
    return open('tests/parsers/files/dict.yml','r')
    with open('tests/parsers/files/dict.yml','r') as f:
        output = f.read()
    return output

