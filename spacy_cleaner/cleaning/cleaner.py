"""class `Cleaner` allows for configurable cleaning of text using `spaCy`.

Functionality:
    - Remove numbers.
    - Remove punctuation.
    - Remove part-of-speech tags.
    - Remove stopwords
    - Remove emails.
    - Remove URLs.
    - Lemmatization.

Typical usage example:
    ```python
    texts = ["I won £1000"]
    nlp = spacy.load("en_core_web_sm")
    cleaner = Cleaner(nlp, remove_numbers=True)
    clean_texts = cleaner.clean(texts, disable=["ner"])
    ```
"""

from typing import List, Optional

import warnings

import tqdm
from spacy import Language
from spacy.tokens import Doc, Token

from spacy_cleaner.base.base_cleaner import BaseCleaner
from spacy_cleaner.utils import exceptions


class Cleaner(BaseCleaner):
    """Cleans text using SpaCy!

    Args:
      model: The `spaCy` model to use.
      remove_numbers: Remove numbers from the text.
      remove_punctuation: Remove punctuation from the text.
      remove_pos: A list of POS tags to remove. For example, if you want to
          remove all nouns, you can pass in `['NOUN']`.
      remove_stopwords: Remove stopwords from the text.
      remove_email: Remove email addresses from the text.
      remove_url: Remove URLs from the text.
      lemmatize: If True, lemmatize the text.

    Raises:
        SpacyCleanerMisconfigurationError: When attempting to lemmatize when a
            `lemmatizer` is not in the model pipeline.

    Example:
        ```python
        nlp = spacy.load("en_core_web_sm")

        cleaner = Cleaner(
            spacy_model=nlp,
            lemmatize=True,
            remove_numbers=True,
        )

        raw_texts = [
            "Travelling to London with Cellan took 3 hours",
            "I love to go to the beach and see seagulls",
        ]

        cleaner.clean(raw_texts)
        ```
    """

    def __init__(
        self,
        model: Language,
        remove_numbers: bool = False,
        remove_punctuation: bool = True,
        remove_pos: Optional[List[str]] = None,
        remove_stopwords: bool = True,
        remove_email: bool = True,
        remove_url: bool = True,
        lemmatize: bool = False,
    ) -> None:
        super().__init__(model)

        if remove_pos is not None and "tagger" not in model.pipe_names:
            warnings.warn(
                "A `tagger` is not in your model pipeline. POS tags will not "
                "be removed."
            )

        if lemmatize and "lemmatizer" not in model.pipe_names:
            raise exceptions.SpacyCleanerMisconfigurationError(
                "A `lemmatizer` is not in your model pipeline."
            )

        self.remove_numbers = remove_numbers
        self.remove_punctuation = remove_punctuation
        self.remove_pos = remove_pos
        self.remove_stopwords = remove_stopwords
        self.remove_email = remove_email
        self.remove_url = remove_url
        self.lemmatize = lemmatize

    def clean(self, texts: List[str], **kwargs) -> List[str]:  # type: ignore
        """Cleans each text in texts.

        The method `clean` wraps the `spaCy` `Language` model pipe. When
            cleaning, a progress bar is shown.

        Args:
          texts: List of texts to clean.
          **kwargs: Keyword Arguments for pipe method:
            https://spacy.io/api/language#pipe

        Returns:
          A list of cleaned texts.

        """
        return [
            self._clean_doc(doc)
            for doc in tqdm.tqdm(
                self.model.pipe(texts, **kwargs),
                desc="Cleaning Progress",
                total=len(texts),
            )
        ]

    def _clean_doc(self, doc: Doc) -> str:
        """Cleans a `spaCy` document.

        If the token is allowed, then append the token to the list of tokens.

        Args:
          doc: The document to be cleaned.

        Returns:
          A string of the cleaned document.
        """
        tokens = []
        for tok in doc:
            if not self._allowed_token(tok):
                continue
            if self.lemmatize:
                tokens.append(str(tok.lemma_))
            else:
                tokens.append(str(tok))
        return " ".join(tokens).lower()

    def _allowed_token(self, tok: Token) -> bool:
        """Checks if a token is allowed.

        If the token does not meet the conditions then it is allowed.

        Args:
          tok: A `spaCy` token.

        Returns:
          True if the token is allowed and False if it is not allowed.
        """
        if isinstance(self.remove_pos, List) and tok.pos_ in self.remove_pos:
            return False
        elif self.remove_stopwords and tok.is_stop:
            return False
        elif self.remove_punctuation and tok.is_punct:
            return False
        elif self.remove_numbers and tok.like_num:
            return False
        elif self.remove_email and tok.like_email:
            return False
        elif self.remove_url and tok.like_url:
            return False
        elif tok.text.strip() == "":
            return False
        else:
            return True
