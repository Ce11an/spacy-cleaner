from typing import List, Optional

import spacy_cleaner
from spacy_cleaner.utils import helpers


def run_clean(
    texts: List[str],
    remove_numbers: bool = False,
    remove_punctuation: bool = True,
    remove_pos: Optional[List[str]] = None,
    remove_stopwords: bool = True,
    extra_stopwords: Optional[List[str]] = None,
    remove_email: bool = True,
    remove_url: bool = True,
    lemmatize: bool = False,
) -> List[str]:
    """
    Example of how to use spacy_cleaner.SpacyCleaner.

    :param texts: List of text to be cleaned.
    :param remove_numbers: If True, removes numbers from text. Default is False.
    :param remove_punctuation: If True,removes punctuation from text. Default is
        True.
    :param remove_pos: Specify the part-of-speech to remove from text.
    :param remove_stopwords: If True, removes stopwords from text. Default is False.
    :param extra_stopwords: Extra stopwords to be removed. Default is None.
    :param remove_email: If True, removes emails from text. Default is True.
    :param remove_url: If True, removes URLs from text. Default is True.
    :param lemmatize: If True, lemmatizes remaining tokens. Default is False.

    :return: List of text that has been cleaned.

    Examples:
        run_clean(
            texts=["spacy-cleaner makes processing text easy!"],
            remove_numbers=False,
            remove_punctuation=True,
            remove_pos=None,
            remove_stopwords=True,
            extra_stopwords=None,
            remove_email=True,
            remove_url=False,
            lemmatize=False,
        )

    """

    cleaner = spacy_cleaner.SpacyCleaner(
        spacy_model=helpers.load_model("en_core_web_sm"),
        remove_numbers=remove_numbers,
        remove_punctuation=remove_punctuation,
        remove_pos=remove_pos,
        remove_stopwords=remove_stopwords,
        extra_stopwords=extra_stopwords,
        remove_email=remove_email,
        remove_url=remove_url,
        lemmatize=lemmatize,
    )
    return cleaner.clean(texts)


if __name__ == "__main__":
    run_clean(texts=["I love spacy"])
