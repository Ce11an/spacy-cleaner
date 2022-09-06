import pytest

from spacy_cleaner.processing.evaluators import PunctuationEvaluator
from spacy_cleaner.processing.transformers import TokenTransformer


class TestTokenTransformer:
    @pytest.fixture
    def evaluator(self):
        return PunctuationEvaluator()

    @pytest.fixture
    def transformer(self, evaluator):
        return TokenTransformer(evaluator, replace="_IS_PUNCT_")

    def test_transform_replace_success(self, model, transformer):
        doc = model(".")
        tok = doc[0]
        assert transformer.transform(tok) == "_IS_PUNCT_"

    def test_transform_replace_fail(self, model, transformer):
        doc = model("London")
        tok = doc[0]
        assert transformer.transform(tok) == tok
