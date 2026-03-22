SHELL := /bin/bash
PIP ?= pip3
PYTHON ?= python3

clean:
	rm -rf ./venv/ .coverage coverage.xml pytest-coverage.txt pytest.xml htmlcov/

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
	source ./venv/bin/activate && pytest -v -s \
		--cov=sam_local_backend \
		--cov-branch \
		--cov-report=term-missing:skip-covered \
		--cov-report=xml:coverage.xml \
		--junitxml=pytest.xml \
		tests/unit/ | tee pytest-coverage.txt

coverage-html:
	source ./venv/bin/activate && pytest -v -s \
		--cov=sam_local_backend \
		--cov-branch \
		--cov-report=html:htmlcov \
		tests/unit/
	@echo "Report disponibile in htmlcov/index.html"
	@open htmlcov/index.html 2>/dev/null || xdg-open htmlcov/index.html 2>/dev/null || true

build:
	source ./venv/bin/activate && sam build

deploy:
	source ./venv/bin/activate &&  sam build
	source ./venv/bin/activate &&  sam deploy

#############
#  Helpers  #
#############

define HELP_MESSAGE

	Usage: make <command>

	Commands:

	build     		Build Lambda function and dependencies
	deploy    		Deploy subsequent changes
	
	install			Install application and dev dependencies defined in requirements.txt
	deps      		Install project dependencies locally
	coverage  		Run tests + genera coverage.xml e pytest.xml (usati dalla CI)
    coverage-html 	Apre il report HTML nel browser

	clean     		Cleans up local build artifacts and environment

endef