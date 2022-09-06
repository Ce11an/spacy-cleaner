"""Protocols."""

from typing import Protocol

from spacy.tokens import Token


class Evaluator(Protocol):
    """A protocol with an `evaluate` method."""

    def evaluate(self, tok: Token) -> bool:
        """Evaluates a spaCy token.

        Args:
            tok: spaCy token.

        Returns:
            bool.
        """
