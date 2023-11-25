"""Remove `spaCy` tokens.

This module contains functions that assist with removing `spaCy` tokens.

A typical usage example:
    ```python
    import spacy
    from spacy_cleaner import processing

    nlp = spacy.load("en_core_web_md")
    doc = nlp("and")
    tok = doc[0]

    processing.remove_stopword_token(tok)
    ```
    `and` is a stopword so an empty string is returned.
"""

from typing import Union

from spacy import tokens

from spacy_cleaner.processing import evaluators, transformers


def remove_stopword_token(tok: tokens.Token) -> Union[str, tokens.Token]:
    """If the token is a stopword, replace it with an empty string.

    Args:
      tok: A `spaCy` token.

    Returns:
      An empty string or the original token.
    """
    return transformers.Transformer(
        evaluators.StopwordsEvaluator(), replace=""
    ).transform(tok)


def remove_punctuation_token(tok: tokens.Token) -> Union[str, tokens.Token]:
    """If the token is punctuation, replace it with an empty string.

    Args:
      tok: A `spaCy` token.

    Returns:
      An empty string or the original token.
    """
    return transformers.Transformer(
        evaluators.PunctuationEvaluator(), replace=""
    ).transform(tok)


def remove_email_token(tok: tokens.Token) -> Union[str, tokens.Token]:
    """If the token is like an email, replace it with an empty string.

    Args:
      tok: A `spaCy` token.

    Returns:
      An empty string or the original token.
    """
    return transformers.Transformer(
        evaluators.EmailEvaluator(), replace=""
    ).transform(tok)


def remove_url_token(tok: tokens.Token) -> Union[str, tokens.Token]:
    """If the token is like a URL, replace it with an empty string.

    Args:
      tok: A `spaCy` token.

    Returns:
      An empty string or the original token.
    """
    return transformers.Transformer(
        evaluators.URLEvaluator(), replace=""
    ).transform(tok)


def remove_number_token(tok: tokens.Token) -> Union[str, tokens.Token]:
    """If the token is like a number, replace it with an empty string.

    Args:
      tok: A `spaCy` token.

    Returns:
      An empty string or the original token.
    """
    return transformers.Transformer(
        evaluators.NumberEvaluator(), replace=""
    ).transform(tok)
