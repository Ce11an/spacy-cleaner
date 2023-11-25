"""Tests for `spacy_cleaner.processing.transformers`."""

import pytest
import spacy

from spacy_cleaner.processing.evaluators import PunctuationEvaluator
from spacy_cleaner.processing.transformers import Transformer


class TestTransformer:
    """Tests for `Transformer`."""

    @pytest.fixture()
    def evaluator(self) -> PunctuationEvaluator:
        """Return a `PunctuationEvaluator`."""
        return PunctuationEvaluator()

    @pytest.fixture()
    def transformer(self, evaluator: PunctuationEvaluator) -> Transformer:
        """Return a `Transformer` with a `PunctuationEvaluator`."""
        return Transformer(evaluator, replace="_IS_PUNCT_")

    def test_transform_replace_success(
        self, model: spacy.Language, transformer: Transformer
    ) -> None:
        """Test that punctuation is replaced."""
        doc = model(".")
        tok = doc[0]
        assert transformer.transform(tok) == "_IS_PUNCT_"

    def test_transform_replace_fail(
        self, model: spacy.Language, transformer: Transformer
    ) -> None:
        """Test that non-punctuation is not replaced."""
        doc = model("London")
        tok = doc[0]
        assert transformer.transform(tok) == tok
