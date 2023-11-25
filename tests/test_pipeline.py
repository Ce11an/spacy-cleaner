"""Test the `Cleaner` class."""
from typing import List

import spacy

from spacy_cleaner import Cleaner, processing


class TestCleaner:
    """Test the `Cleaner` class."""

    def test_clean(self, model: spacy.Language, texts: List[str]) -> None:
        """Test the `clean` method."""
        cleaner = Cleaner(
            model,
            processing.remove_stopword_token,
            processing.replace_punctuation_token,
            processing.mutate_lemma_token,
        )
        assert cleaner.clean(texts) == [
            "spacy _IS_PUNCT_ clean package excite use _IS_PUNCT_ IssUes "
            "_IS_PUNCT_ email _IS_PUNCT_ hallcellan@gmail.com _IS_PUNCT_ "
            "improvement _IS_PUNCT_ issue _IS_PUNCT_ https://github.com/Ce11an/"
            "spacy-cleaner/issues _IS_PUNCT_",
            "Text clean lot easy _IS_PUNCT_ _IS_PUNCT_",
            "favourite Anime _IS_PUNCT_ Demon Slayer awesome _IS_PUNCT_",
            "Annie travel London 9",
        ]
