import pytest

tests_set =  [("3+5", 8), ("2+4", 6), ("6*9", 42)]
@pytest.mark.parametrize("test_input,expected", tests_set)
def test_eval(test_input, expected):
    assert eval(test_input) == expected



@pytest.mark.parametrize("test_input,expected", tests_set)
def test_load(format_name, format_params, input_filename, expected)

