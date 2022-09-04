"""Processing helper functions."""

import typing
from typing import Callable, Union

import re

from spacy.tokens import Doc, Token


def replace_multi_whitespace(s: str, replace: str = " ") -> str:
    """Replace multiple whitespace characters with a single space.

    Args:
      s: The string to be replaced.
      replace: The replacement string. Defaults to " "

    Returns:
      A string with all the whitespace replaced with a single space.
    """
    return re.sub(r"\s\s+", replace, s, flags=re.UNICODE)


@typing.no_type_check
def token_pipe(tok: Token, *funcs: Callable[[Token], Union[str, Token]]) -> str:

    """It takes a token, and applies a series of functions to it, until one of the functions returns a string.

    Args:
        tok: the token to be processed

    Returns:
        A string.
    """
    for func in funcs:
        tok = func(tok)
        if isinstance(tok, str):
            return str(tok)
    return str(tok)


def clean_doc(doc: Doc, *pipeline: Callable[[Token], Union[str, Token]]) -> str:
    """Cleans a spaCy document and returns a cleaned string.

    Args:
        doc: spaCy Doc to be cleaned.
        pipeline: Callable functions that process tokens.

    Returns:
        A string of the cleaned text.

    Examples:
        >>> import spacy
        >>> from spacy_cleaner.processing import remove_stopword_token, replace_punctuation_token, mutate_lemma_token

        >>> model = spacy.blank("en")
        >>> model.add_pipe("lemmatizer", config={"mode": "lookup"})
        >>> model.initialize()

        >>> _doc = model("Hello, my name is Cellan! I love to swim!")
        >>> clean_doc(_doc, remove_stopword_token, replace_punctuation_token, mutate_lemma_token)
        >>> 'Hello _IS_PUNCT_ Cellan _IS_PUNCT_ love swim _IS_PUNCT_'
    """
    s = " ".join([token_pipe(tok, *pipeline) for tok in doc])
    return replace_multi_whitespace(s)
