import pytest
import spacy

from spacy_cleaner import Cleaner
from spacy_cleaner.utils import exceptions


class TestCleaner:
    @pytest.fixture
    def doc(self, model, texts):
        return model(texts[0])

    @pytest.fixture
    def cleaner(self, model):
        return Cleaner(model)

    def test_default_clean(self, cleaner, texts):
        clean_texts = cleaner.clean(texts)
        assert clean_texts == [
            "spacy cleaner package excited use issues email improvements issue",
            "text cleaning lot easier",
            "favourite anime demon slayer awesome",
            "annie travelling london 9",
        ]

    def test__clean_doc(self, cleaner, doc):
        text = cleaner._clean_doc(doc)
        assert (
            text == "spacy cleaner package excited use issues email "
            "improvements issue"
        )

    def test__allowed_token(self, cleaner, doc):
        tok = doc[0]
        allowed = cleaner._allowed_token(tok)
        assert allowed is True

    def test_remove_numbers(self, model, texts):
        cleaner = Cleaner(model, remove_numbers=True)
        clean_texts = cleaner.clean(texts)
        assert clean_texts == [
            "spacy cleaner package excited use issues email improvements issue",
            "text cleaning lot easier",
            "favourite anime demon slayer awesome",
            "annie travelling london",
        ]

    def test_lemmatization(self, model, texts):
        cleaner = Cleaner(model, lemmatize=True)
        clean_texts = cleaner.clean(texts)
        assert clean_texts == [
            "spacy clean package excite use issues email improvement issue",
            "text clean lot easy",
            "favourite anime demon slayer awesome",
            "annie travel london 9",
        ]

    def test_warning(self):
        nlp = spacy.blank("en")
        with pytest.warns(
            UserWarning,
            match="A `tagger` is not in your model pipeline. POS tags will not "
            "be removed.",
        ):
            Cleaner(nlp, remove_pos=["NOUN"])

    def test_error(self):
        nlp = spacy.blank("en")
        with pytest.raises(exceptions.SpacyCleanerMisconfigurationError):
            Cleaner(nlp, lemmatize=True)
