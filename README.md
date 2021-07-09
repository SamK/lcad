# lcad: Load, convert and dump

Convert any data type to any data type.

Examples:

* Convert json to yaml:
```
lcad convert --from json --to yaml < file.json
```

* Display a yaml file as a table:
```
lcad convert --from yaml --to tabulate < file.json
```

Supported formats:
* json
* yaml
* pandas
* tabulate
* vertical
* raw python
* CSV

# Install

## Install as a binary file

```
make
make install
```

* Extra tip: add shell aliases
```
alias python2json="lcad --from python --to json"
alias python2yaml="lcad --from python --to yaml"
alias json2python="lcad --from json --to python"
alias json2yaml="lcad --from json --to yaml"
alias yaml2json="lcad --from yaml --to json"
alias yaml2python="lcad --from yaml --to python"
alias yaml2csv="lcad --from yaml --to csv"
alias csv2yaml="lcad --from csv --to yaml"
```

## Execute locally

```
PYTHONPATH=. python ./bin/lcad_bin.py
```

# Development

## Execute tests

```
make clean
make tests
```

* pytest tip: Add `--capture=no` to see `print()` statements

## Release

1. Create release branch
1. Update version in `lcad/__init__.py`
1. Pin versions in `requirements.txt`
1. Execute tests with `make clean tests`
1. Merge into master
1. tag with `git tag ...`
1. push the work with `git push && git push --tags`
1. Install locally with `make install`
