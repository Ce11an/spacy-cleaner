
# Getting started

You can install spacy-cleaner with [`pip`][pip] or using [`poetry`][poetry].

  [pip]: #with-pip
  [poetry]: #with-poetry

## Installation

### with pip <small>recommended</small> { #with-pip data-toc-label="with pip" }

spacy-cleaner is published as a [Python package] and can be installed with
`pip`, ideally by using a [virtual environment]. If not, scroll down and expand
the help box. Install with:

=== "Latest"

    ``` sh
    pip install spacy-cleaner
    ```

=== "3.x"

    ``` sh
    pip install spacy-cleaner=="3.*" # (1)!
    ```

    1.  spacy-cleaner uses [semantic versioning], which is why it's a
        good idea to limit upgrades to the current major version.


This will automatically install compatible versions of all dependencies:
[spaCy], [spaCy Lookups], and [tqdm]. We always strive to support the latest versions, so there's no need to install those packages separately.

---

  [Python package]: https://pypi.org/project/spacy-cleaner/
  [virtual environment]: https://realpython.com/what-is-pip/#using-pip-in-a-python-virtual-environment
  [semantic versioning]: https://semver.org/
  [spaCy]: https://spacy.io/
  [spaCy Lookups]: https://github.com/explosion/spacy-lookups-data
  [tqdm]: https://tqdm.github.io/

You can install spacy-cleaner using [Poetry]:

```sh
poetry add spacy-cleaner
```

---

  [Poetry]: https://python-poetry.org/

