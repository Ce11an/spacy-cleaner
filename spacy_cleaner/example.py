from typing import List

from spacy_cleaner import core
from spacy_cleaner.utils import helpers

nlp = helpers.load_model("en_core_web_sm")

cleaner = core.SpacyCleaner(
    spacy_model=nlp,
    lemmatize=True,
    remove_stopwords=True,
    remove_numbers=True,
    extra_stopwords=["cellan", "seagulls"],
)


def run_spacy_clean(spacy_cleaner: core.SpacyCleaner, texts: List[str]) -> List[str]:
    """
    Example of how to use core.SpacyCleaner.

    :param spacy_cleaner: core.SpacyCleaner to clean text with.
    :param texts: List of text to be cleaned.

    :return: List of text that has been cleaned.
    """
    return spacy_cleaner.clean(texts)
