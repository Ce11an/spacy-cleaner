"""Class `TokenTransformer` allows for transformation of `spaCy` tokens."""

from typing import Union

from spacy import tokens

from spacy_cleaner.processing import evaluators


class Transformer:
    """Transforms a token using the evaluator.

    Args:
        evaluator: Evaluates if the token should be processed or not.
        replace: Replaces token based on the token evaluation.

    Example:
        ```python
        from spacy_cleaner.processing.evaluators import StopwordsEvaluator

        transformer = Transformer(StopwordsEvaluator(), replace="")
        transformer.transform(tok)
        ```
    """

    def __init__(self, evaluator: evaluators.Evaluator, replace: str) -> None:
        self.evaluator = evaluator
        self.replace = replace

    def transform(self, tok: tokens.Token) -> Union[str, tokens.Token]:
        """Processes a token using the evaluator.

        Args:
            tok: The token to be evaluated.

        Returns:
            A string or token depending on evaluation.
        """
        return self.replace if self.evaluator.evaluate(tok) else tok
