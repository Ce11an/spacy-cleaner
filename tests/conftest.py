import pytest
import spacy


@pytest.fixture
def texts():
    return [
        "spacy-cleaner is the first package I have made so I am very "
        "excited for others to use it :) IF YoU HAve anY IssUes, please "
        "email: hallcellan@gmail.com - For improvements, make an issue "
        "here: https://github.com/Ce11an/spacy-cleaner/issues.",
        "Text cleaning is about to be a whole lot easier!!",
        "What's your favourite Anime? Demon Slayer is awesome...",
        "Annie is travelling to London at 9 AM",
    ]


@pytest.fixture
def model():
    model = spacy.blank("en")
    model.add_pipe("lemmatizer", config={"mode": "lookup"})
    model.initialize()
    return model
