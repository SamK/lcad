import lcad.parserlib

def test_discover_parsers():
    parsers = lcad.parserlib.discover_parsers()
    assert isinstance(parsers, dict)
    assert 'json' in parsers
    assert 'yaml' in parsers
    assert 'zero' in parsers
    assert parsers['json']['dump'] is True
    assert parsers['json']['load'] is True
    assert parsers['zero']['dump'] is True
    assert parsers['zero']['load'] is True
    assert parsers['fail']['dump'] is True
    assert parsers['fail']['load'] is True
    assert parsers['vertical']['dump'] is True
    assert parsers['vertical']['load'] is False
