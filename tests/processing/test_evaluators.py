from spacy_cleaner.processing.evaluators import (
    EmailEvaluator,
    PunctuationEvaluator,
    StopwordsEvaluator,
    URLEvaluator,
)


class TestStopwordsEvaluator:
    def test_evaluate_true(self, model):
        doc = model("and")
        tok = doc[0]
        evaluator = StopwordsEvaluator()
        assert evaluator.evaluate(tok) is True

    def test_evaluate_false(self, model):
        doc = model("London")
        tok = doc[0]
        evaluator = StopwordsEvaluator()
        assert evaluator.evaluate(tok) is False


class TestEmailEvaluator:
    def test_evaluate_true(self, model):
        doc = model("hallcellan@gmail.com")
        tok = doc[0]
        evaluator = EmailEvaluator()
        assert evaluator.evaluate(tok) is True

    def test_evaluate_false(self, model):
        doc = model("London")
        tok = doc[0]
        evaluator = EmailEvaluator()
        assert evaluator.evaluate(tok) is False


class TestPunctuationEvaluator:
    def test_evaluate_true(self, model):
        doc = model(".")
        tok = doc[0]
        evaluator = PunctuationEvaluator()
        assert evaluator.evaluate(tok) is True

    def test_evaluate_false(self, model):
        doc = model("London")
        tok = doc[0]
        evaluator = PunctuationEvaluator()
        assert evaluator.evaluate(tok) is False


class TestURLEvaluator:
    def test_evaluate_true(self, model):
        doc = model("www.google.com")
        tok = doc[0]
        evaluator = URLEvaluator()
        assert evaluator.evaluate(tok) is True

    def test_evaluate_false(self, model):
        doc = model("London")
        tok = doc[0]
        evaluator = URLEvaluator()
        assert evaluator.evaluate(tok) is False
