from spacy_cleaner.processing import (
    replace_email_token,
    replace_punctuation_token,
    replace_stopword_token,
)
from spacy_cleaner.processing.replacers import replace_url_token


class TestReplaceStopwordToken:
    def test_replace_stopword_token_is_stopword(self, model):
        doc = model("and")
        tok = doc[0]
        assert replace_stopword_token(tok) == "_IS_STOP_"

    def test_replace_stopword_token_is_not_stopword(self, model):
        doc = model(".")
        tok = doc[0]
        assert replace_stopword_token(tok) == tok


class TestReplacePunctuationToken:
    def test_replace_punctuation_token_is_punctuation(self, model):
        doc = model(".")
        tok = doc[0]
        assert replace_punctuation_token(tok) == "_IS_PUNCT_"

    def test_replace_punctuation_token_is_not_punctuation(self, model):
        doc = model("London")
        tok = doc[0]
        assert replace_punctuation_token(tok) == tok


class TestReplaceEmailToken:
    def test_replace_email_token_is_email(self, model):
        doc = model("hallcellan@gmail.com")
        tok = doc[0]
        assert replace_email_token(tok) == "_LIKE_EMAIL_"

    def test_replace_email_token_is_not_email(self, model):
        doc = model(".")
        tok = doc[0]
        assert replace_email_token(tok) == tok


class TestReplaceURLToken:
    def test_replace_url_token_is_url(self, model):
        doc = model("www.google.com")
        tok = doc[0]
        assert replace_url_token(tok) == "_LIKE_URL_"

    def test_replace_url_token_is_not_url(self, model):
        doc = model(".")
        tok = doc[0]
        assert replace_url_token(tok) == tok
