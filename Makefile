SOURCEDIR = lcad bin
requirements := venv/.requirements.txt
test_requirements := venv/.test_requirements.txt
SOURCEFILES := $(shell find $(SOURCEDIR) -name '*.py')
ACTIVATE = . ./venv/bin/activate

# default target
# alias
build: dist/lcad

venv:
	python3 -m venv venv

dist/lcad: venv $(SOURCEFILES) $(requirements)
	$(ACTIVATE) && \
	PYTHONPATH=. pyinstaller \
		--onefile \
		--name=lcad \
		--hidden-import argparse \
		--hidden-import lcad \
		bin/lcad_bin.py \

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
	PYTHONPATH=. pylint $(SOURCEDIR) --max-line-length=120 --max-attributes=99 --fail-under=9.95

test-build: test_requirements build
	./dist/lcad --version
	./dist/lcad --help

test-unit: test_requirements
	$(ACTIVATE) && \
	PYTHONDONTWRITEBYTECODE=1 coverage run -m pytest -v && \
	coverage report

test-coverage: test_requirements
	$(ACTIVATE) && \
	coverage report

clean-build:
	/bin/rm -rf ./build ./dist

clean-venv:
	/bin/rm -rf ./venv

clean: clean-build clean-venv
