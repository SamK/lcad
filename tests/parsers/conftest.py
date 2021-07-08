import pytest


@pytest.fixture
def basic_python_txt():
    with open('tests/parsers/files/basic.python','r') as f:
        data = f.read()
    return eval(data)


@pytest.fixture
def basic_json_txt():
    with open('tests/parsers/files/basic.json','r') as f:
        output = f.read()
    return output


@pytest.fixture
def basic_yaml_io():
    return open('tests/parsers/files/basic.yml','r')
    with open('tests/parsers/files/basic.yml','r') as f:
        output = f.read()
    return output

