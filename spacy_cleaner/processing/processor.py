"""Processor class."""

from typing import Union

from spacy.tokens import Token

from spacy_cleaner.base.base_processor import BaseProcessor
from spacy_cleaner.base.protocols import Evaluator


class Processor(BaseProcessor):
    """Processes a token using the evaluator.

    Attributes:
        evaluator: Evaluates if the token should be processed or not.
        replace: Replaces token based on the token evaluation.
    """

    def __init__(self, evaluator: Evaluator, replace: str) -> None:
        super().__init__(evaluator)
        self.replace = replace

    def process(self, tok: Token) -> Union[str, Token]:
        """Processes a token using the evaluator.

        Args:
            tok: The token to be evaluated.

        Returns:
            A string or token depending on evaluation.
        """
        return self.replace if self.evaluator.evaluate(tok) else tok
