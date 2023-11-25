"""Tests for `spacy_cleaner.processing.evaluators`."""

import spacy

from spacy_cleaner.processing.evaluators import (
    EmailEvaluator,
    PunctuationEvaluator,
    StopwordsEvaluator,
    URLEvaluator,
)


class TestStopwordsEvaluator:
    """Tests for `StopwordsEvaluator`."""

    def test_evaluate_true(self, model: spacy.Language) -> None:
        """Test that stopwords are evaluated to `True`."""
        doc = model("and")
        tok = doc[0]
        evaluator = StopwordsEvaluator()
        assert evaluator.evaluate(tok) is True

    def test_evaluate_false(self, model: spacy.Language) -> None:
        """Test that non-stopwords are evaluated to `False`."""
        doc = model("London")
        tok = doc[0]
        evaluator = StopwordsEvaluator()
        assert evaluator.evaluate(tok) is False


class TestEmailEvaluator:
    """Tests for `EmailEvaluator`."""

    def test_evaluate_true(self, model: spacy.Language) -> None:
        """Test that emails are evaluated to `True`."""
        doc = model("hallcellan@gmail.com")
        tok = doc[0]
        evaluator = EmailEvaluator()
        assert evaluator.evaluate(tok) is True

    def test_evaluate_false(self, model: spacy.Language) -> None:
        """Test that non-emails are evaluated to `False`."""
        doc = model("London")
        tok = doc[0]
        evaluator = EmailEvaluator()
        assert evaluator.evaluate(tok) is False


class TestPunctuationEvaluator:
    """Tests for `PunctuationEvaluator`."""

    def test_evaluate_true(self, model: spacy.Language) -> None:
        """Test that punctuation is evaluated to `True`."""
        doc = model(".")
        tok = doc[0]
        evaluator = PunctuationEvaluator()
        assert evaluator.evaluate(tok) is True

    def test_evaluate_false(self, model: spacy.Language) -> None:
        """Test that non-punctuation is evaluated to `False`."""
        doc = model("London")
        tok = doc[0]
        evaluator = PunctuationEvaluator()
        assert evaluator.evaluate(tok) is False


class TestURLEvaluator:
    """Tests for `URLEvaluator`."""

    def test_evaluate_true(self, model: spacy.Language) -> None:
        """Test that URLs are evaluated to `True`."""
        doc = model("www.google.com")
        tok = doc[0]
        evaluator = URLEvaluator()
        assert evaluator.evaluate(tok) is True

    def test_evaluate_false(self, model: spacy.Language) -> None:
        """Test that non-URLs are evaluated to `False`."""
        doc = model("London")
        tok = doc[0]
        evaluator = URLEvaluator()
        assert evaluator.evaluate(tok) is False
