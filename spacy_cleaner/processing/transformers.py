"""Class `TokenTransformer` allows for transformation of `spaCy` tokens."""

from typing import Union

from spacy.tokens import Token

from spacy_cleaner.base.protocols import Evaluator


class TokenTransformer:
    """Transforms a token using the evaluator.

    Args:
        evaluator: Evaluates if the token should be processed or not.
        replace: Replaces token based on the token evaluation.

    Example:
        ```python
        from spacy_cleaner.processing.evaluators import StopwordsEvaluator

        transformer = TokenTransformer(StopwordsEvaluator(), replace="")
        transformer.transform(tok)
        ```
    """

    def __init__(self, evaluator: Evaluator, replace: str) -> None:
        self.evaluator = evaluator
        self.replace = replace

    def transform(self, tok: Token) -> Union[str, Token]:
        """Processes a token using the evaluator.

        Args:
            tok: The token to be evaluated.

        Returns:
            A string or token depending on evaluation.
        """
        return self.replace if self.evaluator.evaluate(tok) else tok
