"""Tests for `spacy_cleaner.processing.replacers`."""

import spacy

from spacy_cleaner.processing import (
    replace_email_token,
    replace_punctuation_token,
    replace_stopword_token,
)
from spacy_cleaner.processing.replacers import (
    replace_number_token,
    replace_url_token,
)


class TestReplaceStopwordToken:
    """Tests for `replace_stopword_token`."""

    def test_replace_stopword_token_is_stopword(
        self, model: spacy.Language
    ) -> None:
        """Test that stopwords are replaced."""
        doc = model("and")
        tok = doc[0]
        assert replace_stopword_token(tok) == "_IS_STOP_"

    def test_replace_stopword_token_is_not_stopword(
        self, model: spacy.Language
    ) -> None:
        """Test that non-stopwords are not replaced."""
        doc = model(".")
        tok = doc[0]
        assert replace_stopword_token(tok) == tok


class TestReplacePunctuationToken:
    """Tests for `replace_punctuation_token`."""

    def test_replace_punctuation_token_is_punctuation(
        self, model: spacy.Language
    ) -> None:
        """Test that punctuation is replaced."""
        doc = model(".")
        tok = doc[0]
        assert replace_punctuation_token(tok) == "_IS_PUNCT_"

    def test_replace_punctuation_token_is_not_punctuation(
        self, model: spacy.Language
    ) -> None:
        """Test that non-punctuation is not replaced."""
        doc = model("London")
        tok = doc[0]
        assert replace_punctuation_token(tok) == tok


class TestReplaceEmailToken:
    """Tests for `replace_email_token`."""

    def test_replace_email_token_is_email(self, model: spacy.Language) -> None:
        """Test that emails are replaced."""
        doc = model("hallcellan@gmail.com")
        tok = doc[0]
        assert replace_email_token(tok) == "_LIKE_EMAIL_"

    def test_replace_email_token_is_not_email(
        self, model: spacy.Language
    ) -> None:
        """Test that non-emails are not replaced."""
        doc = model(".")
        tok = doc[0]
        assert replace_email_token(tok) == tok


class TestReplaceURLToken:
    """Tests for `replace_url_token`."""

    def test_replace_url_token_is_url(self, model: spacy.Language) -> None:
        """Test that URLs are replaced."""
        doc = model("www.google.com")
        tok = doc[0]
        assert replace_url_token(tok) == "_LIKE_URL_"

    def test_replace_url_token_is_not_url(self, model: spacy.Language) -> None:
        """Test that non-URLs are not replaced."""
        doc = model(".")
        tok = doc[0]
        assert replace_url_token(tok) == tok


class TestReplaceNumberToken:
    """Tests for `replace_number_token`."""

    def test_replace_number_token_is_number(
        self, model: spacy.Language
    ) -> None:
        """Test that numbers are replaced."""
        doc = model("ten")
        tok = doc[0]
        assert replace_number_token(tok) == "_LIKE_NUM_"

    def test_replace_url_token_is_not_url(self, model: spacy.Language) -> None:
        """Test that non-numbers are not replaced."""
        doc = model(".")
        tok = doc[0]
        assert replace_number_token(tok) == tok
