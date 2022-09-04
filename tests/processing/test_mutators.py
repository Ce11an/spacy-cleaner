from spacy_cleaner.processing import mutate_lemma_token


class TestMutateLemmaToken:
    def test_mutate_lemma_token_has_lemma(self, model):
        doc = model("swimming")
        tok = doc[0]
        assert mutate_lemma_token(tok) == "swim"

    def test_mutate_lemma_token_does_not_have_lemma(self, model):
        doc = model("London")
        tok = doc[0]
        assert mutate_lemma_token(tok) == "London"
