"""Module containing functions that remove spaCy tokens from strings."""

from typing import Union

from spacy.tokens import Token

from spacy_cleaner.processing import evaluators, processor


def remove_stopword_token(tok: Token) -> Union[str, Token]:
    """If the token is a stopword, replace it with an empty string.

    Args:
      tok: A spaCy Token.

    Returns:
      A string or a token.
    """
    return processor.Processor(
        evaluators.StopwordsEvaluator(), replace=""
    ).process(tok)
