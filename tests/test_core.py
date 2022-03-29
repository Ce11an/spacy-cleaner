import numpy as np
import pytest
import spacy

from spacy_cleaner import core
from spacy_cleaner.utils import helpers


@pytest.fixture
def nlp():
    return helpers.load_model("en_core_web_sm")


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
    return core.SpacyCleaner(spacy_model=nlp)


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
        cleaner = core.SpacyCleaner(
            nlp, remove_stopwords=False, extra_stopwords=[extra_stopword]
        )


def test_valid_extra_stopwords(nlp, extra_stopword):
    cleaner = core.SpacyCleaner(
        nlp, remove_stopwords=True, extra_stopwords=[extra_stopword]
    )

    doc = nlp("Cellan is a Welsh name.")
    assert isinstance(nlp.vocab["cellan"], spacy.lexeme.Lexeme)
    assert doc[0].check_flag(spacy.attrs.IS_STOP) is True
