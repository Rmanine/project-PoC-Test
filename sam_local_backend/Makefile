SHELL := /bin/bash  # <- aggiunge questa riga in cima
PIP ?= pip3
PYTHON ?= python3

clean:
	rm -rf ./venv/

checkOSDependencies:
	$(PYTHON) --version

install: checkOSDependencies
	$(PYTHON) -m venv venv
	source ./venv/bin/activate && $(PIP) install -r tests/requirements.txt

deps:
	source ./venv/bin/activate && $(PIP) install -r tests/requirements.txt

test:
	source ./venv/bin/activate && pytest -v -s tests/unit/

coverage:
	source ./venv/bin/activate &&  coverage run --branch -m pytest -v -s tests/unit/
	source ./venv/bin/activate &&  coverage report -m

build:
	source ./venv/bin/activate && sam build

#############
#  Helpers  #
#############

define HELP_MESSAGE

	Usage: make <command>

	Commands:

	build     Build Lambda function and dependencies
	install   Install application and dev dependencies defined in requirements.txt
	deps      Install project dependencies locally
	test      Run unit test locally using mocks
	coverage  Run unit test coverage reports

	clean     Cleans up local build artifacts and environment

endef