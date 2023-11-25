"""Tests for `spacy_cleaner.processing.removers`."""
import spacy

from spacy_cleaner.processing.removers import (
    remove_email_token,
    remove_number_token,
    remove_punctuation_token,
    remove_stopword_token,
    remove_url_token,
)


class TestRemoveStopwordToken:
    """Tests for `remove_stopword_token`."""

    def test_remove_stopword_token_is_stopword(
        self, model: spacy.Language
    ) -> None:
        """Test that stopwords are removed."""
        doc = model("and")
        tok = doc[0]
        assert remove_stopword_token(tok) == ""

    def test_remove_stopword_token_is_not_stopword(
        self, model: spacy.Language
    ) -> None:
        """Test that non-stopwords are not removed."""
        doc = model(".")
        tok = doc[0]
        assert remove_stopword_token(tok) == tok


class TestRemovePunctuationToken:
    """Tests for `remove_punctuation_token`."""

    def test_remove_punctuation_token_is_punctuation(
        self, model: spacy.Language
    ) -> None:
        """Test that punctuation is removed."""
        doc = model(".")
        tok = doc[0]
        assert remove_punctuation_token(tok) == ""

    def test_remove_punctuation_token_is_not_punctuation(
        self, model: spacy.Language
    ) -> None:
        """Test that non-punctuation is not removed."""
        doc = model("London")
        tok = doc[0]
        assert remove_punctuation_token(tok) == tok


class TestRemoveEmailToken:
    """Tests for `remove_email_token`."""

    def test_remove_email_token_is_email(self, model: spacy.Language) -> None:
        """Test that emails are removed."""
        doc = model("hallcellan@gmail.com")
        tok = doc[0]
        assert remove_email_token(tok) == ""

    def test_remove_email_token_is_not_email(
        self, model: spacy.Language
    ) -> None:
        """Test that non-emails are not removed."""
        doc = model(".")
        tok = doc[0]
        assert remove_email_token(tok) == tok


class TestURLToken:
    """Tests for `remove_url_token`."""

    def test_remove_url_token_is_url(self, model: spacy.Language) -> None:
        """Test that URLs are removed."""
        doc = model("www.google.com")
        tok = doc[0]
        assert remove_url_token(tok) == ""

    def test_remove_url_token_is_not_url(self, model: spacy.Language) -> None:
        """Test that non-URLs are not removed."""
        doc = model(".")
        tok = doc[0]
        assert remove_url_token(tok) == tok


class TestNumberToken:
    """Tests for `remove_number_token`."""

    def test_remove_number_token_is_number(self, model: spacy.Language) -> None:
        """Test that numbers are removed."""
        doc = model("ten")
        tok = doc[0]
        assert remove_number_token(tok) == ""

    def test_remove_number_token_is_not_number(
        self, model: spacy.Language
    ) -> None:
        """Test that non-numbers are not removed."""
        doc = model(".")
        tok = doc[0]
        assert remove_number_token(tok) == tok
