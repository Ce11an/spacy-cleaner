"""Base processing classes."""

from typing import Union

import abc

from spacy.tokens import Token

from spacy_cleaner.base.protocols import Evaluator


class BaseProcessor(abc.ABC):
    """Base processor class.

    Processes a token using the evaluator.

    Attributes:
        evaluator: Evaluates if the token should be processed or not.
    """

    def __init__(self, evaluator: Evaluator) -> None:
        """Initialises class."""
        self.evaluator = evaluator

    @abc.abstractmethod
    def process(self, tok: Token) -> Union[str, Token]:
        """Processes a token using the evaluator.

        Args:
            tok: The token to be evaluated.

        Returns:
            A string or token depending on evaluation.
        """
