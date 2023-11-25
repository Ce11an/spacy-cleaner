"""Replace `spaCy` tokens.

This module contains functions that assist with replace `spaCy` tokens.

A typical usage example:
    ```python
    import spacy
    from spacy_cleaner import processing

    nlp = spacy.load("en_core_web_md")
    doc = nlp(",")
    tok = doc[0]

    processing.replace_punctuation_token(tok)
    ```
    `,` is replaced with `_IS_PUNCT_`.
"""

from typing import Union

from spacy import tokens

from spacy_cleaner.processing import evaluators, transformers


def replace_stopword_token(
    tok: tokens.Token, replace: str = "_IS_STOP_"
) -> Union[str, tokens.Token]:
    """If the token is a stopword, replace it with the string `_IS_STOP_`.

    Args:
      tok: A `spaCy` token.
      replace: The replacement string.

    Returns:
      The replacement string or the original token.
    """
    return transformers.Transformer(
        evaluators.StopwordsEvaluator(), replace
    ).transform(tok)


def replace_punctuation_token(
    tok: tokens.Token, replace: str = "_IS_PUNCT_"
) -> Union[str, tokens.Token]:
    """If the token is punctuation, replace it with the string `_IS_PUNCT_`.

    Args:
      tok: A `spaCy` token.
      replace: The replacement string.

    Returns:
      The replacement string or the original token.
    """
    return transformers.Transformer(
        evaluators.PunctuationEvaluator(), replace
    ).transform(tok)


def replace_email_token(
    tok: tokens.Token, replace: str = "_LIKE_EMAIL_"
) -> Union[str, tokens.Token]:
    """If the token is like an email, replace it with the string `_LIKE_EMAIL_`.

    Args:
      tok: A `spaCy` token.
      replace: The replacement string.

    Returns:
      The replacement string or the original token.
    """
    return transformers.Transformer(
        evaluators.EmailEvaluator(), replace
    ).transform(tok)


def replace_url_token(
    tok: tokens.Token, replace: str = "_LIKE_URL_"
) -> Union[str, tokens.Token]:
    """If the token is like a URL, replace it with the string `_LIKE_URL_`.

    Args:
      tok: A `spaCy` token.
      replace: The replacement string.

    Returns:
      The replacement string or the original token.
    """
    return transformers.Transformer(
        evaluators.URLEvaluator(), replace
    ).transform(tok)


def replace_number_token(
    tok: tokens.Token, replace: str = "_LIKE_NUM_"
) -> Union[str, tokens.Token]:
    """If the token is like a number, replace it with the string `_LIKE_NUM_`.

    Args:
      tok: A `spaCy` token.
      replace: The replacement string.

    Returns:
      The replacement string or the original token.
    """
    return transformers.Transformer(
        evaluators.NumberEvaluator(), replace
    ).transform(tok)
