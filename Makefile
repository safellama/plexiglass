ENVIRONMENT := development

OS := $(shell uname -s)

.PHONY: develop
develop: verify-dev-env clean-build
	python setup.py sdist
	python setup.py install
	pip install -e .

.PHONY: verify-dev-env
verify-dev-env: verify-python-version

.PHONY: verify-python-version
verify-python-version:
	@./verify-python-version.sh

.PHONY: clean-build
clean-build: 
	rm -rf ./build
	rm -rf ./dist
