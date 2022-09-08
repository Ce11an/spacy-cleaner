# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys

sys.path.insert(0, os.path.abspath("../.."))

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "spacy-cleaner"
copyright = "2022, spacy-cleaner"
author = "Cellan Hall"

version = "latest"
release = "latest"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.napoleon",  # Interpret Google and NumPy docstrings
    "sphinx.ext.autodoc",  # Auto-document from docstrings
    "sphinx.ext.intersphinx",  # Activate links to documentation when referencing external libraries/objects
    "sphinx.ext.todo",
    "sphinx.ext.viewcode",  # Adds button next to object definition to view source code
    "sphinx.ext.autosectionlabel",  # Automatic section labels in reST files (i.e., READMEs) for cross-referencing
    "sphinx.ext.githubpages",  # Automatically create .nojekyll file for deployment on GitHub Pages
    "sphinx_rtd_dark_mode",  # Dark mode toggle
    "sphinx_github_changelog",  # Automatic changelog
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

language = "en"

pygments_style = "colorful"  # 'colorful' best for dark text on light background, 'material' for reverse

default_role = "code"  # Tells Sphinx what to default to when interpreting text enclosed in just backticks, i.e., `...`

add_module_names = False  # Don't render full module paths

source_suffix = {
    ".rst": "restructuredtext",
    ".txt": "restructuredtext",
    ".md": "markdown",
}

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]

# -- Options for intersphinx extension ---------------------------------------
# https://www.sphinx-doc.org/en/master/usage/extensions/intersphinx.html#configuration

intersphinx_mapping = {
    "spacy": ("https://spacy.io/", None),
    "tqdm": ("https://tqdm.github.io/", None),
    "spacy-lookups-data": ("https://github.com/explosion/spacy-lookups-data/", None),
    "python": ("https://docs.python.org/3", None),
}

# -- Options for todo extension ----------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/extensions/todo.html#configuration

todo_include_todos = True

# -- Options for autodoc extension -------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/extensions/autodoc.html#configuration

autodoc_default_options = {"exclude-members": ""}  # comma-separated class members to ignore

# Show default kwargs as their names, not values (e.g., show "date=get_date()", instead of "date='21-06-28'")
autodoc_preserve_defaults = True

# -- Options for sphinx-rtd-dark-mode extension ------------------------------
# https://github.com/MrDogeBro/sphinx_rtd_dark_mode

default_dark_mode = False
