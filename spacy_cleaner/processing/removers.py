"""Module containing functions that remove spaCy tokens from strings."""

from typing import Union

from spacy.tokens import Token

from spacy_cleaner.processing import evaluators, transformers


def remove_stopword_token(tok: Token) -> Union[str, Token]:
    """If the token is a stopword, replace it with an empty string.

    Args:
      tok: A spaCy Token.

    Returns:
      An empty string or the original token.
    """
    return transformers.TokenTransformer(
        evaluators.StopwordsEvaluator(), replace=""
    ).transform(tok)


def remove_punctuation_token(tok: Token) -> Union[str, Token]:
    """If the token is punctuation, replace it with an empty string.

    Args:
      tok: A spaCy Token.

    Returns:
      An empty string or the original token.
    """
    return transformers.TokenTransformer(
        evaluators.PunctuationEvaluator(), replace=""
    ).transform(tok)


def remove_email_token(tok: Token) -> Union[str, Token]:
    """If the token is like an email, replace it with an empty string.

    Args:
      tok: A spaCy Token.

    Returns:
      An empty string or the original token.
    """
    return transformers.TokenTransformer(
        evaluators.EmailEvaluator(), replace=""
    ).transform(tok)
