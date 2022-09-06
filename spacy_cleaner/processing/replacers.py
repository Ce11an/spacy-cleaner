"""Module containing functions that replace spaCy tokens with strings."""

from typing import Union

from spacy.tokens import Token

from spacy_cleaner.processing import evaluators, transformers


def replace_punctuation_token(
    tok: Token, replace: str = "_IS_PUNCT_"
) -> Union[str, Token]:
    """If the token is punctuation, replace it with the string `_IS_PUNCT_`.

    Args:
      tok: A spaCy Token.
      replace: The replacement string. Defaults to "_IS_PUNCT_".

    Returns:
      The replacement string or the original token.
    """
    return transformers.TokenTransformer(
        evaluators.PunctuationEvaluator(), replace
    ).transform(tok)


def replace_stopword_token(
    tok: Token, replace: str = "_IS_STOP_"
) -> Union[str, Token]:
    """If the token is a stopword, replace it with the string `_IS_STOP_`.

    Args:
      tok: A spaCy Token.
      replace: The replacement string. Defaults to "_IS_STOP_".

    Returns:
      The replacement string or the original token.
    """
    return transformers.TokenTransformer(
        evaluators.StopwordsEvaluator(), replace
    ).transform(tok)


def replace_email_token(
    tok: Token, replace: str = "_LIKE_EMAIL_"
) -> Union[str, Token]:
    """If the token is like an email, replace it with the string `_LIKE_EMAIL_`.

    Args:
      tok: A spaCy Token.
      replace: The replacement string. Defaults to "_LIKE_EMAIL_".

    Returns:
      The replacement string or the original token.
    """
    return transformers.TokenTransformer(
        evaluators.EmailEvaluator(), replace
    ).transform(tok)
