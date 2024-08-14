# lcad: Load, convert and dump

Convert any data type to any data type.

Examples:

* Convert json to yaml:
```
lcad convert --from json --to yaml --input-file file.json
```

* Display a yaml file as a table:
```
lcad convert --from yaml --to tabulate --input-file file.json
```

Supported formats:

This table shows what format lcad can read (input) and write (output).

| format | input | output | notes |
|--------|-------|--------|-------|
| `json` | :white_check_mark: | :white_check_mark: | |
| `yaml` | :white_check_mark: | :white_check_mark: | |
| `csv`  | :white_check_mark: | :white_check_mark: | |
| `pandas` | :x: | :white_check_mark: | https://pandas.pydata.org/ |
| `tabulate` | :x: | :white_check_mark: | https://pypi.org/project/tabulate/ |
| `vertical` | :x: | :white_check_mark: | a kind of vertical formatting |
| `python` | :white_check_mark: | :white_check_mark: | raw Python |
| `pickle` | :white_check_mark: | :white_check_mark: | serialized Python |
| `lines` | :white_check_mark: | :white_check_mark: | a list, one element per line |

# Install

## Install as a binary file

```
make
make install
```

* Extra tip: add shell aliases
```
alias python2json="lcad convert --from python --to json"
alias python2yaml="lcad convert --from python --to yaml"
alias json2python="lcad convert --from json --to python"
alias json2yaml="lcad convert --from json --to yaml"
alias yaml2json="lcad convert --from yaml --to json"
alias yaml2python="lcad convert --from yaml --to python"
alias yaml2csv="lcad convert --from yaml --to csv"
alias csv2yaml="lcad convert --from csv --to yaml"
alias yaml2lines="lcad convert --from yaml --to lines"
alias lines2yaml="lcad convert --from lines --to yaml"
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

## Build the doc

```
make doc
```
The generated doc is available at `doc/index.html`.

## Release

1. Create release branch
1. Update version in `lcad/__init__.py`
1. Pin versions in `requirements.txt`
1. Execute tests with `make clean tests`
1. Merge into master
1. tag with `git tag ...`
1. push the work with `git push && git push --tags`
1. Install locally with `make install`
1. Update version in `lcad/__init__.py` to `master`
