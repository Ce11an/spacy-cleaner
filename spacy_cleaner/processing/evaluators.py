"""Evaluate `spaCy` tokens.

This module contains classes that assist with evaluating `spaCy` tokens.

A typical usage example:
    ```python
    import spacy
    from spacy_cleaner.processing import evaluators

    nlp = spacy.load("en_core_web_md")
    doc = nlp("and")
    tok = doc[0]

    evaluator = evaluators.StopwordsEvaluator()
    evaluator.evaluate(tok)
    ```
    Calling evaluate returns `True` as `and` is a stopword.
"""

import abc

from spacy import tokens


class Evaluator(abc.ABC):
    """Base class for evaluators."""

    @abc.abstractmethod
    def evaluate(self, tok: tokens.Token) -> bool:
        """Evaluates a `spaCy` token.

        Args:
            tok: Token to evaluate.

        Returns:
           Whether the token is evaluated to `True` or `False`.
        """


class StopwordsEvaluator(Evaluator):
    """Evaluates stopwords."""

    def evaluate(self, tok: tokens.Token) -> bool:
        """If the given token is a stopword.

        Args:
            tok: Token to evaluate.

        Returns:
            `True` if the token is a stopword. `False` if not.
        """
        return tok.is_stop


class PunctuationEvaluator(Evaluator):
    """Evaluates emails."""

    def evaluate(self, tok: tokens.Token) -> bool:
        """If the given token is like an email.

        Args:
            tok: Token to evaluate.

        Returns:
            `True` if the token is punctuation. `False` if not.
        """
        return tok.is_punct


class EmailEvaluator(Evaluator):
    """Evaluates emails."""

    def evaluate(self, tok: tokens.Token) -> bool:
        """If the given token is like an email.

        Args:
            tok: Token to evaluate.

        Returns:
            `True` if the token is like an email. `False` if not.
        """
        return tok.like_email


class URLEvaluator(Evaluator):
    """Evaluates URLs."""

    def evaluate(self, tok: tokens.Token) -> bool:
        """If the given token is like a URL.

        Args:
            tok: Token to evaluate.

        Returns:
            `True` if the token is like a URL. `False` if not.
        """
        return tok.like_url


class NumberEvaluator(Evaluator):
    """Evaluates Numbers."""

    def evaluate(self, tok: tokens.Token) -> bool:
        """If the given token is like a number.

        Args:
            tok: Token to evaluate.

        Returns:
            `True` if the token is like a number. `False` if not.
        """
        return tok.like_num
