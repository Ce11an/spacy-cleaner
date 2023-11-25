.DEFAULT_GOAL := help

.PHONY: help
# See <https://gist.github.com/klmr/575726c7e05d8780505a> for explanation.
help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

.PHONY: fmt
fmt: ## Format code.
	poetry run ruff format .
	poetry run ruff check . --fix

.PHONY: build
build: ## Builds the source and wheel archives.
	poetry build

.PHONY: install
install: ## Install the Python dependencies, including those for development and testing.
	poetry install --no-root

.PHONY: type-check
type-check: ## Check for typing errors.
	poetry run mypy .

.PHONY: test
test: ## Test code
	poetry run pytest --cov-report term --cov-report xml:coverage.xml --cov-report=html tests --cov=spacy_cleaner

.PHONY: coverage-remove
coverage-remove:
	rm -rf .coverage
	rm -rf htmlcov/
	rm -rf coverage.xml
	rm -rf gitlab-report.xml

.PHONY: pycache-remove
pycache-remove:
	find . | grep -E "(__pycache__|\.pyc|\.pyo$$)" | xargs rm -rf

.PHONY: dsstore-remove
dsstore-remove:
	find . | grep -E ".DS_Store" | xargs rm -rf

.PHONY: mypycache-remove
mypycache-remove:
	find . | grep -E ".mypy_cache" | xargs rm -rf

.PHONY: pytestcache-remove
pytestcache-remove:
	find . | grep -E ".pytest_cache" | xargs rm -rf

.PHONY: ruff-remove
ruff-remove:
	find . | grep -E ".ruff_cache" | xargs rm -rf

.PHONY: dist-remove
dist-remove:
	rm -rf dist/

.PHONY: public-remove
public-remove:
	rm -rf public

.PHONY: cleanup
cleanup: coverage-remove pycache-remove dsstore-remove mypycache-remove pytestcache-remove dist-remove ruff-remove public-remove ## Cleanup residual files.
