"""SpaCy token evaluators."""

from spacy.tokens import Token

from spacy_cleaner.base.protocols import Evaluator


class StopwordsEvaluator(Evaluator):
    """Evaluates stopwords."""

    def evaluate(self, tok: Token) -> bool:
        """If the given token is a stopword.

        Args:
            tok: The token to evaluate.

        Returns:
            True if the token is a stopword. False if not.
        """
        return tok.is_stop


class EmailEvaluator(Evaluator):
    """Evaluates emails."""

    def evaluate(self, tok: Token) -> bool:
        """If the given token is like an email.

        Args:
            tok: The token to evaluate.

        Returns:
            True if the token is a stopword. False if not.
        """
        return tok.like_email


class PunctuationEvaluator(Evaluator):
    """Evaluates emails."""

    def evaluate(self, tok: Token) -> bool:
        """If the given token is like an email.

        Args:
            tok: The token to evaluate.

        Returns:
            True if the token is a stopword. False if not.
        """
        return tok.is_punct
