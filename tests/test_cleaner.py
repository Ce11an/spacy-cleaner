import numpy as np
import pytest
import spacy

import spacy_cleaner

spacy.cli.download("en_core_web_sm")


@pytest.fixture
def nlp():
    return spacy.load("en_core_web_sm")


@pytest.fixture
def testing_texts():
    return [
        """spacy-cleaner is the first package I have made so I am very excited for
        others to use it :) IF YoU HAve anY IssUes, please email:
        hallcellan@gmail.com - For improvements, make an issue here:
        https://github.com/Ce11an/spacy-cleaner/issues.""",
        "Text cleaning is about to be a whole lot easier!!",
        "What's your favourite Anime? Demon Slayer is awesome...",
    ]


@pytest.fixture
def extra_stopword():
    return "cellan"


@pytest.fixture
def cleaner(nlp):
    return spacy_cleaner.SpacyCleaner(spacy_model=nlp)


def test_clean(cleaner, testing_texts):
    assert cleaner.clean(testing_texts) == [
        "spacy cleaner package excited use issues email improvements issue",
        "text cleaning lot easier",
        "favourite anime demon slayer awesome",
    ]


def test_vectorise(cleaner, testing_texts):
    vectorised_texts = cleaner.vectorise(testing_texts)
    assert isinstance(vectorised_texts, np.ndarray)
    assert vectorised_texts.shape == (3, 96)


def test_invalid_extra_stopwords(nlp, extra_stopword):
    with pytest.raises(ValueError):
        cleaner = spacy_cleaner.SpacyCleaner(
            nlp, remove_stopwords=False, extra_stopwords=[extra_stopword]
        )


def test_valid_extra_stopwords(nlp, extra_stopword):
    cleaner = spacy_cleaner.SpacyCleaner(
        nlp, remove_stopwords=True, extra_stopwords=[extra_stopword]
    )

    doc = nlp("Cellan is a Welsh name.")
    assert isinstance(nlp.vocab["cellan"], spacy.lexeme.Lexeme)
    assert doc[0].check_flag(spacy.attrs.IS_STOP) is True


def test_remove_pos_remove_numbers_lemmatization_(nlp):
    cleaner = spacy_cleaner.SpacyCleaner(
        nlp,
        remove_numbers=True,
        remove_pos=["VERB", "AUX"],
        lemmatize=True,
    )

    clean_texts = cleaner.clean(["Annie is travelling to London at 9 AM"])
    assert clean_texts == ["annie london"]
