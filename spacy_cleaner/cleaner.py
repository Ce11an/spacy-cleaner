from typing import List, Optional

import numpy as np
import spacy
from tqdm import tqdm


class SpacyCleaner:
    """
    Clean text data using spaCy.

    Load a spaCy model of your choosing and have the ability to do the following when
    cleaning text:

    - remove numbers
    - remove punctuation
    - remove specified part of speech tags
    - remove stopwords
    - add extra stopwords
    - remove emails
    - remove urls
    - lemmatize strings
    - vectorize strings

    Examples:

        helpers.download_model("en_core_web_sm")
        nlp = helpers.load_model("en_core_web_sm")

        cleaner = SpacyCleaner(
            spacy_model=nlp,
            lemmatize=True,
            remove_stopwords=True,
            remove_numbers=True,
            extra_stopwords=["cellan", "seagulls"],
        )

        raw_texts = [
            "Travelling to London with Cellan took 3 hours
            "I love to go to the beach and see seagulls",
        ]

        clean_texts = cleaner.clean_text(raw_texts)
        vectors = cleaner.vectorize(clean_texts)

        print(clean_texts)
        ['travel london take hour', 'love beach']
    """

    def __init__(
        self,
        spacy_model: spacy.language.Language,
        remove_numbers: bool = False,
        remove_punctuation: bool = True,
        remove_pos: Optional[List[str]] = None,
        remove_stopwords: bool = True,
        extra_stopwords: Optional[List[str]] = None,
        remove_email: bool = True,
        remove_url: bool = True,
        lemmatize: bool = False,
    ) -> None:
        """
        :param spacy_model: Specify what spaCy model to use to clean text. If None,
            `en_core_web_sm` will be loaded.
        :param remove_numbers: If True, removes numbers from text. Default is False.
        :param remove_punctuation: If True,removes punctuation from text. Default is
            True.
        :param remove_pos: Specify the part-of-speech to remove from text.
        :param remove_stopwords: If True, removes stopwords from text. Default is False.
        :param extra_stopwords: Extra stopwords to be removed. Default is None.
        :param remove_email: If True, removes emails from text. Default is True.
        :param remove_url: If True, removes URLs from text. Default is True.
        :param lemmatize: If True, lemmatizes remaining tokens. Default is False.

        :raises OSError: If the spaCy model is not installed.
        :raises ValueError: If remove_stopwords=False and extra_stopwords is not None.

        """
        self.spacy_model = spacy_model
        self.remove_numbers = remove_numbers
        self.remove_punctuation = remove_punctuation
        self.remove_pos = remove_pos
        self.remove_stopwords = remove_stopwords
        self.extra_stopwords = extra_stopwords
        self.remove_email = remove_email
        self.remove_url = remove_url
        self.lemmatize = lemmatize

        if not remove_stopwords and (extra_stopwords is not None):
            raise ValueError(
                "Please set remove_stopwords=True to remove extra stopwords"
            )
        elif remove_stopwords and (extra_stopwords is not None):

            new_stopwords = spacy.lang.en.stop_words.STOP_WORDS.copy()
            new_stopwords.update({*self.extra_stopwords})

            self.spacy_model.vocab.add_flag(
                lambda s: s.lower() in new_stopwords, spacy.attrs.IS_STOP
            )

    def clean(self, texts: List[str]) -> List[str]:
        """
        Run a spaCy pipeline to remove unwanted tokens from texts.

        :param texts: List texts to be cleaned.

        :return: List of cleaned texts.
        """
        return [
            self._clean_pipe(doc)
            for doc in tqdm(
                self.spacy_model.pipe(texts),
                desc="Cleaning Progress",
                total=len(texts),
            )
        ]

    def vectorise(self, texts: List[str]) -> np.ndarray:
        """
        Converts texts to vectors.

        :param texts: List of texts to be vectorised.

        :return: NumPy array of vectorised texts. Shape depends on size of spaCy model.
        """
        return np.concatenate(
            [
                doc.vector.reshape(1, -1)
                for doc in tqdm(
                    self.spacy_model.pipe(
                        texts, disable=["tagger, lemmatizer, textcat"]
                    ),
                    desc="Vectorizing Progress",
                    total=len(texts),
                )
            ]
        )

    def _clean_pipe(self, doc: spacy.tokens.Doc) -> str:
        """
        Cleans a spaCy document.

        :param  spaCy document.

        :return: Cleaned text.
        """
        tokens = []

        for tok in doc:

            if self.remove_pos and (tok in self.remove_pos) and tok.pos_:
                continue

            if self.remove_stopwords and tok.is_stop:
                continue

            if self.remove_punctuation and tok.is_punct:
                continue

            if self.remove_numbers and tok.like_num:
                continue

            if self.remove_email and tok.like_email:
                continue

            if self.remove_url and tok.like_url:
                continue

            if tok.text.strip() == "":
                continue

            if self.lemmatize:
                tokens.append(str(tok.lemma_))
            else:
                tokens.append(str(tok))

        return " ".join(tokens).lower()
