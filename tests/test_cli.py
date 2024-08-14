import pytest
import lcad.cli
import json

def test_cli_help(capsys):
    """
    Make sure the usage help is displayed when no argument is passed
    """
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        lcad.cli.parse_arguments(['--help'])
    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code == 0
    captured = capsys.readouterr()
    assert captured.err == ""
    assert captured.out.startswith("usage:")

def test_cli_simple_test(capsys):
    """
    Execute a simple execution
    """
    iargs = '-vv convert --input-file tests/fixtures/dict.yaml --from yaml --to json'.split()
    lcad.cli.main(iargs)
    captured = capsys.readouterr()
    # validate
    json.loads(captured.out)

def test_cli_no_rogue_print(capsys):
    iargs = '-vv convert --input-file tests/fixtures/dict.yaml --from yaml --to zero'.split()
    lcad.cli.main(iargs)
    captured = capsys.readouterr()
    assert captured.out.strip() == ""


def test_exit_noarg():
    with pytest.raises(SystemExit) as pytest_wrapped_e:
        lcad.cli.main()
        lcad.cli.parse_arguments()
    assert pytest_wrapped_e.type == SystemExit
    assert pytest_wrapped_e.value.code == 2
