from spacy_cleaner.processing import mutate_lemma_token, remove_stopword_token
from spacy_cleaner.processing.helpers import (
    replace_multi_whitespace,
    token_pipe,
)


class TestReplaceMultiWhitespace:
    def test_replace_multi_whitespace(self):
        s = "   this  is a    test!"
        assert replace_multi_whitespace(s) == "this is a test!"


class TestTokenPipe:
    def test_token_pipe(self, model):
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
