import pytest
import spacy

from spacy_cleaner.cleaner import SpacyCleaner
from spacy_cleaner.utils import helpers


def test_not_valid_model_download():
    with pytest.raises(SystemExit) as cm:
        helpers.download_model("not_a_spacy_model")
        assert cm.exception.code == 1


def test_can_load_model():
    assert isinstance(helpers.load_model("en_core_web_sm"), spacy.language.Language)


def test_cannot_load_model():
    with pytest.raises(OSError):
        helpers.load_model("en_core_web_lg")
