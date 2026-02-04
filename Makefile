# Environment configuration (development or production)
ENVIRONMENT ?= development

OS := $(shell uname -s)

# Development targets
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

# Production targets
.PHONY: prod
prod: ENVIRONMENT=production
prod: verify-python-version clean-build
	PYPI_RELEASE=1 python setup.py sdist bdist_wheel

.PHONY: publish
publish: prod
	python -m twine upload dist/*

.PHONY: publish-test
publish-test: prod
	python -m twine upload --repository testpypi dist/*

# Testing targets
.PHONY: test
test:
	python -m pytest tests/ -v

.PHONY: lint
lint:
	python -m flake8 plexiglass/ --max-line-length=120

# Environment info
.PHONY: info
info:
	@echo "Environment: $(ENVIRONMENT)"
	@echo "OS: $(OS)"
	@echo "Python: $$(python --version)"
