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

# Install

## Install as a binary file

```
make
make install
```

## Install with Git

Since there is no pip package yet, this seems to be a viable alternative.
This documentation assumes the Git repository is installed in the `~/github` folder
and the virtual env is located in `~/.virtualenvs/python3`

* Install the Git repo locally
```
cd github
git clone https://github.com/SamK/lcad.git
```

* Create a venv and install the dependencies
```
mkdir -p ~/.virtualenvs
python -m venv =~/.virtualenvs/lcad
. ~/.virtualenvs/lcad/bin/activate
pip install pyyaml pandas tabulate
```

* Create a function to put in your .bashrc or whatever file fits your environment:
```
function lcad(){
    local LCAD_DIR=~/github/lcad
    local VENV_DIR=~/.virtualenvs/lcad

    local LCAD_BIN=${LCAD_DIR}/bin/lcad_bin.py
    . $VENV_DIR/bin/activate
    PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=$LCAD_DIR python $LCAD_BIN $*
}
```

* Extra tip: add aliases
```
alias python2json="lcad --from python --to json"
alias python2yaml="lcad --from python --to yaml"
alias json2python="lcad --from json --to python"
alias json2yaml="lcad --from json --to yaml"
alias yaml2json="lcad --from yaml --to json"
alias yaml2python="lcad --from yaml --to python"
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

```
make clean tests
git tag ...
git push && git push --tags
make install
```
