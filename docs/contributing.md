## Contributing code

Check the [Makefile](https://github.com/Ce11an/spacy-cleaner/blob/main/Makefile) for useful commands to help you get started. Run
`make help` to see a list of all available commands.

### Dependencies
We use [Poetry](https://python-poetry.org/) to manage dependencies. Please 
install Poetry before contributing code. We also utilise 
[pre-commit](https://pre-commit.com/) to manage pre-commit hooks. Please install
pre-commit before contributing code.

You can install all dependencies by running `make install` in the root directory 
of this project.

### Code style
We use [ruff](https://beta.ruff.rs/docs/) to format and lint our code. Please 
run `pre-commit run --all-files` or `make fmt` before submitting a pull 
request to ensure your code is formatted correctly and passes all linting 
checks.

### Testing
We use [pytest](https://docs.pytest.org/en/stable/) to test our code. Please 
write tests for all new code you write. You can run all tests by running 
`make test` in the root directory of this project.

### Type checking
We use [mypy](https://mypy.readthedocs.io/en/stable/) to type check our code. Please run `make type-check` before 
submitting a pull request to ensure your code is type checked correctly.

## Before submitting a pull request
Before submitting a pull request, please ensure that you have run 
`pre-commit run --all-files`, `make test`, and `make type-check` to ensure your 
code is formatted correctly, passes all linting checks, and passes all tests.

Please ensure you follow these steps:

1. Fork the repository and create your branch from `main`.
2. If you've added code that should be tested, add tests.
3. Ensure the test suite passes.
4. Make sure your code lints.
5. Issue that pull request!
