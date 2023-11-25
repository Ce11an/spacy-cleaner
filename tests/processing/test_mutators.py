"""Tests for `spacy_cleaner.processing.mutators`."""

import spacy

from spacy_cleaner.processing import mutate_lemma_token


class TestMutateLemmaToken:
    """Tests for `mutate_lemma_token`."""

    def test_mutate_lemma_token_has_lemma(self, model: spacy.Language) -> None:
        """Test that lemma is returned for string."""
        doc = model("swimming")
        tok = doc[0]
        assert mutate_lemma_token(tok) == "swim"

    def test_mutate_lemma_token_does_not_have_lemma(
        self, model: spacy.Language
    ) -> None:
        """Test that original token is returned for token."""
        doc = model("London")
        tok = doc[0]
        assert mutate_lemma_token(tok) == "London"
