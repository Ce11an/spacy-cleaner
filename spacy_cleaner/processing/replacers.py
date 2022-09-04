"""Module containing functions that replace spaCy tokens with strings."""

from typing import Union

from spacy.tokens import Token

from spacy_cleaner.processing import evaluators, processor


def replace_punctuation_token(
    tok: Token, replace: str = "_IS_PUNCT_"
) -> Union[str, Token]:
    """If the token is punctuation, replace it with the string `_IS_PUNCT_`.

    Args:
      tok: A spaCy Token.
      replace: The replacement string. Defaults to "_IS_PUNCT_".

    Returns:
      A string or a token.
    """
    return processor.Processor(
        evaluators.PunctuationEvaluator(), replace
    ).process(tok)


def replace_stopword_token(
    tok: Token, replace: str = "_IS_STOP_"
) -> Union[str, Token]:
    """If the token is a stopword, replace it with the string `_IS_STOP_`.

    Args:
      tok: A spaCy Token.
      replace: The replacement string. Defaults to "_IS_STOP_".

    Returns:
      A string or a token.
    """
    return processor.Processor(
        evaluators.StopwordsEvaluator(), replace
    ).process(tok)


def replace_like_email_token(
    tok: Token, replace: str = "_LIKE_EMAIL_"
) -> Union[str, Token]:
    """If the token is like an email, replace it with the string `_LIKE_EMAIL_`.

    Args:
      tok: A spaCy Token.
      replace: The replacement string. Defaults to "_LIKE_EMAIL_".

    Returns:
      A string or a token.
    """
    return processor.Processor(evaluators.EmailEvaluator(), replace).process(
        tok
    )
