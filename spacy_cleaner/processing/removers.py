"""Remove `spaCy` tokens.

This module contains functions that assist with removing `spaCy` tokens.

A typical usage example:
    ```python
    import spacy

    nlp = spacy.load("en_core_web_md")
    doc = nlp("and")
    tok = doc[0]

    remove_stopword_token(tok)
    ```
    `and` is a stopword so an empty string is returned.
"""

from typing import Union

from spacy.tokens import Token

from spacy_cleaner.processing import evaluators, transformers


def remove_stopword_token(tok: Token) -> Union[str, Token]:
    """If the token is a stopword, replace it with an empty string.

    Args:
      tok: A `spaCy` token.

    Returns:
      An empty string or the original token.
    """
    return transformers.TokenTransformer(
        evaluators.StopwordsEvaluator(), replace=""
    ).transform(tok)


def remove_punctuation_token(tok: Token) -> Union[str, Token]:
    """If the token is punctuation, replace it with an empty string.

    Args:
      tok: A `spaCy` token.

    Returns:
      An empty string or the original token.
    """
    return transformers.TokenTransformer(
        evaluators.PunctuationEvaluator(), replace=""
    ).transform(tok)


def remove_email_token(tok: Token) -> Union[str, Token]:
    """If the token is like an email, replace it with an empty string.

    Args:
      tok: A `spaCy` token.

    Returns:
      An empty string or the original token.
    """
    return transformers.TokenTransformer(
        evaluators.EmailEvaluator(), replace=""
    ).transform(tok)


def remove_url_token(tok: Token) -> Union[str, Token]:
    """If the token is like a URL, replace it with an empty string.

    Args:
      tok: A `spaCy` token.

    Returns:
      An empty string or the original token.
    """
    return transformers.TokenTransformer(
        evaluators.URLEvaluator(), replace=""
    ).transform(tok)
