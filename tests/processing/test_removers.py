from spacy_cleaner.processing import remove_stopword_token
from spacy_cleaner.processing.removers import (
    remove_email_token,
    remove_punctuation_token,
    remove_url_token,
)


class TestRemoveStopwordToken:
    def test_remove_stopword_token_is_stopword(self, model):
        doc = model("and")
        tok = doc[0]
        assert remove_stopword_token(tok) == ""

    def test_remove_stopword_token_is_not_stopword(self, model):
        doc = model(".")
        tok = doc[0]
        assert remove_stopword_token(tok) == tok


class TestRemovePunctuationToken:
    def test_remove_punctuation_token_is_punctuation(self, model):
        doc = model(".")
        tok = doc[0]
        assert remove_punctuation_token(tok) == ""

    def test_remove_punctuation_token_is_not_punctuation(self, model):
        doc = model("London")
        tok = doc[0]
        assert remove_punctuation_token(tok) == tok


class TestRemoveEmailToken:
    def test_remove_email_token_is_email(self, model):
        doc = model("hallcellan@gmail.com")
        tok = doc[0]
        assert remove_email_token(tok) == ""

    def test_remove_email_token_is_not_email(self, model):
        doc = model(".")
        tok = doc[0]
        assert remove_email_token(tok) == tok


class TestURLToken:
    def test_remove_url_token_is_url(self, model):
        doc = model("www.google.com")
        tok = doc[0]
        assert remove_url_token(tok) == ""

    def test_remove_url_token_is_not_url(self, model):
        doc = model(".")
        tok = doc[0]
        assert remove_url_token(tok) == tok
