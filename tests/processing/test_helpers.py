"""Tests for `spacy_cleaner.processing.helpers`."""

import spacy

from spacy_cleaner.processing import mutate_lemma_token, remove_stopword_token
from spacy_cleaner.processing.helpers import (
    replace_multi_whitespace,
    token_pipe,
)


class TestReplaceMultiWhitespace:
    """Tests for `replace_multi_whitespace`."""

    def test_replace_multi_whitespace(self) -> None:
        """Test multiple whitespaces are replaced with a single whitespace."""
        s = "   this  is a    test!"
        assert replace_multi_whitespace(s) == "this is a test!"


class TestTokenPipe:
    """Tests for `token_pipe`."""

    def test_token_pipe_replace(self, model: spacy.Language) -> None:
        """Test that lemma is returned for string."""
        doc = model("swimming")
        tok = doc[0]
        assert (
            token_pipe(
                tok,
                remove_stopword_token,
                mutate_lemma_token,
            )
            == "swim"
        )

    def test_token_pipe_original(self, model: spacy.Language) -> None:
        """That that original token is returned for token."""
        doc = model("swimming")
        tok = doc[0]
        assert (
            token_pipe(
                tok,
                remove_stopword_token,
            )
            == "swimming"
        )
