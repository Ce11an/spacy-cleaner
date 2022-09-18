"""Evaluate `spaCy` tokens.

This module contains classes that assist with evaluating `spaCy` tokens.

A typical usage example:
    ```python
    import spacy

    nlp = spacy.load("en_core_web_md")
    doc = nlp("and")
    tok = doc[0]

    evaluator = StopwordsEvaluator()
    evaluator.evaluate(tok)
    ```
    Calling evaluate returns `True` as `and` is a stopword.
"""

from spacy.tokens import Token

from spacy_cleaner.base.protocols import Evaluator


class StopwordsEvaluator(Evaluator):
    """Evaluates stopwords."""

    def evaluate(self, tok: Token) -> bool:
        """If the given token is a stopword.

        Args:
            tok: The token to evaluate.

        Returns:
            `True` if the token is a stopword. `False` if not.
        """
        return tok.is_stop


class PunctuationEvaluator(Evaluator):
    """Evaluates emails."""

    def evaluate(self, tok: Token) -> bool:
        """If the given token is like an email.

        Args:
            tok: The token to evaluate.

        Returns:
            `True` if the token is punctuation. `False` if not.
        """
        return tok.is_punct


class EmailEvaluator(Evaluator):
    """Evaluates emails."""

    def evaluate(self, tok: Token) -> bool:
        """If the given token is like an email.

        Args:
            tok: The token to evaluate.

        Returns:
            `True` if the token is like an email. `False` if not.
        """
        return tok.like_email


class URLEvaluator(Evaluator):
    """Evaluates URLs."""

    def evaluate(self, tok: Token) -> bool:
        """If the given token is like a URL.

        Args:
            tok: The token to evaluate.

        Returns:
            `True` if the token is like a URL. `False` if not.
        """
        return tok.like_url
