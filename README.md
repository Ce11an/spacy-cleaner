# spacy-cleaner

<div align="center">

![spacy-cleaner](https://raw.githubusercontent.com/Ce11an/spacy-cleaner/main/docs/assets/images/spacemen.png)

[![Built with spaCy](https://img.shields.io/badge/built%20with-spaCy-09a3d5.svg)](https://spacy.io)
[![Build status](https://github.com/Ce11an/spacy-cleaner/workflows/build/badge.svg?branch=main&event=push)](https://github.com/Ce11an/spacy-cleaner/actions?query=workflow%3Abuild)
[![Python Version](https://img.shields.io/pypi/pyversions/spacy-cleaner.svg)](https://pypi.org/project/spacy-cleaner/)
[![Dependencies Status](https://img.shields.io/badge/dependencies-up%20to%20date-brightgreen.svg)](https://github.com/Ce11an/spacy-cleaner/pulls?utf8=%E2%9C%93&q=is%3Apr%20author%3Aapp%2Fdependabot)

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/Ce11an/spacy-cleaner/blob/main/.pre-commit-config.yaml)
[![Semantic Versions](https://img.shields.io/badge/%20%20%F0%9F%93%A6%F0%9F%9A%80-semantic--versions-e10079.svg)](https://github.com/Ce11an/spacy-cleaner/releases)
[![License](https://img.shields.io/github/license/Ce11an/spacy-cleaner)](https://github.com/Ce11an/spacy-cleaner/blob/main/LICENSE)
[![codecov](https://codecov.io/gh/Ce11an/spacy-cleaner/branch/main/graph/badge.svg?token=H28KHYYFHX)](https://codecov.io/gh/Ce11an/spacy-cleaner)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=Ce11an_spacy-cleaner&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=Ce11an_spacy-cleaner)
Easily clean text with spaCy!

</div>

## Key Features

**spacy-cleaner** utilises `spaCy` `Language` models to replace, remove, and 
  mutate `spaCy` tokens. Cleaning actions available are:

* Remove/replace stopwords.
* Remove/replace punctuation.
* Remove/replace numbers.
* Remove/replace emails.
* Remove/replace URLs.
* Perform lemmatisation.

See our [docs](https://ce11an.github.io/spacy-cleaner/) for more information.

## Installation

```bash
pip install -U spacy-cleaner
```

or install with `Poetry`

```bash
poetry add spacy-cleaner
```

## 📖 Example

**spacy-cleaner** can clean text written in any language `spaCy` has a model 
  for:
```python
import spacy
import spacy_cleaner
from spacy_cleaner.processing import removers, replacers, mutators

model = spacy.load("en_core_web_sm")
```

Class `Pipeline` allows for configurable cleaning of text using `spaCy`. The 
  `Pipeline` is initialised with a model and functions that transform `spaCy` 
  tokens:

```python
pipeline = spacy_cleaner.Pipeline(
    model,
    removers.remove_stopword_token,
    replacers.replace_punctuation_token,
    mutators.mutate_lemma_token,
)
```

Next the `pipeline` can be called with the method `clean` to clean a list of 
  texts:
```python
texts = ["Hello, my name is Cellan! I love to swim!"]

pipeline.clean(texts)
```

<details markdown="1">
<summary>About the method <code>clean</code>...</summary>

The method `clean` is a wrapper around the `spaCy` `Language` class method 
  `pipe`. Check the docs for more information:

https://spacy.io/api/language#pipe

</details>

Giving the output:
```python
['hello _IS_PUNCT_ Cellan _IS_PUNCT_ love swim _IS_PUNCT_']
```

### Makefile usage

[`Makefile`](https://github.com/Ce11an/spacy-cleaner/blob/main/Makefile) contains a lot of functions for faster development.

<details>
<summary>1. Download and remove Poetry</summary>
<p>

To download and install Poetry run:

```bash
make poetry-download
```

To uninstall

```bash
make poetry-remove
```

</p>
</details>

<details>
<summary>2. Install all dependencies and pre-commit hooks</summary>
<p>

Install requirements:

```bash
make install
```

Pre-commit hooks can be installed after `git init` via

```bash
make pre-commit-install
```

</p>
</details>

<details>
<summary>3. Codestyle</summary>
<p>

Automatic formatting uses `pyupgrade`, `isort` and `black`.

```bash
make codestyle

# or use synonym
make formatting
```

Codestyle checks only, without rewriting files:

```bash
make check-codestyle
```

> Note: `check-codestyle` uses `isort`, `black` and `darglint` library

Update all dev libraries to the latest version using one command

```bash
make update-dev-deps
```

</details>

<details>
<summary>4. Type checks</summary>
<p>

Run `mypy` static type checker

```bash
make mypy
```

</p>
</details>

<details>
<summary>5. Tests with coverage badges</summary>
<p>

Run `pytest`

```bash
make test
```

</p>
</details>

<details>
<summary>6. All linters</summary>
<p>

Of course there is a command to ~~rule~~ run all linters in one:

```bash
make lint
```

the same as:

```bash
make test && make check-codestyle && make mypy
```

</p>
</details>

<details>
<summary>7. Cleanup</summary>
<p>
Delete pycache files

```bash
make pycache-remove
```

Remove package build

```bash
make build-remove
```

Delete .DS_STORE files

```bash
make dsstore-remove
```

Remove .mypy_cache

```bash
make mypycache-remove
```

Or to remove all above run:

```bash
make cleanup
```

</p>
</details>

## 📈 Releases

You can see the list of available releases on the [GitHub Releases](https://github.com/Ce11an/spacy-cleaner/releases) page.

We follow [Semantic Versions](https://semver.org/) specification.

We use [`Release Drafter`](https://github.com/marketplace/actions/release-drafter). As pull requests are merged, a draft release is kept up-to-date listing the changes, ready to publish when you’re ready. With the categories option, you can categorize pull requests in release notes using labels.

### List of labels and corresponding titles

|               **Label**               |  **Title in Releases**  |
|:-------------------------------------:|:-----------------------:|
|       `enhancement`, `feature`        |       🚀 Features       |
| `bug`, `refactoring`, `bugfix`, `fix` | 🔧 Fixes & Refactoring  |
|       `build`, `ci`, `testing`        | 📦 Build System & CI/CD |
|              `breaking`               |   💥 Breaking Changes   |
|            `documentation`            |    📝 Documentation     |
|            `dependencies`             | ⬆️ Dependencies updates |

You can update it in [`release-drafter.yml`](https://github.com/Ce11an/spacy-cleaner/blob/main/.github/release-drafter.yml).

GitHub creates the `bug`, `enhancement`, and `documentation` labels for you. Dependabot creates the `dependencies` label. Create the remaining labels on the Issues tab of your GitHub repository, when you need them.

## 🛡 License

[![License](https://img.shields.io/github/license/Ce11an/spacy-cleaner)](https://github.com/Ce11an/spacy-cleaner/blob/main/LICENSE)

This project is licensed under the terms of the `MIT` license. See [LICENSE](https://github.com/Ce11an/spacy-cleaner/blob/main/LICENSE) for more details.

## 📃 Citation

```bibtex
@misc{spacy-cleaner,
  author = {spacy-cleaner},
  title = {Easily clean text with spaCy!},
  year = {2022},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/Ce11an/spacy-cleaner}}
}
```

## 🚀 Credits

This project was generated with [`python-package-template`](https://github.com/TezRomacH/python-package-template)

This project was built using [IntelliJ IDEA](https://www.jetbrains.com/community/opensource/?utm_campaign=opensource&utm_content=approved&utm_medium=email&utm_source=newsletter&utm_term=jblogo#support) 

![JetBrains Black Box Logo logo](https://resources.jetbrains.com/storage/products/company/brand/logos/jb_square.svg)
