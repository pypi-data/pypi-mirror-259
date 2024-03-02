SERVICE_NAME = tms

clean: clean-build clean-pyc clean-test ## remove all build, test, coverage and Python artifacts

clean-build: ## remove build artifacts
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -f {} +

clean-pyc: ## remove Python file artifacts
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-test: ## remove test and coverage artifacts
	rm -fr .tox/
	rm -f .coverage
	rm -fr htmlcov/
	rm -fr .pytest_cache

install: clean ## install the package to the active Python's site-packages
	pip install .

install-dev:
	export SETUPTOOLS_SCM_PRETEND_VERSION=1.0.0 && pip install -e .[dev]

build:
	docker build -t SERVICE_NAME -f Dockerfile --platform linux/amd64 .

run-dev: build
	docker compose \
	-f docker-compose/docker-compose.yml \
	--env-file .dev.env up
