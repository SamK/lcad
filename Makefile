SOURCEDIR = lcad bin
requirements := venv/.requirements.txt
test_requirements := venv/.test_requirements.txt
SOURCEFILES := $(shell find $(SOURCEDIR) -name '*.py')
ACTIVATE = . ./venv/bin/activate

# default target
# alias
build: dist/lcad

doc: doc/index.html

venv:
	python3 -m venv venv

doc/index.html: $(SOURCEFILES)
	$(ACTIVATE) && \
	pip install --require-virtualenv pdoc && \
	pdoc lcad -o doc

dist/lcad: venv $(SOURCEFILES) $(requirements)
	$(ACTIVATE) && \
	PYTHONPATH=. pyinstaller \
		--onefile \
		--name=lcad \
		--collect-submodules lcad \
		bin/lcad_bin.py

# alias
.PHONY: requirements
requirements: $(requirements)

$(requirements): requirements.txt venv
	$(ACTIVATE) && \
	pip install -r requirements.txt && \
	touch $(requirements)

# alias
.PHONY: test_requirements
test_requirements: $(test_requirements)

$(test_requirements): test_requirements.txt $(requirements)
	$(ACTIVATE) && \
	pip install -r test_requirements.txt && \
	touch $(test_requirements)

install:
	install ./dist/lcad ~/.local/bin

tests: test-black test-lint test-build test-unit

test-black: test_requirements
	$(ACTIVATE) && \
	black --check --diff $(SOURCEDIR) # tests

test-lint: test_requirements
	$(ACTIVATE) && \
	PYTHONPATH=. pylint $(SOURCEDIR) --max-line-length=120 --max-attributes=99 --fail-under=9.95 && \
	PYTHONPATH=. pylint tests --disable=C,R,unspecified-encoding,eval-used --ignore=tests/fixtures

test-build: build
	./dist/lcad --version
	./dist/lcad --help
	./dist/lcad formats
	./dist/lcad convert --from json --to py -i tests/fixtures/dict.json
	./dist/lcad convert --from json --to yaml -i tests/fixtures/dict.json
	./dist/lcad convert --from csv --to yaml -i tests/fixtures/list_of_dict.csv
	./dist/lcad convert --from csv --to vertical -i tests/fixtures/list_of_dict.csv
	./dist/lcad convert --from yaml --to csv -i tests/fixtures/list_of_dict.yaml

test-unit: test_requirements
	$(ACTIVATE) && \
	PYTHONDONTWRITEBYTECODE=1 coverage run -m pytest -v && \
	coverage report

test-coverage: test_requirements
	$(ACTIVATE) && \
	coverage report

clean-build:
	/bin/rm -rf ./build ./dist
	/bin/rm -f ./lcad.spec

clean-venv:
	/bin/rm -rf ./venv

clean-doc:
	/bin/rm -rf ./doc

clean: clean-build clean-venv clean-doc
