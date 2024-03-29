"""Processing helper functions."""

import re
from typing import Callable, Union

from spacy import tokens


def replace_multi_whitespace(s: str, replace: str = " ") -> str:
    """Replace multiple whitespace characters with a single space.

    Args:
      s: The string to be replaced.
      replace: The replacement string.

    Returns:
      A string with all the whitespace replaced with a single space.
    """
    return re.sub(r"\s\s+", replace, s, flags=re.UNICODE).strip()


def token_pipe(
    tok: tokens.Token,
    *processors: Callable[[tokens.Token], Union[str, tokens.Token]],
) -> str:
    """Applies a series of processors to a token until it becomes a string.

    It takes a token, and applies a series of functions to it, until one of
        the functions returns a string.

    Args:
        tok: The token to be transformed,
        *processors: Callable token processors.

    Returns:
        A string of the token after being processed.
    """
    for processor in processors:
        tok = processor(tok)  # type: ignore[assignment]
        if isinstance(tok, str):
            return str(tok)
    return str(tok)


def clean_doc(
    doc: tokens.Doc,
    *processors: Callable[[tokens.Token], Union[str, tokens.Token]],
) -> str:
    """Cleans a spaCy document and returns a cleaned string.

    Args:
        doc: spaCy document to be cleaned.
        *processors: Callable token processors.

    Returns:
        A string of the cleaned text.
    """
    s = " ".join([token_pipe(tok, *processors) for tok in doc])
    return replace_multi_whitespace(s)
