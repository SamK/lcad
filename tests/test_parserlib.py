import lcad.parserlib

def test_discover_parsers():
    """Ensure the parsers exist"""
    # discovers the parsers
    parsers = lcad.parserlib.discover_parsers()
    assert isinstance(parsers, dict)

    # make sure these parsers exist
    assert 'json' in parsers
    assert 'yaml' in parsers
    assert 'zero' in parsers
    assert 'lines' in parsers

    # make sure "load" and "dump" exist (or not) based on the documentation
    assert parsers['json']['dump'] is True
    assert parsers['json']['load'] is True
    assert parsers['zero']['dump'] is True
    assert parsers['zero']['load'] is True
    assert parsers['fail']['dump'] is True
    assert parsers['fail']['load'] is True
    assert parsers['vertical']['dump'] is True
    assert parsers['vertical']['load'] is False
    assert parsers['lines']['dump'] is True
    assert parsers['lines']['load'] is True
