# spacy-cleaner

![spacy-cleaner](assets/images/spacemen.png)

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

## Key Features

**spacy-cleaner** utilises `spaCy` `Language` models to replace, remove, and 
  mutate `spaCy` tokens. Cleaning actions available are:

* Remove/replace stopwords.
* Remove/replace punctuation.
* Remove/replace numbers.
* Remove/replace emails.
* Remove/replace URLs.
* Perform lemmatisation.

## Example

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
